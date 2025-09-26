#!/usr/bin/env python3
"""
Smart Batch Processor for Keyword Extraction
Processes papers efficiently with date-based prioritization and batch management
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
from collections import defaultdict

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('smart_batch_processor.log'),
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


class SmartBatchProcessor:
    """Smart batch processor with prioritization and checkpointing"""

    def __init__(self, papers_dir: Path, batch_size: int = 50):
        self.papers_dir = papers_dir
        self.batch_size = batch_size
        self.translator = get_translator('openai')
        self.extractor = KeywordExtractor(self.translator)
        self.budget_manager = LinkBudgetManager(max_links_per_paper=3)

        # Stats tracking
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'failed': 0,
            'skipped': 0,
            'api_calls': 0,
            'start_time': None,
            'batches_completed': 0
        }

        # Controlled vocabulary (expanded)
        self.controlled_vocab = self._build_controlled_vocab()
        self.recent_trending = self._build_trending_keywords()

    def _build_controlled_vocab(self) -> Dict[str, Any]:
        """Build comprehensive controlled vocabulary"""
        return {
            # Core ML/AI
            'Machine Learning': {'canonical_name': 'Machine Learning', 'aliases': ['ML'], 'frequency': 200, 'category': 'broad_technical'},
            'Deep Learning': {'canonical_name': 'Deep Learning', 'aliases': ['DL'], 'frequency': 180, 'category': 'broad_technical'},
            'Neural Networks': {'canonical_name': 'Neural Networks', 'aliases': ['NN', 'neural nets'], 'frequency': 150, 'category': 'broad_technical'},
            'Reinforcement Learning': {'canonical_name': 'Reinforcement Learning', 'aliases': ['RL'], 'frequency': 75, 'category': 'specific_connectable'},

            # Architectures
            'Transformer Architecture': {'canonical_name': 'Transformer Architecture', 'aliases': ['Transformers'], 'frequency': 95, 'category': 'specific_connectable'},
            'Convolutional Neural Networks': {'canonical_name': 'Convolutional Neural Networks', 'aliases': ['CNN', 'ConvNets'], 'frequency': 120, 'category': 'specific_connectable'},
            'Graph Neural Networks': {'canonical_name': 'Graph Neural Networks', 'aliases': ['GNN'], 'frequency': 65, 'category': 'specific_connectable'},
            'Attention Mechanism': {'canonical_name': 'Attention Mechanism', 'aliases': ['attention'], 'frequency': 85, 'category': 'specific_connectable'},

            # Applications
            'Computer Vision': {'canonical_name': 'Computer Vision', 'aliases': ['CV'], 'frequency': 110, 'category': 'broad_technical'},
            'Natural Language Processing': {'canonical_name': 'Natural Language Processing', 'aliases': ['NLP'], 'frequency': 90, 'category': 'broad_technical'},
            'Speech Recognition': {'canonical_name': 'Speech Recognition', 'aliases': ['ASR'], 'frequency': 40, 'category': 'specific_connectable'},

            # Techniques
            'Transfer Learning': {'canonical_name': 'Transfer Learning', 'aliases': [], 'frequency': 55, 'category': 'specific_connectable'},
            'Few-Shot Learning': {'canonical_name': 'Few-Shot Learning', 'aliases': [], 'frequency': 35, 'category': 'specific_connectable'},
            'Self-Supervised Learning': {'canonical_name': 'Self-Supervised Learning', 'aliases': [], 'frequency': 45, 'category': 'specific_connectable'},
            'Federated Learning': {'canonical_name': 'Federated Learning', 'aliases': [], 'frequency': 30, 'category': 'specific_connectable'},

            # Advanced concepts
            'Optimization': {'canonical_name': 'Optimization', 'aliases': [], 'frequency': 70, 'category': 'broad_technical'},
            'Generative Models': {'canonical_name': 'Generative Models', 'aliases': [], 'frequency': 50, 'category': 'specific_connectable'},
            'Uncertainty Quantification': {'canonical_name': 'Uncertainty Quantification', 'aliases': ['UQ'], 'frequency': 25, 'category': 'specific_connectable'}
        }

    def _build_trending_keywords(self) -> Dict[str, Any]:
        """Build recent trending keywords"""
        return {
            'Large Language Models': {'frequency': 50, 'growth_rate': 3.5},
            'Vision Transformers': {'frequency': 35, 'growth_rate': 2.8},
            'Diffusion Models': {'frequency': 40, 'growth_rate': 3.0},
            'Multi-Modal Learning': {'frequency': 30, 'growth_rate': 2.5},
            'Foundation Models': {'frequency': 25, 'growth_rate': 2.2},
            'In-Context Learning': {'frequency': 20, 'growth_rate': 2.0}
        }

    def analyze_papers_distribution(self) -> Dict[str, int]:
        """Analyze distribution of papers by date"""
        date_counts = defaultdict(int)

        for paper_file in self.papers_dir.rglob("*.md"):
            if len(paper_file.parts) >= 4:  # Check if has date folder structure
                date_folder = paper_file.parts[-2]
                if date_folder.startswith('2025-'):
                    date_counts[date_folder] += 1

        return dict(date_counts)

    def get_prioritized_files(self, max_files: int = None) -> List[Path]:
        """Get files prioritized by date (newest first)"""
        all_files = list(self.papers_dir.rglob("*.md"))

        # Sort by date (newest first) and then by filename
        def sort_key(file_path):
            parts = file_path.parts
            if len(parts) >= 4 and parts[-2].startswith('2025-'):
                date_str = parts[-2]
                return (date_str, parts[-1])
            else:
                return ('1900-01-01', parts[-1])  # Put non-dated files last

        all_files.sort(key=sort_key, reverse=True)

        if max_files:
            all_files = all_files[:max_files]

        return all_files

    def process_single_paper(self, paper_path: Path) -> bool:
        """Process a single paper with keyword extraction"""
        try:
            # Read current content
            content = paper_path.read_text(encoding='utf-8')

            # Check if already processed
            if '<!-- KEYWORD_LINKING_METADATA:' in content:
                logger.debug(f"Skipping already processed: {paper_path.name}")
                self.stats['skipped'] += 1
                return True

            # Extract title and abstract
            title, abstract = self.extract_title_abstract(content)
            if not title or not abstract:
                logger.warning(f"Missing title/abstract: {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Extract keywords
            candidates = self.extractor.extract_from_paper(
                paper_path, self.controlled_vocab, self.recent_trending
            )
            self.stats['api_calls'] += 1

            if not candidates:
                logger.warning(f"No keywords extracted: {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Apply budget management
            selected_keywords = self.budget_manager.select_keywords(candidates)
            if not selected_keywords:
                logger.warning(f"No keywords selected: {paper_path.name}")
                self.stats['failed'] += 1
                return False

            # Update paper with new keywords
            updated_content = self.update_paper_content(content, candidates, selected_keywords)
            paper_path.write_text(updated_content, encoding='utf-8')

            self.stats['processed'] += 1
            logger.info(f"✅ {paper_path.name}: {len(selected_keywords)} keywords")

            # Rate limiting
            time.sleep(0.5)  # 0.5 second delay
            return True

        except Exception as e:
            logger.error(f"❌ Failed {paper_path.name}: {e}")
            self.stats['failed'] += 1
            return False

    def extract_title_abstract(self, content: str) -> Tuple[str, str]:
        """Extract title and abstract from content"""
        # Title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ""

        # Abstract
        abstract_pattern = re.compile(r'## 📄 Abstract \(원문\)\s*\n\n(.*?)(?=\n## |$)', re.DOTALL)
        abstract_match = abstract_pattern.search(content)
        abstract = abstract_match.group(1).strip() if abstract_match else ""

        return title, abstract

    def update_paper_content(self, content: str, candidates: List, selected_keywords: List) -> str:
        """Update paper content with new keywords and metadata"""
        # Generate keywords section
        keywords_section = self.generate_keywords_section(selected_keywords)

        # Insert after metadata section
        metadata_pattern = re.compile(r'(## 📋 메타데이터\s*\n.*?\n\n)', re.DOTALL)
        metadata_match = metadata_pattern.search(content)

        if metadata_match:
            insert_position = metadata_match.end()
            content = content[:insert_position] + keywords_section + content[insert_position:]
        else:
            # Insert after title if no metadata section
            title_pattern = re.compile(r'(^# .+\n\n)', re.MULTILINE)
            title_match = title_pattern.search(content)
            if title_match:
                insert_position = title_match.end()
                content = content[:insert_position] + keywords_section + content[insert_position:]

        # Add metadata comment
        metadata_comment = self.create_metadata_comment(candidates, selected_keywords)
        return metadata_comment + "\n\n" + content

    def generate_keywords_section(self, keywords: List) -> str:
        """Generate keywords section markdown"""
        category_groups = defaultdict(list)
        for kw in keywords:
            category_groups[kw.category].append(kw)

        section = "## 🏷️ 카테고리화된 키워드\n"

        category_emoji = {
            'broad_technical': '🌐 Broad Technical',
            'specific_connectable': '🔗 Specific Connectable',
            'unique_technical': '⚡ Unique Technical',
            'evolved_concepts': '🚀 Evolved Concepts'
        }

        for category, emoji_label in category_emoji.items():
            if category in category_groups:
                links = [f"[[keywords/{kw.canonical}|{kw.surface}]]" for kw in category_groups[category]]
                section += f"**{emoji_label}**: {', '.join(links)}\n"

        return section + "\n"

    def create_metadata_comment(self, candidates: List, selected_keywords: List) -> str:
        """Create metadata comment"""
        metadata = {
            "processed_timestamp": str(datetime.now()),
            "vocabulary_version": "1.0",
            "selected_keywords": [kw.canonical for kw in selected_keywords],
            "rejected_keywords": [kw.canonical for kw in candidates if kw not in selected_keywords],
            "similarity_scores": {kw.canonical: kw.link_intent_score for kw in selected_keywords},
            "extraction_method": "AI_prompt_based",
            "budget_applied": True
        }

        metadata_json = json.dumps(metadata, indent=2, ensure_ascii=False)
        return f"<!-- KEYWORD_LINKING_METADATA:\n{metadata_json}\n-->"

    def process_batch(self, files: List[Path], batch_num: int) -> Dict[str, int]:
        """Process a batch of files"""
        batch_stats = {'processed': 0, 'failed': 0, 'skipped': 0}

        logger.info(f"🔄 Processing batch {batch_num}: {len(files)} files")

        for i, file_path in enumerate(files, 1):
            if i % 10 == 0:
                logger.info(f"  Progress: {i}/{len(files)} ({i/len(files)*100:.1f}%)")

            if self.process_single_paper(file_path):
                if file_path.name.endswith('.md') and '<!-- KEYWORD_LINKING_METADATA:' in file_path.read_text(encoding='utf-8'):
                    batch_stats['processed'] += 1
                else:
                    batch_stats['skipped'] += 1
            else:
                batch_stats['failed'] += 1

        self.stats['batches_completed'] += 1
        logger.info(f"✅ Batch {batch_num} complete: {batch_stats}")
        return batch_stats

    def run_smart_processing(self, max_papers: int = None, start_batch: int = 1):
        """Run smart batch processing"""
        self.stats['start_time'] = datetime.now()

        # Analyze distribution
        date_dist = self.analyze_papers_distribution()
        logger.info("📊 Paper distribution by date:")
        for date in sorted(date_dist.keys(), reverse=True):
            logger.info(f"  {date}: {date_dist[date]} papers")

        total_papers = sum(date_dist.values())
        logger.info(f"📋 Total papers: {total_papers}")

        if max_papers:
            logger.info(f"🎯 Processing limited to: {max_papers} papers")

        # Get prioritized files
        files_to_process = self.get_prioritized_files(max_papers)
        self.stats['total_files'] = len(files_to_process)

        logger.info(f"🚀 Starting smart batch processing...")
        logger.info(f"📦 Batch size: {self.batch_size}")
        logger.info(f"⏱️ Rate limiting: 0.5s per paper")

        # Process in batches
        for batch_num in range(start_batch, (len(files_to_process) // self.batch_size) + 2):
            start_idx = (batch_num - 1) * self.batch_size
            end_idx = min(start_idx + self.batch_size, len(files_to_process))

            if start_idx >= len(files_to_process):
                break

            batch_files = files_to_process[start_idx:end_idx]
            self.process_batch(batch_files, batch_num)

            # Progress update
            elapsed = datetime.now() - self.stats['start_time']
            rate = self.stats['processed'] / elapsed.total_seconds() * 60 if elapsed.total_seconds() > 0 else 0

            logger.info(f"📈 Overall progress: {self.stats['processed']}/{self.stats['total_files']} "
                       f"({self.stats['processed']/self.stats['total_files']*100:.1f}%) - "
                       f"Rate: {rate:.1f} papers/min")

        # Final statistics
        end_time = datetime.now()
        elapsed = end_time - self.stats['start_time']

        logger.info("="*80)
        logger.info("🎉 SMART BATCH PROCESSING COMPLETE")
        logger.info("="*80)
        logger.info(f"⏱️ Total time: {elapsed}")
        logger.info(f"📊 Papers processed: {self.stats['processed']}")
        logger.info(f"❌ Papers failed: {self.stats['failed']}")
        logger.info(f"⏭️ Papers skipped: {self.stats['skipped']}")
        logger.info(f"📞 API calls: {self.stats['api_calls']}")
        logger.info(f"🏁 Batches completed: {self.stats['batches_completed']}")
        logger.info(f"💰 Estimated cost: ${self.stats['api_calls'] * 0.005:.2f}")
        logger.info("="*80)


def main():
    papers_dir = Path("reports/individual_papers")

    if not papers_dir.exists():
        logger.error(f"Papers directory not found: {papers_dir}")
        return

    if not os.getenv('OPENAI_API_KEY'):
        logger.error("OPENAI_API_KEY not set")
        return

    # Configuration
    batch_size = 30  # Smaller batches for safety
    max_papers = None  # Set to limit papers (e.g., 100 for testing)

    # Show configuration and proceed
    print("🤖 Smart Batch Keyword Extraction")
    print("="*50)
    print(f"📦 Batch size: {batch_size}")
    print(f"🎯 Max papers: {max_papers or 'All papers'}")
    print(f"💰 Estimated cost: ${(max_papers or 1324) * 0.005:.2f}")
    print("\n🚀 Starting keyword extraction automatically...")

    processor = SmartBatchProcessor(papers_dir, batch_size)
    processor.run_smart_processing(max_papers)


if __name__ == "__main__":
    main()