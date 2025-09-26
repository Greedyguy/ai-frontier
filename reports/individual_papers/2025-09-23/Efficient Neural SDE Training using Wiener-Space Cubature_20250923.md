---
keywords:
  - Neural Stochastic Differential Equation
  - Wiener Space Cubature
  - Monte Carlo Simulation
  - Deterministic Ordinary Differential Equation Solutions
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.12395
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:39:12.776412",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Stochastic Differential Equation",
    "Wiener Space Cubature",
    "Monte Carlo Simulation",
    "Deterministic Ordinary Differential Equation Solutions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Stochastic Differential Equation": 0.78,
    "Wiener Space Cubature": 0.79,
    "Monte Carlo Simulation": 0.72,
    "Deterministic Ordinary Differential Equation Solutions": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural SDE",
        "canonical": "Neural Stochastic Differential Equation",
        "aliases": [
          "Neural SDE",
          "Stochastic Neural DE"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specific type of differential equation with neural network parameters, crucial for linking with stochastic processes and neural network research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Wiener Space Cubature",
        "canonical": "Wiener Space Cubature",
        "aliases": [
          "Cubature on Wiener Space"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's novel contribution, linking stochastic calculus with numerical methods.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Monte-Carlo Simulation",
        "canonical": "Monte Carlo Simulation",
        "aliases": [
          "Monte-Carlo",
          "MC Simulation"
        ],
        "category": "broad_technical",
        "rationale": "A widely used method in computational mathematics, relevant for linking with stochastic and simulation-based research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.55,
        "link_intent_score": 0.72
      },
      {
        "surface": "Deterministic ODE Solutions",
        "canonical": "Deterministic Ordinary Differential Equation Solutions",
        "aliases": [
          "Deterministic ODE",
          "ODE Solutions"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding the paper's approach to bypassing stochastic simulations, linking with numerical analysis.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "procedure",
      "objective functional",
      "training technique"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural SDE",
      "resolved_canonical": "Neural Stochastic Differential Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Wiener Space Cubature",
      "resolved_canonical": "Wiener Space Cubature",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Monte-Carlo Simulation",
      "resolved_canonical": "Monte Carlo Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.55,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Deterministic ODE Solutions",
      "resolved_canonical": "Deterministic Ordinary Differential Equation Solutions",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Efficient Neural SDE Training using Wiener-Space Cubature

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.12395.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.12395](https://arxiv.org/abs/2502.12395)

## 🔗 유사한 논문
- [[2025-09-23/Efficient Sliced Wasserstein Distance Computation via Adaptive Bayesian Optimization_20250923|Efficient Sliced Wasserstein Distance Computation via Adaptive Bayesian Optimization]] (83.9% similar)
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (83.4% similar)
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (82.2% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (82.1% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Monte Carlo Simulation|Monte Carlo Simulation]]
**🔗 Specific Connectable**: [[keywords/Deterministic Ordinary Differential Equation Solutions|Deterministic Ordinary Differential Equation Solutions]]
**⚡ Unique Technical**: [[keywords/Neural Stochastic Differential Equation|Neural Stochastic Differential Equation]], [[keywords/Wiener Space Cubature|Wiener Space Cubature]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.12395v3 Announce Type: replace 
Abstract: A neural stochastic differential equation (SDE) is an SDE with drift and diffusion terms parametrized by neural networks. The training procedure for neural SDEs consists of optimizing the SDE vector field (neural network) parameters to minimize the expected value of an objective functional on infinite-dimensional path-space. Existing training techniques focus on methods to efficiently compute path-wise gradients of the objective functional with respect to these parameters, then pair this with Monte-Carlo simulation to estimate the gradient expectation. In this work we introduce a novel training technique which bypasses and improves upon this Monte-Carlo simulation; we extend results in the theory of Wiener space cubature to approximate the expected objective functional value by a weighted sum of functional evaluations of deterministic ODE solutions. Our main mathematical contribution enabling this approximation is an extension of cubature bounds to the setting of Lipschitz-nonlinear functionals acting on path-space. Our resulting constructive algorithm allows for more computationally efficient training along several lines. First, it circumvents Brownian motion simulation and enables the use of efficient parallel ODE solvers, thus decreasing the complexity of path-functional evaluation. Furthermore, and more surprisingly, we show that the number of paths required to achieve a given (expected loss functional oracle value) approximation can be reduced in this deterministic cubature regime. Specifically, we show that under reasonable regularity assumptions we can observe a O(1/n) convergence rate, where n is the number of path evaluations; in contrast with the standard O(1/sqrt(n)) rate of naive Monte-Carlo or the O(log(n)^d /n) rate of quasi-Monte-Carlo.

## 📝 요약

이 논문은 신경망으로 매개변수화된 확률 미분 방정식(SDE)의 새로운 학습 기법을 제안합니다. 기존 방법은 경로별 기울기를 계산하고 몬테카를로 시뮬레이션을 사용하여 기울기 기대값을 추정합니다. 그러나 본 연구는 비결정적 경로 시뮬레이션을 우회하여, 결정론적 ODE 해의 함수 평가를 가중 합으로 사용해 기대값을 근사하는 방법을 제시합니다. 이는 경로 공간에서 작용하는 리프시츠 비선형 함수에 대한 큐베이처 경계 확장을 통해 가능해졌습니다. 이 알고리즘은 브라운 운동 시뮬레이션을 피하고 병렬 ODE 해석기를 활용해 계산 효율성을 높이며, 경로 수를 줄여 O(1/n)의 수렴 속도를 달성합니다. 이는 기존의 몬테카를로 방법보다 효율적입니다.

## 🎯 주요 포인트

- 1. 신경망으로 매개변수화된 드리프트와 확산 항을 가진 신경 확률 미분 방정식(SDE)의 훈련 절차를 제안합니다.
- 2. 기존의 몬테카를로 시뮬레이션을 개선하여 경로 공간에서의 Lipschitz-비선형 함수에 대한 큐베이처 경계를 확장합니다.
- 3. 결정론적 ODE 솔루션의 함수 평가의 가중합을 통해 기대 목적 함수 값을 근사하는 새로운 훈련 기법을 도입합니다.
- 4. 제안된 알고리즘은 브라운 운동 시뮬레이션을 우회하고 효율적인 병렬 ODE 솔버를 사용하여 경로 함수 평가의 복잡성을 줄입니다.
- 5. 제안된 방법은 경로 평가 수를 줄여 O(1/n) 수렴 속도를 달성할 수 있으며, 이는 기존의 몬테카를로 방법보다 효율적입니다.


---

*Generated on 2025-09-24 02:39:12*