---
keywords:
  - VoXtream
  - Transformer
  - Zero-Shot Learning
  - Streaming Text-to-Speech
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15969
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:55:32.736781",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "VoXtream",
    "Transformer",
    "Zero-Shot Learning",
    "Streaming Text-to-Speech"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "VoXtream": 0.85,
    "Transformer": 0.8,
    "Zero-Shot Learning": 0.78,
    "Streaming Text-to-Speech": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "VoXtream",
        "canonical": "VoXtream",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "VoXtream is the unique name of the system introduced in the paper, which is central to the study.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformer is a foundational model architecture used in the system, relevant for linking to other works using similar architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Zero-Shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key feature of the system, enabling it to operate without prior specific training data.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Streaming Text-to-Speech",
        "canonical": "Streaming Text-to-Speech",
        "aliases": [
          "Streaming TTS"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application focus of the paper, distinguishing it from other TTS systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "real-time use",
      "initial delay",
      "output settings"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "VoXtream",
      "resolved_canonical": "VoXtream",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Zero-Shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Streaming Text-to-Speech",
      "resolved_canonical": "Streaming Text-to-Speech",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency

**Korean Title:** VoXtream: 극도로 낮은 지연 시간을 갖춘 풀 스트림 텍스트-음성 변환

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15969.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15969](https://arxiv.org/abs/2509.15969)

## 🔗 유사한 논문
- [[2025-09-22/FocalCodec-Stream_ Streaming Low-Bitrate Speech Coding via Causal Distillation_20250922|FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation]] (83.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (82.3% similar)
- [[2025-09-22/StreamBridge_ Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant_20250922|StreamBridge: Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant]] (80.8% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (79.8% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/VoXtream|VoXtream]], [[keywords/Streaming Text-to-Speech|Streaming Text-to-Speech]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15969v1 Announce Type: cross 
Abstract: We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.

## 🔍 Abstract (한글 번역)

arXiv:2509.15969v1 발표 유형: 교차  
초록: 우리는 VoXtream을 소개합니다. VoXtream은 첫 단어부터 말을 시작하는 실시간 사용을 위한 완전 자회귀적, 제로샷 스트리밍 텍스트-음성 변환(TTS) 시스템입니다. VoXtream은 단조로운 정렬 방식과 시작 지연을 발생시키지 않는 동적 예측을 사용하여 들어오는 음소를 직접 오디오 토큰으로 매핑합니다. VoXtream은 점진적 음소 변환기, 의미 및 지속 시간 토큰을 예측하는 시간 변환기, 그리고 음향 토큰을 생성하는 깊이 변환기를 중심으로 구축되어, 우리가 알기로는 공개된 스트리밍 TTS 중 가장 낮은 초기 지연을 달성합니다: GPU에서 102 ms. 중간 규모의 9천 시간 코퍼스에서 훈련되었음에도 불구하고, 여러 지표에서 더 큰 기준치를 맞추거나 능가하며, 출력 및 전체 스트리밍 설정 모두에서 경쟁력 있는 품질을 제공합니다. 데모와 코드는 https://herimor.github.io/voxtream에서 확인할 수 있습니다.

## 📝 요약

VoXtream은 실시간 사용을 위한 완전 자회귀적 제로샷 스트리밍 텍스트-음성 변환(TTS) 시스템으로, 첫 단어부터 즉시 발화를 시작합니다. 이 시스템은 단조 정렬 방식과 동적 선행 예측을 사용하여 지연 없이 음소를 오디오 토큰으로 직접 변환합니다. VoXtream은 점진적 음소 변환기, 의미 및 지속 시간 토큰을 예측하는 시간 변환기, 음향 토큰을 생성하는 깊이 변환기로 구성되어 있으며, GPU에서 102ms의 초기 지연을 기록하여 현재 공개된 스트리밍 TTS 중 가장 낮은 지연을 달성했습니다. 9,000시간 규모의 중간 크기 데이터로 학습되었음에도 불구하고, 여러 지표에서 더 큰 기준 모델들과 동등하거나 그 이상의 성능을 보이며, 출력 및 전체 스트리밍 설정에서 경쟁력 있는 품질을 제공합니다. 데모와 코드는 [링크](https://herimor.github.io/voxtream)에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. VoXtream은 실시간 사용을 위한 완전 자회귀적, 제로샷 스트리밍 텍스트-음성 변환(TTS) 시스템으로, 첫 단어부터 즉시 발화를 시작합니다.
- 2. VoXtream은 단조 정렬 방식과 동적 예측을 사용하여 지연 없이 음소를 오디오 토큰으로 직접 변환합니다.
- 3. VoXtream은 GPU에서 102ms의 초기 지연을 달성하며, 이는 공개된 스트리밍 TTS 중 가장 낮은 수준입니다.
- 4. 중간 규모의 9천 시간 코퍼스에서 훈련되었음에도 불구하고, VoXtream은 여러 지표에서 더 큰 기준 모델과 동등하거나 그 이상의 성능을 보여줍니다.
- 5. VoXtream의 데모와 코드는 https://herimor.github.io/voxtream에서 확인할 수 있습니다.


---

*Generated on 2025-09-23 10:55:32*