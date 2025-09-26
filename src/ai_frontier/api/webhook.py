"""Webhook endpoints for automation tools like n8n."""

import asyncio
import uuid
import time
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field

from ..main import ArxivReportingService
from .models import CollectionProgress
from .task_manager import TaskManager

# Get logger
logger = logging.getLogger("webhook")

router = APIRouter(prefix="/webhook", tags=["webhook"])

# Task manager for webhook tasks
webhook_task_manager = TaskManager()


class WebhookCollectionRequest(BaseModel):
    """Simplified request model for webhook-based paper collection."""
    keywords: List[str] = Field(default=[], description="Keywords to search for")
    categories: List[str] = Field(default=["cs.AI", "cs.LG", "cs.CL", "cs.CV"], description="ArXiv categories")
    days_back: int = Field(default=1, description="Number of days back to search")
    start_date: Optional[str] = Field(default=None, description="Start date (YYYYMMDD)")
    end_date: Optional[str] = Field(default=None, description="End date (YYYYMMDD)")
    keyword_only: bool = Field(default=False, description="Search only by keywords")
    translation_provider: str = Field(default="openai", description="Translation provider")
    summarization_provider: str = Field(default="openai", description="Summarization provider")
    callback_url: Optional[str] = Field(default=None, description="URL to call when completed")
    use_rss: bool = Field(default=False, description="Use RSS feeds instead of ArXiv API")


class WebhookResponse(BaseModel):
    """Response model for webhook endpoints."""
    success: bool
    task_id: str
    message: str
    estimated_completion_minutes: Optional[int] = None


class WebhookTaskStatus(BaseModel):
    """Task status for webhook endpoints."""
    task_id: str
    status: str  # pending, running, completed, failed
    progress_percentage: int
    current_step: str
    papers_found: int
    papers_processed: int
    result_files: List[str] = Field(default=[])
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


async def webhook_collection_task(
    task_id: str,
    request: WebhookCollectionRequest,
    callback_url: Optional[str] = None
):
    """Background task for webhook-based paper collection."""
    try:
        logger.info(f"Webhook task {task_id} started")

        # Update task status to running
        webhook_task_manager.update_progress(task_id, CollectionProgress(
            status="running",
            current_step="논문 수집 시작",
            papers_found=0,
            papers_processed=0,
            progress_percentage=0
        ))

        # Create service instance
        service = ArxivReportingService(
            translation_provider=request.translation_provider,
            summarization_provider=request.summarization_provider,
            output_dir="reports"
        )

        # Progress callback for webhook task
        def progress_callback(progress: CollectionProgress):
            webhook_task_manager.update_progress(task_id, progress)

        # Execute paper collection
        report_path = await service.process_papers(
            categories=request.categories if request.categories else None,
            days_back=request.days_back,
            keywords=request.keywords if request.keywords else None,
            keyword_only=request.keyword_only,
            start_date=request.start_date,
            end_date=request.end_date,
            progress_callback=progress_callback
        )

        # Update final status
        final_progress = CollectionProgress(
            status="completed",
            current_step="논문 수집 완료",
            papers_found=webhook_task_manager.tasks[task_id].progress.papers_found,
            papers_processed=webhook_task_manager.tasks[task_id].progress.papers_processed,
            progress_percentage=100
        )
        webhook_task_manager.update_progress(task_id, final_progress)

        # Store result files
        import os
        result_files = []
        reports_dir = "reports/individual_papers"
        if os.path.exists(reports_dir):
            result_files = [f for f in os.listdir(reports_dir) if f.endswith('.md')]

        webhook_task_manager.complete_task(task_id, {
            "report_path": str(report_path),
            "result_files": result_files,
            "papers_collected": final_progress.papers_processed
        })

        logger.info(f"Webhook task {task_id} completed successfully")

        # Call callback URL if provided
        if callback_url:
            try:
                import requests
                callback_data = {
                    "task_id": task_id,
                    "status": "completed",
                    "report_path": str(report_path),
                    "papers_collected": final_progress.papers_processed
                }
                requests.post(callback_url, json=callback_data, timeout=30)
                logger.info(f"Callback sent to {callback_url}")
            except Exception as e:
                logger.error(f"Failed to send callback: {e}")

    except Exception as e:
        logger.error(f"Webhook task {task_id} failed: {e}")

        # Update task status to failed
        webhook_task_manager.update_progress(task_id, CollectionProgress(
            status="failed",
            current_step=f"오류 발생: {str(e)}",
            papers_found=0,
            papers_processed=0,
            progress_percentage=0
        ))

        webhook_task_manager.fail_task(task_id, str(e))

        # Call callback URL with error if provided
        if callback_url:
            try:
                import requests
                callback_data = {
                    "task_id": task_id,
                    "status": "failed",
                    "error": str(e)
                }
                requests.post(callback_url, json=callback_data, timeout=30)
            except Exception as callback_error:
                logger.error(f"Failed to send error callback: {callback_error}")


