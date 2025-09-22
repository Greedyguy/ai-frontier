#!/usr/bin/env python3
"""
CLI Interface for Keyword Linking Pipeline

Provides command-line interface for managing and running the keyword linking system.
"""

import argparse
import sys
import logging
from pathlib import Path
from typing import Optional

from ..translation.translator import get_translator
from .ai_integration import IntegratedKeywordLinker


def setup_logging(level: str = "INFO"):
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def process_papers_command(args):
    """Process papers with keyword linking"""
    # Setup
    vocab_path = Path(args.vocab_path)
    papers_dir = Path(args.papers_dir)
    translation_provider = get_translator(args.provider)

    # Initialize linker
    linker = IntegratedKeywordLinker(vocab_path, papers_dir.parent, translation_provider)

    # Process papers
    print(f"Processing papers in: {papers_dir}")
    print(f"Using vocabulary: {vocab_path}")
    print(f"Translation provider: {args.provider}")

    stats = linker.process_papers_batch(
        papers_dir=papers_dir,
        pattern=args.pattern,
        force_reprocess=args.force
    )

    # Print results
    print(f"\nProcessing complete:")
    print(f"  Processed: {stats['processed']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Skipped: {stats['skipped']}")

    # Show vocabulary stats
    vocab_stats = linker.get_vocabulary_stats()
    print(f"\nVocabulary statistics:")
    print(f"  Total entries: {vocab_stats['total_entries']}")
    print(f"  Avg frequency: {vocab_stats['avg_frequency']:.2f}")
    print(f"  Avg degree: {vocab_stats['avg_degree']:.2f}")


def process_single_paper_command(args):
    """Process a single paper"""
    paper_path = Path(args.paper_path)
    vocab_path = Path(args.vocab_path)
    translation_provider = get_translator(args.provider)

    # Initialize linker
    linker = IntegratedKeywordLinker(vocab_path, paper_path.parent, translation_provider)

    # Process paper
    print(f"Processing paper: {paper_path}")

    success = linker.process_paper_with_ai(paper_path, force_reprocess=args.force)

    if success:
        print("✅ Paper processed successfully")
    else:
        print("❌ Paper processing failed")
        sys.exit(1)


def rebuild_vocabulary_command(args):
    """Rebuild vocabulary from all papers"""
    vocab_path = Path(args.vocab_path)
    papers_dir = Path(args.papers_dir)
    translation_provider = get_translator(args.provider)

    # Initialize linker
    linker = IntegratedKeywordLinker(vocab_path, papers_dir.parent, translation_provider)

    # Rebuild vocabulary
    print(f"Rebuilding vocabulary from: {papers_dir}")
    print("This will process ALL papers and may take a while...")

    processed_count = linker.rebuild_vocabulary_from_papers(papers_dir)

    print(f"✅ Vocabulary rebuilt from {processed_count} papers")

    # Show new stats
    vocab_stats = linker.get_vocabulary_stats()
    print(f"\nNew vocabulary statistics:")
    print(f"  Total entries: {vocab_stats['total_entries']}")
    print(f"  Categories: {vocab_stats['categories']}")


def export_vocabulary_command(args):
    """Export vocabulary to file"""
    vocab_path = Path(args.vocab_path)
    output_path = Path(args.output_path)
    papers_dir = Path(args.papers_dir) if args.papers_dir else vocab_path.parent
    translation_provider = get_translator(args.provider)

    # Initialize linker
    linker = IntegratedKeywordLinker(vocab_path, papers_dir, translation_provider)

    # Export vocabulary
    print(f"Exporting vocabulary to: {output_path}")

    success = linker.export_vocabulary(output_path)

    if success:
        print("✅ Vocabulary exported successfully")
    else:
        print("❌ Vocabulary export failed")
        sys.exit(1)


