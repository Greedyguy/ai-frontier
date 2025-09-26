---
keywords:
  - Deep Gaussian Process
  - Batch Bayesian Optimization
  - Materials Design
  - Upper-Confidence-Bound Acquisition
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.14408
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:45:54.182683",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Gaussian Process",
    "Batch Bayesian Optimization",
    "Materials Design",
    "Upper-Confidence-Bound Acquisition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Gaussian Process": 0.78,
    "Batch Bayesian Optimization": 0.82,
    "Materials Design": 0.7,
    "Upper-Confidence-Bound Acquisition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Gaussian Process",
        "canonical": "Deep Gaussian Process",
        "aliases": [
          "DGP"
        ],
        "category": "unique_technical",
        "rationale": "Deep Gaussian Processes are a novel approach to modeling complex hierarchical relationships, making them a unique technical concept in this context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Batch Bayesian Optimization",
        "canonical": "Batch Bayesian Optimization",
        "aliases": [
          "BBO"
        ],
        "category": "unique_technical",
        "rationale": "Batch Bayesian Optimization is a specific method that enhances connectivity by linking to optimization strategies in machine learning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Materials Design",
        "canonical": "Materials Design",
        "aliases": [
          "Materials Discovery"
        ],
        "category": "broad_technical",
        "rationale": "Materials Design is a broad technical area that connects to various research in materials science and engineering.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Upper-Confidence-Bound Acquisition",
        "canonical": "Upper-Confidence-Bound Acquisition",
        "aliases": [
          "UCB Acquisition"
        ],
        "category": "specific_connectable",
        "rationale": "This acquisition function is crucial for balancing exploration and exploitation in optimization, linking it to decision-making strategies.",
        "novelty_score": 0.62,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "optimization framework",
      "evaluation resources"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Gaussian Process",
      "resolved_canonical": "Deep Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Batch Bayesian Optimization",
      "resolved_canonical": "Batch Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Materials Design",
      "resolved_canonical": "Materials Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Upper-Confidence-Bound Acquisition",
      "resolved_canonical": "Upper-Confidence-Bound Acquisition",
      "decision": "linked",
      "scores": {
        "novelty": 0.62,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns

**Korean Title:** 복잡한 소재 설계 캠페인을 위한 비용 인식 배치 베이지안 최적화를 기반으로 한 심층 가우시안 프로세스

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14408.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.14408](https://arxiv.org/abs/2509.14408)

## 🔗 유사한 논문
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (83.6% similar)
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (80.4% similar)
- [[2025-09-22/Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems_20250922|Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems]] (80.3% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (79.9% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Materials Design|Materials Design]]
**🔗 Specific Connectable**: [[keywords/Upper-Confidence-Bound Acquisition|Upper-Confidence-Bound Acquisition]]
**⚡ Unique Technical**: [[keywords/Deep Gaussian Process|Deep Gaussian Process]], [[keywords/Batch Bayesian Optimization|Batch Bayesian Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14408v1 Announce Type: cross 
Abstract: The accelerating pace and expanding scope of materials discovery demand optimization frameworks that efficiently navigate vast, nonlinear design spaces while judiciously allocating limited evaluation resources. We present a cost-aware, batch Bayesian optimization scheme powered by deep Gaussian process (DGP) surrogates and a heterotopic querying strategy. Our DGP surrogate, formed by stacking GP layers, models complex hierarchical relationships among high-dimensional compositional features and captures correlations across multiple target properties, propagating uncertainty through successive layers. We integrate evaluation cost into an upper-confidence-bound acquisition extension, which, together with heterotopic querying, proposes small batches of candidates in parallel, balancing exploration of under-characterized regions with exploitation of high-mean, low-variance predictions across correlated properties. Applied to refractory high-entropy alloys for high-temperature applications, our framework converges to optimal formulations in fewer iterations with cost-aware queries than conventional GP-based BO, highlighting the value of deep, uncertainty-aware, cost-sensitive strategies in materials campaigns.

## 🔍 Abstract (한글 번역)

arXiv:2509.14408v1 발표 유형: 교차  
초록: 재료 발견의 가속화된 속도와 확장되는 범위는 방대한 비선형 설계 공간을 효율적으로 탐색하면서 제한된 평가 자원을 신중하게 할당하는 최적화 프레임워크를 요구합니다. 우리는 깊은 가우시안 프로세스(DGP) 대리모델과 이질적 쿼리 전략에 의해 구동되는 비용 인식 배치 베이지안 최적화 방식을 제시합니다. GP 계층을 쌓아 형성된 우리의 DGP 대리모델은 고차원 조성적 특징들 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 속성 간의 상관관계를 포착하며, 연속적인 계층을 통해 불확실성을 전파합니다. 우리는 평가 비용을 상한 신뢰 경계 획득 확장에 통합하여, 이질적 쿼리와 함께 상관된 속성 전반에서 고평균, 저분산 예측의 활용과 덜 특성화된 영역의 탐색을 균형 있게 수행하며, 병렬로 소규모 후보 배치를 제안합니다. 고온 응용을 위한 내화 고엔트로피 합금에 적용된 우리의 프레임워크는 전통적인 GP 기반 BO보다 비용 인식 쿼리를 통해 적은 반복으로 최적의 조성에 수렴하며, 재료 캠페인에서 깊고, 불확실성 인식, 비용 민감한 전략의 가치를 강조합니다.

## 📝 요약

이 논문은 재료 발견의 가속화된 속도와 확장된 범위에 대응하기 위해, 제한된 평가 자원을 효율적으로 활용하면서 비선형 설계 공간을 탐색하는 최적화 프레임워크를 제안합니다. 제안된 방법은 심층 가우시안 프로세스(DGP) 대리모델과 이질적 쿼리 전략을 활용한 비용 인식 배치 베이지안 최적화 기법입니다. DGP 대리모델은 GP 레이어를 쌓아 고차원 조성 특징 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 속성 간의 상관관계를 포착하여 불확실성을 전파합니다. 평가 비용을 상한 신뢰 경계 획득 확장에 통합하고, 이질적 쿼리와 함께 소규모 후보군을 병렬로 제안하여, 덜 특성화된 영역의 탐색과 상관된 속성 전반의 높은 평균, 낮은 분산 예측을 활용하는 균형을 맞춥니다. 고온 응용을 위한 내화 고엔트로피 합금에 적용한 결과, 제안된 프레임워크는 기존의 GP 기반 베이지안 최적화보다 적은 반복으로 최적의 조성에 수렴하여, 심층적이고 불확실성 인식 및 비용 민감 전략의 가치를 강조합니다.

## 🎯 주요 포인트

- 1. 본 연구는 재료 발견의 가속화된 속도와 확장된 범위를 다루기 위해 효율적인 최적화 프레임워크를 제안합니다.
- 2. 딥 가우시안 프로세스(DGP) 서로게이트와 이질적 쿼리 전략을 활용한 비용 인식 배치 베이지안 최적화 방식을 소개합니다.
- 3. DGP 서로게이트는 고차원 조성 특징 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 속성 간의 상관관계를 포착합니다.
- 4. 평가 비용을 고려한 상한 신뢰 경계 획득 확장을 통합하여, 이질적 쿼리와 함께 소규모 후보군을 병렬로 제안합니다.
- 5. 제안된 프레임워크는 고온 응용을 위한 내화 고엔트로피 합금에 적용되어, 기존 GP 기반 BO보다 적은 반복 횟수로 최적의 조성에 수렴합니다.


---

*Generated on 2025-09-23 10:45:54*