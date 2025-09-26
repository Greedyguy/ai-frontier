---
keywords:
  - Text-to-Image Models
  - Large Language Model
  - Action Depiction
  - Knowledge Distillation
  - Temporal Details
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16141
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:22:13.008154",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Image Models",
    "Large Language Model",
    "Action Depiction",
    "Knowledge Distillation",
    "Temporal Details"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Image Models": 0.8,
    "Large Language Model": 0.7,
    "Action Depiction": 0.75,
    "Knowledge Distillation": 0.78,
    "Temporal Details": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Text-to-Image models",
        "canonical": "Text-to-Image Models",
        "aliases": [
          "T2I models"
        ],
        "category": "unique_technical",
        "rationale": "Text-to-Image models are central to the paper's focus on action depiction and image generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are used for knowledge distillation, enhancing the connectivity with existing NLP frameworks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "action depiction",
        "canonical": "Action Depiction",
        "aliases": [
          "depiction of actions"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the challenges in accurately rendering complex scenes in T2I models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "knowledge distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [
          "distillation of knowledge"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge distillation is employed to improve T2I models, linking it to broader machine learning techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "temporal details",
        "canonical": "Temporal Details",
        "aliases": [
          "time-based details"
        ],
        "category": "unique_technical",
        "rationale": "Incorporating temporal details is highlighted as a significant improvement for image generation accuracy.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "evaluation",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Text-to-Image models",
      "resolved_canonical": "Text-to-Image Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "action depiction",
      "resolved_canonical": "Action Depiction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "knowledge distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "temporal details",
      "resolved_canonical": "Temporal Details",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models

**Korean Title:** AcT2I: 텍스트-이미지 모델에서 행동 묘사를 평가하고 개선하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16141.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16141](https://arxiv.org/abs/2509.16141)

## 🔗 유사한 논문
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (87.2% similar)
- [[2025-09-22/Structured Information for Improving Spatial Relationships in Text-to-Image Generation_20250922|Structured Information for Improving Spatial Relationships in Text-to-Image Generation]] (85.9% similar)
- [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER: A Causal Cure for Brand-Obsessed Text-to-Image Models]] (84.6% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (82.9% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Distillation|Knowledge Distillation]]
**⚡ Unique Technical**: [[keywords/Text-to-Image Models|Text-to-Image Models]], [[keywords/Action Depiction|Action Depiction]], [[keywords/Temporal Details|Temporal Details]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16141v1 Announce Type: new 
Abstract: Text-to-Image (T2I) models have recently achieved remarkable success in generating images from textual descriptions. However, challenges still persist in accurately rendering complex scenes where actions and interactions form the primary semantic focus. Our key observation in this work is that T2I models frequently struggle to capture nuanced and often implicit attributes inherent in action depiction, leading to generating images that lack key contextual details. To enable systematic evaluation, we introduce AcT2I, a benchmark designed to evaluate the performance of T2I models in generating images from action-centric prompts. We experimentally validate that leading T2I models do not fare well on AcT2I. We further hypothesize that this shortcoming arises from the incomplete representation of the inherent attributes and contextual dependencies in the training corpora of existing T2I models. We build upon this by developing a training-free, knowledge distillation technique utilizing Large Language Models to address this limitation. Specifically, we enhance prompts by incorporating dense information across three dimensions, observing that injecting prompts with temporal details significantly improves image generation accuracy, with our best model achieving an increase of 72%. Our findings highlight the limitations of current T2I methods in generating images that require complex reasoning and demonstrate that integrating linguistic knowledge in a systematic way can notably advance the generation of nuanced and contextually accurate images.

## 🔍 Abstract (한글 번역)

arXiv:2509.16141v1 발표 유형: 신규  
초록: 텍스트-이미지(T2I) 모델은 최근 텍스트 설명으로부터 이미지를 생성하는 데 있어 놀라운 성공을 거두었습니다. 그러나, 행동과 상호작용이 주요 의미적 초점을 이루는 복잡한 장면을 정확하게 렌더링하는 데에는 여전히 도전 과제가 남아 있습니다. 본 연구에서의 주요 관찰은 T2I 모델이 행동 묘사에 내재된 미묘하고 종종 암묵적인 속성을 포착하는 데 자주 어려움을 겪어, 주요 맥락적 세부사항이 결여된 이미지를 생성하게 된다는 점입니다. 체계적인 평가를 가능하게 하기 위해, 우리는 행동 중심의 프롬프트로부터 이미지를 생성하는 T2I 모델의 성능을 평가하기 위한 벤치마크인 AcT2I를 도입합니다. 실험적으로 우리는 주요 T2I 모델들이 AcT2I에서 좋은 성과를 내지 못한다는 것을 검증합니다. 우리는 이러한 단점이 기존 T2I 모델의 훈련 코퍼스에서 내재된 속성과 맥락적 의존성의 불완전한 표현에서 기인한다고 가설을 세웁니다. 이를 바탕으로 우리는 대형 언어 모델을 활용한 훈련 없는 지식 증류 기법을 개발하여 이 한계를 해결합니다. 구체적으로, 우리는 세 가지 차원에 걸쳐 밀집된 정보를 통합하여 프롬프트를 강화하며, 시간적 세부사항을 주입함으로써 이미지 생성 정확도가 크게 향상됨을 관찰하였고, 우리의 최적 모델은 72%의 증가를 달성했습니다. 우리의 연구 결과는 복잡한 추론이 필요한 이미지를 생성하는 데 있어 현재 T2I 방법의 한계를 강조하며, 체계적인 방식으로 언어적 지식을 통합하는 것이 미묘하고 맥락적으로 정확한 이미지 생성에 상당한 발전을 가져올 수 있음을 보여줍니다.

## 📝 요약

최근 텍스트-이미지(T2I) 모델은 텍스트 설명을 기반으로 이미지를 생성하는 데 큰 성공을 거두었습니다. 그러나 복잡한 장면에서의 행동과 상호작용을 정확히 표현하는 데 어려움이 있습니다. 본 연구에서는 T2I 모델이 행동 묘사에 내재된 미묘한 속성을 잘 포착하지 못해 중요한 맥락적 세부사항이 부족한 이미지를 생성한다는 점을 발견했습니다. 이를 평가하기 위해 행동 중심의 프롬프트를 사용한 이미지 생성 성능을 측정하는 AcT2I 벤치마크를 도입했습니다. 실험 결과, 주요 T2I 모델들이 AcT2I에서 좋은 성과를 내지 못했으며, 이는 기존 T2I 모델의 훈련 데이터에서 속성과 맥락적 의존성이 불완전하게 표현되었기 때문이라고 가설을 세웠습니다. 이를 해결하기 위해 대형 언어 모델을 활용한 훈련 없는 지식 증류 기법을 개발했습니다. 특히, 프롬프트에 시간적 세부사항을 포함시켜 이미지 생성 정확도를 72% 향상시켰습니다. 우리의 연구는 현재 T2I 방법의 한계를 보여주며, 체계적인 언어 지식 통합이 복잡하고 맥락적으로 정확한 이미지 생성에 크게 기여할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. Text-to-Image(T2I) 모델은 복잡한 장면의 동작과 상호작용을 정확히 표현하는 데 어려움을 겪고 있습니다.
- 2. AcT2I라는 벤치마크를 도입하여 동작 중심의 프롬프트에서 T2I 모델의 성능을 평가합니다.
- 3. 기존 T2I 모델의 학습 데이터가 내재된 속성과 맥락적 의존성을 충분히 표현하지 못해 성능이 저하된다고 가정합니다.
- 4. 대형 언어 모델을 활용한 지식 증류 기법을 통해 프롬프트에 시간적 정보를 추가하여 이미지 생성 정확도를 72% 향상시켰습니다.
- 5. 언어적 지식을 체계적으로 통합하면 복잡한 추론이 필요한 이미지 생성의 정확성을 크게 개선할 수 있음을 보여줍니다.


---

*Generated on 2025-09-23 12:22:13*