<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:09:26.495179",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reduced-Order Model-Guided Reinforcement Learning",
    "Proximal Policy Optimization",
    "Soft Actor-Critic",
    "Adversarial Discriminator"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reduced-Order Model-Guided Reinforcement Learning": 0.78,
    "Proximal Policy Optimization": 0.79,
    "Soft Actor-Critic": 0.77,
    "Adversarial Discriminator": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reduced-Order Model-Guided Reinforcement Learning",
        "canonical": "Reduced-Order Model-Guided Reinforcement Learning",
        "aliases": [
          "ROM-GRL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework that combines reduced-order models with reinforcement learning, offering a unique approach to humanoid locomotion.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "A widely used reinforcement learning algorithm that can connect to various RL-based studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Soft Actor-Critic",
        "canonical": "Soft Actor-Critic",
        "aliases": [
          "SAC"
        ],
        "category": "specific_connectable",
        "rationale": "A popular algorithm in reinforcement learning, facilitating connections to other works using similar methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "adversarial discriminator",
        "canonical": "Adversarial Discriminator",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This component is crucial for ensuring policy alignment, linking to adversarial learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.76,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "humanoid locomotion",
      "gait templates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reduced-Order Model-Guided Reinforcement Learning",
      "resolved_canonical": "Reduced-Order Model-Guided Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Soft Actor-Critic",
      "resolved_canonical": "Soft Actor-Critic",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "adversarial discriminator",
      "resolved_canonical": "Adversarial Discriminator",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.76,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Reduced-Order Model-Guided Reinforcement Learning for Demonstration-Free Humanoid Locomotion

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19023.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19023](https://arxiv.org/abs/2509.19023)

## 🔗 유사한 논문
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (85.3% similar)
- [[2025-09-23/HuMam_ Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba_20250923|HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba]] (84.3% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (83.6% similar)
- [[2025-09-23/Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation_20250923|Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation]] (83.4% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]], [[keywords/Soft Actor-Critic|Soft Actor-Critic]], [[keywords/Adversarial Discriminator|Adversarial Discriminator]]
**⚡ Unique Technical**: [[keywords/Reduced-Order Model-Guided Reinforcement Learning|Reduced-Order Model-Guided Reinforcement Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19023v1 Announce Type: cross 
Abstract: We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 📝 요약

이 논문은 인간형 로봇의 보행을 위한 강화 학습 프레임워크인 ROM-GRL을 소개합니다. ROM-GRL은 모션 캡처 데이터나 복잡한 보상 설계 없이 두 단계로 구성됩니다. 첫 번째 단계에서는 4자유도(4-DOF)의 간소화된 모델을 사용하여 에너지 효율적인 보행 템플릿을 생성합니다. 두 번째 단계에서는 이러한 템플릿을 기반으로 전신 정책을 학습하여 안정적이고 대칭적인 보행을 구현합니다. 실험 결과, ROM-GRL은 순수 보상 기반 방법보다 낮은 추적 오류를 보이며, 인간 시연 없이도 자연스러운 로봇 행동을 가능하게 합니다.

## 🎯 주요 포인트

- 1. ROM-GRL은 모션 캡처 데이터나 복잡한 보상 설계 없이 인간형 로봇의 보행을 위한 강화 학습 프레임워크를 제공합니다.
- 2. 첫 번째 단계에서는 4자유도(4-DOF) 축소 모델(ROM)을 사용하여 에너지 효율적인 보행 템플릿을 생성합니다.
- 3. 두 번째 단계에서는 ROM의 동적 궤적을 기반으로 전체 신체 정책을 학습하여 5차원 보행 특징 분포를 맞춥니다.
- 4. ROM-GRL은 1m/s 및 4m/s 실험에서 안정적이고 대칭적인 보행을 생성하며, 순수 보상 기반 방법보다 추적 오류가 적습니다.
- 5. ROM-GRL은 보상 기반과 모방 기반 보행 방법 간의 격차를 줄여 인간 시연 없이도 자연스러운 인간형 로봇 행동을 가능하게 합니다.


---

*Generated on 2025-09-24 14:09:26*