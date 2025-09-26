---
keywords:
  - Safe Dynamics Learning
  - Probabilistic Models
  - Online Learning
  - Non-Episodic Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16650
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:12:18.629871",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Safe Dynamics Learning",
    "Probabilistic Models",
    "Online Learning",
    "Non-Episodic Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Safe Dynamics Learning": 0.78,
    "Probabilistic Models": 0.7,
    "Online Learning": 0.77,
    "Non-Episodic Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "safe dynamics learning",
        "canonical": "Safe Dynamics Learning",
        "aliases": [
          "safe dynamics exploration"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and represents a novel method for ensuring safety in unknown dynamics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "probabilistic models",
        "canonical": "Probabilistic Models",
        "aliases": [
          "stochastic models"
        ],
        "category": "broad_technical",
        "rationale": "Probabilistic models are a foundational concept in the paper, linking to broader machine learning techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "online learning",
        "canonical": "Online Learning",
        "aliases": [
          "continuous learning"
        ],
        "category": "specific_connectable",
        "rationale": "Online learning is a key feature of the proposed method, connecting to ongoing research in adaptive systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "non-episodic setting",
        "canonical": "Non-Episodic Learning",
        "aliases": [
          "continuous setting"
        ],
        "category": "unique_technical",
        "rationale": "The non-episodic setting is a unique aspect of the approach, differentiating it from typical RL methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "optimality",
      "safety",
      "model uncertainty"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "safe dynamics learning",
      "resolved_canonical": "Safe Dynamics Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "probabilistic models",
      "resolved_canonical": "Probabilistic Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "online learning",
      "resolved_canonical": "Online Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "non-episodic setting",
      "resolved_canonical": "Non-Episodic Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Safe Guaranteed Dynamics Exploration with Probabilistic Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16650.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16650](https://arxiv.org/abs/2509.16650)

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (85.4% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (84.4% similar)
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (83.5% similar)
- [[2025-09-23/Automating Steering for Safe Multimodal Large Language Models_20250923|Automating Steering for Safe Multimodal Large Language Models]] (82.4% similar)
- [[2025-09-23/ORN-CBF_ Learning Observation-conditioned Residual Neural Control Barrier Functions via Hypernetworks_20250923|ORN-CBF: Learning Observation-conditioned Residual Neural Control Barrier Functions via Hypernetworks]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Probabilistic Models|Probabilistic Models]]
**🔗 Specific Connectable**: [[keywords/Online Learning|Online Learning]]
**⚡ Unique Technical**: [[keywords/Safe Dynamics Learning|Safe Dynamics Learning]], [[keywords/Non-Episodic Learning|Non-Episodic Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16650v1 Announce Type: cross 
Abstract: Ensuring both optimality and safety is critical for the real-world deployment of agents, but becomes particularly challenging when the system dynamics are unknown. To address this problem, we introduce a notion of maximum safe dynamics learning via sufficient exploration in the space of safe policies. We propose a $\textit{pessimistically}$ safe framework that $\textit{optimistically}$ explores informative states and, despite not reaching them due to model uncertainty, ensures continuous online learning of dynamics. The framework achieves first-of-its-kind results: learning the dynamics model sufficiently $-$ up to an arbitrary small tolerance (subject to noise) $-$ in a finite time, while ensuring provably safe operation throughout with high probability and without requiring resets. Building on this, we propose an algorithm to maximize rewards while learning the dynamics $\textit{only to the extent needed}$ to achieve close-to-optimal performance. Unlike typical reinforcement learning (RL) methods, our approach operates online in a non-episodic setting and ensures safety throughout the learning process. We demonstrate the effectiveness of our approach in challenging domains such as autonomous car racing and drone navigation under aerodynamic effects $-$ scenarios where safety is critical and accurate modeling is difficult.

## 📝 요약

이 논문은 시스템 동작이 알려지지 않은 상황에서 에이전트의 최적성과 안전성을 보장하기 위한 새로운 접근법을 제안합니다. 저자들은 안전한 정책 공간에서 충분한 탐색을 통해 최대 안전 동적 학습 개념을 도입하고, 비관적으로 안전한 프레임워크가 낙관적으로 정보 상태를 탐색하도록 합니다. 이 프레임워크는 모델 불확실성에도 불구하고 연속적인 온라인 동적 학습을 보장하며, 안전한 작동을 높은 확률로 보장하면서도 리셋이 필요하지 않습니다. 또한, 동적 모델을 필요한 만큼만 학습하여 거의 최적의 성능을 달성하는 알고리즘을 제안합니다. 이 접근법은 비에피소드 환경에서 온라인으로 작동하며, 학습 과정 내내 안전성을 보장합니다. 자율주행 자동차 경주와 드론 내비게이션과 같은 안전이 중요한 도메인에서 그 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 시스템 동작이 알려지지 않은 상황에서 최적성과 안전성을 동시에 보장하기 위한 새로운 안전 동적 학습 개념을 제안합니다.
- 2. 제안된 프레임워크는 안전한 정책 공간에서 충분한 탐색을 통해 최대한의 안전한 동적 학습을 수행합니다.
- 3. 온라인 학습을 통해 모델 불확실성에도 불구하고 지속적인 동적 학습을 보장하며, 안전한 작동을 높은 확률로 보장합니다.
- 4. 제안된 알고리즘은 동적 모델을 필요한 범위 내에서만 학습하여 거의 최적의 성능을 달성하도록 설계되었습니다.
- 5. 자율주행 자동차 경주 및 드론 내비게이션과 같은 도전적인 도메인에서 제안된 접근 방식의 효과를 입증하였습니다.


---

*Generated on 2025-09-24 02:12:18*