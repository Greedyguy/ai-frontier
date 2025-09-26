"""
BM25 키워드 검색 서비스
"""
import pickle
from pathlib import Path
from typing import List, Dict, Any, Tuple
import logging
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

logger = logging.getLogger(__name__)


class BM25SearchService:
    """BM25 알고리즘을 이용한 키워드 검색 서비스"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.embeddings_dir = self.data_dir / "embeddings"
        self.bm25_index_path = self.embeddings_dir / "bm25_index.pkl"
        self.papers_metadata_path = self.embeddings_dir / "metadata.pkl"

        self.bm25_index = None
        self.papers_metadata = []
        self.tokenized_corpus = []

        # 불용어 설정 (영어 + 일반적인 논문 용어)
        self.stop_words = set(ENGLISH_STOP_WORDS) | {
            'paper', 'study', 'research', 'method', 'approach', 'algorithm',
            'model', 'system', 'analysis', 'based', 'using', 'propose',
            'show', 'present', 'novel', 'new', 'framework', 'technique'
        }

    def preprocess_text(self, text: str) -> List[str]:
        """텍스트 전처리 및 토큰화"""
        if not text:
            return []

        # 소문자 변환 및 특수문자 제거
        text = re.sub(r'[^\w\s]', ' ', text.lower())

        # 토큰화
        tokens = text.split()

        # 불용어 제거 및 최소 길이 필터링
        tokens = [token for token in tokens
                 if token not in self.stop_words and len(token) > 2]

        return tokens

    def build_index(self, papers_metadata: List[Dict[str, Any]]) -> None:
        """BM25 인덱스 구축"""
        logger.info(f"Building BM25 index for {len(papers_metadata)} papers")

        self.papers_metadata = papers_metadata
        self.tokenized_corpus = []

        for paper in papers_metadata:
            # 제목과 초록을 결합하여 검색 대상 텍스트 생성
            title = paper.get('title', '')
            abstract = paper.get('abstract', '')
            categories = ' '.join(paper.get('categories', []))

            # 텍스트 결합 (제목에 더 높은 가중치 부여)
            combined_text = f"{title} {title} {abstract} {categories}"

            tokens = self.preprocess_text(combined_text)
            self.tokenized_corpus.append(tokens)

        # BM25 인덱스 생성
        self.bm25_index = BM25Okapi(self.tokenized_corpus)

        # 인덱스 저장
        self.save_index()

        logger.info("BM25 index built and saved successfully")

    def save_index(self) -> None:
        """BM25 인덱스를 파일에 저장"""
        self.embeddings_dir.mkdir(parents=True, exist_ok=True)

        index_data = {
            'bm25_index': self.bm25_index,
            'tokenized_corpus': self.tokenized_corpus,
            'papers_metadata': self.papers_metadata
        }

        with open(self.bm25_index_path, 'wb') as f:
            pickle.dump(index_data, f)

    def load_index(self) -> bool:
        """저장된 BM25 인덱스 로드"""
        if not self.bm25_index_path.exists():
            logger.warning("BM25 index file not found")
            return False

        try:
            with open(self.bm25_index_path, 'rb') as f:
                index_data = pickle.load(f)

            self.bm25_index = index_data['bm25_index']
            self.tokenized_corpus = index_data['tokenized_corpus']
            self.papers_metadata = index_data['papers_metadata']

            logger.info(f"BM25 index loaded with {len(self.papers_metadata)} papers")
            return True

        except Exception as e:
            logger.error(f"Failed to load BM25 index: {e}")
            return False

    def search(self, query: str, top_k: int = 100) -> Tuple[List[Tuple[Dict[str, Any], float]], List[str]]:
        """BM25 검색 수행"""
        if not self.bm25_index:
            if not self.load_index():
                logger.error("BM25 index not available")
                return [], []

        # 쿼리 전처리
        query_tokens = self.preprocess_text(query)
        if not query_tokens:
            return [], []

        # BM25 점수 계산
        scores = self.bm25_index.get_scores(query_tokens)

        # 점수와 논문 메타데이터 결합
        paper_scores = []
        for i, score in enumerate(scores):
            if score > 0:  # 점수가 0보다 큰 경우만 포함
                paper_scores.append((self.papers_metadata[i], float(score)))

        # 점수순으로 정렬
        paper_scores.sort(key=lambda x: x[1], reverse=True)

        # 상위 k개 반환 + 사용된 키워드들
        return paper_scores[:top_k], query_tokens

    def get_stats(self) -> Dict[str, Any]:
        """BM25 인덱스 통계 정보 반환"""
        if not self.bm25_index:
            if not self.load_index():
                return {"status": "index_not_available"}

        return {
            "status": "available",
            "total_papers": len(self.papers_metadata),
            "corpus_size": len(self.tokenized_corpus),
            "average_doc_length": sum(len(doc) for doc in self.tokenized_corpus) / len(self.tokenized_corpus) if self.tokenized_corpus else 0,
            "index_file_exists": self.bm25_index_path.exists()
        }

    def rebuild_index_if_needed(self) -> bool:
        """필요시 BM25 인덱스 재구축"""
        # 메타데이터 파일이 BM25 인덱스보다 최신인 경우 재구축
        if (self.papers_metadata_path.exists() and
            (not self.bm25_index_path.exists() or
             self.papers_metadata_path.stat().st_mtime > self.bm25_index_path.stat().st_mtime)):

            try:
                with open(self.papers_metadata_path, 'rb') as f:
                    raw_metadata = pickle.load(f)

                # 메타데이터 구조 변환: PaperEmbedding 객체를 딕셔너리로 변환
                papers_metadata = []
                if isinstance(raw_metadata, dict) and 'metadata' in raw_metadata:
                    for paper_embedding in raw_metadata['metadata'].values():
                        paper_dict = {
                            'arxiv_id': paper_embedding.arxiv_id,
                            'title': paper_embedding.title,
                            'abstract': paper_embedding.abstract,
                            'summary': paper_embedding.summary,
                            'key_points': paper_embedding.key_points,
                            'categories': paper_embedding.metadata.get('category', '').split() if paper_embedding.metadata else [],
                            'category': paper_embedding.metadata.get('category', '') if paper_embedding.metadata else '',
                            'published_date': paper_embedding.metadata.get('published', '') if paper_embedding.metadata else '',
                            'authors': paper_embedding.metadata.get('authors', '') if paper_embedding.metadata else '',
                            'metadata': paper_embedding.metadata or {}
                        }
                        papers_metadata.append(paper_dict)
                elif isinstance(raw_metadata, list):
                    # 이미 리스트 형태인 경우
                    papers_metadata = raw_metadata
                else:
                    logger.warning(f"Unexpected metadata format: {type(raw_metadata)}")
                    return False

                if papers_metadata:
                    self.build_index(papers_metadata)
                    return True
                else:
                    logger.warning("No papers found in metadata")
                    return False

            except Exception as e:
                logger.error(f"Failed to rebuild BM25 index: {e}")
                import traceback
                logger.error(traceback.format_exc())
                return False

        return self.load_index()