---
keywords:
  - Synthetic Robot Pose Generation
  - RGB-D Data Augmentation
  - Imitation Learning
  - Stable Diffusion
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19454
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:35:52.460298",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Synthetic Robot Pose Generation",
    "RGB-D Data Augmentation",
    "Imitation Learning",
    "Stable Diffusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Synthetic Robot Pose Generation": 0.8,
    "RGB-D Data Augmentation": 0.78,
    "Imitation Learning": 0.75,
    "Stable Diffusion": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Synthetic Robot Pose Generation",
        "canonical": "Synthetic Robot Pose Generation",
        "aliases": [
          "ROPA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for understanding the specific data augmentation technique discussed.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "RGB-D Bimanual Data Augmentation",
        "canonical": "RGB-D Data Augmentation",
        "aliases": [
          "Bimanual Data Augmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to the broader topic of data augmentation in computer vision, specifically for RGB-D data.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "Learning from Demonstration"
        ],
        "category": "broad_technical",
        "rationale": "Imitation learning is a foundational concept in machine learning, relevant to the training methods discussed.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Stable Diffusion",
        "canonical": "Stable Diffusion",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Stable Diffusion is a key technique used in the paper for generating synthetic data, linking to broader diffusion models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
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
      "candidate_surface": "Synthetic Robot Pose Generation",
      "resolved_canonical": "Synthetic Robot Pose Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "RGB-D Bimanual Data Augmentation",
      "resolved_canonical": "RGB-D Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Imitation Learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Stable Diffusion",
      "resolved_canonical": "Stable Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# ROPA: Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19454.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19454](https://arxiv.org/abs/2509.19454)

## 🔗 유사한 논문
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (85.7% similar)
- [[2025-09-23/End-to-end RL Improves Dexterous Grasping Policies_20250923|End-to-end RL Improves Dexterous Grasping Policies]] (85.0% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (84.6% similar)
- [[2025-09-24/MV-UMI_ A Scalable Multi-View Interface for Cross-Embodiment Learning_20250924|MV-UMI: A Scalable Multi-View Interface for Cross-Embodiment Learning]] (84.2% similar)
- [[2025-09-23/Leveraging RGB Images for Pre-Training of Event-Based Hand Pose Estimation_20250923|Leveraging RGB Images for Pre-Training of Event-Based Hand Pose Estimation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Imitation Learning|Imitation Learning]]
**🔗 Specific Connectable**: [[keywords/RGB-D Data Augmentation|RGB-D Data Augmentation]], [[keywords/Stable Diffusion|Stable Diffusion]]
**⚡ Unique Technical**: [[keywords/Synthetic Robot Pose Generation|Synthetic Robot Pose Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19454v1 Announce Type: cross 
Abstract: Training robust bimanual manipulation policies via imitation learning requires demonstration data with broad coverage over robot poses, contacts, and scene contexts. However, collecting diverse and precise real-world demonstrations is costly and time-consuming, which hinders scalability. Prior works have addressed this with data augmentation, typically for either eye-in-hand (wrist camera) setups with RGB inputs or for generating novel images without paired actions, leaving augmentation for eye-to-hand (third-person) RGB-D training with new action labels less explored. In this paper, we propose Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation (ROPA), an offline imitation learning data augmentation method that fine-tunes Stable Diffusion to synthesize third-person RGB and RGB-D observations of novel robot poses. Our approach simultaneously generates corresponding joint-space action labels while employing constrained optimization to enforce physical consistency through appropriate gripper-to-object contact constraints in bimanual scenarios. We evaluate our method on 5 simulated and 3 real-world tasks. Our results across 2625 simulation trials and 300 real-world trials demonstrate that ROPA outperforms baselines and ablations, showing its potential for scalable RGB and RGB-D data augmentation in eye-to-hand bimanual manipulation. Our project website is available at: https://ropaaug.github.io/.

## 📝 요약

이 논문은 모방 학습을 통한 견고한 양손 조작 정책 훈련을 위해 다양한 로봇 자세와 접촉, 장면 맥락을 포함하는 시연 데이터를 필요로 하지만, 실제 시연 데이터를 수집하는 것은 비용이 많이 들고 시간이 소요된다는 문제를 해결하고자 합니다. 이를 위해 제안된 방법론은 ROPA(Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation)로, Stable Diffusion을 활용하여 새로운 로봇 자세의 제3자 시점 RGB 및 RGB-D 관측을 생성하고, 물리적 일관성을 유지하기 위해 제약 최적화를 사용하여 적절한 그리퍼-객체 접촉 제약을 적용합니다. 5개의 시뮬레이션 및 3개의 실제 과제를 통해 평가한 결과, ROPA는 기존 방법들을 능가하며, eye-to-hand 양손 조작에서의 확장 가능한 데이터 증강 가능성을 보여주었습니다.

## 🎯 주요 포인트

- 1. ROPA는 새로운 로봇 자세의 RGB 및 RGB-D 관찰을 합성하여 모방 학습 데이터 증강을 수행하는 방법입니다.
- 2. 이 방법은 물리적 일관성을 유지하기 위해 그리퍼와 객체 간의 접촉 제약을 활용하여 적절한 조인트 공간 행동 레이블을 생성합니다.
- 3. 5개의 시뮬레이션 작업과 3개의 실제 작업에서 ROPA의 성능을 평가했으며, 총 2625회의 시뮬레이션 실험과 300회의 실제 실험에서 기존 방법보다 우수한 성과를 보였습니다.
- 4. ROPA는 eye-to-hand 방식의 양손 조작에서 RGB 및 RGB-D 데이터 증강의 확장 가능성을 보여줍니다.


---

*Generated on 2025-09-25 15:35:52*