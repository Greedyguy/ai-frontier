---
keywords:
  - Aphasia-Specific Speech Recognition
  - Whisper-Tiny
  - GPT-4 Reference Enhancement
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.06566
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:02:28.758204",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Aphasia-Specific Speech Recognition",
    "Whisper-Tiny",
    "GPT-4 Reference Enhancement",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Aphasia-Specific Speech Recognition": 0.88,
    "Whisper-Tiny": 0.8,
    "GPT-4 Reference Enhancement": 0.85,
    "Zero-Shot Learning": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "aphasia-specific speech recognition",
        "canonical": "Aphasia-Specific Speech Recognition",
        "aliases": [
          "AS-ASR"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel application of speech recognition technology tailored for aphasia, offering a unique link to specialized research in disordered speech.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Whisper-tiny",
        "canonical": "Whisper-Tiny",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "As a specific model variant used in the framework, it provides a link to discussions on lightweight models for edge devices.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "GPT-4-based reference enhancement",
        "canonical": "GPT-4 Reference Enhancement",
        "aliases": [
          "GPT-4 Enhancement"
        ],
        "category": "specific_connectable",
        "rationale": "This technique links to broader discussions on using advanced language models for improving data quality.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Baseline",
        "canonical": "Zero-Shot Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This concept ties into the trending topic of zero-shot learning, which is crucial for understanding model performance without prior specific training.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "standard speech",
      "evaluation settings",
      "supervision quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "aphasia-specific speech recognition",
      "resolved_canonical": "Aphasia-Specific Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Whisper-tiny",
      "resolved_canonical": "Whisper-Tiny",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "GPT-4-based reference enhancement",
      "resolved_canonical": "GPT-4 Reference Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Baseline",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition

**Korean Title:** AS-ASR: 실어증 특화 자동 음성 인식을 위한 경량 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.06566.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.06566](https://arxiv.org/abs/2506.06566)

## 🔗 유사한 논문
- [[2025-09-19/Listening, Imagining \& Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (85.5% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (84.0% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (82.5% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (81.5% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/GPT-4 Reference Enhancement|GPT-4 Reference Enhancement]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Aphasia-Specific Speech Recognition|Aphasia-Specific Speech Recognition]], [[keywords/Whisper-Tiny|Whisper-Tiny]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.06566v2 Announce Type: replace-cross 
Abstract: This paper proposes AS-ASR, a lightweight aphasia-specific speech recognition framework based on Whisper-tiny, tailored for low-resource deployment on edge devices. Our approach introduces a hybrid training strategy that systematically combines standard and aphasic speech at varying ratios, enabling robust generalization, and a GPT-4-based reference enhancement method that refines noisy aphasic transcripts, improving supervision quality. We conduct extensive experiments across multiple data mixing configurations and evaluation settings. Results show that our fine-tuned model significantly outperforms the zero-shot baseline, reducing WER on aphasic speech by over 30% while preserving performance on standard speech. The proposed framework offers a scalable, efficient solution for real-world disordered speech recognition.

## 🔍 Abstract (한글 번역)

arXiv:2506.06566v2 발표 유형: 교차 교체  
초록: 본 논문은 Whisper-tiny를 기반으로 한 경량형 실어증 특화 음성 인식 프레임워크인 AS-ASR을 제안하며, 엣지 디바이스에서의 저자원 배포에 적합하도록 설계되었습니다. 우리의 접근 방식은 표준 음성과 실어증 음성을 다양한 비율로 체계적으로 결합하는 하이브리드 훈련 전략을 도입하여 강력한 일반화를 가능하게 하고, GPT-4 기반의 참조 향상 방법을 통해 잡음이 있는 실어증 전사를 정제하여 감독 품질을 향상시킵니다. 우리는 여러 데이터 혼합 구성 및 평가 설정에서 광범위한 실험을 수행하였습니다. 결과는 미세 조정된 모델이 제로샷 기준선을 크게 능가하며, 실어증 음성의 WER을 30% 이상 감소시키면서 표준 음성의 성능을 유지함을 보여줍니다. 제안된 프레임워크는 실제 환경에서의 장애 음성 인식을 위한 확장 가능하고 효율적인 솔루션을 제공합니다.

## 📝 요약

이 논문은 경량화된 실어증 특화 음성 인식 프레임워크인 AS-ASR을 제안합니다. Whisper-tiny를 기반으로 한 이 프레임워크는 엣지 디바이스에서의 저자원 배포를 목표로 합니다. 제안된 방법은 표준 및 실어증 음성을 다양한 비율로 결합하는 하이브리드 훈련 전략과 GPT-4 기반의 참조 개선 방법을 도입하여, 잡음이 많은 실어증 음성 전사를 개선합니다. 다양한 데이터 혼합 구성과 평가 설정에서의 실험 결과, 미세 조정된 모델이 실어증 음성의 WER을 30% 이상 감소시키면서 표준 음성 성능을 유지하는 것으로 나타났습니다. 이 프레임워크는 실제 환경에서의 장애 음성 인식을 위한 확장 가능하고 효율적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. AS-ASR은 Whisper-tiny 기반의 경량화된 실어증 특화 음성 인식 프레임워크로, 엣지 디바이스에서의 저자원 배포를 목표로 한다.
- 2. 표준 및 실어증 음성을 다양한 비율로 결합하는 하이브리드 훈련 전략을 도입하여 강력한 일반화를 가능하게 한다.
- 3. GPT-4 기반의 참조 향상 방법을 통해 실어증 음성의 잡음이 섞인 전사를 개선하여 감독 품질을 향상시킨다.
- 4. 다양한 데이터 혼합 구성과 평가 설정에서의 실험 결과, 미세 조정된 모델이 제로샷 기준 모델 대비 실어증 음성의 WER을 30% 이상 감소시킨다.
- 5. 제안된 프레임워크는 실제 환경에서의 장애 음성 인식을 위한 확장 가능하고 효율적인 솔루션을 제공한다.


---

*Generated on 2025-09-23 10:02:28*