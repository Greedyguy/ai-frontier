---
keywords:
  - Linear Quadratic Regulator
  - Adaptive Dynamic Programming
  - Lyapunov Method
  - Markov Decision Process
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16746
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:15:09.130525",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Linear Quadratic Regulator",
    "Adaptive Dynamic Programming",
    "Lyapunov Method",
    "Markov Decision Process"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Linear Quadratic Regulator": 0.85,
    "Adaptive Dynamic Programming": 0.82,
    "Lyapunov Method": 0.78,
    "Markov Decision Process": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "linear quadratic regulator",
        "canonical": "Linear Quadratic Regulator",
        "aliases": [
          "LQR"
        ],
        "category": "specific_connectable",
        "rationale": "LQR is a fundamental concept in control theory, providing strong links to related adaptive control and optimization techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "adaptive dynamic programming",
        "canonical": "Adaptive Dynamic Programming",
        "aliases": [
          "ADP"
        ],
        "category": "specific_connectable",
        "rationale": "ADP is a key method in reinforcement learning, connecting to broader machine learning frameworks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Lyapunov-based analytical methodology",
        "canonical": "Lyapunov Method",
        "aliases": [
          "Lyapunov Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Lyapunov methods are crucial for stability analysis in control systems, linking to theoretical and practical applications.",
        "novelty_score": 0.58,
        "connectivity_score": 0.8,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Markov decision process",
        "canonical": "Markov Decision Process",
        "aliases": [
          "MDP"
        ],
        "category": "broad_technical",
        "rationale": "MDPs are foundational in decision-making models, connecting to various stochastic and dynamic programming approaches.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "offline designs",
      "controlled environment",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "linear quadratic regulator",
      "resolved_canonical": "Linear Quadratic Regulator",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "adaptive dynamic programming",
      "resolved_canonical": "Adaptive Dynamic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Lyapunov-based analytical methodology",
      "resolved_canonical": "Lyapunov Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.8,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Markov decision process",
      "resolved_canonical": "Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# On the System Theoretic Offline Learning of Continuous-Time LQR with Exogenous Disturbances

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16746.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16746](https://arxiv.org/abs/2509.16746)

## 🔗 유사한 논문
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (81.8% similar)
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (81.0% similar)
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty: A Sample-Based Approach]] (80.1% similar)
- [[2025-09-19/Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (79.7% similar)
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Markov Decision Process|Markov Decision Process]]
**🔗 Specific Connectable**: [[keywords/Linear Quadratic Regulator|Linear Quadratic Regulator]], [[keywords/Adaptive Dynamic Programming|Adaptive Dynamic Programming]], [[keywords/Lyapunov Method|Lyapunov Method]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16746v1 Announce Type: cross 
Abstract: We analyze offline designs of linear quadratic regulator (LQR) strategies with uncertain disturbances. First, we consider the scenario where the exogenous variable can be estimated in a controlled environment, and subsequently, consider a more practical and challenging scenario where it is unknown in a stochastic setting. Our approach builds on the fundamental learning-based framework of adaptive dynamic programming (ADP), combined with a Lyapunov-based analytical methodology to design the algorithms and derive sample-based approximations motivated from the Markov decision process (MDP)-based approaches. For the scenario involving non-measurable disturbances, we further establish stability and convergence guarantees for the learned control gains under sample-based approximations. The overall methodology emphasizes simplicity while providing rigorous guarantees. Finally, numerical experiments focus on the intricacies and validations for the design of offline continuous-time LQR with exogenous disturbances.

## 📝 요약

이 논문은 불확실한 외란이 있는 선형 이차 조절기(LQR) 전략의 오프라인 설계를 분석합니다. 먼저, 외생 변수를 제어된 환경에서 추정할 수 있는 경우를 다루고, 이후 확률적 환경에서 알 수 없는 경우를 다룹니다. 적응형 동적 프로그래밍(ADP)과 Lyapunov 기반 분석 방법론을 결합하여 알고리즘을 설계하고, 마르코프 결정 과정(MDP) 기반 접근법에서 영감을 받은 샘플 기반 근사치를 도출합니다. 측정 불가능한 외란이 있는 경우, 학습된 제어 이득의 안정성과 수렴성을 보장합니다. 이 방법론은 단순성을 강조하면서도 엄격한 보장을 제공합니다. 마지막으로, 수치 실험을 통해 외생 외란이 있는 오프라인 연속 시간 LQR 설계의 복잡성과 검증을 중점적으로 다룹니다.

## 🎯 주요 포인트

- 1. 불확실한 외란이 있는 선형 이차 조절기(LQR) 전략의 오프라인 설계를 분석합니다.
- 2. 제어된 환경에서 외생 변수를 추정할 수 있는 시나리오와 확률적 설정에서 외생 변수가 알려지지 않은 시나리오를 고려합니다.
- 3. 적응형 동적 프로그래밍(ADP)과 Lyapunov 기반 분석 방법론을 결합하여 알고리즘을 설계하고, 마르코프 결정 과정(MDP) 기반 접근 방식에서 영감을 얻은 샘플 기반 근사치를 도출합니다.
- 4. 비측정 가능한 외란이 있는 시나리오에 대해 학습된 제어 이득의 안정성과 수렴성을 보장합니다.
- 5. 오프라인 연속 시간 LQR 설계의 복잡성과 검증을 위한 수치 실험을 수행합니다.


---

*Generated on 2025-09-24 02:15:09*