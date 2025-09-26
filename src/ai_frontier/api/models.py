"""API models for AI Frontier service."""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr
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


class DigestRequest(BaseModel):
    """Request model for digest generation."""
    digest_type: str = Field(description="Type: daily or weekly")
    date: Optional[str] = Field(default=None, description="Date in YYYYMMDD format")
    translation_provider: str = Field(default="openai", description="Translation service provider")
    summarization_provider: str = Field(default="openai", description="Summarization service provider")


class DigestInfo(BaseModel):
    """Digest information model."""
    digest_type: str
    date: str
    file_path: str
    created_at: datetime
    papers_count: int
    summary: Optional[str] = None


class DigestResult(BaseModel):
    """Digest generation result model."""
    success: bool
    message: str
    digest_path: Optional[str] = None
    papers_count: int
    processing_time: float
    error_details: Optional[str] = None


# Notification Models
class EmailSubscribeRequest(BaseModel):
    """Request model for email subscription."""
    email: EmailStr = Field(description="Email address to subscribe")
    digest_type: str = Field(default="daily", description="Digest type: daily or weekly")


# Keyword Subscription Models
class KeywordSubscribeRequest(BaseModel):
    """Request model for keyword-based email subscription."""
    email: EmailStr = Field(description="Email address to subscribe")
    keywords: List[str] = Field(description="Keywords for personalized digest")
    digest_type: str = Field(default="daily", description="Digest type: daily or weekly")


class KeywordSubscriptionInfo(BaseModel):
    """Model for keyword subscription information."""
    email: str
    keywords: List[str]
    digest_type: str
    created_at: str
    updated_at: str
    active: bool = True


class KeywordSubscriptionsResponse(BaseModel):
    """Response model for keyword subscriptions list."""
    subscriptions: List[KeywordSubscriptionInfo]
    total_count: int


class KeywordSubscriptionResponse(BaseModel):
    """Response model for keyword subscription operation."""
    success: bool
    message: str
    subscription: Optional[KeywordSubscriptionInfo] = None


class EmailUnsubscribeRequest(BaseModel):
    """Request model for email unsubscription."""
    email: EmailStr = Field(description="Email address to unsubscribe")
    digest_type: str = Field(default="daily", description="Digest type: daily or weekly")


class NotificationSettingsRequest(BaseModel):
    """Request model for notification settings."""
    send_email: Optional[bool] = Field(default=None, description="Send email notifications")
    send_slack: Optional[bool] = Field(default=None, description="Send Slack notifications")
    send_webhooks: Optional[bool] = Field(default=True, description="Send webhook notifications")
    custom_email_recipients: Optional[List[EmailStr]] = Field(default=None, description="Custom email recipients")


class NotificationTestRequest(BaseModel):
    """Request model for notification testing."""
    test_email: bool = Field(default=False, description="Test email service")
    test_slack: bool = Field(default=False, description="Test Slack service")
    test_webhooks: bool = Field(default=False, description="Test webhook services")


class NotificationStatus(BaseModel):
    """Notification service status model."""
    auto_send_email: bool
    auto_send_slack: bool
    email_configured: bool
    slack_configured: bool
    webhooks_configured: bool
    subscribers: Dict[str, int]
    webhook_urls_count: int


class NotificationResult(BaseModel):
    """Notification result model."""
    email: bool = Field(default=False, description="Email notification success")
    slack: bool = Field(default=False, description="Slack notification success")
    webhooks: bool = Field(default=False, description="Webhook notifications success")


class MailingListResponse(BaseModel):
    """Mailing list response model."""
    daily_subscribers: List[str]
    weekly_subscribers: List[str]


# RAG Search Models
class PaperSearchRequest(BaseModel):
    """Request model for paper search."""
    query: str = Field(description="Search query text")
    top_k: int = Field(default=10, description="Maximum number of results (1-100)")
    min_similarity: float = Field(default=0.5, description="Minimum similarity threshold (0.0-1.0)")
    categories: Optional[List[str]] = Field(default=None, description="Filter by categories")
    start_date: Optional[str] = Field(default=None, description="Start date filter (YYYY-MM-DD)")
    end_date: Optional[str] = Field(default=None, description="End date filter (YYYY-MM-DD)")
    page: int = Field(default=1, description="Page number (1-based)")
    page_size: int = Field(default=10, description="Results per page (1-100)")