def show_stats_command(args):
    """Show vocabulary statistics"""
    vocab_path = Path(args.vocab_path)
    papers_dir = Path(args.papers_dir) if args.papers_dir else vocab_path.parent
    translation_provider = get_translator(args.provider)

    # Initialize linker
    linker = IntegratedKeywordLinker(vocab_path, papers_dir, translation_provider)

    # Get stats
    stats = linker.get_vocabulary_stats()

    print("Vocabulary Statistics:")
    print("=" * 50)
    print(f"Total entries: {stats['total_entries']}")
    print(f"Total frequency: {stats['total_frequency']}")
    print(f"Total degree: {stats['total_degree']}")
    print(f"Average frequency: {stats['avg_frequency']:.2f}")
    print(f"Average degree: {stats['avg_degree']:.2f}")

    print("\nCategories:")
    for category, count in stats['categories'].items():
        print(f"  {category}: {count}")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Keyword Linking Pipeline for Obsidian Graph Management",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all papers in directory
  python -m ai_frontier.keywords.cli process-papers \\
    --papers-dir reports/individual_papers \\
    --vocab-path data/vocabulary.json

  # Process single paper
  python -m ai_frontier.keywords.cli process-paper \\
    --paper-path "reports/individual_papers/2025-09-17/A Taxonomy_20250917.md" \\
    --vocab-path data/vocabulary.json

  # Rebuild entire vocabulary
  python -m ai_frontier.keywords.cli rebuild-vocab \\
    --papers-dir reports/individual_papers \\
    --vocab-path data/vocabulary.json

  # Export vocabulary
  python -m ai_frontier.keywords.cli export-vocab \\
    --vocab-path data/vocabulary.json \\
    --output-path exports/vocabulary_export.json

  # Show vocabulary statistics
  python -m ai_frontier.keywords.cli stats \\
    --vocab-path data/vocabulary.json
        """
    )

    # Global arguments
    parser.add_argument('--vocab-path', default='data/vocabulary.json',
                       help='Path to vocabulary file (default: data/vocabulary.json)')
    parser.add_argument('--provider', choices=['openai', 'claude'], default='openai',
                       help='AI provider for keyword extraction (default: openai)')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Logging level (default: INFO)')

    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Process papers command
    process_parser = subparsers.add_parser('process-papers', help='Process multiple papers')
    process_parser.add_argument('--papers-dir', required=True,
                               help='Directory containing paper files')
    process_parser.add_argument('--pattern', default='*.md',
                               help='File pattern to match (default: *.md)')
    process_parser.add_argument('--force', action='store_true',
                               help='Force reprocessing of all papers')

    # Process single paper command
    single_parser = subparsers.add_parser('process-paper', help='Process single paper')
    single_parser.add_argument('--paper-path', required=True,
                              help='Path to paper file')
    single_parser.add_argument('--force', action='store_true',
                              help='Force reprocessing')

    # Rebuild vocabulary command
    rebuild_parser = subparsers.add_parser('rebuild-vocab', help='Rebuild vocabulary')
    rebuild_parser.add_argument('--papers-dir', required=True,
                               help='Directory containing paper files')

    # Export vocabulary command
    export_parser = subparsers.add_parser('export-vocab', help='Export vocabulary')
    export_parser.add_argument('--output-path', required=True,
                              help='Output file path')
    export_parser.add_argument('--papers-dir',
                              help='Papers directory (for loading linker)')

    # Show statistics command
    stats_parser = subparsers.add_parser('stats', help='Show vocabulary statistics')
    stats_parser.add_argument('--papers-dir',
                             help='Papers directory (for loading linker)')

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Setup logging
    setup_logging(args.log_level)

    # Route to command handlers
    try:
        if args.command == 'process-papers':
            process_papers_command(args)
        elif args.command == 'process-paper':
            process_single_paper_command(args)
        elif args.command == 'rebuild-vocab':
            rebuild_vocabulary_command(args)
        elif args.command == 'export-vocab':
            export_vocabulary_command(args)
        elif args.command == 'stats':
            show_stats_command(args)
        else:
            print(f"Unknown command: {args.command}")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Command failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()