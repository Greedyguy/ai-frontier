"""Main application entry point for AI Frontier."""

import os
import asyncio
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
def setup_logging():
    """Configure logging for the application."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler for all logs
    file_handler = logging.FileHandler(
        log_dir / f"ai_frontier_{datetime.now().strftime('%Y%m%d')}.log",
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    
    # Console handler for important logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return logging.getLogger(__name__)

# Initialize logging
logger = setup_logging()

from .arxiv.client import ArxivClient, ArxivPaper
from .translation.translator import get_translator
from .summarization.summarizer import get_summarizer
from .reporting.generator import ReportGenerator
from .keywords.extractor import get_keyword_extractor
from .embeddings.similarity_manager import get_similarity_manager
from .utils.duplicate_manager import DuplicateManager

class ArxivReportingService:
    """Main service for arxiv paper reporting automation."""

    def __init__(
        self,
        translation_provider: str = "openai",
        summarization_provider: str = "openai",
        keyword_provider: str = "openai",
        output_dir: str = "reports",
        use_rss: bool = False,
        enable_embeddings: bool = True
    ):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Initialize ArxivClient with error handling and higher max_results
        try:
            self.arxiv_client = ArxivClient(max_results=5000, use_rss=use_rss)
            search_method = "RSS feeds" if use_rss else "ArXiv API"
            self.logger.info(f"✅ ArxivReportingService: ArxivClient created successfully (using {search_method})")
            print(f"✅ ArxivReportingService: ArxivClient created successfully (using {search_method})")
        except Exception as e:
            self.logger.error(f"❌ ArxivReportingService: Failed to create ArxivClient: {e}")
            print(f"❌ ArxivReportingService: Failed to create ArxivClient: {e}")
            raise ImportError(f"Could not initialize ArxivClient: {e}")
            
        self.translator = get_translator(translation_provider)
        self.summarizer = get_summarizer(summarization_provider)
        self.keyword_extractor = get_keyword_extractor(keyword_provider)
        self.report_generator = ReportGenerator()

        # Initialize embeddings and similarity if enabled
        self.enable_embeddings = enable_embeddings
        self.similarity_manager = None
        if enable_embeddings:
            try:
                self.similarity_manager = get_similarity_manager()
                self.logger.info("✅ Similarity manager initialized successfully")
            except Exception as e:
                self.logger.warning(f"⚠️ Could not initialize similarity manager: {e}")
                self.enable_embeddings = False

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Initialize duplicate manager
        individual_papers_dir = self.output_dir / "individual_papers"
        individual_papers_dir.mkdir(exist_ok=True)
        self.duplicate_manager = DuplicateManager(str(individual_papers_dir))
        self.logger.info(f"✅ Duplicate manager initialized with {self.duplicate_manager.get_statistics()['total_existing_papers']} existing papers")

        self.logger.info(f"ArxivReportingService initialized with translation: {translation_provider}, summarization: {summarization_provider}, keywords: {keyword_provider}")

    def _save_individual_paper_immediately(
        self,
        paper: ArxivPaper,
        translated_title: str,
        translated_abstract: str,
        summary: str,
        key_points: List[str],
        keywords: List[str],
        output_dir: Path
    ) -> Path:
        """개별 논문 파일을 즉시 저장"""

        # 파일명 생성: 원문 제목 사용
        date_str = paper.published.strftime("%Y%m%d")
        safe_title = self._sanitize_filename(paper.title[:50])  # 원문 제목을 50자로 제한
        filename = f"{safe_title}_{date_str}.md"

        # 파일 경로
        file_path = output_dir / filename

        # 임베딩 처리 (콘텐츠 생성 전)
        if self.enable_embeddings and self.similarity_manager:
            try:
                self.logger.debug(f"Creating embedding for paper {paper.arxiv_id}")
                paper_embedding = self.similarity_manager.process_paper(paper, summary, key_points)
                self.logger.debug(f"Successfully created and stored embedding for {paper.arxiv_id}")
            except Exception as e:
                self.logger.warning(f"Failed to create embedding for {paper.arxiv_id}: {e}")

        # ReportGenerator를 사용하여 마크다운 콘텐츠 생성 (임베딩 저장 후)
        from .reporting.generator import ReportGenerator

        generator = ReportGenerator()

        # 번역 데이터 준비
        translations = {
            f"{paper.arxiv_id}_title": translated_title,
            f"{paper.arxiv_id}_abstract": translated_abstract
        }

        # 요약 데이터 준비
        summaries = {paper.arxiv_id: summary}

        # 핵심 포인트 데이터 준비
        key_points_dict = {paper.arxiv_id: key_points}

        # 새로운 format으로 콘텐츠 생성 (이제 유사도 링크 포함)
        content = generator.generate_individual_paper_file(
            paper=paper,
            translations=translations,
            summaries=summaries,
            key_points=key_points_dict,
            output_format="markdown"
        )

        # 파일 저장
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path

    def _sanitize_filename(self, filename: str) -> str:
        """파일명에서 불법 문자 제거"""
        import re
        # 윈도우와 유닉스에서 금지된 문자들 제거
        illegal_chars = r'[<>:"/\\|?*\x00-\x1f]'
        filename = re.sub(illegal_chars, '_', filename)
        # 연속된 언더스코어 제거
        filename = re.sub(r'_+', '_', filename)
        # 앞뒤 공백과 점 제거
        filename = filename.strip(' .')
        # 빈 문자열인 경우 기본값 사용
        if not filename:
            filename = "untitled"
        return filename

    def _generate_paper_markdown(
        self,
        paper: ArxivPaper,
        translated_title: str,
        translated_abstract: str,
        summary: str,
        key_points: List[str],
        keywords: List[str]
    ) -> str:
        """개별 논문의 마크다운 콘텐츠 생성"""

        content = f"""# {paper.title}

