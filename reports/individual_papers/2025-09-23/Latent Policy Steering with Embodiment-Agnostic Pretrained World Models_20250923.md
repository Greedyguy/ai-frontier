---
keywords:
  - Visuomotor Policies
  - World Model
  - Latent Policy Steering
  - Optic Flow
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2507.13340
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:13:25.548281",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Visuomotor Policies",
    "World Model",
    "Latent Policy Steering",
    "Optic Flow"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Visuomotor Policies": 0.8,
    "World Model": 0.82,
    "Latent Policy Steering": 0.78,
    "Optic Flow": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "visuomotor policies",
        "canonical": "Visuomotor Policies",
        "aliases": [
          "visual motor policies"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on improving robot learning and is specific to the intersection of vision and motor control.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "World Model",
        "canonical": "World Model",
        "aliases": [
          "WM"
        ],
        "category": "specific_connectable",
        "rationale": "World Models are key to the paper's methodology, providing a framework for policy improvement across different embodiments.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Latent Policy Steering",
        "canonical": "Latent Policy Steering",
        "aliases": [
          "LPS"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for enhancing policy performance in the described experiments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "optic flow",
        "canonical": "Optic Flow",
        "aliases": [
          "optical flow"
        ],
        "category": "specific_connectable",
        "rationale": "Optic flow is used as an embodiment-agnostic action representation, making it a pivotal concept for cross-embodiment learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.77,
        "specificity_score": 0.73,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "robot data",
      "training demonstrations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "visuomotor policies",
      "resolved_canonical": "Visuomotor Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "World Model",
      "resolved_canonical": "World Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Latent Policy Steering",
      "resolved_canonical": "Latent Policy Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "optic flow",
      "resolved_canonical": "Optic Flow",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.77,
        "specificity": 0.73,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Latent Policy Steering with Embodiment-Agnostic Pretrained World Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.13340.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2507.13340](https://arxiv.org/abs/2507.13340)

## 🔗 유사한 논문
- [[2025-09-18/Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (84.2% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (83.8% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (83.6% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (83.3% similar)
- [[2025-09-23/Robot Learning with Sparsity and Scarcity_20250923|Robot Learning with Sparsity and Scarcity]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/World Model|World Model]], [[keywords/Optic Flow|Optic Flow]]
**⚡ Unique Technical**: [[keywords/Visuomotor Policies|Visuomotor Policies]], [[keywords/Latent Policy Steering|Latent Policy Steering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.13340v2 Announce Type: replace-cross 
Abstract: Learning visuomotor policies via imitation has proven effective across a wide range of robotic domains. However, the performance of these policies is heavily dependent on the number of training demonstrations, which requires expensive data collection in the real world. In this work, we aim to reduce data collection efforts when learning visuomotor robot policies by leveraging existing or cost-effective data from a wide range of embodiments, such as public robot datasets and the datasets of humans playing with objects (human data from play). Our approach leverages two key insights. First, we use optic flow as an embodiment-agnostic action representation to train a World Model (WM) across multi-embodiment datasets, and finetune it on a small amount of robot data from the target embodiment. Second, we develop a method, Latent Policy Steering (LPS), to improve the output of a behavior-cloned policy by searching in the latent space of the WM for better action sequences. In real world experiments, we observe significant improvements in the performance of policies trained with a small amount of data (over 50% relative improvement with 30 demonstrations and over 20% relative improvement with 50 demonstrations) by combining the policy with a WM pretrained on two thousand episodes sampled from the existing Open X-embodiment dataset across different robots or a cost-effective human dataset from play.

## 📝 요약

이 논문은 로봇의 시각-운동 정책 학습 시 데이터 수집 비용을 줄이기 위한 방법을 제안합니다. 기존의 로봇 데이터셋과 인간의 놀이 데이터를 활용하여 데이터 수집을 최소화하고자 합니다. 주요 기여는 두 가지입니다. 첫째, 다양한 구현체의 데이터셋을 활용해 세계 모델(WM)을 훈련하고, 목표 로봇 데이터로 미세 조정합니다. 둘째, 잠재 공간에서 더 나은 행동 시퀀스를 탐색하는 잠재 정책 조정(LPS) 방법을 개발했습니다. 실제 실험에서, 30개의 시연으로 50% 이상, 50개의 시연으로 20% 이상의 성능 향상을 확인했습니다.

## 🎯 주요 포인트

- 1. 시각-운동 정책 학습은 다양한 로봇 분야에서 효과적이지만, 많은 훈련 시연이 필요하여 실제 데이터 수집 비용이 높습니다.
- 2. 본 연구는 공공 로봇 데이터셋과 인간의 놀이 데이터셋 같은 기존 또는 저비용 데이터를 활용하여 데이터 수집 노력을 줄이고자 합니다.
- 3. 광류(optic flow)를 사용하여 다양한 구현 데이터셋에서 세계 모델(WM)을 훈련하고, 목표 구현의 소량 로봇 데이터로 미세 조정합니다.
- 4. 잠재 정책 조정(LPS) 방법을 개발하여 행동 복제 정책의 출력을 개선하고, WM의 잠재 공간에서 더 나은 행동 시퀀스를 검색합니다.
- 5. 실제 실험에서, 기존 데이터셋을 활용한 WM 사전 훈련을 통해 적은 양의 데이터로 훈련된 정책의 성능이 크게 향상되었습니다.


---

*Generated on 2025-09-24 01:13:25*