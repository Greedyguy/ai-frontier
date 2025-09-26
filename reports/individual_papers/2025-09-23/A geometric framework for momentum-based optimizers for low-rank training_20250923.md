---
keywords:
  - Low-Rank Training
  - Momentum-Based Optimization
  - Dynamical Low-Rank Approximation
  - Optimization Landscape
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.17475
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:46:39.996438",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Training",
    "Momentum-Based Optimization",
    "Dynamical Low-Rank Approximation",
    "Optimization Landscape"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Training": 0.78,
    "Momentum-Based Optimization": 0.8,
    "Dynamical Low-Rank Approximation": 0.75,
    "Optimization Landscape": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "low-rank pre-training",
        "canonical": "Low-Rank Training",
        "aliases": [
          "low-rank parameterization",
          "low-rank fine-tuning"
        ],
        "category": "unique_technical",
        "rationale": "Low-rank training is a specialized optimization technique that can be linked to discussions on efficient neural network training.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "momentum-based optimizers",
        "canonical": "Momentum-Based Optimization",
        "aliases": [
          "momentum methods",
          "heavy ball momentum"
        ],
        "category": "specific_connectable",
        "rationale": "Momentum-based optimization is a key concept in training neural networks and can connect to broader discussions on optimization techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "dynamical low-rank approximation",
        "canonical": "Dynamical Low-Rank Approximation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel approach that combines geometry and optimization, offering a unique perspective on training strategies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "optimization landscape",
        "canonical": "Optimization Landscape",
        "aliases": [
          "optimization geometry"
        ],
        "category": "broad_technical",
        "rationale": "Understanding the optimization landscape is crucial for designing effective training strategies in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "training methods",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "low-rank pre-training",
      "resolved_canonical": "Low-Rank Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "momentum-based optimizers",
      "resolved_canonical": "Momentum-Based Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "dynamical low-rank approximation",
      "resolved_canonical": "Dynamical Low-Rank Approximation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "optimization landscape",
      "resolved_canonical": "Optimization Landscape",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# A geometric framework for momentum-based optimizers for low-rank training

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.17475.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.17475](https://arxiv.org/abs/2506.17475)

## 🔗 유사한 논문
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (84.0% similar)
- [[2025-09-22/Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size_20250922|Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size]] (83.6% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (83.3% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (82.9% similar)
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Optimization Landscape|Optimization Landscape]]
**🔗 Specific Connectable**: [[keywords/Momentum-Based Optimization|Momentum-Based Optimization]]
**⚡ Unique Technical**: [[keywords/Low-Rank Training|Low-Rank Training]], [[keywords/Dynamical Low-Rank Approximation|Dynamical Low-Rank Approximation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.17475v2 Announce Type: replace 
Abstract: Low-rank pre-training and fine-tuning have recently emerged as promising techniques for reducing the computational and storage costs of large neural networks. Training low-rank parameterizations typically relies on conventional optimizers such as heavy ball momentum methods or Adam. In this work, we identify and analyze potential difficulties that these training methods encounter when used to train low-rank parameterizations of weights. In particular, we show that classical momentum methods can struggle to converge to a local optimum due to the geometry of the underlying optimization landscape. To address this, we introduce novel training strategies derived from dynamical low-rank approximation, which explicitly account for the underlying geometric structure. Our approach leverages and combines tools from dynamical low-rank approximation and momentum-based optimization to design optimizers that respect the intrinsic geometry of the parameter space. We validate our methods through numerical experiments, demonstrating faster convergence, and stronger validation metrics at given parameter budgets.

## 📝 요약

이 논문은 대형 신경망의 계산 및 저장 비용을 줄이기 위한 저랭크 사전 훈련 및 미세 조정 기법을 다룹니다. 기존의 모멘텀 방법이나 Adam과 같은 최적화 기법이 저랭크 매개변수화 훈련 시 겪는 문제점을 분석하고, 이러한 기법들이 최적화 지형의 기하학적 구조로 인해 지역 최적점에 수렴하는 데 어려움을 겪을 수 있음을 보여줍니다. 이를 해결하기 위해, 저자들은 기하학적 구조를 고려한 새로운 훈련 전략을 제안합니다. 이 전략은 동적 저랭크 근사와 모멘텀 기반 최적화를 결합하여 매개변수 공간의 본질적 기하학을 존중하는 최적화 기법을 설계합니다. 수치 실험을 통해 제안된 방법이 더 빠른 수렴 속도와 향상된 검증 지표를 달성함을 입증합니다.

## 🎯 주요 포인트

- 1. 저차원 사전 훈련과 미세 조정은 대형 신경망의 계산 및 저장 비용을 줄이는 유망한 기술로 부상하고 있다.
- 2. 기존의 모멘텀 방법은 최적화 지형의 기하학적 구조 때문에 지역 최적점에 수렴하는 데 어려움을 겪을 수 있다.
- 3. 본 연구에서는 기하학적 구조를 명시적으로 고려한 새로운 훈련 전략을 도입하였다.
- 4. 제안된 방법은 동적 저차원 근사와 모멘텀 기반 최적화를 결합하여 매개변수 공간의 내재된 기하학을 존중하는 최적화 도구를 설계한다.
- 5. 수치 실험을 통해 제안된 방법이 더 빠른 수렴 속도와 강력한 검증 지표를 달성함을 입증하였다.


---

*Generated on 2025-09-24 02:46:39*