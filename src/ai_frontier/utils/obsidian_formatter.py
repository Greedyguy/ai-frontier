"""Obsidian formatting utilities for generating linked metadata."""

import re
from typing import List, Dict, Set, Optional
from datetime import datetime
from ..arxiv.client import ArxivPaper
from ..summarization.summarizer import get_summarizer
from ..keywords.extractor import get_keyword_extractor
from ..embeddings.similarity_manager import get_similarity_manager


class ObsidianFormatter:
    """Format paper data with Obsidian-style links."""

    def __init__(self, summarization_provider: str = "openai", enable_similarity: bool = True):
        """Initialize the formatter."""
        self.summarizer = get_summarizer(summarization_provider)
        self.keyword_extractor = get_keyword_extractor(provider=summarization_provider)

        # Initialize similarity manager if enabled
        self.enable_similarity = enable_similarity
        self.similarity_manager = None
        if enable_similarity:
            try:
                self.similarity_manager = get_similarity_manager()
            except Exception as e:
                print(f"Warning: Could not initialize similarity manager: {e}")
                self.enable_similarity = False

    def _sanitize_link_name(self, text: str) -> str:
        """Sanitize text for use in Obsidian links."""
        # Remove or replace characters that might cause issues in Obsidian links
        sanitized = re.sub(r'[<>:"/\\|?*]', '', text)
        sanitized = re.sub(r'\s+', ' ', sanitized).strip()
        return sanitized

    def _extract_keywords_from_paper(self, paper: ArxivPaper, summary: str = "", key_points: List[str] = None) -> List[str]:
        """Extract categorized keywords using the new keyword extraction system."""
        try:
            # Use the new categorized keyword extractor
            categorized_keywords = self.keyword_extractor.extract_keywords(paper.title, paper.abstract)

            # Convert categorized keywords to flat list, maintaining priority order
            keywords = []

            # Priority order for trend analysis and research connections
            priority_categories = ["broad_technical", "specific_connectable", "unique_technical", "evolved_concepts"]

            for category in priority_categories:
                if category in categorized_keywords:
                    keywords.extend(categorized_keywords[category])

            # Log the categorized extraction for debugging
            print(f"Categorized keywords extracted: {categorized_keywords}")
            print(f"Final keywords list: {keywords}")

            return keywords[:5]  # Limit to 5 keywords maximum

        except Exception as e:
            print(f"Categorized keyword extraction failed: {e}, falling back to rule-based method")
            # Fallback to rule-based method if extraction fails
            return self.extract_keywords_from_title_abstract(paper.title, paper.abstract)[:5]

    def _extract_keywords_with_llm(self, title: str, abstract: str, summary: str = "", key_points: List[str] = None) -> List[str]:
        """Extract keywords using LLM analysis."""
        key_points = key_points or []

        # Prepare content for LLM analysis
        content_parts = [f"제목: {title}", f"초록: {abstract}"]

        if summary:
            content_parts.append(f"요약: {summary}")

        if key_points:
            content_parts.append(f"주요 포인트: {', '.join(key_points)}")

        content = "\n\n".join(content_parts)

        prompt = f"""다음 논문 정보를 분석하여 Obsidian 링크에 적합한 키워드들을 추출해주세요.

{content}

요구사항:
1. 논문의 핵심 개념, 기술, 방법론을 나타내는 키워드 선택
2. 5-10개의 키워드 추출
3. 각 키워드는 1-3단어로 구성
4. 너무 일반적인 단어(예: "연구", "논문", "방법") 피하기
5. 기술명, 알고리즘명, 도메인 용어 우선
6. 새로운 기술이나 개념도 포함

형식: 키워드들을 쉼표로 구분하여 나열
예시: Deep Learning, Transformer, Attention Mechanism, Computer Vision, Image Classification

키워드:"""

        try:
            response = self.summarizer.summarize_text(prompt)

            # Parse keywords from response
            keywords = []
            # Extract keywords from the response
            lines = response.strip().split('\n')
            for line in lines:
                # Look for lines with comma-separated keywords
                if ',' in line and not line.startswith('예시:') and not line.startswith('형식:'):
                    keyword_line = line.strip()
                    # Remove any leading text like "키워드:" or numbers
                    keyword_line = re.sub(r'^[^a-zA-Z가-힣]*', '', keyword_line)

                    # Split by comma and clean up
                    extracted = [kw.strip() for kw in keyword_line.split(',')]
                    for kw in extracted:
                        if kw and len(kw) >= 2 and len(kw) <= 30:
                            # Clean up the keyword
                            clean_kw = re.sub(r'[^\w\s가-힣]', '', kw).strip()
                            if clean_kw:
                                keywords.append(clean_kw)

                    if keywords:  # If we found keywords in this line, we're done
                        break

            # If no keywords found through comma parsing, try other methods
            if not keywords:
                # Look for quoted keywords or other patterns
                quoted_keywords = re.findall(r'"([^"]+)"', response)
                keywords.extend([kw.strip() for kw in quoted_keywords if kw.strip()])

                # Look for keywords in bullet points
                bullet_keywords = re.findall(r'[-•*]\s*([^\n]+)', response)
                keywords.extend([kw.strip() for kw in bullet_keywords if kw.strip()])

            # Clean and format keywords
            final_keywords = []
            for kw in keywords[:10]:  # Limit to 10 keywords
                if len(kw) >= 2 and len(kw) <= 30:
                    # Format keyword (title case)
                    formatted_kw = ' '.join(word.capitalize() for word in kw.split())
                    final_keywords.append(formatted_kw)

            return final_keywords

        except Exception as e:
            print(f"Error in LLM keyword extraction: {e}")
            return []

    def generate_obsidian_links(
        self,
        paper: ArxivPaper,
        summary: str = "",
        key_points: List[str] = None
    ) -> str:
        """Generate Obsidian-style links for paper metadata."""
        links = []

        # Date link
        date_str = paper.published.strftime("%Y-%m-%d")
        links.append(f"[[daily/{date_str}|{date_str}]]")

        # Keywords links with categorized approach
        try:
            categorized_keywords = self.keyword_extractor.extract_keywords(paper.title, paper.abstract)

            # Add keywords with category prefixes for better organization
            for category, keywords_list in categorized_keywords.items():
                for keyword in keywords_list:
                    sanitized_keyword = self._sanitize_link_name(keyword)
                    # Use category-specific folders for better organization
                    if category == "broad_technical":
                        links.append(f"[[keywords/broad/{sanitized_keyword}|{sanitized_keyword}]]")
                    elif category == "specific_connectable":
                        links.append(f"[[keywords/specific/{sanitized_keyword}|{sanitized_keyword}]]")
                    elif category == "unique_technical":
                        links.append(f"[[keywords/unique/{sanitized_keyword}|{sanitized_keyword}]]")
                    elif category == "evolved_concepts":
                        links.append(f"[[keywords/evolved/{sanitized_keyword}|{sanitized_keyword}]]")
        except Exception as e:
            print(f"Error in categorized keyword linking: {e}, using fallback")
            # Fallback to simple keyword extraction
            keywords = self._extract_keywords_from_paper(paper, summary, key_points)
            for keyword in keywords:
                sanitized_keyword = self._sanitize_link_name(keyword)
                links.append(f"[[keywords/{sanitized_keyword}|{sanitized_keyword}]]")

        # Author links
        for author in paper.authors[:5]:  # Limit to first 5 authors to avoid clutter
            sanitized_author = self._sanitize_link_name(author)
            links.append(f"[[authors/{sanitized_author}|{sanitized_author}]]")

        # Category link
        sanitized_category = self._sanitize_link_name(paper.category)
        links.append(f"[[categories/{sanitized_category}|{sanitized_category}]]")

        # Similar papers links (if similarity is enabled)
        if self.enable_similarity and self.similarity_manager:
            try:
                similar_links = self.similarity_manager.generate_obsidian_similarity_links(
                    paper.arxiv_id, max_links=3, min_similarity=0.6
                )
                links.extend(similar_links)
            except Exception as e:
                print(f"Warning: Could not generate similarity links for {paper.arxiv_id}: {e}")

        return " ".join(links)

    def generate_metadata_section(
        self,
        paper: ArxivPaper,
        summary: str = "",
        key_points: List[str] = None
    ) -> str:
        """Generate a complete metadata section with Obsidian links and categorized keywords."""
        links = self.generate_obsidian_links(paper, summary, key_points)

        # Generate categorized keywords display
        try:
            categorized_keywords = self.keyword_extractor.extract_keywords(paper.title, paper.abstract)

            keywords_display = []
            category_names = {
                "broad_technical": "🔬 Broad Technical",
                "specific_connectable": "🔗 Specific Connectable",
                "unique_technical": "⭐ Unique Technical",
                "evolved_concepts": "🚀 Evolved Concepts"
            }

            for category, keywords_list in categorized_keywords.items():
                if keywords_list:  # Only show categories that have keywords
                    category_display = category_names.get(category, category)
                    keywords_str = ", ".join(keywords_list)
                    keywords_display.append(f"**{category_display}**: {keywords_str}")

            keywords_section = "\n".join(keywords_display) if keywords_display else "No keywords extracted"

        except Exception as e:
            print(f"Error generating categorized keywords display: {e}")
            keywords_section = "Error extracting keywords"

        # Generate similarity section if enabled
        similarity_section = ""
        if self.enable_similarity and self.similarity_manager:
            try:
                similar_papers = self.similarity_manager.find_similar_papers(
                    paper.arxiv_id, top_k=5, min_similarity=0.6
                )
                if similar_papers:
                    similarity_lines = []
                    for similar_paper, similarity in similar_papers:
                        sim_pct = round(similarity * 100, 1)
                        sanitized_title = self._sanitize_link_name(similar_paper.title)
                        similarity_lines.append(f"- [[{sanitized_title}]] ({sim_pct}% similar)")

                    similarity_section = f"""
## 🔗 유사한 논문
{chr(10).join(similarity_lines)}
"""
            except Exception as e:
                print(f"Warning: Could not generate similarity section for {paper.arxiv_id}: {e}")

        metadata = f"""## 📋 메타데이터

**Links**: {links}

## 🏷️ 카테고리화된 키워드
{keywords_section}{similarity_section}

**ArXiv ID**: [{paper.arxiv_id}](https://arxiv.org/abs/{paper.arxiv_id})
**Published**: {paper.published.strftime("%Y-%m-%d")}
**Category**: {paper.category}
**PDF**: [Download]({paper.pdf_url})
"""
        return metadata

    def extract_keywords_from_title_abstract(self, title: str, abstract: str) -> List[str]:
        """Extract keywords specifically from title and abstract text."""
        keywords = set()
        text = f"{title} {abstract}".lower()

        # Technical terms that are commonly used in AI/ML papers
        technical_terms = [
            # Core ML/AI terms
            'neural network', 'deep learning', 'machine learning', 'artificial intelligence',
            'reinforcement learning', 'supervised learning', 'unsupervised learning',
            'self-supervised learning', 'semi-supervised learning',

            # Architecture terms
            'transformer', 'attention mechanism', 'self-attention', 'cross-attention',
            'convolutional neural network', 'cnn', 'recurrent neural network', 'rnn',
            'lstm', 'gru', 'autoencoder', 'vae', 'gan', 'generative adversarial network',

            # Model names
            'bert', 'gpt', 'llama', 't5', 'resnet', 'vit', 'vision transformer',

            # Techniques
            'fine-tuning', 'pre-training', 'transfer learning', 'few-shot learning',
            'zero-shot learning', 'in-context learning', 'prompt engineering',
            'knowledge distillation', 'pruning', 'quantization',

            # Applications
            'computer vision', 'natural language processing', 'nlp', 'speech recognition',
            'image classification', 'object detection', 'semantic segmentation',
            'machine translation', 'question answering', 'text generation',

            # Data and methods
            'multimodal', 'cross-modal', 'embedding', 'representation learning',
            'contrastive learning', 'adversarial training', 'data augmentation',
            'regularization', 'dropout', 'batch normalization',

            # Specific techniques
            'diffusion model', 'stable diffusion', 'clip', 'rag',
            'retrieval augmented generation', 'chain of thought', 'reasoning',
            'graph neural network', 'gnn', 'knowledge graph',

            # Algorithmic and theoretical terms
            'optimization', 'algorithm', 'fairness', 'assignment', 'scheduling',
            'graph theory', 'combinatorial optimization', 'linear programming',
            'integer programming', 'approximation algorithm', 'complexity',
            'multi-agent', 'game theory', 'mechanism design', 'auction',
            'matching', 'allocation', 'resource allocation', 'load balancing',
            'distributed computing', 'parallel computing', 'consensus',
            'blockchain', 'cryptocurrency', 'smart contract', 'federated learning',
            'privacy', 'differential privacy', 'homomorphic encryption',
            'adversarial example', 'robustness', 'interpretability', 'explainability',
            'bias', 'equity', 'social welfare', 'utility function', 'pareto optimal'
        ]

        # Look for these terms in the text
        for term in technical_terms:
            if term in text:
                # Format for display (capitalize first letter of each word)
                formatted_term = ' '.join(word.capitalize() for word in term.split())
                keywords.add(formatted_term)

        # Extract quoted terms (often indicate important concepts)
        quoted_terms = re.findall(r'"([^"]+)"', title + " " + abstract)
        for term in quoted_terms:
            if len(term.split()) <= 3:  # Only short phrases
                formatted_term = term.strip()
                if formatted_term:
                    keywords.add(formatted_term)

        # Extract terms in ALL CAPS (often acronyms)
        caps_terms = re.findall(r'\b[A-Z]{2,}\b', title + " " + abstract)
        for term in caps_terms:
            if len(term) >= 2 and len(term) <= 6:  # Reasonable acronym length
                keywords.add(term)

        # Extract important single words from title (often key concepts)
        title_words = [word.strip('.,!?;:()[]{}') for word in title.lower().split()]
        important_words = [
            'fairness', 'assignment', 'optimization', 'algorithm', 'learning', 'network',
            'model', 'training', 'inference', 'prediction', 'classification', 'regression',
            'clustering', 'segmentation', 'detection', 'recognition', 'generation', 'synthesis',
            'analysis', 'evaluation', 'framework', 'approach', 'method', 'technique',
            'system', 'architecture', 'design', 'implementation', 'performance', 'efficiency',
            'robustness', 'scalability', 'privacy', 'security', 'interpretability', 'explainability',
            'benchmark', 'dataset', 'experiment', 'study', 'survey', 'review',
            'multi-stage', 'multi-agent', 'multi-modal', 'multi-task', 'cross-domain',
            'real-time', 'large-scale', 'high-dimensional', 'sparse', 'dense',
            'supervised', 'unsupervised', 'semi-supervised', 'self-supervised',
            'online', 'offline', 'incremental', 'adaptive', 'dynamic', 'static'
        ]

        for word in title_words:
            if word in important_words and len(word) >= 4:  # Avoid short common words
                keywords.add(word.capitalize())

        # Extract compound terms with hyphens or underscores from title and abstract
        compound_terms = re.findall(r'\b[a-zA-Z]+[-_][a-zA-Z]+(?:[-_][a-zA-Z]+)*\b', title + " " + abstract)
        for term in compound_terms:
            if len(term) >= 5 and len(term) <= 25:  # Reasonable length
                # Format compound terms
                formatted_term = term.replace('-', ' ').replace('_', ' ').title()
                keywords.add(formatted_term)

        return sorted(list(keywords))