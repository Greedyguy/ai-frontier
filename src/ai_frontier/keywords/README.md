# Keyword Linking Pipeline for Obsidian Graph Management

A comprehensive system for normalizing keywords, managing canonical vocabulary, and inserting idempotent wikilinks into paper templates while preserving metadata.

## Overview

This system implements the requirements for an Obsidian-focused keyword linking pipeline that:

- ✅ **Canonical Vocabulary Matching**: Uses cosine similarity ≥ 0.85 to match keywords to existing vocabulary
- ✅ **Link Budget Management**: Enforces constraints (max 3 links per paper, category limits)
- ✅ **Idempotent Wikilink Insertion**: Safely updates papers without duplication
- ✅ **Metadata Preservation**: Stores linking metadata in hidden HTML comments
- ✅ **Vocabulary Rebuilding**: Manages canonical vocabulary with merge operations and degree capping

## Architecture

### Core Components

1. **CanonicalVocabularyMatcher**: Handles vocabulary matching with TF-IDF embeddings and cosine similarity
2. **LinkBudgetManager**: Enforces linking constraints and selects optimal keywords
3. **WikilinkInserter**: Manages idempotent wikilink insertion with metadata preservation
4. **VocabularyBuilder**: Handles vocabulary updates with merge operations and degree capping
5. **KeywordLinkingPipeline**: Main orchestrator coordinating all components

### AI Integration

- **KeywordExtractor**: Integrates with existing AI prompt system for keyword extraction
- **IntegratedKeywordLinker**: Combines AI extraction with the linking pipeline

## Usage

### CLI Interface

The system provides a comprehensive CLI for all operations:

```bash
# Process all papers in a directory
python -m ai_frontier.keywords.cli --vocab-path data/vocabulary.json process-papers \
  --papers-dir reports/individual_papers

# Process a single paper
python -m ai_frontier.keywords.cli --vocab-path data/vocabulary.json process-paper \
  --paper-path "reports/individual_papers/2025-09-17/A Taxonomy_20250917.md"

# Rebuild entire vocabulary from papers
python -m ai_frontier.keywords.cli --vocab-path data/vocabulary.json rebuild-vocab \
  --papers-dir reports/individual_papers

# Export vocabulary for inspection
python -m ai_frontier.keywords.cli --vocab-path data/vocabulary.json export-vocab \
  --output-path exports/vocabulary_export.json

# Show vocabulary statistics
python -m ai_frontier.keywords.cli --vocab-path data/vocabulary.json stats
```

### Programmatic Usage

```python
from pathlib import Path
from ai_frontier.keywords import IntegratedKeywordLinker
from ai_frontier.translation.translator import get_translator

# Initialize the system
vocab_path = Path("data/vocabulary.json")
papers_dir = Path("reports/individual_papers")
translator = get_translator("openai")  # or "claude"

linker = IntegratedKeywordLinker(vocab_path, papers_dir, translator)

# Process papers
stats = linker.process_papers_batch(papers_dir)
print(f"Processed: {stats['processed']}, Failed: {stats['failed']}")

# Get vocabulary statistics
vocab_stats = linker.get_vocabulary_stats()
print(f"Total vocabulary entries: {vocab_stats['total_entries']}")
```

## Implementation Details

### Canonical Vocabulary Matching

The `resolve_canonical()` function implements the core matching logic:

```python
def resolve_canonical(candidate: str, controlled_vocab: Dict) -> Tuple[Optional[str], float, str]:
    """
    Returns:
        (matched_name | None, similarity, action)
        action: 'exact_match', 'similarity_match', 'new_canonical'
    """
```

- **Exact matching**: Checks canonical names and aliases for perfect matches
- **Similarity matching**: Uses TF-IDF + cosine similarity with threshold ≥ 0.85
- **New canonical**: Proposes new entries when no good match exists

### Link Selection Budget

The budget system enforces these constraints:

