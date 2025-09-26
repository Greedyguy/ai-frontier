<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:18:45.942183",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio-Based Pedestrian Detection",
    "Vehicular Noise",
    "Cross-Dataset Evaluation",
    "Acoustic Context"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Audio-Based Pedestrian Detection": 0.78,
    "Vehicular Noise": 0.72,
    "Cross-Dataset Evaluation": 0.75,
    "Acoustic Context": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "audio-based pedestrian detection",
        "canonical": "Audio-Based Pedestrian Detection",
        "aliases": [
          "pedestrian detection with audio",
          "audio pedestrian recognition"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application of detection technology that can be linked to other research in audio and pedestrian safety.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "vehicular noise",
        "canonical": "Vehicular Noise",
        "aliases": [
          "traffic noise",
          "car noise"
        ],
        "category": "unique_technical",
        "rationale": "Understanding and mitigating vehicular noise is crucial for improving audio-based detection systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "cross-dataset evaluation",
        "canonical": "Cross-Dataset Evaluation",
        "aliases": [
          "dataset comparison",
          "multi-dataset analysis"
        ],
        "category": "specific_connectable",
        "rationale": "This evaluation method is important for validating models across different datasets, enhancing generalization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "acoustic context",
        "canonical": "Acoustic Context",
        "aliases": [
          "sound environment",
          "audio context"
        ],
        "category": "specific_connectable",
        "rationale": "Acoustic context is a key factor in audio processing and can be linked to broader audio analysis research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.73,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "model performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "audio-based pedestrian detection",
      "resolved_canonical": "Audio-Based Pedestrian Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "vehicular noise",
      "resolved_canonical": "Vehicular Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "cross-dataset evaluation",
      "resolved_canonical": "Cross-Dataset Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "acoustic context",
      "resolved_canonical": "Acoustic Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.73,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Audio-Based Pedestrian Detection in the Presence of Vehicular Noise

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19295.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19295](https://arxiv.org/abs/2509.19295)

## 🔗 유사한 논문
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (80.1% similar)
- [[2025-09-22/Semantic Change Detection of Roads and Bridges_ A Fine-grained Dataset and Multimodal Frequency-driven Detector_20250922|Semantic Change Detection of Roads and Bridges: A Fine-grained Dataset and Multimodal Frequency-driven Detector]] (79.9% similar)
- [[2025-09-23/Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models_20250923|Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models]] (79.7% similar)
- [[2025-09-22/Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection_20250922|Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection]] (79.2% similar)
- [[2025-09-17/Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction_20250917|Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Cross-Dataset Evaluation|Cross-Dataset Evaluation]], [[keywords/Acoustic Context|Acoustic Context]]
**⚡ Unique Technical**: [[keywords/Audio-Based Pedestrian Detection|Audio-Based Pedestrian Detection]], [[keywords/Vehicular Noise|Vehicular Noise]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19295v1 Announce Type: cross 
Abstract: Audio-based pedestrian detection is a challenging task and has, thus far, only been explored in noise-limited environments. We present a new dataset, results, and a detailed analysis of the state-of-the-art in audio-based pedestrian detection in the presence of vehicular noise. In our study, we conduct three analyses: (i) cross-dataset evaluation between noisy and noise-limited environments, (ii) an assessment of the impact of noisy data on model performance, highlighting the influence of acoustic context, and (iii) an evaluation of the model's predictive robustness on out-of-domain sounds. The new dataset is a comprehensive 1321-hour roadside dataset. It incorporates traffic-rich soundscapes. Each recording includes 16kHz audio synchronized with frame-level pedestrian annotations and 1fps video thumbnails.

## 📝 요약

이 논문은 차량 소음이 있는 환경에서의 오디오 기반 보행자 검출을 다루며, 새로운 데이터셋과 분석 결과를 제시합니다. 연구는 세 가지 분석을 수행합니다: (i) 소음이 있는 환경과 제한된 환경 간의 교차 데이터셋 평가, (ii) 소음 데이터가 모델 성능에 미치는 영향 평가, (iii) 도메인 외 소리에 대한 모델의 예측 강건성 평가. 새로운 데이터셋은 1321시간의 도로변 녹음으로, 16kHz 오디오와 보행자 주석, 1fps 비디오 썸네일을 포함합니다.

## 🎯 주요 포인트

- 1. 본 연구는 차량 소음이 있는 환경에서의 오디오 기반 보행자 탐지에 대한 새로운 데이터셋과 분석 결과를 제시합니다.
- 2. 소음이 있는 환경과 소음이 제한된 환경 간의 교차 데이터셋 평가를 수행하였습니다.
- 3. 소음 데이터가 모델 성능에 미치는 영향을 평가하고, 음향적 맥락의 영향을 강조하였습니다.
- 4. 모델의 예측 강건성을 도메인 외 소리에 대해 평가하였습니다.
- 5. 새로운 데이터셋은 1321시간의 도로변 데이터셋으로, 16kHz 오디오와 프레임 수준의 보행자 주석 및 1fps 비디오 썸네일을 포함합니다.


---

*Generated on 2025-09-24 14:18:45*