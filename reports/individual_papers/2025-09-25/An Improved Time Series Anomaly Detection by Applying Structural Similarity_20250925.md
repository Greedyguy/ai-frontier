---
keywords:
  - Time Series Anomaly Detection
  - Structural Similarity
  - Reconstruction-based Methods
  - Pattern-wise Anomalies
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20184
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:01:06.269602",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Time Series Anomaly Detection",
    "Structural Similarity",
    "Reconstruction-based Methods",
    "Pattern-wise Anomalies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Time Series Anomaly Detection": 0.8,
    "Structural Similarity": 0.78,
    "Reconstruction-based Methods": 0.75,
    "Pattern-wise Anomalies": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Time Series Anomaly Detection",
        "canonical": "Time Series Anomaly Detection",
        "aliases": [
          "TS Anomaly Detection",
          "Anomaly Detection in Time Series"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized area within anomaly detection, focusing on time series data, which is central to the paper's contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structural Similarity",
        "canonical": "Structural Similarity",
        "aliases": [
          "Structural Features",
          "Structure-based Similarity"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces structural similarity as a key component for improving anomaly detection, making it a novel concept in this context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reconstruction-based Methods",
        "canonical": "Reconstruction-based Methods",
        "aliases": [
          "Reconstruction Approaches",
          "Data Reconstruction Methods"
        ],
        "category": "specific_connectable",
        "rationale": "Reconstruction-based methods are a common approach in anomaly detection, providing a point of connection with other related works.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Pattern-wise Anomalies",
        "canonical": "Pattern-wise Anomalies",
        "aliases": [
          "Pattern Anomalies",
          "Complex Anomalies"
        ],
        "category": "unique_technical",
        "rationale": "The focus on pattern-wise anomalies differentiates this work from others that may only consider point-wise anomalies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
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
      "candidate_surface": "Time Series Anomaly Detection",
      "resolved_canonical": "Time Series Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structural Similarity",
      "resolved_canonical": "Structural Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reconstruction-based Methods",
      "resolved_canonical": "Reconstruction-based Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Pattern-wise Anomalies",
      "resolved_canonical": "Pattern-wise Anomalies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# An Improved Time Series Anomaly Detection by Applying Structural Similarity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20184.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20184](https://arxiv.org/abs/2509.20184)

## 🔗 유사한 논문
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (85.1% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals: Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (84.4% similar)
- [[2025-09-23/Periodic Graph-Enhanced Multivariate Time Series Anomaly Detector_20250923|Periodic Graph-Enhanced Multivariate Time Series Anomaly Detector]] (82.8% similar)
- [[2025-09-23/Robust Anomaly Detection Under Normality Distribution Shift in Dynamic Graphs_20250923|Robust Anomaly Detection Under Normality Distribution Shift in Dynamic Graphs]] (81.7% similar)
- [[2025-09-24/Graph Enhanced Trajectory Anomaly Detection_20250924|Graph Enhanced Trajectory Anomaly Detection]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reconstruction-based Methods|Reconstruction-based Methods]]
**⚡ Unique Technical**: [[keywords/Time Series Anomaly Detection|Time Series Anomaly Detection]], [[keywords/Structural Similarity|Structural Similarity]], [[keywords/Pattern-wise Anomalies|Pattern-wise Anomalies]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20184v1 Announce Type: cross 
Abstract: Effective anomaly detection in time series is pivotal for modern industrial applications and financial systems. Due to the scarcity of anomaly labels and the high cost of manual labeling, reconstruction-based unsupervised approaches have garnered considerable attention. However, accurate anomaly detection remains an unsettled challenge, since the optimization objectives of reconstruction-based methods merely rely on point-by-point distance measures, ignoring the potential structural characteristics of time series and thus failing to tackle complex pattern-wise anomalies. In this paper, we propose StrAD, a novel structure-enhanced anomaly detection approach to enrich the optimization objective by incorporating structural information hidden in the time series and steering the data reconstruction procedure to better capture such structural features. StrAD accommodates the trend, seasonality, and shape in the optimization objective of the reconstruction model to learn latent structural characteristics and capture the intrinsic pattern variation of time series. The proposed structure-aware optimization objective mechanism can assure the alignment between the original data and the reconstructed data in terms of structural features, thereby keeping consistency in global fluctuation and local characteristics. The mechanism is pluggable and applicable to any reconstruction-based methods, enhancing the model sensitivity to both point-wise anomalies and pattern-wise anomalies. Experimental results show that StrAD improves the performance of state-of-the-art reconstruction-based models across five real-world anomaly detection datasets.

## 📝 요약

이 논문은 시계열 데이터에서의 효과적인 이상 탐지를 위한 새로운 접근법인 StrAD를 제안합니다. StrAD는 시계열 데이터의 구조적 정보를 통합하여 기존의 재구성 기반 비지도 학습 방법의 최적화 목표를 강화합니다. 이를 통해 데이터의 추세, 계절성, 형태를 고려하여 복잡한 패턴 이상을 더 잘 탐지할 수 있습니다. StrAD는 구조적 특징을 활용하여 원본 데이터와 재구성된 데이터 간의 일관성을 유지하며, 기존 모델의 민감도를 향상시킵니다. 실험 결과, StrAD는 다섯 개의 실제 데이터셋에서 최첨단 모델의 성능을 개선하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. StrAD는 시계열 데이터의 구조적 정보를 활용하여 최적화 목표를 강화한 새로운 이상 탐지 방법입니다.
- 2. 제안된 방법은 시계열의 추세, 계절성, 모양을 고려하여 잠재적인 구조적 특성을 학습합니다.
- 3. StrAD는 원본 데이터와 재구성된 데이터 간의 구조적 특징 일치를 보장하여 전반적인 변동성과 지역적 특성을 유지합니다.
- 4. 이 메커니즘은 플러그형으로, 어떤 재구성 기반 방법에도 적용 가능하며, 점 단위 및 패턴 단위 이상에 대한 민감도를 높입니다.
- 5. 실험 결과, StrAD는 다섯 개의 실제 이상 탐지 데이터셋에서 최첨단 재구성 기반 모델의 성능을 향상시킵니다.


---

*Generated on 2025-09-25 16:01:06*