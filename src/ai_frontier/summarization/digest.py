"""Daily and weekly digest generation for collected papers."""

import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from collections import defaultdict, Counter
import re

from ..translation.translator import get_translator
from ..summarization.summarizer import get_summarizer
from ..notification.keyword_subscription_manager import get_paper_filter_service


class DigestGenerator:
    """Generate daily and weekly digests from collected papers."""

    def __init__(self, translation_provider: str = "openai", summarization_provider: str = "openai"):
        self.translator = get_translator(provider=translation_provider)
        self.summarizer = get_summarizer(provider=summarization_provider)
        self.paper_filter_service = get_paper_filter_service()
        self.logger = logging.getLogger(__name__)

    def _parse_paper_from_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Parse paper information from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else "Unknown Title"

            # Extract Korean title
            korean_title_match = re.search(r'\*\*Korean Title:\*\* (.+)$', content, re.MULTILINE)
            korean_title = korean_title_match.group(1) if korean_title_match else title

            # Extract ArXiv ID from Links section
            arxiv_id_match = re.search(r'\*\*ArXiv ID:\*\* \[([^\]]+)\]', content)
            arxiv_id = arxiv_id_match.group(1) if arxiv_id_match else "unknown"

            # Extract published date from Links section
            published_match = re.search(r'\*\*Published\*\*: (.+)$', content, re.MULTILINE)
            published_str = published_match.group(1) if published_match else None
            published = None
            if published_str:
                try:
                    published = datetime.strptime(published_str, "%Y-%m-%d")
                except ValueError:
                    pass

            # Extract category from Links section
            category_match = re.search(r'\*\*Category\*\*: (.+)$', content, re.MULTILINE)
            category = category_match.group(1) if category_match else "unknown"

            # Extract Korean abstract
            korean_abstract_match = re.search(r'## 🔍 Abstract \(한글 번역\)\s*\n\n(.+?)(?=\n##|\n---|\Z)', content, re.DOTALL)
            korean_abstract = korean_abstract_match.group(1).strip() if korean_abstract_match else ""

            # Extract summary
            summary_match = re.search(r'## 📝 요약\s*\n\n(.+?)(?=\n##|\n---|\Z)', content, re.DOTALL)
            summary = summary_match.group(1).strip() if summary_match else ""

            # Extract key points
            key_points_match = re.search(r'## 🎯 주요 포인트\s*\n\n(.+?)(?=\n##|\n---|\Z)', content, re.DOTALL)
            key_points = []
            if key_points_match:
                key_points_text = key_points_match.group(1).strip()
                key_points = [line.strip('- ').strip() for line in key_points_text.split('\n') if line.strip().startswith('- ')]

            # Extract keywords from categorized keywords section
            keywords = []
            keywords_section_match = re.search(r'## 🏷️ 카테고리화된 키워드\s*\n(.+?)(?=\n##|\n---|\Z)', content, re.DOTALL)
            if keywords_section_match:
                keywords_text = keywords_section_match.group(1)
                keyword_matches = re.findall(r'\[\[keywords/([^\|]+)\|[^\]]+\]\]', keywords_text)
                keywords = [kw.strip() for kw in keyword_matches]

            return {
                'title': title,
                'korean_title': korean_title,
                'arxiv_id': arxiv_id,
                'published': published,
                'category': category,
                'korean_abstract': korean_abstract,
                'summary': summary,
                'key_points': key_points,
                'keywords': keywords,
                'file_path': str(file_path)
            }

        except Exception as e:
            self.logger.error(f"Error parsing file {file_path}: {e}")
            return None

    def _collect_papers_from_directory(self, directory: Path, start_date: datetime, end_date: datetime) -> List[Dict[str, Any]]:
        """Collect papers from directory within date range, including date subdirectories."""
        papers = []

        if not directory.exists():
            self.logger.warning(f"Directory does not exist: {directory}")
            return papers

        # Search in main directory and date subdirectories
        search_paths = [directory]

        # Add date-specific subdirectories that might exist
        for single_date in self._date_range(start_date, end_date):
            date_str = single_date.strftime("%Y-%m-%d")
            date_dir = directory / date_str
            if date_dir.exists():
                search_paths.append(date_dir)

        for search_path in search_paths:
            for file_path in search_path.glob("*.md"):
                paper_data = self._parse_paper_from_file(file_path)
                if paper_data and paper_data['published']:
                    if start_date <= paper_data['published'] <= end_date:
                        papers.append(paper_data)

        # Sort by published date
        papers.sort(key=lambda x: x['published'])
        return papers

    def _date_range(self, start_date: datetime, end_date: datetime):
        """Generate date range between start and end dates."""
        current_date = start_date
        while current_date <= end_date:
            yield current_date
            current_date += timedelta(days=1)

    def _analyze_papers_statistics(self, papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze papers for statistics and trends."""
        if not papers:
            return {}

        # Category analysis
        category_counts = Counter(paper['category'] for paper in papers)

        # Keyword analysis
        all_keywords = []
        for paper in papers:
            all_keywords.extend(paper['keywords'])
        keyword_counts = Counter(all_keywords)

        # Daily distribution for weekly digest
        daily_counts = defaultdict(int)
        for paper in papers:
            date_key = paper['published'].strftime("%Y-%m-%d")
            daily_counts[date_key] += 1

        return {
            'total_papers': len(papers),
            'categories': dict(category_counts.most_common()),
            'top_keywords': dict(keyword_counts.most_common(15)),
            'daily_distribution': dict(daily_counts),
            'category_count': len(category_counts),
            'unique_keywords': len(keyword_counts)
        }

    def _generate_digest_summary(self, papers: List[Dict[str, Any]], digest_type: str = "daily") -> str:
        """Generate an AI summary focused on insights and trends."""
        if not papers:
            return "이 기간에 수집된 논문이 없습니다."

        # Get statistics
        stats = self._analyze_papers_statistics(papers)

        # Prepare detailed analysis text for AI with key points from each paper
        analysis_text = f"{digest_type} 논문 분석 데이터:\n\n"
        analysis_text += f"전체 논문 수: {stats['total_papers']}편\n"
        analysis_text += f"연구 분야 수: {stats['category_count']}개\n"
        analysis_text += f"고유 키워드 수: {stats['unique_keywords']}개\n\n"

        analysis_text += "주요 연구 분야:\n"
        for cat, count in list(stats['categories'].items())[:5]:
            analysis_text += f"- {cat}: {count}편\n"

        analysis_text += "\n주요 키워드:\n"
        for keyword, count in list(stats['top_keywords'].items())[:10]:
            analysis_text += f"- {keyword}: {count}회\n"

        # Group papers by category for detailed analysis
        analysis_text += "\n카테고리별 논문 주요 포인트 분석:\n\n"
        papers_by_category = defaultdict(list)
        for paper in papers:
            papers_by_category[paper['category']].append(paper)

        for category, category_papers in papers_by_category.items():
            analysis_text += f"=== {category} ({len(category_papers)}편) ===\n"
            for paper in category_papers[:8]:  # 카테고리당 최대 8편까지
                analysis_text += f"논문: {paper['korean_title']}\n"
                analysis_text += f"주요 포인트: {', '.join(paper['key_points'][:3])}\n"
                analysis_text += f"요약: {paper['summary'][:200]}...\n"
                analysis_text += f"키워드: {', '.join(paper['keywords'][:5])}\n\n"

        # Generate comprehensive AI analysis
        try:
            prompt = f"""다음 {digest_type} 논문 데이터를 카테고리별 주요 포인트를 기반으로 기술 발전과 새로운 기술 등장 관점에서 깊이 있게 분석해주세요:

{analysis_text}

다음 구조로 상세한 기술 발전 중심의 인사이트를 작성해주세요:

## 🚀 기술 발전 및 혁신 동향
각 카테고리별로 개별 논문들의 주요 포인트를 분석하여:
- 새롭게 등장하는 기술이나 방법론의 특징
- 기존 기술의 개선점이나 한계 극복 방안
- 기술 간 융합이나 새로운 접근법의 등장

## 🔬 카테고리별 기술 진화 분석
각 연구 분야별로:
- 주요 기술적 브레이크스루나 개선사항
- 실용화 가능성이 높은 새로운 기술
- 기존 패러다임의 변화나 새로운 연구 방향

## 💡 혁신적 연구 하이라이트
- 기술적으로 가장 혁신적인 접근법을 보인 연구들
- 산업계에 실질적 영향을 줄 수 있는 기술들
- 향후 연구 트렌드를 주도할 것으로 예상되는 기술들

각 논문의 구체적인 주요 포인트를 근거로 기술 발전 관점에서 심도 있는 분석을 제공해주세요."""

            # AI 요약 생성 (토큰 수를 늘려서 완전한 응답 생성)
            summary = self.summarizer.summarize_text(prompt, max_tokens=2500)
            return summary

        except Exception as e:
            self.logger.error(f"Failed to generate AI summary: {e}")
            return f"총 {len(papers)}편의 논문이 수집되었습니다. AI 요약 생성 중 오류가 발생했습니다."

    def generate_daily_digest(self, target_date: datetime, papers_dir: Path = None) -> str:
        """Generate daily digest focused on insights and trends."""
        if papers_dir is None:
            papers_dir = Path("reports/individual_papers")

        # Set date range for the day
        start_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = target_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Collect papers
        papers = self._collect_papers_from_directory(papers_dir, start_date, end_date)

        # Get statistics
        stats = self._analyze_papers_statistics(papers)

        # Generate AI summary
        ai_summary = self._generate_digest_summary(papers, "일일")

        # Generate markdown content
        date_str = target_date.strftime("%Y-%m-%d")
        digest_content = f"""# 일일 논문 다이제스트 - {date_str}

## 📊 수집 통계

**수집 일자**: {date_str}
**총 논문 수**: {len(papers)}편
**연구 분야 수**: {stats.get('category_count', 0)}개
**고유 키워드 수**: {stats.get('unique_keywords', 0)}개

## 📈 분야별 분포

"""

        if papers:
            # Add category distribution
            for category, count in list(stats['categories'].items())[:10]:
                percentage = (count / len(papers)) * 100
                digest_content += f"- **{category}**: {count}편 ({percentage:.1f}%)\n"

            digest_content += f"\n## 🔖 주요 키워드 트렌드\n\n"

            # Add top keywords
            for keyword, count in list(stats['top_keywords'].items())[:15]:
                digest_content += f"- **{keyword}**: {count}회\n"

            digest_content += f"\n{ai_summary}\n\n"

            digest_content += f"## 📋 개별 논문 목록\n\n"

            # Simple list with title and PDF link only
            for paper in papers:
                digest_content += f"- [{paper['korean_title']}](https://arxiv.org/pdf/{paper['arxiv_id']}.pdf)\n"

        else:
            digest_content += "이 날짜에 수집된 논문이 없습니다.\n\n"

        digest_content += f"\n---\n*생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

        return digest_content

    def generate_weekly_digest(self, target_date: datetime, papers_dir: Path = None) -> str:
        """Generate weekly digest for the week containing target_date."""
        if papers_dir is None:
            papers_dir = Path("reports/individual_papers")

        # Calculate week range (Monday to Sunday)
        days_since_monday = target_date.weekday()
        start_date = target_date - timedelta(days=days_since_monday)
        end_date = start_date + timedelta(days=6)

        # Set time ranges
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Collect papers
        papers = self._collect_papers_from_directory(papers_dir, start_date, end_date)

        # Get statistics
        stats = self._analyze_papers_statistics(papers)

        # Group by date
        papers_by_date = defaultdict(list)
        for paper in papers:
            date_key = paper['published'].strftime("%Y-%m-%d")
            papers_by_date[date_key].append(paper)

        # Generate AI summary
        ai_summary = self._generate_digest_summary(papers, "주간")

        # Generate markdown content
        week_str = f"{start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}"
        digest_content = f"""# 주간 논문 다이제스트 - {week_str}

## 📊 수집 통계

**수집 기간**: {week_str}
**총 논문 수**: {len(papers)}편
**수집 일수**: {len(papers_by_date)}일
**연구 분야 수**: {stats.get('category_count', 0)}개
**고유 키워드 수**: {stats.get('unique_keywords', 0)}개

## 📈 분야별 분포

"""

        if papers:
            # Add category distribution
            for category, count in list(stats['categories'].items())[:10]:
                percentage = (count / len(papers)) * 100
                digest_content += f"- **{category}**: {count}편 ({percentage:.1f}%)\n"

            digest_content += f"\n## 🔖 주요 키워드 트렌드\n\n"

            # Add top keywords
            for keyword, count in list(stats['top_keywords'].items())[:20]:
                digest_content += f"- **{keyword}**: {count}회\n"

            digest_content += f"\n{ai_summary}\n\n"

            digest_content += f"## 📈 일별 분포\n\n"

            # Add daily statistics
            for date_key in sorted(papers_by_date.keys()):
                day_papers = papers_by_date[date_key]
                categories = defaultdict(int)
                for paper in day_papers:
                    categories[paper['category']] += 1

                digest_content += f"**{date_key}**: {len(day_papers)}편"
                if categories:
                    category_str = ", ".join([f"{cat}({count})" for cat, count in categories.items()])
                    digest_content += f" - {category_str}"
                digest_content += "\n"

            digest_content += f"\n## 📋 개별 논문 목록\n\n"

            # Simple list with title and PDF link only
            for paper in papers:
                digest_content += f"- [{paper['korean_title']}](https://arxiv.org/pdf/{paper['arxiv_id']}.pdf)\n"
            digest_content += f"\n"

        else:
            digest_content += "이 주에 수집된 논문이 없습니다.\n\n"

        digest_content += f"---\n*생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

        return digest_content

    def generate_filtered_digest(self, target_date: datetime, keywords: List[str], digest_type: str = "daily", papers_dir: Path = None) -> str:
        """Generate a keyword-filtered digest for personalized subscriptions."""
        if papers_dir is None:
            papers_dir = Path("reports/individual_papers")

        # Set date range based on digest type
        if digest_type == "daily":
            start_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = target_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        else:  # weekly
            days_since_monday = target_date.weekday()
            start_date = target_date - timedelta(days=days_since_monday)
            end_date = start_date + timedelta(days=6)
            start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Collect all papers for the period
        all_papers = self._collect_papers_from_directory(papers_dir, start_date, end_date)

        # Filter papers by keywords
        filtered_papers = self.paper_filter_service.filter_papers_by_keywords(all_papers, keywords)

        # Get statistics
        stats = self._analyze_papers_statistics(filtered_papers)

        # Generate AI summary for filtered papers
        ai_summary = self._generate_digest_summary(filtered_papers, digest_type)

        # Generate personalized digest content
        date_str = target_date.strftime("%Y-%m-%d")
        keywords_str = ", ".join(keywords) if keywords else "모든 키워드"

        if digest_type == "daily":
            digest_content = f"""# 🎯 맞춤형 일일 논문 다이제스트 - {date_str}

## 📌 개인화 설정

**구독 키워드**: {keywords_str}
**수집 일자**: {date_str}
**총 매칭 논문**: {len(filtered_papers)}편 (전체 {len(all_papers)}편 중)
**매칭률**: {(len(filtered_papers) / len(all_papers) * 100) if all_papers else 0:.1f}%
**연구 분야 수**: {stats.get('category_count', 0)}개
**고유 키워드 수**: {stats.get('unique_keywords', 0)}개

"""
        else:  # weekly
            week_str = f"{start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}"
            digest_content = f"""# 🎯 맞춤형 주간 논문 다이제스트 - {week_str}

## 📌 개인화 설정

**구독 키워드**: {keywords_str}
**수집 기간**: {week_str}
**총 매칭 논문**: {len(filtered_papers)}편 (전체 {len(all_papers)}편 중)
**매칭률**: {(len(filtered_papers) / len(all_papers) * 100) if all_papers else 0:.1f}%
**연구 분야 수**: {stats.get('category_count', 0)}개
**고유 키워드 수**: {stats.get('unique_keywords', 0)}개

"""

        if filtered_papers:
            # Add category distribution
            digest_content += f"## 📈 분야별 분포\n\n"
            for category, count in list(stats['categories'].items())[:10]:
                percentage = (count / len(filtered_papers)) * 100
                digest_content += f"- **{category}**: {count}편 ({percentage:.1f}%)\n"

            digest_content += f"\n## 🔖 주요 키워드 트렌드\n\n"

            # Add top keywords
            for keyword, count in list(stats['top_keywords'].items())[:15]:
                digest_content += f"- **{keyword}**: {count}회\n"

            digest_content += f"\n{ai_summary}\n\n"

            if digest_type == "weekly":
                # Group by date for weekly digest
                papers_by_date = defaultdict(list)
                for paper in filtered_papers:
                    date_key = paper['published'].strftime("%Y-%m-%d")
                    papers_by_date[date_key].append(paper)

                digest_content += f"## 📈 일별 분포\n\n"
                for date_key in sorted(papers_by_date.keys()):
                    day_papers = papers_by_date[date_key]
                    categories = defaultdict(int)
                    for paper in day_papers:
                        categories[paper['category']] += 1

                    digest_content += f"**{date_key}**: {len(day_papers)}편"
                    if categories:
                        category_str = ", ".join([f"{cat}({count})" for cat, count in categories.items()])
                        digest_content += f" - {category_str}"
                    digest_content += "\n"

            digest_content += f"\n## 📋 개별 논문 목록\n\n"

            # Simple list with title and PDF link only
            for paper in filtered_papers:
                digest_content += f"- [{paper['korean_title']}](https://arxiv.org/pdf/{paper['arxiv_id']}.pdf)\n"

        else:
            digest_content += f"""## ⚠️ 매칭 결과 없음

이 기간에 귀하의 키워드 **"{keywords_str}"**와 매칭되는 논문이 없습니다.

### 💡 키워드 제안
- 더 넓은 범위의 키워드 사용을 고려해보세요
- 동의어나 관련 용어 추가를 고려해보세요
- 키워드를 줄이거나 더 일반적인 용어로 변경해보세요

전체 {len(all_papers)}편의 논문이 이 기간에 수집되었습니다.

"""

        digest_content += f"\n---\n*생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        digest_content += f"*개인화 필터 적용: 키워드 기반 맞춤형 다이제스트*\n"

        return digest_content

    def save_daily_digest(self, target_date: datetime, output_dir: Path = None) -> Path:
        """Generate and save daily digest."""
        if output_dir is None:
            output_dir = Path("reports/digests")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate content
        content = self.generate_daily_digest(target_date)

        # Save file
        filename = f"daily_digest_{target_date.strftime('%Y%m%d')}.md"
        file_path = output_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.logger.info(f"Daily digest saved: {file_path}")

        # Send notifications if configured
        try:
            from ..notification.notification_manager import NotificationManager
            notification_manager = NotificationManager()
            notification_results = notification_manager.send_digest_notifications(
                digest_file_path=file_path,
                digest_type="daily",
                digest_date=target_date.strftime("%Y-%m-%d")
            )
            self.logger.info(f"Daily digest notifications sent: {notification_results}")
        except Exception as e:
            self.logger.warning(f"Failed to send daily digest notifications: {e}")

        return file_path

    def save_weekly_digest(self, target_date: datetime, output_dir: Path = None) -> Path:
        """Generate and save weekly digest."""
        if output_dir is None:
            output_dir = Path("reports/digests")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate content
        content = self.generate_weekly_digest(target_date)

        # Calculate week info for filename
        days_since_monday = target_date.weekday()
        week_start = target_date - timedelta(days=days_since_monday)

        # Save file
        filename = f"weekly_digest_{week_start.strftime('%Y%m%d')}.md"
        file_path = output_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.logger.info(f"Weekly digest saved: {file_path}")

        # Send notifications if configured
        try:
            from ..notification.notification_manager import NotificationManager
            notification_manager = NotificationManager()
            notification_results = notification_manager.send_digest_notifications(
                digest_file_path=file_path,
                digest_type="weekly",
                digest_date=target_date.strftime("%Y-%m-%d")
            )
            self.logger.info(f"Weekly digest notifications sent: {notification_results}")
        except Exception as e:
            self.logger.warning(f"Failed to send weekly digest notifications: {e}")

        return file_path