- **Global limit**: Maximum 3 links per paper
- **Category limits**:
  - `broad_technical`: Max 1 per paper
  - `specific_connectable`: No limit
  - `unique_technical`: No limit (but requires novelty ≥ 0.6)
  - `evolved_concepts`: No limit
- **Quality filter**: All links must have `link_intent_score ≥ 0.5`

### Wikilink Format

Generated wikilinks follow Obsidian format:
```markdown
[[keywords/Transformer Architecture|transformer]]
[[keywords/Attention Mechanism|attention]]
```

### Metadata Preservation

Linking metadata is stored in HTML comments:

```html
<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22T16:45:30",
  "vocabulary_version": "1.0",
  "selected_keywords": ["Transformer Architecture", "Attention Mechanism"],
  "rejected_keywords": ["Neural Networks"],
  "similarity_scores": {"Transformer Architecture": 0.95}
}
-->
```

## Data Structures

### KeywordCandidate

```python
@dataclass
class KeywordCandidate:
    surface: str                # As appears in paper
    canonical: str              # Canonical form
    aliases: List[str]          # Alternative names
    category: str               # Category classification
    rationale: str              # Selection rationale
    novelty_score: float        # 0-1
    connectivity_score: float   # 0-1
    specificity_score: float    # 0-1
    link_intent_score: float    # 0-1
```

### CanonicalEntry

```python
@dataclass
class CanonicalEntry:
    canonical_name: str
    aliases: Set[str]
    frequency: int              # Usage frequency
    degree: int                 # Number of papers linking
    category: str
    embedding: Optional[np.ndarray]  # TF-IDF embedding
```

## Configuration

### Environment Variables

Required for AI integration:
- `OPENAI_API_KEY`: For OpenAI-based keyword extraction
- `ANTHROPIC_API_KEY`: For Claude-based keyword extraction

### File Paths

- **Vocabulary file**: `data/vocabulary.json` (default)
- **Papers directory**: `reports/individual_papers/`
- **Export directory**: `exports/`

## Integration with Existing System

The keyword linking pipeline integrates seamlessly with the existing AI Frontier system:

1. **Prompt Templates**: Uses existing `keyword_extraction` template from `prompts/templates.py`
2. **Translation System**: Leverages existing `BaseTranslator` classes
3. **Paper Format**: Works with current markdown paper template structure
4. **Metadata Sections**: Preserves and enhances existing metadata format

## Performance Characteristics

- **Vocabulary matching**: O(n) where n = vocabulary size
- **TF-IDF similarity**: O(m*k) where m = candidate length, k = vocabulary size
- **Memory usage**: Scales with vocabulary size and embedding dimensions
- **Batch processing**: Efficient for large paper collections

## Error Handling

The system includes comprehensive error handling:

- **Missing dependencies**: Graceful fallback when API keys unavailable
- **Malformed papers**: Skips invalid files with logging
- **Vocabulary corruption**: Rebuilds from papers if needed
- **Network failures**: Retries with exponential backoff

## Testing

Basic functionality tested:
- ✅ Core component imports
- ✅ Keyword candidate creation
- ✅ Link budget management
- ✅ Vocabulary matching logic
- ✅ CLI interface help system

## Future Enhancements

Potential improvements for future versions:

1. **Advanced Embeddings**: Upgrade to transformer-based embeddings (e.g., sentence-transformers)
2. **Interactive Mode**: GUI for vocabulary curation and link approval
3. **Batch Processing**: Parallel processing for large paper collections
4. **Analytics Dashboard**: Visualization of vocabulary growth and linking patterns
5. **Integration Testing**: Comprehensive end-to-end testing with real papers

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies installed: `pip install -e .`
2. **API Key Missing**: Set environment variables for translation providers
3. **Vocabulary Not Found**: Initialize with `rebuild-vocab` command first
4. **Permission Errors**: Check file/directory permissions for vocabulary and papers

### Debug Mode

Enable detailed logging:
```bash
python -m ai_frontier.keywords.cli --log-level DEBUG <command>
```

## License

Part of the AI Frontier project - see main project LICENSE for details.