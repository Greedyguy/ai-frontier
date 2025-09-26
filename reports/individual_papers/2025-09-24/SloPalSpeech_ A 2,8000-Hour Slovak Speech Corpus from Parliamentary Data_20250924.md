<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:17:36.417593",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automatic Speech Recognition",
    "SloPalSpeech",
    "OpenAI Whisper",
    "Word Error Rate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automatic Speech Recognition": 0.85,
    "SloPalSpeech": 0.78,
    "OpenAI Whisper": 0.8,
    "Word Error Rate": 0.77
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
        "rationale": "ASR is a key technology in the study and development of speech recognition systems, providing a strong link to related research in low-resource languages.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "SloPalSpeech",
        "canonical": "SloPalSpeech",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "SloPalSpeech is a unique dataset specifically designed for Slovak ASR, making it a significant contribution to low-resource language research.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "OpenAI Whisper models",
        "canonical": "OpenAI Whisper",
        "aliases": [
          "Whisper models"
        ],
        "category": "specific_connectable",
        "rationale": "OpenAI Whisper models are prominent in the field of ASR, providing a direct connection to state-of-the-art model fine-tuning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Word Error Rate",
        "canonical": "Word Error Rate",
        "aliases": [
          "WER"
        ],
        "category": "specific_connectable",
        "rationale": "WER is a critical metric for evaluating ASR systems, linking to performance assessment and benchmarking discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.83,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "parliamentary data",
      "training data",
      "model training"
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
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SloPalSpeech",
      "resolved_canonical": "SloPalSpeech",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "OpenAI Whisper models",
      "resolved_canonical": "OpenAI Whisper",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Word Error Rate",
      "resolved_canonical": "Word Error Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.83,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SloPalSpeech: A 2,8000-Hour Slovak Speech Corpus from Parliamentary Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19270.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19270](https://arxiv.org/abs/2509.19270)

## 🔗 유사한 논문
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (83.6% similar)
- [[2025-09-23/SynParaSpeech_ Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding_20250923|SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding]] (83.2% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (81.6% similar)
- [[2025-09-22/Speech Language Models for Under-Represented Languages_ Insights from Wolof_20250922|Speech Language Models for Under-Represented Languages: Insights from Wolof]] (81.3% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/OpenAI Whisper|OpenAI Whisper]], [[keywords/Word Error Rate|Word Error Rate]]
**⚡ Unique Technical**: [[keywords/SloPalSpeech|SloPalSpeech]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19270v1 Announce Type: cross 
Abstract: Automatic Speech Recognition (ASR) for low-resource languages like Slovak is hindered by the scarcity of training data. To address this, we introduce SloPalSpeech, a new, large-scale Slovak ASR dataset containing 2,806 hours of speech from parliamentary proceedings. We developed a robust processing pipeline to align and segment long-form recordings into clean, 30-second audio-transcript pairs suitable for model training. We use this dataset to fine-tune several OpenAI Whisper models (small, medium, large-v3, and large-v3-turbo), achieving significant Word Error Rate (WER) reductions on standard Slovak benchmarks like Common Voice and FLEURS. For instance, the fine-tuned Whisper-small model's WER dropped by up to 70\%, approaching the baseline performance of the much larger Whisper-large-v3 model. To foster future research in low-resource speech recognition, we publicly release the complete SloPalSpeech dataset, the fully segmented transcripts (60 million words), and all our fine-tuned models.

## 📝 요약

이 논문은 저자들이 저자원이 부족한 언어인 슬로바키아어의 자동 음성 인식을 개선하기 위해 SloPalSpeech라는 대규모 ASR 데이터셋을 소개한 연구입니다. 이 데이터셋은 2,806시간의 슬로바키아어 국회 회의 녹음을 포함하며, 이를 통해 긴 녹음을 30초 길이의 깨끗한 오디오-전사 쌍으로 정렬하고 세분화하는 강력한 처리 파이프라인을 개발했습니다. 이 데이터셋을 활용하여 OpenAI의 Whisper 모델들을 미세 조정하였고, Common Voice 및 FLEURS와 같은 슬로바키아어 벤치마크에서 단어 오류율(WER)을 크게 감소시켰습니다. 특히, Whisper-small 모델의 WER은 최대 70% 감소하여 더 큰 Whisper-large-v3 모델의 성능에 근접했습니다. 저자들은 저자원이 부족한 언어의 음성 인식 연구를 촉진하기 위해 SloPalSpeech 데이터셋, 세분화된 전사본, 미세 조정된 모델들을 공개했습니다.

## 🎯 주요 포인트

- 1. SloPalSpeech는 2,806시간의 슬로바키아어 의회 발언을 포함한 대규모 ASR 데이터셋입니다.
- 2. 긴 녹음을 30초 길이의 오디오-전사 쌍으로 정리하는 강력한 처리 파이프라인을 개발했습니다.
- 3. OpenAI Whisper 모델을 SloPalSpeech 데이터셋으로 미세 조정하여 슬로바키아어 벤치마크에서 WER를 크게 감소시켰습니다.
- 4. Whisper-small 모델의 WER이 최대 70% 감소하여 Whisper-large-v3 모델의 성능에 근접했습니다.
- 5. SloPalSpeech 데이터셋, 전사본, 미세 조정된 모델을 공개하여 저자원 언어 음성 인식 연구를 지원합니다.


---

*Generated on 2025-09-24 14:17:36*