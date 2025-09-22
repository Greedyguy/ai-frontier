"""
Keyword Linking Pipeline Package

Provides comprehensive keyword normalization, canonical vocabulary management,
and Obsidian wikilink insertion for paper templates.
"""

from .linking_pipeline import (
    KeywordCandidate,
    CanonicalEntry,
    LinkingMetadata,
    CanonicalVocabularyMatcher,
    LinkBudgetManager,
    WikilinkInserter,
    VocabularyBuilder,
    KeywordLinkingPipeline
)

from .ai_integration import (
    KeywordExtractor,
    IntegratedKeywordLinker
)

__all__ = [
    # Data classes
    'KeywordCandidate',
    'CanonicalEntry',
    'LinkingMetadata',

    # Core components
    'CanonicalVocabularyMatcher',
    'LinkBudgetManager',
    'WikilinkInserter',
    'VocabularyBuilder',
    'KeywordLinkingPipeline',

    # AI integration
    'KeywordExtractor',
    'IntegratedKeywordLinker'
]