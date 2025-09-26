---
keywords:
  - Self-supervised Learning
  - Abnormal Sound Detection
  - Data Augmentation
  - High-Frequency Information
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15570
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:04:54.019538",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Abnormal Sound Detection",
    "Data Augmentation",
    "High-Frequency Information"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Abnormal Sound Detection": 0.7,
    "Data Augmentation": 0.65,
    "High-Frequency Information": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a form of self-supervised learning, which is crucial for linking concepts in unsupervised anomaly detection.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Abnormal Sound Detection",
        "canonical": "Abnormal Sound Detection",
        "aliases": [
          "Anomaly Sound Detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that can connect to broader anomaly detection and audio processing concepts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Data Augmentation",
        "canonical": "Data Augmentation",
        "aliases": [
          "Data Augmentation"
        ],
        "category": "broad_technical",
        "rationale": "Data augmentation is a fundamental technique in machine learning, relevant to improving model robustness.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "High-Frequency Information",
        "canonical": "High-Frequency Information",
        "aliases": [
          "High-Frequency Data"
        ],
        "category": "unique_technical",
        "rationale": "Focusing on high-frequency information is a unique aspect of the proposed method, relevant for distinguishing normal and anomalous sounds.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "model",
      "method",
      "dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Abnormal Sound Detection",
      "resolved_canonical": "Abnormal Sound Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Data Augmentation",
      "resolved_canonical": "Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "High-Frequency Information",
      "resolved_canonical": "High-Frequency Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection

**Korean Title:** 비정상 소리 탐지에서 스펙트럼 정보 증강을 활용한 대조 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15570.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15570](https://arxiv.org/abs/2509.15570)

## 🔗 유사한 논문
- [[2025-09-22/Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training_20250922|Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training]] (83.6% similar)
- [[2025-09-18/AnoF-Diff_ One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use_20250918|AnoF-Diff: One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use]] (81.0% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (79.9% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (79.1% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Data Augmentation|Data Augmentation]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Abnormal Sound Detection|Abnormal Sound Detection]], [[keywords/High-Frequency Information|High-Frequency Information]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15570v1 Announce Type: cross 
Abstract: The outlier exposure method is an effective approach to address the unsupervised anomaly sound detection problem. The key focus of this method is how to make the model learn the distribution space of normal data. Based on biological perception and data analysis, it is found that anomalous audio and noise often have higher frequencies. Therefore, we propose a data augmentation method for high-frequency information in contrastive learning. This enables the model to pay more attention to the low-frequency information of the audio, which represents the normal operational mode of the machine. We evaluated the proposed method on the DCASE 2020 Task 2. The results showed that our method outperformed other contrastive learning methods used on this dataset. We also evaluated the generalizability of our method on the DCASE 2022 Task 2 dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.15570v1 발표 유형: 교차  
초록: 이상치 노출 방법은 비지도 이상 음향 탐지 문제를 해결하는 효과적인 접근법입니다. 이 방법의 주요 초점은 모델이 정상 데이터의 분포 공간을 학습하도록 하는 것입니다. 생물학적 인식과 데이터 분석을 기반으로, 이상 음향과 잡음은 종종 더 높은 주파수를 가진다는 것이 발견되었습니다. 따라서 우리는 대조 학습에서 고주파 정보를 위한 데이터 증강 방법을 제안합니다. 이를 통해 모델이 기계의 정상 작동 모드를 나타내는 오디오의 저주파 정보에 더 많은 주의를 기울일 수 있게 합니다. 우리는 제안된 방법을 DCASE 2020 Task 2에서 평가했습니다. 결과는 이 데이터셋에서 사용된 다른 대조 학습 방법보다 우리의 방법이 더 우수하다는 것을 보여주었습니다. 또한 DCASE 2022 Task 2 데이터셋에서 우리의 방법의 일반화 가능성을 평가했습니다.

## 📝 요약

이 논문은 비지도 이상 음향 탐지 문제를 해결하기 위한 효과적인 방법인 이상치 노출 기법을 다룹니다. 이 방법의 핵심은 모델이 정상 데이터의 분포 공간을 학습하도록 하는 것입니다. 생물학적 인식과 데이터 분석을 통해 이상 음향과 노이즈는 종종 높은 주파수를 가진다는 점을 발견했습니다. 이에 따라 대조 학습에서 고주파 정보를 활용한 데이터 증강 방법을 제안하여, 모델이 기계의 정상 작동 모드를 나타내는 저주파 정보에 더 집중하도록 했습니다. 제안된 방법은 DCASE 2020 Task 2에서 다른 대조 학습 방법보다 우수한 성능을 보였으며, DCASE 2022 Task 2 데이터셋에서도 일반화 가능성을 평가했습니다.

## 🎯 주요 포인트

- 1. 이상치 노출 방법은 비지도 이상 음향 탐지 문제를 해결하는 효과적인 접근법이다.
- 2. 이상 음향과 노이즈는 종종 높은 주파수를 가지므로, 대조 학습에서 고주파 정보를 활용한 데이터 증강 방법을 제안한다.
- 3. 제안된 방법은 모델이 오디오의 저주파 정보에 더 주목하게 하여 기계의 정상 작동 모드를 학습하도록 돕는다.
- 4. DCASE 2020 Task 2 데이터셋에서 제안된 방법이 다른 대조 학습 방법보다 우수한 성능을 보였다.
- 5. DCASE 2022 Task 2 데이터셋에서도 제안된 방법의 일반화 가능성을 평가하였다.


---

*Generated on 2025-09-23 09:04:54*