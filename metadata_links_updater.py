#!/usr/bin/env python3
"""
Metadata Links Updater
Updates all paper files to have standardized **Links** section with:
- daily_digest_YYYYMMDD
- categories/CATEGORY
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
        logging.FileHandler('metadata_links_updater.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MetadataLinksUpdater:
    """Updates metadata Links sections in all papers"""

    def __init__(self, papers_dir: Path):
        self.papers_dir = papers_dir
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'links_added': 0,
            'links_updated': 0
        }

    def update_single_paper(self, paper_path: Path) -> bool:
        """Update Links section in a single paper file"""
        try:
            content = paper_path.read_text(encoding='utf-8')
            original_content = content

            # Extract date from file path
            date_str = self._extract_date_from_path(paper_path)
            if not date_str:
                logger.warning(f"Could not extract date from path: {paper_path}")
                return False

            # Extract category from content
            category = self._extract_category_from_content(content)
            if not category:
                logger.warning(f"Could not extract category from: {paper_path.name}")
                return False

            # Generate new Links section
            new_links_section = self._generate_links_section(date_str, category)

            # Update or add Links section
            content = self._update_links_section(content, new_links_section)

            # Check if any changes were made
            if content != original_content:
                paper_path.write_text(content, encoding='utf-8')
                self.stats['processed'] += 1

                # Track if links were added or updated
                if '**Links**:' in original_content:
                    self.stats['links_updated'] += 1
                else:
                    self.stats['links_added'] += 1

                logger.info(f"✅ Updated: {paper_path.name}")
                return True
            else:
                logger.debug(f"⏭️ No changes needed: {paper_path.name}")
                return True

        except Exception as e:
            logger.error(f"❌ Failed to update {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def _extract_date_from_path(self, paper_path: Path) -> Optional[str]:
        """Extract date from paper file path"""
        # Look for date pattern in path parts
        for part in paper_path.parts:
            if re.match(r'^\d{4}-\d{2}-\d{2}$', part):
                return part.replace('-', '')  # Convert 2025-09-22 to 20250922
        return None

    def _extract_category_from_content(self, content: str) -> Optional[str]:
        """Extract category from paper content"""
        # Look for **Category**: pattern
        category_pattern = r'\*\*Category\*\*:\s*([^\n]+)'
        match = re.search(category_pattern, content)
        if match:
            return match.group(1).strip()
        return None

    def _generate_links_section(self, date_str: str, category: str) -> str:
        """Generate standardized Links section"""
        daily_link = f"[[daily_digest_{date_str}|{date_str}]]"
        category_link = f"[[categories/{category}|{category}]]"

        return f"**Links**: {daily_link} {category_link}"

    def _update_links_section(self, content: str, new_links_section: str) -> str:
        """Update or add Links section in metadata"""

        # Check if metadata section exists
        metadata_pattern = re.compile(r'(## 📋 메타데이터\s*\n)(.*?)(?=\n## |\n---|\nGenerated on|\Z)', re.DOTALL)
        metadata_match = metadata_pattern.search(content)

        if not metadata_match:
            logger.warning("No metadata section found")
            return content

        metadata_header = metadata_match.group(1)
        metadata_content = metadata_match.group(2)

        # Check if Links already exists in metadata
        links_pattern = r'\*\*Links\*\*:.*?\n'

        if re.search(links_pattern, metadata_content):
            # Replace existing Links
            updated_metadata = re.sub(links_pattern, new_links_section + '\n', metadata_content)
        else:
            # Add new Links at the beginning of metadata content
            updated_metadata = new_links_section + '\n' + metadata_content

        # Reconstruct content
        start_pos = metadata_match.start()
        end_pos = metadata_match.end()

        return content[:start_pos] + metadata_header + updated_metadata + content[end_pos:]

    def process_all_papers(self):
        """Process all papers in the directory"""
        logger.info(f"🚀 Starting metadata links update in {self.papers_dir}")

        # Find all markdown files
        paper_files = list(self.papers_dir.rglob("*.md"))
        self.stats['total_files'] = len(paper_files)

        logger.info(f"📊 Found {len(paper_files)} paper files")

        # Process each file
        for i, paper_path in enumerate(paper_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(paper_files)} ({i/len(paper_files)*100:.1f}%)")

            self.update_single_paper(paper_path)

        # Print final statistics
        logger.info("=" * 80)
        logger.info("🎉 METADATA LINKS UPDATE COMPLETE")
        logger.info("=" * 80)
        logger.info(f"📊 Total files: {self.stats['total_files']}")
        logger.info(f"✅ Files processed: {self.stats['processed']}")
        logger.info(f"❌ Files failed: {self.stats['failed']}")
        logger.info(f"🔗 Links added: {self.stats['links_added']}")
        logger.info(f"📝 Links updated: {self.stats['links_updated']}")
        logger.info("=" * 80)


def main():
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    # Show what will be done
    print("🔗 Metadata Links Updater")
    print("=" * 50)
    print("This will:")
    print("1. Add **Links** section to metadata with daily_digest and categories links")
    print("2. Update existing **Links** sections to standardized format")
    print("3. Remove any existing author/keyword links from **Links** sections")
    print("\n🚀 Starting update automatically...")

    updater = MetadataLinksUpdater(papers_dir)
    updater.process_all_papers()


if __name__ == "__main__":
    main()