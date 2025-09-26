---
keywords:
  - Automatic Speech Recognition
  - Speaker Attribution
  - Transcription Errors
  - Human-Transcribed Data
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2507.08660
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:21:09.467022",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automatic Speech Recognition",
    "Speaker Attribution",
    "Transcription Errors",
    "Human-Transcribed Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automatic Speech Recognition": 0.85,
    "Speaker Attribution": 0.78,
    "Transcription Errors": 0.77,
    "Human-Transcribed Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Automatic Speech Recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is central to the study and connects with broader fields like Natural Language Processing and Machine Learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.85
      },
      {
        "surface": "Speaker Attribution",
        "canonical": "Speaker Attribution",
        "aliases": [
          "Speaker Identification"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical term central to the paper's focus on identifying speakers from transcripts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transcription Errors",
        "canonical": "Transcription Errors",
        "aliases": [
          "ASR Errors",
          "Speech Recognition Errors"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding errors in transcription is crucial for improving ASR systems and speaker attribution.",
        "novelty_score": 0.58,
        "connectivity_score": 0.72,
        "specificity_score": 0.69,
        "link_intent_score": 0.77
      },
      {
        "surface": "Human-Transcribed Data",
        "canonical": "Human-Transcribed Data",
        "aliases": [
          "Manual Transcription"
        ],
        "category": "specific_connectable",
        "rationale": "Contrasting human and ASR transcriptions provides insights into the effectiveness of different transcription methods.",
        "novelty_score": 0.61,
        "connectivity_score": 0.7,
        "specificity_score": 0.73,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "study",
      "impact"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Automatic Speech Recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Speaker Attribution",
      "resolved_canonical": "Speaker Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transcription Errors",
      "resolved_canonical": "Transcription Errors",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.72,
        "specificity": 0.69,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Human-Transcribed Data",
      "resolved_canonical": "Human-Transcribed Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.61,
        "connectivity": 0.7,
        "specificity": 0.73,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# The Impact of Automatic Speech Transcription on Speaker Attribution

**Korean Title:** 자동 음성 전사가 화자 귀속에 미치는 영향

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.08660.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2507.08660](https://arxiv.org/abs/2507.08660)

## 🔗 유사한 논문
- [[2025-09-22/Impact of Phonetics on Speaker Identity in Adversarial Voice Attack_20250922|Impact of Phonetics on Speaker Identity in Adversarial Voice Attack]] (82.8% similar)
- [[2025-09-19/Listening, Imagining \& Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (80.2% similar)
- [[2025-09-18/Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation_20250918|Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation]] (80.1% similar)
- [[2025-09-22/Rethinking Speaker Embeddings for Speech Generation_ Sub-Center Modeling for Capturing Intra-Speaker Diversity_20250922|Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity]] (80.0% similar)
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/Transcription Errors|Transcription Errors]], [[keywords/Human-Transcribed Data|Human-Transcribed Data]]
**⚡ Unique Technical**: [[keywords/Speaker Attribution|Speaker Attribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.08660v2 Announce Type: replace-cross 
Abstract: Speaker attribution from speech transcripts is the task of identifying a speaker from the transcript of their speech based on patterns in their language use. This task is especially useful when the audio is unavailable (e.g. deleted) or unreliable (e.g. anonymized speech). Prior work in this area has primarily focused on the feasibility of attributing speakers using transcripts produced by human annotators. However, in real-world settings, one often only has more errorful transcripts produced by automatic speech recognition (ASR) systems. In this paper, we conduct what is, to our knowledge, the first comprehensive study of the impact of automatic transcription on speaker attribution performance. In particular, we study the extent to which speaker attribution performance degrades in the face of transcription errors, as well as how properties of the ASR system impact attribution. We find that attribution is surprisingly resilient to word-level transcription errors and that the objective of recovering the true transcript is minimally correlated with attribution performance. Overall, our findings suggest that speaker attribution on more errorful transcripts produced by ASR is as good, if not better, than attribution based on human-transcribed data, possibly because ASR transcription errors can capture speaker-specific features revealing of speaker identity.

## 🔍 Abstract (한글 번역)

arXiv:2507.08660v2 발표 유형: 교차 대체  
초록: 음성 전사에서 화자 귀속은 화자의 언어 사용 패턴에 기반하여 그들의 발화 전사에서 화자를 식별하는 작업입니다. 이 작업은 오디오가 사용 불가능하거나(예: 삭제된 경우) 신뢰할 수 없을 때(예: 익명화된 음성) 특히 유용합니다. 이 분야의 이전 연구는 주로 인간 주석자가 작성한 전사를 사용하여 화자를 귀속하는 가능성에 초점을 맞추었습니다. 그러나 실제 환경에서는 종종 자동 음성 인식(ASR) 시스템이 생성한 오류가 많은 전사만을 사용할 수 있습니다. 본 논문에서는 자동 전사가 화자 귀속 성능에 미치는 영향을 포괄적으로 연구한 최초의 연구를 수행합니다. 특히, 전사 오류로 인해 화자 귀속 성능이 어느 정도 저하되는지, ASR 시스템의 속성이 귀속에 어떻게 영향을 미치는지를 연구합니다. 우리는 단어 수준의 전사 오류에 대해 귀속이 놀라울 정도로 탄력적이며, 실제 전사를 복구하는 목표가 귀속 성능과 최소한으로 상관되어 있음을 발견했습니다. 전반적으로, 우리의 연구 결과는 ASR이 생성한 오류가 많은 전사에서의 화자 귀속이 인간이 전사한 데이터에 기반한 귀속보다 좋거나 더 나을 수 있음을 시사합니다. 이는 ASR 전사 오류가 화자 정체성을 드러내는 화자 고유의 특징을 포착할 수 있기 때문일 수 있습니다.

## 📝 요약

이 논문은 음성 기록에서 화자를 식별하는 작업인 화자 귀속을 연구합니다. 특히, 자동 음성 인식(ASR) 시스템이 생성한 오류가 있는 전사본이 화자 귀속 성능에 미치는 영향을 처음으로 포괄적으로 분석합니다. 연구 결과, 단어 수준의 전사 오류에도 불구하고 화자 귀속 성능은 크게 저하되지 않으며, ASR 시스템의 특성이 귀속에 영향을 미친다는 것을 발견했습니다. ASR 전사 오류가 오히려 화자의 고유한 언어적 특징을 포착하여 화자 식별에 도움이 될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 화자 귀속은 화자의 언어 사용 패턴을 기반으로 그들의 발화 기록에서 화자를 식별하는 작업이다.
- 2. 자동 음성 인식(ASR) 시스템으로 생성된 오류가 많은 전사에서도 화자 귀속 성능이 인간 전사에 비해 크게 떨어지지 않는다.
- 3. 단어 수준의 전사 오류에도 불구하고 화자 귀속은 놀라울 정도로 강인한 성능을 보인다.
- 4. ASR 전사 오류가 화자의 정체성을 드러내는 화자 특유의 특징을 포착할 수 있어, 인간 전사보다 더 나은 화자 귀속 성능을 보일 수 있다.
- 5. 진정한 전사를 복구하는 목표는 화자 귀속 성능과 최소한의 상관관계를 가진다.


---

*Generated on 2025-09-23 11:21:09*