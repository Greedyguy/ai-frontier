---
keywords:
  - Machine Learning
  - Robotic Manipulation
  - Symmetry-Guided Learning
  - Behavior Cloning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2304.06055
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:36:29.354375",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Robotic Manipulation",
    "Symmetry-Guided Learning",
    "Behavior Cloning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Robotic Manipulation": 0.78,
    "Symmetry-Guided Learning": 0.82,
    "Behavior Cloning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a subset of Machine Learning, which is a broad technical category relevant to the paper's focus.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Robotic Manipulation",
        "canonical": "Robotic Manipulation",
        "aliases": [
          "Robot Control",
          "Robot Handling"
        ],
        "category": "unique_technical",
        "rationale": "Robotic Manipulation is a specific domain within robotics, crucial for the paper's context and novel in its application of symmetry-guided learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Symmetry-Guided Demonstrations",
        "canonical": "Symmetry-Guided Learning",
        "aliases": [
          "Symmetry-Based Learning"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's novel approach to improving sample efficiency in RL.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Behavior Cloning",
        "canonical": "Behavior Cloning",
        "aliases": [
          "Imitation Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Behavior Cloning is a specific technique in RL that enhances connectivity with other imitation learning methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "General Abstract Symmetry",
      "Demo-EASE"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Robotic Manipulation",
      "resolved_canonical": "Robotic Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Symmetry-Guided Demonstrations",
      "resolved_canonical": "Symmetry-Guided Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Behavior Cloning",
      "resolved_canonical": "Behavior Cloning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2304.06055.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2304.06055](https://arxiv.org/abs/2304.06055)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations_20250922|Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations]] (83.6% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (83.5% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (83.2% similar)
- [[2025-09-19/ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (82.8% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Behavior Cloning|Behavior Cloning]]
**⚡ Unique Technical**: [[keywords/Robotic Manipulation|Robotic Manipulation]], [[keywords/Symmetry-Guided Learning|Symmetry-Guided Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2304.06055v2 Announce Type: replace-cross 
Abstract: Reinforcement learning (RL) suffers from low sample efficiency, particularly in high-dimensional continuous state-action spaces of complex robotic manipulation tasks. RL performance can improve by leveraging prior knowledge, even when demonstrations are limited and collected from simplified environments. To address this, we define General Abstract Symmetry (GAS) for aggregating demonstrations from symmetrical abstract partitions of the robot environment. We introduce Demo-EASE, a novel training framework using a dual-buffer architecture that stores both demonstrations and RL-generated experiences. Demo-EASE improves sample efficiency through symmetry-guided demonstrations and behavior cloning, enabling strong initialization and balanced exploration-exploitation. Demo-EASE is compatible with both on-policy and off-policy RL algorithms, supporting various training regimes. We evaluate our framework in three simulation experiments using a Kinova Gen3 robot with joint-space control within PyBullet. Our results show that Demo-EASE significantly accelerates convergence and improves final performance compared to standard RL baselines, demonstrating its potential for efficient real-world robotic manipulation learning.

## 📝 요약

이 논문은 강화 학습(RL)의 샘플 효율성을 개선하기 위해 'Demo-EASE'라는 새로운 훈련 프레임워크를 제안합니다. RL은 특히 복잡한 로봇 조작 작업의 고차원 연속 상태-행동 공간에서 샘플 효율성이 낮습니다. 이를 해결하기 위해, 저자들은 로봇 환경의 대칭적 추상 분할에서 시연을 집계하는 일반 추상 대칭(GAS)을 정의합니다. Demo-EASE는 대칭에 기반한 시연과 행동 복제를 통해 샘플 효율성을 높이며, 강력한 초기화와 균형 잡힌 탐색-활용을 가능하게 합니다. 이 프레임워크는 온-정책 및 오프-정책 RL 알고리즘 모두와 호환되며, 다양한 훈련 환경을 지원합니다. Kinova Gen3 로봇을 사용한 세 가지 시뮬레이션 실험에서, Demo-EASE는 표준 RL 기준선과 비교하여 수렴 속도를 가속화하고 최종 성능을 향상시켰습니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)은 복잡한 로봇 조작 작업의 고차원 연속 상태-행동 공간에서 낮은 샘플 효율성을 겪습니다.
- 2. General Abstract Symmetry(GAS)를 정의하여 로봇 환경의 대칭적 추상 분할에서 시연을 집계합니다.
- 3. Demo-EASE는 시연과 RL 생성 경험을 저장하는 이중 버퍼 아키텍처를 사용하는 새로운 훈련 프레임워크입니다.
- 4. Demo-EASE는 대칭 유도 시연과 행동 복제를 통해 샘플 효율성을 개선하며, 강력한 초기화와 균형 잡힌 탐색-활용을 가능하게 합니다.
- 5. Demo-EASE는 표준 RL 기준선과 비교하여 수렴을 가속화하고 최종 성능을 향상시킵니다.


---

*Generated on 2025-09-24 00:36:29*