---
keywords:
  - Multi-Objective Reinforcement Learning
  - Policy Gradient
  - Biased Estimator
  - Global Optimization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2105.14125
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:35:35.681146",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Objective Reinforcement Learning",
    "Policy Gradient",
    "Biased Estimator",
    "Global Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Objective Reinforcement Learning": 0.82,
    "Policy Gradient": 0.79,
    "Biased Estimator": 0.77,
    "Global Optimization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Objective Reinforcement Learning",
        "canonical": "Multi-Objective Reinforcement Learning",
        "aliases": [
          "MORL"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper and connects to broader reinforcement learning topics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Policy Gradient Algorithm",
        "canonical": "Policy Gradient",
        "aliases": [
          "Policy Gradient Methods"
        ],
        "category": "specific_connectable",
        "rationale": "Policy gradient methods are a key technique in reinforcement learning, facilitating connections to related algorithms.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Biased Estimator",
        "canonical": "Biased Estimator",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The biased estimator is a unique contribution of the paper, offering a novel approach to gradient estimation.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Global Optima",
        "canonical": "Global Optimization",
        "aliases": [
          "Global Optimum"
        ],
        "category": "broad_technical",
        "rationale": "Global optimization is a fundamental concept in optimization problems, relevant across multiple domains.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "non-linear function",
      "discount factor",
      "sampling trajectories"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Objective Reinforcement Learning",
      "resolved_canonical": "Multi-Objective Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Policy Gradient Algorithm",
      "resolved_canonical": "Policy Gradient",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Biased Estimator",
      "resolved_canonical": "Biased Estimator",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Global Optima",
      "resolved_canonical": "Global Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2105.14125.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2105.14125](https://arxiv.org/abs/2105.14125)

## 🔗 유사한 논문
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (85.3% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (84.2% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (84.1% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (83.0% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Global Optimization|Global Optimization]]
**🔗 Specific Connectable**: [[keywords/Multi-Objective Reinforcement Learning|Multi-Objective Reinforcement Learning]], [[keywords/Policy Gradient|Policy Gradient]]
**⚡ Unique Technical**: [[keywords/Biased Estimator|Biased Estimator]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2105.14125v2 Announce Type: replace-cross 
Abstract: Many engineering problems have multiple objectives, and the overall aim is to optimize a non-linear function of these objectives. In this paper, we formulate the problem of maximizing a non-linear concave function of multiple long-term objectives. A policy-gradient based model-free algorithm is proposed for the problem. To compute an estimate of the gradient, a biased estimator is proposed. The proposed algorithm is shown to achieve convergence to within an $\epsilon$ of the global optima after sampling $\mathcal{O}(\frac{M^4\sigma^2}{(1-\gamma)^8\epsilon^4})$ trajectories where $\gamma$ is the discount factor and $M$ is the number of the agents, thus achieving the same dependence on $\epsilon$ as the policy gradient algorithm for the standard reinforcement learning.

## 📝 요약

이 논문은 여러 장기 목표의 비선형 오목 함수를 최대화하는 문제를 다룹니다. 이를 위해 정책 경사 기반의 모델 프리 알고리즘을 제안하며, 경사 추정을 위해 편향된 추정자를 사용합니다. 제안된 알고리즘은 샘플링을 통해 글로벌 최적점에 $\epsilon$ 이내로 수렴함을 보이며, 이는 표준 강화 학습의 정책 경사 알고리즘과 동일한 $\epsilon$ 의존성을 가집니다.

## 🎯 주요 포인트

- 1. 다중 장기 목표의 비선형 오목 함수 최대화를 문제로 공식화하였습니다.
- 2. 정책 경사 기반의 모델 프리 알고리즘을 제안하였습니다.
- 3. 경사 추정을 위해 편향된 추정기를 제안하였습니다.
- 4. 제안된 알고리즘은 $\mathcal{O}(\frac{M^4\sigma^2}{(1-\gamma)^8\epsilon^4})$ 경로를 샘플링하여 글로벌 최적점에 $\epsilon$ 이내로 수렴함을 보였습니다.
- 5. 표준 강화 학습의 정책 경사 알고리즘과 동일한 $\epsilon$ 의존성을 달성하였습니다.


---

*Generated on 2025-09-24 00:35:35*