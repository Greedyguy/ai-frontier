---
keywords:
  - Convex Regression
  - Subgradient
  - Queueing Theory
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19788
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:58:17.783542",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convex Regression",
    "Subgradient",
    "Queueing Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Convex Regression": 0.75,
    "Subgradient": 0.78,
    "Queueing Theory": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convex Regression",
        "canonical": "Convex Regression",
        "aliases": [
          "Convex Function Estimation"
        ],
        "category": "unique_technical",
        "rationale": "Convex regression is a specific statistical method that is central to the paper's contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Subgradient",
        "canonical": "Subgradient",
        "aliases": [
          "Subgradient Method"
        ],
        "category": "unique_technical",
        "rationale": "The subgradient is a key mathematical concept used in the proposed estimator, linking it to optimization techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Single-Server Queue",
        "canonical": "Queueing Theory",
        "aliases": [
          "Queueing Model",
          "Single-Server Model"
        ],
        "category": "specific_connectable",
        "rationale": "Queueing theory is relevant for applications of the estimator, providing a bridge to operational research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Penalty",
      "Estimator",
      "Sum of Squared Errors"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convex Regression",
      "resolved_canonical": "Convex Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Subgradient",
      "resolved_canonical": "Subgradient",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Single-Server Queue",
      "resolved_canonical": "Queueing Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Convex Regression with a Penalty

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19788.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19788](https://arxiv.org/abs/2509.19788)

## 🔗 유사한 논문
- [[2025-09-24/Pareto-optimal Tradeoffs Between Communication and Computation with Flexible Gradient Tracking_20250924|Pareto-optimal Tradeoffs Between Communication and Computation with Flexible Gradient Tracking]] (82.1% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (81.6% similar)
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (81.2% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (81.1% similar)
- [[2025-09-23/Conformal Prediction with Upper and Lower Bound Models_20250923|Conformal Prediction with Upper and Lower Bound Models]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Queueing Theory|Queueing Theory]]
**⚡ Unique Technical**: [[keywords/Convex Regression|Convex Regression]], [[keywords/Subgradient|Subgradient]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19788v1 Announce Type: cross 
Abstract: A common way to estimate an unknown convex regression function $f_0: \Omega \subset \mathbb{R}^d \rightarrow \mathbb{R}$ from a set of $n$ noisy observations is to fit a convex function that minimizes the sum of squared errors. However, this estimator is known for its tendency to overfit near the boundary of $\Omega$, posing significant challenges in real-world applications. In this paper, we introduce a new estimator of $f_0$ that avoids this overfitting by minimizing a penalty on the subgradient while enforcing an upper bound $s_n$ on the sum of squared errors. The key advantage of this method is that $s_n$ can be directly estimated from the data. We establish the uniform almost sure consistency of the proposed estimator and its subgradient over $\Omega$ as $n \rightarrow \infty$ and derive convergence rates. The effectiveness of our estimator is illustrated through its application to estimating waiting times in a single-server queue.

## 📝 요약

이 논문은 경계 근처에서 과적합 문제가 있는 기존의 볼록 회귀 함수 추정 방법을 개선하기 위해 새로운 추정 방법을 제안합니다. 제안된 방법은 제곱 오차 합에 상한을 두고, 서브그래디언트에 패널티를 부과하여 과적합을 방지합니다. 이 상한은 데이터로부터 직접 추정할 수 있는 장점이 있습니다. 제안된 추정기의 균일 거의 확실한 일치성과 수렴 속도를 증명하였으며, 단일 서버 대기열의 대기 시간 추정에 적용하여 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 기존의 볼록 회귀 함수 추정 방법은 경계 근처에서 과적합 문제가 발생할 수 있다.
- 2. 새로운 추정 방법은 서브그래디언트에 대한 패널티를 최소화하고, 오차 제곱합에 상한을 두어 과적합을 방지한다.
- 3. 제안된 추정 방법은 데이터로부터 직접 상한을 추정할 수 있는 장점이 있다.
- 4. 제안된 추정기의 일관성과 수렴 속도를 이론적으로 증명하였다.
- 5. 단일 서버 대기열의 대기 시간 추정에 적용하여 추정기의 효과성을 입증하였다.


---

*Generated on 2025-09-25 16:58:17*