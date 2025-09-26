<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:52:29.278681",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Non-uniform Vector Quantization",
    "Embedding Vectors",
    "Vector Search",
    "High-Dimensionality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Non-uniform Vector Quantization": 0.78,
    "Embedding Vectors": 0.7,
    "Vector Search": 0.75,
    "High-Dimensionality": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "non-uniform vector quantization",
        "canonical": "Non-uniform Vector Quantization",
        "aliases": [
          "NVQ"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, offering a new approach to vector compression.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "embedding vectors",
        "canonical": "Embedding Vectors",
        "aliases": [
          "vector embeddings"
        ],
        "category": "broad_technical",
        "rationale": "Embedding vectors are fundamental to the paper's discussion on vector search and compression.",
        "novelty_score": 0.45,
        "connectivity_score": 0.72,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "vector search",
        "canonical": "Vector Search",
        "aliases": [
          "vector retrieval"
        ],
        "category": "specific_connectable",
        "rationale": "Vector search is a key application area for the proposed quantization technique.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "high-dimensionality",
        "canonical": "High-Dimensionality",
        "aliases": [
          "high-dimensional"
        ],
        "category": "specific_connectable",
        "rationale": "High-dimensionality is a critical challenge addressed by the quantization technique.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "retrieving large vectors",
      "computational cost"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "non-uniform vector quantization",
      "resolved_canonical": "Non-uniform Vector Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "embedding vectors",
      "resolved_canonical": "Embedding Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.72,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "vector search",
      "resolved_canonical": "Vector Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "high-dimensionality",
      "resolved_canonical": "High-Dimensionality",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Individualized non-uniform quantization for vector search

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18471.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18471](https://arxiv.org/abs/2509.18471)

## 🔗 유사한 논문
- [[2025-09-24/SBVR_ Summation of BitVector Representation for Efficient LLM Quantization_20250924|SBVR: Summation of BitVector Representation for Efficient LLM Quantization]] (82.3% similar)
- [[2025-09-22/Triplet Loss Based Quantum Encoding for Class Separability_20250922|Triplet Loss Based Quantum Encoding for Class Separability]] (82.0% similar)
- [[2025-09-23/GuidedQuant_ Large Language Model Quantization via Exploiting End Loss Guidance_20250923|GuidedQuant: Large Language Model Quantization via Exploiting End Loss Guidance]] (81.8% similar)
- [[2025-09-23/QVGen_ Pushing the Limit of Quantized Video Generative Models_20250923|QVGen: Pushing the Limit of Quantized Video Generative Models]] (81.6% similar)
- [[2025-09-23/VQToken_ Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models_20250923|VQToken: Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Embedding Vectors|Embedding Vectors]]
**🔗 Specific Connectable**: [[keywords/Vector Search|Vector Search]], [[keywords/High-Dimensionality|High-Dimensionality]]
**⚡ Unique Technical**: [[keywords/Non-uniform Vector Quantization|Non-uniform Vector Quantization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18471v1 Announce Type: new 
Abstract: Embedding vectors are widely used for representing unstructured data and searching through it for semantically similar items. However, the large size of these vectors, due to their high-dimensionality, creates problems for modern vector search techniques: retrieving large vectors from memory/storage is expensive and their footprint is costly. In this work, we present NVQ (non-uniform vector quantization), a new vector compression technique that is computationally and spatially efficient in the high-fidelity regime. The core in NVQ is to use novel parsimonious and computationally efficient nonlinearities for building non-uniform vector quantizers. Critically, these quantizers are \emph{individually} learned for each indexed vector. Our experimental results show that NVQ exhibits improved accuracy compared to the state of the art with a minimal computational cost.

## 📝 요약

이 연구는 비정형 데이터를 표현하고 유사 항목을 검색하는 데 사용되는 임베딩 벡터의 고차원성으로 인한 문제를 해결하기 위해 NVQ(비균일 벡터 양자화)라는 새로운 벡터 압축 기법을 제안합니다. NVQ는 고충실도 환경에서 계산 및 공간 효율성을 제공하며, 각 벡터에 대해 개별적으로 학습된 비균일 벡터 양자기를 사용합니다. 실험 결과, NVQ는 최소한의 계산 비용으로 기존 기술 대비 향상된 정확성을 보여줍니다.

## 🎯 주요 포인트

- 1. NVQ는 비균일 벡터 양자화를 통해 고차원 벡터의 크기를 효율적으로 압축하는 기술입니다.
- 2. NVQ는 각 벡터에 대해 개별적으로 학습된 새로운 비선형성을 사용하여 벡터 양자화를 수행합니다.
- 3. 실험 결과, NVQ는 최소한의 계산 비용으로 기존 기술 대비 향상된 정확성을 보여줍니다.
- 4. NVQ는 높은 정확성을 유지하면서도 계산 및 공간 효율성을 제공합니다.


---

*Generated on 2025-09-24 14:52:29*