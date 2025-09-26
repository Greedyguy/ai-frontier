---
keywords:
  - Generative Entropy Maximization for Tables
  - Maximum Entropy
  - Higher-Order Interactions
  - Heterogeneous Data Types
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17752
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:07:51.897113",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Entropy Maximization for Tables",
    "Maximum Entropy",
    "Higher-Order Interactions",
    "Heterogeneous Data Types"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Entropy Maximization for Tables": 0.8,
    "Maximum Entropy": 0.75,
    "Higher-Order Interactions": 0.82,
    "Heterogeneous Data Types": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "GEM-T",
        "canonical": "Generative Entropy Maximization for Tables",
        "aliases": [
          "GEM-T"
        ],
        "category": "unique_technical",
        "rationale": "GEM-T is a novel approach specifically designed for generating synthetic tabular data, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "maximum entropy",
        "canonical": "Maximum Entropy",
        "aliases": [
          "MaxEnt"
        ],
        "category": "broad_technical",
        "rationale": "Maximum Entropy is a foundational concept in statistical mechanics and information theory, relevant to various generative models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "nth-order interactions",
        "canonical": "Higher-Order Interactions",
        "aliases": [
          "nth-order interactions"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding higher-order interactions is crucial for modeling complex dependencies in tabular data.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "heterogeneous data types",
        "canonical": "Heterogeneous Data Types",
        "aliases": [
          "mixed data types"
        ],
        "category": "specific_connectable",
        "rationale": "Handling heterogeneous data types is essential for generative models dealing with diverse datasets.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "tabular data",
      "synthetic data",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "GEM-T",
      "resolved_canonical": "Generative Entropy Maximization for Tables",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "maximum entropy",
      "resolved_canonical": "Maximum Entropy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "nth-order interactions",
      "resolved_canonical": "Higher-Order Interactions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "heterogeneous data types",
      "resolved_canonical": "Heterogeneous Data Types",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# GEM-T: Generative Tabular Data via Fitting Moments

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17752.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17752](https://arxiv.org/abs/2509.17752)

## 🔗 유사한 논문
- [[2025-09-19/TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (79.1% similar)
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (78.7% similar)
- [[2025-09-18/GEM-Bench_ A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing_20250918|GEM-Bench: A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing]] (78.6% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (77.9% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Maximum Entropy|Maximum Entropy]]
**🔗 Specific Connectable**: [[keywords/Higher-Order Interactions|Higher-Order Interactions]], [[keywords/Heterogeneous Data Types|Heterogeneous Data Types]]
**⚡ Unique Technical**: [[keywords/Generative Entropy Maximization for Tables|Generative Entropy Maximization for Tables]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17752v1 Announce Type: cross 
Abstract: Tabular data dominates data science but poses challenges for generative models, especially when the data is limited or sensitive. We present a novel approach to generating synthetic tabular data based on the principle of maximum entropy -- MaxEnt -- called GEM-T, for ``generative entropy maximization for tables.'' GEM-T directly captures nth-order interactions -- pairwise, third-order, etc. -- among columns of training data. In extensive testing, GEM-T matches or exceeds deep neural network approaches previously regarded as state-of-the-art in 23 of 34 publicly available datasets representing diverse subject domains (68\%). Notably, GEM-T involves orders-of-magnitude fewer trainable parameters, demonstrating that much of the information in real-world data resides in low-dimensional, potentially human-interpretable correlations, provided that the input data is appropriately transformed first. Furthermore, MaxEnt better handles heterogeneous data types (continuous vs. discrete vs. categorical), lack of local structure, and other features of tabular data. GEM-T represents a promising direction for light-weight high-performance generative models for structured data.

## 📝 요약

GEM-T는 최대 엔트로피 원칙을 기반으로 한 새로운 합성 표형 데이터 생성 방법으로, 데이터 열 간의 n차 상호작용을 직접 포착합니다. 34개의 다양한 공개 데이터셋 중 23개에서 기존 최첨단 심층 신경망 접근법과 동등하거나 더 나은 성능을 보였으며, 훈련 가능한 매개변수가 훨씬 적습니다. 이는 실제 데이터의 많은 정보가 저차원 상관관계에 있음을 시사합니다. GEM-T는 이질적인 데이터 유형과 지역 구조의 부재를 효과적으로 처리하며, 구조화된 데이터에 적합한 경량 고성능 생성 모델의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. GEM-T는 최대 엔트로피 원칙을 기반으로 한 새로운 합성 표형 데이터 생성 방법입니다.
- 2. GEM-T는 훈련 데이터 열 간의 n차 상호작용을 직접 포착하여, 기존의 심층 신경망 접근법과 비교해 68%의 데이터셋에서 동등하거나 더 나은 성능을 보였습니다.
- 3. GEM-T는 훈련 가능한 매개변수가 훨씬 적어도 실제 데이터의 정보가 저차원 상관관계에 많이 존재한다는 것을 보여줍니다.
- 4. MaxEnt는 이질적인 데이터 유형, 지역 구조의 부재 등 표형 데이터의 다양한 특성을 더 잘 처리합니다.
- 5. GEM-T는 구조화된 데이터를 위한 경량 고성능 생성 모델의 유망한 방향성을 제시합니다.


---

*Generated on 2025-09-24 00:07:51*