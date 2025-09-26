"""Similarity manager for paper relationship analysis and Obsidian link generation."""

import logging
from typing import List, Dict, Optional, Tuple
from pathlib import Path

from .service import EmbeddingsService, PaperEmbedding, get_embeddings_service
from .vector_db import VectorDatabase, get_vector_database
from ..arxiv.client import ArxivPaper


class SimilarityManager:
    """Manages paper similarity analysis and related paper discovery."""

    def __init__(self,
                 embeddings_service: Optional[EmbeddingsService] = None,
                 vector_db: Optional[VectorDatabase] = None,
                 db_path: str = "data/embeddings"):
        """Initialize similarity manager.

        Args:
            embeddings_service: EmbeddingsService instance
            vector_db: VectorDatabase instance
            db_path: Path to vector database
        """
        self.embeddings_service = embeddings_service or get_embeddings_service()
        self.vector_db = vector_db or get_vector_database(db_path=db_path)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def process_paper(self, paper: ArxivPaper, summary: str, key_points: List[str]) -> PaperEmbedding:
        """Process a paper and add it to the vector database.

        Args:
            paper: ArxivPaper object
            summary: Generated summary
            key_points: List of key points

        Returns:
            PaperEmbedding object
        """
        try:
            # Create embedding for the paper
            paper_embedding = self.embeddings_service.embed_paper_content(paper, summary, key_points)

            # Add to vector database
            success = self.vector_db.add_paper(paper_embedding)

            if success:
                self.logger.info(f"Successfully processed and stored paper: {paper.arxiv_id}")
            else:
                self.logger.warning(f"Paper already exists in database: {paper.arxiv_id}")

            return paper_embedding

        except Exception as e:
            self.logger.error(f"Failed to process paper {paper.arxiv_id}: {e}")
            raise

    def process_papers_batch(self, papers_data: List[Tuple[ArxivPaper, str, List[str]]]) -> List[PaperEmbedding]:
        """Process multiple papers in batch.

        Args:
            papers_data: List of tuples (paper, summary, key_points)

        Returns:
            List of PaperEmbedding objects
        """
        paper_embeddings = []

        try:
            # Create embeddings for all papers
            for paper, summary, key_points in papers_data:
                try:
                    paper_embedding = self.embeddings_service.embed_paper_content(paper, summary, key_points)
                    paper_embeddings.append(paper_embedding)
                except Exception as e:
                    self.logger.error(f"Failed to create embedding for {paper.arxiv_id}: {e}")

            # Add all embeddings to database in batch
            if paper_embeddings:
                added_count = self.vector_db.add_papers_batch(paper_embeddings)
                self.logger.info(f"Successfully processed {added_count} papers in batch")

            return paper_embeddings

        except Exception as e:
            self.logger.error(f"Failed to process papers batch: {e}")
            return paper_embeddings

    def find_similar_papers(self, arxiv_id: str, top_k: int = 5,
                           min_similarity: float = 0.75) -> List[Tuple[PaperEmbedding, float]]:
        """Find papers similar to a given paper.

        Args:
            arxiv_id: ArXiv ID of the reference paper
            top_k: Number of similar papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            List of tuples (PaperEmbedding, similarity_score)
        """
        return self.vector_db.find_similar_papers(arxiv_id, top_k, min_similarity)

    def search_by_content(self, query: str, top_k: int = 10,
                         min_similarity: float = 0.7) -> List[Tuple[PaperEmbedding, float]]:
        """Search papers by content similarity.

        Args:
            query: Search query text
            top_k: Number of papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            List of tuples (PaperEmbedding, similarity_score)
        """
        try:
            query_embedding = self.embeddings_service.embed_query(query)
            return self.vector_db.search_similar(query_embedding, top_k, min_similarity)

        except Exception as e:
            self.logger.error(f"Failed to search by content: {e}")
            return []

    def generate_similarity_report(self, arxiv_id: str) -> Optional[Dict]:
        """Generate a comprehensive similarity report for a paper.

        Args:
            arxiv_id: ArXiv ID of the paper

        Returns:
            Dictionary containing similarity analysis
        """
        try:
            # Get the paper
            paper = self.vector_db.get_paper(arxiv_id)
            if not paper:
                return None

            # Find similar papers
            similar_papers = self.find_similar_papers(arxiv_id, top_k=10, min_similarity=0.6)

            # Categorize similarities
            high_similarity = [(p, s) for p, s in similar_papers if s >= 0.8]
            medium_similarity = [(p, s) for p, s in similar_papers if 0.7 <= s < 0.8]
            low_similarity = [(p, s) for p, s in similar_papers if 0.6 <= s < 0.7]

            # Generate report
            report = {
                "paper": {
                    "arxiv_id": paper.arxiv_id,
                    "title": paper.title,
                    "summary": paper.summary
                },
                "similarity_analysis": {
                    "total_similar_papers": len(similar_papers),
                    "high_similarity": len(high_similarity),
                    "medium_similarity": len(medium_similarity),
                    "low_similarity": len(low_similarity)
                },
                "similar_papers": {
                    "high_similarity": [
                        {
                            "arxiv_id": p.arxiv_id,
                            "title": p.title,
                            "similarity": round(s, 3),
                            "category": p.metadata.get("category", "unknown")
                        }
                        for p, s in high_similarity
                    ],
                    "medium_similarity": [
                        {
                            "arxiv_id": p.arxiv_id,
                            "title": p.title,
                            "similarity": round(s, 3),
                            "category": p.metadata.get("category", "unknown")
                        }
                        for p, s in medium_similarity
                    ],
                    "low_similarity": [
                        {
                            "arxiv_id": p.arxiv_id,
                            "title": p.title,
                            "similarity": round(s, 3),
                            "category": p.metadata.get("category", "unknown")
                        }
                        for p, s in low_similarity
                    ]
                }
            }

            return report

        except Exception as e:
            self.logger.error(f"Failed to generate similarity report for {arxiv_id}: {e}")
            return None

    def _generate_filename_from_title_and_date(self, title: str, published_date) -> str:
        """Generate filename from paper title and published date."""
        import re
        # Sanitize title for filename - 콜론만 언더스코어로 변경, 띄어쓰기는 유지
        sanitized_title = title.replace(':', '_')
        # 다른 금지된 문자들 제거 (띄어쓰기는 유지)
        illegal_chars = r'[<>"/\\|?*\x00-\x1f]'
        sanitized_title = re.sub(illegal_chars, '', sanitized_title)
        sanitized_title = re.sub(r'_+', '_', sanitized_title)
        sanitized_title = sanitized_title.strip(' .')
        if not sanitized_title:
            sanitized_title = "untitled"
        # Get date string
        date_str = published_date.strftime("%Y%m%d")
        return f"{sanitized_title}_{date_str}"

    def generate_obsidian_similarity_links(self, arxiv_id: str, max_links: int = 3,
                                         min_similarity: float = 0.75) -> List[str]:
        """Generate Obsidian links to similar papers.

        Args:
            arxiv_id: ArXiv ID of the reference paper
            max_links: Maximum number of links to generate
            min_similarity: Minimum similarity threshold

        Returns:
            List of Obsidian link strings
        """
        try:
            similar_papers = self.find_similar_papers(arxiv_id, top_k=max_links, min_similarity=min_similarity)

            links = []
            for paper, similarity in similar_papers:
                # Create Obsidian link to similar paper using actual filename
                # Format: [[filename_without_extension|display_text]]
                # published 정보를 metadata에서 가져오기
                published_str = paper.metadata.get("published", "")
                if published_str:
                    from datetime import datetime
                    try:
                        published_date = datetime.fromisoformat(published_str.replace('Z', '+00:00'))
                    except:
                        published_date = datetime.now()
                else:
                    published_date = datetime.now()
                
                filename_base = self._generate_filename_from_title_and_date(paper.title, published_date)
                similarity_pct = round(similarity * 100, 1)
                # Use title for display, filename for linking
                sanitized_title = paper.title.replace("[", "").replace("]", "").replace("|", "")
                # Add date folder path to the link
                date_folder = published_date.strftime("%Y-%m-%d")
                link = f"[[{date_folder}/{filename_base}|{sanitized_title}]] ({similarity_pct}% similar)"
                links.append(link)

            return links

        except Exception as e:
            self.logger.error(f"Failed to generate Obsidian similarity links for {arxiv_id}: {e}")
            return []

    def get_database_stats(self) -> Dict:
        """Get vector database statistics.

        Returns:
            Dictionary with database statistics
        """
        return self.vector_db.get_stats()

    def rebuild_database(self) -> bool:
        """Rebuild the vector database from scratch.

        Returns:
            True if successful, False otherwise
        """
        try:
            # Get all current papers
            papers = self.vector_db.list_papers()

            # Create new database instance
            db_path = self.vector_db.db_path
            self.vector_db = get_vector_database(str(db_path))

            # Re-add all papers
            if papers:
                added_count = self.vector_db.add_papers_batch(papers)
                self.logger.info(f"Rebuilt database with {added_count} papers")

            return True

        except Exception as e:
            self.logger.error(f"Failed to rebuild database: {e}")
            return False

    def export_similarities(self, output_path: str) -> bool:
        """Export all paper similarities to a file.

        Args:
            output_path: Path to output file

        Returns:
            True if successful, False otherwise
        """
        try:
            papers = self.vector_db.list_papers()
            similarities_data = []

            for paper in papers:
                similar_papers = self.find_similar_papers(paper.arxiv_id, top_k=5, min_similarity=0.7)

                paper_data = {
                    "arxiv_id": paper.arxiv_id,
                    "title": paper.title,
                    "similar_papers": [
                        {
                            "arxiv_id": p.arxiv_id,
                            "title": p.title,
                            "similarity": round(s, 3)
                        }
                        for p, s in similar_papers
                    ]
                }
                similarities_data.append(paper_data)

            # Save to file
            import json
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(similarities_data, f, indent=2, ensure_ascii=False)

            self.logger.info(f"Exported similarities for {len(similarities_data)} papers to {output_path}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to export similarities: {e}")
            return False


def get_similarity_manager(db_path: str = "data/embeddings") -> SimilarityManager:
    """Factory function for creating SimilarityManager instance."""
    return SimilarityManager(db_path=db_path)