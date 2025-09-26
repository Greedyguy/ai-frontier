"""Report generation service."""

from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import json
import markdown
import re
from jinja2 import Template

from ..arxiv.client import ArxivPaper
from ..utils.obsidian_formatter import ObsidianFormatter

class ReportGenerator:
    """Generate reports from arxiv papers."""

    def __init__(self, template_dir: Optional[Path] = None):
        self.template_dir = template_dir or Path(__file__).parent / "templates"
        self.template_dir.mkdir(exist_ok=True)
        self.obsidian_formatter = ObsidianFormatter(enable_similarity=True)

    def generate_daily_report(
        self,
        papers: List[ArxivPaper],
        translations: Dict[str, str],
        summaries: Dict[str, str],
        key_points: Dict[str, List[str]],
        output_format: str = "markdown"
    ) -> str:
        """Generate daily report from papers and analysis."""

        report_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "total_papers": len(papers),
            "papers": []
        }

        for paper in papers:
            paper_data = {
                "title": paper.title,
                "title_ko": translations.get(f"{paper.arxiv_id}_title", paper.title),
                "authors": ", ".join(paper.authors),
                "arxiv_id": paper.arxiv_id,
                "published": paper.published.strftime("%Y-%m-%d"),
                "category": paper.category,
                "abstract": paper.abstract,
                "abstract_ko": translations.get(f"{paper.arxiv_id}_abstract", ""),
                "summary": summaries.get(paper.arxiv_id, ""),
                "key_points": key_points.get(paper.arxiv_id, []),
                "pdf_url": paper.pdf_url
            }
            report_data["papers"].append(paper_data)

        if output_format.lower() == "markdown":
            return self._generate_markdown_report(report_data)
        elif output_format.lower() == "html":
            return self._generate_html_report(report_data)
        elif output_format.lower() == "json":
            return json.dumps(report_data, indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

    def _generate_markdown_report(self, data: Dict[str, Any]) -> str:
        """Generate markdown report."""
        template_str = """
# ArXiv Daily Report - {{ date }}

**총 논문 수: {{ total_papers }}**

---

{% for paper in papers %}
## {{ loop.index }}. {{ paper.title }}

**Korean Title:** {{ paper.title_ko }}

**Authors:** {{ paper.authors }}
**ArXiv ID:** [{{ paper.arxiv_id }}](https://arxiv.org/abs/{{ paper.arxiv_id }})
**Published:** {{ paper.published }}
**Category:** {{ paper.category }}
**PDF:** [Download]({{ paper.pdf_url }})

### Abstract (한글 번역)
{{ paper.abstract_ko }}

### 요약
{{ paper.summary }}

### 주요 포인트
{% for point in paper.key_points %}
- {{ point }}
{% endfor %}

---

{% endfor %}

*Report generated on {{ date }}*
"""
        template = Template(template_str)
        return template.render(**data)

    def _generate_html_report(self, data: Dict[str, Any]) -> str:
        """Generate HTML report."""
        markdown_content = self._generate_markdown_report(data)
        html_content = markdown.markdown(
            markdown_content,
            extensions=['fenced_code', 'tables', 'toc']
        )

        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ArXiv Daily Report - {data['date']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1, h2, h3 {{ color: #333; }}
        .paper {{ border: 1px solid #ddd; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        .abstract {{ background-color: #f8f9fa; padding: 10px; border-left: 4px solid #007bff; }}
        .summary {{ background-color: #e8f5e9; padding: 10px; border-left: 4px solid #4caf50; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
        return html_template

    def _sanitize_filename(self, filename: str) -> str:
        """파일명에서 불법 문자 제거 - 콜론만 언더스코어로 변경, 띄어쓰기는 유지"""
        # 콜론만 언더스코어로 변경
        sanitized = filename.replace(':', '_')
        # 다른 금지된 문자들 제거 (띄어쓰기는 유지)
        illegal_chars = r'[<>"/\\|?*\x00-\x1f]'
        sanitized = re.sub(illegal_chars, '', sanitized)
        # 연속된 언더스코어를 하나로 변경
        sanitized = re.sub(r'_+', '_', sanitized)
        # 앞뒤 공백과 점 제거
        sanitized = sanitized.strip(' .')
        # 빈 문자열인 경우 기본값 사용
        if not sanitized:
            sanitized = "untitled"
        return sanitized
    
    def generate_individual_paper_file(
        self,
        paper: ArxivPaper,
        translations: Dict[str, str],
        summaries: Dict[str, str],
        key_points: Dict[str, List[str]],
        keywords: Dict[str, List[str]] = None,
        output_format: str = "markdown"
    ) -> str:
        """개별 논문 파일 내용 생성"""
        
        # Get summary and key points for LLM-based keyword extraction
        summary = summaries.get(paper.arxiv_id, "")
        paper_key_points = key_points.get(paper.arxiv_id, [])

        # Extract keywords using LLM with summary and key points
        extracted_keywords = self.obsidian_formatter._extract_keywords_from_paper(
            paper, summary, paper_key_points
        )

        # Generate Obsidian metadata with enriched context
        obsidian_metadata = self.obsidian_formatter.generate_metadata_section(
            paper, summary, paper_key_points
        )

        # Generate categorized keywords display
        try:
            categorized_keywords = self.obsidian_formatter.keyword_extractor.extract_keywords(paper.title, paper.abstract)
            keywords_display = []
            category_names = {
                "evolved_concepts": "🚀 Evolved Concepts",
                "specific_connectable": "🔗 Specific Connectable",
                "unique_technical": "⭐ Unique Technical",
                "broad_technical": "🔬 Broad Technical"
            }
            for category in ["evolved_concepts", "specific_connectable", "unique_technical", "broad_technical"]:
                if category in categorized_keywords and categorized_keywords[category]:
                    category_display = category_names.get(category, category)
                    keywords_str = ", ".join(categorized_keywords[category])
                    keywords_display.append(f"**{category_display}**: {keywords_str}")
            categorized_keywords_display = "\n".join(keywords_display) if keywords_display else "No categorized keywords extracted"
        except Exception as e:
            print(f"Error generating categorized keywords display: {e}")
            categorized_keywords_display = "Error extracting categorized keywords"

        # Generate similar papers display (placeholder for now)
        similar_papers_display = "Similar papers will be displayed here based on embedding similarity."

        paper_data = {
            "title": paper.title,
            "title_ko": translations.get(f"{paper.arxiv_id}_title", paper.title),
            "authors": ", ".join(paper.authors),
            "arxiv_id": paper.arxiv_id,
            "published": paper.published.strftime("%Y-%m-%d"),
            "category": paper.category,
            "abstract": paper.abstract,
            "abstract_ko": translations.get(f"{paper.arxiv_id}_abstract", ""),
            "summary": summaries.get(paper.arxiv_id, ""),
            "key_points": key_points.get(paper.arxiv_id, []),
            "keywords": keywords.get(paper.arxiv_id, []) if keywords else [],
            "extracted_keywords": extracted_keywords,
            "obsidian_metadata": obsidian_metadata,
            "categorized_keywords_display": categorized_keywords_display,
            "similar_papers_display": similar_papers_display,
            "pdf_url": paper.pdf_url,
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if output_format.lower() == "markdown":
            return self._generate_individual_markdown(paper_data)
        elif output_format.lower() == "html":
            return self._generate_individual_html(paper_data)
        elif output_format.lower() == "json":
            return json.dumps(paper_data, indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_individual_markdown(self, paper_data: Dict[str, Any]) -> str:
        """개별 논문 마크다운 생성"""
        template_str = """# {{ title }}

**Korean Title:** {{ title_ko }}

## 📋 메타데이터

{{ obsidian_metadata }}

**ArXiv ID**: [{{ arxiv_id }}](https://arxiv.org/abs/{{ arxiv_id }})
**Published**: {{ published }}
**Category**: {{ category }}
**PDF**: [Download]({{ pdf_url }})

## 🏷️ 카테고리화된 키워드
{{ categorized_keywords_display }}

## 🏷️ 추출된 키워드

{% if extracted_keywords %}
{% for keyword in extracted_keywords %}
`{{ keyword }}`{% if not loop.last %} • {% endif %}
{% endfor %}
{% else %}
키워드가 추출되지 않았습니다.
{% endif %}

## 🔗 유사한 논문

{{ similar_papers_display }}

## 📋 저자 정보

**Authors:** {{ authors }}

## 📄 Abstract (원문)

{{ abstract }}

## 🔍 Abstract (한글 번역)

{{ abstract_ko }}

## 📝 요약

{{ summary }}

## 🎯 주요 포인트

{% for point in key_points %}
- {{ point }}
{% endfor %}

---

*Generated on {{ generation_date }}*
"""
        template = Template(template_str)
        return template.render(**paper_data)
    
    def _generate_individual_html(self, paper_data: Dict[str, Any]) -> str:
        """개별 논문 HTML 생성"""
        markdown_content = self._generate_individual_markdown(paper_data)
        html_content = markdown.markdown(
            markdown_content,
            extensions=['fenced_code', 'tables', 'toc']
        )

        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{paper_data['title']}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
               max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        h1, h2, h3 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        .info-section {{ background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .abstract {{ background-color: #e3f2fd; padding: 15px; border-left: 4px solid #2196f3; margin: 15px 0; }}
        .summary {{ background-color: #e8f5e9; padding: 15px; border-left: 4px solid #4caf50; margin: 15px 0; }}
        .key-points {{ background-color: #fff3e0; padding: 15px; border-left: 4px solid #ff9800; margin: 15px 0; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 8px 0; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
        return html_template

    def save_individual_paper_files(
        self,
        papers: List[ArxivPaper],
        translations: Dict[str, str],
        summaries: Dict[str, str],
        key_points: Dict[str, List[str]],
        keywords: Dict[str, List[str]] = None,
        output_dir: Path = None,
        output_format: str = "markdown"
    ) -> List[Path]:
        """개별 논문 파일들을 저장 (날짜별 폴더 구조)"""
        if output_dir is None:
            output_dir = Path("reports") / "individual_papers"

        saved_files = []

        for paper in papers:
            # 날짜별 폴더 생성
            date_str = paper.published.strftime("%Y-%m-%d")  # YYYY-MM-DD 형태
            date_dir = output_dir / date_str
            date_dir.mkdir(parents=True, exist_ok=True)

            # 파일명 생성: 원문 제목_날짜
            filename_base = f"{self._sanitize_filename(paper.title)}_{paper.published.strftime('%Y%m%d')}"

            # 확장자 결정
            if output_format.lower() == "markdown":
                filename = f"{filename_base}.md"
            elif output_format.lower() == "html":
                filename = f"{filename_base}.html"
            elif output_format.lower() == "json":
                filename = f"{filename_base}.json"
            else:
                filename = f"{filename_base}.txt"

            # 파일 내용 생성
            content = self.generate_individual_paper_file(
                paper, translations, summaries, key_points, keywords, output_format
            )

            # 파일 저장 (날짜 폴더 하위에 저장)
            file_path = date_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            saved_files.append(file_path)

        return saved_files

    def save_report(self, content: str, filename: str, output_dir: Path = None) -> Path:
        """Save report to file."""
        if output_dir is None:
            output_dir = Path("reports")

        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / filename

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path