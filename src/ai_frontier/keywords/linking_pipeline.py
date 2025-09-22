"""
Obsidian Keyword Linking Pipeline

A comprehensive system for normalizing keywords, managing canonical vocabulary,
and inserting idempotent wikilinks into paper templates while preserving metadata.
"""

import json
import re
from typing import Dict, List, Optional, Tuple, Set, Any
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

logger = logging.getLogger(__name__)


@dataclass
class KeywordCandidate:
    """Represents a keyword candidate from paper analysis"""
    surface: str
    canonical: str
    aliases: List[str]
    category: str
    rationale: str
    novelty_score: float
    connectivity_score: float
    specificity_score: float
    link_intent_score: float


@dataclass
class CanonicalEntry:
    """Represents a canonical vocabulary entry"""
    canonical_name: str
    aliases: Set[str]
    frequency: int = 0
    degree: int = 0  # Number of papers linking to this
    embedding: Optional[np.ndarray] = None
    category: str = "general"


@dataclass
class LinkingMetadata:
    """Hidden metadata stored in HTML comments"""
    processed_timestamp: str
    vocabulary_version: str
    selected_keywords: List[str]
    rejected_keywords: List[str]
    similarity_scores: Dict[str, float]


class CanonicalVocabularyMatcher:
    """Handles canonical vocabulary matching with cosine similarity"""

    def __init__(self, vocab_path: Path, similarity_threshold: float = 0.85):
        self.vocab_path = vocab_path
        self.similarity_threshold = similarity_threshold
        self.vocabulary: Dict[str, CanonicalEntry] = {}
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            max_features=10000,
            stop_words='english',
            lowercase=True
        )
        self._load_vocabulary()

    def _load_vocabulary(self):
        """Load canonical vocabulary from file"""
        if self.vocab_path.exists():
            try:
                with open(self.vocab_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                for item in data.get('vocabulary', []):
                    entry = CanonicalEntry(
                        canonical_name=item['canonical_name'],
                        aliases=set(item.get('aliases', [])),
                        frequency=item.get('frequency', 0),
                        degree=item.get('degree', 0),
                        category=item.get('category', 'general')
                    )
                    self.vocabulary[entry.canonical_name] = entry

                # Build embeddings for existing vocabulary
                self._build_embeddings()
                logger.info(f"Loaded {len(self.vocabulary)} vocabulary entries")
            except Exception as e:
                logger.warning(f"Failed to load vocabulary: {e}")

    def _build_embeddings(self):
        """Build TF-IDF embeddings for vocabulary matching"""
        if not self.vocabulary:
            return

        # Prepare text corpus for vectorization
        vocab_texts = []
        vocab_keys = []

        for canonical, entry in self.vocabulary.items():
            # Combine canonical name with aliases for better matching
            text_variants = [canonical] + list(entry.aliases)
            combined_text = " ".join(text_variants)
            vocab_texts.append(combined_text)
            vocab_keys.append(canonical)

        if vocab_texts:
            # Fit vectorizer and compute embeddings
            embeddings = self.vectorizer.fit_transform(vocab_texts)

            for i, canonical in enumerate(vocab_keys):
                self.vocabulary[canonical].embedding = embeddings[i].toarray().flatten()

    def resolve_canonical(self, candidate: str, controlled_vocab: Dict[str, Any]) -> Tuple[Optional[str], float, str]:
        """
        Resolve canonical form of a candidate keyword

        Args:
            candidate: Surface form of keyword candidate
            controlled_vocab: Top 500 canonical vocabulary subset

        Returns:
            Tuple of (matched_name | None, similarity, action)
            action: 'exact_match', 'similarity_match', 'new_canonical'
        """
        if not candidate or not candidate.strip():
            return None, 0.0, 'invalid'

        candidate_clean = candidate.strip().lower()

        # 1. Check for exact matches first
        for canonical, entry in self.vocabulary.items():
            if canonical.lower() == candidate_clean:
                return canonical, 1.0, 'exact_match'

            # Check aliases
            for alias in entry.aliases:
                if alias.lower() == candidate_clean:
                    return canonical, 1.0, 'exact_match'

        # 2. Check similarity matches if we have embeddings
        if self.vectorizer and any(entry.embedding is not None for entry in self.vocabulary.values()):
            best_match, best_similarity = self._find_similarity_match(candidate)

            if best_similarity >= self.similarity_threshold:
                return best_match, best_similarity, 'similarity_match'

        # 3. No good match found - suggest as new canonical
        return None, 0.0, 'new_canonical'

    def _find_similarity_match(self, candidate: str) -> Tuple[Optional[str], float]:
        """Find best similarity match using cosine similarity"""
        try:
            # Vectorize the candidate
            candidate_vec = self.vectorizer.transform([candidate])
            candidate_embedding = candidate_vec.toarray().flatten()

            best_similarity = 0.0
            best_match = None

            for canonical, entry in self.vocabulary.items():
                if entry.embedding is not None:
                    # Compute cosine similarity
                    similarity = cosine_similarity(
                        candidate_embedding.reshape(1, -1),
                        entry.embedding.reshape(1, -1)
                    )[0][0]

                    if similarity > best_similarity:
                        best_similarity = similarity
                        best_match = canonical

            return best_match, best_similarity

        except Exception as e:
            logger.warning(f"Similarity matching failed for '{candidate}': {e}")
            return None, 0.0


class LinkBudgetManager:
    """Manages link selection with budget constraints"""

    def __init__(self, max_links_per_paper: int = 3):
        self.max_links_per_paper = max_links_per_paper
        self.category_limits = {
            'broad_technical': 1,
            'specific_connectable': float('inf'),  # No limit
            'unique_technical': float('inf'),
            'evolved_concepts': float('inf')
        }

    def select_keywords(self, candidates: List[KeywordCandidate]) -> List[KeywordCandidate]:
        """
        Select keywords based on budget constraints and scoring

        Args:
            candidates: List of keyword candidates

        Returns:
            Selected keywords within budget constraints
        """
        # Filter by link intent score first
        viable_candidates = [
            c for c in candidates
            if c.link_intent_score >= 0.5
        ]

        # Apply category limits
        category_counts = defaultdict(int)
        filtered_candidates = []

        for candidate in viable_candidates:
            category = candidate.category
            limit = self.category_limits.get(category, float('inf'))

            if category_counts[category] < limit:
                filtered_candidates.append(candidate)
                category_counts[category] += 1

        # Sort by composite score and select top N
        def composite_score(candidate: KeywordCandidate) -> float:
            return (
                candidate.link_intent_score * 0.4 +
                candidate.connectivity_score * 0.3 +
                candidate.specificity_score * 0.2 +
                candidate.novelty_score * 0.1
            )

        filtered_candidates.sort(key=composite_score, reverse=True)
        selected = filtered_candidates[:self.max_links_per_paper]

        logger.info(f"Selected {len(selected)} keywords from {len(candidates)} candidates")
        return selected


class WikilinkInserter:
    """Handles idempotent wikilink insertion with metadata preservation"""

    def __init__(self):
        self.wikilink_pattern = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
        self.metadata_comment_pattern = re.compile(
            r'<!-- KEYWORD_LINKING_METADATA:\s*({.*?})\s*-->',
            re.DOTALL
        )

    def insert_wikilinks(self, content: str, selected_keywords: List[KeywordCandidate],
                        metadata: LinkingMetadata) -> str:
        """
        Insert wikilinks idempotently while preserving metadata

        Args:
            content: Original markdown content
            selected_keywords: Keywords to link
            metadata: Linking metadata to preserve

        Returns:
            Updated content with wikilinks and metadata
        """
        # Extract existing metadata if present
        existing_metadata = self._extract_metadata(content)

        # Remove old metadata comment
        content = self.metadata_comment_pattern.sub('', content).strip()

        # Insert/update wikilinks in keywords section
        updated_content = self._update_keywords_section(content, selected_keywords)

        # Insert updated metadata comment
        metadata_comment = self._create_metadata_comment(metadata)
        updated_content = metadata_comment + "\n\n" + updated_content

        return updated_content

    def _extract_metadata(self, content: str) -> Optional[LinkingMetadata]:
        """Extract existing linking metadata from HTML comment"""
        match = self.metadata_comment_pattern.search(content)
        if match:
            try:
                metadata_dict = json.loads(match.group(1))
                return LinkingMetadata(**metadata_dict)
            except (json.JSONDecodeError, TypeError):
                logger.warning("Failed to parse existing metadata")
        return None

    def _update_keywords_section(self, content: str, keywords: List[KeywordCandidate]) -> str:
        """Update the categorized keywords section with wikilinks"""
        # Find the keywords section
        keywords_pattern = re.compile(
            r'(## 🏷️ 카테고리화된 키워드\s*\n)(.*?)(?=\n## |$)',
            re.DOTALL
        )

        match = keywords_pattern.search(content)
        if not match:
            logger.warning("Keywords section not found")
            return content

        # Group keywords by category
        category_groups = defaultdict(list)
        for keyword in keywords:
            category_groups[keyword.category].append(keyword)

        # Build new keywords section
        new_keywords_section = match.group(1)  # Keep header

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
                    # Create wikilink in format [[keywords/canonical|surface]]
                    wikilink = f"[[keywords/{keyword.canonical}|{keyword.surface}]]"
                    keyword_links.append(wikilink)

                keywords_str = ", ".join(keyword_links)
                new_keywords_section += f"**{emoji_label}**: {keywords_str}\n\n"

        # Replace the section in content
        return keywords_pattern.sub(new_keywords_section.rstrip() + "\n", content)

    def _create_metadata_comment(self, metadata: LinkingMetadata) -> str:
        """Create HTML comment with linking metadata"""
        metadata_dict = asdict(metadata)
        metadata_json = json.dumps(metadata_dict, indent=2, ensure_ascii=False)
        return f"<!-- KEYWORD_LINKING_METADATA:\n{metadata_json}\n-->"


class VocabularyBuilder:
    """Handles vocabulary rebuilding with merge operations"""

    def __init__(self, vocab_path: Path, max_degree: int = 50):
        self.vocab_path = vocab_path
        self.max_degree = max_degree
        self.vocabulary: Dict[str, CanonicalEntry] = {}

    def merge_keywords(self, new_keywords: List[KeywordCandidate]):
        """Merge new keywords into vocabulary with degree capping"""
        for keyword in new_keywords:
            canonical = keyword.canonical

            if canonical in self.vocabulary:
                # Update existing entry
                entry = self.vocabulary[canonical]
                entry.frequency += 1
                entry.degree += 1
                entry.aliases.update(keyword.aliases)

                # Apply degree capping
                if entry.degree > self.max_degree:
                    logger.info(f"Capping degree for '{canonical}' at {self.max_degree}")
                    entry.degree = self.max_degree
            else:
                # Create new entry
                self.vocabulary[canonical] = CanonicalEntry(
                    canonical_name=canonical,
                    aliases=set(keyword.aliases),
                    frequency=1,
                    degree=1,
                    category=keyword.category
                )

    def save_vocabulary(self):
        """Save updated vocabulary to file"""
        self.vocab_path.parent.mkdir(parents=True, exist_ok=True)

        vocab_data = {
            'vocabulary': [
                {
                    'canonical_name': entry.canonical_name,
                    'aliases': list(entry.aliases),
                    'frequency': entry.frequency,
                    'degree': entry.degree,
                    'category': entry.category
                }
                for entry in self.vocabulary.values()
            ],
            'metadata': {
                'total_entries': len(self.vocabulary),
                'last_updated': str(datetime.now())
            }
        }

        with open(self.vocab_path, 'w', encoding='utf-8') as f:
            json.dump(vocab_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Saved vocabulary with {len(self.vocabulary)} entries")


class KeywordLinkingPipeline:
    """Main orchestrator for the keyword linking pipeline"""

    def __init__(self, vocab_path: Path, data_dir: Path):
        self.vocab_path = vocab_path
        self.data_dir = data_dir

        # Initialize components
        self.matcher = CanonicalVocabularyMatcher(vocab_path)
        self.budget_manager = LinkBudgetManager()
        self.inserter = WikilinkInserter()
        self.vocab_builder = VocabularyBuilder(vocab_path)

    def process_paper(self, paper_path: Path, candidates: List[KeywordCandidate]) -> bool:
        """
        Process a single paper with keyword linking

        Args:
            paper_path: Path to paper markdown file
            candidates: Keyword candidates from AI extraction

        Returns:
            True if processing succeeded
        """
        try:
            # Read current content
            content = paper_path.read_text(encoding='utf-8')

            # Resolve canonical forms
            resolved_candidates = []
            controlled_vocab = self._get_controlled_vocab_subset()

            for candidate in candidates:
                canonical, similarity, action = self.matcher.resolve_canonical(
                    candidate.surface, controlled_vocab
                )

                if action == 'new_canonical':
                    canonical = candidate.canonical  # Use proposed canonical

                if canonical:
                    candidate.canonical = canonical
                    resolved_candidates.append(candidate)

            # Select keywords within budget
            selected_keywords = self.budget_manager.select_keywords(resolved_candidates)

            if not selected_keywords:
                logger.info(f"No keywords selected for {paper_path.name}")
                return True

            # Create linking metadata
            metadata = LinkingMetadata(
                processed_timestamp=str(datetime.now()),
                vocabulary_version="1.0",
                selected_keywords=[k.canonical for k in selected_keywords],
                rejected_keywords=[k.canonical for k in resolved_candidates
                                 if k not in selected_keywords],
                similarity_scores={k.canonical: k.link_intent_score
                                 for k in selected_keywords}
            )

            # Insert wikilinks
            updated_content = self.inserter.insert_wikilinks(
                content, selected_keywords, metadata
            )

            # Write updated content
            paper_path.write_text(updated_content, encoding='utf-8')

            # Update vocabulary
            self.vocab_builder.merge_keywords(selected_keywords)

            logger.info(f"Processed {paper_path.name} with {len(selected_keywords)} keywords")
            return True

        except Exception as e:
            logger.error(f"Failed to process {paper_path.name}: {e}")
            return False

    def _get_controlled_vocab_subset(self) -> Dict[str, Any]:
        """Get top 500 canonical vocabulary entries"""
        # Sort by frequency and degree, take top 500
        sorted_vocab = sorted(
            self.matcher.vocabulary.values(),
            key=lambda x: (x.frequency + x.degree),
            reverse=True
        )

        return {
            entry.canonical_name: asdict(entry)
            for entry in sorted_vocab[:500]
        }

    def process_all_papers(self, papers_dir: Path) -> Dict[str, int]:
        """Process all papers in directory"""
        stats = {'processed': 0, 'failed': 0, 'skipped': 0}

        paper_files = list(papers_dir.rglob("*.md"))
        logger.info(f"Found {len(paper_files)} paper files to process")

        for paper_path in paper_files:
            # Skip if already processed recently (check metadata)
            if self._is_recently_processed(paper_path):
                stats['skipped'] += 1
                continue

            # Extract keywords using existing prompt template
            candidates = self._extract_keywords_from_paper(paper_path)

            if self.process_paper(paper_path, candidates):
                stats['processed'] += 1
            else:
                stats['failed'] += 1

        # Save updated vocabulary
        self.vocab_builder.save_vocabulary()

        return stats

    def _is_recently_processed(self, paper_path: Path) -> bool:
        """Check if paper was recently processed"""
        try:
            content = paper_path.read_text(encoding='utf-8')
            metadata_match = self.inserter.metadata_comment_pattern.search(content)
            if metadata_match:
                # Could add timestamp checking logic here
                return True
        except Exception:
            pass
        return False

    def _extract_keywords_from_paper(self, paper_path: Path) -> List[KeywordCandidate]:
        """Extract keywords using existing AI prompt system"""
        # This would integrate with the existing prompt template system
        # For now, return empty list - will be implemented with AI integration
        return []