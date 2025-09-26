---
keywords:
  - Operator Inference
  - State Constraints
  - Reduced-Order Model
  - Char Combustion
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.03672
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:01:08.386712",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Operator Inference",
    "State Constraints",
    "Reduced-Order Model",
    "Char Combustion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Operator Inference": 0.8,
    "State Constraints": 0.78,
    "Reduced-Order Model": 0.72,
    "Char Combustion": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Operator Inference",
        "canonical": "Operator Inference",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Operator Inference is central to the paper's methodology and is a unique approach within scientific machine learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "state constraints",
        "canonical": "State Constraints",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "State constraints are crucial for enhancing the stability and accuracy of the reduced-order model discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "reduced-order model",
        "canonical": "Reduced-Order Model",
        "aliases": [
          "ROM"
        ],
        "category": "broad_technical",
        "rationale": "Reduced-order models are a fundamental concept in the paper, linking to broader topics in computational modeling.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "char combustion",
        "canonical": "Char Combustion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Char combustion is the specific application used to demonstrate the methodology, providing a concrete example of the approach.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Numerical simulations",
      "key performance indicator",
      "computationally efficient"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Operator Inference",
      "resolved_canonical": "Operator Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "state constraints",
      "resolved_canonical": "State Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reduced-order model",
      "resolved_canonical": "Reduced-Order Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "char combustion",
      "resolved_canonical": "Char Combustion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Physically consistent predictive reduced-order modeling by enhancing Operator Inference with state constraints

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.03672.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.03672](https://arxiv.org/abs/2502.03672)

## 🔗 유사한 논문
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (83.5% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (82.3% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (81.3% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (81.2% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reduced-Order Model|Reduced-Order Model]]
**⚡ Unique Technical**: [[keywords/Operator Inference|Operator Inference]], [[keywords/State Constraints|State Constraints]], [[keywords/Char Combustion|Char Combustion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.03672v2 Announce Type: replace-cross 
Abstract: Numerical simulations of complex multiphysics systems, such as char combustion considered herein, yield numerous state variables that inherently exhibit physical constraints. This paper presents a new approach to augment Operator Inference -- a methodology within scientific machine learning that enables learning from data a low-dimensional representation of a high-dimensional system governed by nonlinear partial differential equations -- by embedding such state constraints in the reduced-order model predictions. In the model learning process, we propose a new way to choose regularization hyperparameters based on a key performance indicator. Since embedding state constraints improves the stability of the Operator Inference reduced-order model, we compare the proposed state constraints-embedded Operator Inference with the standard Operator Inference and other stability-enhancing approaches. For an application to char combustion, we demonstrate that the proposed approach yields state predictions superior to the other methods regarding stability and accuracy. It extrapolates over 200\% past the training regime while being computationally efficient and physically consistent.

## 📝 요약

이 논문은 비선형 편미분 방정식으로 지배되는 고차원 시스템의 저차원 표현을 데이터로부터 학습하는 과학적 기계 학습 방법론인 Operator Inference를 개선하는 새로운 접근법을 제시합니다. 특히, 상태 제약 조건을 포함하여 모델 예측의 안정성을 높이는 방법을 제안합니다. 규제 하이퍼파라미터 선택을 위한 새로운 방법을 도입하고, 이를 통해 안정성이 향상된 Operator Inference를 기존 방법들과 비교합니다. 숯 연소에 대한 응용에서 제안된 방법은 기존 방법들보다 안정성과 정확성 면에서 우수한 상태 예측을 제공하며, 훈련 범위를 200% 이상 초과하여도 물리적으로 일관된 결과를 효율적으로 산출합니다.

## 🎯 주요 포인트

- 1. 본 논문은 비선형 편미분 방정식으로 지배되는 고차원 시스템의 저차원 표현을 학습하는 Operator Inference 방법론에 상태 제약을 내재화하여 개선하는 새로운 접근법을 제시합니다.
- 2. 모델 학습 과정에서 주요 성능 지표를 기반으로 정규화 하이퍼파라미터를 선택하는 새로운 방법을 제안합니다.
- 3. 제안된 방법은 상태 제약을 내재화하여 Operator Inference 저차원 모델의 안정성을 향상시키며, 기존의 표준 Operator Inference 및 다른 안정성 향상 접근법과 비교됩니다.
- 4. 제안된 방법은 차 연소에 대한 응용에서 안정성과 정확성 면에서 다른 방법보다 우수한 상태 예측을 제공하며, 훈련 범위를 200% 이상 초과하여 외삽할 수 있습니다.
- 5. 제안된 접근법은 계산 효율성이 높고 물리적으로 일관성이 있습니다.


---

*Generated on 2025-09-24 03:01:08*