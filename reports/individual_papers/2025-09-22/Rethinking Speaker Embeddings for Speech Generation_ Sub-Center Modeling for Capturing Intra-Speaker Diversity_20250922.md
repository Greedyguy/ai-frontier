---
keywords:
  - Speaker Embeddings
  - Voice Conversion
  - Prosodic Expressiveness
  - Sub-Center Modeling
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2407.04291
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:15:01.802202",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Speaker Embeddings",
    "Voice Conversion",
    "Prosodic Expressiveness",
    "Sub-Center Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Speaker Embeddings": 0.75,
    "Voice Conversion": 0.8,
    "Prosodic Expressiveness": 0.78,
    "Sub-Center Modeling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Speaker Embeddings",
        "canonical": "Speaker Embeddings",
        "aliases": [
          "Speaker Representation",
          "Voice Embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Speaker embeddings are central to the paper's approach and are unique in the context of speech generation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Voice Conversion",
        "canonical": "Voice Conversion",
        "aliases": [
          "Speech Conversion",
          "Voice Transformation"
        ],
        "category": "specific_connectable",
        "rationale": "Voice conversion is a specific application area that links to broader speech synthesis research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Prosodic Expressiveness",
        "canonical": "Prosodic Expressiveness",
        "aliases": [
          "Prosody Variations",
          "Speech Prosody"
        ],
        "category": "unique_technical",
        "rationale": "Prosodic expressiveness is a unique aspect of speech that the paper aims to enhance, crucial for naturalness in speech synthesis.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sub-Center Modeling",
        "canonical": "Sub-Center Modeling",
        "aliases": [
          "Multi-Center Embeddings",
          "Sub-Center Approach"
        ],
        "category": "unique_technical",
        "rationale": "Sub-center modeling is a novel approach proposed in the paper, enhancing the capturing of intra-speaker diversity.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Speaker Embeddings",
      "resolved_canonical": "Speaker Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Voice Conversion",
      "resolved_canonical": "Voice Conversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Prosodic Expressiveness",
      "resolved_canonical": "Prosodic Expressiveness",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sub-Center Modeling",
      "resolved_canonical": "Sub-Center Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity

**Korean Title:** 화자 임베딩의 재고를 통한 음성 생성: 화자 내 다양성을 포착하기 위한 서브센터 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2407.04291.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2407.04291](https://arxiv.org/abs/2407.04291)

## 🔗 유사한 논문
- [[2025-09-18/Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation_20250918|Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation]] (84.9% similar)
- [[2025-09-19/Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (81.0% similar)
- [[2025-09-22/The Impact of Automatic Speech Transcription on Speaker Attribution_20250922|The Impact of Automatic Speech Transcription on Speaker Attribution]] (80.0% similar)
- [[2025-09-22/Impact of Phonetics on Speaker Identity in Adversarial Voice Attack_20250922|Impact of Phonetics on Speaker Identity in Adversarial Voice Attack]] (79.8% similar)
- [[2025-09-22/P2VA_ Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech_20250922|P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Voice Conversion|Voice Conversion]]
**⚡ Unique Technical**: [[keywords/Speaker Embeddings|Speaker Embeddings]], [[keywords/Prosodic Expressiveness|Prosodic Expressiveness]], [[keywords/Sub-Center Modeling|Sub-Center Modeling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.04291v3 Announce Type: replace-cross 
Abstract: Modeling the rich prosodic variations inherent in human speech is essential for generating natural-sounding speech. While speaker embeddings are commonly used as conditioning inputs in personalized speech generation, they are typically optimized for speaker recognition, which encourages the loss of intra-speaker variation. This strategy makes them suboptimal for speech generation in terms of modeling the rich variations at the output speech distribution. In this work, we propose a novel speaker embedding network that employs multiple sub-centers per speaker class during training, instead of a single center as in conventional approaches. This sub-center modeling allows the embedding to capture a broader range of speaker-specific variations while maintaining speaker classification performance. We demonstrate the effectiveness of the proposed embeddings on a voice conversion task, showing improved naturalness and prosodic expressiveness in the synthesized speech.

## 🔍 Abstract (한글 번역)

arXiv:2407.04291v3 발표 유형: 교차 교체  
초록: 인간 음성에 내재된 풍부한 운율 변화를 모델링하는 것은 자연스러운 음성을 생성하기 위해 필수적입니다. 화자 임베딩은 개인화된 음성 생성에서 조건 입력으로 일반적으로 사용되지만, 이는 일반적으로 화자 인식을 위해 최적화되어 있어 화자 내 변화를 잃게 만듭니다. 이러한 전략은 출력 음성 분포에서의 풍부한 변화를 모델링하는 측면에서 음성 생성에 비효율적입니다. 본 연구에서는 기존 접근 방식에서의 단일 중심 대신, 훈련 중 화자 클래스당 여러 하위 중심을 사용하는 새로운 화자 임베딩 네트워크를 제안합니다. 이러한 하위 중심 모델링은 화자 분류 성능을 유지하면서도 화자 고유의 다양한 변화를 포착할 수 있도록 합니다. 우리는 제안된 임베딩의 효과를 음성 변환 작업에서 입증하였으며, 합성된 음성에서 자연스러움과 운율 표현력이 향상됨을 보여줍니다.

## 📝 요약

이 논문은 인간 음성의 다양한 운율 변화를 효과적으로 모델링하기 위한 새로운 화자 임베딩 네트워크를 제안합니다. 기존의 화자 임베딩은 화자 인식에 최적화되어 있어 화자 내 변이성을 잃기 쉽습니다. 이를 개선하기 위해, 본 연구는 화자 클래스당 여러 하위 중심을 사용하는 네트워크를 도입하여 더 넓은 범위의 화자 특유 변이를 포착합니다. 제안된 임베딩은 음성 변환 작업에서 자연스러움과 운율 표현력을 향상시키는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 인간 음성의 풍부한 운율 변화를 모델링하는 것은 자연스러운 음성 생성을 위해 필수적이다.
- 2. 기존의 화자 임베딩은 화자 인식을 위해 최적화되어 있어 화자 내 변이 손실을 초래한다.
- 3. 본 연구에서는 화자 클래스당 여러 개의 하위 중심을 사용하는 새로운 화자 임베딩 네트워크를 제안한다.
- 4. 제안된 임베딩은 화자 분류 성능을 유지하면서 화자 특유의 다양한 변이를 포착할 수 있다.
- 5. 음성 변환 작업에서 제안된 임베딩의 효과를 입증하며, 합성된 음성의 자연스러움과 운율 표현력이 향상되었다.


---

*Generated on 2025-09-23 11:15:01*