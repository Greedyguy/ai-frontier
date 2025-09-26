<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:10:00.672586",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Diffusion Models",
    "Robotic Manipulation",
    "World Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Diffusion Models": 0.79,
    "Robotic Manipulation": 0.82,
    "World Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept in the paper, facilitating connections to policy refinement and robotic manipulation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based Models"
        ],
        "category": "unique_technical",
        "rationale": "The use of diffusion models is central to the proposed framework, offering a novel approach to world modeling in robotics.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Robotic Manipulation",
        "canonical": "Robotic Manipulation",
        "aliases": [
          "Robot Manipulation"
        ],
        "category": "specific_connectable",
        "rationale": "Robotic manipulation is a key application area discussed, linking to both policy refinement and simulation.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "World Models",
        "canonical": "World Models",
        "aliases": [
          "World Model"
        ],
        "category": "specific_connectable",
        "rationale": "World models are integral to the framework, enabling policy refinement in simulated environments.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "imitation learning",
      "expert data",
      "real-world interactions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Robotic Manipulation",
      "resolved_canonical": "Robotic Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "World Models",
      "resolved_canonical": "World Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19080.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19080](https://arxiv.org/abs/2509.19080)

## 🔗 유사한 논문
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (85.8% similar)
- [[2025-09-23/Prepare Before You Act_ Learning From Humans to Rearrange Initial States_20250923|Prepare Before You Act: Learning From Humans to Rearrange Initial States]] (83.6% similar)
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (83.6% similar)
- [[2025-09-23/Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation_20250923|Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation]] (83.4% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Robotic Manipulation|Robotic Manipulation]], [[keywords/World Models|World Models]]
**⚡ Unique Technical**: [[keywords/Diffusion Models|Diffusion Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19080v1 Announce Type: cross 
Abstract: Robotic manipulation policies are commonly initialized through imitation learning, but their performance is limited by the scarcity and narrow coverage of expert data. Reinforcement learning can refine polices to alleviate this limitation, yet real-robot training is costly and unsafe, while training in simulators suffers from the sim-to-real gap. Recent advances in generative models have demonstrated remarkable capabilities in real-world simulation, with diffusion models in particular excelling at generation. This raises the question of how diffusion model-based world models can be combined to enhance pre-trained policies in robotic manipulation. In this work, we propose World4RL, a framework that employs diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely in imagined environments for robotic manipulation. Unlike prior works that primarily employ world models for planning, our framework enables direct end-to-end policy optimization. World4RL is designed around two principles: pre-training a diffusion world model that captures diverse dynamics on multi-task datasets and refining policies entirely within a frozen world model to avoid online real-world interactions. We further design a two-hot action encoding scheme tailored for robotic manipulation and adopt diffusion backbones to improve modeling fidelity. Extensive simulation and real-world experiments demonstrate that World4RL provides high-fidelity environment modeling and enables consistent policy refinement, yielding significantly higher success rates compared to imitation learning and other baselines. More visualization results are available at https://world4rl.github.io/.

## 📝 요약

이 논문은 로봇 조작 정책을 개선하기 위해 제안된 World4RL이라는 프레임워크를 소개합니다. 기존의 모방 학습과 강화 학습의 한계를 극복하기 위해, World4RL은 확산 모델 기반의 세계 모델을 활용하여 고품질 시뮬레이션 환경을 제공합니다. 이 프레임워크는 사전 학습된 정책을 상상된 환경 내에서 최적화하며, 실제 환경과의 상호작용 없이 정책을 개선합니다. 두 가지 주요 원칙은 다양한 동적 데이터를 포괄하는 확산 세계 모델의 사전 학습과 고정된 세계 모델 내에서의 정책 최적화입니다. 또한, 로봇 조작에 특화된 이중-핫 액션 인코딩 방식을 설계했습니다. 실험 결과, World4RL은 높은 성공률을 보이며 기존의 모방 학습 및 다른 기준보다 뛰어난 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. World4RL은 확산 기반 세계 모델을 사용하여 로봇 조작을 위한 사전 학습된 정책을 상상된 환경에서 정제하는 프레임워크입니다.
- 2. 이 프레임워크는 계획에 주로 사용되던 기존의 세계 모델과 달리, 직접적인 종단 간 정책 최적화를 가능하게 합니다.
- 3. World4RL은 다양한 동적 특성을 포착하는 다중 작업 데이터셋에서 확산 세계 모델을 사전 학습하고, 온라인 현실 세계 상호작용을 피하기 위해 고정된 세계 모델 내에서 정책을 정제합니다.
- 4. 로봇 조작에 맞춘 투-핫 액션 인코딩 방식을 설계하고, 확산 백본을 채택하여 모델링 정확도를 향상시킵니다.
- 5. 광범위한 시뮬레이션 및 실제 실험을 통해 World4RL이 높은 정확도의 환경 모델링을 제공하고, 일관된 정책 정제를 가능하게 하여 모방 학습 및 기타 기준보다 훨씬 높은 성공률을 달성함을 입증합니다.


---

*Generated on 2025-09-24 14:10:00*