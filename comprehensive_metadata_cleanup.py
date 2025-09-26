#!/usr/bin/env python3
"""
Comprehensive Metadata Cleanup Script
Fixes mixed metadata issues including:
1. Duplicate keyword sections
2. Mixed Links formats
3. Inconsistent metadata structure
4. Multiple similar paper sections
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
        logging.FileHandler('comprehensive_metadata_cleanup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ComprehensiveMetadataCleanup:
    """Comprehensive metadata cleanup for all papers"""

    def __init__(self, papers_dir: Path):
        self.papers_dir = papers_dir
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'metadata_fixed': 0,
            'keywords_cleaned': 0,
            'links_standardized': 0,
            'duplicates_removed': 0
        }

    def clean_single_paper(self, paper_path: Path) -> bool:
        """Clean metadata issues in a single paper file"""
        try:
            content = paper_path.read_text(encoding='utf-8')
            original_content = content

            # Step 1: Extract basic metadata
            date_str = self._extract_date_from_path(paper_path)
            category = self._extract_category_from_content(content)

            if not date_str or not category:
                logger.warning(f"Could not extract date/category from: {paper_path.name}")
                return False

            # Step 2: Clean duplicate sections
            content = self._remove_duplicate_sections(content)

            # Step 3: Standardize Links section
            content = self._standardize_links_section(content, date_str, category)

            # Step 4: Clean keyword sections (remove old ones, keep AI-generated ones)
            content = self._clean_keyword_sections(content)

            # Step 5: Fix similar papers section
            content = self._fix_similar_papers_section(content)

            # Step 6: Remove any remaining duplicates
            content = self._remove_remaining_duplicates(content)

            # Check if any changes were made
            if content != original_content:
                paper_path.write_text(content, encoding='utf-8')
                self.stats['processed'] += 1
                self.stats['metadata_fixed'] += 1
                logger.info(f"✅ Cleaned: {paper_path.name}")
                return True
            else:
                logger.debug(f"⏭️ No changes needed: {paper_path.name}")
                return True

        except Exception as e:
            logger.error(f"❌ Failed to clean {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def _extract_date_from_path(self, paper_path: Path) -> Optional[str]:
        """Extract date from paper file path"""
        for part in paper_path.parts:
            if re.match(r'^\d{4}-\d{2}-\d{2}$', part):
                return part.replace('-', '')  # Convert 2025-09-22 to 20250922
        return None

    def _extract_category_from_content(self, content: str) -> Optional[str]:
        """Extract category from paper content"""
        category_pattern = r'\*\*Category\*\*:\s*([^\\n]+)'
        match = re.search(category_pattern, content)
        if match:
            return match.group(1).strip()
        return None

    def _remove_duplicate_sections(self, content: str) -> str:
        """Remove duplicate metadata sections"""
        # Find all metadata sections
        metadata_sections = list(re.finditer(r'## 📋 메타데이터', content))

        if len(metadata_sections) > 1:
            logger.info(f"Found {len(metadata_sections)} metadata sections - removing duplicates")
            # Keep only the first one
            first_end = content.find('\n##', metadata_sections[0].end())
            if first_end == -1:
                first_end = len(content)

            # Remove all subsequent metadata sections
            for i in range(len(metadata_sections) - 1, 0, -1):
                section_start = metadata_sections[i].start()
                section_end = content.find('\n##', section_start + 1)
                if section_end == -1:
                    section_end = len(content)
                else:
                    section_end = content.find('\n', section_end)

                content = content[:section_start] + content[section_end:]
                self.stats['duplicates_removed'] += 1

        return content

    def _standardize_links_section(self, content: str, date_str: str, category: str) -> str:
        """Standardize Links section format"""
        # Generate standard links
        daily_link = f"[[daily_digest_{date_str}|{date_str}]]"
        category_link = f"[[categories/{category}|{category}]]"
        standard_links = f"**Links**: {daily_link} {category_link}"

        # Find metadata section
        metadata_pattern = re.compile(r'(## 📋 메타데이터\\s*\\n)(.*?)(?=\\n## |\\n---|\\nGenerated on|\\Z)', re.DOTALL)
        metadata_match = metadata_pattern.search(content)

        if not metadata_match:
            logger.warning("No metadata section found")
            return content

        metadata_header = metadata_match.group(1)
        metadata_content = metadata_match.group(2)

        # Remove any existing Links lines
        metadata_content = re.sub(r'\\*\\*Links\\*\\*:.*?\\n', '', metadata_content)

        # Add standard links at the beginning
        updated_metadata = standard_links + '\\n' + metadata_content.lstrip()

        # Reconstruct content
        start_pos = metadata_match.start()
        end_pos = metadata_match.end()

        self.stats['links_standardized'] += 1
        return content[:start_pos] + metadata_header + updated_metadata + content[end_pos:]

    def _clean_keyword_sections(self, content: str) -> str:
        """Clean up keyword sections - remove old ones, keep AI-generated ones"""
        # Remove old-style keyword sections
        old_keyword_patterns = [
            r'## 🏷️ 추출된 키워드\\s*\\n.*?(?=\\n## |\\n---|\\Z)',
            r'## 🔗 유사한 논문\\s*\\nSimilar papers will be displayed here.*?(?=\\n## |\\n---|\\Z)'
        ]

        for pattern in old_keyword_patterns:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, '', content, flags=re.DOTALL)
                self.stats['keywords_cleaned'] += 1

        return content

    def _fix_similar_papers_section(self, content: str) -> str:
        """Fix similar papers section - remove duplicates"""
        # Find all similar papers sections
        similar_sections = list(re.finditer(r'## 🔗 유사한 논문', content))

        if len(similar_sections) > 1:
            logger.info(f"Found {len(similar_sections)} similar papers sections - removing duplicates")
            # Keep only the first one
            for i in range(len(similar_sections) - 1, 0, -1):
                section_start = similar_sections[i].start()
                section_end = content.find('\\n##', section_start + 1)
                if section_end == -1:
                    section_end = len(content)
                else:
                    section_end = content.find('\\n', section_end)

                content = content[:section_start] + content[section_end:]
                self.stats['duplicates_removed'] += 1

        return content

    def _remove_remaining_duplicates(self, content: str) -> str:
        """Remove any remaining duplicate patterns"""
        # Remove empty sections
        content = re.sub(r'\\n\\n\\n+', '\\n\\n', content)

        # Remove duplicate ArXiv ID lines
        arxiv_lines = re.findall(r'\\*\\*ArXiv ID\\*\\*:.*?\\n', content)
        if len(arxiv_lines) > 1:
            # Keep only the first occurrence
            for i in range(1, len(arxiv_lines)):
                content = content.replace(arxiv_lines[i], '', 1)
                self.stats['duplicates_removed'] += 1

        # Remove duplicate Category lines
        category_lines = re.findall(r'\\*\\*Category\\*\\*:.*?\\n', content)
        if len(category_lines) > 1:
            # Keep only the first occurrence
            for i in range(1, len(category_lines)):
                content = content.replace(category_lines[i], '', 1)
                self.stats['duplicates_removed'] += 1

        return content

    def process_all_papers(self):
        """Process all papers in the directory"""
        logger.info(f"🚀 Starting comprehensive metadata cleanup in {self.papers_dir}")

        # Find all markdown files recursively
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
        logger.info("🎉 COMPREHENSIVE METADATA CLEANUP COMPLETE")
        logger.info("=" * 80)
        logger.info(f"📊 Total files: {self.stats['total_files']}")
        logger.info(f"✅ Files processed: {self.stats['processed']}")
        logger.info(f"❌ Files failed: {self.stats['failed']}")
        logger.info(f"🔧 Metadata fixed: {self.stats['metadata_fixed']}")
        logger.info(f"🏷️ Keywords cleaned: {self.stats['keywords_cleaned']}")
        logger.info(f"🔗 Links standardized: {self.stats['links_standardized']}")
        logger.info(f"🗑️ Duplicates removed: {self.stats['duplicates_removed']}")
        logger.info("=" * 80)


def main():
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    print("🧹 Comprehensive Metadata Cleanup")
    print("=" * 50)
    print("This will:")
    print("1. Remove duplicate metadata sections")
    print("2. Standardize Links sections")
    print("3. Clean up old keyword sections")
    print("4. Fix similar papers sections")
    print("5. Remove any remaining duplicates")
    print("\\n🚀 Starting cleanup automatically...")

    cleanup = ComprehensiveMetadataCleanup(papers_dir)
    cleanup.process_all_papers()


if __name__ == "__main__":
    main()