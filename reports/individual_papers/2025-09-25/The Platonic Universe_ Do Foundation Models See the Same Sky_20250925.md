---
keywords:
  - Transformer
  - Self-supervised Learning
  - Astronomy-specific Architectures
  - Representational Convergence
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19453
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:54:15.317812",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Self-supervised Learning",
    "Astronomy-specific Architectures",
    "Representational Convergence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.8,
    "Self-supervised Learning": 0.82,
    "Astronomy-specific Architectures": 0.75,
    "Representational Convergence": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "vision transformers",
        "canonical": "Transformer",
        "aliases": [
          "Vision Transformer",
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in machine learning, crucial for linking various model types.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "self-supervised models",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key method for training models without labeled data, relevant across domains.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "astronomy-specific architectures",
        "canonical": "Astronomy-specific Architectures",
        "aliases": [
          "astro architectures"
        ],
        "category": "unique_technical",
        "rationale": "These architectures are tailored for astronomical data, providing unique insights into domain-specific model design.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "representational convergence",
        "canonical": "Representational Convergence",
        "aliases": [
          "convergence of representations"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to understanding how different models align in their representations, crucial for cross-model analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "JWST",
      "HSC",
      "Legacy Survey",
      "DESI"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "vision transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "self-supervised models",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "astronomy-specific architectures",
      "resolved_canonical": "Astronomy-specific Architectures",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "representational convergence",
      "resolved_canonical": "Representational Convergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# The Platonic Universe: Do Foundation Models See the Same Sky?

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19453.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19453](https://arxiv.org/abs/2509.19453)

## 🔗 유사한 논문
- [[2025-09-22/Comparing Computational Pathology Foundation Models using Representational Similarity Analysis_20250922|Comparing Computational Pathology Foundation Models using Representational Similarity Analysis]] (80.6% similar)
- [[2025-09-17/Towards a Physics Foundation Model_20250917|Towards a Physics Foundation Model]] (79.3% similar)
- [[2025-09-23/From Prediction to Understanding_ Will AI Foundation Models Transform Brain Science?_20250923|From Prediction to Understanding: Will AI Foundation Models Transform Brain Science?]] (78.9% similar)
- [[2025-09-23/$\boldsymbol{\lambda}$-Orthogonality Regularization for Compatible Representation Learning_20250923|$\boldsymbol{\lambda}$-Orthogonality Regularization for Compatible Representation Learning]] (78.3% similar)
- [[2025-09-24/The Transparent Earth_ A Multimodal Foundation Model for the Earth's Subsurface_20250924|The Transparent Earth: A Multimodal Foundation Model for the Earth's Subsurface]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Astronomy-specific Architectures|Astronomy-specific Architectures]], [[keywords/Representational Convergence|Representational Convergence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19453v1 Announce Type: cross 
Abstract: We test the Platonic Representation Hypothesis (PRH) in astronomy by measuring representational convergence across a range of foundation models trained on different data types. Using spectroscopic and imaging observations from JWST, HSC, Legacy Survey, and DESI, we compare representations from vision transformers, self-supervised models, and astronomy-specific architectures via mutual $k$-nearest neighbour analysis. We observe consistent scaling: representational alignment generally increases with model capacity across our tested architectures, supporting convergence toward a shared representation of galaxy astrophysics. Our results suggest that astronomical foundation models can use pre-trained general-purpose architectures, allowing us to capitalise on the broader machine learning community's already-spent computational investment.

## 📝 요약

이 논문은 천문학에서 플라톤적 표현 가설(PRH)을 검증하기 위해 다양한 데이터 유형으로 훈련된 기초 모델 간의 표현 수렴을 측정합니다. JWST, HSC, Legacy Survey, DESI의 분광 및 이미지 관측 데이터를 사용하여 비전 트랜스포머, 자가 지도 학습 모델, 천문학 전용 아키텍처의 표현을 상호 $k$-최근접 이웃 분석을 통해 비교했습니다. 연구 결과, 모델 용량이 증가할수록 표현 정렬이 일반적으로 증가하여 은하 천체물리학의 공통 표현으로 수렴함을 확인했습니다. 이는 천문학 기초 모델이 사전 훈련된 범용 아키텍처를 활용할 수 있음을 시사하며, 기계 학습 커뮤니티의 기존 컴퓨팅 투자를 활용할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 플라톤적 표현 가설(PRH)을 천문학에서 테스트하여 다양한 데이터 유형으로 훈련된 기초 모델 간의 표현 수렴을 측정했습니다.
- 2. JWST, HSC, Legacy Survey, DESI의 분광 및 이미지 관측 데이터를 사용하여 비전 트랜스포머, 자기 지도 학습 모델, 천문학 전용 아키텍처의 표현을 상호 $k$-최근접 이웃 분석을 통해 비교했습니다.
- 3. 모델 용량이 증가함에 따라 표현 정렬이 일반적으로 증가하는 일관된 스케일링을 관찰했으며, 이는 은하 천체물리학의 공유 표현으로의 수렴을 지지합니다.
- 4. 우리의 결과는 천문학 기초 모델이 사전 훈련된 범용 아키텍처를 사용할 수 있음을 시사하며, 이를 통해 기계 학습 커뮤니티의 이미 투자된 계산 자원을 활용할 수 있습니다.


---

*Generated on 2025-09-25 16:54:15*