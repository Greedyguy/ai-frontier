"""논문 중복 체크 및 업데이트 관리 모듈"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging
from dataclasses import dataclass

from ai_frontier.arxiv.client import ArxivPaper

logger = logging.getLogger(__name__)


@dataclass
class ExistingPaper:
    """기존 논문 정보"""
    arxiv_id: str
    title: str
    published_date: datetime
    updated_date: datetime
    file_path: str

    def __post_init__(self):
        """제목 정규화"""
        self.normalized_title = self._normalize_title(self.title)

    @staticmethod
    def _normalize_title(title: str) -> str:
        """제목 정규화 - 공백, 특수문자, 대소문자 통일"""
        # 소문자 변환, 연속된 공백을 하나로, 특수문자 제거
        normalized = re.sub(r'[^\w\s]', '', title.lower())
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        return normalized


class DuplicateManager:
    """논문 중복 체크 및 업데이트 관리자"""

    def __init__(self, reports_dir: str = "reports/individual_papers"):
        self.reports_dir = Path(reports_dir)
        self.existing_papers: Dict[str, ExistingPaper] = {}
        self._load_existing_papers()

    def _load_existing_papers(self) -> None:
        """기존 논문 파일들을 스캔하여 메타데이터 로드"""
        # 기존 논문 딕셔너리 초기화
        self.existing_papers = {}

        if not self.reports_dir.exists():
            logger.info(f"Reports directory {self.reports_dir} does not exist")
            return

        logger.info(f"Scanning existing papers in {self.reports_dir}")

        for md_file in self.reports_dir.rglob("*.md"):
            try:
                paper_info = self._extract_paper_info(md_file)
                if paper_info:
                    # ArXiv ID를 키로 사용하여 저장
                    self.existing_papers[paper_info.arxiv_id] = paper_info
                    logger.debug(f"Loaded existing paper: {paper_info.arxiv_id} - {paper_info.title[:50]}...")
            except Exception as e:
                logger.warning(f"Failed to parse {md_file}: {e}")

        logger.info(f"Loaded {len(self.existing_papers)} existing papers")

    def _extract_paper_info(self, file_path: Path) -> Optional[ExistingPaper]:
        """마크다운 파일에서 논문 정보 추출"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # ArXiv ID 추출
            arxiv_match = re.search(r'\*\*ArXiv ID\*\*: \[([^\]]+)\]', content)
            if not arxiv_match:
                return None
            arxiv_id = arxiv_match.group(1)

            # 제목 추출 (첫 번째 # 헤더)
            title_match = re.search(r'^# ([^\n]+)', content, re.MULTILINE)
            if not title_match:
                return None
            title = title_match.group(1)

            # 발행일 추출
            published_match = re.search(r'\*\*Published\*\*: ([^\n]+)', content)
            if not published_match:
                return None
            published_str = published_match.group(1)

            # 날짜 파싱
            try:
                # YYYY-MM-DD 형태로 파싱
                published_date = datetime.strptime(published_str, "%Y-%m-%d")
                # timezone-naive 날짜를 UTC로 변환
                from datetime import timezone
                published_date = published_date.replace(tzinfo=timezone.utc)
            except ValueError:
                logger.warning(f"Failed to parse published date: {published_str}")
                return None

            # 업데이트일은 발행일과 동일하다고 가정 (ArXiv에서는 updated 정보가 별도로 없는 경우가 많음)
            # 실제로는 ArXiv API에서 updated 정보를 가져와야 함
            updated_date = published_date

            return ExistingPaper(
                arxiv_id=arxiv_id,
                title=title,
                published_date=published_date,
                updated_date=updated_date,
                file_path=str(file_path)
            )

        except Exception as e:
            logger.error(f"Error extracting paper info from {file_path}: {e}")
            return None

    def check_duplicate(self, paper: ArxivPaper) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        논문 중복 체크

        Returns:
            Tuple[bool, Optional[str], Optional[str]]:
            - is_duplicate: 중복 여부
            - action: 'skip' (건너뛰기) 또는 'update' (업데이트) 또는 None
            - reason: 액션 이유
        """
        # timezone 처리를 위한 유틸리티 함수
        def make_timezone_aware(dt):
            from datetime import timezone
            if dt.tzinfo is None:
                return dt.replace(tzinfo=timezone.utc)
            return dt

        # 1. ArXiv ID로 직접 매치 체크
        if paper.arxiv_id in self.existing_papers:
            existing = self.existing_papers[paper.arxiv_id]

            # 업데이트 날짜 비교 (timezone-aware로 변환)
            new_updated = make_timezone_aware(paper.updated_date)
            existing_updated = make_timezone_aware(existing.updated_date)

            if new_updated > existing_updated:
                return True, 'update', f"Newer version found (existing: {existing_updated}, new: {new_updated})"
            else:
                return True, 'skip', f"Same or older version (existing: {existing_updated}, new: {new_updated})"

        # 2. 제목 기반 중복 체크
        normalized_new_title = ExistingPaper._normalize_title(paper.title)

        for existing_id, existing in self.existing_papers.items():
            # 제목이 매우 유사한 경우 (90% 이상 일치)
            similarity = self._calculate_title_similarity(normalized_new_title, existing.normalized_title)

            if similarity > 0.9:  # 90% 이상 유사
                # 날짜 비교 (timezone-aware로 변환)
                new_updated = make_timezone_aware(paper.updated_date)
                existing_updated = make_timezone_aware(existing.updated_date)

                if new_updated > existing_updated:
                    return True, 'update', f"Similar title with newer date (similarity: {similarity:.2f})"
                else:
                    return True, 'skip', f"Similar title with same/older date (similarity: {similarity:.2f})"

        # 3. 중복 아님
        return False, None, "New paper"

    def _calculate_title_similarity(self, title1: str, title2: str) -> float:
        """제목 유사도 계산 (간단한 단어 기반 Jaccard 유사도)"""
        words1 = set(title1.split())
        words2 = set(title2.split())

        if not words1 and not words2:
            return 1.0
        if not words1 or not words2:
            return 0.0

        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))

        return intersection / union if union > 0 else 0.0

    def remove_old_paper(self, file_path: str) -> bool:
        """기존 논문 파일 제거"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Removed old paper file: {file_path}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to remove old paper file {file_path}: {e}")
            return False

    def update_existing_paper(self, arxiv_id: str, new_paper_info: ExistingPaper) -> None:
        """기존 논문 정보 업데이트"""
        if arxiv_id in self.existing_papers:
            old_info = self.existing_papers[arxiv_id]
            # 기존 파일 제거
            self.remove_old_paper(old_info.file_path)

        # 새 정보로 업데이트
        self.existing_papers[arxiv_id] = new_paper_info
        logger.info(f"Updated paper info: {arxiv_id}")

    def add_new_paper(self, paper: ArxivPaper, file_path: str) -> None:
        """새로운 논문 정보 추가"""
        paper_info = ExistingPaper(
            arxiv_id=paper.arxiv_id,
            title=paper.title,
            published_date=paper.published_date,
            updated_date=paper.updated_date,
            file_path=file_path
        )
        self.existing_papers[paper.arxiv_id] = paper_info
        logger.info(f"Added new paper: {paper.arxiv_id}")

    def get_statistics(self) -> Dict[str, int]:
        """중복 체크 통계 반환"""
        return {
            "total_existing_papers": len(self.existing_papers),
            "oldest_paper": min(
                (p.published_date for p in self.existing_papers.values()),
                default=datetime.now()
            ).strftime("%Y-%m-%d") if self.existing_papers else "N/A",
            "newest_paper": max(
                (p.published_date for p in self.existing_papers.values()),
                default=datetime.now()
            ).strftime("%Y-%m-%d") if self.existing_papers else "N/A"
        }