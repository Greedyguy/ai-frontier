---
keywords:
  - Multimodal Learning
  - Pixel-level Visual Reasoning
  - Vision-Language Model
  - Referring Expression Segmentation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18094
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:21:40.182725",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Pixel-level Visual Reasoning",
    "Vision-Language Model",
    "Referring Expression Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Pixel-level Visual Reasoning": 0.78,
    "Vision-Language Model": 0.79,
    "Referring Expression Segmentation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Multi-modal Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "LMMs",
          "Large Multimodal Models"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of integrating multiple data types, which is central to the paper's approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pixel-level Visual Reasoning",
        "canonical": "Pixel-level Visual Reasoning",
        "aliases": [
          "Pixel-level Reasoning",
          "Fine-grained Visual Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach within the field, focusing on detailed visual analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Understanding",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Integration"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the intersection of visual and language processing, crucial for the paper's methodology.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Referring Expression Segmentation",
        "canonical": "Referring Expression Segmentation",
        "aliases": [
          "Referring Segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "A specific task that aligns with the paper's focus on integrating segmentation and language.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
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
      "candidate_surface": "Large Multi-modal Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pixel-level Visual Reasoning",
      "resolved_canonical": "Pixel-level Visual Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Understanding",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Referring Expression Segmentation",
      "resolved_canonical": "Referring Expression Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# UniPixel: Unified Object Referring and Segmentation for Pixel-Level Visual Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18094.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18094](https://arxiv.org/abs/2509.18094)

## 🔗 유사한 논문
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (83.8% similar)
- [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (83.7% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (83.4% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.4% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Referring Expression Segmentation|Referring Expression Segmentation]]
**⚡ Unique Technical**: [[keywords/Pixel-level Visual Reasoning|Pixel-level Visual Reasoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18094v1 Announce Type: cross 
Abstract: Recent advances in Large Multi-modal Models (LMMs) have demonstrated their remarkable success as general-purpose multi-modal assistants, with particular focuses on holistic image- and video-language understanding. Conversely, less attention has been given to scaling fine-grained pixel-level understanding capabilities, where the models are expected to realize pixel-level alignment between visual signals and language semantics. Some previous studies have applied LMMs to related tasks such as region-level captioning and referring expression segmentation. However, these models are limited to performing either referring or segmentation tasks independently and fail to integrate these fine-grained perception capabilities into visual reasoning. To bridge this gap, we propose UniPixel, a large multi-modal model capable of flexibly comprehending visual prompt inputs and generating mask-grounded responses. Our model distinguishes itself by seamlessly integrating pixel-level perception with general visual understanding capabilities. Specifically, UniPixel processes visual prompts and generates relevant masks on demand, and performs subsequent reasoning conditioning on these intermediate pointers during inference, thereby enabling fine-grained pixel-level reasoning. The effectiveness of our approach has been verified on 10 benchmarks across a diverse set of tasks, including pixel-level referring/segmentation and object-centric understanding in images/videos. A novel PixelQA task that jointly requires referring, segmentation, and question answering is also designed to verify the flexibility of our method.

## 📝 요약

최근 대규모 멀티모달 모델(LMMs)의 발전은 이미지 및 비디오-언어 이해에서 큰 성공을 거두었지만, 세밀한 픽셀 수준의 이해 능력 확장에는 상대적으로 덜 주목받았습니다. 이를 해결하기 위해 UniPixel이라는 모델을 제안합니다. UniPixel은 시각적 프롬프트를 유연하게 이해하고 마스크 기반의 응답을 생성할 수 있는 대규모 멀티모달 모델로, 픽셀 수준의 인식과 일반적인 시각 이해 능력을 통합합니다. 이 모델은 시각적 프롬프트를 처리하고 필요한 마스크를 생성하며, 이를 기반으로 추론을 수행하여 세밀한 픽셀 수준의 추론을 가능하게 합니다. 우리의 접근법은 10개의 다양한 벤치마크에서 효과가 검증되었으며, PixelQA라는 새로운 과제를 통해 모델의 유연성을 확인했습니다.

## 🎯 주요 포인트

- 1. 최근 대규모 멀티모달 모델(LMMs)은 이미지 및 비디오 언어 이해에서 뛰어난 성과를 보였으나, 세밀한 픽셀 수준의 이해 능력 확장에는 상대적으로 적은 관심이 주어졌습니다.
- 2. 기존 연구들은 LMMs를 영역 수준 캡션 생성 및 지시 표현 분할과 같은 관련 작업에 적용했지만, 이러한 모델들은 지시 또는 분할 작업을 독립적으로 수행하는 데 한정되었습니다.
- 3. UniPixel은 시각적 프롬프트 입력을 유연하게 이해하고 마스크 기반 응답을 생성할 수 있는 대규모 멀티모달 모델로, 픽셀 수준의 인식과 일반적인 시각적 이해 능력을 통합합니다.
- 4. UniPixel은 시각적 프롬프트를 처리하고 필요에 따라 관련 마스크를 생성하며, 추론 중 이러한 중간 포인터를 기반으로 세밀한 픽셀 수준의 추론을 수행합니다.
- 5. 우리의 접근 방식은 10개의 다양한 작업 벤치마크에서 그 효과가 검증되었으며, PixelQA라는 새로운 작업을 통해 지시, 분할, 질문 응답을 통합적으로 요구하는 방법의 유연성을 입증했습니다.


---

*Generated on 2025-09-24 00:21:40*