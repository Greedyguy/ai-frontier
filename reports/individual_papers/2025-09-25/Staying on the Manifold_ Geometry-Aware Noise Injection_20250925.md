---
keywords:
  - Geometry-Aware Noise
  - Manifold
  - Brownian Motion Noise
  - Tangent Space
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20201
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:46:05.591812",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Geometry-Aware Noise",
    "Manifold",
    "Brownian Motion Noise",
    "Tangent Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Geometry-Aware Noise": 0.78,
    "Manifold": 0.82,
    "Brownian Motion Noise": 0.7,
    "Tangent Space": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "geometry-aware noise",
        "canonical": "Geometry-Aware Noise",
        "aliases": [
          "geometric noise",
          "manifold noise"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and involves a novel approach to noise injection in machine learning models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "manifold",
        "canonical": "Manifold",
        "aliases": [
          "data manifold",
          "input manifold"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding manifolds is crucial for linking concepts related to data structure and geometry in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Brownian motion noise",
        "canonical": "Brownian Motion Noise",
        "aliases": [
          "stochastic noise",
          "random walk noise"
        ],
        "category": "unique_technical",
        "rationale": "This specific type of noise is a unique contribution to the noise injection methods discussed in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "tangent space",
        "canonical": "Tangent Space",
        "aliases": [
          "tangent plane",
          "linear approximation space"
        ],
        "category": "specific_connectable",
        "rationale": "Tangent spaces are fundamental in understanding the geometric properties of manifolds, which is key to the paper's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "input space",
      "ambient noise"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "geometry-aware noise",
      "resolved_canonical": "Geometry-Aware Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "manifold",
      "resolved_canonical": "Manifold",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Brownian motion noise",
      "resolved_canonical": "Brownian Motion Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "tangent space",
      "resolved_canonical": "Tangent Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Staying on the Manifold: Geometry-Aware Noise Injection

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20201.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20201](https://arxiv.org/abs/2509.20201)

## 🔗 유사한 논문
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (86.5% similar)
- [[2025-09-22/Manifold Dimension Estimation_ An Empirical Study_20250922|Manifold Dimension Estimation: An Empirical Study]] (83.7% similar)
- [[2025-09-25/Generative Model Inversion Through the Lens of the Manifold Hypothesis_20250925|Generative Model Inversion Through the Lens of the Manifold Hypothesis]] (81.2% similar)
- [[2025-09-17/A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations: Unifying Stochastic Mirror Descent, Learning and LLM Training]] (80.9% similar)
- [[2025-09-23/GeoSplat_ A Deep Dive into Geometry-Constrained Gaussian Splatting_20250923|GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Manifold|Manifold]], [[keywords/Tangent Space|Tangent Space]]
**⚡ Unique Technical**: [[keywords/Geometry-Aware Noise|Geometry-Aware Noise]], [[keywords/Brownian Motion Noise|Brownian Motion Noise]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20201v1 Announce Type: new 
Abstract: It has been shown that perturbing the input during training implicitly regularises the gradient of the learnt function, leading to smoother models and enhancing generalisation. However, previous research mostly considered the addition of ambient noise in the input space, without considering the underlying structure of the data. In this work, we propose several methods of adding geometry-aware input noise that accounts for the lower dimensional manifold the input space inhabits. We start by projecting ambient Gaussian noise onto the tangent space of the manifold. In a second step, the noise sample is mapped on the manifold via the associated geodesic curve. We also consider Brownian motion noise, which moves in random steps along the manifold. We show that geometry-aware noise leads to improved generalization and robustness to hyperparameter selection on highly curved manifolds, while performing at least as well as training without noise on simpler manifolds. Our proposed framework extends to learned data manifolds.

## 📝 요약

이 연구는 입력 데이터에 기하학적으로 인식된 노이즈를 추가하여 모델의 일반화 성능을 향상시키는 방법을 제안합니다. 기존 연구는 주로 입력 공간에 주변 노이즈를 추가하는 데 초점을 맞췄지만, 본 연구는 데이터의 저차원 매니폴드 구조를 고려한 노이즈 추가 방법을 개발했습니다. 구체적으로, 매니폴드의 접공간에 주변 가우시안 노이즈를 투영하고, 지오데식 곡선을 통해 매니폴드에 매핑하는 방법을 사용합니다. 또한, 매니폴드를 따라 무작위로 이동하는 브라운 운동 노이즈도 고려했습니다. 실험 결과, 기하학적으로 인식된 노이즈는 복잡한 매니폴드에서 일반화와 하이퍼파라미터 선택의 견고성을 개선하며, 단순한 매니폴드에서는 노이즈 없이 훈련한 경우와 유사한 성능을 보였습니다. 이 프레임워크는 학습된 데이터 매니폴드에도 확장 가능합니다.

## 🎯 주요 포인트

- 1. 입력 데이터에 대한 기하학적 구조를 고려한 노이즈 추가 방법을 제안합니다.
- 2. 매니폴드의 접공간에 주변 가우시안 노이즈를 투영하는 방법을 사용합니다.
- 3. 브라운 운동 노이즈를 통해 매니폴드를 따라 무작위로 이동하는 방법을 고려합니다.
- 4. 기하학적으로 인식된 노이즈는 일반화 및 하이퍼파라미터 선택에 대한 강건성을 향상시킵니다.
- 5. 제안된 프레임워크는 학습된 데이터 매니폴드로 확장 가능합니다.


---

*Generated on 2025-09-25 16:46:05*