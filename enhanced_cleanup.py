#!/usr/bin/env python3
"""
Enhanced cleanup script for remaining issues in paper files
- Remove duplicate ArXiv metadata blocks
- Remove old "추출된 키워드" sections completely
- Ensure all metadata is properly organized under "## 메타데이터" section
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Any
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('enhanced_cleanup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class EnhancedPaperCleanup:
    """Enhanced cleanup for remaining duplicate and format issues"""

    def __init__(self, papers_dir: Path):
        self.papers_dir = papers_dir
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'arxiv_duplicates_removed': 0,
            'old_keywords_removed': 0,
            'metadata_organized': 0
        }

    def clean_single_paper(self, paper_path: Path) -> bool:
        """Clean a single paper file"""
        try:
            content = paper_path.read_text(encoding='utf-8')
            original_content = content

            # Step 1: Remove duplicate ArXiv metadata blocks
            content = self._remove_duplicate_arxiv_metadata(content)

            # Step 2: Remove old "추출된 키워드" sections completely
            content = self._remove_old_keyword_sections(content)

            # Step 3: Organize metadata under proper section
            content = self._organize_metadata_section(content)

            # Check if any changes were made
            if content != original_content:
                paper_path.write_text(content, encoding='utf-8')
                self.stats['processed'] += 1

                # Track specific changes
                if self._has_duplicate_arxiv(original_content):
                    self.stats['arxiv_duplicates_removed'] += 1
                if self._has_old_keywords(original_content):
                    self.stats['old_keywords_removed'] += 1
                if self._needs_metadata_organization(original_content):
                    self.stats['metadata_organized'] += 1

                logger.info(f"✅ Cleaned: {paper_path.name}")
                return True
            else:
                logger.debug(f"⏭️ No changes needed: {paper_path.name}")
                return True

        except Exception as e:
            logger.error(f"❌ Failed to clean {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def _remove_duplicate_arxiv_metadata(self, content: str) -> str:
        """Remove duplicate ArXiv ID, Published, Category, PDF entries"""

        # Find all ArXiv ID patterns
        arxiv_pattern = r'\*\*ArXiv ID\*\*:\s*\[([^\]]+)\]\([^)]+\)'
        arxiv_matches = list(re.finditer(arxiv_pattern, content))

        if len(arxiv_matches) <= 1:
            return content  # No duplicates

        # Keep only the first occurrence, remove the rest
        for match in reversed(arxiv_matches[1:]):  # Remove from end to avoid index issues
            start, end = match.span()
            # Look for the entire line including newlines
            line_start = content.rfind('\n', 0, start) + 1
            line_end = content.find('\n', end)
            if line_end == -1:
                line_end = len(content)
            else:
                line_end += 1  # Include the newline

            content = content[:line_start] + content[line_end:]

        # Also remove duplicate Published, Category, PDF lines
        for field in ['Published', 'Category', 'PDF']:
            pattern = rf'\*\*{field}\*\*:[^\n]*\n'
            matches = list(re.finditer(pattern, content))

            if len(matches) > 1:
                # Remove all but the first
                for match in reversed(matches[1:]):
                    start, end = match.span()
                    content = content[:start] + content[end:]

        return content

    def _remove_old_keyword_sections(self, content: str) -> str:
        """Remove old '추출된 키워드' sections completely"""

        # Pattern to match the old keyword section
        old_keyword_pattern = re.compile(
            r'## 🏷️ 추출된 키워드\s*\n\n.*?(?=\n## |\n---|\nGenerated on|\Z)',
            re.DOTALL
        )

        content = old_keyword_pattern.sub('', content)

        # Also remove any remaining individual keyword lines with backticks
        content = re.sub(r'^`[^`]+`\s*•\s*\n\n', '', content, flags=re.MULTILINE)

        # Clean up any double newlines that might be left
        content = re.sub(r'\n\n\n+', '\n\n', content)

        return content

    def _organize_metadata_section(self, content: str) -> str:
        """Organize all metadata under proper '## 📋 메타데이터' section"""

        # Check if metadata section exists
        metadata_pattern = re.compile(r'## 📋 메타데이터\s*\n')
        metadata_match = metadata_pattern.search(content)

        if not metadata_match:
            # Create metadata section after title
            title_pattern = re.compile(r'^# .+\n\n', re.MULTILINE)
            title_match = title_pattern.search(content)

            if title_match:
                insert_pos = title_match.end()
                # Add Korean title if it exists
                korean_title_pattern = re.compile(r'\*\*Korean Title:\*\*[^\n]*\n\n')
                korean_match = korean_title_pattern.search(content, insert_pos)

                if korean_match:
                    insert_pos = korean_match.end()

                content = content[:insert_pos] + "## 📋 메타데이터\n\n" + content[insert_pos:]

        # Find scattered metadata and move it to metadata section
        metadata_items = []

        # Patterns for metadata that should be under 메타데이터 section
        metadata_patterns = [
            r'\*\*ArXiv ID\*\*:[^\n]*\n',
            r'\*\*Published\*\*:[^\n]*\n',
            r'\*\*Category\*\*:[^\n]*\n',
            r'\*\*PDF\*\*:[^\n]*\n'
        ]

        # Extract metadata items and remove from their current locations
        for pattern in metadata_patterns:
            matches = list(re.finditer(pattern, content))
            for match in reversed(matches):  # Remove from end to avoid index issues
                metadata_items.insert(0, match.group().strip())
                content = content[:match.start()] + content[match.end():]

        # Insert metadata items under the metadata section
        if metadata_items:
            metadata_pattern = re.compile(r'(## 📋 메타데이터\s*\n)')
            metadata_content = '\n'.join(metadata_items) + '\n\n'
            content = metadata_pattern.sub(r'\1\n' + metadata_content, content)

        # Clean up any excessive newlines
        content = re.sub(r'\n\n\n+', '\n\n', content)

        return content

    def _has_duplicate_arxiv(self, content: str) -> bool:
        """Check if content has duplicate ArXiv metadata"""
        arxiv_pattern = r'\*\*ArXiv ID\*\*:'
        return len(re.findall(arxiv_pattern, content)) > 1

    def _has_old_keywords(self, content: str) -> bool:
        """Check if content has old keyword sections"""
        return '## 🏷️ 추출된 키워드' in content

    def _needs_metadata_organization(self, content: str) -> bool:
        """Check if metadata needs to be organized"""
        # Check if ArXiv metadata exists outside of metadata section
        metadata_section_pattern = re.compile(r'## 📋 메타데이터\s*\n(.*?)(?=\n## |\Z)', re.DOTALL)
        metadata_match = metadata_section_pattern.search(content)

        if not metadata_match:
            return True  # No metadata section at all

        metadata_section = metadata_match.group(1)

        # Check if ArXiv info is outside the metadata section
        arxiv_pattern = r'\*\*ArXiv ID\*\*:'
        total_arxiv = len(re.findall(arxiv_pattern, content))
        section_arxiv = len(re.findall(arxiv_pattern, metadata_section))

        return total_arxiv > section_arxiv

    def process_all_papers(self):
        """Process all papers in the directory"""
        logger.info(f"🚀 Starting enhanced cleanup in {self.papers_dir}")

        # Find all markdown files
        paper_files = list(self.papers_dir.rglob("*.md"))
        self.stats['total_files'] = len(paper_files)

        logger.info(f"📊 Found {len(paper_files)} paper files")

        # Process each file
        for i, paper_path in enumerate(paper_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(paper_files)} ({i/len(paper_files)*100:.1f}%)")

            self.clean_single_paper(paper_path)

        # Print final statistics
        logger.info("=" * 80)
        logger.info("🎉 ENHANCED CLEANUP COMPLETE")
        logger.info("=" * 80)
        logger.info(f"📊 Total files: {self.stats['total_files']}")
        logger.info(f"✅ Files processed: {self.stats['processed']}")
        logger.info(f"❌ Files failed: {self.stats['failed']}")
        logger.info(f"🔧 ArXiv duplicates removed: {self.stats['arxiv_duplicates_removed']}")
        logger.info(f"🗑️ Old keyword sections removed: {self.stats['old_keywords_removed']}")
        logger.info(f"📋 Metadata sections organized: {self.stats['metadata_organized']}")
        logger.info("=" * 80)


def main():
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    # Show what will be done
    print("🔧 Enhanced Paper Cleanup")
    print("=" * 50)
    print("This will:")
    print("1. Remove duplicate ArXiv metadata blocks")
    print("2. Remove old '추출된 키워드' sections completely")
    print("3. Organize all metadata under '## 📋 메타데이터' section")
    print("\n🚀 Starting cleanup automatically...")

    cleanup = EnhancedPaperCleanup(papers_dir)
    cleanup.process_all_papers()


if __name__ == "__main__":
    main()