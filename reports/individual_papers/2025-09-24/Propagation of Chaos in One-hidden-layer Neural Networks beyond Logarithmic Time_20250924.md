<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:32:54.328344",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Mean-Field Dynamics",
    "Single-Index Model",
    "Projected Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Mean-Field Dynamics": 0.78,
    "Single-Index Model": 0.7,
    "Projected Gradient Descent": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the study and provide a broad technical context for linking.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mean-Field Dynamics",
        "canonical": "Mean-Field Dynamics",
        "aliases": [
          "Mean Field Theory"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the approximation gap and dynamics discussed in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Single-Index Model",
        "canonical": "Single-Index Model",
        "aliases": [
          "SIM"
        ],
        "category": "unique_technical",
        "rationale": "The single-index model is a specific problem context for applying the study's results.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      },
      {
        "surface": "Projected Gradient Descent",
        "canonical": "Projected Gradient Descent",
        "aliases": [
          "PGD"
        ],
        "category": "specific_connectable",
        "rationale": "This optimization method is key to the training process described in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "dynamics",
      "approximation gap"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Mean-Field Dynamics",
      "resolved_canonical": "Mean-Field Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Single-Index Model",
      "resolved_canonical": "Single-Index Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Projected Gradient Descent",
      "resolved_canonical": "Projected Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Propagation of Chaos in One-hidden-layer Neural Networks beyond Logarithmic Time

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.13110.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2504.13110](https://arxiv.org/abs/2504.13110)

## 🔗 유사한 논문
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.1% similar)
- [[2025-09-23/A geometric framework for momentum-based optimizers for low-rank training_20250923|A geometric framework for momentum-based optimizers for low-rank training]] (80.4% similar)
- [[2025-09-23/Efficient Neural SDE Training using Wiener-Space Cubature_20250923|Efficient Neural SDE Training using Wiener-Space Cubature]] (80.3% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (80.2% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Projected Gradient Descent|Projected Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Mean-Field Dynamics|Mean-Field Dynamics]], [[keywords/Single-Index Model|Single-Index Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.13110v2 Announce Type: replace-cross 
Abstract: We study the approximation gap between the dynamics of a polynomial-width neural network and its infinite-width counterpart, both trained using projected gradient descent in the mean-field scaling regime. We demonstrate how to tightly bound this approximation gap through a differential equation governed by the mean-field dynamics. A key factor influencing the growth of this ODE is the local Hessian of each particle, defined as the derivative of the particle's velocity in the mean-field dynamics with respect to its position. We apply our results to the canonical feature learning problem of estimating a well-specified single-index model; we permit the information exponent to be arbitrarily large, leading to convergence times that grow polynomially in the ambient dimension $d$. We show that, due to a certain ``self-concordance'' property in these problems -- where the local Hessian of a particle is bounded by a constant times the particle's velocity -- polynomially many neurons are sufficient to closely approximate the mean-field dynamics throughout training.

## 📝 요약

이 논문은 다항식 너비의 신경망과 무한 너비 신경망 간의 동적 근사 차이를 연구합니다. 평균장 스케일링 체제에서 투영 경사 하강법을 사용하여 훈련된 두 신경망의 근사 차이를 미분 방정식을 통해 엄밀히 제한할 수 있음을 보여줍니다. 이 방정식의 성장은 각 입자의 위치에 대한 평균장 동역학의 속도의 미분인 국소 헤시안에 의해 영향을 받습니다. 이 결과를 단일 지수 모델 추정 문제에 적용하여 정보 지수가 임의로 커질 수 있도록 하여, 주변 차원 $d$에 대해 다항식적으로 증가하는 수렴 시간을 얻습니다. 또한, 입자의 국소 헤시안이 입자의 속도에 비례하여 일정한 상수로 제한되는 "자기 일치" 특성 덕분에, 다항식적으로 많은 뉴런이 훈련 내내 평균장 동역학을 가깝게 근사할 수 있음을 증명합니다.

## 🎯 주요 포인트

- 1. 유한 차원의 신경망과 무한 차원의 신경망 간의 근사 차이를 평균장 스케일링 체제에서 분석합니다.
- 2. 평균장 동역학에 의해 지배되는 미분 방정식을 통해 근사 차이를 엄밀히 제한할 수 있음을 보여줍니다.
- 3. 입자의 위치에 대한 평균장 동역학에서의 속도의 도함수로 정의된 입자의 국소 헤시안이 ODE의 성장을 결정하는 주요 요인입니다.
- 4. 단일 지수 모델을 추정하는 문제에 결과를 적용하여, 정보 지수가 임의로 클 수 있음을 허용하고 수렴 시간이 차원 $d$에 대해 다항적으로 증가함을 보입니다.
- 5. 입자의 국소 헤시안이 입자의 속도에 일정한 배수로 제한되는 "자기 일치" 속성 덕분에, 다항적으로 많은 뉴런이 훈련 내내 평균장 동역학을 근사하는 데 충분합니다.


---

*Generated on 2025-09-24 15:32:54*