---
keywords:
  - Text-to-Image Synthesis
  - Attribute-Specific Image Prompting
  - Diffusion Model
  - Compositional Control
  - Cross-Reference Training Strategy
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.18092
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:08:47.604882",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Image Synthesis",
    "Attribute-Specific Image Prompting",
    "Diffusion Model",
    "Compositional Control",
    "Cross-Reference Training Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Image Synthesis": 0.82,
    "Attribute-Specific Image Prompting": 0.79,
    "Diffusion Model": 0.8,
    "Compositional Control": 0.77,
    "Cross-Reference Training Strategy": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text-to-image synthesis",
        "canonical": "Text-to-Image Synthesis",
        "aliases": [
          "text-to-image generation"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's focus on generating images from textual descriptions, making it a key linkable topic.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "attribute-specific image prompting",
        "canonical": "Attribute-Specific Image Prompting",
        "aliases": [
          "attribute-based image generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced by the paper, emphasizing control over specific image attributes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "diffusion model",
        "canonical": "Diffusion Model",
        "aliases": [
          "diffusion-based model"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are a fundamental technology used in the paper's methodology, linking to broader machine learning concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "compositional control",
        "canonical": "Compositional Control",
        "aliases": [
          "compositional generation"
        ],
        "category": "unique_technical",
        "rationale": "This term describes the paper's ability to manage multiple visual factors simultaneously, which is a unique feature of the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      },
      {
        "surface": "cross-reference training strategy",
        "canonical": "Cross-Reference Training Strategy",
        "aliases": [
          "cross-reference training"
        ],
        "category": "unique_technical",
        "rationale": "This strategy is a novel contribution of the paper, enhancing the model's ability to handle misaligned inputs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "identity preservation",
      "visual prompts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text-to-image synthesis",
      "resolved_canonical": "Text-to-Image Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "attribute-specific image prompting",
      "resolved_canonical": "Attribute-Specific Image Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "diffusion model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "compositional control",
      "resolved_canonical": "Compositional Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "cross-reference training strategy",
      "resolved_canonical": "Cross-Reference Training Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ComposeMe: Attribute-Specific Image Prompts for Controllable Human Image Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18092.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.18092](https://arxiv.org/abs/2509.18092)

## 🔗 유사한 논문
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (83.9% similar)
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (83.7% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (83.2% similar)
- [[2025-09-23/Stencil_ Subject-Driven Generation with Context Guidance_20250923|Stencil: Subject-Driven Generation with Context Guidance]] (82.7% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Model|Diffusion Model]]
**🔗 Specific Connectable**: [[keywords/Text-to-Image Synthesis|Text-to-Image Synthesis]]
**⚡ Unique Technical**: [[keywords/Attribute-Specific Image Prompting|Attribute-Specific Image Prompting]], [[keywords/Compositional Control|Compositional Control]], [[keywords/Cross-Reference Training Strategy|Cross-Reference Training Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18092v1 Announce Type: new 
Abstract: Generating high-fidelity images of humans with fine-grained control over attributes such as hairstyle and clothing remains a core challenge in personalized text-to-image synthesis. While prior methods emphasize identity preservation from a reference image, they lack modularity and fail to provide disentangled control over specific visual attributes. We introduce a new paradigm for attribute-specific image prompting, in which distinct sets of reference images are used to guide the generation of individual aspects of human appearance, such as hair, clothing, and identity. Our method encodes these inputs into attribute-specific tokens, which are injected into a pre-trained text-to-image diffusion model. This enables compositional and disentangled control over multiple visual factors, even across multiple people within a single image. To promote natural composition and robust disentanglement, we curate a cross-reference training dataset featuring subjects in diverse poses and expressions, and propose a multi-attribute cross-reference training strategy that encourages the model to generate faithful outputs from misaligned attribute inputs while adhering to both identity and textual conditioning. Extensive experiments show that our method achieves state-of-the-art performance in accurately following both visual and textual prompts. Our framework paves the way for more configurable human image synthesis by combining visual prompting with text-driven generation. Webpage is available at: https://snap-research.github.io/composeme/.

## 📝 요약

이 논문은 개인화된 텍스트-이미지 합성에서 인간의 세부 속성에 대한 정교한 제어를 통해 고품질 이미지를 생성하는 새로운 방법을 제안합니다. 기존 방법들은 참조 이미지로부터의 정체성 보존에 중점을 두었지만, 모듈성이 부족하고 특정 시각적 속성에 대한 분리된 제어를 제공하지 못했습니다. 본 연구는 머리 스타일, 의상, 정체성과 같은 인간 외모의 개별 측면을 안내하기 위해 속성별 이미지 프롬프트 방식을 도입합니다. 이 방법은 속성별 토큰을 사전 훈련된 텍스트-이미지 확산 모델에 주입하여 여러 시각적 요소에 대한 조합적이고 분리된 제어를 가능하게 합니다. 다양한 자세와 표정의 주제를 포함한 교차 참조 훈련 데이터셋을 구성하고, 잘못 정렬된 속성 입력으로부터도 충실한 출력을 생성하도록 하는 다중 속성 교차 참조 훈련 전략을 제안합니다. 실험 결과, 본 방법이 시각적 및 텍스트 프롬프트를 정확하게 따르는 데 있어 최첨단 성능을 달성함을 보여줍니다. 이 프레임워크는 시각적 프롬프트와 텍스트 기반 생성을 결합하여 보다 구성 가능한 인간 이미지 합성을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 본 연구는 세분화된 인간 속성 제어가 가능한 고품질 이미지 생성을 목표로 하며, 특히 헤어스타일과 의상과 같은 속성에 대한 세밀한 제어를 가능하게 합니다.
- 2. 기존 방법의 모듈성 부족과 특정 시각적 속성에 대한 분리된 제어의 한계를 극복하기 위해, 속성별 이미지 프롬프트 방식을 도입하여 개별 속성에 대한 참조 이미지를 사용합니다.
- 3. 제안된 방법은 속성별 토큰을 사전 학습된 텍스트-이미지 확산 모델에 주입하여, 여러 시각적 요소에 대한 조합적이고 분리된 제어를 가능하게 합니다.
- 4. 다양한 포즈와 표정을 가진 주제를 포함한 교차 참조 학습 데이터셋을 통해 자연스러운 구성과 강력한 분리를 촉진하며, 다중 속성 교차 참조 학습 전략을 제안합니다.
- 5. 실험 결과, 제안된 방법은 시각적 및 텍스트적 프롬프트를 정확하게 따르는 데 있어 최첨단 성능을 달성하며, 시각적 프롬프트와 텍스트 기반 생성을 결합하여 인간 이미지 합성을 보다 구성 가능하게 합니다.


---

*Generated on 2025-09-24 05:08:47*