#!/usr/bin/env python3
"""
Standalone script for automation tools (n8n, Zapier, etc.)

이 스크립트는 백엔드 서버 없이도 n8n과 같은 자동화 도구에서
직접 실행할 수 있도록 설계되었습니다.

Usage:
    python automation_script.py collect --keywords "transformer" "attention" --days-back 7
    python automation_script.py digest daily --date 20250926
    python automation_script.py digest weekly
"""

import asyncio
import json
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import logging

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_frontier.main import ArxivReportingService
from ai_frontier.summarization.digest import DigestGenerator
from ai_frontier.embeddings.service import EmbeddingService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("automation_script")


class AutomationResult:
    """결과를 표준화된 형식으로 반환하기 위한 클래스"""

    def __init__(self, success: bool, message: str, data: Dict[str, Any] = None):
        self.success = success
        self.message = message
        self.data = data or {}

    def to_json(self) -> str:
        """JSON 형태로 결과 반환"""
        result = {
            "success": self.success,
            "message": self.message,
            "timestamp": datetime.now().isoformat(),
            **self.data
        }
        return json.dumps(result, ensure_ascii=False, indent=2)

    def print_result(self):
        """결과를 콘솔에 출력 (n8n에서 stdout 캡처용)"""
        print(self.to_json())


