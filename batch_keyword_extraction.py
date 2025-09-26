#!/usr/bin/env python3
"""
Batch keyword extraction for all individual papers
Apply new AI-based keyword extraction system to all papers
"""

import re
import json
import os
import time
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
        logging.FileHandler('batch_keyword_extraction.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

try:
    from src.ai_frontier.keywords.ai_integration import KeywordExtractor
    from src.ai_frontier.translation.translator import get_translator
    from src.ai_frontier.keywords.linking_pipeline import LinkBudgetManager
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    exit(1)


class BatchKeywordExtractor:
    """Batch keyword extraction for all papers"""

    def __init__(self, papers_dir: Path, vocab_path: Path, max_papers: int = None):
        self.papers_dir = papers_dir
        self.vocab_path = vocab_path
        self.max_papers = max_papers
        self.translator = get_translator('openai')
        self.extractor = KeywordExtractor(self.translator)
        self.budget_manager = LinkBudgetManager(max_links_per_paper=3)

        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'skipped': 0,
            'keywords_extracted': 0,
            'api_calls': 0,
            'start_time': None,
            'end_time': None
        }

        # Build controlled vocabulary from common AI/ML terms
        self.controlled_vocab = {
            'Neural Networks': {
                'canonical_name': 'Neural Networks',
                'aliases': ['NN', 'neural nets'],
                'frequency': 150,
                'category': 'broad_technical'
            },
            'Machine Learning': {
                'canonical_name': 'Machine Learning',
                'aliases': ['ML'],
                'frequency': 200,
                'category': 'broad_technical'
            },
            'Deep Learning': {
                'canonical_name': 'Deep Learning',
                'aliases': ['DL'],
                'frequency': 180,
                'category': 'broad_technical'
            },
            'Transformer Architecture': {
                'canonical_name': 'Transformer Architecture',
                'aliases': ['Transformers', 'transformer models'],
                'frequency': 95,
                'category': 'specific_connectable'
            },
            'Attention Mechanism': {
                'canonical_name': 'Attention Mechanism',
                'aliases': ['attention', 'self-attention'],
                'frequency': 85,
                'category': 'specific_connectable'
            },
            'Convolutional Neural Networks': {
                'canonical_name': 'Convolutional Neural Networks',
                'aliases': ['CNN', 'ConvNets'],
                'frequency': 120,
                'category': 'specific_connectable'
            },
            'Reinforcement Learning': {
                'canonical_name': 'Reinforcement Learning',
                'aliases': ['RL'],
                'frequency': 75,
                'category': 'specific_connectable'
            },
            'Computer Vision': {
                'canonical_name': 'Computer Vision',
                'aliases': ['CV'],
                'frequency': 110,
                'category': 'broad_technical'
            },
            'Natural Language Processing': {
                'canonical_name': 'Natural Language Processing',
                'aliases': ['NLP'],
                'frequency': 90,
                'category': 'broad_technical'
            },
            'Graph Neural Networks': {
                'canonical_name': 'Graph Neural Networks',
                'aliases': ['GNN', 'graph networks'],
                'frequency': 65,
                'category': 'specific_connectable'
            }
        }

        # Recent trending keywords
        self.recent_trending = {
            'Large Language Models': {'frequency': 45, 'growth_rate': 3.2},
            'Diffusion Models': {'frequency': 35, 'growth_rate': 2.8},
            'Vision Transformers': {'frequency': 30, 'growth_rate': 2.5},
            'Multi-Modal Learning': {'frequency': 25, 'growth_rate': 2.1},
            'Federated Learning': {'frequency': 20, 'growth_rate': 1.9},
            'Few-Shot Learning': {'frequency': 18, 'growth_rate': 1.7},
            'Self-Supervised Learning': {'frequency': 22, 'growth_rate': 2.0}
        }

    def extract_title_abstract(self, content: str) -> Tuple[str, str]:
        """Extract title and abstract from paper content"""
        # Extract title (first # heading)
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ""

        # Extract abstract from "## 📄 Abstract (원문)" section
        abstract_pattern = re.compile(
            r'## 📄 Abstract \(원문\)\s*\n\n(.*?)(?=\n## |$)',
            re.DOTALL
        )
        abstract_match = abstract_pattern.search(content)
        abstract = abstract_match.group(1).strip() if abstract_match else ""

        return title, abstract

    def process_single_paper(self, paper_path: Path) -> bool:
        """Process a single paper with keyword extraction"""
        try:
            self.stats['total_files'] += 1

            # Read current content
            content = paper_path.read_text(encoding='utf-8')

            # Check if already processed (has KEYWORD_LINKING_METADATA comment)
            if '<!-- KEYWORD_LINKING_METADATA:' in content:
                logger.debug(f"Skipping already processed paper: {paper_path.name}")
                self.stats['skipped'] += 1
                return True

            # Extract title and abstract
            title, abstract = self.extract_title_abstract(content)

            if not title or not abstract:
                logger.warning(f"Could not extract title/abstract from {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Extract keywords using AI (with rate limiting)
            logger.info(f"Processing: {paper_path.name}")

            try:
                candidates = self.extractor.extract_from_paper(
                    paper_path,
                    self.controlled_vocab,
                    self.recent_trending
                )
                self.stats['api_calls'] += 1

                # Rate limiting to avoid API limits
                time.sleep(1)  # 1 second delay between requests

            except Exception as e:
                logger.error(f"AI extraction failed for {paper_path.name}: {e}")
                self.stats['failed'] += 1
                return False

            if not candidates:
                logger.warning(f"No keywords extracted for {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Apply budget management
            selected_keywords = self.budget_manager.select_keywords(candidates)

            if not selected_keywords:
                logger.warning(f"No keywords selected after budget filtering for {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Generate new keywords section
            new_keywords_section = self.generate_keywords_section(selected_keywords)

            # Insert new keywords section after metadata
            updated_content = self.insert_keywords_section(content, new_keywords_section)

            # Add linking metadata
            metadata_comment = self.create_metadata_comment(candidates, selected_keywords)
            final_content = metadata_comment + "\n\n" + updated_content

            # Write updated content
            paper_path.write_text(final_content, encoding='utf-8')

            self.stats['processed'] += 1
            self.stats['keywords_extracted'] += len(selected_keywords)

            logger.info(f"✅ Processed {paper_path.name} - {len(selected_keywords)} keywords")
            return True

        except Exception as e:
            logger.error(f"Failed to process {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def generate_keywords_section(self, keywords: List) -> str:
        """Generate markdown keywords section"""
        # Group keywords by category
        category_groups = {}
        for keyword in keywords:
            category = keyword.category
            if category not in category_groups:
                category_groups[category] = []
            category_groups[category].append(keyword)

        # Build section
        section = "## 🏷️ 카테고리화된 키워드\n"

        category_emoji = {
            'broad_technical': '🌐 Broad Technical',
            'specific_connectable': '🔗 Specific Connectable',
            'unique_technical': '⚡ Unique Technical',
            'evolved_concepts': '🚀 Evolved Concepts'
        }

        for category, emoji_label in category_emoji.items():
            if category in category_groups:
                keyword_links = []
                for keyword in category_groups[category]:
                    wikilink = f"[[keywords/{keyword.canonical}|{keyword.surface}]]"
                    keyword_links.append(wikilink)

                keywords_str = ", ".join(keyword_links)
                section += f"**{emoji_label}**: {keywords_str}\n"

        section += "\n"
        return section

    def insert_keywords_section(self, content: str, keywords_section: str) -> str:
        """Insert keywords section after metadata"""
        # Find metadata section
        metadata_pattern = re.compile(r'(## 📋 메타데이터\s*\n.*?\n\n)', re.DOTALL)
        metadata_match = metadata_pattern.search(content)

        if metadata_match:
            insert_position = metadata_match.end()
            return content[:insert_position] + keywords_section + content[insert_position:]
        else:
            # If no metadata section found, insert after title
            title_pattern = re.compile(r'(^# .+\n\n)', re.MULTILINE)
            title_match = title_pattern.search(content)
            if title_match:
                insert_position = title_match.end()
                return content[:insert_position] + keywords_section + content[insert_position:]

        # If neither found, just prepend
        return keywords_section + content

    def create_metadata_comment(self, candidates: List, selected_keywords: List) -> str:
        """Create HTML comment with linking metadata"""
        metadata = {
            "processed_timestamp": str(datetime.now()),
            "vocabulary_version": "1.0",
            "selected_keywords": [kw.canonical for kw in selected_keywords],
            "rejected_keywords": [kw.canonical for kw in candidates if kw not in selected_keywords],
            "similarity_scores": {kw.canonical: kw.link_intent_score for kw in selected_keywords},
            "extraction_method": "AI_prompt_based",
            "budget_applied": True,
            "max_links_per_paper": 3
        }

        metadata_json = json.dumps(metadata, indent=2, ensure_ascii=False)
        return f"<!-- KEYWORD_LINKING_METADATA:\n{metadata_json}\n-->"

    def process_all_papers(self) -> Dict[str, Any]:
        """Process all papers in the directory"""
        self.stats['start_time'] = datetime.now()
        logger.info(f"Starting batch keyword extraction in {self.papers_dir}")

        # Find all markdown files
        paper_files = list(self.papers_dir.rglob("*.md"))
        logger.info(f"Found {len(paper_files)} paper files")

        # Limit number of papers if specified
        if self.max_papers:
            paper_files = paper_files[:self.max_papers]
            logger.info(f"Limited to first {self.max_papers} papers for testing")

        # Process each file
        for i, paper_path in enumerate(paper_files, 1):
            if i % 10 == 0:
                elapsed = datetime.now() - self.stats['start_time']
                rate = i / elapsed.total_seconds() * 60  # papers per minute
                remaining = len(paper_files) - i
                eta = remaining / rate if rate > 0 else 0

                logger.info(f"Progress: {i}/{len(paper_files)} ({i/len(paper_files)*100:.1f}%) - "
                          f"Rate: {rate:.1f} papers/min - ETA: {eta:.1f} min")

            self.process_single_paper(paper_path)

            # Progress checkpoint every 50 files
            if i % 50 == 0:
                self.print_stats()

        self.stats['end_time'] = datetime.now()
        return self.stats

    def print_stats(self):
        """Print current statistics"""
        elapsed = datetime.now() - self.stats['start_time']
        rate = self.stats['processed'] / elapsed.total_seconds() * 60 if elapsed.total_seconds() > 0 else 0

        logger.info("="*60)
        logger.info("📊 INTERMEDIATE STATISTICS")
        logger.info("="*60)
        logger.info(f"Elapsed time: {elapsed}")
        logger.info(f"Files processed: {self.stats['processed']}")
        logger.info(f"Files failed: {self.stats['failed']}")
        logger.info(f"Files skipped: {self.stats['skipped']}")
        logger.info(f"Keywords extracted: {self.stats['keywords_extracted']}")
        logger.info(f"API calls made: {self.stats['api_calls']}")
        logger.info(f"Processing rate: {rate:.1f} papers/min")
        logger.info("="*60)


def main():
    """Main execution function"""
    papers_dir = Path("reports/individual_papers")
    vocab_path = Path("data/vocabulary.json")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    # Check API key
    if not os.getenv('OPENAI_API_KEY'):
        logger.error("OPENAI_API_KEY environment variable not set")
        return

    # Start with a test batch first
    test_mode = input("Run in test mode? (y/N): ").lower().strip() == 'y'
    max_papers = 20 if test_mode else None

    extractor = BatchKeywordExtractor(papers_dir, vocab_path, max_papers)

    logger.info("Starting batch keyword extraction...")
    if test_mode:
        logger.info("⚠️  Running in test mode (limited to 20 papers)")

    stats = extractor.process_all_papers()

    # Final statistics
    elapsed = stats['end_time'] - stats['start_time']
    rate = stats['processed'] / elapsed.total_seconds() * 60 if elapsed.total_seconds() > 0 else 0

    print("\n" + "="*80)
    print("📊 BATCH KEYWORD EXTRACTION RESULTS")
    print("="*80)
    print(f"Total runtime: {elapsed}")
    print(f"Files processed: {stats['processed']}")
    print(f"Files failed: {stats['failed']}")
    print(f"Files skipped: {stats['skipped']}")
    print(f"Total keywords extracted: {stats['keywords_extracted']}")
    print(f"Average keywords per paper: {stats['keywords_extracted']/max(stats['processed'], 1):.1f}")
    print(f"API calls made: {stats['api_calls']}")
    print(f"Processing rate: {rate:.1f} papers/min")
    print(f"Estimated cost (approximate): ${stats['api_calls'] * 0.01:.2f}")
    print("="*80)


if __name__ == "__main__":
    main()