**Korean Title:** {translated_title}

## 📋 논문 정보

- **Authors:** {', '.join(paper.authors)}
- **ArXiv ID:** [{paper.arxiv_id}](https://arxiv.org/abs/{paper.arxiv_id})
- **Published:** {paper.published.strftime('%Y-%m-%d')}
- **Category:** {paper.category}
- **PDF URL:** [Download PDF]({paper.pdf_url})

## 📝 Original Abstract

{paper.abstract}

## 🇰🇷 Korean Abstract

{translated_abstract}

## 📊 Summary

{summary}

## 🔍 Key Points

"""

        for i, point in enumerate(key_points, 1):
            content += f"{i}. {point}\n"

        content += f"""
## 🏷️ 키워드

"""

        if keywords:
            keyword_items = " • ".join([f"`{kw}`" for kw in keywords])
            content += f"{keyword_items}\n"
        else:
            content += "키워드가 추출되지 않았습니다.\n"

        content += f"""
## 🔗 링크

- [ArXiv 페이지](https://arxiv.org/abs/{paper.arxiv_id})
- [PDF 다운로드]({paper.pdf_url})

---
*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        return content

    def _parse_date(self, date_str: str) -> datetime:
        """Parse date string in YYYYMMDD or YYYY-MM-DD format."""
        try:
            # Try YYYYMMDD format first
            return datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            try:
                # Try YYYY-MM-DD format
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Invalid date format: {date_str}. Expected YYYYMMDD or YYYY-MM-DD format.")

    async def process_papers(
        self,
        categories: List[str] = None,
        days_back: int = 1,
        target_language: str = "ko",
        keywords: List[str] = None,
        keyword_only: bool = False,
        start_date: str = None,
        end_date: str = None,
        progress_callback = None
    ) -> str:
        """Process papers and generate report."""
        
        self.logger.info("=== 논문 수집 작업 시작 ===")
        self.logger.info(f"설정 - 카테고리: {categories}, 일수: {days_back}, 언어: {target_language}")
        self.logger.info(f"키워드: {keywords}, 키워드 전용: {keyword_only}")
        self.logger.info(f"날짜 범위: {start_date} ~ {end_date}")

        # Handle date range input
        if start_date or end_date:
            if not start_date or not end_date:
                raise ValueError("Both start_date and end_date must be provided when using date range.")

            start_dt = self._parse_date(start_date)
            end_dt = self._parse_date(end_date)

            if start_dt > end_dt:
                raise ValueError("start_date must be earlier than end_date.")

            # Validate that end_date is not in the future
            today = datetime.now().date()
            if end_dt.date() > today:
                raise ValueError(f"end_date ({end_date}) cannot be in the future. Today is {today.strftime('%Y%m%d')}")

            # When using date range, we pass start_date and end_date directly
            # days_back will be ignored by ArXiv client when start_date/end_date are provided

            self.logger.info(f"날짜 범위 검색: {start_date} ~ {end_date}")
            print(f"Searching papers from {start_date} to {end_date}")

        if keywords:
            if keyword_only:
                self.logger.info(f"키워드 전용 검색: {', '.join(keywords)}")
                print(f"Searching papers by keywords: {', '.join(keywords)}")
                papers = self.arxiv_client.search_by_keywords_only(
                    keywords=keywords,
                    days_back=days_back,
                    categories=categories,
                    start_date=start_dt if start_date else None,
                    end_date=end_dt if end_date else None
                )
            else:
                self.logger.info(f"키워드+카테고리 검색: {', '.join(keywords)} in {categories or 'default'}")
                print(f"Searching papers with keywords: {', '.join(keywords)} in categories: {categories or 'default'}")
                papers = self.arxiv_client.search_recent_papers(
                    categories=categories,
                    days_back=days_back,
                    keywords=keywords,
                    start_date=start_dt if start_date else None,
                    end_date=end_dt if end_date else None
                )
        else:
            if start_date and end_date:
                self.logger.info(f"날짜 범위별 논문 검색: {start_date} ~ {end_date}")
                print(f"Fetching papers from {start_date} to {end_date}...")
            else:
                self.logger.info(f"최근 {days_back}일간 논문 검색, 카테고리: {categories}")
                print("Fetching recent papers from ArXiv...")
            papers = self.arxiv_client.search_recent_papers(
                categories=categories,
                days_back=days_back,
                start_date=start_dt if start_date else None,
                end_date=end_dt if end_date else None
            )

        if not papers:
            self.logger.warning("검색된 논문이 없습니다.")
            print("No recent papers found.")
            if progress_callback:
                from .api.models import CollectionProgress
                progress_callback(CollectionProgress(
                    status="completed",
                    current_step="검색된 논문이 없습니다.",
                    papers_found=0,
                    papers_processed=0,
                    total_papers=0,
                    progress_percentage=100
                ))
            return ""

        self.logger.info(f"검색 완료: {len(papers)}개의 논문 발견")
        print(f"Found {len(papers)} papers. Processing...")
        
        if progress_callback:
            from .api.models import CollectionProgress
            progress_callback(CollectionProgress(
                status="collecting",
                current_step=f"{len(papers)}개의 논문을 처리하고 있습니다...",
                papers_found=len(papers),
                papers_processed=0,
                total_papers=len(papers),
                progress_percentage=20
            ))

        # 개별 논문 파일 저장을 위한 디렉토리 준비
        individual_papers_dir = self.output_dir / "individual_papers"
        individual_papers_dir.mkdir(parents=True, exist_ok=True)
        saved_files = []

        # 중복 체크 통계
        skipped_papers = []
        updated_papers = []
        new_papers = []

        for i, paper in enumerate(papers, 1):
            self.logger.info(f"논문 처리 중 {i}/{len(papers)}: {paper.arxiv_id} - {paper.title[:100]}")
            print(f"Processing paper {i}/{len(papers)}: {paper.title[:50]}...")

            # 중복 체크 수행
            is_duplicate, action, reason = self.duplicate_manager.check_duplicate(paper)

            if is_duplicate:
                if action == 'skip':
                    skipped_papers.append((paper.arxiv_id, reason))
                    self.logger.info(f"논문 건너뛰기 - {paper.arxiv_id}: {reason}")
                    print(f"Skipping paper {paper.arxiv_id}: {reason}")
                    continue
                elif action == 'update':
                    updated_papers.append((paper.arxiv_id, reason))
                    self.logger.info(f"논문 업데이트 - {paper.arxiv_id}: {reason}")
                    print(f"Updating paper {paper.arxiv_id}: {reason}")
                    # 업데이트의 경우 처리를 계속 진행
            else:
                new_papers.append(paper.arxiv_id)
                self.logger.info(f"새로운 논문 - {paper.arxiv_id}: {reason}")
                print(f"New paper {paper.arxiv_id}: {reason}")

            # 중단 체크를 위한 progress_callback 호출
            if progress_callback:
                from .api.models import CollectionProgress
                progress_percentage = 20 + int((70 * (i-1)) / len(papers))  # 20% ~ 90%
                try:
                    progress_callback(CollectionProgress(
                        status="processing",
                        current_step=f"논문 {i}/{len(papers)} 처리 중: {paper.title[:30]}...",
                        papers_found=len(papers),
                        papers_processed=i-1,
                        total_papers=len(papers),
                        progress_percentage=progress_percentage
                    ))
                except Exception as e:
                    # 중단 예외 발생 시 루프 종료
                    if "중단되었습니다" in str(e):
                        self.logger.info(f"논문 처리 중단됨 - {i-1}/{len(papers)} 완료")
                        raise e
                    else:
                        self.logger.warning(f"Progress callback 오류: {e}")
                        # 다른 오류는 무시하고 계속 진행

            # Process paper
            try:
                self.logger.debug(f"번역 시작 - 논문 {paper.arxiv_id}")
                translated_title = self.translator.translate(
                    paper.title, target_language
                )
                translated_abstract = self.translator.translate(
                    paper.abstract, target_language
                )

                # Generate summary
                self.logger.debug(f"요약 생성 시작 - 논문 {paper.arxiv_id}")
                summary = self.summarizer.summarize(paper.abstract)

                # Extract key points
                points = self.summarizer.summarize_key_points(paper.abstract)
                self.logger.debug(f"요약 완료 - 논문 {paper.arxiv_id}")

                # Extract keywords
                self.logger.debug(f"키워드 추출 시작 - 논문 {paper.arxiv_id}")
                paper_keywords = self.keyword_extractor.extract_keywords(
                    paper.title, paper.abstract
                )
                self.logger.debug(f"키워드 추출 완료 - 논문 {paper.arxiv_id}: {paper_keywords}")

                # 개별 논문 파일 즉시 저장
                self.logger.debug(f"개별 파일 저장 시작 - 논문 {paper.arxiv_id}")
                file_path = self._save_individual_paper_immediately(
                    paper=paper,
                    translated_title=translated_title,
                    translated_abstract=translated_abstract,
                    summary=summary,
                    key_points=points,
                    keywords=paper_keywords,
                    output_dir=individual_papers_dir
                )
                saved_files.append(file_path)

                # 중복 관리자에 논문 정보 업데이트
                from .utils.duplicate_manager import ExistingPaper
                if is_duplicate and action == 'update':
                    self.duplicate_manager.update_existing_paper(
                        paper.arxiv_id,
                        ExistingPaper(
                            arxiv_id=paper.arxiv_id,
                            title=paper.title,
                            published_date=paper.published_date,
                            updated_date=paper.updated_date,
                            file_path=str(file_path)
                        )
                    )
                else:
                    self.duplicate_manager.add_new_paper(paper, str(file_path))

                self.logger.info(f"논문 처리 및 저장 완료 - {paper.arxiv_id}: {file_path}")
                print(f"Saved: {file_path.name}")

                # 논문 저장 완료 후 진행 상황 업데이트
                if progress_callback:
                    from .api.models import CollectionProgress
                    progress_percentage = 20 + int((70 * i) / len(papers))  # 20% ~ 90%
                    try:
                        progress_callback(CollectionProgress(
                            status="processing",
                            current_step=f"논문 {i}/{len(papers)} 저장 완료: {translated_title[:30]}...",
                            papers_found=len(papers),
                            papers_processed=i,  # 현재 완료된 논문 수
                            total_papers=len(papers),
                            progress_percentage=progress_percentage
                        ))
                    except Exception as e:
                        # 중단 예외 발생 시 루프 종료
                        if "중단되었습니다" in str(e):
                            self.logger.info(f"논문 처리 중단됨 - {i}/{len(papers)} 완료")
                            raise e
                        else:
                            self.logger.warning(f"Progress callback 오류 (저장 후): {e}")

            except Exception as e:
                self.logger.error(f"논문 처리 실패 - {paper.arxiv_id}: {str(e)}")
                print(f"Error processing paper {paper.arxiv_id}: {e}")
                continue

        # 중복 체크 통계 출력
        self.logger.info(f"=== 중복 체크 통계 ===")
        self.logger.info(f"새로운 논문: {len(new_papers)}개")
        self.logger.info(f"업데이트된 논문: {len(updated_papers)}개")
        self.logger.info(f"건너뛴 논문: {len(skipped_papers)}개")

        print(f"\n=== Duplicate Check Statistics ===")
        print(f"New papers: {len(new_papers)}")
        print(f"Updated papers: {len(updated_papers)}")
        print(f"Skipped papers: {len(skipped_papers)}")

        if skipped_papers:
            print("\nSkipped papers:")
            for arxiv_id, reason in skipped_papers:
                print(f"  - {arxiv_id}: {reason}")

        if updated_papers:
            print("\nUpdated papers:")
            for arxiv_id, reason in updated_papers:
                print(f"  - {arxiv_id}: {reason}")

        self.logger.info(f"=== 논문 수집 작업 완료 - 총 {len(saved_files)}개 논문 파일 저장 ===")
        print(f"\nIndividual files saved to: {individual_papers_dir}")
        print(f"Total files saved: {len(saved_files)}")

        # Log all saved file paths
        for file_path in saved_files:
            self.logger.info(f"저장된 파일: {file_path}")

        if progress_callback:
            from .api.models import CollectionProgress
            progress_callback(CollectionProgress(
                status="completed",
                current_step=f"모든 논문 파일 저장 완료 ({len(saved_files)}개 파일)",
                papers_found=len(papers),
                papers_processed=len(saved_files),
                total_papers=len(papers),
                progress_percentage=100
            ))

        # Return the individual papers directory path
        return str(individual_papers_dir)

def main():
    """Main function for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(description="ArXiv Paper Reporting Service")
    parser.add_argument(
        "--categories",
        nargs="+",
        default=["cs.AI", "cs.LG", "cs.CL", "cs.CV"],
        help="ArXiv categories to search"
    )
    parser.add_argument(
        "--days-back",
        type=int,
        default=1,
        help="Number of days back to search"
    )
    parser.add_argument(
        "--start-date",
        type=str,
        help="Start date for paper collection (YYYYMMDD format)"
    )
    parser.add_argument(
        "--end-date",
        type=str,
        help="End date for paper collection (YYYYMMDD format)"
    )
    parser.add_argument(
        "--translation-provider",
        choices=["openai", "claude"],
        default="openai",
        help="Translation service provider"
    )
    parser.add_argument(
        "--summarization-provider",
        choices=["openai", "claude"],
        default="openai",
        help="Summarization service provider"
    )
    parser.add_argument(
        "--output-dir",
        default="reports",
        help="Output directory for reports"
    )
    parser.add_argument(
        "--keywords",
        nargs="+",
        help="Keywords to search for in papers (title, abstract, comments)"
    )
    parser.add_argument(
        "--keyword-only",
        action="store_true",
        help="Search only by keywords without category restrictions"
    )
    parser.add_argument(
        "--generate-digest",
        choices=["daily", "weekly"],
        help="Generate daily or weekly digest from existing papers"
    )
    parser.add_argument(
        "--digest-date",
        type=str,
        help="Date for digest generation (YYYYMMDD format, defaults to today)"
    )
    parser.add_argument(
        "--use-rss",
        action="store_true",
        help="Use RSS feeds instead of ArXiv API (more accurate for recent papers)"
    )

    args = parser.parse_args()

    # Handle digest generation
    if args.generate_digest:
        from .summarization.digest import DigestGenerator
        from datetime import datetime

        # Parse target date
        if args.digest_date:
            try:
                target_date = datetime.strptime(args.digest_date, "%Y%m%d")
            except ValueError:
                print(f"Invalid date format: {args.digest_date}. Expected YYYYMMDD format.")
                return 1
        else:
            target_date = datetime.now()

        # Create digest generator
        digest_generator = DigestGenerator(
            translation_provider=args.translation_provider,
            summarization_provider=args.summarization_provider
        )

        try:
            if args.generate_digest == "daily":
                digest_path = digest_generator.save_daily_digest(target_date)
                print(f"Daily digest generated: {digest_path}")
            elif args.generate_digest == "weekly":
                digest_path = digest_generator.save_weekly_digest(target_date)
                print(f"Weekly digest generated: {digest_path}")

            return 0

        except Exception as e:
            print(f"Error generating digest: {e}")
            return 1

    # Regular paper collection
    service = ArxivReportingService(
        translation_provider=args.translation_provider,
        summarization_provider=args.summarization_provider,
        output_dir=args.output_dir,
        use_rss=args.use_rss
    )

    try:
        report_path = asyncio.run(
            service.process_papers(
                categories=args.categories,
                days_back=args.days_back,
                keywords=args.keywords,
                keyword_only=args.keyword_only,
                start_date=args.start_date,
                end_date=args.end_date
            )
        )
        print(f"Successfully generated report: {report_path}")

    except Exception as e:
        print(f"Error generating report: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())