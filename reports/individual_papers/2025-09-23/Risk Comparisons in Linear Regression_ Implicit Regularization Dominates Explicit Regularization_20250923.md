---
keywords:
  - Gradient Descent
  - Ridge Regression
  - Stochastic Gradient Descent
  - Benign Overfitting
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17251
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:21:13.547838",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gradient Descent",
    "Ridge Regression",
    "Stochastic Gradient Descent",
    "Benign Overfitting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gradient Descent": 0.78,
    "Ridge Regression": 0.72,
    "Stochastic Gradient Descent": 0.75,
    "Benign Overfitting": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gradient Descent",
        "canonical": "Gradient Descent",
        "aliases": [
          "GD"
        ],
        "category": "broad_technical",
        "rationale": "Gradient Descent is a fundamental optimization algorithm widely used in machine learning, making it a strong link across various studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Ridge Regression",
        "canonical": "Ridge Regression",
        "aliases": [
          "Ridge"
        ],
        "category": "specific_connectable",
        "rationale": "Ridge Regression is a specific regularization technique that is crucial for understanding the paper's comparative analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Stochastic Gradient Descent",
        "canonical": "Stochastic Gradient Descent",
        "aliases": [
          "SGD"
        ],
        "category": "specific_connectable",
        "rationale": "Stochastic Gradient Descent is a key algorithm in the paper's analysis, providing a basis for comparison with Gradient Descent.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Benign Overfitting",
        "canonical": "Benign Overfitting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Benign Overfitting is a unique concept explored in the paper, highlighting specific conditions where GD can be suboptimal.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "minimax optimal",
      "well-specified linear regression problem"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gradient Descent",
      "resolved_canonical": "Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Ridge Regression",
      "resolved_canonical": "Ridge Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Stochastic Gradient Descent",
      "resolved_canonical": "Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Benign Overfitting",
      "resolved_canonical": "Benign Overfitting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Risk Comparisons in Linear Regression: Implicit Regularization Dominates Explicit Regularization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17251.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17251](https://arxiv.org/abs/2509.17251)

## 🔗 유사한 논문
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (82.0% similar)
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (79.7% similar)
- [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (79.3% similar)
- [[2025-09-22/Generalization and Optimization of SGD with Lookahead_20250922|Generalization and Optimization of SGD with Lookahead]] (79.0% similar)
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gradient Descent|Gradient Descent]]
**🔗 Specific Connectable**: [[keywords/Ridge Regression|Ridge Regression]], [[keywords/Stochastic Gradient Descent|Stochastic Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Benign Overfitting|Benign Overfitting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17251v1 Announce Type: cross 
Abstract: Existing theory suggests that for linear regression problems categorized by capacity and source conditions, gradient descent (GD) is always minimax optimal, while both ridge regression and online stochastic gradient descent (SGD) are polynomially suboptimal for certain categories of such problems. Moving beyond minimax theory, this work provides instance-wise comparisons of the finite-sample risks for these algorithms on any well-specified linear regression problem.
  Our analysis yields three key findings. First, GD dominates ridge regression: with comparable regularization, the excess risk of GD is always within a constant factor of ridge, but ridge can be polynomially worse even when tuned optimally. Second, GD is incomparable with SGD. While it is known that for certain problems GD can be polynomially better than SGD, the reverse is also true: we construct problems, inspired by benign overfitting theory, where optimally stopped GD is polynomially worse. Finally, GD dominates SGD for a significant subclass of problems -- those with fast and continuously decaying covariance spectra -- which includes all problems satisfying the standard capacity condition.

## 📝 요약

이 연구는 선형 회귀 문제에서 경사 하강법(GD), 릿지 회귀, 온라인 확률적 경사 하강법(SGD)의 유한 샘플 위험을 비교합니다. 주요 발견사항은 다음과 같습니다. 첫째, GD는 릿지 회귀보다 항상 우수하며, 릿지가 최적 조정되더라도 GD의 초과 위험이 일정한 범위 내에 있습니다. 둘째, GD와 SGD는 비교할 수 없으며, 특정 문제에서는 GD가 SGD보다 우수하거나 그 반대일 수 있습니다. 마지막으로, GD는 빠르게 감소하는 공분산 스펙트럼을 가진 문제에서 SGD보다 우수하며, 이는 표준 용량 조건을 만족하는 모든 문제를 포함합니다.

## 🎯 주요 포인트

- 1. 선형 회귀 문제에서 경사 하강법(GD)은 리지 회귀보다 항상 우수하며, 리지 회귀는 최적화되더라도 다항식적으로 더 나쁠 수 있다.
- 2. 경사 하강법(GD)과 온라인 확률적 경사 하강법(SGD)은 비교할 수 없으며, 특정 문제에서는 GD가 SGD보다 다항식적으로 우수할 수 있지만 그 반대도 가능하다.
- 3. 경사 하강법(GD)은 빠르고 지속적으로 감소하는 공분산 스펙트럼을 가진 문제들, 즉 표준 용량 조건을 만족하는 모든 문제에 대해 온라인 확률적 경사 하강법(SGD)을 지배한다.


---

*Generated on 2025-09-24 02:21:13*