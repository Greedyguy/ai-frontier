---
keywords:
  - Persona-to-Voice-Attribute
  - Large Language Model
  - Voice Attributes
  - Societal Biases
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.17093
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:52:45.592130",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Persona-to-Voice-Attribute",
    "Large Language Model",
    "Voice Attributes",
    "Societal Biases"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Persona-to-Voice-Attribute": 0.8,
    "Large Language Model": 0.85,
    "Voice Attributes": 0.78,
    "Societal Biases": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Persona-to-Voice-Attribute",
        "canonical": "Persona-to-Voice-Attribute",
        "aliases": [
          "P2VA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for linking persona descriptions to voice synthesis, which is crucial for bridging the gap in TTS systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing knowledge on language models, essential for understanding the context of persona-driven systems.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Voice Attributes",
        "canonical": "Voice Attributes",
        "aliases": [
          "Voice Characteristics"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on converting persona descriptions into specific voice features.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Societal Biases",
        "canonical": "Societal Biases",
        "aliases": [
          "Social Biases"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the impact of biases in LLMs, relevant for ethical considerations in AI development.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
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
      "candidate_surface": "Persona-to-Voice-Attribute",
      "resolved_canonical": "Persona-to-Voice-Attribute",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Voice Attributes",
      "resolved_canonical": "Voice Attributes",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Societal Biases",
      "resolved_canonical": "Societal Biases",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech

**Korean Title:** P2VA: 공정하고 제어 가능한 텍스트-음성 변환을 위한 페르소나 설명을 음성 속성으로 변환하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17093.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.17093](https://arxiv.org/abs/2505.17093)

## 🔗 유사한 논문
- [[2025-09-22/PILOT_ Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting_20250922|PILOT: Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting]] (86.3% similar)
- [[2025-09-22/Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting_20250922|Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting]] (83.6% similar)
- [[2025-09-22/Fed-PISA_ Federated Voice Cloning via Personalized Identity-Style Adaptation_20250922|Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation]] (82.8% similar)
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (80.5% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Voice Attributes|Voice Attributes]]
**⚡ Unique Technical**: [[keywords/Persona-to-Voice-Attribute|Persona-to-Voice-Attribute]]
**🚀 Evolved Concepts**: [[keywords/Societal Biases|Societal Biases]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17093v2 Announce Type: replace-cross 
Abstract: While persona-driven large language models (LLMs) and prompt-based text-to-speech (TTS) systems have advanced significantly, a usability gap arises when users attempt to generate voices matching their desired personas from implicit descriptions. Most users lack specialized knowledge to specify detailed voice attributes, which often leads TTS systems to misinterpret their expectations. To address these gaps, we introduce Persona-to-Voice-Attribute (P2VA), the first framework enabling voice generation automatically from persona descriptions. Our approach employs two strategies: P2VA-C for structured voice attributes, and P2VA-O for richer style descriptions. Evaluation shows our P2VA-C reduces WER by 5% and improves MOS by 0.33 points. To the best of our knowledge, P2VA is the first framework to establish a connection between persona and voice synthesis. In addition, we discover that current LLMs embed societal biases in voice attributes during the conversion process. Our experiments and findings further provide insights into the challenges of building persona-voice systems.

## 🔍 Abstract (한글 번역)

arXiv:2505.17093v2 발표 유형: 교차 대체  
초록: 페르소나 기반의 대형 언어 모델(LLMs)과 프롬프트 기반의 텍스트-음성 변환(TTS) 시스템이 상당히 발전했지만, 사용자가 암묵적인 설명에서 원하는 페르소나에 맞는 음성을 생성하려고 할 때 사용성의 격차가 발생합니다. 대부분의 사용자는 상세한 음성 속성을 지정할 수 있는 전문 지식이 부족하여 TTS 시스템이 그들의 기대를 잘못 해석하는 경우가 많습니다. 이러한 격차를 해결하기 위해, 우리는 페르소나 설명에서 자동으로 음성을 생성할 수 있는 최초의 프레임워크인 Persona-to-Voice-Attribute (P2VA)를 소개합니다. 우리의 접근 방식은 구조화된 음성 속성을 위한 P2VA-C와 더 풍부한 스타일 설명을 위한 P2VA-O라는 두 가지 전략을 사용합니다. 평가 결과, P2VA-C는 WER을 5% 감소시키고 MOS를 0.33점 향상시켰습니다. 우리가 아는 한, P2VA는 페르소나와 음성 합성을 연결하는 최초의 프레임워크입니다. 또한, 현재의 LLM이 변환 과정에서 음성 속성에 사회적 편견을 내포하고 있음을 발견했습니다. 우리의 실험과 발견은 페르소나-음성 시스템 구축의 도전에 대한 통찰력을 제공합니다.

## 📝 요약

이 논문은 사용자들이 원하는 페르소나에 맞는 목소리를 생성하는 데 어려움을 겪는 문제를 해결하기 위해 Persona-to-Voice-Attribute (P2VA)라는 새로운 프레임워크를 제안합니다. P2VA는 페르소나 설명으로부터 자동으로 목소리를 생성하며, 구조화된 음성 속성을 위한 P2VA-C와 풍부한 스타일 설명을 위한 P2VA-O 두 가지 전략을 사용합니다. 평가 결과, P2VA-C는 음성 인식 오류율(WER)을 5% 줄이고, 주관적 평가 점수(MOS)를 0.33점 향상시켰습니다. 이는 페르소나와 음성 합성을 연결하는 최초의 프레임워크로, 현재의 대형 언어 모델(LLM)이 음성 속성 변환 과정에서 사회적 편견을 내포하고 있음을 발견했습니다. 이러한 실험과 발견은 페르소나-음성 시스템 구축의 도전에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. Persona-to-Voice-Attribute (P2VA)는 페르소나 설명으로부터 자동으로 음성을 생성하는 최초의 프레임워크입니다.
- 2. P2VA는 구조화된 음성 속성을 위한 P2VA-C와 풍부한 스타일 설명을 위한 P2VA-O 두 가지 전략을 사용합니다.
- 3. P2VA-C는 음성 인식 오류율(WER)을 5% 감소시키고 주관적 음질 평가(MOS)를 0.33점 향상시킵니다.
- 4. 현재의 대형 언어 모델(LLM)은 음성 속성 변환 과정에서 사회적 편견을 내포하고 있음을 발견했습니다.
- 5. 연구 결과는 페르소나-음성 시스템 구축의 도전 과제에 대한 통찰을 제공합니다.


---

*Generated on 2025-09-23 11:52:45*