class SimilarPapersRequest(BaseModel):
    """Request model for finding similar papers."""
    arxiv_id: str = Field(description="ArXiv ID of reference paper")
    top_k: int = Field(default=5, description="Number of similar papers (1-20)")
    min_similarity: float = Field(default=0.7, description="Minimum similarity threshold (0.0-1.0)")


class PaperSearchResult(BaseModel):
    """Individual paper search result."""
    arxiv_id: str
    title: str
    abstract: str
    summary: str
    key_points: List[str]
    similarity_score: float
    timestamp: str
    metadata: Dict[str, Any]
    category: str
    published_date: Optional[str]
    authors: List[str]
    pdf_url: str


class PaperSearchResponse(BaseModel):
    """Response model for paper search."""
    query: str
    total_results: int
    page: int
    page_size: int
    total_pages: int
    min_similarity: float
    applied_filters: Dict[str, Any]
    results: List[PaperSearchResult]
    search_stats: Dict[str, Any]
    error: Optional[str] = None


class SimilarPaperResult(BaseModel):
    """Individual similar paper result."""
    arxiv_id: str
    title: str
    abstract: str
    summary: str
    similarity_score: float
    category: str
    published_date: Optional[str]
    pdf_url: str


class SimilarPapersResponse(BaseModel):
    """Response model for similar papers search."""
    reference_paper: Optional[Dict[str, str]]
    similar_papers: List[SimilarPaperResult]
    total_found: int
    min_similarity: float
    error: Optional[str] = None


class DatabaseStatsResponse(BaseModel):
    """Response model for database statistics."""
    total_papers: int
    embedding_dimension: int
    categories: Dict[str, int]
    date_range: Dict[str, Optional[str]]
    index_type: str


# Hybrid Search Models
class HybridSearchRequest(BaseModel):
    """Request model for hybrid search."""
    query: str = Field(description="Search query text")
    keyword_weight: float = Field(default=0.3, description="BM25 keyword search weight (0.0-1.0)")
    vector_weight: float = Field(default=0.7, description="Vector search weight (0.0-1.0)")
    top_k: int = Field(default=10, description="Maximum number of results (1-100)")
    min_similarity: float = Field(default=0.3, description="Minimum similarity threshold (0.0-1.0)")
    categories: Optional[List[str]] = Field(default=None, description="Filter by categories")
    start_date: Optional[str] = Field(default=None, description="Start date filter (YYYY-MM-DD)")
    end_date: Optional[str] = Field(default=None, description="End date filter (YYYY-MM-DD)")
    page: int = Field(default=1, description="Page number (1-based)")
    page_size: int = Field(default=10, description="Results per page (1-100)")


class HybridSearchResult(BaseModel):
    """Individual hybrid search result."""
    arxiv_id: str
    title: str
    abstract: str
    summary: str
    key_points: List[str]
    hybrid_score: float
    timestamp: str
    metadata: Dict[str, Any]
    category: str
    published_date: Optional[str]
    authors: List[str]
    pdf_url: str


class HybridSearchResponse(BaseModel):
    """Response model for hybrid search."""
    query: str
    search_type: str
    weights: Dict[str, float]
    total_results: int
    page: int
    page_size: int
    total_pages: int
    min_similarity: float
    applied_filters: Dict[str, Any]
    results: List[HybridSearchResult]
    search_stats: Dict[str, Any]
    error: Optional[str] = None


class HybridStatsResponse(BaseModel):
    """Response model for hybrid search statistics."""
    service_type: str
    vector_search: Dict[str, Any]
    keyword_search: Dict[str, Any]
    capabilities: List[str]
    status: Optional[str] = None
    error: Optional[str] = None