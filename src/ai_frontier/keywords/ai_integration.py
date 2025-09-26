"""
AI Integration for Keyword Linking Pipeline

Integrates the keyword linking pipeline with existing AI prompt system
for automated keyword extraction and canonical resolution.
"""

import json
import re
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from datetime import datetime
import logging

from ..prompts.templates import PromptManager
from ..translation.translator import BaseTranslator
from .linking_pipeline import (
    KeywordCandidate, KeywordLinkingPipeline,
    CanonicalVocabularyMatcher, LinkingMetadata
)

logger = logging.getLogger(__name__)


class KeywordExtractor:
    """Extracts keywords from papers using AI prompts"""

    def __init__(self, translation_provider: BaseTranslator):
        self.translation_provider = translation_provider
        self.prompt_manager = PromptManager()

    def extract_from_paper(self, paper_path: Path,
                          controlled_vocab: Dict[str, Any] = None,
                          recent_trending: Dict[str, Any] = None) -> List[KeywordCandidate]:
        """
        Extract keyword candidates from a paper using AI

        Args:
            paper_path: Path to paper markdown file
            controlled_vocab: Top 500 canonical vocabulary
            recent_trending: Recent 30-day trending keywords

        Returns:
            List of keyword candidates
        """
        try:
            # Read paper content
            content = paper_path.read_text(encoding='utf-8')

            # Extract title and abstract
            title, abstract = self._extract_title_abstract(content)

            if not title or not abstract:
                logger.warning(f"Could not extract title/abstract from {paper_path.name}")
                return []

            # Prepare prompt parameters
            prompt_params = {
                'title': title,
                'abstract': abstract,
                'controlled_vocab_json': json.dumps(controlled_vocab or {}, ensure_ascii=False),
                'recent_trending_json': json.dumps(recent_trending or {}, ensure_ascii=False)
            }

            # Generate prompt
            prompt = self.prompt_manager.generate_prompt('keyword_extraction', **prompt_params)

            # Get AI response (use translate method but with original language preserved)
            response = self._send_prompt_to_ai(prompt)

            # Parse response
            candidates = self._parse_ai_response(response)

            logger.info(f"Extracted {len(candidates)} keyword candidates from {paper_path.name}")
            return candidates

        except Exception as e:
            logger.error(f"Failed to extract keywords from {paper_path.name}: {e}")
            return []

    def _send_prompt_to_ai(self, prompt: str) -> str:
        """Send prompt directly to AI without translation"""
        try:
            # Use the underlying OpenAI client directly
            if hasattr(self.translation_provider, 'client'):
                response = self.translation_provider.client.chat.completions.create(
                    model=self.translation_provider.model,
                    messages=[
                        {"role": "system", "content": "You are an expert keyword extraction assistant for academic papers. Follow the instructions exactly and return valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.1,
                    max_tokens=1000
                )
                return response.choices[0].message.content.strip()
            else:
                # Fallback to translate method but try to prevent translation
                return self.translation_provider.translate(prompt, target_language="original")
        except Exception as e:
            logger.error(f"Failed to send prompt to AI: {e}")
            raise

    def _extract_title_abstract(self, content: str) -> Tuple[str, str]:
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

    def _parse_ai_response(self, response: str) -> List[KeywordCandidate]:
        """Parse AI response to extract keyword candidates"""
        try:
            # Try multiple approaches to extract JSON
            json_content = None

            # Approach 1: Look for JSON code blocks
            code_block_match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
            if code_block_match:
                json_content = code_block_match.group(1)
            else:
                # Approach 2: Look for any JSON-like structure
                json_match = re.search(r'\{[^{}]*"candidates"[^{}]*\[[^\]]*\][^{}]*\}', response, re.DOTALL)
                if json_match:
                    json_content = json_match.group()
                else:
                    # Approach 3: Find the largest JSON-like structure
                    json_match = re.search(r'\{.*\}', response, re.DOTALL)
                    if json_match:
                        json_content = json_match.group()

            if not json_content:
                logger.warning("No JSON found in AI response")
                logger.debug(f"Response was: {response[:500]}...")
                return []

            # Clean up common JSON issues
            json_content = json_content.strip()

            # Try to parse JSON
            try:
                data = json.loads(json_content)
            except json.JSONDecodeError:
                # Try to fix common issues and parse again
                json_content = re.sub(r',\s*}', '}', json_content)  # Remove trailing commas
                json_content = re.sub(r',\s*]', ']', json_content)  # Remove trailing commas in arrays
                data = json.loads(json_content)

            candidates = []

            for candidate_data in data.get('candidates', []):
                try:
                    candidate = KeywordCandidate(
                        surface=candidate_data.get('surface', ''),
                        canonical=candidate_data.get('canonical', ''),
                        aliases=candidate_data.get('aliases', []),
                        category=candidate_data.get('category', 'general'),
                        rationale=candidate_data.get('rationale', ''),
                        novelty_score=float(candidate_data.get('novelty_score', 0)),
                        connectivity_score=float(candidate_data.get('connectivity_score', 0)),
                        specificity_score=float(candidate_data.get('specificity_score', 0)),
                        link_intent_score=float(candidate_data.get('link_intent_score', 0))
                    )
                    candidates.append(candidate)
                except (KeyError, ValueError, TypeError) as e:
                    logger.warning(f"Failed to parse candidate: {e}")
                    continue

            return candidates

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse AI response JSON: {e}")
            logger.debug(f"Attempted to parse: {json_content[:200]}...")
            return []


class IntegratedKeywordLinker:
    """Integrated keyword linking system with AI extraction"""

    def __init__(self, vocab_path: Path, data_dir: Path, translation_provider: BaseTranslator):
        self.pipeline = KeywordLinkingPipeline(vocab_path, data_dir)
        self.extractor = KeywordExtractor(translation_provider)
        self.vocab_path = vocab_path

    def process_paper_with_ai(self, paper_path: Path, force_reprocess: bool = False) -> bool:
        """
        Process a paper with AI-based keyword extraction

        Args:
            paper_path: Path to paper file
            force_reprocess: Force reprocessing even if recently processed

        Returns:
            True if successful
        """
        try:
            # Check if already processed
            if not force_reprocess and self._is_recently_processed(paper_path):
                logger.info(f"Skipping recently processed paper: {paper_path.name}")
                return True

            # Get controlled vocabulary subset for AI prompt
            controlled_vocab = self.pipeline._get_controlled_vocab_subset()

            # Get recent trending keywords (placeholder - could be implemented later)
            recent_trending = self._get_recent_trending_keywords()

            # Extract keywords using AI
            candidates = self.extractor.extract_from_paper(
                paper_path, controlled_vocab, recent_trending
            )

            if not candidates:
                logger.warning(f"No keyword candidates extracted for {paper_path.name}")
                return True

            # Process with pipeline
            return self.pipeline.process_paper(paper_path, candidates)

        except Exception as e:
            logger.error(f"Failed to process paper with AI: {e}")
            return False

    def process_papers_batch(self, papers_dir: Path,
                           pattern: str = "*.md",
                           force_reprocess: bool = False) -> Dict[str, int]:
        """
        Process multiple papers in batch

        Args:
            papers_dir: Directory containing papers
            pattern: File pattern to match
            force_reprocess: Force reprocessing of all papers

        Returns:
            Processing statistics
        """
        stats = {'processed': 0, 'failed': 0, 'skipped': 0}

        # Find paper files
        paper_files = list(papers_dir.rglob(pattern))
        logger.info(f"Found {len(paper_files)} papers to process")

        for paper_path in paper_files:
            if self.process_paper_with_ai(paper_path, force_reprocess):
                stats['processed'] += 1
            else:
                stats['failed'] += 1

        # Save updated vocabulary
        self.pipeline.vocab_builder.save_vocabulary()

        logger.info(f"Batch processing complete: {stats}")
        return stats

    def rebuild_vocabulary_from_papers(self, papers_dir: Path) -> int:
        """
        Rebuild vocabulary by re-analyzing all papers

        Args:
            papers_dir: Directory containing papers

        Returns:
            Number of papers processed
        """
        # Clear existing vocabulary
        self.pipeline.vocab_builder.vocabulary.clear()

        # Process all papers to rebuild vocabulary
        stats = self.process_papers_batch(papers_dir, force_reprocess=True)

        logger.info(f"Vocabulary rebuilt from {stats['processed']} papers")
        return stats['processed']

    def _is_recently_processed(self, paper_path: Path) -> bool:
        """Check if paper was processed recently"""
        try:
            content = paper_path.read_text(encoding='utf-8')

            # Look for linking metadata comment
            metadata_pattern = re.compile(
                r'<!-- KEYWORD_LINKING_METADATA:\s*({.*?})\s*-->',
                re.DOTALL
            )

            match = metadata_pattern.search(content)
            if match:
                metadata_dict = json.loads(match.group(1))
                # Could add timestamp comparison logic here
                return True

        except Exception:
            pass
        return False

    def _get_recent_trending_keywords(self) -> Dict[str, Any]:
        """Get recent trending keywords (placeholder implementation)"""
        # This could be implemented later to track keyword frequency over time
        return {}

    def get_vocabulary_stats(self) -> Dict[str, Any]:
        """Get vocabulary statistics"""
        vocab = self.pipeline.matcher.vocabulary

        if not vocab:
            return {'total_entries': 0, 'categories': {}}

        # Count by category
        category_counts = {}
        total_frequency = 0
        total_degree = 0

        for entry in vocab.values():
            category = entry.category
            category_counts[category] = category_counts.get(category, 0) + 1
            total_frequency += entry.frequency
            total_degree += entry.degree

        return {
            'total_entries': len(vocab),
            'categories': category_counts,
            'total_frequency': total_frequency,
            'total_degree': total_degree,
            'avg_frequency': total_frequency / len(vocab) if vocab else 0,
            'avg_degree': total_degree / len(vocab) if vocab else 0
        }

    def export_vocabulary(self, output_path: Path) -> bool:
        """Export vocabulary in human-readable format"""
        try:
            vocab = self.pipeline.matcher.vocabulary

            export_data = {
                'metadata': {
                    'total_entries': len(vocab),
                    'export_timestamp': str(datetime.now())
                },
                'vocabulary': [
                    {
                        'canonical': entry.canonical_name,
                        'aliases': list(entry.aliases),
                        'category': entry.category,
                        'frequency': entry.frequency,
                        'degree': entry.degree
                    }
                    for entry in sorted(vocab.values(),
                                      key=lambda x: x.frequency + x.degree,
                                      reverse=True)
                ]
            }

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)

            logger.info(f"Vocabulary exported to {output_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to export vocabulary: {e}")
            return False