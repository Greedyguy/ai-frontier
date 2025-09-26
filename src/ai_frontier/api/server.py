"""FastAPI server for AI Frontier service."""

import asyncio
import uuid
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any
from datetime import datetime
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import uvicorn

# Configure logging for API server
def setup_api_logging():
    """Configure logging for API server."""
    from pathlib import Path
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # API specific log file
    api_handler = logging.FileHandler(
        log_dir / f"api_server_{time.strftime('%Y%m%d')}.log",
        encoding='utf-8'
    )
    api_handler.setLevel(logging.INFO)
    api_handler.setFormatter(formatter)
    
    # Get or create logger
    api_logger = logging.getLogger("api_server")
    api_logger.setLevel(logging.INFO)
    api_logger.addHandler(api_handler)
    
    return api_logger

# Initialize API logger
api_logger = setup_api_logging()

from .models import (
    PaperCollectionRequest,
    CollectionStatus,
    CollectionProgress,
    CollectionResult,
    PaperInfo,
    DigestRequest,
    DigestInfo,
    DigestResult,
    EmailSubscribeRequest,
    EmailUnsubscribeRequest,
    NotificationSettingsRequest,
    NotificationTestRequest,
    NotificationStatus,
    NotificationResult,
    MailingListResponse,
    KeywordSubscribeRequest,
    KeywordSubscriptionInfo,
    KeywordSubscriptionsResponse,
    KeywordSubscriptionResponse,
    PaperSearchRequest,
    SimilarPapersRequest,
    PaperSearchResponse,
    SimilarPapersResponse,
    DatabaseStatsResponse,
    HybridSearchRequest,
    HybridSearchResponse,
    HybridStatsResponse
)
from ..main import ArxivReportingService
from .webhook import router as webhook_router
from ..summarization.digest import DigestGenerator
from ..notification.notification_manager import NotificationManager
from ..notification.keyword_subscription_manager import KeywordSubscriptionManager, PaperFilterService
from ..search.rag_service import RAGSearchService
from ..search.hybrid_service import HybridSearchService

