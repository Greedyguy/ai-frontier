"""키워드 기반 구독자 관리 및 필터링 시스템"""

import json
import logging
import re
from typing import Dict, List, Optional, Set, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class KeywordSubscription:
    """키워드 구독 정보"""
    email: str
    keywords: List[str]
    digest_type: str  # 'daily' or 'weekly'
    created_at: str
    updated_at: str
    active: bool = True


class KeywordSubscriptionManager:
    """키워드 기반 구독자 관리자"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.subscriptions_file = self.data_dir / "keyword_subscriptions.json"
        self.legacy_mailing_file = self.data_dir / "mailing_list.json"

        # 구독자 정보: {email: KeywordSubscription}
        self.subscriptions: Dict[str, KeywordSubscription] = {}
        self._load_subscriptions()

    def _load_subscriptions(self):
        """구독자 정보 로드"""
        # 새로운 키워드 구독 파일 로드
        if self.subscriptions_file.exists():
            try:
                with open(self.subscriptions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                for email, sub_data in data.items():
                    self.subscriptions[email] = KeywordSubscription(**sub_data)

                logger.info(f"키워드 구독자 {len(self.subscriptions)}명 로드됨")
            except Exception as e:
                logger.error(f"키워드 구독 파일 로드 실패: {e}")

        # 기존 mailing_list.json에서 마이그레이션
        if self.legacy_mailing_file.exists() and not self.subscriptions:
            self._migrate_from_legacy()

    def _migrate_from_legacy(self):
        """기존 메일링 리스트에서 마이그레이션"""
        try:
            with open(self.legacy_mailing_file, 'r', encoding='utf-8') as f:
                legacy_data = json.load(f)

            current_time = datetime.now().isoformat()

            # daily 구독자들 마이그레이션 (키워드 없음)
            for email in legacy_data.get('daily', []):
                self.subscriptions[email] = KeywordSubscription(
                    email=email,
                    keywords=[],  # 기존 사용자는 모든 논문 받음
                    digest_type='daily',
                    created_at=current_time,
                    updated_at=current_time,
                    active=True
                )

            # weekly 구독자들 마이그레이션
            for email in legacy_data.get('weekly', []):
                self.subscriptions[email] = KeywordSubscription(
                    email=email,
                    keywords=[],
                    digest_type='weekly',
                    created_at=current_time,
                    updated_at=current_time,
                    active=True
                )

            # 새 형식으로 저장
            self._save_subscriptions()
            logger.info(f"기존 메일링 리스트에서 {len(self.subscriptions)}명 마이그레이션 완료")

        except Exception as e:
            logger.error(f"기존 메일링 리스트 마이그레이션 실패: {e}")

    def _save_subscriptions(self):
        """구독자 정보 저장"""
        try:
            data = {email: asdict(sub) for email, sub in self.subscriptions.items()}
            with open(self.subscriptions_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.debug("키워드 구독자 정보 저장 완료")
        except Exception as e:
            logger.error(f"키워드 구독자 정보 저장 실패: {e}")

    def add_subscription(self, email: str, keywords: List[str], digest_type: str = 'daily') -> bool:
        """구독자 추가 또는 업데이트"""
        try:
            current_time = datetime.now().isoformat()

            if email in self.subscriptions:
                # 기존 구독자 업데이트
                subscription = self.subscriptions[email]
                subscription.keywords = [kw.strip().lower() for kw in keywords if kw.strip()]
                subscription.digest_type = digest_type
                subscription.updated_at = current_time
                subscription.active = True
            else:
                # 새 구독자 추가
                self.subscriptions[email] = KeywordSubscription(
                    email=email,
                    keywords=[kw.strip().lower() for kw in keywords if kw.strip()],
                    digest_type=digest_type,
                    created_at=current_time,
                    updated_at=current_time,
                    active=True
                )

            self._save_subscriptions()
            logger.info(f"구독자 추가/업데이트: {email}, 키워드: {keywords}, 타입: {digest_type}")
            return True

        except Exception as e:
            logger.error(f"구독자 추가 실패: {e}")
            return False

    def remove_subscription(self, email: str) -> bool:
        """구독자 제거"""
        try:
            if email in self.subscriptions:
                del self.subscriptions[email]
                self._save_subscriptions()
                logger.info(f"구독자 제거: {email}")
                return True
            return False
        except Exception as e:
            logger.error(f"구독자 제거 실패: {e}")
            return False

    def get_subscription(self, email: str) -> Optional[KeywordSubscription]:
        """특정 구독자 정보 조회"""
        return self.subscriptions.get(email)

    def get_all_subscriptions(self, digest_type: str = None, active_only: bool = True) -> List[KeywordSubscription]:
        """구독자 목록 조회"""
        subscriptions = []
        for sub in self.subscriptions.values():
            if active_only and not sub.active:
                continue
            if digest_type and sub.digest_type != digest_type:
                continue
            subscriptions.append(sub)
        return subscriptions

    def get_subscribers_for_keywords(self, digest_type: str = 'daily') -> Dict[str, List[str]]:
        """키워드별 구독자 목록 반환 (이메일별로 해당 키워드 리스트 포함)"""
        result = {}
        for sub in self.get_all_subscriptions(digest_type=digest_type):
            result[sub.email] = sub.keywords
        return result


class PaperFilterService:
    """논문 필터링 서비스"""

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def filter_papers_by_keywords(self, papers: List[Dict], keywords: List[str]) -> List[Dict]:
        """키워드 기반 논문 필터링"""
        if not keywords:
            # 키워드가 없으면 모든 논문 반환 (기존 사용자 호환성)
            return papers

        filtered_papers = []
        keywords_lower = [kw.lower() for kw in keywords]

        for paper in papers:
            if self._paper_matches_keywords(paper, keywords_lower):
                filtered_papers.append(paper)

        self.logger.info(f"키워드 필터링: {len(papers)}개 논문 중 {len(filtered_papers)}개 선택됨")
        return filtered_papers

    def _paper_matches_keywords(self, paper: Dict, keywords: List[str]) -> bool:
        """논문이 키워드와 매칭되는지 확인"""
        try:
            # 검색 대상 텍스트 수집
            search_text = ""

            # 제목 추가
            if 'title' in paper:
                search_text += paper['title'] + " "

            # 초록 추가
            if 'abstract' in paper:
                search_text += paper['abstract'] + " "

            # 추출된 키워드 추가 (있다면)
            if 'keywords' in paper and isinstance(paper['keywords'], list):
                search_text += " ".join(paper['keywords']) + " "

            # 카테고리 추가
            if 'category' in paper:
                search_text += paper['category'] + " "

            search_text = search_text.lower()

            # 키워드 매칭 (OR 조건)
            for keyword in keywords:
                if self._keyword_matches_text(keyword, search_text):
                    return True

            return False

        except Exception as e:
            self.logger.warning(f"논문 키워드 매칭 중 오류: {e}")
            return False

    def _keyword_matches_text(self, keyword: str, text: str) -> bool:
        """키워드가 텍스트와 매칭되는지 확인 (유연한 매칭)"""
        # 정확한 단어 매칭
        if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE):
            return True

        # 부분 문자열 매칭 (3글자 이상인 경우)
        if len(keyword) >= 3 and keyword in text:
            return True

        # 약어 매칭 (대문자로 구성된 키워드)
        if keyword.isupper() and len(keyword) >= 2:
            # "ML", "AI", "NLP" 등의 약어
            if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE):
                return True

        return False

    def get_paper_statistics(self, papers: List[Dict]) -> Dict:
        """논문 통계 정보 반환"""
        if not papers:
            return {"total_papers": 0, "categories": [], "avg_abstract_length": 0}

        categories = {}
        total_abstract_length = 0
        abstract_count = 0

        for paper in papers:
            # 카테고리 집계
            if 'category' in paper:
                cat = paper['category']
                categories[cat] = categories.get(cat, 0) + 1

            # 초록 길이 계산
            if 'abstract' in paper and paper['abstract']:
                total_abstract_length += len(paper['abstract'])
                abstract_count += 1

        return {
            "total_papers": len(papers),
            "categories": list(categories.keys()),
            "category_distribution": categories,
            "avg_abstract_length": total_abstract_length // abstract_count if abstract_count > 0 else 0
        }


def get_keyword_subscription_manager() -> KeywordSubscriptionManager:
    """키워드 구독 매니저 팩토리 함수"""
    return KeywordSubscriptionManager()


def get_paper_filter_service() -> PaperFilterService:
    """논문 필터링 서비스 팩토리 함수"""
    return PaperFilterService()