class AutomationScriptRunner:
    """자동화 도구를 위한 메인 스크립트 실행기"""

    def __init__(self):
        self.logger = logger

    async def collect_papers(
        self,
        keywords: List[str] = None,
        categories: List[str] = None,
        days_back: int = 1,
        start_date: str = None,
        end_date: str = None,
        keyword_only: bool = False,
        translation_provider: str = "openai",
        summarization_provider: str = "openai",
        output_dir: str = "reports"
    ) -> AutomationResult:
        """논문 수집 실행"""
        try:
            self.logger.info("=== 논문 수집 시작 ===")
            self.logger.info(f"키워드: {keywords}")
            self.logger.info(f"카테고리: {categories}")
            self.logger.info(f"기간: {days_back}일 전부터" if not start_date else f"기간: {start_date} ~ {end_date}")

            # 기본값 설정
            if not categories:
                categories = ["cs.AI", "cs.LG", "cs.CL", "cs.CV"]

            # 서비스 인스턴스 생성
            service = ArxivReportingService(
                translation_provider=translation_provider,
                summarization_provider=summarization_provider,
                output_dir=output_dir
            )

            # 진행 상황 출력 콜백
            def progress_callback(progress):
                self.logger.info(f"진행률: {progress.progress_percentage}% - {progress.current_step}")

            # 논문 수집 실행
            result = await service.process_papers(
                categories=categories if not keyword_only else None,
                days_back=days_back,
                keywords=keywords,
                keyword_only=keyword_only,
                start_date=start_date,
                end_date=end_date,
                progress_callback=progress_callback
            )

            # 결과 처리
            if isinstance(result, tuple):
                report_path, papers_collected = result
            else:
                report_path = result
                papers_collected = 0

            # 개별 논문 파일 수 확인
            papers_dir = Path(output_dir) / "individual_papers"
            individual_files = list(papers_dir.glob("*.md")) if papers_dir.exists() else []

            self.logger.info(f"=== 논문 수집 완료 ===")
            self.logger.info(f"수집된 논문: {papers_collected}개")
            self.logger.info(f"개별 파일: {len(individual_files)}개")
            self.logger.info(f"보고서 경로: {report_path}")

            return AutomationResult(
                success=True,
                message=f"논문 수집 완료: {papers_collected}개 논문 수집됨",
                data={
                    "papers_collected": papers_collected,
                    "individual_files_count": len(individual_files),
                    "report_path": str(report_path),
                    "individual_files": [f.name for f in individual_files[-10:]],  # 최신 10개 파일명
                    "collection_params": {
                        "keywords": keywords,
                        "categories": categories,
                        "days_back": days_back,
                        "start_date": start_date,
                        "end_date": end_date,
                        "keyword_only": keyword_only
                    }
                }
            )

        except Exception as e:
            self.logger.error(f"논문 수집 실패: {str(e)}")
            return AutomationResult(
                success=False,
                message=f"논문 수집 실패: {str(e)}",
                data={"error_type": type(e).__name__}
            )

    async def generate_digest(
        self,
        digest_type: str = "daily",
        date: str = None,
        translation_provider: str = "openai",
        summarization_provider: str = "openai"
    ) -> AutomationResult:
        """다이제스트 생성 실행"""
        try:
            self.logger.info(f"=== {digest_type.upper()} 다이제스트 생성 시작 ===")

            # 날짜 파싱
            if date:
                target_date = datetime.strptime(date, "%Y%m%d")
            else:
                target_date = datetime.now()

            self.logger.info(f"대상 날짜: {target_date.strftime('%Y-%m-%d')}")

            # 다이제스트 생성기 생성
            digest_generator = DigestGenerator(
                translation_provider=translation_provider,
                summarization_provider=summarization_provider
            )

            # 다이제스트 생성
            if digest_type.lower() == "daily":
                digest_path = digest_generator.save_daily_digest(target_date)
            elif digest_type.lower() == "weekly":
                digest_path = digest_generator.save_weekly_digest(target_date)
            else:
                raise ValueError(f"Invalid digest type: {digest_type}")

            # 생성된 파일 정보
            file_size = digest_path.stat().st_size if digest_path.exists() else 0

            self.logger.info(f"=== {digest_type.upper()} 다이제스트 생성 완료 ===")
            self.logger.info(f"파일 경로: {digest_path}")
            self.logger.info(f"파일 크기: {file_size} bytes")

            return AutomationResult(
                success=True,
                message=f"{digest_type.capitalize()} digest generated successfully",
                data={
                    "digest_type": digest_type,
                    "digest_date": target_date.strftime("%Y-%m-%d"),
                    "digest_path": str(digest_path),
                    "file_size": file_size,
                    "filename": digest_path.name
                }
            )

        except Exception as e:
            self.logger.error(f"다이제스트 생성 실패: {str(e)}")
            return AutomationResult(
                success=False,
                message=f"Digest generation failed: {str(e)}",
                data={
                    "error_type": type(e).__name__,
                    "digest_type": digest_type
                }
            )

    def list_recent_files(self, limit: int = 20) -> AutomationResult:
        """최근 생성된 파일 목록 조회"""
        try:
            papers_dir = Path("reports/individual_papers")

            if not papers_dir.exists():
                return AutomationResult(
                    success=True,
                    message="No papers directory found",
                    data={"files": [], "total": 0}
                )

            # 최근 파일들 가져오기
            files = []
            for file_path in papers_dir.glob("*.md"):
                try:
                    stat = file_path.stat()
                    files.append({
                        "filename": file_path.name,
                        "path": str(file_path),
                        "size": stat.st_size,
                        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
                except Exception as e:
                    self.logger.warning(f"Error processing file {file_path}: {e}")

            # 수정시간 기준 정렬
            files.sort(key=lambda x: x['modified'], reverse=True)

            return AutomationResult(
                success=True,
                message=f"Found {len(files)} paper files",
                data={
                    "files": files[:limit],
                    "total": len(files),
                    "limit": limit
                }
            )

        except Exception as e:
            return AutomationResult(
                success=False,
                message=f"Failed to list files: {str(e)}"
            )

    async def generate_embeddings(self) -> AutomationResult:
        """수집된 논문들의 임베딩 생성"""
        try:
            self.logger.info("=== 임베딩 생성 시작 ===")

            # 임베딩 서비스 초기화
            embedding_service = EmbeddingService()

            # 논문 파일들 찾기
            papers_dir = Path("reports/individual_papers")
            if not papers_dir.exists():
                return AutomationResult(
                    success=False,
                    message="No papers directory found. Run collect command first."
                )

            paper_files = list(papers_dir.glob("*.md"))
            if not paper_files:
                return AutomationResult(
                    success=False,
                    message="No paper files found. Run collect command first."
                )

            self.logger.info(f"논문 파일 수: {len(paper_files)}개")

            # 임베딩 생성
            embeddings_generated = await embedding_service.generate_embeddings_for_papers(paper_files)

            # 벡터 데이터베이스 파일 확인
            embeddings_dir = Path("data/embeddings")
            faiss_index = embeddings_dir / "faiss.index"
            metadata_file = embeddings_dir / "metadata.pkl"

            index_size = faiss_index.stat().st_size if faiss_index.exists() else 0
            metadata_size = metadata_file.stat().st_size if metadata_file.exists() else 0

            self.logger.info(f"=== 임베딩 생성 완료 ===")
            self.logger.info(f"생성된 임베딩 수: {embeddings_generated}개")
            self.logger.info(f"FAISS 인덱스 크기: {index_size} bytes")
            self.logger.info(f"메타데이터 크기: {metadata_size} bytes")

            return AutomationResult(
                success=True,
                message=f"Embeddings generated successfully: {embeddings_generated} papers processed",
                data={
                    "embeddings_generated": embeddings_generated,
                    "paper_files_processed": len(paper_files),
                    "faiss_index_size": index_size,
                    "metadata_size": metadata_size,
                    "faiss_index_path": str(faiss_index),
                    "metadata_path": str(metadata_file),
                    "vector_db_exists": faiss_index.exists() and metadata_file.exists()
                }
            )

        except Exception as e:
            self.logger.error(f"임베딩 생성 실패: {str(e)}")
            return AutomationResult(
                success=False,
                message=f"Embedding generation failed: {str(e)}",
                data={"error_type": type(e).__name__}
            )


async def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(
        description="AI Frontier Automation Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 키워드로 논문 수집
  python automation_script.py collect --keywords "transformer" "attention" --days-back 7

  # 특정 날짜 범위로 논문 수집
  python automation_script.py collect --start-date 20250920 --end-date 20250926

  # 일일 다이제스트 생성
  python automation_script.py digest daily

  # 특정 날짜의 주간 다이제스트 생성
  python automation_script.py digest weekly --date 20250926

  # 최근 파일 목록 조회
  python automation_script.py list --limit 10

  # 논문 임베딩 생성 (RAG 검색용)
  python automation_script.py generate-embeddings
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # collect 명령어
    collect_parser = subparsers.add_parser('collect', help='Collect papers')
    collect_parser.add_argument('--keywords', nargs='*', help='Keywords to search for')
    collect_parser.add_argument('--categories', nargs='*', default=['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV'], help='ArXiv categories')
    collect_parser.add_argument('--days-back', type=int, default=1, help='Number of days back to search')
    collect_parser.add_argument('--start-date', help='Start date (YYYYMMDD)')
    collect_parser.add_argument('--end-date', help='End date (YYYYMMDD)')
    collect_parser.add_argument('--keyword-only', action='store_true', help='Search only by keywords')
    collect_parser.add_argument('--translation-provider', default='openai', choices=['openai', 'claude'])
    collect_parser.add_argument('--summarization-provider', default='openai', choices=['openai', 'claude'])
    collect_parser.add_argument('--output-dir', default='reports', help='Output directory')

    # digest 명령어
    digest_parser = subparsers.add_parser('digest', help='Generate digest')
    digest_parser.add_argument('type', choices=['daily', 'weekly'], help='Digest type')
    digest_parser.add_argument('--date', help='Target date (YYYYMMDD)')
    digest_parser.add_argument('--translation-provider', default='openai', choices=['openai', 'claude'])
    digest_parser.add_argument('--summarization-provider', default='openai', choices=['openai', 'claude'])

    # list 명령어
    list_parser = subparsers.add_parser('list', help='List recent files')
    list_parser.add_argument('--limit', type=int, default=20, help='Number of files to list')

    # generate-embeddings 명령어
    embeddings_parser = subparsers.add_parser('generate-embeddings', help='Generate embeddings for collected papers')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    runner = AutomationScriptRunner()

    try:
        if args.command == 'collect':
            result = await runner.collect_papers(
                keywords=args.keywords,
                categories=args.categories,
                days_back=args.days_back,
                start_date=args.start_date,
                end_date=args.end_date,
                keyword_only=args.keyword_only,
                translation_provider=args.translation_provider,
                summarization_provider=args.summarization_provider,
                output_dir=args.output_dir
            )

        elif args.command == 'digest':
            result = await runner.generate_digest(
                digest_type=args.type,
                date=args.date,
                translation_provider=args.translation_provider,
                summarization_provider=args.summarization_provider
            )

        elif args.command == 'list':
            result = runner.list_recent_files(limit=args.limit)

        elif args.command == 'generate-embeddings':
            result = await runner.generate_embeddings()

        else:
            result = AutomationResult(
                success=False,
                message=f"Unknown command: {args.command}"
            )

        # 결과 출력 (n8n이 stdout을 캡처함)
        result.print_result()

        # 실패시 exit code 1
        if not result.success:
            sys.exit(1)

    except KeyboardInterrupt:
        logger.info("작업이 사용자에 의해 중단되었습니다.")
        result = AutomationResult(
            success=False,
            message="작업이 사용자에 의해 중단되었습니다."
        )
        result.print_result()
        sys.exit(1)

    except Exception as e:
        logger.error(f"예기치 못한 오류 발생: {str(e)}")
        result = AutomationResult(
            success=False,
            message=f"Unexpected error: {str(e)}",
            data={"error_type": type(e).__name__}
        )
        result.print_result()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())