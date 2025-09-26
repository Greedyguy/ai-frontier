---
keywords:
  - Self-supervised Learning
  - Time Series Classification
  - Bag-of-symbol Representation
  - Data Distribution Shift
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19654
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:38:45.643677",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Time Series Classification",
    "Bag-of-symbol Representation",
    "Data Distribution Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Time Series Classification": 0.75,
    "Bag-of-symbol Representation": 0.78,
    "Data Distribution Shift": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key approach in the paper, aligning with existing concepts for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Time Series Classification",
        "canonical": "Time Series Classification",
        "aliases": [
          "TSC"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving classification in time series data, a unique technical challenge.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Bag-of-symbol Representation",
        "canonical": "Bag-of-symbol Representation",
        "aliases": [
          "BoS Representation"
        ],
        "category": "unique_technical",
        "rationale": "This representation is pivotal for handling data shifts in the study, offering a unique technical insight.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Distribution Shift",
        "canonical": "Data Distribution Shift",
        "aliases": [
          "Distribution Shift"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding and addressing distribution shifts is crucial for model robustness, linking to broader themes in ML.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "methodologies",
      "performance",
      "patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised Learning",
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
      "candidate_surface": "Time Series Classification",
      "resolved_canonical": "Time Series Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Bag-of-symbol Representation",
      "resolved_canonical": "Bag-of-symbol Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Distribution Shift",
      "resolved_canonical": "Data Distribution Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Symbol-Temporal Consistency Self-supervised Learning for Robust Time Series Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19654.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19654](https://arxiv.org/abs/2509.19654)

## 🔗 유사한 논문
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals: Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (82.8% similar)
- [[2025-09-24/A Deep Learning Approach for Spatio-Temporal Forecasting of InSAR Ground Deformation in Eastern Ireland_20250924|A Deep Learning Approach for Spatio-Temporal Forecasting of InSAR Ground Deformation in Eastern Ireland]] (81.4% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (81.4% similar)
- [[2025-09-25/Diffusion-Augmented Contrastive Learning_ A Noise-Robust Encoder for Biosignal Representations_20250925|Diffusion-Augmented Contrastive Learning: A Noise-Robust Encoder for Biosignal Representations]] (81.4% similar)
- [[2025-09-23/TS-P$^2$CL_ Plug-and-Play Dual Contrastive Learning for Vision-Guided Medical Time Series Classification_20250923|TS-P$^2$CL: Plug-and-Play Dual Contrastive Learning for Vision-Guided Medical Time Series Classification]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Data Distribution Shift|Data Distribution Shift]]
**⚡ Unique Technical**: [[keywords/Time Series Classification|Time Series Classification]], [[keywords/Bag-of-symbol Representation|Bag-of-symbol Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19654v1 Announce Type: new 
Abstract: The surge in the significance of time series in digital health domains necessitates advanced methodologies for extracting meaningful patterns and representations. Self-supervised contrastive learning has emerged as a promising approach for learning directly from raw data. However, time series data in digital health is known to be highly noisy, inherently involves concept drifting, and poses a challenge for training a generalizable deep learning model. In this paper, we specifically focus on data distribution shift caused by different human behaviors and propose a self-supervised learning framework that is aware of the bag-of-symbol representation. The bag-of-symbol representation is known for its insensitivity to data warping, location shifts, and noise existed in time series data, making it potentially pivotal in guiding deep learning to acquire a representation resistant to such data shifting. We demonstrate that the proposed method can achieve significantly better performance where significant data shifting exists.

## 📝 요약

이 논문은 디지털 헬스 분야의 시계열 데이터에서 의미 있는 패턴을 추출하기 위한 방법론을 제안합니다. 저자들은 자기 지도 대조 학습을 활용하여 데이터 분포 변화에 대응하는 프레임워크를 개발했습니다. 특히, 인간 행동의 다양성으로 인한 데이터 분포 변화를 고려하여, 데이터 왜곡과 위치 변화, 노이즈에 강한 'bag-of-symbol' 표현을 사용했습니다. 제안된 방법은 이러한 데이터 변화가 있는 상황에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 디지털 헬스 분야의 시계열 데이터는 높은 노이즈와 개념 변화로 인해 일반화 가능한 딥러닝 모델 훈련에 어려움을 겪습니다.
- 2. 본 논문은 인간 행동에 의해 발생하는 데이터 분포 변화에 중점을 두고, 자가 지도 학습 프레임워크를 제안합니다.
- 3. 제안된 프레임워크는 데이터 왜곡, 위치 변화, 노이즈에 민감하지 않은 bag-of-symbol 표현을 활용하여 데이터 변화에 강한 표현을 학습합니다.
- 4. 제안된 방법은 데이터 변화가 큰 상황에서 기존 방법보다 성능이 크게 향상됨을 입증합니다.


---

*Generated on 2025-09-25 16:38:45*