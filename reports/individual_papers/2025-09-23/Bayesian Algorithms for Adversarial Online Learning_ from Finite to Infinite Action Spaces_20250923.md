---
keywords:
  - Thompson Sampling
  - Bayesian Optimization
  - Gaussian Process
  - Adversarial Online Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.14790
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:39:28.882619",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Thompson Sampling",
    "Bayesian Optimization",
    "Gaussian Process",
    "Adversarial Online Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Thompson Sampling": 0.78,
    "Bayesian Optimization": 0.8,
    "Gaussian Process": 0.77,
    "Adversarial Online Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Thompson sampling",
        "canonical": "Thompson Sampling",
        "aliases": [
          "Thompson sampling method"
        ],
        "category": "specific_connectable",
        "rationale": "Thompson Sampling is a well-known method in online learning and connects to Bayesian decision processes.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bayesian optimization",
        "canonical": "Bayesian Optimization",
        "aliases": [
          "Bayesian optimization technique"
        ],
        "category": "specific_connectable",
        "rationale": "Bayesian Optimization is a key concept in machine learning for optimizing complex functions and connects well with Gaussian processes.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gaussian process prior",
        "canonical": "Gaussian Process",
        "aliases": [
          "GP prior"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian Processes are fundamental in Bayesian statistics and optimization, providing a probabilistic approach to modeling.",
        "novelty_score": 0.4,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "adversarial online learning",
        "canonical": "Adversarial Online Learning",
        "aliases": [
          "adversarial learning"
        ],
        "category": "unique_technical",
        "rationale": "Adversarial Online Learning is a specialized area focusing on learning in the presence of adversarial conditions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "finite-expert setting",
      "excess regret",
      "unit cube"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Thompson sampling",
      "resolved_canonical": "Thompson Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bayesian optimization",
      "resolved_canonical": "Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gaussian process prior",
      "resolved_canonical": "Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "adversarial online learning",
      "resolved_canonical": "Adversarial Online Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Bayesian Algorithms for Adversarial Online Learning: from Finite to Infinite Action Spaces

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.14790.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.14790](https://arxiv.org/abs/2502.14790)

## 🔗 유사한 논문
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (82.0% similar)
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (80.9% similar)
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty: A Sample-Based Approach]] (80.6% similar)
- [[2025-09-19/Reinforcement Learning Agent for a 2D Shooter Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (80.5% similar)
- [[2025-09-19/Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Thompson Sampling|Thompson Sampling]], [[keywords/Bayesian Optimization|Bayesian Optimization]], [[keywords/Gaussian Process|Gaussian Process]]
**⚡ Unique Technical**: [[keywords/Adversarial Online Learning|Adversarial Online Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.14790v5 Announce Type: replace 
Abstract: We develop a form Thompson sampling for online learning under full feedback - also known as prediction with expert advice - where the learner's prior is defined over the space of an adversary's future actions, rather than the space of experts. We show regret decomposes into regret the learner expected a priori, plus a prior-robustness-type term we call excess regret. In the classical finite-expert setting, this recovers optimal rates. As an initial step towards practical online learning in settings with a potentially-uncountably-infinite number of experts, we show that Thompson sampling over the $d$-dimensional unit cube, using a certain Gaussian process prior widely-used in the Bayesian optimization literature, has a $\mathcal{O}\Big(\beta\sqrt{Td\log(1+\sqrt{d}\frac{\lambda}{\beta})}\Big)$ rate against a $\beta$-bounded $\lambda$-Lipschitz adversary.

## 📝 요약

이 논문은 온라인 학습에서 전체 피드백을 활용하는 톰슨 샘플링 방법을 개발했습니다. 기존의 전문가 조언 기반 예측과 달리, 학습자의 사전 지식은 전문가가 아닌 적의 미래 행동에 기반합니다. 이 방법은 후회가 사전 기대 후회와 초과 후회로 분해됨을 보여주며, 고전적인 유한 전문가 설정에서 최적의 속도를 회복합니다. 또한, 무한대의 전문가가 존재할 수 있는 환경에서 실용적인 온라인 학습을 위한 초기 단계로, 베이지안 최적화 문헌에서 널리 사용되는 특정 가우시안 프로세스 사전을 활용하여 $d$-차원 단위 큐브에서 톰슨 샘플링이 $\beta$-제한 $\lambda$-립시츠 적에 대해 $\mathcal{O}\Big(\beta\sqrt{Td\log(1+\sqrt{d}\frac{\lambda}{\beta})}\Big)$ 속도를 달성함을 보였습니다.

## 🎯 주요 포인트

- 1. 본 연구는 전문가 조언을 통한 예측 문제에서 적의 미래 행동 공간에 대한 사전 확률을 설정하여 온라인 학습을 위한 톰슨 샘플링 기법을 개발합니다.
- 2. 후회는 사전에 예상된 후회와 초과 후회라는 사전 견고성 유형의 항으로 분해될 수 있음을 보입니다.
- 3. 고전적인 유한 전문가 설정에서 최적의 비율을 회복할 수 있음을 증명합니다.
- 4. 잠재적으로 셀 수 없이 많은 전문가가 있는 환경에서 실용적인 온라인 학습을 위한 초기 단계로, $d$-차원 단위 큐브에서의 톰슨 샘플링이 특정 가우시안 프로세스 사전을 사용하여 $\beta$-제한 $\lambda$-리프시츠 적에 대해 특정한 비율을 가짐을 보입니다.


---

*Generated on 2025-09-24 02:39:28*