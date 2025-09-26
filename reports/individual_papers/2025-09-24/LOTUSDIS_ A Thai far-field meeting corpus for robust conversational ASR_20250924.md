<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:41:55.545371",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Far-Field Automatic Speech Recognition",
    "Whisper Model",
    "Distance-Diverse Training Data",
    "Zero-Shot and Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Far-Field Automatic Speech Recognition": 0.78,
    "Whisper Model": 0.82,
    "Distance-Diverse Training Data": 0.77,
    "Zero-Shot and Fine-Tuning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "far-field conversational ASR",
        "canonical": "Far-Field Automatic Speech Recognition",
        "aliases": [
          "far-field ASR",
          "conversational ASR"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on improving ASR systems for distant speech, which is a niche area in ASR research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Whisper variants",
        "canonical": "Whisper Model",
        "aliases": [
          "Whisper",
          "Whisper ASR"
        ],
        "category": "specific_connectable",
        "rationale": "The Whisper model is a specific ASR model evaluated in the study, relevant for linking to discussions on ASR model performance.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.76,
        "link_intent_score": 0.82
      },
      {
        "surface": "distance-diverse training data",
        "canonical": "Distance-Diverse Training Data",
        "aliases": [
          "distance-varied data",
          "distance diversity"
        ],
        "category": "unique_technical",
        "rationale": "This concept is pivotal for improving ASR robustness, highlighting the importance of varied data in training models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.71,
        "link_intent_score": 0.77
      },
      {
        "surface": "zero-shot and fine-tuned conditions",
        "canonical": "Zero-Shot and Fine-Tuning",
        "aliases": [
          "zero-shot learning",
          "fine-tuning"
        ],
        "category": "specific_connectable",
        "rationale": "These learning paradigms are crucial for understanding the performance benchmarks discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.69,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "microphone types",
      "train, dev, test splits",
      "baseline system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "far-field conversational ASR",
      "resolved_canonical": "Far-Field Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Whisper variants",
      "resolved_canonical": "Whisper Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.76,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "distance-diverse training data",
      "resolved_canonical": "Distance-Diverse Training Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.71,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "zero-shot and fine-tuned conditions",
      "resolved_canonical": "Zero-Shot and Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.69,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LOTUSDIS: A Thai far-field meeting corpus for robust conversational ASR

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18722.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18722](https://arxiv.org/abs/2509.18722)

## 🔗 유사한 논문
- [[2025-09-24/SloPalSpeech_ A 2,8000-Hour Slovak Speech Corpus from Parliamentary Data_20250924|SloPalSpeech: A 2,8000-Hour Slovak Speech Corpus from Parliamentary Data]] (84.1% similar)
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (80.6% similar)
- [[2025-09-23/Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing_20250923|Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing]] (79.8% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (79.8% similar)
- [[2025-09-23/WenetSpeech-Chuan_ A Large-Scale Sichuanese Corpus with Rich Annotation for Dialectal Speech Processing_20250923|WenetSpeech-Chuan: A Large-Scale Sichuanese Corpus with Rich Annotation for Dialectal Speech Processing]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Whisper Model|Whisper Model]], [[keywords/Zero-Shot and Fine-Tuning|Zero-Shot and Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Far-Field Automatic Speech Recognition|Far-Field Automatic Speech Recognition]], [[keywords/Distance-Diverse Training Data|Distance-Diverse Training Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18722v1 Announce Type: new 
Abstract: We present LOTUSDIS, a publicly available Thai meeting corpus designed to advance far-field conversational ASR. The dataset comprises 114 hours of spontaneous, unscripted dialogue collected in 15-20 minute sessions with three participants, where overlapping speech is frequent and natural. Speech was recorded simultaneously by nine independent single-channel devices spanning six microphone types at distances from 0.12 m to 10 m, preserving the authentic effects of reverberation, noise, and device coloration without relying on microphone arrays. We provide standard train, dev, test splits and release a reproducible baseline system. We benchmarked several Whisper variants under zero-shot and fine-tuned conditions. Off-the-shelf models showed strong degradation with distance, confirming a mismatch between pre-training data and Thai far-field speech. Fine-tuning on LOTUSDIS dramatically improved robustness: a Thai Whisper baseline reduced overall WER from 64.3 to 38.3 and far-field WER from 81.6 to 49.5, with especially large gains on the most distant microphones. These results underscore the importance of distance-diverse training data for robust ASR. The corpus is available under CC-BY-SA 4.0. We also release training and evaluation scripts as a baseline system to promote reproducible research in this field.

## 📝 요약

LOTUSDIS는 원거리 대화형 음성 인식(ASR)을 발전시키기 위해 개발된 공개 태국어 회의 코퍼스로, 114시간의 자발적 대화를 포함합니다. 이 데이터는 0.12m에서 10m 거리의 다양한 마이크로 수집되어 자연스러운 반향과 잡음을 보존합니다. 기본 학습, 개발, 테스트 세트를 제공하며, 재현 가능한 기준 시스템을 공개했습니다. 사전 학습 모델은 거리 증가에 따라 성능이 저하되었으나, LOTUSDIS로 미세 조정한 결과, WER이 크게 개선되었습니다. 이 연구는 거리 다양성을 고려한 훈련 데이터의 중요성을 강조합니다. 데이터는 CC-BY-SA 4.0 라이선스로 제공됩니다.

## 🎯 주요 포인트

- 1. LOTUSDIS는 태국어 원거리 대화형 ASR을 발전시키기 위해 설계된 공개된 태국 회의 코퍼스입니다.
- 2. 데이터셋은 114시간의 자발적이고 대본 없는 대화를 포함하며, 3명의 참가자가 15-20분 세션 동안 대화하는 형식으로 수집되었습니다.
- 3. 0.12m에서 10m 거리의 6가지 마이크 유형을 사용하는 9개의 독립적인 단일 채널 장치로 동시에 녹음하여, 반향, 소음 및 장치 색채의 효과를 자연스럽게 보존했습니다.
- 4. LOTUSDIS로 미세 조정한 결과, 태국어 Whisper 모델의 WER이 전반적으로 64.3에서 38.3으로, 원거리 WER이 81.6에서 49.5로 크게 개선되었습니다.
- 5. 이 연구는 다양한 거리의 훈련 데이터가 강력한 ASR을 위해 중요하다는 것을 강조하며, 코퍼스는 CC-BY-SA 4.0 라이선스로 제공됩니다.


---

*Generated on 2025-09-24 15:41:55*