"""ArXiv API client for fetching papers."""

from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import re

# Simple and direct arxiv import
try:
    import arxiv
    print("✅ ArXiv imported successfully")
    ARXIV_AVAILABLE = True
except ImportError as e:
    print(f"❌ ArXiv import failed: {e}")
    ARXIV_AVAILABLE = False
    arxiv = None

# RSS feed parser import
try:
    import feedparser
    print("✅ Feedparser imported successfully")
    FEEDPARSER_AVAILABLE = True
except ImportError as e:
    print(f"❌ Feedparser import failed: {e}")
    FEEDPARSER_AVAILABLE = False
    feedparser = None

class ArxivPaper(BaseModel):
    """ArXiv paper data model."""
    title: str
    abstract: str
    authors: List[str]
    arxiv_id: str
    published: datetime
    updated: Optional[datetime] = None
    pdf_url: str
    category: str

    @property
    def published_date(self) -> datetime:
        """Get published date (alias for published)."""
        return self.published

    @property
    def updated_date(self) -> datetime:
        """Get updated date (use updated if available, otherwise published)."""
        return self.updated or self.published

class ArxivClient:
    """Client for interacting with ArXiv API."""

    def __init__(self, max_results: int = 3000, use_rss: bool = False):
        self.max_results = max_results
        self.use_rss = use_rss

        if not ARXIV_AVAILABLE and not use_rss:
            raise ImportError("arxiv library is not available. Please install with: pip install arxiv")

        if use_rss and not FEEDPARSER_AVAILABLE:
            raise ImportError("feedparser library is not available. Please install with: pip install feedparser")

        # Try to create arxiv client, fallback to direct search if needed
        try:
            self.client = arxiv.Client()
            self.use_client = True
            print("✅ ArXiv Client created successfully")
        except Exception as e:
            print(f"⚠️ Cannot create arxiv.Client: {e}")
            print("🔄 Falling back to direct Search.results() method")
            self.client = None
            self.use_client = False

    def search_recent_papers(
        self,
        categories: List[str] = None,
        days_back: int = 1,
        query: Optional[str] = None,
        keywords: List[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[ArxivPaper]:
        """Search for recent papers in specified categories and keywords."""
        if categories is None:
            categories = ["cs.AI", "cs.LG", "cs.CL", "cs.CV"]

        # Use RSS feed method if enabled
        if self.use_rss:
            return self._search_rss_papers(categories, days_back, keywords, start_date, end_date)

        # Use original API method
        return self._search_api_papers(categories, days_back, query, keywords, start_date, end_date)

    def _search_rss_papers(
        self,
        categories: List[str],
        days_back: int,
        keywords: List[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[ArxivPaper]:
        """Search papers using RSS feeds."""
        if not FEEDPARSER_AVAILABLE:
            raise ImportError("feedparser library is required for RSS search. Install with: pip install feedparser")

        # RSS 피드는 최신 1일치만 지원하므로 사용자에게 알림
        if start_date and end_date:
            print("⚠️ RSS 피드는 최신 논문만 제공하므로 특정 날짜 범위 검색이 제한됩니다.")
        elif days_back > 1:
            print("⚠️ RSS 피드는 최신 논문만 제공하므로 최근 1일 논문을 검색합니다.")

        # RSS는 최신 발표일 기준으로만 검색 가능 (실제 RSS 데이터에서 날짜 확인)
        print(f"RSS: Searching for latest papers in {len(categories)} categories")

        # RSS에서 실제 사용 가능한 날짜를 동적으로 확인
        available_dates = set()
        all_papers = []
        seen_arxiv_ids = set()  # 중복 제거를 위한 추적

        for category in categories:
            try:
                url = f'https://rss.arxiv.org/rss/{category}'
                feed = feedparser.parse(url)

                if feed.bozo:
                    print(f'RSS parsing error for {category}')
                    continue

                for entry in feed.entries:
                    # Apply keyword filter if specified (search in title and summary)
                    if keywords:
                        title_lower = entry.title.lower()
                        summary_lower = getattr(entry, 'summary', '').lower()
                        content_text = f"{title_lower} {summary_lower}"

                        # Check if any keyword appears in title or abstract
                        keyword_found = any(keyword.lower() in content_text for keyword in keywords)
                        if not keyword_found:
                            continue

                    try:
                        # Parse RSS date format: 'Wed, 17 Sep 2025 00:00:00 -0400'
                        pub_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
                        date_str = pub_date.strftime('%Y-%m-%d')
                        available_dates.add(date_str)

                        # RSS 모드에서는 실제 피드에 있는 모든 논문을 수집 (날짜 필터링 없음)
                        if True:  # RSS에서는 모든 논문 수집
                            # Extract ArXiv ID from URL
                            arxiv_id = ''
                            if 'arxiv.org/abs/' in entry.link:
                                arxiv_id = entry.link.split('/')[-1]

                            # Skip duplicate papers
                            if arxiv_id in seen_arxiv_ids:
                                continue
                            seen_arxiv_ids.add(arxiv_id)

                            # Create paper object
                            paper = ArxivPaper(
                                title=entry.title,
                                abstract=entry.summary,
                                authors=[],  # RSS doesn't provide detailed author info
                                arxiv_id=arxiv_id,
                                published=pub_date,
                                updated=pub_date,  # RSS doesn't provide separate updated date
                                pdf_url=entry.link.replace('/abs/', '/pdf/') + '.pdf',
                                category=category
                            )
                            all_papers.append(paper)

                    except Exception as e:
                        print(f'Error processing entry {entry.title}: {e}')
                        continue

            except Exception as e:
                print(f'Error fetching RSS for {category}: {e}')
                continue

        if available_dates:
            dates_str = ', '.join(sorted(available_dates, reverse=True))
            print(f"RSS: Found {len(all_papers)} papers from dates: {dates_str}")
        else:
            print(f"RSS: Found {len(all_papers)} papers")
        return all_papers

    def _search_api_papers(
        self,
        categories: List[str],
        days_back: int,
        query: Optional[str] = None,
        keywords: List[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[ArxivPaper]:
        """Search papers using ArXiv API (original method)."""

        # Build search query
        category_query = " OR ".join([f"cat:{cat}" for cat in categories])

        # Build keyword query
        query_parts = [category_query]

        if keywords:
            # Search keywords in title, abstract, and comments
            keyword_queries = []
            for keyword in keywords:
                # Search only in title to match ArXiv website behavior
                keyword_query = f'ti:"{keyword}"'
                keyword_queries.append(keyword_query)

            # Combine keywords with OR (any keyword matches)
            keywords_query = " OR ".join(keyword_queries)
            query_parts.append(f"({keywords_query})")

        if query:
            query_parts.append(f"({query})")

        search_query = " AND ".join(query_parts)

        # Use pagination to get all papers in date range
        papers = []

        # Set date filters
        if start_date and end_date:
            # Convert to timezone-aware and set to beginning/end of day
            if start_date.tzinfo is None:
                start_date = start_date.replace(tzinfo=timezone.utc)
            if end_date.tzinfo is None:
                end_date = end_date.replace(tzinfo=timezone.utc)

            # Set to beginning of start date and end of end date
            cutoff_start = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
            cutoff_end = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            print(f"Searching papers between {cutoff_start.date()} and {cutoff_end.date()}")
        else:
            # Set cutoff_start to beginning of the day 'days_back' days ago
            now = datetime.now(timezone.utc)
            cutoff_start = (now - timedelta(days=days_back)).replace(hour=0, minute=0, second=0, microsecond=0)
            cutoff_end = now


        # Use ArXiv's built-in pagination properly
        try:
            search = arxiv.Search(
                query=search_query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )
        except AttributeError as e:
            # Fallback: create search without sort parameters if they're not available
            print(f"⚠️ Sort parameters not available ({e}), using basic search")
            try:
                search = arxiv.Search(
                    query=search_query,
                    max_results=self.max_results
                )
            except Exception as e2:
                raise RuntimeError(f"arxiv.Search creation failed: {e2}. Please check arxiv library installation.")

        total_collected = 0
        processed_count = 0
        max_processed = 5000  # Increased limit to get more results

        try:
            # Use client if available, otherwise direct search
            if self.use_client and self.client:
                results_iter = self.client.results(search)
            else:
                # Suppress deprecation warning for fallback
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    results_iter = search.results()

            for result in results_iter:
                processed_count += 1
                if processed_count > max_processed:
                    print(f"Reached maximum processed limit ({max_processed}), stopping")
                    break

                # Convert result.published to timezone-aware if it isn't already
                published_date = result.published
                if published_date.tzinfo is None:
                    published_date = published_date.replace(tzinfo=timezone.utc)

                # Check if paper is within date range
                if cutoff_start <= published_date <= cutoff_end:
                    paper = ArxivPaper(
                        title=result.title,
                        abstract=result.summary,
                        authors=[author.name for author in result.authors],
                        arxiv_id=result.get_short_id(),
                        published=published_date,
                        updated=result.updated,
                        pdf_url=result.pdf_url,
                        category=result.primary_category
                    )
                    papers.append(paper)
                    total_collected += 1

                    # Show progress every 10 papers
                    if total_collected % 10 == 0:
                        print(f"Collected {total_collected} papers so far...")

        except Exception as e:
            # Don't show error for empty pages (normal when we've reached the end)
            if "unexpectedly empty" not in str(e):
                print(f"Error fetching papers: {e}")
            if not papers:
                # If we couldn't get any papers, try a simpler search
                print("Retrying with simpler search...")
                try:
                    simple_search = arxiv.Search(
                        query=search_query,
                        max_results=100,
                        sort_by=arxiv.SortCriterion.SubmittedDate,
                        sort_order=arxiv.SortOrder.Descending
                    )
                except AttributeError:
                    return []

                try:
                    if self.use_client and self.client:
                        simple_results_iter = self.client.results(simple_search)
                    else:
                        import warnings
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore", DeprecationWarning)
                            simple_results_iter = simple_search.results()

                    for result in simple_results_iter:
                        published_date = result.published
                        if published_date.tzinfo is None:
                            published_date = published_date.replace(tzinfo=timezone.utc)

                        if cutoff_start <= published_date <= cutoff_end:
                            paper = ArxivPaper(
                                title=result.title,
                                abstract=result.summary,
                                authors=[author.name for author in result.authors],
                                arxiv_id=result.get_short_id(),
                                published=published_date,
                                updated=result.updated,
                                pdf_url=result.pdf_url,
                                category=result.primary_category
                            )
                            papers.append(paper)
                            total_collected += 1

                except Exception as e2:
                    print(f"Simple search also failed: {e2}")
                    return []

        print(f"Total collected: {len(papers)} papers")
        return papers

    def search_by_keywords_only(
        self,
        keywords: List[str],
        days_back: int = 7,
        categories: List[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[ArxivPaper]:
        """Search for papers by keywords only, without category restriction."""
        if not keywords:
            raise ValueError("At least one keyword is required")

        # Use RSS feed method if enabled
        if self.use_rss:
            # If no categories specified, use all CS categories for RSS
            if not categories:
                categories = ["cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.CR", "cs.DC",
                             "cs.DS", "cs.GT", "cs.HC", "cs.IR", "cs.IT", "cs.MA",
                             "cs.NI", "cs.RO"]
            return self._search_rss_papers(categories, days_back, keywords, start_date, end_date)

        # Use original API method

        # Build keyword query
        keyword_queries = []
        for keyword in keywords:
            # Search only in title to match ArXiv website behavior
            keyword_query = f'ti:"{keyword}"'
            keyword_queries.append(keyword_query)

        # Combine keywords with OR (any keyword matches)
        keywords_query = " OR ".join(keyword_queries)

        # Add category filter if specified
        if categories:
            category_query = " OR ".join([f"cat:{cat}" for cat in categories])
            search_query = f"({keywords_query}) AND ({category_query})"
        else:
            search_query = keywords_query

        # Use pagination to get all papers in date range
        papers = []

        # Set date filters
        if start_date and end_date:
            # Convert to timezone-aware and set to beginning/end of day
            if start_date.tzinfo is None:
                start_date = start_date.replace(tzinfo=timezone.utc)
            if end_date.tzinfo is None:
                end_date = end_date.replace(tzinfo=timezone.utc)

            # Set to beginning of start date and end of end date
            cutoff_start = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
            cutoff_end = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            print(f"Searching papers between {cutoff_start.date()} and {cutoff_end.date()}")
        else:
            # Set cutoff_start to beginning of the day 'days_back' days ago
            now = datetime.now(timezone.utc)
            cutoff_start = (now - timedelta(days=days_back)).replace(hour=0, minute=0, second=0, microsecond=0)
            cutoff_end = now

        # Use ArXiv's built-in pagination properly
        try:
            search = arxiv.Search(
                query=search_query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )
        except AttributeError as e:
            # Fallback: create search without sort parameters if they're not available
            print(f"⚠️ Sort parameters not available ({e}), using basic search")
            try:
                search = arxiv.Search(
                    query=search_query,
                    max_results=self.max_results
                )
            except Exception as e2:
                raise RuntimeError(f"arxiv.Search creation failed: {e2}. Please check arxiv library installation.")

        total_collected = 0
        processed_count = 0
        max_processed = 5000  # Increased limit to get more results

        try:
            # Use client if available, otherwise direct search
            if self.use_client and self.client:
                results_iter = self.client.results(search)
            else:
                # Suppress deprecation warning for fallback
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    results_iter = search.results()

            for result in results_iter:
                processed_count += 1
                if processed_count > max_processed:
                    print(f"Reached maximum processed limit ({max_processed}), stopping")
                    break

                published_date = result.published
                if published_date.tzinfo is None:
                    published_date = published_date.replace(tzinfo=timezone.utc)

                # Check if paper is within date range
                if cutoff_start <= published_date <= cutoff_end:
                    paper = ArxivPaper(
                        title=result.title,
                        abstract=result.summary,
                        authors=[author.name for author in result.authors],
                        arxiv_id=result.get_short_id(),
                        published=published_date,
                        updated=result.updated,
                        pdf_url=result.pdf_url,
                        category=result.primary_category
                    )
                    papers.append(paper)
                    total_collected += 1

                    # Show progress every 10 papers
                    if total_collected % 10 == 0:
                        print(f"Collected {total_collected} papers so far...")

        except Exception as e:
            # Don't show error for empty pages (normal when we've reached the end)
            if "unexpectedly empty" not in str(e):
                print(f"Error fetching papers: {e}")
            if not papers:
                # If we couldn't get any papers, try a simpler search
                print("Retrying with simpler search...")
                try:
                    simple_search = arxiv.Search(
                        query=search_query,
                        max_results=100,
                        sort_by=arxiv.SortCriterion.SubmittedDate,
                        sort_order=arxiv.SortOrder.Descending
                    )
                except AttributeError:
                    return []

                try:
                    if self.use_client and self.client:
                        simple_results_iter = self.client.results(simple_search)
                    else:
                        import warnings
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore", DeprecationWarning)
                            simple_results_iter = simple_search.results()

                    for result in simple_results_iter:
                        published_date = result.published
                        if published_date.tzinfo is None:
                            published_date = published_date.replace(tzinfo=timezone.utc)

                        if cutoff_start <= published_date <= cutoff_end:
                            paper = ArxivPaper(
                                title=result.title,
                                abstract=result.summary,
                                authors=[author.name for author in result.authors],
                                arxiv_id=result.get_short_id(),
                                published=published_date,
                                updated=result.updated,
                                pdf_url=result.pdf_url,
                                category=result.primary_category
                            )
                            papers.append(paper)
                            total_collected += 1

                except Exception as e2:
                    print(f"Simple search also failed: {e2}")
                    return []

        print(f"Total collected: {len(papers)} papers")
        return papers