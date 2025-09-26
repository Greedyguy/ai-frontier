---
keywords:
  - Large Language Model
  - Semantic Indexing
  - Generative Recommendation
  - Recursive Residual Searching
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16446
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:38:16.777642",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Semantic Indexing",
    "Generative Recommendation",
    "Recursive Residual Searching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Semantic Indexing": 0.78,
    "Generative Recommendation": 0.77,
    "Recursive Residual Searching": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and connect to a broad range of related research topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Semantic Indexing",
        "canonical": "Semantic Indexing",
        "aliases": [
          "Semantic ID Generation"
        ],
        "category": "unique_technical",
        "rationale": "Semantic Indexing is a novel approach proposed in the paper, essential for understanding the unique contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Generative Recommendation",
        "canonical": "Generative Recommendation",
        "aliases": [
          "Generative RecSys"
        ],
        "category": "unique_technical",
        "rationale": "Generative Recommendation is a key application area for the proposed methods, linking to specific advancements in recommendation systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Recursive Residual Searching",
        "canonical": "Recursive Residual Searching",
        "aliases": [
          "RRS"
        ],
        "category": "unique_technical",
        "rationale": "Recursive Residual Searching is a novel algorithm introduced in the paper, crucial for understanding its technical innovations.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Semantic Indexing",
      "resolved_canonical": "Semantic Indexing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Generative Recommendation",
      "resolved_canonical": "Generative Recommendation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Recursive Residual Searching",
      "resolved_canonical": "Recursive Residual Searching",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16446.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16446](https://arxiv.org/abs/2509.16446)

## 🔗 유사한 논문
- [[2025-09-22/IGD_ Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation_20250922|IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation]] (84.2% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (82.4% similar)
- [[2025-09-22/Chunk Knowledge Generation Model for Enhanced Information Retrieval_ A Multi-task Learning Approach_20250922|Chunk Knowledge Generation Model for Enhanced Information Retrieval: A Multi-task Learning Approach]] (80.9% similar)
- [[2025-09-22/Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings_20250922|Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings]] (80.5% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Semantic Indexing|Semantic Indexing]], [[keywords/Generative Recommendation|Generative Recommendation]], [[keywords/Recursive Residual Searching|Recursive Residual Searching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16446v1 Announce Type: cross 
Abstract: Semantic identifiers (IDs) have proven effective in adapting large language models for generative recommendation and retrieval. However, existing methods often suffer from semantic ID conflicts, where semantically similar documents (or items) are assigned identical IDs. A common strategy to avoid conflicts is to append a non-semantic token to distinguish them, which introduces randomness and expands the search space, therefore hurting performance. In this paper, we propose purely semantic indexing to generate unique, semantic-preserving IDs without appending non-semantic tokens. We enable unique ID assignment by relaxing the strict nearest-centroid selection and introduce two model-agnostic algorithms: exhaustive candidate matching (ECM) and recursive residual searching (RRS). Extensive experiments on sequential recommendation, product search, and document retrieval tasks demonstrate that our methods improve both overall and cold-start performance, highlighting the effectiveness of ensuring ID uniqueness.

## 📝 요약

이 논문은 대규모 언어 모델을 위한 생성 추천 및 검색에서 발생하는 의미 ID 충돌 문제를 해결하기 위해 고유한 의미 보존 ID를 생성하는 방법을 제안합니다. 기존 방법은 유사한 문서에 동일한 ID를 부여하는 문제를 겪으며, 이를 피하기 위해 비의미적 토큰을 추가하지만 이는 성능 저하를 초래합니다. 본 연구는 비의미적 토큰 없이 고유한 ID를 생성하기 위해 ECM(Exhaustive Candidate Matching)과 RRS(Recursive Residual Searching)라는 두 가지 모델 비종속 알고리즘을 도입합니다. 실험 결과, 제안된 방법은 순차적 추천, 제품 검색, 문서 검색에서 전반적인 성능과 콜드 스타트 성능을 개선하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 기존 방법은 유사한 문서에 동일한 ID를 할당하여 발생하는 의미 ID 충돌 문제를 겪습니다.
- 2. 비의미적 토큰을 추가하여 ID 충돌을 피하는 기존 전략은 무작위성을 도입하고 검색 공간을 확장하여 성능을 저하시킵니다.
- 3. 본 연구에서는 비의미적 토큰을 추가하지 않고 고유하고 의미를 보존하는 ID를 생성하는 순수 의미 인덱싱을 제안합니다.
- 4. 고유 ID 할당을 위해 엄격한 최근접 중심 선택을 완화하고, ECM과 RRS라는 두 가지 모델 비종속 알고리즘을 도입합니다.
- 5. 실험 결과, 제안된 방법이 순차 추천, 제품 검색, 문서 검색에서 전반적인 성능과 콜드 스타트 성능을 향상시킵니다.


---

*Generated on 2025-09-24 03:38:16*