@router.post("/collect", response_model=WebhookResponse)
async def webhook_collect_papers(
    request: WebhookCollectionRequest,
    background_tasks: BackgroundTasks
):
    """
    Start paper collection for automation tools.

    This endpoint is designed for automation tools like n8n.
    It returns immediately with a task ID and processes papers in the background.
    """
    try:
        # Generate task ID
        task_id = str(uuid.uuid4())

        # Estimate completion time based on parameters
        estimated_papers = 50 if not request.keywords else len(request.keywords) * 20
        estimated_minutes = max(5, estimated_papers // 10)  # Rough estimate

        # Initialize task
        webhook_task_manager.create_task(task_id, {
            "keywords": request.keywords,
            "categories": request.categories,
            "days_back": request.days_back,
            "start_date": request.start_date,
            "end_date": request.end_date
        })

        # Start background task
        background_tasks.add_task(
            webhook_collection_task,
            task_id,
            request,
            request.callback_url
        )

        logger.info(f"Webhook collection started with task ID: {task_id}")

        return WebhookResponse(
            success=True,
            task_id=task_id,
            message="Paper collection started successfully",
            estimated_completion_minutes=estimated_minutes
        )

    except Exception as e:
        logger.error(f"Failed to start webhook collection: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status/{task_id}", response_model=WebhookTaskStatus)
async def get_webhook_task_status(task_id: str):
    """Get the status of a webhook task."""
    try:
        if task_id not in webhook_task_manager.tasks:
            raise HTTPException(status_code=404, detail="Task not found")

        task = webhook_task_manager.tasks[task_id]

        # Get result files if completed
        result_files = []
        if task.result and "result_files" in task.result:
            result_files = task.result["result_files"]

        return WebhookTaskStatus(
            task_id=task_id,
            status=task.progress.status,
            progress_percentage=task.progress.progress_percentage,
            current_step=task.progress.current_step,
            papers_found=task.progress.papers_found,
            papers_processed=task.progress.papers_processed,
            result_files=result_files,
            error_message=task.error,
            started_at=task.started_at,
            completed_at=task.completed_at
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get task status: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/collect-sync", response_model=Dict)
async def webhook_collect_papers_sync(request: WebhookCollectionRequest):
    """
    Synchronous paper collection for simple automation.

    This endpoint waits for completion and returns the results directly.
    Use this for simple automations that can wait for the result.
    """
    try:
        logger.info("Starting synchronous webhook collection")

        # Create service instance
        service = ArxivReportingService(
            translation_provider=request.translation_provider,
            summarization_provider=request.summarization_provider,
            output_dir="reports"
        )

        # Execute paper collection
        report_path = await service.process_papers(
            categories=request.categories if request.categories else None,
            days_back=request.days_back,
            keywords=request.keywords if request.keywords else None,
            keyword_only=request.keyword_only,
            start_date=request.start_date,
            end_date=request.end_date
        )

        # Get result files
        import os
        result_files = []
        reports_dir = "reports/individual_papers"
        if os.path.exists(reports_dir):
            result_files = [f for f in os.listdir(reports_dir) if f.endswith('.md')]

        logger.info("Synchronous webhook collection completed")

        return {
            "success": True,
            "message": "Paper collection completed successfully",
            "report_path": str(report_path),
            "result_files": result_files,
            "papers_collected": len(result_files)
        }

    except Exception as e:
        logger.error(f"Synchronous webhook collection failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/task/{task_id}")
async def delete_webhook_task(task_id: str):
    """Delete a webhook task and its data."""
    try:
        if task_id not in webhook_task_manager.tasks:
            raise HTTPException(status_code=404, detail="Task not found")

        webhook_task_manager.delete_task(task_id)

        return {"success": True, "message": "Task deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete task: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tasks")
async def list_webhook_tasks():
    """List all webhook tasks."""
    try:
        tasks = []
        for task_id, task in webhook_task_manager.tasks.items():
            tasks.append({
                "task_id": task_id,
                "status": task.progress.status,
                "started_at": task.started_at,
                "completed_at": task.completed_at,
                "papers_processed": task.progress.papers_processed
            })

        return {"tasks": tasks}

    except Exception as e:
        logger.error(f"Failed to list tasks: {e}")
        raise HTTPException(status_code=500, detail=str(e))


class WebhookDigestRequest(BaseModel):
    """Digest request model for webhook endpoints."""
    digest_type: str = Field(description="Type: daily or weekly")
    date: Optional[str] = Field(default=None, description="Date in YYYYMMDD format")
    translation_provider: str = Field(default="openai", description="Translation provider")
    summarization_provider: str = Field(default="openai", description="Summarization provider")
    callback_url: Optional[str] = Field(default=None, description="URL to call when completed")


@router.post("/digest/daily")
async def webhook_generate_daily_digest(request: WebhookDigestRequest = None):
    """
    Generate daily digest for automation tools.

    This is a synchronous endpoint that generates and returns the digest.
    """
    try:
        from datetime import datetime
        from ..summarization.digest import DigestGenerator

        # Parse request if provided
        target_date = datetime.now()
        translation_provider = "openai"
        summarization_provider = "openai"

        if request:
            if request.date:
                try:
                    target_date = datetime.strptime(request.date, "%Y%m%d")
                except ValueError:
                    raise HTTPException(status_code=400, detail="Invalid date format. Expected YYYYMMDD.")
            translation_provider = request.translation_provider
            summarization_provider = request.summarization_provider

        logger.info(f"Generating daily digest for {target_date.strftime('%Y-%m-%d')}")

        # Create digest generator
        digest_generator = DigestGenerator(
            translation_provider=translation_provider,
            summarization_provider=summarization_provider
        )

        # Generate and save digest
        digest_path = digest_generator.save_daily_digest(target_date)

        result = {
            "success": True,
            "message": "Daily digest generated successfully",
            "digest_path": str(digest_path),
            "date": target_date.strftime("%Y-%m-%d"),
            "digest_type": "daily"
        }

        # Call callback URL if provided
        if request and request.callback_url:
            try:
                import httpx
                async with httpx.AsyncClient() as client:
                    await client.post(request.callback_url, json=result)
            except Exception as e:
                logger.warning(f"Failed to call callback URL: {e}")

        logger.info("Daily digest generated successfully")
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Daily digest generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/digest/weekly")
async def webhook_generate_weekly_digest(request: WebhookDigestRequest = None):
    """
    Generate weekly digest for automation tools.

    This is a synchronous endpoint that generates and returns the digest.
    """
    try:
        from datetime import datetime
        from ..summarization.digest import DigestGenerator

        # Parse request if provided
        target_date = datetime.now()
        translation_provider = "openai"
        summarization_provider = "openai"

        if request:
            if request.date:
                try:
                    target_date = datetime.strptime(request.date, "%Y%m%d")
                except ValueError:
                    raise HTTPException(status_code=400, detail="Invalid date format. Expected YYYYMMDD.")
            translation_provider = request.translation_provider
            summarization_provider = request.summarization_provider

        logger.info(f"Generating weekly digest for {target_date.strftime('%Y-%m-%d')}")

        # Create digest generator
        digest_generator = DigestGenerator(
            translation_provider=translation_provider,
            summarization_provider=summarization_provider
        )

        # Generate and save digest
        digest_path = digest_generator.save_weekly_digest(target_date)

        result = {
            "success": True,
            "message": "Weekly digest generated successfully",
            "digest_path": str(digest_path),
            "date": target_date.strftime("%Y-%m-%d"),
            "digest_type": "weekly"
        }

        # Call callback URL if provided
        if request and request.callback_url:
            try:
                import httpx
                async with httpx.AsyncClient() as client:
                    await client.post(request.callback_url, json=result)
            except Exception as e:
                logger.warning(f"Failed to call callback URL: {e}")

        logger.info("Weekly digest generated successfully")
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Weekly digest generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/digests")
async def webhook_list_digests():
    """List all generated digests for automation tools."""
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
                    logger.error(f"Error processing digest file {file_path}: {e}")
                    continue

        # Sort by modification time (newest first)
        digests.sort(key=lambda x: x['modified_at'], reverse=True)

        return {"digests": digests, "total": len(digests)}

    except Exception as e:
        logger.error(f"Failed to list digests: {e}")
        raise HTTPException(status_code=500, detail=str(e))