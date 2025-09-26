---
keywords:
  - Composable Navigation
  - Diffusion Models
  - Motion Primitives
  - Reinforcement Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17941
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:13:07.857650",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Composable Navigation",
    "Diffusion Models",
    "Motion Primitives",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Composable Navigation": 0.8,
    "Diffusion Models": 0.85,
    "Motion Primitives": 0.78,
    "Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ComposableNav",
        "canonical": "Composable Navigation",
        "aliases": [
          "ComposableNav"
        ],
        "category": "unique_technical",
        "rationale": "Composable Navigation is a novel approach in robotics for dynamic environments, enhancing connectivity with related navigation technologies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion model"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion Models are crucial in the paper's methodology, facilitating links to other machine learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "motion primitives",
        "canonical": "Motion Primitives",
        "aliases": [
          "motion primitive"
        ],
        "category": "specific_connectable",
        "rationale": "Motion Primitives are key components in robotic navigation, enabling connections to other robotic control strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "reinforcement learning fine-tuning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL fine-tuning"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational technique in AI, linking to a wide array of learning-based methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "dynamic environments",
      "instruction specifications"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ComposableNav",
      "resolved_canonical": "Composable Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "motion primitives",
      "resolved_canonical": "Motion Primitives",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reinforcement learning fine-tuning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17941.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17941](https://arxiv.org/abs/2509.17941)

## 🔗 유사한 논문
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (84.8% similar)
- [[2025-09-18/NavMoE_ Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts_20250918|NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (82.8% similar)
- [[2025-09-22/Compose by Focus_ Scene Graph-based Atomic Skills_20250922|Compose by Focus: Scene Graph-based Atomic Skills]] (82.7% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (81.9% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Motion Primitives|Motion Primitives]]
**⚡ Unique Technical**: [[keywords/Composable Navigation|Composable Navigation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17941v1 Announce Type: cross 
Abstract: This paper considers the problem of enabling robots to navigate dynamic environments while following instructions. The challenge lies in the combinatorial nature of instruction specifications: each instruction can include multiple specifications, and the number of possible specification combinations grows exponentially as the robot's skill set expands. For example, "overtake the pedestrian while staying on the right side of the road" consists of two specifications: "overtake the pedestrian" and "walk on the right side of the road." To tackle this challenge, we propose ComposableNav, based on the intuition that following an instruction involves independently satisfying its constituent specifications, each corresponding to a distinct motion primitive. Using diffusion models, ComposableNav learns each primitive separately, then composes them in parallel at deployment time to satisfy novel combinations of specifications unseen in training. Additionally, to avoid the onerous need for demonstrations of individual motion primitives, we propose a two-stage training procedure: (1) supervised pre-training to learn a base diffusion model for dynamic navigation, and (2) reinforcement learning fine-tuning that molds the base model into different motion primitives. Through simulation and real-world experiments, we show that ComposableNav enables robots to follow instructions by generating trajectories that satisfy diverse and unseen combinations of specifications, significantly outperforming both non-compositional VLM-based policies and costmap composing baselines. Videos and additional materials can be found on the project page: https://amrl.cs.utexas.edu/ComposableNav/

## 📝 요약

이 논문은 로봇이 동적 환경에서 지시를 따르며 이동하는 문제를 다룹니다. 지시사항은 여러 사양을 포함할 수 있어 조합의 수가 기하급수적으로 증가합니다. 이를 해결하기 위해 ComposableNav를 제안하며, 각 지시사항을 독립적으로 만족시키는 모션 프리미티브로 분해하여 학습합니다. 확산 모델을 사용해 각 프리미티브를 개별적으로 학습하고, 배포 시 새로운 사양 조합을 만족시키도록 병렬로 구성합니다. 또한, 모션 프리미티브에 대한 시범 없이도 학습할 수 있도록, 두 단계의 학습 절차를 제안합니다: (1) 동적 내비게이션을 위한 기본 확산 모델을 학습하는 지도 사전 학습, (2) 강화 학습을 통한 모션 프리미티브 세부 조정. 시뮬레이션 및 실제 실험을 통해 ComposableNav가 다양한 조합의 지시를 효과적으로 수행하며, 기존 방법들보다 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. ComposableNav는 로봇이 동적 환경에서 지시사항을 따르며 이동할 수 있도록 돕는 시스템으로, 각 지시사항의 구성 사양을 독립적으로 만족시키는 방식을 사용합니다.
- 2. 이 시스템은 확산 모델을 활용하여 각 모션 프리미티브를 개별적으로 학습하고, 배포 시 새로운 사양 조합을 병렬로 구성하여 만족시킵니다.
- 3. ComposableNav는 시뮬레이션 및 실제 실험을 통해 다양한 조합의 사양을 만족하는 경로를 생성하여 기존의 비구성적 VLM 기반 정책과 비용 지도 기반 방법보다 우수한 성능을 보였습니다.
- 4. 개별 모션 프리미티브에 대한 시범이 필요하지 않도록, 두 단계의 학습 절차를 제안하여 기본 확산 모델을 학습하고 강화 학습을 통해 다양한 모션 프리미티브로 세분화합니다.


---

*Generated on 2025-09-24 00:13:07*