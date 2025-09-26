---
keywords:
  - Graph Neural Network
  - Multivariate Time Series
  - Fast Fourier Transform
  - Spatio-Temporal Correlations
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17472
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:53:00.597394",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Multivariate Time Series",
    "Fast Fourier Transform",
    "Spatio-Temporal Correlations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Multivariate Time Series": 0.78,
    "Fast Fourier Transform": 0.72,
    "Spatio-Temporal Correlations": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the proposed method, enhancing connectivity with existing literature on neural network applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multivariate Time Series",
        "canonical": "Multivariate Time Series",
        "aliases": [
          "MTS"
        ],
        "category": "unique_technical",
        "rationale": "The focus on multivariate time series is unique and crucial for understanding the context of anomaly detection in this study.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fast Fourier Transform",
        "canonical": "Fast Fourier Transform",
        "aliases": [
          "FFT"
        ],
        "category": "broad_technical",
        "rationale": "FFT is used in the periodic time-slot allocation strategy, linking to broader technical discussions on signal processing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Spatio-Temporal Correlations",
        "canonical": "Spatio-Temporal Correlations",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Understanding spatio-temporal correlations is essential for the proposed anomaly detection method, offering a unique perspective.",
        "novelty_score": 0.68,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "anomaly detection",
      "periodic graphs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multivariate Time Series",
      "resolved_canonical": "Multivariate Time Series",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fast Fourier Transform",
      "resolved_canonical": "Fast Fourier Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Spatio-Temporal Correlations",
      "resolved_canonical": "Spatio-Temporal Correlations",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Periodic Graph-Enhanced Multivariate Time Series Anomaly Detector

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17472.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17472](https://arxiv.org/abs/2509.17472)

## 🔗 유사한 논문
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (88.6% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals: Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (84.4% similar)
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (83.7% similar)
- [[2025-09-22/MTS-DMAE_ Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning_20250922|MTS-DMAE: Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning]] (81.0% similar)
- [[2025-09-18/AnoF-Diff_ One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use_20250918|AnoF-Diff: One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Fast Fourier Transform|Fast Fourier Transform]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Multivariate Time Series|Multivariate Time Series]], [[keywords/Spatio-Temporal Correlations|Spatio-Temporal Correlations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17472v1 Announce Type: new 
Abstract: Multivariate time series (MTS) anomaly detection commonly encounters in various domains like finance, healthcare, and industrial monitoring. However, existing MTS anomaly detection methods are mostly defined on the static graph structure, which fails to perform an accurate representation of complex spatio-temporal correlations in MTS. To address this issue, this study proposes a Periodic Graph-Enhanced Multivariate Time Series Anomaly Detector (PGMA) with the following two-fold ideas: a) designing a periodic time-slot allocation strategy based Fast Fourier Transform (FFT), which enables the graph structure to reflect dynamic changes in MTS; b) utilizing graph neural network and temporal extension convolution to accurate extract the complex spatio-temporal correlations from the reconstructed periodic graphs. Experiments on four real datasets from real applications demonstrate that the proposed PGMA outperforms state-of-the-art models in MTS anomaly detection.

## 📝 요약

이 연구는 금융, 의료, 산업 모니터링 등 다양한 분야에서 발생하는 다변량 시계열(MTS) 이상 탐지의 문제를 해결하기 위해 새로운 방법론을 제안합니다. 기존의 MTS 이상 탐지 방법은 정적 그래프 구조에 기반하여 복잡한 시공간 상관관계를 정확히 표현하지 못하는 한계를 가지고 있습니다. 이를 극복하기 위해, 본 연구는 주기적 그래프 기반의 MTS 이상 탐지기(PGMA)를 제안합니다. 주요 기여로는 FFT 기반의 주기적 시간 슬롯 할당 전략을 설계하여 그래프 구조가 MTS의 동적 변화를 반영할 수 있도록 하고, 그래프 신경망과 시계열 확장 합성을 활용하여 복잡한 시공간 상관관계를 정확히 추출하는 방법론을 제시합니다. 네 가지 실제 데이터셋을 활용한 실험 결과, 제안된 PGMA가 기존 최신 모델들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 다변량 시계열 이상 탐지는 금융, 의료, 산업 모니터링 등 다양한 분야에서 발생한다.
- 2. 기존의 다변량 시계열 이상 탐지 방법은 정적 그래프 구조에 기반하여 복잡한 시공간 상관관계를 정확히 표현하지 못한다.
- 3. 본 연구는 주기적인 그래프 구조를 통해 동적인 변화를 반영하는 FFT 기반의 시간 슬롯 할당 전략을 제안한다.
- 4. 그래프 신경망과 시간 확장 합성을 활용하여 복잡한 시공간 상관관계를 정확히 추출한다.
- 5. 네 가지 실제 데이터셋 실험 결과, 제안된 PGMA 모델이 최신 모델들보다 뛰어난 성능을 보였다.


---

*Generated on 2025-09-24 01:53:00*