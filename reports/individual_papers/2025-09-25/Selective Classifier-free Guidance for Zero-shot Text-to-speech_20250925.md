---
keywords:
  - Zero-Shot Learning
  - Classifier-Free Guidance
  - Speech Synthesis
  - Speaker Similarity
  - Text Adherence
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19668
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:43:19.627254",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Classifier-Free Guidance",
    "Speech Synthesis",
    "Speaker Similarity",
    "Text Adherence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.88,
    "Classifier-Free Guidance": 0.8,
    "Speech Synthesis": 0.7,
    "Speaker Similarity": 0.78,
    "Text Adherence": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot text-to-speech",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot TTS"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of zero-shot learning, which is crucial for understanding the adaptation of models to new tasks without task-specific training.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Classifier-free guidance",
        "canonical": "Classifier-Free Guidance",
        "aliases": [
          "CFG"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel method applied to speech synthesis, highlighting its adaptation from image generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Speech synthesis",
        "canonical": "Speech Synthesis",
        "aliases": [
          "TTS"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental technology discussed in the paper, connecting to broader topics in audio processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Speaker similarity",
        "canonical": "Speaker Similarity",
        "aliases": [
          "Voice similarity"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for evaluating the effectiveness of text-to-speech systems in maintaining speaker characteristics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Text adherence",
        "canonical": "Text Adherence",
        "aliases": [
          "Content fidelity"
        ],
        "category": "unique_technical",
        "rationale": "Important for assessing how well the synthesized speech follows the given text, a key metric in TTS.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "fidelity",
      "trade-offs",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot text-to-speech",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Classifier-free guidance",
      "resolved_canonical": "Classifier-Free Guidance",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Speech synthesis",
      "resolved_canonical": "Speech Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Speaker similarity",
      "resolved_canonical": "Speaker Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Text adherence",
      "resolved_canonical": "Text Adherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Selective Classifier-free Guidance for Zero-shot Text-to-speech

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19668.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19668](https://arxiv.org/abs/2509.19668)

## 🔗 유사한 논문
- [[2025-09-22/Dynamic Classifier-Free Diffusion Guidance via Online Feedback_20250922|Dynamic Classifier-Free Diffusion Guidance via Online Feedback]] (86.3% similar)
- [[2025-09-23/MaskVCT_ Masked Voice Codec Transformer for Zero-Shot Voice Conversion With Increased Controllability via Multiple Guidances_20250923|MaskVCT: Masked Voice Codec Transformer for Zero-Shot Voice Conversion With Increased Controllability via Multiple Guidances]] (81.6% similar)
- [[2025-09-23/PG-CE_ A Progressive Generation Dataset with Constraint Enhancement for Controllable Text Generation_20250923|PG-CE: A Progressive Generation Dataset with Constraint Enhancement for Controllable Text Generation]] (80.2% similar)
- [[2025-09-23/ComposeMe_ Attribute-Specific Image Prompts for Controllable Human Image Generation_20250923|ComposeMe: Attribute-Specific Image Prompts for Controllable Human Image Generation]] (79.4% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Speech Synthesis|Speech Synthesis]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Speaker Similarity|Speaker Similarity]]
**⚡ Unique Technical**: [[keywords/Classifier-Free Guidance|Classifier-Free Guidance]], [[keywords/Text Adherence|Text Adherence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19668v1 Announce Type: cross 
Abstract: In zero-shot text-to-speech, achieving a balance between fidelity to the target speaker and adherence to text content remains a challenge. While classifier-free guidance (CFG) strategies have shown promising results in image generation, their application to speech synthesis are underexplored. Separating the conditions used for CFG enables trade-offs between different desired characteristics in speech synthesis. In this paper, we evaluate the adaptability of CFG strategies originally developed for image generation to speech synthesis and extend separated-condition CFG approaches for this domain. Our results show that CFG strategies effective in image generation generally fail to improve speech synthesis. We also find that we can improve speaker similarity while limiting degradation of text adherence by applying standard CFG during early timesteps and switching to selective CFG only in later timesteps. Surprisingly, we observe that the effectiveness of a selective CFG strategy is highly text-representation dependent, as differences between the two languages of English and Mandarin can lead to different results even with the same model.

## 📝 요약

이 논문은 제로샷 텍스트-음성 변환에서 목표 화자의 음성 충실도와 텍스트 내용의 일치를 동시에 달성하는 문제를 다룹니다. 이미지 생성에서 유망한 결과를 보인 분류기 없는 가이드(CFG) 전략을 음성 합성에 적용하고, 조건을 분리하여 다양한 특성 간의 균형을 맞추는 방법론을 제안합니다. 연구 결과, 이미지 생성에서 효과적이었던 CFG 전략은 음성 합성에서는 일반적으로 개선 효과가 없음을 발견했습니다. 그러나 초기 단계에서 표준 CFG를 적용하고 후반 단계에서 선택적 CFG로 전환하면 화자 유사성을 개선하면서 텍스트 일치도 저하를 최소화할 수 있음을 확인했습니다. 또한, 선택적 CFG 전략의 효과는 텍스트 표현에 크게 의존하며, 영어와 중국어 간의 차이가 동일한 모델에서도 다른 결과를 초래할 수 있음을 관찰했습니다.

## 🎯 주요 포인트

- 1. 제로샷 텍스트-음성 변환에서 목표 화자의 음성 충실도와 텍스트 내용의 일치성을 균형 있게 유지하는 것이 도전 과제입니다.
- 2. 이미지 생성에서 유망한 결과를 보인 분류기 없는 가이드(CFG) 전략의 음성 합성 적용은 아직 충분히 탐구되지 않았습니다.
- 3. 이미지 생성에 효과적인 CFG 전략은 음성 합성에서는 일반적으로 개선 효과를 보이지 않습니다.
- 4. 초기 단계에서는 표준 CFG를 적용하고 후반 단계에서 선택적 CFG로 전환함으로써 화자 유사성을 개선하면서 텍스트 일치성의 저하를 제한할 수 있습니다.
- 5. 선택적 CFG 전략의 효과는 텍스트 표현에 크게 의존하며, 영어와 중국어 간의 차이가 동일한 모델에서도 다른 결과를 초래할 수 있습니다.


---

*Generated on 2025-09-25 15:43:19*