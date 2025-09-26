---
keywords:
  - Hamiltonian Dynamics
  - Kernel Methods
  - Data-Driven Simulations
  - Henon-Heiles System
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17154
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:20:00.539738",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hamiltonian Dynamics",
    "Kernel Methods",
    "Data-Driven Simulations",
    "Henon-Heiles System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hamiltonian Dynamics": 0.78,
    "Kernel Methods": 0.7,
    "Data-Driven Simulations": 0.75,
    "Henon-Heiles System": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hamiltonian dynamics",
        "canonical": "Hamiltonian Dynamics",
        "aliases": [
          "Hamiltonian systems"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, linking to studies on physical systems and conservation laws.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "kernel-based methods",
        "canonical": "Kernel Methods",
        "aliases": [
          "kernel methods"
        ],
        "category": "broad_technical",
        "rationale": "Connects to a wide range of machine learning techniques used for data-driven modeling.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.7
      },
      {
        "surface": "data-driven simulations",
        "canonical": "Data-Driven Simulations",
        "aliases": [
          "data-driven modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Links to broader themes in computational modeling and simulation techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Henon-Heiles system",
        "canonical": "Henon-Heiles System",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific example of a Hamiltonian system, useful for linking to studies on chaotic dynamics.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hamiltonian dynamics",
      "resolved_canonical": "Hamiltonian Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "kernel-based methods",
      "resolved_canonical": "Kernel Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "data-driven simulations",
      "resolved_canonical": "Data-Driven Simulations",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Henon-Heiles system",
      "resolved_canonical": "Henon-Heiles System",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Data-efficient Kernel Methods for Learning Hamiltonian Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17154.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17154](https://arxiv.org/abs/2509.17154)

## 🔗 유사한 논문
- [[2025-09-22/Time-adaptive SympNets for separable Hamiltonian systems_20250922|Time-adaptive SympNets for separable Hamiltonian systems]] (82.0% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (81.6% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (80.1% similar)
- [[2025-09-17/Floating-Body Hydrodynamic Neural Networks_20250917|Floating-Body Hydrodynamic Neural Networks]] (79.8% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Kernel Methods|Kernel Methods]]
**🔗 Specific Connectable**: [[keywords/Data-Driven Simulations|Data-Driven Simulations]]
**⚡ Unique Technical**: [[keywords/Hamiltonian Dynamics|Hamiltonian Dynamics]], [[keywords/Henon-Heiles System|Henon-Heiles System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17154v1 Announce Type: cross 
Abstract: Hamiltonian dynamics describe a wide range of physical systems. As such, data-driven simulations of Hamiltonian systems are important for many scientific and engineering problems. In this work, we propose kernel-based methods for identifying and forecasting Hamiltonian systems directly from data. We present two approaches: a two-step method that reconstructs trajectories before learning the Hamiltonian, and a one-step method that jointly infers both. Across several benchmark systems, including mass-spring dynamics, a nonlinear pendulum, and the Henon-Heiles system, we demonstrate that our framework achieves accurate, data-efficient predictions and outperforms two-step kernel-based baselines, particularly in scarce-data regimes, while preserving the conservation properties of Hamiltonian dynamics. Moreover, our methodology provides theoretical a priori error estimates, ensuring reliability of the learned models. We also provide a more general, problem-agnostic numerical framework that goes beyond Hamiltonian systems and can be used for data-driven learning of arbitrary dynamical systems.

## 📝 요약

이 논문은 데이터 기반으로 해밀토니안 시스템을 식별하고 예측하기 위한 커널 기반 방법을 제안합니다. 두 가지 접근법을 소개하는데, 하나는 궤적을 재구성한 후 해밀토니안을 학습하는 2단계 방법이고, 다른 하나는 이를 동시에 추론하는 1단계 방법입니다. 질량-스프링 동역학, 비선형 진자, Henon-Heiles 시스템 등 여러 벤치마크 시스템에서 제안된 프레임워크가 정확하고 데이터 효율적인 예측을 제공하며, 특히 데이터가 부족한 상황에서 기존 2단계 커널 기반 방법보다 우수한 성능을 보였습니다. 또한, 해밀토니안 동역학의 보존 특성을 유지하고, 학습된 모델의 신뢰성을 보장하는 이론적 사전 오류 추정치를 제공합니다. 이 방법론은 해밀토니안 시스템을 넘어 임의의 동역학 시스템 학습에도 적용 가능한 일반적인 수치적 프레임워크를 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 데이터 기반 시뮬레이션을 통해 해밀토니안 시스템을 식별하고 예측하는 커널 기반 방법을 제안합니다.
- 2. 두 가지 접근법을 제시하며, 하나는 궤적을 재구성한 후 해밀토니안을 학습하는 2단계 방법이고, 다른 하나는 둘을 동시에 추론하는 1단계 방법입니다.
- 3. 제안된 프레임워크는 질량-스프링 동역학, 비선형 진자, Henon-Heiles 시스템 등 여러 벤치마크 시스템에서 정확하고 데이터 효율적인 예측을 달성합니다.
- 4. 희소한 데이터 환경에서 2단계 커널 기반 기준을 능가하며, 해밀토니안 동역학의 보존 특성을 유지합니다.
- 5. 해밀토니안 시스템을 넘어 임의의 동적 시스템에 대한 데이터 기반 학습에 사용할 수 있는 문제에 구애받지 않는 일반적인 수치 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 02:20:00*