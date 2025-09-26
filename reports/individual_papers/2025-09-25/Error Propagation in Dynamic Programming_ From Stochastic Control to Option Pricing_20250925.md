---
keywords:
  - Stochastic Optimal Control
  - Dynamic Programming
  - Reproducing Kernel Hilbert Spaces
  - Monte Carlo Methods
  - American Options
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20239
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:02:46.337838",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Optimal Control",
    "Dynamic Programming",
    "Reproducing Kernel Hilbert Spaces",
    "Monte Carlo Methods",
    "American Options"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Optimal Control": 0.75,
    "Dynamic Programming": 0.8,
    "Reproducing Kernel Hilbert Spaces": 0.78,
    "Monte Carlo Methods": 0.77,
    "American Options": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "stochastic optimal control",
        "canonical": "Stochastic Optimal Control",
        "aliases": [
          "SOC"
        ],
        "category": "unique_technical",
        "rationale": "Key concept in dynamic programming with specific applications in finance and control theory.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "dynamic programming",
        "canonical": "Dynamic Programming",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Fundamental technique in algorithm design and optimization, relevant across multiple domains.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "reproducing kernel Hilbert spaces",
        "canonical": "Reproducing Kernel Hilbert Spaces",
        "aliases": [
          "RKHS"
        ],
        "category": "specific_connectable",
        "rationale": "Mathematical framework used for regression and approximation in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Monte Carlo sampling",
        "canonical": "Monte Carlo Methods",
        "aliases": [
          "Monte Carlo"
        ],
        "category": "specific_connectable",
        "rationale": "Widely used technique for numerical integration and simulation in stochastic processes.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "American options",
        "canonical": "American Options",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Financial derivatives requiring specific pricing strategies, linking finance and stochastic control.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "error propagation",
      "value function"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "stochastic optimal control",
      "resolved_canonical": "Stochastic Optimal Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "dynamic programming",
      "resolved_canonical": "Dynamic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "reproducing kernel Hilbert spaces",
      "resolved_canonical": "Reproducing Kernel Hilbert Spaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Monte Carlo sampling",
      "resolved_canonical": "Monte Carlo Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "American options",
      "resolved_canonical": "American Options",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Error Propagation in Dynamic Programming: From Stochastic Control to Option Pricing

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20239.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20239](https://arxiv.org/abs/2509.20239)

## 🔗 유사한 논문
- [[2025-09-25/Pure Exploration via Frank-Wolfe Self-Play_20250925|Pure Exploration via Frank-Wolfe Self-Play]] (79.4% similar)
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (78.9% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (78.9% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (78.8% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dynamic Programming|Dynamic Programming]]
**🔗 Specific Connectable**: [[keywords/Reproducing Kernel Hilbert Spaces|Reproducing Kernel Hilbert Spaces]], [[keywords/Monte Carlo Methods|Monte Carlo Methods]], [[keywords/American Options|American Options]]
**⚡ Unique Technical**: [[keywords/Stochastic Optimal Control|Stochastic Optimal Control]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20239v1 Announce Type: cross 
Abstract: This paper investigates theoretical and methodological foundations for stochastic optimal control (SOC) in discrete time. We start formulating the control problem in a general dynamic programming framework, introducing the mathematical structure needed for a detailed convergence analysis. The associate value function is estimated through a sequence of approximations combining nonparametric regression methods and Monte Carlo subsampling. The regression step is performed within reproducing kernel Hilbert spaces (RKHSs), exploiting the classical KRR algorithm, while Monte Carlo sampling methods are introduced to estimate the continuation value. To assess the accuracy of our value function estimator, we propose a natural error decomposition and rigorously control the resulting error terms at each time step. We then analyze how this error propagates backward in time-from maturity to the initial stage-a relatively underexplored aspect of the SOC literature. Finally, we illustrate how our analysis naturally applies to a key financial application: the pricing of American options.

## 📝 요약

이 논문은 이산 시간에서 확률적 최적 제어(SOC)의 이론적 및 방법론적 기초를 탐구합니다. 일반적인 동적 프로그래밍 프레임워크에서 제어 문제를 공식화하고, 수렴 분석에 필요한 수학적 구조를 도입합니다. 비모수 회귀 방법과 몬테카를로 서브샘플링을 결합하여 가치 함수를 추정하며, 재생 커널 힐베르트 공간(RKHS)에서 KRR 알고리즘을 활용합니다. 또한, 가치 함수 추정의 정확성을 평가하기 위해 자연스러운 오류 분해를 제안하고, 각 시간 단계에서 오류 항을 엄격히 제어합니다. 이 오류가 시간이 거꾸로 진행되면서 어떻게 전파되는지를 분석하고, 이를 통해 미국 옵션 가격 결정이라는 금융 분야의 주요 응용에 적용 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. 이 논문은 이산 시간에서 확률적 최적 제어(SOC)의 이론적 및 방법론적 기초를 조사합니다.
- 2. 일반적인 동적 프로그래밍 프레임워크에서 제어 문제를 공식화하고, 수렴 분석을 위한 수학적 구조를 도입합니다.
- 3. 비모수 회귀 방법과 몬테카를로 서브샘플링을 결합하여 가치 함수를 추정합니다.
- 4. 재생 커널 힐베르트 공간(RKHS) 내에서 회귀 단계를 수행하고, 몬테카를로 샘플링 방법을 사용하여 연속 가치를 추정합니다.
- 5. 제안된 방법론은 미국 옵션의 가격 결정과 같은 금융 응용에 적용됩니다.


---

*Generated on 2025-09-25 17:02:46*