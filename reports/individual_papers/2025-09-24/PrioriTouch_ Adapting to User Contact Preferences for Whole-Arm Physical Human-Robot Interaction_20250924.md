<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:49:18.666691",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Physical Human-Robot Interaction",
    "Hierarchical Operational Space Control",
    "Learning-to-Rank",
    "Simulation-in-the-Loop Rollouts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Physical Human-Robot Interaction": 0.85,
    "Hierarchical Operational Space Control": 0.8,
    "Learning-to-Rank": 0.78,
    "Simulation-in-the-Loop Rollouts": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Physical Human-Robot Interaction",
        "canonical": "Physical Human-Robot Interaction",
        "aliases": [
          "pHRI"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on adapting to user contact preferences in robotics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Operational Space Control",
        "canonical": "Hierarchical Operational Space Control",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific control strategy used in the framework, relevant for linking to control systems in robotics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Learning-to-Rank",
        "canonical": "Learning-to-Rank",
        "aliases": [
          "LTR"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is used for prioritizing control objectives, linking to machine learning methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Simulation-in-the-Loop Rollouts",
        "canonical": "Simulation-in-the-Loop Rollouts",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This approach is crucial for safe exploration in the framework, connecting to simulation techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Physical Human-Robot Interaction",
      "resolved_canonical": "Physical Human-Robot Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hierarchical Operational Space Control",
      "resolved_canonical": "Hierarchical Operational Space Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Learning-to-Rank",
      "resolved_canonical": "Learning-to-Rank",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Simulation-in-the-Loop Rollouts",
      "resolved_canonical": "Simulation-in-the-Loop Rollouts",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PrioriTouch: Adapting to User Contact Preferences for Whole-Arm Physical Human-Robot Interaction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18447.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18447](https://arxiv.org/abs/2509.18447)

## 🔗 유사한 논문
- [[2025-09-18/Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer_20250918|Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer]] (81.8% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (81.8% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.5% similar)
- [[2025-09-18/The Role of Touch_ Towards Optimal Tactile Sensing Distribution in Anthropomorphic Hands for Dexterous In-Hand Manipulation_20250918|The Role of Touch: Towards Optimal Tactile Sensing Distribution in Anthropomorphic Hands for Dexterous In-Hand Manipulation]] (81.2% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Learning-to-Rank|Learning-to-Rank]]
**⚡ Unique Technical**: [[keywords/Physical Human-Robot Interaction|Physical Human-Robot Interaction]], [[keywords/Hierarchical Operational Space Control|Hierarchical Operational Space Control]], [[keywords/Simulation-in-the-Loop Rollouts|Simulation-in-the-Loop Rollouts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18447v1 Announce Type: cross 
Abstract: Physical human-robot interaction (pHRI) requires robots to adapt to individual contact preferences, such as where and how much force is applied. Identifying preferences is difficult for a single contact; with whole-arm interaction involving multiple simultaneous contacts between the robot and human, the challenge is greater because different body parts can impose incompatible force requirements. In caregiving tasks, where contact is frequent and varied, such conflicts are unavoidable. With multiple preferences across multiple contacts, no single solution can satisfy all objectives--trade-offs are inherent, making prioritization essential. We present PrioriTouch, a framework for ranking and executing control objectives across multiple contacts. PrioriTouch can prioritize from a general collection of controllers, making it applicable not only to caregiving scenarios such as bed bathing and dressing but also to broader multi-contact settings. Our method combines a novel learning-to-rank approach with hierarchical operational space control, leveraging simulation-in-the-loop rollouts for data-efficient and safe exploration. We conduct a user study on physical assistance preferences, derive personalized comfort thresholds, and incorporate them into PrioriTouch. We evaluate PrioriTouch through extensive simulation and real-world experiments, demonstrating its ability to adapt to user contact preferences, maintain task performance, and enhance safety and comfort. Website: https://emprise.cs.cornell.edu/prioritouch.

## 📝 요약

이 논문은 물리적 인간-로봇 상호작용(pHRI)에서 로봇이 개인의 접촉 선호도에 적응할 수 있도록 하는 PrioriTouch라는 프레임워크를 제안합니다. PrioriTouch는 여러 접촉 지점에서의 제어 목표를 우선순위화하여 실행할 수 있으며, 특히 간병 작업과 같은 다중 접촉 상황에 유용합니다. 이 방법은 학습-순위화 접근법과 계층적 운영 공간 제어를 결합하여 데이터 효율적이고 안전한 탐색을 가능하게 합니다. 사용자 연구를 통해 개인화된 편안함 임계값을 도출하고 이를 PrioriTouch에 통합하여 사용자 접촉 선호도에 적응하고 작업 성능을 유지하며 안전성과 편안함을 향상시킵니다. 시뮬레이션과 실제 실험을 통해 이 프레임워크의 효과를 검증했습니다.

## 🎯 주요 포인트

- 1. PrioriTouch는 다중 접촉 상황에서 제어 목표를 우선순위화하여 실행하는 프레임워크입니다.
- 2. 이 방법은 학습 기반 순위 결정 접근법과 계층적 운영 공간 제어를 결합하여 데이터 효율적이고 안전한 탐색을 가능하게 합니다.
- 3. 사용자 연구를 통해 개인화된 편안함 임계값을 도출하고 이를 PrioriTouch에 통합하였습니다.
- 4. PrioriTouch는 시뮬레이션 및 실제 실험을 통해 사용자 접촉 선호도에 적응하고, 작업 성능을 유지하며, 안전성과 편안함을 향상시킵니다.
- 5. 이 프레임워크는 간병 작업뿐만 아니라 다양한 다중 접촉 환경에 적용 가능합니다.


---

*Generated on 2025-09-24 13:49:18*