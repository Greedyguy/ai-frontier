---
keywords:
  - OmniVLA
  - Vision-Language Model
  - Multimodal Learning
  - Robotic Navigation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19480
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:55:15.669055",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "OmniVLA",
    "Vision-Language Model",
    "Multimodal Learning",
    "Robotic Navigation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "OmniVLA": 0.8,
    "Vision-Language Model": 0.88,
    "Multimodal Learning": 0.82,
    "Robotic Navigation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "OmniVLA",
        "canonical": "OmniVLA",
        "aliases": [
          "Omni-Modal Vision-Language-Action Model"
        ],
        "category": "unique_technical",
        "rationale": "OmniVLA is a novel model introduced in the paper, representing a unique approach to omni-modal robotic navigation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language-Action",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA"
        ],
        "category": "evolved_concepts",
        "rationale": "The integration of vision, language, and action in a single model is a significant advancement in multimodal learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Omni-modal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is central to the paper's approach, enhancing connectivity with related research on integrating multiple data types.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Robotic Navigation",
        "canonical": "Robotic Navigation",
        "aliases": [
          "Robot Navigation"
        ],
        "category": "broad_technical",
        "rationale": "Robotic navigation is a fundamental aspect of the study, linking to a wide range of robotics research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
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
      "candidate_surface": "OmniVLA",
      "resolved_canonical": "OmniVLA",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language-Action",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Robotic Navigation",
      "resolved_canonical": "Robotic Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19480.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19480](https://arxiv.org/abs/2509.19480)

## 🔗 유사한 논문
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (86.3% similar)
- [[2025-09-24/Pure Vision Language Action (VLA) Models_ A Comprehensive Survey_20250924|Pure Vision Language Action (VLA) Models: A Comprehensive Survey]] (86.0% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (85.9% similar)
- [[2025-09-24/OmniBridge_ Unified Multimodal Understanding, Generation, and Retrieval via Latent Space Alignment_20250924|OmniBridge: Unified Multimodal Understanding, Generation, and Retrieval via Latent Space Alignment]] (85.7% similar)
- [[2025-09-23/Evo-0_ Vision-Language-Action Model with Implicit Spatial Understanding_20250923|Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Robotic Navigation|Robotic Navigation]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/OmniVLA|OmniVLA]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19480v1 Announce Type: cross 
Abstract: Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 📝 요약

이 논문은 로봇 내비게이션에서 다양한 목표 명세를 유연하게 해석하고 조합할 수 있는 훈련 프레임워크를 제안합니다. 기존 로봇 내비게이션 정책은 단일 모달리티에 의존하지만, 제안된 OmniVLA 모델은 2D 위치, 자아 중심 이미지, 자연어 등 세 가지 주요 목표 모달리티를 결합하여 훈련됩니다. 이 방법은 데이터셋의 활용 범위를 확장하고, 정책이 풍부한 기하학적, 의미적, 시각적 표현을 개발하도록 유도합니다. 결과적으로 OmniVLA는 새로운 환경에 대한 일반화 능력과 희소한 모달리티에 대한 강건성을 보여주며, 새로운 자연어 지시를 따를 수 있습니다. OmniVLA는 다양한 모달리티에서 전문 모델을 능가하며, 새로운 모달리티와 작업에 맞춰 조정할 수 있는 유연한 기반을 제공합니다. 이 모델은 범용적이고 유연한 내비게이션 정책 개발에 기여할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. 인간은 다양한 목표 사양을 유연하게 해석하고 조합할 수 있지만, 대부분의 로봇 내비게이션 정책은 단일 모달리티에 훈련되어 있어 실제 환경에서의 적응력이 제한적입니다.
- 2. 본 연구에서는 비전 기반 내비게이션을 위한 로봇 기초 모델의 훈련 프레임워크를 제안하여, 모든 모달리티의 목표 조건을 가능하게 합니다.
- 3. 제안된 OmniVLA 모델은 보지 못한 환경에 대한 일반화, 모달리티 부족에 대한 강건성, 새로운 자연어 지시를 따르는 능력을 보여줍니다.
- 4. OmniVLA는 모달리티 전반에 걸쳐 전문화된 기준 모델보다 우수한 성능을 발휘하며, 새로운 모달리티와 작업에 대한 유연한 기초를 제공합니다.
- 5. 연구 결과는 OmniVLA가 광범위하게 일반화 가능하고 유연한 내비게이션 정책을 위한 중요한 진전을 제공하며, 모든 모달리티를 아우르는 로봇 기초 모델 구축을 위한 확장 가능한 경로를 제시합니다.


---

*Generated on 2025-09-25 16:55:15*