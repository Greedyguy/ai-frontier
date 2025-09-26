---
keywords:
  - Deep Learning
  - Generalized Laplace Approximation
  - Posterior Tempering
  - Aleatoric Uncertainty
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2405.13535
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:32:22.624464",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Generalized Laplace Approximation",
    "Posterior Tempering",
    "Aleatoric Uncertainty"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.8,
    "Generalized Laplace Approximation": 0.78,
    "Posterior Tempering": 0.77,
    "Aleatoric Uncertainty": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "Bayesian DL"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader field of deep learning, which is central to the paper's focus.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Generalized Laplace Approximation",
        "canonical": "Generalized Laplace Approximation",
        "aliases": [
          "GLA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method that is central to the paper's contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Posterior Tempering",
        "canonical": "Posterior Tempering",
        "aliases": [
          "Tempered Posterior"
        ],
        "category": "specific_connectable",
        "rationale": "A specific technique discussed in the paper that enhances understanding of Bayesian adjustments.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Aleatoric Uncertainty",
        "canonical": "Aleatoric Uncertainty",
        "aliases": [
          "Data Uncertainty"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in understanding uncertainty reduction in Bayesian models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "model misspecification",
      "joint probability",
      "regularized loss"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Generalized Laplace Approximation",
      "resolved_canonical": "Generalized Laplace Approximation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Posterior Tempering",
      "resolved_canonical": "Posterior Tempering",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Aleatoric Uncertainty",
      "resolved_canonical": "Aleatoric Uncertainty",
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

# Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2405.13535.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2405.13535](https://arxiv.org/abs/2405.13535)

## 🔗 유사한 논문
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (83.6% similar)
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (83.2% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (82.3% similar)
- [[2025-09-23/Enhancing Performance and Calibration in Quantile Hyperparameter Optimization_20250923|Enhancing Performance and Calibration in Quantile Hyperparameter Optimization]] (82.2% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Posterior Tempering|Posterior Tempering]], [[keywords/Aleatoric Uncertainty|Aleatoric Uncertainty]]
**⚡ Unique Technical**: [[keywords/Generalized Laplace Approximation|Generalized Laplace Approximation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.13535v5 Announce Type: replace 
Abstract: In recent years, inconsistency in Bayesian deep learning has attracted significant attention. Tempered or generalized posterior distributions are frequently employed as direct and effective solutions. Nonetheless, the underlying mechanisms and the effectiveness of generalized posteriors remain active research topics. In this work, we interpret posterior tempering as a correction for model misspecification via adjustments to the joint probability, and as a recalibration of priors by reducing aleatoric uncertainty. We also introduce the generalized Laplace approximation, which requires only a simple modification to the Hessian calculation of the regularized loss and provides a flexible and scalable framework for high-quality posterior inference. We evaluate the proposed method on state-of-the-art neural networks and real-world datasets, demonstrating that the generalized Laplace approximation enhances predictive performance.

## 📝 요약

이 논문은 베이지안 딥러닝에서 발생하는 불일치 문제를 해결하기 위해 후행 분포의 조정을 통한 모델의 잘못된 명세를 수정하고, 우선순위를 재조정하여 불확실성을 줄이는 방법을 제안합니다. 특히, 일반화된 라플라스 근사를 도입하여 정규화된 손실의 헤시안 계산을 간단히 수정함으로써 고품질의 후행 추론을 위한 유연하고 확장 가능한 프레임워크를 제공합니다. 제안된 방법은 최신 신경망과 실제 데이터셋에서 예측 성능을 향상시키는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 베이지안 딥러닝의 불일치 문제를 해결하기 위해 템퍼링된 또는 일반화된 사후 분포가 자주 사용된다.
- 2. 본 연구에서는 모델의 잘못된 명세를 수정하고, 사전 확률을 재조정하는 방법으로 사후 템퍼링을 해석한다.
- 3. 일반화된 라플라스 근사를 도입하여 정규화된 손실의 헤시안 계산을 간단히 수정함으로써 고품질의 사후 추론을 위한 유연하고 확장 가능한 프레임워크를 제공한다.
- 4. 제안된 방법은 최신 신경망과 실제 데이터셋에서 예측 성능을 향상시킨다.


---

*Generated on 2025-09-24 02:32:22*