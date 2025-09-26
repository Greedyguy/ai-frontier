"""RAG (Retrieval-Augmented Generation) search service for papers."""

import logging
import re
from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime, date
from pathlib import Path

from ..embeddings.service import EmbeddingsService, PaperEmbedding
from ..embeddings.vector_db import VectorDatabase


class RAGSearchService:
    """RAG search service for semantic paper search."""

    def __init__(self,
                 vector_db_path: str = "data/embeddings",
                 embedding_model: str = "text-embedding-3-small"):
        """Initialize RAG search service.

        Args:
            vector_db_path: Path to vector database
            embedding_model: OpenAI embedding model to use
        """
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Initialize services
        self.embeddings_service = EmbeddingsService(model=embedding_model)
        self.vector_db = VectorDatabase(db_path=vector_db_path)

        self.logger.info(f"RAG search service initialized with {self.vector_db.get_stats()['total_papers']} papers")

    def search_papers(self,
                     query: str,
                     top_k: int = 10,
                     min_similarity: float = 0.5,
                     categories: Optional[List[str]] = None,
                     start_date: Optional[date] = None,
                     end_date: Optional[date] = None,
                     page: int = 1,
                     page_size: int = 10) -> Dict[str, Any]:
        """Search for papers using semantic similarity.

        Args:
            query: Search query text
            top_k: Maximum number of results to retrieve (up to 100)
            min_similarity: Minimum similarity threshold (0.0-1.0)
            categories: Filter by categories (e.g., ['cs.AI', 'cs.LG'])
            start_date: Filter papers from this date
            end_date: Filter papers until this date
            page: Page number (1-based)
            page_size: Results per page (max 100)

        Returns:
            Dictionary with search results and metadata
        """
        try:
            # Validate parameters
            top_k = min(max(1, top_k), 100)  # Limit to 100
            page_size = min(max(1, page_size), 100)  # Limit to 100
            page = max(1, page)
            min_similarity = max(0.0, min(1.0, min_similarity))

            # Generate query embedding
            self.logger.info(f"Searching for: '{query}' with similarity >= {min_similarity}")
            query_embedding = self.embeddings_service.create_embedding(query)

            # Get initial results from vector DB (fetch more for filtering)
            raw_results = self.vector_db.search_similar(
                query_embedding=query_embedding,
                top_k=min(top_k * 3, 300),  # Fetch more for filtering
                min_similarity=min_similarity
            )

            # Apply filters
            filtered_results = self._apply_filters(
                raw_results, categories, start_date, end_date
            )

            # Paginate results
            total_results = len(filtered_results)
            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            paginated_results = filtered_results[start_idx:end_idx]

            # Format results
            formatted_results = []
            for paper_embedding, similarity in paginated_results:
                formatted_results.append({
                    "arxiv_id": paper_embedding.arxiv_id,
                    "title": paper_embedding.title,
                    "abstract": paper_embedding.abstract,
                    "summary": paper_embedding.summary,
                    "key_points": paper_embedding.key_points,
                    "similarity_score": round(similarity, 4),
                    "timestamp": paper_embedding.timestamp.isoformat(),
                    "metadata": paper_embedding.metadata or {},
                    "category": paper_embedding.metadata.get("category", "unknown") if paper_embedding.metadata else "unknown",
                    "published_date": paper_embedding.metadata.get("published_date") if paper_embedding.metadata else None,
                    "authors": self._ensure_list(paper_embedding.metadata.get("authors", []) if paper_embedding.metadata else []),
                    "pdf_url": f"https://arxiv.org/pdf/{paper_embedding.arxiv_id}.pdf"
                })

            # Prepare response
            response = {
                "query": query,
                "total_results": total_results,
                "page": page,
                "page_size": page_size,
                "total_pages": (total_results + page_size - 1) // page_size,
                "min_similarity": min_similarity,
                "applied_filters": {
                    "categories": categories,
                    "start_date": start_date.isoformat() if start_date else None,
                    "end_date": end_date.isoformat() if end_date else None
                },
                "results": formatted_results,
                "search_stats": {
                    "query_length": len(query),
                    "embedding_dimension": len(query_embedding),
                    "raw_results_count": len(raw_results),
                    "filtered_results_count": total_results
                }
            }

            self.logger.info(f"Found {total_results} papers (page {page}/{response['total_pages']})")
            return response

        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return {
                "query": query,
                "total_results": 0,
                "page": page,
                "page_size": page_size,
                "total_pages": 0,
                "results": [],
                "error": str(e)
            }

    def _apply_filters(self,
                      results: List[Tuple[PaperEmbedding, float]],
                      categories: Optional[List[str]] = None,
                      start_date: Optional[date] = None,
                      end_date: Optional[date] = None) -> List[Tuple[PaperEmbedding, float]]:
        """Apply filters to search results.

        Args:
            results: Raw search results
            categories: Filter by categories
            start_date: Filter papers from this date
            end_date: Filter papers until this date

        Returns:
            Filtered results
        """
        filtered_results = []

        for paper_embedding, similarity in results:
            # Category filter
            if categories:
                paper_category = paper_embedding.metadata.get("category", "") if paper_embedding.metadata else ""
                if not any(cat.lower() in paper_category.lower() for cat in categories):
                    continue

            # Date filter
            if start_date or end_date:
                paper_date_str = paper_embedding.metadata.get("published_date") if paper_embedding.metadata else None
                if paper_date_str:
                    try:
                        paper_date = datetime.fromisoformat(paper_date_str).date()

                        if start_date and paper_date < start_date:
                            continue
                        if end_date and paper_date > end_date:
                            continue
                    except (ValueError, TypeError):
                        # Skip papers with invalid dates if date filtering is requested
                        if start_date or end_date:
                            continue

            filtered_results.append((paper_embedding, similarity))

        return filtered_results

    def find_similar_papers(self,
                           arxiv_id: str,
                           top_k: int = 5,
                           min_similarity: float = 0.7) -> Dict[str, Any]:
        """Find papers similar to a specific paper.

        Args:
            arxiv_id: ArXiv ID of the reference paper
            top_k: Number of similar papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            Dictionary with similar papers and metadata
        """
        try:
            # Validate parameters
            top_k = min(max(1, top_k), 20)  # Limit to 20 for similar papers
            min_similarity = max(0.0, min(1.0, min_similarity))

            # Find similar papers
            results = self.vector_db.find_similar_papers(
                arxiv_id=arxiv_id,
                top_k=top_k,
                min_similarity=min_similarity
            )

            # Get reference paper info
            reference_paper = self.vector_db.get_paper(arxiv_id)

            # Format results
            formatted_results = []
            for paper_embedding, similarity in results:
                formatted_results.append({
                    "arxiv_id": paper_embedding.arxiv_id,
                    "title": paper_embedding.title,
                    "abstract": paper_embedding.abstract,
                    "summary": paper_embedding.summary,
                    "similarity_score": round(similarity, 4),
                    "category": paper_embedding.metadata.get("category", "unknown") if paper_embedding.metadata else "unknown",
                    "published_date": paper_embedding.metadata.get("published_date") if paper_embedding.metadata else None,
                    "pdf_url": f"https://arxiv.org/pdf/{paper_embedding.arxiv_id}.pdf"
                })

            response = {
                "reference_paper": {
                    "arxiv_id": reference_paper.arxiv_id,
                    "title": reference_paper.title,
                    "abstract": reference_paper.abstract
                } if reference_paper else None,
                "similar_papers": formatted_results,
                "total_found": len(formatted_results),
                "min_similarity": min_similarity
            }

            self.logger.info(f"Found {len(formatted_results)} similar papers for {arxiv_id}")
            return response

        except Exception as e:
            self.logger.error(f"Similar papers search failed for {arxiv_id}: {e}")
            return {
                "reference_paper": None,
                "similar_papers": [],
                "total_found": 0,
                "error": str(e)
            }

    def get_database_stats(self) -> Dict[str, Any]:
        """Get vector database statistics.

        Returns:
            Database statistics
        """
        stats = self.vector_db.get_stats()

        # Get category and date distribution
        papers = self.vector_db.list_papers()
        categories = {}
        date_range = {"earliest": None, "latest": None}

        for paper in papers:
            # Count categories
            if paper.metadata:
                category = paper.metadata.get("category", "unknown")
                categories[category] = categories.get(category, 0) + 1

                # Track date range
                pub_date = paper.metadata.get("published_date")
                if pub_date:
                    try:
                        paper_date = datetime.fromisoformat(pub_date).date()
                        if not date_range["earliest"] or paper_date < date_range["earliest"]:
                            date_range["earliest"] = paper_date
                        if not date_range["latest"] or paper_date > date_range["latest"]:
                            date_range["latest"] = paper_date
                    except (ValueError, TypeError):
                        pass

        return {
            "total_papers": stats["total_papers"],
            "embedding_dimension": stats["embedding_dim"],
            "categories": categories,
            "date_range": {
                "earliest": date_range["earliest"].isoformat() if date_range["earliest"] else None,
                "latest": date_range["latest"].isoformat() if date_range["latest"] else None
            },
            "index_type": self.vector_db.index_type
        }

    def suggest_query_improvements(self, query: str) -> List[str]:
        """Suggest improvements for search queries.

        Args:
            query: Original search query

        Returns:
            List of suggested improvements
        """
        suggestions = []

        # Basic suggestions based on query analysis
        if len(query.split()) == 1:
            suggestions.append("Try adding more descriptive terms to your query")

        if query.islower():
            suggestions.append("Try including technical terms or acronyms in your search")

        if not any(term in query.lower() for term in ["learning", "neural", "algorithm", "model", "analysis"]):
            suggestions.append("Consider adding domain-specific terms like 'learning', 'neural', 'algorithm', etc.")

        # Technical term suggestions
        common_ml_terms = ["machine learning", "deep learning", "neural network", "transformer",
                          "attention", "embedding", "classification", "regression", "clustering"]

        if not any(term in query.lower() for term in common_ml_terms):
            suggestions.append("Try including machine learning terms if relevant to your search")

        return suggestions[:3]  # Limit to 3 suggestions

    def _ensure_list(self, value):
        """Ensure the value is a list, converting from string if necessary."""
        if isinstance(value, list):
            return value
        elif isinstance(value, str):
            if value == "":
                return []
            # Split by comma if it looks like a comma-separated list
            return [item.strip() for item in value.split(",") if item.strip()]
        else:
            return []