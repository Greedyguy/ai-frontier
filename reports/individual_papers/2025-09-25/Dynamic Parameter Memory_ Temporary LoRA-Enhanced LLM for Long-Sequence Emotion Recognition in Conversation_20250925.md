---
keywords:
  - Dynamic Parameter Memory
  - Large Language Model
  - Speech Emotion Recognition
  - LoRA Module
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.09076
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:31:24.071336",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamic Parameter Memory",
    "Large Language Model",
    "Speech Emotion Recognition",
    "LoRA Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamic Parameter Memory": 0.78,
    "Large Language Model": 0.85,
    "Speech Emotion Recognition": 0.82,
    "LoRA Module": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dynamic Parameter Memory",
        "canonical": "Dynamic Parameter Memory",
        "aliases": [
          "DPM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel mechanism for emotion encoding in long-sequence audio processing, enhancing connectivity with emotion recognition research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Serves as the backbone for the proposed method, linking to a wide range of language model applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Speech Emotion Recognition",
        "canonical": "Speech Emotion Recognition",
        "aliases": [
          "SER"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, connecting to emotion analysis and recognition fields.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "LoRA Module",
        "canonical": "LoRA Module",
        "aliases": [
          "Low-Rank Adaptation"
        ],
        "category": "unique_technical",
        "rationale": "Key component in the proposed method for temporary memory enhancement, linking to adaptation techniques in neural networks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
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
      "candidate_surface": "Dynamic Parameter Memory",
      "resolved_canonical": "Dynamic Parameter Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Speech Emotion Recognition",
      "resolved_canonical": "Speech Emotion Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "LoRA Module",
      "resolved_canonical": "LoRA Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Dynamic Parameter Memory: Temporary LoRA-Enhanced LLM for Long-Sequence Emotion Recognition in Conversation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.09076.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.09076](https://arxiv.org/abs/2507.09076)

## 🔗 유사한 논문
- [[2025-09-23/EmoGist_ Efficient In-Context Learning for Visual Emotion Understanding_20250923|EmoGist: Efficient In-Context Learning for Visual Emotion Understanding]] (81.5% similar)
- [[2025-09-24/Memory in Large Language Models_ Mechanisms, Evaluation and Evolution_20250924|Memory in Large Language Models: Mechanisms, Evaluation and Evolution]] (81.2% similar)
- [[2025-09-18/MOOM_ Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues_20250918|MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues]] (81.1% similar)
- [[2025-09-24/MemOrb_ A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service_20250924|MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service]] (80.7% similar)
- [[2025-09-25/Affective Computing and Emotional Data_ Challenges and Implications in Privacy Regulations, The AI Act, and Ethics in Large Language Models_20250925|Affective Computing and Emotional Data: Challenges and Implications in Privacy Regulations, The AI Act, and Ethics in Large Language Models]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Speech Emotion Recognition|Speech Emotion Recognition]]
**⚡ Unique Technical**: [[keywords/Dynamic Parameter Memory|Dynamic Parameter Memory]], [[keywords/LoRA Module|LoRA Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09076v2 Announce Type: replace-cross 
Abstract: Recent research has focused on applying speech large language model (SLLM) to improve speech emotion recognition (SER). However, the inherently high frame rate in speech modality severely limits the signal processing and understanding capabilities of SLLM. For example, a SLLM with a 4K context window can only process 80 seconds of audio at 50Hz feature sampling rate before reaching its capacity limit. Input token compression methods used in SLLM overlook the continuity and inertia of emotions across multiple conversation turns. This paper proposes a Dynamic Parameter Memory (DPM) mechanism with contextual semantics and sentence-level emotion encoding, enabling processing of unlimited-length audio with limited context windows in SLLM. Specifically, DPM progressively encodes sentence-level information and emotions into a temporary LoRA module during inference to effectively "memorize" the contextual information. We trained an emotion SLLM as a backbone and incorporated our DPM into inference for emotion recognition in conversation (ERC). Experimental results on the IEMOCAP dataset show that DPM significantly improves the emotion recognition capabilities of SLLM when processing long audio sequences, achieving state-of-the-art performance.

## 📝 요약

최근 연구에서는 음성 대형 언어 모델(SLLM)을 활용하여 음성 감정 인식(SER)을 개선하는 데 중점을 두고 있습니다. 그러나 음성 모달리티의 높은 프레임 속도는 SLLM의 신호 처리 및 이해 능력을 제한합니다. 본 논문에서는 문맥적 의미와 문장 수준의 감정 인코딩을 통해 제한된 컨텍스트 윈도우에서도 무제한 길이의 오디오를 처리할 수 있는 동적 매개변수 메모리(DPM) 메커니즘을 제안합니다. DPM은 추론 중 문장 수준의 정보와 감정을 임시 LoRA 모듈에 점진적으로 인코딩하여 문맥 정보를 효과적으로 "기억"합니다. 우리는 감정 SLLM을 백본으로 훈련하고, 대화 중 감정 인식을 위해 DPM을 통합했습니다. IEMOCAP 데이터셋을 활용한 실험 결과, DPM은 긴 오디오 시퀀스를 처리할 때 SLLM의 감정 인식 능력을 크게 향상시켜 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 최근 연구에서는 음성 대형 언어 모델(SLLM)을 활용하여 음성 감정 인식(SER)을 개선하는 데 중점을 두고 있습니다.
- 2. SLLM의 입력 토큰 압축 방법은 여러 대화 턴에 걸친 감정의 연속성과 관성을 간과하고 있습니다.
- 3. 본 논문에서는 문맥적 의미와 문장 수준의 감정 인코딩을 통해 제한된 컨텍스트 윈도우로 무제한 길이의 오디오를 처리할 수 있는 동적 매개변수 메모리(DPM) 메커니즘을 제안합니다.
- 4. DPM은 문장 수준의 정보와 감정을 임시 LoRA 모듈에 점진적으로 인코딩하여 문맥 정보를 효과적으로 "기억"합니다.
- 5. IEMOCAP 데이터셋에 대한 실험 결과, DPM은 긴 오디오 시퀀스를 처리할 때 SLLM의 감정 인식 능력을 크게 향상시켜 최첨단 성능을 달성했습니다.


---

*Generated on 2025-09-25 16:31:24*