# FastAPI 앱 생성
app = FastAPI(
    title="AI Frontier API",
    description="ArXiv 논문 자동 수집 및 번역 서비스 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3001", "http://127.0.0.1:3001", "http://localhost:3002", "http://127.0.0.1:3002", "http://localhost:3003", "http://127.0.0.1:3003", "http://localhost:3004", "http://127.0.0.1:3004", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include webhook router
app.include_router(webhook_router)

# Thread pool executor for background tasks
executor = ThreadPoolExecutor(max_workers=2)

# 전역 상태 관리
collection_tasks: Dict[str, CollectionStatus] = {}

# 알림 관리자 초기화
notification_manager = NotificationManager()
keyword_subscription_manager = KeywordSubscriptionManager()
paper_filter_service = PaperFilterService()

# RAG 검색 서비스 초기화
try:
    rag_service = RAGSearchService()
    api_logger.info("RAG search service initialized successfully")
except Exception as e:
    api_logger.warning(f"Failed to initialize RAG search service: {e}")
    rag_service = None

# 하이브리드 검색 서비스 초기화
try:
    hybrid_service = HybridSearchService()
    api_logger.info("Hybrid search service initialized successfully")
except Exception as e:
    api_logger.warning(f"Failed to initialize hybrid search service: {e}")
    hybrid_service = None


class CollectionManager:
    """논문 수집 작업 관리자"""

    def __init__(self):
        self.tasks = collection_tasks
        self.cancellation_flags = {}  # 작업 중단 플래그

    def create_task(self, request: PaperCollectionRequest) -> str:
        """새로운 수집 작업 생성"""
        task_id = str(uuid.uuid4())

        status = CollectionStatus(
            task_id=task_id,
            status="created",
            progress=CollectionProgress(
                status="created",
                current_step="작업이 생성되었습니다.",
                papers_found=0,
                papers_processed=0,
                total_papers=0,
                progress_percentage=0
            )
        )

        self.tasks[task_id] = status
        self.cancellation_flags[task_id] = False  # 중단 플래그 초기화
        return task_id

    def update_progress(self, task_id: str, progress: CollectionProgress):
        """작업 진행 상황 업데이트"""
        if task_id in self.tasks:
            self.tasks[task_id].progress = progress
            self.tasks[task_id].status = progress.status

    def complete_task(self, task_id: str, result: CollectionResult):
        """작업 완료 처리"""
        if task_id in self.tasks:
            self.tasks[task_id].result = result
            self.tasks[task_id].status = "completed" if result.success else "error"

    def get_task(self, task_id: str) -> CollectionStatus:
        """작업 상태 조회"""
        return self.tasks.get(task_id)
    
    def cancel_task(self, task_id: str) -> bool:
        """작업 중단 요청"""
        if task_id in self.cancellation_flags:
            self.cancellation_flags[task_id] = True
            api_logger.info(f"작업 중단 요청됨 - Task ID: {task_id}")
            return True
        return False
    
    def is_cancelled(self, task_id: str) -> bool:
        """작업이 중단되었는지 확인"""
        return self.cancellation_flags.get(task_id, False)


# 전역 매니저 인스턴스
manager = CollectionManager()


def collect_papers_sync(task_id: str, request: PaperCollectionRequest):
    """Thread pool에서 실행할 동기 함수"""
    # 새 이벤트 루프 생성 (스레드에서 실행되므로)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # 비동기 함수 실행
        return loop.run_until_complete(collect_papers_background(task_id, request))
    finally:
        loop.close()


async def collect_papers_background(task_id: str, request: PaperCollectionRequest):
    """백그라운드에서 논문 수집 실행"""
    start_time = time.time()
    
    api_logger.info(f"=== 백그라운드 작업 시작 - Task ID: {task_id} ===")
    api_logger.info(f"요청 설정: {request.dict()}")

    try:
        # 진행 상황 업데이트: 시작
        manager.update_progress(task_id, CollectionProgress(
            status="initializing",
            current_step="서비스를 초기화하고 있습니다...",
            progress_percentage=5
        ))

        api_logger.info(f"ArxivReportingService 초기화 중 - Task: {task_id}")
        # ArxivReportingService 인스턴스 생성
        search_method = "RSS feeds" if request.use_rss else "ArXiv API"
        api_logger.info(f"검색 방식: {search_method}")
        service = ArxivReportingService(
            translation_provider=request.translation_provider,
            summarization_provider=request.summarization_provider,
            keyword_provider="openai",  # 키워드 추출은 현재 OpenAI만 지원
            output_dir="reports",
            use_rss=request.use_rss
        )

        # 진행 상황 업데이트: 검색 시작
        manager.update_progress(task_id, CollectionProgress(
            status="searching",
            current_step="ArXiv에서 논문을 검색하고 있습니다...",
            progress_percentage=10
        ))

        api_logger.info(f"논문 수집 프로세스 시작 - Task: {task_id}")
        api_logger.info(f"수집 파라미터 상세:")
        api_logger.info(f"  - categories: {request.categories}")
        api_logger.info(f"  - days_back: {request.days_back}")
        api_logger.info(f"  - keywords: {request.keywords}")
        api_logger.info(f"  - search_mode: {request.search_mode}")
        api_logger.info(f"  - start_date: {request.start_date}")
        api_logger.info(f"  - end_date: {request.end_date}")
        api_logger.info(f"  - keyword_only: {request.search_mode == 'keyword-only'}")
        
        # 중단 플래그를 확인하는 콜백 함수
        def progress_callback_with_cancellation(progress):
            # 중단 요청이 있는지 확인
            if manager.is_cancelled(task_id):
                api_logger.info(f"작업 중단 감지 - Task ID: {task_id}")
                raise Exception("작업이 사용자에 의해 중단되었습니다.")
            manager.update_progress(task_id, progress)
        
        # 실제 논문 수집 실행
        report_result = await service.process_papers(
            categories=request.categories if request.categories else None,
            days_back=request.days_back,
            keywords=request.keywords if request.keywords else None,
            keyword_only=(request.search_mode == "keyword-only"),
            start_date=request.start_date,
            end_date=request.end_date,
            target_language=request.target_language,
            progress_callback=progress_callback_with_cancellation
        )

        # 반환값 처리 (튜플 또는 단일 값)
        if isinstance(report_result, tuple):
            report_path, papers_collected = report_result
        else:
            # 이전 버전 호환성
            report_path = report_result
            papers_collected = 0

        processing_time = time.time() - start_time
        api_logger.info(f"논문 수집 완료 - Task: {task_id}, 처리 시간: {processing_time:.2f}초, 수집된 논문: {papers_collected}개, 보고서: {report_path}")

        # 성공 결과 저장
        result = CollectionResult(
            success=True,
            message="논문 수집이 성공적으로 완료되었습니다.",
            papers_collected=papers_collected,  # 실제 수집된 논문 수
            report_path=report_path,
            processing_time=processing_time
        )

        manager.complete_task(task_id, result)

    except Exception as e:
        processing_time = time.time() - start_time
        error_message = str(e)
        
        # 중단된 경우와 실제 오류를 구분
        if "중단되었습니다" in error_message:
            api_logger.info(f"작업 중단 완료 - Task: {task_id}, 처리 시간: {processing_time:.2f}초")
            
            # 중단 결과 저장
            result = CollectionResult(
                success=False,
                message="작업이 사용자에 의해 중단되었습니다.",
                papers_collected=0,
                processing_time=processing_time,
                error_details="User cancelled"
            )
            manager.complete_task(task_id, result)
            
            # 중단 상태로 업데이트
            manager.update_progress(task_id, CollectionProgress(
                status="cancelled",
                current_step="작업이 성공적으로 중단되었습니다.",
                progress_percentage=100
            ))
        else:
            api_logger.error(f"논문 수집 실패 - Task: {task_id}, 처리 시간: {processing_time:.2f}초, 오류: {error_message}")

            # 실패 결과 저장
            result = CollectionResult(
                success=False,
                message="논문 수집 중 오류가 발생했습니다.",
                papers_collected=0,
                processing_time=processing_time,
                error_details=error_message
            )

            manager.complete_task(task_id, result)

            # 에러 진행 상황 업데이트
            manager.update_progress(task_id, CollectionProgress(
                status="error",
                current_step="오류가 발생했습니다.",
                progress_percentage=100,
                error_message=error_message
            ))


@app.get("/")
async def root():
    """API 루트 엔드포인트"""
    return {
        "message": "AI Frontier API Server",
        "version": "1.0.0",
        "status": "running"
    }


@app.post("/api/collect", response_model=Dict[str, str])
async def start_collection(
    request: PaperCollectionRequest,
    client_request: Request
):
    """논문 수집 시작"""
    client_ip = client_request.client.host
    api_logger.info(f"논문 수집 요청 시작 - IP: {client_ip}")
    api_logger.info(f"요청 파라미터: {request.dict()}")
    
    try:
        # 새 작업 생성
        task_id = manager.create_task(request)
        api_logger.info(f"새 작업 생성 완료 - Task ID: {task_id}")

        # 백그라운드 작업 시작 (Thread Pool에서 실행)
        executor.submit(collect_papers_sync, task_id, request)
        api_logger.info(f"백그라운드 작업 시작됨 (Thread Pool) - Task ID: {task_id}")

        return {"task_id": task_id, "message": "논문 수집이 시작되었습니다."}

    except Exception as e:
        api_logger.error(f"수집 시작 실패 - IP: {client_ip}, 오류: {str(e)}")
        raise HTTPException(status_code=500, detail=f"수집 시작 실패: {str(e)}")


@app.get("/api/status/{task_id}", response_model=CollectionStatus)
async def get_collection_status(task_id: str, client_request: Request):
    """논문 수집 상태 조회"""
    client_ip = client_request.client.host
    
    status = manager.get_task(task_id)
    if not status:
        api_logger.warning(f"작업 상태 조회 실패 - Task ID: {task_id}, IP: {client_ip} (작업 없음)")
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")

    # 상태 변경이 있을 때만 로깅 (너무 많은 로그 방지)
    if hasattr(get_collection_status, '_last_status'):
        if get_collection_status._last_status.get(task_id) != status.status:
            api_logger.info(f"작업 상태 변경 - Task ID: {task_id}, 상태: {status.status}, 진행률: {status.progress.progress_percentage if status.progress else 0}%")
            get_collection_status._last_status[task_id] = status.status
    else:
        get_collection_status._last_status = {task_id: status.status}
        api_logger.info(f"작업 상태 조회 - Task ID: {task_id}, 상태: {status.status}")

    return status


@app.get("/api/tasks", response_model=Dict[str, Any])
async def get_all_tasks():
    """모든 작업 목록 조회"""
    return {
        "total_tasks": len(collection_tasks),
        "tasks": list(collection_tasks.keys()),
        "active_tasks": [
            task_id for task_id, status in collection_tasks.items()
            if status.status in ["created", "searching", "collecting", "processing"]
        ]
    }


@app.get("/api/download/{task_id}")
async def download_report(task_id: str):
    """생성된 보고서 다운로드"""
    status = manager.get_task(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")

    if not status.result or not status.result.success:
        raise HTTPException(status_code=400, detail="수집이 완료되지 않았거나 실패했습니다.")

    if not status.result.report_path:
        raise HTTPException(status_code=404, detail="보고서 파일을 찾을 수 없습니다.")

    return FileResponse(
        path=status.result.report_path,
        filename=f"arxiv_report_{task_id[:8]}.md",
        media_type="text/markdown"
    )


@app.post("/api/cancel/{task_id}")
async def cancel_collection(task_id: str, client_request: Request):
    """논문 수집 작업 중단"""
    client_ip = client_request.client.host
    api_logger.info(f"작업 중단 요청 - Task ID: {task_id}, IP: {client_ip}")
    
    if not manager.get_task(task_id):
        api_logger.warning(f"작업 중단 실패 - Task ID: {task_id}, IP: {client_ip} (작업 없음)")
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")
    
    success = manager.cancel_task(task_id)
    if success:
        # 작업 상태를 중단됨으로 업데이트
        manager.update_progress(task_id, CollectionProgress(
            status="cancelled",
            current_step="작업이 사용자에 의해 중단되었습니다.",
            progress_percentage=0
        ))
        api_logger.info(f"작업 중단 성공 - Task ID: {task_id}")
        return {"message": "작업이 중단되었습니다.", "task_id": task_id}
    else:
        api_logger.error(f"작업 중단 실패 - Task ID: {task_id}")
        raise HTTPException(status_code=400, detail="작업을 중단할 수 없습니다.")


@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: str):
    """작업 삭제"""
    if task_id not in collection_tasks:
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")

    del collection_tasks[task_id]
    return {"message": "작업이 삭제되었습니다."}


@app.get("/api/files")
async def get_paper_files():
    """생성된 논문 파일 목록 조회"""
    import os
    from pathlib import Path
    import re
    from datetime import datetime
    
    try:
        # 개별 논문 파일 디렉토리 확인
        papers_dir = Path("reports/individual_papers")
        if not papers_dir.exists():
            return {"files": [], "total": 0}
        
        files = []
        for file_path in papers_dir.glob("*.md"):
            try:
                # 파일 정보 읽기
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 메타데이터 추출 (간단한 파싱)
                title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
                korean_title_match = re.search(r'\*\*Korean Title:\*\* (.+)$', content, re.MULTILINE)
                keywords_match = re.search(r'## 🏷️ 키워드\n\n(.+)', content, re.MULTILINE | re.DOTALL)
                authors_match = re.search(r'- \*\*Authors:\*\* (.+)$', content, re.MULTILINE)
                arxiv_id_match = re.search(r'- \*\*ArXiv ID:\*\* \[(.+?)\]', content)
                published_match = re.search(r'- \*\*Published:\*\* (.+)$', content, re.MULTILINE)
                category_match = re.search(r'- \*\*Category:\*\* (.+)$', content, re.MULTILINE)
                
                # 키워드 파싱
                keywords = []
                if keywords_match:
                    keywords_text = keywords_match.group(1).split('\n')[0]
                    keywords = [kw.strip('`').strip() for kw in keywords_text.split('•') if kw.strip() and 'keyword' not in kw.lower()]
                
                file_info = {
                    "filename": file_path.name,
                    "title": title_match.group(1) if title_match else file_path.stem,
                    "title_ko": korean_title_match.group(1) if korean_title_match else "",
                    "authors": authors_match.group(1).split(', ') if authors_match else [],
                    "arxiv_id": arxiv_id_match.group(1) if arxiv_id_match else "",
                    "published": published_match.group(1) if published_match else "",
                    "category": category_match.group(1) if category_match else "",
                    "keywords": keywords,
                    "file_size": file_path.stat().st_size,
                    "created_at": datetime.fromtimestamp(file_path.stat().st_ctime).isoformat(),
                    "modified_at": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                    "pdf_url": f"https://arxiv.org/pdf/{arxiv_id_match.group(1)}.pdf" if arxiv_id_match else "",
                    "arxiv_url": f"https://arxiv.org/abs/{arxiv_id_match.group(1)}" if arxiv_id_match else ""
                }
                files.append(file_info)
                
            except Exception as e:
                api_logger.error(f"파일 파싱 오류 - {file_path}: {str(e)}")
                continue
        
        # 수정 시간 기준으로 정렬 (최신순)
        files.sort(key=lambda x: x['modified_at'], reverse=True)
        
        api_logger.info(f"논문 파일 목록 조회 완료: {len(files)}개 파일")
        return {"files": files, "total": len(files)}
        
    except Exception as e:
        api_logger.error(f"논문 파일 목록 조회 실패: {str(e)}")
        raise HTTPException(status_code=500, detail=f"파일 목록 조회 실패: {str(e)}")


@app.get("/api/files/{filename}")
async def get_paper_file(filename: str):
    """특정 논문 파일 내용 조회"""
    from pathlib import Path
    
    try:
        papers_dir = Path("reports/individual_papers")
        file_path = papers_dir / filename
        
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {"filename": filename, "content": content}
        
    except HTTPException:
        raise
    except Exception as e:
        api_logger.error(f"파일 조회 실패 - {filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"파일 조회 실패: {str(e)}")


@app.post("/api/digest/daily")
async def generate_daily_digest(date: str = None):
    """일일 다이제스트 생성"""
    try:
        from datetime import datetime

        # Parse target date
        if date:
            try:
                target_date = datetime.strptime(date, "%Y%m%d")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date format. Expected YYYYMMDD.")
        else:
            target_date = datetime.now()

        # Create digest generator
        digest_generator = DigestGenerator()

        # Generate and save digest
        digest_path = digest_generator.save_daily_digest(target_date)

        # Send notifications only if not already sent by webhook
        # Check if digest was created in the last minute (to avoid duplicate sends)
        import os
        from datetime import datetime, timedelta

        try:
            file_stat = os.path.getmtime(digest_path)
            file_time = datetime.fromtimestamp(file_stat)
            time_diff = datetime.now() - file_time

            # If file was created more than 1 minute ago, send notifications
            if time_diff > timedelta(minutes=1):
                notification_results = notification_manager.send_digest_notifications(
                    digest_file_path=digest_path,
                    digest_type="daily",
                    digest_date=target_date.strftime("%Y-%m-%d")
                )
                api_logger.info(f"Daily digest notifications sent: {notification_results}")
            else:
                api_logger.info("Daily digest was recently created - skipping duplicate notifications")
        except Exception as e:
            api_logger.error(f"Failed to send daily digest notifications: {e}")

        return {
            "success": True,
            "message": "Daily digest generated successfully",
            "digest_path": str(digest_path),
            "date": target_date.strftime("%Y-%m-%d")
        }

    except HTTPException:
        raise
    except Exception as e:
        api_logger.error(f"Daily digest generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/digest/weekly")
async def generate_weekly_digest(date: str = None):
    """주간 다이제스트 생성"""
    try:
        from datetime import datetime

        # Parse target date
        if date:
            try:
                target_date = datetime.strptime(date, "%Y%m%d")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date format. Expected YYYYMMDD.")
        else:
            target_date = datetime.now()

        # Create digest generator
        digest_generator = DigestGenerator()

        # Generate and save digest
        digest_path = digest_generator.save_weekly_digest(target_date)

        # Send notifications
        try:
            notification_results = notification_manager.send_digest_notifications(
                digest_file_path=digest_path,
                digest_type="weekly",
                digest_date=target_date.strftime("%Y-%m-%d")
            )
            api_logger.info(f"Weekly digest notifications sent: {notification_results}")
        except Exception as e:
            api_logger.error(f"Failed to send weekly digest notifications: {e}")

        return {
            "success": True,
            "message": "Weekly digest generated successfully",
            "digest_path": str(digest_path),
            "date": target_date.strftime("%Y-%m-%d")
        }

    except HTTPException:
        raise
    except Exception as e:
        api_logger.error(f"Weekly digest generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/digests")
async def list_digests():
    """생성된 다이제스트 목록 조회"""
    try:
        from pathlib import Path

        digests_dir = Path("reports/digests")
        digests = []

        if digests_dir.exists():
            for file_path in digests_dir.glob("*.md"):
                try:
                    digest_info = {
                        "filename": file_path.name,
                        "path": str(file_path),
                        "modified_at": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        "size": file_path.stat().st_size
                    }

                    # Determine type from filename
                    if "daily" in file_path.name:
                        digest_info["type"] = "daily"
                    elif "weekly" in file_path.name:
                        digest_info["type"] = "weekly"
                    else:
                        digest_info["type"] = "unknown"

                    digests.append(digest_info)

                except Exception as e:
                    api_logger.error(f"Error processing digest file {file_path}: {e}")
                    continue

        # Sort by modification time (newest first)
        digests.sort(key=lambda x: x['modified_at'], reverse=True)

        return {"digests": digests, "total": len(digests)}

    except Exception as e:
        api_logger.error(f"Failed to list digests: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Notification API endpoints
@app.post("/api/notifications/email/subscribe", response_model=dict)
async def subscribe_email(request: EmailSubscribeRequest):
    """이메일 구독 추가"""
    try:
        success = notification_manager.add_email_subscriber(
            request.email, request.digest_type
        )
        if success:
            return {"success": True, "message": f"Successfully subscribed {request.email} to {request.digest_type} digest"}
        else:
            return {"success": False, "message": "Email already subscribed"}
    except Exception as e:
        api_logger.error(f"Failed to subscribe email: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/notifications/email/unsubscribe", response_model=dict)
async def unsubscribe_email(request: EmailUnsubscribeRequest):
    """이메일 구독 해제"""
    try:
        success = notification_manager.remove_email_subscriber(
            request.email, request.digest_type
        )
        if success:
            return {"success": True, "message": f"Successfully unsubscribed {request.email} from {request.digest_type} digest"}
        else:
            return {"success": False, "message": "Email not found in subscription list"}
    except Exception as e:
        api_logger.error(f"Failed to unsubscribe email: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/notifications/email/subscribers", response_model=MailingListResponse)
async def get_email_subscribers():
    """메일링 리스트 조회"""
    try:
        daily_subscribers = notification_manager.get_email_subscribers("daily")
        weekly_subscribers = notification_manager.get_email_subscribers("weekly")

        return MailingListResponse(
            daily_subscribers=daily_subscribers,
            weekly_subscribers=weekly_subscribers
        )
    except Exception as e:
        api_logger.error(f"Failed to get email subscribers: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# 키워드 구독 관리 API
# =============================================================================

@app.post("/api/notifications/keywords/subscribe", response_model=KeywordSubscriptionResponse)
async def subscribe_keywords(request: KeywordSubscribeRequest):
    """키워드 기반 이메일 구독"""
    try:
        success = keyword_subscription_manager.add_subscription(
            email=str(request.email),
            keywords=request.keywords,
            digest_type=request.digest_type
        )

        if success:
            subscription = keyword_subscription_manager.get_subscription(str(request.email))
            return KeywordSubscriptionResponse(
                success=True,
                message="키워드 구독이 성공적으로 추가/업데이트되었습니다.",
                subscription=KeywordSubscriptionInfo(
                    email=subscription.email,
                    keywords=subscription.keywords,
                    digest_type=subscription.digest_type,
                    created_at=subscription.created_at,
                    updated_at=subscription.updated_at,
                    active=subscription.active
                )
            )
        else:
            return KeywordSubscriptionResponse(
                success=False,
                message="키워드 구독 추가/업데이트에 실패했습니다."
            )
    except Exception as e:
        api_logger.error(f"Failed to subscribe keywords: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/notifications/keywords/unsubscribe", response_model=KeywordSubscriptionResponse)
async def unsubscribe_keywords(email: str):
    """키워드 구독 해제"""
    try:
        success = keyword_subscription_manager.remove_subscription(email)

        if success:
            return KeywordSubscriptionResponse(
                success=True,
                message="키워드 구독이 성공적으로 해제되었습니다."
            )
        else:
            return KeywordSubscriptionResponse(
                success=False,
                message="해당 이메일의 구독을 찾을 수 없습니다."
            )
    except Exception as e:
        api_logger.error(f"Failed to unsubscribe keywords: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/notifications/keywords/subscription/{email}", response_model=KeywordSubscriptionResponse)
async def get_keyword_subscription(email: str):
    """특정 사용자의 키워드 구독 정보 조회"""
    try:
        subscription = keyword_subscription_manager.get_subscription(email)

        if subscription:
            return KeywordSubscriptionResponse(
                success=True,
                message="구독 정보를 성공적으로 조회했습니다.",
                subscription=KeywordSubscriptionInfo(
                    email=subscription.email,
                    keywords=subscription.keywords,
                    digest_type=subscription.digest_type,
                    created_at=subscription.created_at,
                    updated_at=subscription.updated_at,
                    active=subscription.active
                )
            )
        else:
            return KeywordSubscriptionResponse(
                success=False,
                message="해당 이메일의 구독을 찾을 수 없습니다."
            )
    except Exception as e:
        api_logger.error(f"Failed to get keyword subscription: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/notifications/keywords/subscribers", response_model=KeywordSubscriptionsResponse)
async def get_keyword_subscribers(digest_type: str = None):
    """키워드 구독자 목록 조회"""
    try:
        subscriptions = keyword_subscription_manager.get_all_subscriptions(digest_type=digest_type)

        subscription_infos = [
            KeywordSubscriptionInfo(
                email=sub.email,
                keywords=sub.keywords,
                digest_type=sub.digest_type,
                created_at=sub.created_at,
                updated_at=sub.updated_at,
                active=sub.active
            )
            for sub in subscriptions
        ]

        return KeywordSubscriptionsResponse(
            subscriptions=subscription_infos,
            total_count=len(subscription_infos)
        )
    except Exception as e:
        api_logger.error(f"Failed to get keyword subscribers: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/notifications/status", response_model=NotificationStatus)
async def get_notification_status():
    """알림 서비스 상태 조회"""
    try:
        status = notification_manager.get_notification_status()
        return NotificationStatus(**status)
    except Exception as e:
        api_logger.error(f"Failed to get notification status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/notifications/test", response_model=dict)
async def test_notifications(request: NotificationTestRequest):
    """알림 서비스 연결 테스트"""
    try:
        results = {}

        if request.test_email:
            results["email"] = notification_manager.email_service.test_connection()

        if request.test_slack:
            results["slack"] = notification_manager.slack_service.test_connection()

        if request.test_webhooks:
            results["webhooks"] = notification_manager.webhook_service.test_webhooks()

        return {
            "success": True,
            "results": results,
            "message": "Test completed"
        }
    except Exception as e:
        api_logger.error(f"Failed to test notifications: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/notifications/send/digest", response_model=NotificationResult)
async def send_digest_notifications(
    digest_file: str,
    digest_type: str = "daily",
    digest_date: str = None,
    settings: NotificationSettingsRequest = None
):
    """다이제스트 알림 전송"""
    try:
        from pathlib import Path

        digest_path = Path(digest_file)
        if not digest_path.exists():
            raise HTTPException(status_code=404, detail="Digest file not found")

        # 알림 전송 설정
        send_email = settings.send_email if settings else None
        send_slack = settings.send_slack if settings else None
        send_webhooks = settings.send_webhooks if settings else True
        custom_recipients = settings.custom_email_recipients if settings else None

        # 알림 전송
        results = notification_manager.send_digest_notifications(
            digest_file_path=digest_path,
            digest_type=digest_type,
            digest_date=digest_date,
            send_email=send_email,
            send_slack=send_slack,
            send_webhooks=send_webhooks,
            custom_email_recipients=custom_recipients
        )

        return NotificationResult(**results)

    except Exception as e:
        api_logger.error(f"Failed to send digest notifications: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# RAG Search API endpoints
@app.post("/api/search/papers", response_model=PaperSearchResponse)
async def search_papers(request: PaperSearchRequest):
    """벡터 검색을 통한 논문 검색"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG search service not available")

        # Parse dates if provided
        start_date = None
        end_date = None

        if request.start_date:
            try:
                from datetime import datetime
                start_date = datetime.strptime(request.start_date, "%Y-%m-%d").date()
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid start_date format. Use YYYY-MM-DD")

        if request.end_date:
            try:
                from datetime import datetime
                end_date = datetime.strptime(request.end_date, "%Y-%m-%d").date()
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid end_date format. Use YYYY-MM-DD")

        # Perform search
        results = rag_service.search_papers(
            query=request.query,
            top_k=request.top_k,
            min_similarity=request.min_similarity,
            categories=request.categories,
            start_date=start_date,
            end_date=end_date,
            page=request.page,
            page_size=request.page_size
        )

        api_logger.info(f"Paper search completed: '{request.query}' -> {results['total_results']} results")
        return PaperSearchResponse(**results)

    except HTTPException:
        raise
    except Exception as e:
        api_logger.error(f"Paper search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/search/similar", response_model=SimilarPapersResponse)
async def find_similar_papers(request: SimilarPapersRequest):
    """특정 논문과 유사한 논문 검색"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG search service not available")

        results = rag_service.find_similar_papers(
            arxiv_id=request.arxiv_id,
            top_k=request.top_k,
            min_similarity=request.min_similarity
        )

        api_logger.info(f"Similar papers search completed: {request.arxiv_id} -> {results['total_found']} results")
        return SimilarPapersResponse(**results)

    except Exception as e:
        api_logger.error(f"Similar papers search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/stats", response_model=DatabaseStatsResponse)
async def get_search_stats():
    """벡터 데이터베이스 통계 조회"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG search service not available")

        stats = rag_service.get_database_stats()
        return DatabaseStatsResponse(**stats)

    except Exception as e:
        api_logger.error(f"Failed to get search stats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/suggestions")
async def get_query_suggestions(query: str):
    """검색 쿼리 개선 제안"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG search service not available")

        suggestions = rag_service.suggest_query_improvements(query)
        return {"query": query, "suggestions": suggestions}

    except Exception as e:
        api_logger.error(f"Failed to get query suggestions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Hybrid Search API endpoints
@app.post("/api/search/hybrid", response_model=HybridSearchResponse)
async def hybrid_search(request: HybridSearchRequest):
    """하이브리드 검색 (BM25 + 벡터 검색)"""
    try:
        if not hybrid_service:
            raise HTTPException(status_code=503, detail="Hybrid search service not available")

        # Parse dates if provided
        start_date = None
        end_date = None

        if request.start_date:
            try:
                from datetime import datetime
                start_date = datetime.strptime(request.start_date, "%Y-%m-%d").date()
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid start_date format. Use YYYY-MM-DD")

        if request.end_date:
            try:
                from datetime import datetime
                end_date = datetime.strptime(request.end_date, "%Y-%m-%d").date()
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid end_date format. Use YYYY-MM-DD")

        # Perform hybrid search
        results = hybrid_service.hybrid_search(
            query=request.query,
            keyword_weight=request.keyword_weight,
            vector_weight=request.vector_weight,
            top_k=request.top_k,
            min_similarity=request.min_similarity,
            categories=request.categories,
            start_date=start_date,
            end_date=end_date,
            page=request.page,
            page_size=request.page_size
        )

        api_logger.info(f"Hybrid search completed: '{request.query}' (kw:{request.keyword_weight:.2f}, vec:{request.vector_weight:.2f}) -> {results['total_results']} results")
        return HybridSearchResponse(**results)

    except HTTPException:
        raise
    except Exception as e:
        api_logger.error(f"Hybrid search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/hybrid/stats", response_model=HybridStatsResponse)
async def get_hybrid_search_stats():
    """하이브리드 검색 서비스 통계 조회"""
    try:
        if not hybrid_service:
            raise HTTPException(status_code=503, detail="Hybrid search service not available")

        stats = hybrid_service.get_search_stats()
        return HybridStatsResponse(**stats)

    except Exception as e:
        api_logger.error(f"Failed to get hybrid search stats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "active_tasks": len([
            t for t in collection_tasks.values()
            if t.status in ["created", "searching", "collecting", "processing"]
        ])
    }


def run_server(host: str = "localhost", port: int = 8080):
    """서버 실행"""
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()