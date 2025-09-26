---
keywords:
  - Spike-and-wave Discharges
  - Neural Network
  - Moving-average Filter
  - Long-term EEG Monitoring
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19387
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:52:51.185039",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spike-and-wave Discharges",
    "Neural Network",
    "Moving-average Filter",
    "Long-term EEG Monitoring"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Spike-and-wave Discharges": 0.85,
    "Neural Network": 0.78,
    "Moving-average Filter": 0.72,
    "Long-term EEG Monitoring": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spike-and-wave discharges",
        "canonical": "Spike-and-wave Discharges",
        "aliases": [
          "SWD",
          "spike-wave discharges"
        ],
        "category": "unique_technical",
        "rationale": "Key term specific to absence epilepsy, crucial for linking epilepsy-related research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Artificial Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "ANN"
        ],
        "category": "broad_technical",
        "rationale": "Core component of the detection pipeline, connects to broader neural network research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Two-sided moving-average filter",
        "canonical": "Moving-average Filter",
        "aliases": [
          "MA filter"
        ],
        "category": "unique_technical",
        "rationale": "Specific signal processing technique used in the pipeline, relevant for EEG signal analysis.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Long-term EEG",
        "canonical": "Long-term EEG Monitoring",
        "aliases": [
          "extended EEG recordings"
        ],
        "category": "specific_connectable",
        "rationale": "Focus of the study, essential for connecting with other EEG monitoring research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
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
      "candidate_surface": "Spike-and-wave discharges",
      "resolved_canonical": "Spike-and-wave Discharges",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Artificial Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Two-sided moving-average filter",
      "resolved_canonical": "Moving-average Filter",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Long-term EEG",
      "resolved_canonical": "Long-term EEG Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Hybrid Pipeline SWD Detection in Long-Term EEG Signals

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19387.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19387](https://arxiv.org/abs/2509.19387)

## 🔗 유사한 논문
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (82.9% similar)
- [[2025-09-24/Multi-Scale Graph Theoretical Analysis of Resting-State fMRI for Classification of Alzheimer's Disease, Mild Cognitive Impairment, and Healthy Controls_20250924|Multi-Scale Graph Theoretical Analysis of Resting-State fMRI for Classification of Alzheimer's Disease, Mild Cognitive Impairment, and Healthy Controls]] (82.8% similar)
- [[2025-09-25/A Spatio-Temporal Feature Fusion EEG Virtual Channel Signal Generation Network and Its Application in Anxiety Assessment_20250925|A Spatio-Temporal Feature Fusion EEG Virtual Channel Signal Generation Network and Its Application in Anxiety Assessment]] (81.2% similar)
- [[2025-09-25/Online Adaptation via Dual-Stage Alignment and Self-Supervision for Fast-Calibration Brain-Computer Interfaces_20250925|Online Adaptation via Dual-Stage Alignment and Self-Supervision for Fast-Calibration Brain-Computer Interfaces]] (81.0% similar)
- [[2025-09-25/Closed-loop control of seizure activity via real-time seizure forecasting by reservoir neuromorphic computing_20250925|Closed-loop control of seizure activity via real-time seizure forecasting by reservoir neuromorphic computing]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Long-term EEG Monitoring|Long-term EEG Monitoring]]
**⚡ Unique Technical**: [[keywords/Spike-and-wave Discharges|Spike-and-wave Discharges]], [[keywords/Moving-average Filter|Moving-average Filter]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19387v1 Announce Type: cross 
Abstract: Spike-and-wave discharges (SWDs) are the electroencephalographic hallmark of absence epilepsy, yet their manual identification in multi-day recordings remains labour-intensive and error-prone. We present a lightweight hybrid pipeline that couples analytical features with a shallow artificial neural network (ANN) for accurate, patient-specific SWD detection in long-term, monopolar EEG. A two-sided moving-average (MA) filter first suppresses the high-frequency components of normal background activity. The residual signal is then summarised by the mean and the standard deviation of its normally distributed samples, yielding a compact, two-dimensional feature vector for every 20s window. These features are fed to a single-hidden-layer ANN trained via back-propagation to classify each window as SWD or non-SWD. The method was evaluated on 780 channels sampled at 256 Hz from 12 patients, comprising 392 annotated SWD events. It correctly detected 384 events (sensitivity: 98%) while achieving a specificity of 96.2 % and an overall accuracy of 97.2%. Because feature extraction is analytic, and the classifier is small, the pipeline runs in real-time and requires no manual threshold tuning. These results indicate that normal-distribution descriptors combined with a modest ANN provide an effective and computationally inexpensive solution for automated SWD screening in extended EEG recordings.

## 📝 요약

이 논문은 결여 간질의 전형적인 뇌파인 스파이크-웨이브 방전을 자동으로 식별하기 위한 경량 하이브리드 파이프라인을 제안합니다. 이 방법은 분석적 특징과 얕은 인공 신경망(ANN)을 결합하여 장기간의 단극 EEG에서 환자 맞춤형 SWD를 정확히 탐지합니다. 고주파 성분을 억제하는 양방향 이동 평균 필터를 사용하여 20초마다 평균과 표준 편차로 요약된 2차원 특징 벡터를 생성합니다. 이 벡터는 단일 은닉층 ANN에 입력되어 SWD 여부를 분류합니다. 12명의 환자, 780개의 채널에서 평가한 결과, 98%의 민감도와 96.2%의 특이도로 97.2%의 정확도를 달성했습니다. 이 파이프라인은 실시간으로 작동하며 수동 임계값 조정이 필요하지 않아, 장기 EEG 기록에서 SWD 자동 스크리닝에 효과적이고 계산 비용이 적습니다.

## 🎯 주요 포인트

- 1. 본 연구는 absence epilepsy의 특징인 spike-and-wave discharges(SWDs)를 자동으로 감지하기 위한 경량 하이브리드 파이프라인을 제안합니다.
- 2. 제안된 방법은 양측 이동 평균(MA) 필터를 사용하여 고주파수 성분을 억제하고, 잔여 신호를 요약하여 2차원 특징 벡터를 생성합니다.
- 3. 단층 인공 신경망(ANN)을 통해 각 윈도우를 SWD 또는 비-SWD로 분류하며, 98%의 민감도와 96.2%의 특이도로 높은 정확도를 달성했습니다.
- 4. 특징 추출이 분석적이며 분류기가 작기 때문에, 이 파이프라인은 실시간으로 작동하며 수동 임계값 조정이 필요하지 않습니다.
- 5. 이 연구는 정상 분포 기술자와 소규모 ANN의 결합이 장기 EEG 기록에서 SWD를 자동으로 스크리닝하는 효과적이고 계산 비용이 적은 솔루션을 제공함을 보여줍니다.


---

*Generated on 2025-09-25 16:52:51*