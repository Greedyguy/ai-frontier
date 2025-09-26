---
keywords:
  - Sharpness-aware Minimization
  - m-Sharpness
  - Stochastic Gradient Noise
  - Stochastic Differential Equation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18001
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:16:20.422453",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sharpness-aware Minimization",
    "m-Sharpness",
    "Stochastic Gradient Noise",
    "Stochastic Differential Equation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sharpness-aware Minimization": 0.78,
    "m-Sharpness": 0.77,
    "Stochastic Gradient Noise": 0.79,
    "Stochastic Differential Equation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sharpness-aware minimization",
        "canonical": "Sharpness-aware Minimization",
        "aliases": [
          "SAM"
        ],
        "category": "unique_technical",
        "rationale": "SAM is a unique optimization technique that directly relates to model generalization, making it a valuable link for understanding advanced learning methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "m-sharpness",
        "canonical": "m-Sharpness",
        "aliases": [
          "micro-batch sharpness"
        ],
        "category": "unique_technical",
        "rationale": "m-Sharpness is a specific phenomenon within SAM that offers insights into optimization dynamics, providing a unique angle for linking related research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Stochastic Gradient Noise",
        "canonical": "Stochastic Gradient Noise",
        "aliases": [
          "SGN"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding the structure of SGN is crucial for linking to works on optimization and noise in machine learning models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Stochastic Differential Equation",
        "canonical": "Stochastic Differential Equation",
        "aliases": [
          "SDE"
        ],
        "category": "broad_technical",
        "rationale": "SDEs are foundational in modeling stochastic processes, providing a broad technical link to mathematical frameworks in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sharpness-aware minimization",
      "resolved_canonical": "Sharpness-aware Minimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "m-sharpness",
      "resolved_canonical": "m-Sharpness",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Stochastic Gradient Noise",
      "resolved_canonical": "Stochastic Gradient Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Stochastic Differential Equation",
      "resolved_canonical": "Stochastic Differential Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Unveiling m-Sharpness Through the Structure of Stochastic Gradient Noise

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18001.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18001](https://arxiv.org/abs/2509.18001)

## 🔗 유사한 논문
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (79.6% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (79.6% similar)
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (79.4% similar)
- [[2025-09-22/Generalization and Optimization of SGD with Lookahead_20250922|Generalization and Optimization of SGD with Lookahead]] (79.2% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Stochastic Differential Equation|Stochastic Differential Equation]]
**🔗 Specific Connectable**: [[keywords/Stochastic Gradient Noise|Stochastic Gradient Noise]]
**⚡ Unique Technical**: [[keywords/Sharpness-aware Minimization|Sharpness-aware Minimization]], [[keywords/m-Sharpness|m-Sharpness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18001v1 Announce Type: cross 
Abstract: Sharpness-aware minimization (SAM) has emerged as a highly effective technique for improving model generalization, but its underlying principles are not fully understood. We investigated the phenomenon known as m-sharpness, where the performance of SAM improves monotonically as the micro-batch size for computing perturbations decreases. Leveraging an extended Stochastic Differential Equation (SDE) framework, combined with an analysis of the structure of stochastic gradient noise (SGN), we precisely characterize the dynamics of various SAM variants. Our findings reveal that the stochastic noise introduced during SAM perturbations inherently induces a variance-based sharpness regularization effect. Motivated by our theoretical insights, we introduce Reweighted SAM, which employs sharpness-weighted sampling to mimic the generalization benefits of m-SAM while remaining parallelizable. Comprehensive experiments validate the effectiveness of our theoretical analysis and proposed method.

## 📝 요약

이 논문은 모델 일반화를 향상시키는 효과적인 기법인 Sharpness-aware minimization (SAM)의 원리를 탐구합니다. 연구에서는 m-sharpness 현상을 조사하며, 이는 SAM의 성능이 미세 배치 크기가 줄어들수록 개선되는 현상입니다. 확장된 확률 미분 방정식(SDE) 프레임워크와 확률적 그래디언트 노이즈(SGN) 구조 분석을 통해 다양한 SAM 변형의 동태를 정확히 규명했습니다. 연구 결과, SAM의 섭동 과정에서 도입된 확률적 노이즈가 본질적으로 분산 기반의 sharpness 정규화 효과를 유도함을 밝혔습니다. 이러한 이론적 통찰을 바탕으로, m-SAM의 일반화 이점을 모방하면서 병렬화가 가능한 Reweighted SAM을 제안했습니다. 실험을 통해 이론적 분석과 제안된 방법의 효과성을 검증했습니다.

## 🎯 주요 포인트

- 1. Sharpness-aware minimization (SAM)은 모델 일반화 성능을 향상시키는 효과적인 기법이지만, 그 기저 원리는 완전히 이해되지 않았다.
- 2. m-sharpness 현상에서는 미세 배치 크기가 감소할수록 SAM의 성능이 단조롭게 향상된다.
- 3. 확장된 확률 미분 방정식(SDE) 프레임워크와 확률적 그래디언트 노이즈(SGN) 구조 분석을 통해 다양한 SAM 변종의 동역학을 정확히 특성화했다.
- 4. SAM의 섭동 과정에서 도입된 확률적 노이즈는 본질적으로 분산 기반의 샤프니스 정규화 효과를 유도한다.
- 5. 이론적 통찰을 바탕으로, m-SAM의 일반화 이점을 모방하면서 병렬화가 가능한 Reweighted SAM을 제안했다.


---

*Generated on 2025-09-24 00:16:20*