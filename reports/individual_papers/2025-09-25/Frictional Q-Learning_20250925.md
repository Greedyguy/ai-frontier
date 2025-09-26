---
keywords:
  - Frictional Q-learning
  - Extrapolation Error
  - Batch-Constrained Reinforcement Learning
  - Continuous Control
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19771
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:48:24.937635",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Frictional Q-learning",
    "Extrapolation Error",
    "Batch-Constrained Reinforcement Learning",
    "Continuous Control"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Frictional Q-learning": 0.78,
    "Extrapolation Error": 0.82,
    "Batch-Constrained Reinforcement Learning": 0.8,
    "Continuous Control": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Frictional Q-learning",
        "canonical": "Frictional Q-learning",
        "aliases": [
          "Frictional QL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach in reinforcement learning by drawing an analogy with static friction, which is not covered by existing canonicals.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "extrapolation error",
        "canonical": "Extrapolation Error",
        "aliases": [
          "Extrapolation Errors"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in off-policy reinforcement learning that connects to various learning stability discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "batch-constrained reinforcement learning",
        "canonical": "Batch-Constrained Reinforcement Learning",
        "aliases": [
          "Batch-Constrained RL"
        ],
        "category": "specific_connectable",
        "rationale": "A specific technique in reinforcement learning that connects to discussions on policy constraints and learning efficiency.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "continuous control",
        "canonical": "Continuous Control",
        "aliases": [
          "Continuous Action Control"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental area in reinforcement learning that connects to various control and robotics applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "static friction",
      "unsupported actions",
      "replay buffer"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Frictional Q-learning",
      "resolved_canonical": "Frictional Q-learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "extrapolation error",
      "resolved_canonical": "Extrapolation Error",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "batch-constrained reinforcement learning",
      "resolved_canonical": "Batch-Constrained Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "continuous control",
      "resolved_canonical": "Continuous Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Frictional Q-Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19771.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19771](https://arxiv.org/abs/2509.19771)

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.8% similar)
- [[2025-09-23/Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality_20250923|Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality]] (83.5% similar)
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (83.4% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (83.2% similar)
- [[2025-09-23/Robust Reinforcement Learning with Dynamic Distortion Risk Measures_20250923|Robust Reinforcement Learning with Dynamic Distortion Risk Measures]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Continuous Control|Continuous Control]]
**🔗 Specific Connectable**: [[keywords/Extrapolation Error|Extrapolation Error]], [[keywords/Batch-Constrained Reinforcement Learning|Batch-Constrained Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Frictional Q-learning|Frictional Q-learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19771v1 Announce Type: cross 
Abstract: We draw an analogy between static friction in classical mechanics and extrapolation error in off-policy RL, and use it to formulate a constraint that prevents the policy from drifting toward unsupported actions. In this study, we present Frictional Q-learning, a deep reinforcement learning algorithm for continuous control, which extends batch-constrained reinforcement learning. Our algorithm constrains the agent's action space to encourage behavior similar to that in the replay buffer, while maintaining a distance from the manifold of the orthonormal action space. The constraint preserves the simplicity of batch-constrained, and provides an intuitive physical interpretation of extrapolation error. Empirically, we further demonstrate that our algorithm is robustly trained and achieves competitive performance across standard continuous control benchmarks.

## 📝 요약

이 연구에서는 고전 역학의 정지 마찰과 오프-정책 강화 학습의 외삽 오류를 유사하게 보고, 정책이 지원되지 않는 행동으로 이동하는 것을 방지하는 제약 조건을 제시합니다. 이를 통해 Frictional Q-learning이라는 연속 제어를 위한 심층 강화 학습 알고리즘을 제안합니다. 이 알고리즘은 에이전트의 행동 공간을 제약하여 리플레이 버퍼와 유사한 행동을 유도하면서도 직교 행동 공간의 다양체와 거리를 유지합니다. 이러한 제약은 배치 제약의 단순성을 유지하면서 외삽 오류에 대한 직관적인 물리적 해석을 제공합니다. 실험 결과, 제안된 알고리즘은 견고하게 훈련되며 표준 연속 제어 벤치마크에서 경쟁력 있는 성능을 달성함을 보여줍니다.

## 🎯 주요 포인트

- 1. 정적 마찰과 오프폴리시 강화학습의 외삽 오류 간의 유사성을 통해 정책이 지원되지 않는 행동으로 이동하는 것을 방지하는 제약을 제시합니다.
- 2. Frictional Q-learning은 연속 제어를 위한 심층 강화학습 알고리즘으로, 배치 제약 강화학습을 확장합니다.
- 3. 알고리즘은 에이전트의 행동 공간을 제약하여 리플레이 버퍼와 유사한 행동을 유도하면서 직교 행동 공간의 다양체와의 거리를 유지합니다.
- 4. 제약은 배치 제약의 단순성을 유지하며 외삽 오류에 대한 직관적인 물리적 해석을 제공합니다.
- 5. 실험적으로, 제안된 알고리즘은 견고하게 훈련되며 표준 연속 제어 벤치마크에서 경쟁력 있는 성능을 달성함을 보여줍니다.


---

*Generated on 2025-09-25 15:48:24*