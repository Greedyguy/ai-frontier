<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:22:56.316514",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Latent Action Representations",
    "World Modeling",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.82,
    "Latent Action Representations": 0.79,
    "World Modeling": 0.75,
    "Self-supervised Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language-Action",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA"
        ],
        "category": "evolved_concepts",
        "rationale": "Connects to the growing field of integrating vision and language for action tasks, relevant for multimodal learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Latent Action Representations",
        "canonical": "Latent Action Representations",
        "aliases": [
          "LAR"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for unsupervised pretraining in robotics, enhancing task transferability.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "World Modeling",
        "canonical": "World Modeling",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for understanding and predicting environmental changes, crucial for self-supervised learning.",
        "novelty_score": 0.67,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key technique for training models without labeled data, relevant across multiple domains.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "robotic manipulation tasks",
      "real-world settings"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language-Action",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Latent Action Representations",
      "resolved_canonical": "Latent Action Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "World Modeling",
      "resolved_canonical": "World Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Latent Action Pretraining Through World Modeling

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18428.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18428](https://arxiv.org/abs/2509.18428)

## 🔗 유사한 논문
- [[2025-09-24/VLA-LPAF_ Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation_20250924|VLA-LPAF: Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation]] (87.6% similar)
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (86.7% similar)
- [[2025-09-23/Evo-0_ Vision-Language-Action Model with Implicit Spatial Understanding_20250923|Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding]] (86.4% similar)
- [[2025-09-24/Bi-VLA_ Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation_20250924|Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation]] (85.9% similar)
- [[2025-09-24/Pure Vision Language Action (VLA) Models_ A Comprehensive Survey_20250924|Pure Vision Language Action (VLA) Models: A Comprehensive Survey]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Latent Action Representations|Latent Action Representations]], [[keywords/World Modeling|World Modeling]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18428v1 Announce Type: cross 
Abstract: Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $\pi_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is designed to be effective for transferring across tasks, environments, and embodiments. It outperforms models trained with ground-truth robotics actions and similar pretraining methods on the LIBERO benchmark and real-world setup, while being significantly more efficient and practical for real-world settings.

## 📝 요약

Vision-Language-Action (VLA) 모델은 언어 지시에 따라 로봇 조작 작업을 학습하는 데 인기를 얻고 있습니다. 기존의 VLA 모델들은 대규모로 수집된 레이블이 있는 데이터셋을 사용해 훈련되었습니다. 최근에는 LAPA와 villa-X와 같은 접근법이 프레임 간의 추상적인 시각적 변화를 모델링하여 레이블이 없는 데이터셋에서 비지도 사전 학습을 가능하게 했습니다. 그러나 이러한 방법들은 모델 크기가 커 실제 환경에서의 배포가 어렵습니다. 본 연구에서는 LAWM이라는 모델-독립적 프레임워크를 제안하여, 레이블이 없는 비디오 데이터를 통해 잠재적 행동 표현을 학습하는 자기 지도 학습 방식을 사용합니다. 이 프레임워크는 다양한 작업, 환경, 구현체에 걸쳐 효과적으로 전이할 수 있으며, LIBERO 벤치마크 및 실제 환경에서 기존 모델보다 효율적이고 실용적입니다.

## 🎯 주요 포인트

- 1. Vision-Language-Action(VLA) 모델은 언어 지시를 따르는 로봇 조작 작업 학습에 인기를 얻고 있다.
- 2. 기존 VLA 모델은 대규모 수작업으로 라벨링된 데이터셋을 기반으로 훈련되었으나, LAPA와 villa-X는 프레임 간 추상적 시각 변화를 모델링하여 비지도 사전 훈련을 가능하게 한다.
- 3. 대규모 모델 크기로 인해 실제 환경에서의 배포가 어려운 문제를 해결하기 위해, LAWM은 비디오 데이터를 활용한 자기 지도 방식으로 모방 학습 모델을 사전 훈련하는 프레임워크를 제안한다.
- 4. LAWM은 다양한 작업, 환경, 구현체 간의 전이를 효과적으로 수행할 수 있으며, LIBERO 벤치마크와 실제 환경에서 기존 모델보다 효율적이고 실용적이다.
- 5. 제안된 프레임워크는 로봇 녹화 영상이나 일상 물체를 다루는 인간의 행동 영상에서 비디오 데이터를 얻어 활용할 수 있다.


---

*Generated on 2025-09-24 16:22:56*