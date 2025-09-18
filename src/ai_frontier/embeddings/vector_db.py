"""FAISS vector database manager for paper embeddings."""

import os
import pickle
import json
import logging
import numpy as np
import faiss
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime

from .service import PaperEmbedding, EmbeddingsService


class VectorDatabase:
    """FAISS-based vector database for paper embeddings."""

    def __init__(self,
                 db_path: str = "data/embeddings",
                 embedding_dim: int = 1536,
                 index_type: str = "flat"):
        """Initialize vector database.

        Args:
            db_path: Path to store database files
            embedding_dim: Dimension of embedding vectors
            index_type: FAISS index type ('flat', 'ivf', 'hnsw')
        """
        self.db_path = Path(db_path)
        self.db_path.mkdir(parents=True, exist_ok=True)

        self.embedding_dim = embedding_dim
        self.index_type = index_type
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # FAISS index and metadata storage
        self.index = None
        self.paper_metadata: Dict[int, PaperEmbedding] = {}
        self.arxiv_id_to_index: Dict[str, int] = {}
        self.next_index = 0

        # File paths
        self.index_file = self.db_path / "faiss.index"
        self.metadata_file = self.db_path / "metadata.pkl"
        self.config_file = self.db_path / "config.json"

        # Initialize or load existing database
        self._initialize_or_load()

    def _initialize_or_load(self):
        """Initialize new database or load existing one."""
        if self._database_exists():
            self._load_database()
        else:
            self._create_new_database()

    def _database_exists(self) -> bool:
        """Check if database files exist."""
        return (self.index_file.exists() and
                self.metadata_file.exists() and
                self.config_file.exists())

    def _create_new_database(self):
        """Create a new FAISS database."""
        self.logger.info(f"Creating new vector database at {self.db_path}")

        # Create FAISS index based on type
        if self.index_type == "flat":
            self.index = faiss.IndexFlatIP(self.embedding_dim)  # Inner Product (cosine similarity)
        elif self.index_type == "ivf":
            quantizer = faiss.IndexFlatIP(self.embedding_dim)
            self.index = faiss.IndexIVFFlat(quantizer, self.embedding_dim, 100)  # 100 clusters
        elif self.index_type == "hnsw":
            self.index = faiss.IndexHNSWFlat(self.embedding_dim, 32)  # 32 connections
        else:
            raise ValueError(f"Unsupported index type: {self.index_type}")

        # Save initial configuration
        self._save_config()
        self._save_database()

    def _load_database(self):
        """Load existing database from disk."""
        try:
            self.logger.info(f"Loading existing vector database from {self.db_path}")

            # Load configuration
            with open(self.config_file, 'r') as f:
                config = json.load(f)

            # Verify configuration compatibility
            if config['embedding_dim'] != self.embedding_dim:
                raise ValueError(f"Embedding dimension mismatch: {config['embedding_dim']} vs {self.embedding_dim}")

            # Load FAISS index
            self.index = faiss.read_index(str(self.index_file))

            # Load metadata
            with open(self.metadata_file, 'rb') as f:
                data = pickle.load(f)
                self.paper_metadata = data['metadata']
                self.arxiv_id_to_index = data['arxiv_id_to_index']
                self.next_index = data['next_index']

            self.logger.info(f"Loaded database with {len(self.paper_metadata)} papers")

        except Exception as e:
            self.logger.error(f"Failed to load database: {e}")
            self.logger.info("Creating new database instead")
            self._create_new_database()

    def _save_database(self):
        """Save database to disk."""
        try:
            # Save FAISS index
            faiss.write_index(self.index, str(self.index_file))

            # Save metadata
            metadata_data = {
                'metadata': self.paper_metadata,
                'arxiv_id_to_index': self.arxiv_id_to_index,
                'next_index': self.next_index
            }

            with open(self.metadata_file, 'wb') as f:
                pickle.dump(metadata_data, f)

            self.logger.debug("Database saved successfully")

        except Exception as e:
            self.logger.error(f"Failed to save database: {e}")
            raise

    def _save_config(self):
        """Save database configuration."""
        config = {
            'embedding_dim': self.embedding_dim,
            'index_type': self.index_type,
            'created_at': datetime.now().isoformat(),
            'version': '1.0'
        }

        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)

    def add_paper(self, paper_embedding: PaperEmbedding) -> bool:
        """Add a paper embedding to the database.

        Args:
            paper_embedding: PaperEmbedding object to add

        Returns:
            True if successfully added, False if already exists
        """
        try:
            # Check if paper already exists
            if paper_embedding.arxiv_id in self.arxiv_id_to_index:
                self.logger.warning(f"Paper {paper_embedding.arxiv_id} already exists in database")
                return False

            # Normalize embedding for cosine similarity
            embedding = paper_embedding.embedding.copy()
            embedding = embedding / np.linalg.norm(embedding)

            # Add to FAISS index
            embedding_2d = embedding.reshape(1, -1).astype(np.float32)
            self.index.add(embedding_2d)

            # Store metadata
            current_index = self.next_index
            self.paper_metadata[current_index] = paper_embedding
            self.arxiv_id_to_index[paper_embedding.arxiv_id] = current_index
            self.next_index += 1

            # Save database
            self._save_database()

            self.logger.debug(f"Added paper {paper_embedding.arxiv_id} to database (index: {current_index})")
            return True

        except Exception as e:
            self.logger.error(f"Failed to add paper {paper_embedding.arxiv_id}: {e}")
            return False

    def add_papers_batch(self, paper_embeddings: List[PaperEmbedding]) -> int:
        """Add multiple paper embeddings in batch.

        Args:
            paper_embeddings: List of PaperEmbedding objects

        Returns:
            Number of papers successfully added
        """
        added_count = 0

        # Filter out existing papers
        new_papers = []
        for paper_emb in paper_embeddings:
            if paper_emb.arxiv_id not in self.arxiv_id_to_index:
                new_papers.append(paper_emb)
            else:
                self.logger.debug(f"Skipping existing paper: {paper_emb.arxiv_id}")

        if not new_papers:
            self.logger.info("No new papers to add")
            return 0

        try:
            # Prepare embeddings matrix
            embeddings_matrix = []
            for paper_emb in new_papers:
                # Normalize embedding
                embedding = paper_emb.embedding.copy()
                embedding = embedding / np.linalg.norm(embedding)
                embeddings_matrix.append(embedding)

            embeddings_matrix = np.array(embeddings_matrix, dtype=np.float32)

            # Add to FAISS index
            self.index.add(embeddings_matrix)

            # Store metadata
            for i, paper_emb in enumerate(new_papers):
                current_index = self.next_index + i
                self.paper_metadata[current_index] = paper_emb
                self.arxiv_id_to_index[paper_emb.arxiv_id] = current_index

            self.next_index += len(new_papers)
            added_count = len(new_papers)

            # Save database
            self._save_database()

            self.logger.info(f"Added {added_count} papers to database")

        except Exception as e:
            self.logger.error(f"Failed to add papers batch: {e}")

        return added_count

    def search_similar(self, query_embedding: np.ndarray, top_k: int = 10,
                      min_similarity: float = 0.7) -> List[Tuple[PaperEmbedding, float]]:
        """Search for similar papers using embedding.

        Args:
            query_embedding: Query embedding vector
            top_k: Number of similar papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            List of tuples (PaperEmbedding, similarity_score)
        """
        try:
            if self.index.ntotal == 0:
                self.logger.warning("Database is empty")
                return []

            # Normalize query embedding
            query_embedding = query_embedding.copy()
            query_embedding = query_embedding / np.linalg.norm(query_embedding)
            query_2d = query_embedding.reshape(1, -1).astype(np.float32)

            # Search in FAISS
            similarities, indices = self.index.search(query_2d, min(top_k * 2, self.index.ntotal))

            # Filter results and prepare response
            results = []
            for similarity, idx in zip(similarities[0], indices[0]):
                if idx == -1:  # FAISS returns -1 for invalid indices
                    continue

                # Convert inner product back to cosine similarity (0-1 range)
                cosine_similarity = (similarity + 1) / 2

                if cosine_similarity >= min_similarity:
                    paper_embedding = self.paper_metadata.get(idx)
                    if paper_embedding:
                        results.append((paper_embedding, float(cosine_similarity)))

            # Sort by similarity and return top_k
            results.sort(key=lambda x: x[1], reverse=True)
            return results[:top_k]

        except Exception as e:
            self.logger.error(f"Failed to search similar papers: {e}")
            return []

    def find_similar_papers(self, arxiv_id: str, top_k: int = 5,
                           min_similarity: float = 0.7) -> List[Tuple[PaperEmbedding, float]]:
        """Find papers similar to a specific paper in the database.

        Args:
            arxiv_id: ArXiv ID of the reference paper
            top_k: Number of similar papers to return
            min_similarity: Minimum similarity threshold

        Returns:
            List of tuples (PaperEmbedding, similarity_score)
        """
        try:
            # Get the reference paper
            if arxiv_id not in self.arxiv_id_to_index:
                self.logger.warning(f"Paper {arxiv_id} not found in database")
                return []

            ref_index = self.arxiv_id_to_index[arxiv_id]
            ref_paper = self.paper_metadata[ref_index]

            # Search for similar papers
            results = self.search_similar(ref_paper.embedding, top_k + 1, min_similarity)

            # Remove the reference paper itself
            filtered_results = [(paper, sim) for paper, sim in results if paper.arxiv_id != arxiv_id]

            return filtered_results[:top_k]

        except Exception as e:
            self.logger.error(f"Failed to find similar papers for {arxiv_id}: {e}")
            return []

    def get_paper(self, arxiv_id: str) -> Optional[PaperEmbedding]:
        """Get a paper by ArXiv ID.

        Args:
            arxiv_id: ArXiv ID of the paper

        Returns:
            PaperEmbedding object or None if not found
        """
        if arxiv_id in self.arxiv_id_to_index:
            index = self.arxiv_id_to_index[arxiv_id]
            return self.paper_metadata.get(index)
        return None

    def list_papers(self) -> List[PaperEmbedding]:
        """Get list of all papers in the database.

        Returns:
            List of PaperEmbedding objects
        """
        return list(self.paper_metadata.values())

    def remove_paper(self, arxiv_id: str) -> bool:
        """Remove a paper from the database.

        Note: FAISS doesn't support efficient deletion, so this only removes
        from metadata. The embedding remains in the index.

        Args:
            arxiv_id: ArXiv ID of the paper to remove

        Returns:
            True if successfully removed, False if not found
        """
        try:
            if arxiv_id not in self.arxiv_id_to_index:
                return False

            index = self.arxiv_id_to_index[arxiv_id]
            del self.paper_metadata[index]
            del self.arxiv_id_to_index[arxiv_id]

            self._save_database()
            self.logger.info(f"Removed paper {arxiv_id} from database")
            return True

        except Exception as e:
            self.logger.error(f"Failed to remove paper {arxiv_id}: {e}")
            return False

    def get_stats(self) -> Dict[str, int]:
        """Get database statistics.

        Returns:
            Dictionary with database statistics
        """
        return {
            "total_papers": len(self.paper_metadata),
            "index_total": self.index.ntotal if self.index else 0,
            "embedding_dim": self.embedding_dim,
            "next_index": self.next_index
        }


def get_vector_database(db_path: str = "data/embeddings",
                       embedding_dim: int = 1536,
                       index_type: str = "flat") -> VectorDatabase:
    """Factory function for creating VectorDatabase instance."""
    return VectorDatabase(db_path=db_path, embedding_dim=embedding_dim, index_type=index_type)