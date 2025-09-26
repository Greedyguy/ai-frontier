#!/usr/bin/env python3
"""
AI Processed Files Cleanup Script
Specifically targets files that have AI-generated keywords but mixed metadata
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ai_processed_cleanup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AIProcessedCleanup:
    """Cleanup for files already processed by AI keyword extraction"""

    def __init__(self, papers_dir: Path):
        self.papers_dir = papers_dir
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'ai_processed_found': 0,
            'metadata_cleaned': 0,
            'links_fixed': 0
        }

    def clean_ai_processed_file(self, paper_path: Path) -> bool:
        """Clean a file that has been processed by AI keyword extraction"""
        try:
            content = paper_path.read_text(encoding='utf-8')
            original_content = content

            # Check if this file has AI-generated keywords
            if not self._has_ai_keywords(content):
                return True  # Skip files not processed by AI yet

            self.stats['ai_processed_found'] += 1

            # Extract metadata for reconstruction
            date_str = self._extract_date_from_path(paper_path)
            category = self._extract_category_from_content(content)

            if not date_str or not category:
                logger.warning(f"Could not extract date/category from: {paper_path.name}")
                return False

            # Clean and rebuild the file
            content = self._rebuild_clean_file(content, date_str, category)

            # Check if any changes were made
            if content != original_content:
                paper_path.write_text(content, encoding='utf-8')
                self.stats['processed'] += 1
                self.stats['metadata_cleaned'] += 1
                logger.info(f"✅ Cleaned AI-processed: {paper_path.name}")
                return True
            else:
                logger.debug(f"⏭️ No changes needed: {paper_path.name}")
                return True

        except Exception as e:
            logger.error(f"❌ Failed to clean {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def _has_ai_keywords(self, content: str) -> bool:
        """Check if file has AI-generated keywords with HTML metadata"""
        return '<!-- KEYWORD_LINKING_METADATA:' in content

    def _extract_date_from_path(self, paper_path: Path) -> Optional[str]:
        """Extract date from paper file path"""
        for part in paper_path.parts:
            if re.match(r'^\d{4}-\d{2}-\d{2}$', part):
                return part.replace('-', '')  # Convert 2025-09-22 to 20250922
        return None

    def _extract_category_from_content(self, content: str) -> Optional[str]:
        """Extract category from paper content"""
        category_pattern = r'\*\*Category\*\*:\s*([^\n]+)'
        match = re.search(category_pattern, content)
        if match:
            return match.group(1).strip()
        return None

    def _rebuild_clean_file(self, content: str, date_str: str, category: str) -> str:
        """Rebuild file with clean metadata structure"""

        # Extract core components
        title = self._extract_title(content)
        korean_title = self._extract_korean_title(content)
        arxiv_id = self._extract_arxiv_id(content)
        published_date = self._extract_published_date(content)
        pdf_url = self._extract_pdf_url(content)
        similar_papers = self._extract_similar_papers(content)
        ai_keywords = self._extract_ai_keywords(content)
        abstract_original = self._extract_abstract_original(content)
        abstract_korean = self._extract_abstract_korean(content)
        summary = self._extract_summary(content)
        key_points = self._extract_key_points(content)
        generated_date = self._extract_generated_date(content)

        # Generate clean Links section
        daily_link = f"[[daily_digest_{date_str}|{date_str}]]"
        category_link = f"[[categories/{category}|{category}]]"
        clean_links = f"**Links**: {daily_link} {category_link}"

        # Rebuild file from scratch
        clean_content = []

        # AI keyword metadata (keep at top)
        keyword_metadata = self._extract_keyword_metadata(content)
        if keyword_metadata:
            clean_content.append(keyword_metadata)
            clean_content.append("")

        # Title and Korean title
        clean_content.append(f"# {title}")
        clean_content.append("")
        clean_content.append(f"**Korean Title:** {korean_title}")
        clean_content.append("")

        # Metadata section
        clean_content.append("## 📋 메타데이터")
        clean_content.append("")
        clean_content.append(clean_links)
        clean_content.append(f"**PDF**: [Download](https://arxiv.org/pdf/{arxiv_id}.pdf)")
        clean_content.append(f"**Category**: {category}")
        clean_content.append(f"**Published**: {published_date}")
        clean_content.append(f"**ArXiv ID**: [{arxiv_id}](https://arxiv.org/abs/{arxiv_id})")
        clean_content.append("")

        # Similar papers section
        if similar_papers:
            clean_content.append("## 🔗 유사한 논문")
            clean_content.extend(similar_papers)
            clean_content.append("")

        # AI Keywords section
        if ai_keywords:
            clean_content.append("## 🏷️ 카테고리화된 키워드")
            clean_content.extend(ai_keywords)
            clean_content.append("")

        # Authors section
        clean_content.append("## 📋 저자 정보")
        clean_content.append("")
        clean_content.append("**Authors:** ")
        clean_content.append("")

        # Abstract sections
        if abstract_original:
            clean_content.append("## 📄 Abstract (원문)")
            clean_content.append("")
            clean_content.append(abstract_original)
            clean_content.append("")

        if abstract_korean:
            clean_content.append("## 🔍 Abstract (한글 번역)")
            clean_content.append("")
            clean_content.append(abstract_korean)
            clean_content.append("")

        # Summary section
        if summary:
            clean_content.append("## 📝 요약")
            clean_content.append("")
            clean_content.append(summary)
            clean_content.append("")

        # Key points section
        if key_points:
            clean_content.append("## 🎯 주요 포인트")
            clean_content.append("")
            clean_content.extend(key_points)
            clean_content.append("")

        # Footer
        clean_content.append("---")
        clean_content.append("")
        if generated_date:
            clean_content.append(f"*Generated on {generated_date}*")
        else:
            clean_content.append("*Generated on 2025-09-22 21:35:00*")

        return '\n'.join(clean_content)

    def _extract_keyword_metadata(self, content: str) -> Optional[str]:
        """Extract AI keyword metadata"""
        match = re.search(r'<!-- KEYWORD_LINKING_METADATA:.*?-->', content, re.DOTALL)
        return match.group(0) if match else None

    def _extract_title(self, content: str) -> str:
        """Extract main title"""
        match = re.search(r'^# ([^\n]+)', content, re.MULTILINE)
        return match.group(1) if match else "Unknown Title"

    def _extract_korean_title(self, content: str) -> str:
        """Extract Korean title"""
        match = re.search(r'\*\*Korean Title:\*\* ([^\n]+)', content)
        return match.group(1) if match else "Unknown Korean Title"

    def _extract_arxiv_id(self, content: str) -> str:
        """Extract ArXiv ID"""
        match = re.search(r'\*\*ArXiv ID\*\*: \[([^\]]+)\]', content)
        return match.group(1) if match else "unknown.id"

    def _extract_published_date(self, content: str) -> str:
        """Extract published date"""
        match = re.search(r'\*\*Published\*\*: ([^\n]+)', content)
        return match.group(1) if match else "Unknown"

    def _extract_pdf_url(self, content: str) -> str:
        """Extract PDF URL"""
        match = re.search(r'\*\*PDF\*\*: \[Download\]\(([^\)]+)\)', content)
        return match.group(1) if match else ""

    def _extract_similar_papers(self, content: str) -> List[str]:
        """Extract similar papers section"""
        similar_match = re.search(r'## 🔗 유사한 논문\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        if similar_match:
            lines = similar_match.group(1).strip().split('\n')
            return [line for line in lines if line.strip() and line.startswith('-')]
        return []

    def _extract_ai_keywords(self, content: str) -> List[str]:
        """Extract AI-generated keywords"""
        keyword_match = re.search(r'## 🏷️ 카테고리화된 키워드\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        if keyword_match:
            lines = keyword_match.group(1).strip().split('\n')
            return [line for line in lines if line.strip()]
        return []

    def _extract_abstract_original(self, content: str) -> str:
        """Extract original abstract"""
        match = re.search(r'## 📄 Abstract \(원문\)\s*\n\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        return match.group(1).strip() if match else ""

    def _extract_abstract_korean(self, content: str) -> str:
        """Extract Korean abstract"""
        match = re.search(r'## 🔍 Abstract \(한글 번역\)\s*\n\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        return match.group(1).strip() if match else ""

    def _extract_summary(self, content: str) -> str:
        """Extract summary"""
        match = re.search(r'## 📝 요약\s*\n\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        return match.group(1).strip() if match else ""

    def _extract_key_points(self, content: str) -> List[str]:
        """Extract key points"""
        points_match = re.search(r'## 🎯 주요 포인트\s*\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        if points_match:
            lines = points_match.group(1).strip().split('\n')
            return [line for line in lines if line.strip()]
        return []

    def _extract_generated_date(self, content: str) -> Optional[str]:
        """Extract generated date"""
        match = re.search(r'\*Generated on ([^\*]+)\*', content)
        return match.group(1) if match else None

    def process_all_papers(self):
        """Process all papers in the directory"""
        logger.info(f"🚀 Starting AI-processed files cleanup in {self.papers_dir}")

        # Find all markdown files recursively
        paper_files = list(self.papers_dir.rglob("*.md"))
        self.stats['total_files'] = len(paper_files)

        logger.info(f"📊 Found {len(paper_files)} paper files")

        # Process each file
        for i, paper_path in enumerate(paper_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(paper_files)} ({i/len(paper_files)*100:.1f}%)")

            self.clean_ai_processed_file(paper_path)

        # Print final statistics
        logger.info("=" * 80)
        logger.info("🎉 AI PROCESSED FILES CLEANUP COMPLETE")
        logger.info("=" * 80)
        logger.info(f"📊 Total files: {self.stats['total_files']}")
        logger.info(f"🤖 AI-processed files found: {self.stats['ai_processed_found']}")
        logger.info(f"✅ Files cleaned: {self.stats['processed']}")
        logger.info(f"❌ Files failed: {self.stats['failed']}")
        logger.info(f"🔧 Metadata cleaned: {self.stats['metadata_cleaned']}")
        logger.info("=" * 80)


def main():
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    print("🤖 AI Processed Files Cleanup")
    print("=" * 50)
    print("This will:")
    print("1. Find files with AI-generated keywords")
    print("2. Rebuild them with clean metadata structure")
    print("3. Remove duplicate sections")
    print("4. Standardize Links sections")
    print("\n🚀 Starting cleanup automatically...")

    cleanup = AIProcessedCleanup(papers_dir)
    cleanup.process_all_papers()


if __name__ == "__main__":
    main()