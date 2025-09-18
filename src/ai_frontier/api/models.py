"""API models for AI Frontier service."""

from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class PaperCollectionRequest(BaseModel):
    """Request model for paper collection."""
    keywords: List[str] = Field(default=[], description="Keywords to search for")
    categories: List[str] = Field(default=[], description="ArXiv categories to search in")
    search_mode: str = Field(default="category", description="Search mode: category, keyword, keyword-only")
    date_mode: str = Field(default="recent", description="Date mode: recent or range")
    days_back: int = Field(default=7, description="Number of days back to search")
    start_date: Optional[str] = Field(default=None, description="Start date (YYYYMMDD)")
    end_date: Optional[str] = Field(default=None, description="End date (YYYYMMDD)")
    translation_provider: str = Field(default="openai", description="Translation service provider")
    summarization_provider: str = Field(default="openai", description="Summarization service provider")
    target_language: str = Field(default="ko", description="Target language for translation")
    use_rss: bool = Field(default=False, description="Use RSS feeds instead of ArXiv API")


class PaperInfo(BaseModel):
    """Paper information model."""
    arxiv_id: str
    title: str
    abstract: str
    authors: List[str]
    published: datetime
    pdf_url: str
    category: str
    translated_title: Optional[str] = None
    translated_abstract: Optional[str] = None
    summary: Optional[str] = None
    key_points: Optional[List[str]] = None


class CollectionProgress(BaseModel):
    """Collection progress model."""
    status: str = Field(description="Status: searching, collecting, processing, completed, error")
    current_step: str = Field(description="Current step description")
    papers_found: int = Field(default=0, description="Number of papers found")
    papers_processed: int = Field(default=0, description="Number of papers processed")
    total_papers: int = Field(default=0, description="Total papers to process")
    progress_percentage: int = Field(default=0, description="Progress percentage")
    error_message: Optional[str] = Field(default=None, description="Error message if any")


class CollectionResult(BaseModel):
    """Collection result model."""
    success: bool
    message: str
    papers_collected: int
    report_path: Optional[str] = None
    papers: Optional[List[PaperInfo]] = None
    processing_time: float
    error_details: Optional[str] = None


class CollectionStatus(BaseModel):
    """Collection status model."""
    task_id: str
    status: str
    progress: CollectionProgress
    result: Optional[CollectionResult] = None