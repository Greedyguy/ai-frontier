---
keywords:
  - Neural Ordinary Differential Equations
  - Control Disturbance
  - Flat Minima
  - Projected Gradient Descent
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18034
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:01:26.602605",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Ordinary Differential Equations",
    "Control Disturbance",
    "Flat Minima",
    "Projected Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Ordinary Differential Equations": 0.78,
    "Control Disturbance": 0.77,
    "Flat Minima": 0.75,
    "Projected Gradient Descent": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural ODEs",
        "canonical": "Neural Ordinary Differential Equations",
        "aliases": [
          "Neural ODE",
          "NODE"
        ],
        "category": "unique_technical",
        "rationale": "Neural ODEs are a specific type of neural network model that extends the concept of ordinary differential equations to machine learning, providing a unique approach to modeling dynamic systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "control disturbance",
        "canonical": "Control Disturbance",
        "aliases": [
          "parameter disturbance",
          "control perturbation"
        ],
        "category": "unique_technical",
        "rationale": "Control disturbance is a key concept in the paper, focusing on the model's resilience to parameter changes, which is crucial for robustness in dynamic systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "flat minima",
        "canonical": "Flat Minima",
        "aliases": [
          "flat minimum",
          "flat minima concept"
        ],
        "category": "specific_connectable",
        "rationale": "The concept of flat minima is important for understanding the optimization landscape in neural networks, contributing to the robustness and generalization of models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "projected gradient descent",
        "canonical": "Projected Gradient Descent",
        "aliases": [
          "PGD",
          "projected GD"
        ],
        "category": "specific_connectable",
        "rationale": "Projected gradient descent is a specific optimization technique used in the paper, relevant for its role in handling constraints in parameter space.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.76,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "iterative training algorithm",
      "parameter space",
      "simulations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural ODEs",
      "resolved_canonical": "Neural Ordinary Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "control disturbance",
      "resolved_canonical": "Control Disturbance",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "flat minima",
      "resolved_canonical": "Flat Minima",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "projected gradient descent",
      "resolved_canonical": "Projected Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.76,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Control Disturbance Rejection in Neural ODEs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18034.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18034](https://arxiv.org/abs/2509.18034)

## 🔗 유사한 논문
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (81.9% similar)
- [[2025-09-22/Geometric Integration for Neural Control Variates_20250922|Geometric Integration for Neural Control Variates]] (81.4% similar)
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (81.1% similar)
- [[2025-09-23/Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm_20250923|Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm]] (80.8% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Flat Minima|Flat Minima]], [[keywords/Projected Gradient Descent|Projected Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Neural Ordinary Differential Equations|Neural Ordinary Differential Equations]], [[keywords/Control Disturbance|Control Disturbance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18034v1 Announce Type: new 
Abstract: In this paper, we propose an iterative training algorithm for Neural ODEs that provides models resilient to control (parameter) disturbances. The method builds on our earlier work Tuning without Forgetting-and similarly introduces training points sequentially, and updates the parameters on new data within the space of parameters that do not decrease performance on the previously learned training points-with the key difference that, inspired by the concept of flat minima, we solve a minimax problem for a non-convex non-concave functional over an infinite-dimensional control space. We develop a projected gradient descent algorithm on the space of parameters that admits the structure of an infinite-dimensional Banach subspace. We show through simulations that this formulation enables the model to effectively learn new data points and gain robustness against control disturbance.

## 📝 요약

이 논문에서는 제어(매개변수) 교란에 강인한 Neural ODE 모델을 위한 반복적 학습 알고리즘을 제안합니다. 이전 연구인 'Tuning without Forgetting'을 기반으로 하여, 새로운 데이터로 매개변수를 업데이트하면서 이전 학습 데이터의 성능을 유지하는 방법을 사용합니다. 주요 차별점은 평탄한 최소값 개념을 활용하여, 무한 차원의 제어 공간에서 비볼록 비오목 함수에 대한 미니맥스 문제를 해결하는 것입니다. 우리는 무한 차원의 바나흐 부분공간 구조를 갖는 매개변수 공간에서 투영 경사 하강 알고리즘을 개발했습니다. 시뮬레이션을 통해 이 방법이 새로운 데이터 학습과 제어 교란에 대한 강인성을 효과적으로 향상시킴을 보였습니다.

## 🎯 주요 포인트

- 1. 본 논문에서는 제어(파라미터) 교란에 강인한 Neural ODE 모델을 위한 반복적 학습 알고리즘을 제안합니다.
- 2. 이전 연구인 Tuning without Forgetting을 기반으로 하여, 새로운 데이터에서 성능 저하 없이 파라미터를 업데이트하는 방법을 사용합니다.
- 3. 평탄한 최소값 개념에 영감을 받아, 무한 차원의 제어 공간에서 비볼록 비오목 함수에 대한 미니맥스 문제를 해결합니다.
- 4. 무한 차원의 바나흐 부분공간 구조를 갖는 파라미터 공간에서 투영된 경사 하강 알고리즘을 개발하였습니다.
- 5. 시뮬레이션을 통해 제안된 방법이 새로운 데이터 포인트를 효과적으로 학습하고 제어 교란에 대한 강인성을 획득함을 보였습니다.


---

*Generated on 2025-09-24 02:01:26*