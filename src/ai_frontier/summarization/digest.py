"""Daily and weekly digest generation for collected papers."""

import os
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from collections import defaultdict
import re

from ..arxiv.client import ArxivPaper
from ..translation.translator import get_translator
from ..summarization.summarizer import get_summarizer


class DigestGenerator:
    """Generate daily and weekly digests from collected papers."""

    def __init__(self, translation_provider: str = "openai", summarization_provider: str = "openai"):
        self.translator = get_translator(provider=translation_provider)
        self.summarizer = get_summarizer(provider=summarization_provider)
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
            published_match = re.search(r'\*\*Published:\*\* (.+)$', content, re.MULTILINE)
            published_str = published_match.group(1) if published_match else None
            published = None
            if published_str:
                try:
                    published = datetime.strptime(published_str, "%Y-%m-%d")
                except ValueError:
                    pass

            # Extract category from Links section
            category_match = re.search(r'\*\*Category:\*\* (.+)$', content, re.MULTILINE)
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

            # Extract keywords from Links section
            links_match = re.search(r'\*\*Links\*\*: (.+)$', content, re.MULTILINE)
            keywords = []
            if links_match:
                links_text = links_match.group(1)
                keyword_matches = re.findall(r'\[\[keywords/([^\|]+)\|[^\]]+\]\]', links_text)
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
        """Collect papers from directory within date range."""
        papers = []

        if not directory.exists():
            self.logger.warning(f"Directory does not exist: {directory}")
            return papers

        for file_path in directory.glob("*.md"):
            paper_data = self._parse_paper_from_file(file_path)
            if paper_data and paper_data['published']:
                if start_date <= paper_data['published'] <= end_date:
                    papers.append(paper_data)

        # Sort by published date
        papers.sort(key=lambda x: x['published'])
        return papers

    def _generate_digest_summary(self, papers: List[Dict[str, Any]], digest_type: str = "daily") -> str:
        """Generate an AI summary of the papers for the digest."""
        if not papers:
            return "이 기간에 수집된 논문이 없습니다."

        # Prepare text for summarization
        papers_text = f"{digest_type} 논문 요약:\n\n"

        for i, paper in enumerate(papers, 1):
            papers_text += f"{i}. {paper['korean_title']} ({paper['category']})\n"
            papers_text += f"   요약: {paper['summary'][:200]}...\n"
            papers_text += f"   키워드: {', '.join(paper['keywords'][:5])}\n\n"

        # Generate summary using AI
        try:
            prompt = f"""다음 논문들을 분석하여 {digest_type} 요약을 작성해주세요:

{papers_text}

다음 형식으로 요약해주세요:
1. 전체 개요 (2-3문장)
2. 주요 연구 동향 (3-4개 포인트)
3. 주목할 만한 논문 (2-3편)
4. 키워드 트렌드"""

            summary = self.summarizer.summarize_text(prompt)
            return summary

        except Exception as e:
            self.logger.error(f"Failed to generate AI summary: {e}")
            return f"총 {len(papers)}편의 논문이 수집되었습니다. AI 요약 생성 중 오류가 발생했습니다."

    def generate_daily_digest(self, target_date: datetime, papers_dir: Path = None) -> str:
        """Generate daily digest for a specific date."""
        if papers_dir is None:
            papers_dir = Path("reports/individual_papers")

        # Set date range for the day
        start_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = target_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Collect papers
        papers = self._collect_papers_from_directory(papers_dir, start_date, end_date)

        # Generate AI summary
        ai_summary = self._generate_digest_summary(papers, "일일")

        # Generate markdown content
        date_str = target_date.strftime("%Y-%m-%d")
        digest_content = f"""# 일일 논문 다이제스트 - {date_str}

## 📊 개요

**수집 일자**: {date_str}
**총 논문 수**: {len(papers)}편

## 🤖 AI 요약

{ai_summary}

## 📋 논문 목록

"""

        # Add paper list
        if papers:
            for i, paper in enumerate(papers, 1):
                digest_content += f"""### {i}. {paper['korean_title']}

**원제**: {paper['title']}
**카테고리**: {paper['category']}
**ArXiv ID**: [{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']})
**키워드**: {', '.join(paper['keywords'])}

**요약**: {paper['summary']}

**주요 포인트**:
"""
                for point in paper['key_points']:
                    digest_content += f"- {point}\n"

                digest_content += f"\n**파일**: [{paper['file_path'].split('/')[-1]}]({paper['file_path']})\n\n---\n\n"
        else:
            digest_content += "이 날짜에 수집된 논문이 없습니다.\n\n"

        digest_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

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

## 📊 개요

**수집 기간**: {week_str}
**총 논문 수**: {len(papers)}편
**수집 일수**: {len(papers_by_date)}일

## 🤖 AI 요약

{ai_summary}

## 📈 일별 통계

"""

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

        digest_content += "\n## 📋 카테고리별 논문\n\n"

        # Group by category
        papers_by_category = defaultdict(list)
        for paper in papers:
            papers_by_category[paper['category']].append(paper)

        # Add papers by category
        for category in sorted(papers_by_category.keys()):
            category_papers = papers_by_category[category]
            digest_content += f"### {category} ({len(category_papers)}편)\n\n"

            for paper in category_papers:
                digest_content += f"- **{paper['korean_title']}** ({paper['published'].strftime('%m-%d')})\n"
                digest_content += f"  *{paper['summary'][:150]}...*\n"
                digest_content += f"  [[{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']})] "
                digest_content += f"키워드: {', '.join(paper['keywords'][:3])}\n\n"

        if not papers:
            digest_content += "이 주에 수집된 논문이 없습니다.\n\n"

        digest_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

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
        return file_path