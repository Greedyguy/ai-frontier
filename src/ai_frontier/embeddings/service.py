"""OpenAI embeddings service for paper similarity analysis."""

import os
import logging
import numpy as np
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
from datetime import datetime
import openai
from openai import OpenAI

from ..arxiv.client import ArxivPaper


@dataclass
class PaperEmbedding:
    """Paper embedding data structure."""
    arxiv_id: str
    title: str
    abstract: str
    summary: str
    key_points: List[str]
    embedding: np.ndarray
    timestamp: datetime
    metadata: Dict[str, str] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class EmbeddingsService:
    """OpenAI embeddings service for generating paper embeddings."""

    def __init__(self, api_key: Optional[str] = None, model: str = "text-embedding-3-small"):
        """Initialize embeddings service.

        Args:
            api_key: OpenAI API key. If None, uses OPENAI_API_KEY environment variable
            model: OpenAI embedding model to use
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Embedding model dimensions
        self.dimensions = {
            "text-embedding-3-small": 1536,
            "text-embedding-3-large": 3072,
            "text-embedding-ada-002": 1536
        }
        self.embedding_dim = self.dimensions.get(model, 1536)

        self.logger.info(f"EmbeddingsService initialized with model: {model}, dimensions: {self.embedding_dim}")

    def create_embedding(self, text: str) -> np.ndarray:
        """Create embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            Numpy array containing the embedding vector
        """
        try:
            response = self.client.embeddings.create(
                input=text,
                model=self.model
            )

            embedding = np.array(response.data[0].embedding, dtype=np.float32)
            return embedding

        except Exception as e:
            self.logger.error(f"Failed to create embedding: {e}")
            raise

    def create_embeddings_batch(self, texts: List[str]) -> List[np.ndarray]:
        """Create embeddings for multiple texts in a batch.

        Args:
            texts: List of texts to embed

        Returns:
            List of numpy arrays containing embedding vectors
        """
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=self.model
            )

            embeddings = []
            for data in response.data:
                embedding = np.array(data.embedding, dtype=np.float32)
                embeddings.append(embedding)

            return embeddings

        except Exception as e:
            self.logger.error(f"Failed to create batch embeddings: {e}")
            raise

    def embed_paper_content(self, paper: ArxivPaper, summary: str, key_points: List[str]) -> PaperEmbedding:
        """Create embedding for a research paper's content.

        Combines title, abstract, summary, and key points into a comprehensive text
        representation for embedding.

        Args:
            paper: ArxivPaper object
            summary: Generated summary of the paper
            key_points: List of key points from the paper

        Returns:
            PaperEmbedding object containing the paper data and embedding
        """
        try:
            # Combine all text content for embedding
            content_parts = [
                f"Title: {paper.title}",
                f"Abstract: {paper.abstract}",
                f"Summary: {summary}",
                f"Key Points: {'; '.join(key_points)}"
            ]

            combined_text = "\\n\\n".join(content_parts)

            # Create embedding
            embedding = self.create_embedding(combined_text)

            # Create PaperEmbedding object
            paper_embedding = PaperEmbedding(
                arxiv_id=paper.arxiv_id,
                title=paper.title,
                abstract=paper.abstract,
                summary=summary,
                key_points=key_points,
                embedding=embedding,
                timestamp=datetime.now(),
                metadata={
                    "category": paper.category,
                    "published": paper.published.isoformat(),
                    "authors": ", ".join(paper.authors[:3]),  # First 3 authors
                    "pdf_url": paper.pdf_url
                }
            )

            self.logger.debug(f"Created embedding for paper {paper.arxiv_id}")
            return paper_embedding

        except Exception as e:
            self.logger.error(f"Failed to embed paper {paper.arxiv_id}: {e}")
            raise

    def embed_query(self, query: str) -> np.ndarray:
        """Create embedding for a search query.

        Args:
            query: Search query text

        Returns:
            Numpy array containing the query embedding
        """
        return self.create_embedding(query)

    def calculate_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """Calculate cosine similarity between two embeddings.

        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector

        Returns:
            Cosine similarity score between 0 and 1
        """
        try:
            # Normalize vectors
            norm1 = np.linalg.norm(embedding1)
            norm2 = np.linalg.norm(embedding2)

            if norm1 == 0 or norm2 == 0:
                return 0.0

            # Calculate cosine similarity
            similarity = np.dot(embedding1, embedding2) / (norm1 * norm2)

            # Ensure result is between 0 and 1
            similarity = (similarity + 1) / 2

            return float(similarity)

        except Exception as e:
            self.logger.error(f"Failed to calculate similarity: {e}")
            return 0.0

    def find_similar_papers(self, target_embedding: np.ndarray, paper_embeddings: List[PaperEmbedding],
                          top_k: int = 5, min_similarity: float = 0.7) -> List[tuple]:
        """Find papers similar to the target embedding.

        Args:
            target_embedding: Target embedding to compare against
            paper_embeddings: List of PaperEmbedding objects to search
            top_k: Maximum number of similar papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            List of tuples (PaperEmbedding, similarity_score) sorted by similarity
        """
        similarities = []

        for paper_emb in paper_embeddings:
            similarity = self.calculate_similarity(target_embedding, paper_emb.embedding)

            if similarity >= min_similarity:
                similarities.append((paper_emb, similarity))

        # Sort by similarity (descending) and return top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]


def get_embeddings_service(api_key: Optional[str] = None, model: str = "text-embedding-3-small") -> EmbeddingsService:
    """Factory function for creating EmbeddingsService instance."""
    return EmbeddingsService(api_key=api_key, model=model)