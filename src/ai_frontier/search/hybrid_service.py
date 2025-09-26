"""
하이브리드 검색 서비스 - BM25와 벡터 검색을 결합
"""
import logging
from typing import List, Dict, Optional, Tuple, Any
from datetime import date
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from .rag_service import RAGSearchService
from .bm25_service import BM25SearchService


class HybridSearchService:
    """BM25 키워드 검색과 벡터 검색을 결합한 하이브리드 검색 서비스"""

    def __init__(self,
                 vector_db_path: str = "data/embeddings",
                 embedding_model: str = "text-embedding-3-small"):
        """하이브리드 검색 서비스 초기화

        Args:
            vector_db_path: 벡터 데이터베이스 경로
            embedding_model: OpenAI 임베딩 모델명
        """
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # 개별 검색 서비스 초기화
        self.rag_service = RAGSearchService(vector_db_path, embedding_model)
        self.bm25_service = BM25SearchService(vector_db_path.replace("/embeddings", ""))

        # BM25 인덱스 준비
        self.bm25_service.rebuild_index_if_needed()

        self.logger.info("Hybrid search service initialized")

    def hybrid_search(self,
                     query: str,
                     keyword_weight: float = 0.3,
                     vector_weight: float = 0.7,
                     top_k: int = 10,
                     min_similarity: float = 0.3,
                     categories: Optional[List[str]] = None,
                     start_date: Optional[date] = None,
                     end_date: Optional[date] = None,
                     page: int = 1,
                     page_size: int = 10) -> Dict[str, Any]:
        """하이브리드 검색 수행

        Args:
            query: 검색 쿼리
            keyword_weight: BM25 키워드 검색 가중치 (0.0-1.0)
            vector_weight: 벡터 검색 가중치 (0.0-1.0)
            top_k: 최대 결과 수
            min_similarity: 최소 유사도 임계값
            categories: 카테고리 필터
            start_date: 시작 날짜 필터
            end_date: 종료 날짜 필터
            page: 페이지 번호
            page_size: 페이지 크기

        Returns:
            하이브리드 검색 결과
        """
        try:
            # 가중치 정규화 (합이 1이 되도록)
            total_weight = keyword_weight + vector_weight
            if total_weight > 0:
                keyword_weight = keyword_weight / total_weight
                vector_weight = vector_weight / total_weight
            else:
                keyword_weight = 0.3
                vector_weight = 0.7

            self.logger.info(f"Hybrid search: '{query}' (keyword: {keyword_weight:.2f}, vector: {vector_weight:.2f})")

            # 1. BM25 키워드 검색
            bm25_results = []
            extracted_keywords = []
            if keyword_weight > 0:
                bm25_raw, extracted_keywords = self.bm25_service.search(query, top_k=top_k * 3)
                bm25_results = [(paper, score) for paper, score in bm25_raw]

            # 2. 벡터 검색
            vector_results = []
            if vector_weight > 0:
                vector_response = self.rag_service.search_papers(
                    query=query,
                    top_k=top_k * 3,
                    min_similarity=0.0,  # 낮은 임계값으로 더 많은 결과 수집
                    categories=categories,
                    start_date=start_date,
                    end_date=end_date,
                    page=1,
                    page_size=top_k * 3
                )

                # 벡터 검색 결과를 (paper_dict, score) 형태로 변환
                for result in vector_response.get('results', []):
                    vector_results.append((result, result['similarity_score']))

            # 3. 점수 정규화 및 결합
            combined_results = self._combine_and_normalize_scores(
                bm25_results, vector_results, keyword_weight, vector_weight
            )

            # 4. 필터링 적용 (벡터 검색에서 이미 적용되지 않은 BM25 결과에 대해)
            if bm25_results and (categories or start_date or end_date):
                combined_results = self._apply_filters_to_combined(
                    combined_results, categories, start_date, end_date
                )

            # 5. 최소 유사도 필터링
            filtered_results = [
                (paper, score) for paper, score in combined_results
                if score >= min_similarity
            ]

            # 6. 페이지네이션
            total_results = len(filtered_results)
            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            paginated_results = filtered_results[start_idx:end_idx]

            # 7. 결과 포맷팅
            formatted_results = []
            for paper, score in paginated_results:
                # 기본값들을 설정
                arxiv_id = ''
                timestamp = ''
                authors = []

                # BM25 결과와 벡터 결과의 형태를 통일
                if isinstance(paper, dict):
                    # 이미 포맷된 벡터 검색 결과인 경우
                    arxiv_id = paper.get('arxiv_id', '')
                    timestamp = paper.get('timestamp', '')
                    authors = self._ensure_list(paper.get('authors', []))

                    formatted_paper = paper.copy()
                    formatted_paper['hybrid_score'] = round(score, 4)

                    # 누락된 필드들 보완
                    if 'timestamp' not in formatted_paper or not formatted_paper['timestamp']:
                        formatted_paper['timestamp'] = timestamp

                    # authors 필드 강제 리스트 변환
                    formatted_paper['authors'] = self._ensure_list(formatted_paper.get('authors', []))

                    if 'pdf_url' not in formatted_paper:
                        formatted_paper['pdf_url'] = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

                else:
                    # BM25 결과를 포맷팅
                    arxiv_id = paper.get('arxiv_id', '')
                    timestamp = paper.get('timestamp', '')
                    if not timestamp:
                        from datetime import datetime
                        timestamp = datetime.now().isoformat()

                    formatted_paper = {
                        "arxiv_id": arxiv_id,
                        "title": paper.get('title', ''),
                        "abstract": paper.get('abstract', ''),
                        "summary": paper.get('summary', ''),
                        "key_points": paper.get('key_points', []),
                        "hybrid_score": round(score, 4),
                        "timestamp": timestamp,
                        "metadata": paper.get('metadata', {}),
                        "category": paper.get('category', paper.get('metadata', {}).get('category', 'unknown')),
                        "published_date": paper.get('published_date', paper.get('metadata', {}).get('published_date')),
                        "authors": self._ensure_list(paper.get('authors', paper.get('metadata', {}).get('authors', []))),
                        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                    }

                formatted_results.append(formatted_paper)

            # 8. 응답 생성
            response = {
                "query": query,
                "search_type": "hybrid",
                "weights": {
                    "keyword_weight": round(keyword_weight, 2),
                    "vector_weight": round(vector_weight, 2)
                },
                "total_results": total_results,
                "page": page,
                "page_size": page_size,
                "total_pages": (total_results + page_size - 1) // page_size,
                "min_similarity": min_similarity,
                "applied_filters": {
                    "categories": categories,
                    "start_date": start_date.isoformat() if start_date else None,
                    "end_date": end_date.isoformat() if end_date else None
                },
                "results": formatted_results,
                "search_stats": {
                    "bm25_results_count": len(bm25_results),
                    "vector_results_count": len(vector_results),
                    "combined_results_count": len(combined_results),
                    "filtered_results_count": total_results,
                    "extracted_keywords": extracted_keywords
                }
            }

            self.logger.info(f"Hybrid search completed: {total_results} results (BM25: {len(bm25_results)}, Vector: {len(vector_results)})")
            return response

        except Exception as e:
            self.logger.error(f"Hybrid search failed: {e}")
            return {
                "query": query,
                "search_type": "hybrid",
                "total_results": 0,
                "page": page,
                "page_size": page_size,
                "total_pages": 0,
                "results": [],
                "error": str(e)
            }

    def _combine_and_normalize_scores(self,
                                    bm25_results: List[Tuple[Dict, float]],
                                    vector_results: List[Tuple[Dict, float]],
                                    keyword_weight: float,
                                    vector_weight: float) -> List[Tuple[Dict, float]]:
        """BM25와 벡터 검색 점수를 정규화하고 결합"""

        # 점수 정규화를 위한 스케일러
        scaler = MinMaxScaler()

        # BM25 점수 정규화
        bm25_scores = []
        bm25_papers_dict = {}
        if bm25_results:
            scores = np.array([score for _, score in bm25_results]).reshape(-1, 1)
            if len(scores) > 1:
                normalized_scores = scaler.fit_transform(scores).flatten()
            else:
                normalized_scores = [1.0] if scores[0][0] > 0 else [0.0]

            for i, (paper, _) in enumerate(bm25_results):
                arxiv_id = paper.get('arxiv_id', '')
                normalized_score = normalized_scores[i]
                bm25_scores.append((paper, normalized_score))
                bm25_papers_dict[arxiv_id] = (paper, normalized_score)

        # 벡터 점수 정규화 (이미 0-1 범위이지만 동일한 방식으로 처리)
        vector_scores = []
        vector_papers_dict = {}
        if vector_results:
            scores = np.array([score for _, score in vector_results]).reshape(-1, 1)
            if len(scores) > 1:
                normalized_scores = scaler.fit_transform(scores).flatten()
            else:
                normalized_scores = [score for _, score in vector_results]

            for i, (paper, _) in enumerate(vector_results):
                arxiv_id = paper.get('arxiv_id', '')
                normalized_score = normalized_scores[i]
                vector_scores.append((paper, normalized_score))
                vector_papers_dict[arxiv_id] = (paper, normalized_score)

        # 논문별로 점수 결합
        combined_papers = {}

        # BM25 결과 처리
        for paper, norm_score in bm25_scores:
            arxiv_id = paper.get('arxiv_id', '')
            combined_score = norm_score * keyword_weight
            combined_papers[arxiv_id] = (paper, combined_score, norm_score, 0.0)

        # 벡터 결과 처리 및 기존 BM25 결과와 결합
        for paper, norm_score in vector_scores:
            arxiv_id = paper.get('arxiv_id', '')
            vector_contribution = norm_score * vector_weight

            if arxiv_id in combined_papers:
                # 이미 BM25에서 찾은 논문 - 점수 합산
                existing_paper, existing_score, bm25_score, _ = combined_papers[arxiv_id]
                new_combined_score = existing_score + vector_contribution
                # 더 완전한 정보를 가진 것을 사용 (보통 벡터 검색 결과가 더 완전함)
                better_paper = paper if len(str(paper)) > len(str(existing_paper)) else existing_paper
                combined_papers[arxiv_id] = (better_paper, new_combined_score, bm25_score, norm_score)
            else:
                # 벡터 검색에서만 찾은 논문
                combined_papers[arxiv_id] = (paper, vector_contribution, 0.0, norm_score)

        # 점수순으로 정렬하여 반환
        combined_results = [
            (paper, combined_score)
            for paper, combined_score, _, _ in combined_papers.values()
        ]
        combined_results.sort(key=lambda x: x[1], reverse=True)

        return combined_results

    def _apply_filters_to_combined(self,
                                 results: List[Tuple[Dict, float]],
                                 categories: Optional[List[str]] = None,
                                 start_date: Optional[date] = None,
                                 end_date: Optional[date] = None) -> List[Tuple[Dict, float]]:
        """결합된 결과에 필터 적용"""
        if not categories and not start_date and not end_date:
            return results

        filtered_results = []
        for paper, score in results:
            # 카테고리 필터
            if categories:
                paper_category = paper.get('category', '') or paper.get('metadata', {}).get('category', '')
                if not any(cat.lower() in paper_category.lower() for cat in categories):
                    continue

            # 날짜 필터
            if start_date or end_date:
                paper_date_str = paper.get('published_date') or paper.get('metadata', {}).get('published_date')
                if paper_date_str:
                    try:
                        from datetime import datetime
                        paper_date = datetime.fromisoformat(paper_date_str.replace('Z', '+00:00')).date()

                        if start_date and paper_date < start_date:
                            continue
                        if end_date and paper_date > end_date:
                            continue
                    except (ValueError, TypeError):
                        if start_date or end_date:
                            continue

            filtered_results.append((paper, score))

        return filtered_results

    def get_search_stats(self) -> Dict[str, Any]:
        """검색 서비스 통계 정보 반환"""
        try:
            rag_stats = self.rag_service.get_database_stats()
            bm25_stats = self.bm25_service.get_stats()

            return {
                "service_type": "hybrid",
                "vector_search": {
                    "status": "available",
                    "total_papers": rag_stats.get("total_papers", 0),
                    "embedding_dimension": rag_stats.get("embedding_dimension", 0),
                    "categories": rag_stats.get("categories", {}),
                    "date_range": rag_stats.get("date_range", {})
                },
                "keyword_search": bm25_stats,
                "capabilities": [
                    "semantic_search",
                    "keyword_search",
                    "hybrid_scoring",
                    "weight_adjustment",
                    "category_filtering",
                    "date_filtering"
                ]
            }
        except Exception as e:
            self.logger.error(f"Failed to get search stats: {e}")
            return {
                "service_type": "hybrid",
                "status": "error",
                "error": str(e)
            }

    def _ensure_list(self, value):
        """값이 리스트인지 확인하고, 문자열인 경우 리스트로 변환"""
        if isinstance(value, list):
            return value
        elif isinstance(value, str):
            if value == "":
                return []
            return [item.strip() for item in value.split(",") if item.strip()]
        else:
            return []