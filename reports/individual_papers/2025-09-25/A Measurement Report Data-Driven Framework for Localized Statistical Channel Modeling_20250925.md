---
keywords:
  - Graph Neural Network
  - Localized Statistical Channel Modeling
  - Measurement Report Framework
  - Self-supervised Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19342
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:50:50.769255",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Localized Statistical Channel Modeling",
    "Measurement Report Framework",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.82,
    "Localized Statistical Channel Modeling": 0.68,
    "Measurement Report Framework": 0.7,
    "Self-supervised Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "hypergraph neural networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "HGNN",
          "hypergraph NN"
        ],
        "category": "specific_connectable",
        "rationale": "This concept extends the Graph Neural Network framework by incorporating hypergraphs, which enhances connectivity in graph-based models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "localized statistical channel modeling",
        "canonical": "Localized Statistical Channel Modeling",
        "aliases": [
          "LSCM"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized technique crucial for network optimization, providing a unique link to digital twin applications.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.68
      },
      {
        "surface": "measurement report data-driven framework",
        "canonical": "Measurement Report Framework",
        "aliases": [
          "MR framework"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper's contribution, offering a novel approach to channel modeling using MR data.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "semi-supervised method",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "semi-supervised approach"
        ],
        "category": "specific_connectable",
        "rationale": "The method aligns with self-supervised learning techniques, which are increasingly relevant in data-driven frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "drive test data",
      "performance evaluation",
      "real-world MR dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "hypergraph neural networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "localized statistical channel modeling",
      "resolved_canonical": "Localized Statistical Channel Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "measurement report data-driven framework",
      "resolved_canonical": "Measurement Report Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "semi-supervised method",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Measurement Report Data-Driven Framework for Localized Statistical Channel Modeling

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19342.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19342](https://arxiv.org/abs/2509.19342)

## 🔗 유사한 논문
- [[2025-09-25/Improving Outdoor Multi-cell Fingerprinting-based Positioning via Mobile Data Augmentation_20250925|Improving Outdoor Multi-cell Fingerprinting-based Positioning via Mobile Data Augmentation]] (81.9% similar)
- [[2025-09-24/Joint Cooperative and Non-Cooperative Localization in WSNs with Distributed Scaled Proximal ADMM Algorithms_20250924|Joint Cooperative and Non-Cooperative Localization in WSNs with Distributed Scaled Proximal ADMM Algorithms]] (81.8% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (81.7% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (80.8% similar)
- [[2025-09-25/Radio Propagation Modelling_ To Differentiate or To Deep Learn, That Is The Question_20250925|Radio Propagation Modelling: To Differentiate or To Deep Learn, That Is The Question]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Localized Statistical Channel Modeling|Localized Statistical Channel Modeling]], [[keywords/Measurement Report Framework|Measurement Report Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19342v1 Announce Type: cross 
Abstract: Localized statistical channel modeling (LSCM) is crucial for effective performance evaluation in digital twin-assisted network optimization. Solely relying on the multi-beam reference signal receiving power (RSRP), LSCM aims to model the localized statistical propagation environment by estimating the channel angular power spectrum (APS). However, existing methods rely heavily on drive test data with high collection costs and limited spatial coverage. In this paper, we propose a measurement report (MR) data-driven framework for LSCM, exploiting the low-cost and extensive collection of MR data. The framework comprises two novel modules. The MR localization module addresses the issue of missing locations in MR data by introducing a semi-supervised method based on hypergraph neural networks, which exploits multi-modal information via distance-aware hypergraph modeling and hypergraph convolution for location extraction. To enhance the computational efficiency and solution robustness, LSCM operates at the grid level. Compared to independently constructing geographically uniform grids and estimating channel APS, the joint grid construction and channel APS estimation module enhances robustness in complex environments with spatially non-uniform data by exploiting their correlation. This module alternately optimizes grid partitioning and APS estimation using clustering and improved sparse recovery for the ill-conditioned measurement matrix and incomplete observations. Through comprehensive experiments on a real-world MR dataset, we demonstrate the superior performance and robustness of our framework in localization and channel modeling.

## 📝 요약

이 논문은 디지털 트윈 기반 네트워크 최적화를 위한 지역화된 통계적 채널 모델링(LSCM)을 제안합니다. 기존 방법은 비용이 많이 드는 드라이브 테스트 데이터에 의존하지만, 본 연구는 저비용의 MR 데이터를 활용하는 프레임워크를 제안합니다. 이 프레임워크는 두 가지 주요 모듈로 구성됩니다. 첫째, MR 데이터의 위치 결측 문제를 해결하기 위해 하이퍼그래프 신경망을 활용한 반지도 학습 방법을 도입하여 위치를 추출합니다. 둘째, 격자 수준에서의 LSCM을 통해 계산 효율성과 솔루션의 강건성을 향상시키며, 공간적으로 비균일한 데이터 환경에서도 강건성을 높입니다. 실제 MR 데이터셋을 통한 실험에서 이 프레임워크의 우수한 성능과 강건성이 입증되었습니다.

## 🎯 주요 포인트

- 1. 디지털 트윈 기반 네트워크 최적화를 위한 지역화된 통계적 채널 모델링(LSCM)은 채널 각도 전력 스펙트럼(APS)을 추정하여 지역화된 통계적 전파 환경을 모델링하는 것을 목표로 합니다.
- 2. 기존 방법은 높은 수집 비용과 제한된 공간적 범위를 가진 드라이브 테스트 데이터에 의존하지만, 제안된 프레임워크는 저비용 및 광범위한 MR 데이터 수집을 활용합니다.
- 3. MR 데이터의 누락된 위치 문제를 해결하기 위해 하이퍼그래프 신경망을 기반으로 한 반지도 학습 방법을 도입하여 위치를 추출합니다.
- 4. 격자 수준에서의 LSCM은 공간적으로 비균일한 데이터와의 상관성을 활용하여 복잡한 환경에서의 강건성을 향상시킵니다.
- 5. 실제 MR 데이터셋을 통한 실험을 통해 제안된 프레임워크의 위치 추정 및 채널 모델링에서의 우수한 성능과 강건성을 입증하였습니다.


---

*Generated on 2025-09-25 16:50:50*