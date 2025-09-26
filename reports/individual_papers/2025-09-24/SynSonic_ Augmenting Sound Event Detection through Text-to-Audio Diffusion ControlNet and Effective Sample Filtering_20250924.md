<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:56:44.298586",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sound Event Detection",
    "Text-to-Audio Diffusion",
    "ControlNet",
    "Polyphonic Sound Detection Scores"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sound Event Detection": 0.8,
    "Text-to-Audio Diffusion": 0.85,
    "ControlNet": 0.75,
    "Polyphonic Sound Detection Scores": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sound Event Detection",
        "canonical": "Sound Event Detection",
        "aliases": [
          "SED"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, it connects with audio processing and machine learning domains.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "text-to-audio diffusion",
        "canonical": "Text-to-Audio Diffusion",
        "aliases": [
          "audio diffusion"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel generative approach specific to audio synthesis, linking to diffusion models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "ControlNet",
        "canonical": "ControlNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific model used in the paper, linking to neural network control techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Polyphonic Sound Detection Scores",
        "canonical": "Polyphonic Sound Detection Scores",
        "aliases": [
          "PSDS1",
          "PSDS2"
        ],
        "category": "unique_technical",
        "rationale": "Key evaluation metric in the paper, connecting to sound detection performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "augmentation",
      "model performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sound Event Detection",
      "resolved_canonical": "Sound Event Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "text-to-audio diffusion",
      "resolved_canonical": "Text-to-Audio Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ControlNet",
      "resolved_canonical": "ControlNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Polyphonic Sound Detection Scores",
      "resolved_canonical": "Polyphonic Sound Detection Scores",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# SynSonic: Augmenting Sound Event Detection through Text-to-Audio Diffusion ControlNet and Effective Sample Filtering

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18603.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18603](https://arxiv.org/abs/2509.18603)

## 🔗 유사한 논문
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (81.9% similar)
- [[2025-09-23/SynParaSpeech_ Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding_20250923|SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding]] (81.8% similar)
- [[2025-09-23/Extract and Diffuse_ Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement_20250923|Extract and Diffuse: Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement]] (81.5% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (81.0% similar)
- [[2025-09-22/Generating Moving 3D Soundscapes with Latent Diffusion Models_20250922|Generating Moving 3D Soundscapes with Latent Diffusion Models]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Sound Event Detection|Sound Event Detection]], [[keywords/Text-to-Audio Diffusion|Text-to-Audio Diffusion]], [[keywords/ControlNet|ControlNet]], [[keywords/Polyphonic Sound Detection Scores|Polyphonic Sound Detection Scores]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18603v1 Announce Type: cross 
Abstract: Data synthesis and augmentation are essential for Sound Event Detection (SED) due to the scarcity of temporally labeled data. While augmentation methods like SpecAugment and Mix-up can enhance model performance, they remain constrained by the diversity of existing samples. Recent generative models offer new opportunities, yet their direct application to SED is challenging due to the lack of precise temporal annotations and the risk of introducing noise through unreliable filtering. To address these challenges and enable generative-based augmentation for SED, we propose SynSonic, a data augmentation method tailored for this task. SynSonic leverages text-to-audio diffusion models guided by an energy-envelope ControlNet to generate temporally coherent sound events. A joint score filtering strategy with dual classifiers ensures sample quality, and we explore its practical integration into training pipelines. Experimental results show that SynSonic improves Polyphonic Sound Detection Scores (PSDS1 and PSDS2), enhancing both temporal localization and sound class discrimination.

## 📝 요약

이 논문은 소리 이벤트 감지(SED)에서 데이터 부족 문제를 해결하기 위해 제안된 SynSonic이라는 데이터 증강 방법을 소개합니다. 기존의 증강 방법들은 샘플 다양성의 한계가 있지만, SynSonic은 텍스트-오디오 변환 확산 모델과 에너지-엔벨로프 ControlNet을 활용하여 시간적으로 일관된 소리 이벤트를 생성합니다. 또한, 이중 분류기를 사용한 공동 점수 필터링 전략을 통해 샘플의 품질을 보장합니다. 실험 결과, SynSonic은 다성 소리 감지 점수(PSDS1 및 PSDS2)를 개선하여 시간적 위치 지정과 소리 클래스 구별 능력을 향상시킵니다.

## 🎯 주요 포인트

- 1. 데이터 합성과 증강은 시간적으로 라벨링된 데이터가 부족한 소리 이벤트 감지(SED)에서 필수적입니다.
- 2. 기존의 증강 방법인 SpecAugment와 Mix-up은 모델 성능을 향상시킬 수 있지만, 기존 샘플의 다양성에 의해 제한됩니다.
- 3. SynSonic은 에너지-엔벨로프 ControlNet으로 안내되는 텍스트-오디오 확산 모델을 활용하여 시간적으로 일관된 소리 이벤트를 생성합니다.
- 4. 이중 분류기를 사용한 공동 점수 필터링 전략을 통해 샘플 품질을 보장하며, 이를 훈련 파이프라인에 통합하는 방법을 탐구합니다.
- 5. 실험 결과 SynSonic이 다성 소리 감지 점수(PSDS1 및 PSDS2)를 개선하여 시간적 위치 지정과 소리 클래스 구별을 향상시킵니다.


---

*Generated on 2025-09-24 13:56:44*