"""Task manager for handling background tasks."""

import uuid
import time
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass
from .models import CollectionProgress


@dataclass
class Task:
    """Task data structure."""
    task_id: str
    request_data: Dict[str, Any]
    progress: CollectionProgress
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class TaskManager:
    """Simple task manager for webhook operations."""

    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.cancellation_flags: Dict[str, bool] = {}

    def create_task(self, task_id: str, request_data: Dict[str, Any]) -> str:
        """Create a new task."""
        progress = CollectionProgress(
            status="pending",
            current_step="작업이 생성되었습니다.",
            papers_found=0,
            papers_processed=0,
            progress_percentage=0
        )

        task = Task(
            task_id=task_id,
            request_data=request_data,
            progress=progress,
            started_at=datetime.now()
        )

        self.tasks[task_id] = task
        self.cancellation_flags[task_id] = False
        return task_id

    def update_progress(self, task_id: str, progress: CollectionProgress):
        """Update task progress."""
        if task_id in self.tasks:
            self.tasks[task_id].progress = progress

    def complete_task(self, task_id: str, result: Dict[str, Any]):
        """Mark task as completed."""
        if task_id in self.tasks:
            self.tasks[task_id].result = result
            self.tasks[task_id].completed_at = datetime.now()
            self.tasks[task_id].progress.status = "completed"

    def fail_task(self, task_id: str, error: str):
        """Mark task as failed."""
        if task_id in self.tasks:
            self.tasks[task_id].error = error
            self.tasks[task_id].completed_at = datetime.now()
            self.tasks[task_id].progress.status = "failed"

    def cancel_task(self, task_id: str):
        """Cancel a task."""
        if task_id in self.cancellation_flags:
            self.cancellation_flags[task_id] = True
        if task_id in self.tasks:
            self.tasks[task_id].progress.status = "cancelled"

    def is_cancelled(self, task_id: str) -> bool:
        """Check if task is cancelled."""
        return self.cancellation_flags.get(task_id, False)

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get task by ID."""
        return self.tasks.get(task_id)

    def delete_task(self, task_id: str):
        """Delete a task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
        if task_id in self.cancellation_flags:
            del self.cancellation_flags[task_id]

    def list_tasks(self) -> Dict[str, Task]:
        """List all tasks."""
        return self.tasks.copy()