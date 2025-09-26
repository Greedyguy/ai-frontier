---
keywords:
  - End-to-End Reinforcement Learning
  - Mamba Encoder
  - Proximal Policy Optimization
  - Humanoid Locomotion
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18046
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:18:54.560130",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "End-to-End Reinforcement Learning",
    "Mamba Encoder",
    "Proximal Policy Optimization",
    "Humanoid Locomotion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "End-to-End Reinforcement Learning": 0.78,
    "Mamba Encoder": 0.82,
    "Proximal Policy Optimization": 0.85,
    "Humanoid Locomotion": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "End-to-end reinforcement learning",
        "canonical": "End-to-End Reinforcement Learning",
        "aliases": [
          "E2E RL"
        ],
        "category": "broad_technical",
        "rationale": "This concept is central to the paper's approach and connects to broader discussions in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mamba encoder",
        "canonical": "Mamba Encoder",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique component of the proposed framework, offering a novel approach to state fusion.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "A widely used algorithm in reinforcement learning, facilitating connections to similar works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Humanoid locomotion",
        "canonical": "Humanoid Locomotion",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific application area of the study, linking to research in robotics and biomechanics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "training stability",
      "task performance",
      "energy saving"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "End-to-end reinforcement learning",
      "resolved_canonical": "End-to-End Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mamba encoder",
      "resolved_canonical": "Mamba Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Humanoid locomotion",
      "resolved_canonical": "Humanoid Locomotion",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18046.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18046](https://arxiv.org/abs/2509.18046)

## 🔗 유사한 논문
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (85.2% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (84.7% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.7% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (83.2% similar)
- [[2025-09-19/DreamControl_ Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion_20250919|DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/End-to-End Reinforcement Learning|End-to-End Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]], [[keywords/Humanoid Locomotion|Humanoid Locomotion]]
**⚡ Unique Technical**: [[keywords/Mamba Encoder|Mamba Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18046v1 Announce Type: cross 
Abstract: End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 📝 요약

이 논문에서는 휴머노이드 로봇의 보행을 위한 종단간 강화학습(RL) 프레임워크인 HuMam을 제안합니다. HuMam은 로봇 중심 상태와 발걸음 목표를 단일 레이어 Mamba 인코더로 융합하고, 연속적인 위상 시계를 사용하여 정책을 최적화합니다. 정책은 관절 위치 목표를 출력하고, PPO 알고리즘으로 최적화됩니다. 보상은 접촉 품질, 스윙 부드러움, 발 위치, 자세, 신체 안정성을 균형 있게 고려하며 에너지 절약을 촉진합니다. HuMam은 mc-mujoco의 JVRC-1 휴머노이드에서 학습 효율성, 안정성, 과제 수행 능력을 향상시키고, 전력 소비와 토크 피크를 줄입니다. Mamba를 융합 백본으로 사용하는 최초의 휴머노이드 RL 컨트롤러로서 효율성과 안정성, 제어 경제성에서 실질적인 개선을 보여줍니다.

## 🎯 주요 포인트

- 1. HuMam은 로봇 중심 상태와 발걸음 목표를 융합하는 Mamba 인코더를 사용하여 효율적인 학습과 안정성을 제공합니다.
- 2. 정책은 저수준 PD 루프가 추적하는 관절 위치 목표를 출력하며, PPO로 최적화됩니다.
- 3. 여섯 가지 보상 항목은 접촉 품질, 스윙 부드러움, 발 위치, 자세, 신체 안정성을 균형 있게 조절하며 에너지 절약을 촉진합니다.
- 4. HuMam은 mc-mujoco의 JVRC-1 휴머노이드에서 학습 효율성, 훈련 안정성, 과제 성능을 개선하고 전력 소비와 토크 피크를 줄입니다.
- 5. Mamba를 융합 백본으로 채택한 최초의 휴머노이드 RL 컨트롤러로, 효율성, 안정성, 제어 경제성에서 실질적인 이점을 보여줍니다.


---

*Generated on 2025-09-24 00:18:54*