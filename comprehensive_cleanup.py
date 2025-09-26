#!/usr/bin/env python3
"""
Comprehensive cleanup script for all individual papers
1. Remove duplicate metadata sections
2. Remove existing keyword information
3. Apply new keyword extraction system
"""

import re
import json
import os
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('comprehensive_cleanup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ComprehensiveCleanup:
    """Comprehensive cleanup for all paper files"""

    def __init__(self, papers_dir: Path):
        self.papers_dir = papers_dir
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'duplicates_removed': 0,
            'keywords_removed': 0,
            'failed': 0,
            'skipped': 0
        }

    def clean_duplicate_metadata(self, content: str) -> Tuple[str, bool]:
        """Remove duplicate metadata sections"""
        original_content = content
        changes_made = False

        # 1. Remove duplicate metadata headers - keep only the first one
        metadata_headers = list(re.finditer(r'^## 📋 메타데이터\s*$', content, re.MULTILINE))
        if len(metadata_headers) > 1:
            logger.debug("Found multiple metadata headers, removing duplicates")
            # Remove all subsequent metadata headers and their content
            for i in range(len(metadata_headers) - 1, 0, -1):
                start_pos = metadata_headers[i].start()
                # Find the end of this metadata section (next ## section or end)
                next_section = re.search(r'\n## ', content[start_pos + 1:])
                if next_section:
                    end_pos = start_pos + 1 + next_section.start()
                else:
                    end_pos = len(content)

                content = content[:start_pos] + content[end_pos:]
                changes_made = True

        # 2. Remove duplicate "🏷️ 카테고리화된 키워드" sections
        keyword_sections = list(re.finditer(r'^## 🏷️ 카테고리화된 키워드', content, re.MULTILINE))
        if len(keyword_sections) > 1:
            logger.debug("Found multiple keyword sections, removing duplicates")
            for i in range(len(keyword_sections) - 1, 0, -1):
                start_pos = keyword_sections[i].start()
                # Find the end of this section
                next_section = re.search(r'\n## ', content[start_pos + 1:])
                if next_section:
                    end_pos = start_pos + 1 + next_section.start()
                else:
                    end_pos = len(content)

                content = content[:start_pos] + content[end_pos:]
                changes_made = True

        # 3. Remove standalone ArXiv metadata blocks that appear outside metadata section
        arxiv_pattern = re.compile(
            r'^\*\*ArXiv ID:\*\*.*?\n\*\*Published:\*\*.*?\n\*\*Categories:\*\*.*?\n',
            re.MULTILINE | re.DOTALL
        )

        # Only remove if it's not within the metadata section
        metadata_section_match = re.search(r'## 📋 메타데이터.*?(?=\n## |\n# |$)', content, re.DOTALL)

        for match in arxiv_pattern.finditer(content):
            if metadata_section_match and (
                match.start() < metadata_section_match.start() or
                match.end() > metadata_section_match.end()
            ):
                content = content.replace(match.group(), '')
                changes_made = True

        # 4. Remove orphaned keyword lines (카테고리화된 키워드 content without header)
        orphaned_keywords = re.findall(
            r'^\*\*🚀 Evolved Concepts\*\*:.*?\n|^\*\*🔗 Specific Connectable\*\*:.*?\n|^\*\*⚡ Unique Technical\*\*:.*?\n|^\*\*🌐 Broad Technical\*\*:.*?\n',
            content,
            re.MULTILINE
        )

        for orphan in orphaned_keywords:
            # Only remove if it's not under a proper section header
            orphan_pos = content.find(orphan)
            preceding_section = content.rfind('## 🏷️ 카테고리화된 키워드', 0, orphan_pos)
            next_section = content.find('\n## ', orphan_pos)

            if preceding_section == -1 or (next_section != -1 and next_section < orphan_pos + len(orphan)):
                content = content.replace(orphan, '')
                changes_made = True

        # 5. Remove duplicate "🔗 유사한 논문" sections
        similar_sections = list(re.finditer(r'^## 🔗 유사한 논문', content, re.MULTILINE))
        if len(similar_sections) > 1:
            logger.debug("Found multiple similar papers sections, removing duplicates")
            for i in range(len(similar_sections) - 1, 0, -1):
                start_pos = similar_sections[i].start()
                next_section = re.search(r'\n## ', content[start_pos + 1:])
                if next_section:
                    end_pos = start_pos + 1 + next_section.start()
                else:
                    end_pos = len(content)

                content = content[:start_pos] + content[end_pos:]
                changes_made = True

        return content, changes_made

    def remove_existing_keywords(self, content: str) -> Tuple[str, bool]:
        """Remove existing keyword sections completely"""
        original_content = content

        # Remove the entire 카테고리화된 키워드 section
        keyword_pattern = re.compile(
            r'## 🏷️ 카테고리화된 키워드.*?(?=\n## |\n# |$)',
            re.DOTALL
        )

        match = keyword_pattern.search(content)
        if match:
            content = keyword_pattern.sub('', content)
            # Clean up extra newlines
            content = re.sub(r'\n{3,}', '\n\n', content)
            return content, True

        return content, False

    def process_single_file(self, file_path: Path) -> bool:
        """Process a single paper file"""
        try:
            self.stats['total_files'] += 1

            # Read current content
            content = file_path.read_text(encoding='utf-8')
            original_content = content

            # Step 1: Remove duplicate metadata
            content, duplicates_removed = self.clean_duplicate_metadata(content)
            if duplicates_removed:
                self.stats['duplicates_removed'] += 1
                logger.debug(f"Removed duplicates from {file_path.name}")

            # Step 2: Remove existing keywords
            content, keywords_removed = self.remove_existing_keywords(content)
            if keywords_removed:
                self.stats['keywords_removed'] += 1
                logger.debug(f"Removed keywords from {file_path.name}")

            # Write back if changes were made
            if content != original_content:
                file_path.write_text(content, encoding='utf-8')
                self.stats['processed'] += 1
                logger.info(f"Processed {file_path.name}")
                return True
            else:
                self.stats['skipped'] += 1
                return True

        except Exception as e:
            self.stats['failed'] += 1
            logger.error(f"Failed to process {file_path}: {e}")
            return False

    def process_all_files(self) -> Dict[str, int]:
        """Process all paper files in the directory"""
        logger.info(f"Starting comprehensive cleanup in {self.papers_dir}")

        # Find all markdown files
        paper_files = list(self.papers_dir.rglob("*.md"))
        logger.info(f"Found {len(paper_files)} paper files to process")

        # Process each file
        for i, paper_path in enumerate(paper_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(paper_files)} files processed")

            self.process_single_file(paper_path)

        # Final statistics
        logger.info("Comprehensive cleanup completed!")
        logger.info(f"Total files: {self.stats['total_files']}")
        logger.info(f"Processed: {self.stats['processed']}")
        logger.info(f"Duplicates removed: {self.stats['duplicates_removed']}")
        logger.info(f"Keywords removed: {self.stats['keywords_removed']}")
        logger.info(f"Failed: {self.stats['failed']}")
        logger.info(f"Skipped: {self.stats['skipped']}")

        return self.stats


def main():
    """Main execution function"""
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    cleanup = ComprehensiveCleanup(papers_dir)
    stats = cleanup.process_all_files()

    print("\n" + "="*60)
    print("📊 COMPREHENSIVE CLEANUP RESULTS")
    print("="*60)
    print(f"Total files scanned: {stats['total_files']}")
    print(f"Files modified: {stats['processed']}")
    print(f"Files with duplicates removed: {stats['duplicates_removed']}")
    print(f"Files with keywords removed: {stats['keywords_removed']}")
    print(f"Files failed: {stats['failed']}")
    print(f"Files skipped (no changes): {stats['skipped']}")
    print("="*60)


if __name__ == "__main__":
    main()