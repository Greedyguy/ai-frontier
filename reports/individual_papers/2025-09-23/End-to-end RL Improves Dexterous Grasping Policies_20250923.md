---
keywords:
  - End-to-End Reinforcement Learning
  - Dexterous Grasping
  - Vision-Based Reinforcement Learning
  - Depth Distillation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16434
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:08:34.567355",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "End-to-End Reinforcement Learning",
    "Dexterous Grasping",
    "Vision-Based Reinforcement Learning",
    "Depth Distillation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "End-to-End Reinforcement Learning": 0.82,
    "Dexterous Grasping": 0.78,
    "Vision-Based Reinforcement Learning": 0.77,
    "Depth Distillation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "end-to-end RL",
        "canonical": "End-to-End Reinforcement Learning",
        "aliases": [
          "end-to-end reinforcement learning"
        ],
        "category": "specific_connectable",
        "rationale": "End-to-end RL is a key concept in the paper, linking vision-based policies with reinforcement learning techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "dexterous grasping",
        "canonical": "Dexterous Grasping",
        "aliases": [
          "dexterous manipulation"
        ],
        "category": "unique_technical",
        "rationale": "Dexterous grasping is a unique application area for robotics, central to the paper's focus.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "vision-based RL",
        "canonical": "Vision-Based Reinforcement Learning",
        "aliases": [
          "vision-based reinforcement learning"
        ],
        "category": "specific_connectable",
        "rationale": "Vision-based RL is crucial for understanding the paper's approach to integrating visual data in RL.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      },
      {
        "surface": "depth distillation",
        "canonical": "Depth Distillation",
        "aliases": [
          "depth policy distillation"
        ],
        "category": "unique_technical",
        "rationale": "Depth distillation is a novel technique discussed in the paper, enhancing policy performance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "simulator",
      "GPU"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "end-to-end RL",
      "resolved_canonical": "End-to-End Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "dexterous grasping",
      "resolved_canonical": "Dexterous Grasping",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "vision-based RL",
      "resolved_canonical": "Vision-Based Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "depth distillation",
      "resolved_canonical": "Depth Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# End-to-end RL Improves Dexterous Grasping Policies

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16434.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16434](https://arxiv.org/abs/2509.16434)

## 🔗 유사한 논문
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (83.9% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (83.7% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (83.4% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.9% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/End-to-End Reinforcement Learning|End-to-End Reinforcement Learning]], [[keywords/Vision-Based Reinforcement Learning|Vision-Based Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Dexterous Grasping|Dexterous Grasping]], [[keywords/Depth Distillation|Depth Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16434v1 Announce Type: cross 
Abstract: This work explores techniques to scale up image-based end-to-end learning for dexterous grasping with an arm + hand system. Unlike state-based RL, vision-based RL is much more memory inefficient, resulting in relatively low batch sizes, which is not amenable for algorithms like PPO. Nevertheless, it is still an attractive method as unlike the more commonly used techniques which distill state-based policies into vision networks, end-to-end RL can allow for emergent active vision behaviors. We identify a key bottleneck in training these policies is the way most existing simulators scale to multiple GPUs using traditional data parallelism techniques. We propose a new method where we disaggregate the simulator and RL (both training and experience buffers) onto separate GPUs. On a node with four GPUs, we have the simulator running on three of them, and PPO running on the fourth. We are able to show that with the same number of GPUs, we can double the number of existing environments compared to the previous baseline of standard data parallelism. This allows us to train vision-based environments, end-to-end with depth, which were previously performing far worse with the baseline. We train and distill both depth and state-based policies into stereo RGB networks and show that depth distillation leads to better results, both in simulation and reality. This improvement is likely due to the observability gap between state and vision policies which does not exist when distilling depth policies into stereo RGB. We further show that the increased batch size brought about by disaggregated simulation also improves real world performance. When deploying in the real world, we improve upon the previous state-of-the-art vision-based results using our end-to-end policies.

## 📝 요약

이 연구는 팔과 손 시스템을 활용한 이미지 기반의 종단 간 학습을 확장하는 기술을 탐구합니다. 기존의 상태 기반 강화 학습과 달리, 비전 기반 강화 학습은 메모리 효율이 낮아 배치 크기가 작아지는 문제가 있습니다. 그러나 종단 간 학습은 능동적 비전 행동을 유도할 수 있어 매력적입니다. 기존 시뮬레이터가 여러 GPU로 확장할 때의 병목 현상을 해결하기 위해, 시뮬레이터와 강화 학습을 개별 GPU에 분산시키는 새로운 방법을 제안합니다. 네 개의 GPU 노드에서 세 개는 시뮬레이터, 하나는 PPO를 실행하여, 기존 데이터 병렬 처리 방식보다 두 배 많은 환경을 생성할 수 있었습니다. 이를 통해 깊이 기반 정책을 스테레오 RGB 네트워크로 증류하여 더 나은 성능을 달성했습니다. 또한, 분산된 시뮬레이션으로 인한 배치 크기 증가가 실제 환경에서도 성능을 향상시킴을 보였습니다.

## 🎯 주요 포인트

- 1. 이미지 기반의 종단간 학습을 확장하여 팔과 손 시스템을 이용한 정교한 그립을 가능하게 하는 기술을 탐구했습니다.
- 2. 기존의 데이터 병렬 처리 기법으로는 여러 GPU에 시뮬레이터를 확장하는 데 한계가 있음을 확인했습니다.
- 3. 시뮬레이터와 강화학습을 별도의 GPU에 분산하여 실행하는 새로운 방법을 제안했습니다.
- 4. 제안된 방법으로 기존의 데이터 병렬 처리 방식보다 두 배의 환경을 동일한 GPU 수로 실행할 수 있었습니다.
- 5. 깊이 기반 정책을 스테레오 RGB 네트워크로 증류하여 시뮬레이션 및 실제 환경에서 더 나은 성능을 보였습니다.


---

*Generated on 2025-09-24 02:08:34*