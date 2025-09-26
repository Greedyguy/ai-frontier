---
keywords:
  - Graph Neural Network
  - Multi-scale Dependencies
  - Heterogeneous Data
  - Automatic Identification System
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2507.20362
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:47:56.068661",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Multi-scale Dependencies",
    "Heterogeneous Data",
    "Automatic Identification System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Multi-scale Dependencies": 0.78,
    "Heterogeneous Data": 0.77,
    "Automatic Identification System": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph-based Imputation Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Network"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing work on graph neural networks, which are central to the proposed method.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-scale Dependencies",
        "canonical": "Multi-scale Dependencies",
        "aliases": [
          "Multi-scale Relations"
        ],
        "category": "unique_technical",
        "rationale": "Captures the unique aspect of the approach in modeling dependencies at multiple scales.",
        "novelty_score": 0.67,
        "connectivity_score": 0.72,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Heterogeneous Attributes",
        "canonical": "Heterogeneous Data",
        "aliases": [
          "Diverse Attributes"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the method's focus on handling diverse data types, which is crucial for its application.",
        "novelty_score": 0.61,
        "connectivity_score": 0.75,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "Automatic Identification System",
        "canonical": "Automatic Identification System",
        "aliases": [
          "AIS"
        ],
        "category": "unique_technical",
        "rationale": "Essential for understanding the specific application context of the research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "imputation",
      "dataset",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph-based Imputation Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-scale Dependencies",
      "resolved_canonical": "Multi-scale Dependencies",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.72,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Heterogeneous Attributes",
      "resolved_canonical": "Heterogeneous Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.61,
        "connectivity": 0.75,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Automatic Identification System",
      "resolved_canonical": "Automatic Identification System",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MH-GIN: Multi-scale Heterogeneous Graph-based Imputation Network for AIS Data (Extended Version)

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.20362.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2507.20362](https://arxiv.org/abs/2507.20362)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (81.1% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (81.0% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (80.8% similar)
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (80.7% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Multi-scale Dependencies|Multi-scale Dependencies]], [[keywords/Heterogeneous Data|Heterogeneous Data]], [[keywords/Automatic Identification System|Automatic Identification System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.20362v2 Announce Type: replace 
Abstract: Location-tracking data from the Automatic Identification System, much of which is publicly available, plays a key role in a range of maritime safety and monitoring applications. However, the data suffers from missing values that hamper downstream applications. Imputing the missing values is challenging because the values of different heterogeneous attributes are updated at diverse rates, resulting in the occurrence of multi-scale dependencies among attributes. Existing imputation methods that assume similar update rates across attributes are unable to capture and exploit such dependencies, limiting their imputation accuracy. We propose MH-GIN, a Multi-scale Heterogeneous Graph-based Imputation Network that aims improve imputation accuracy by capturing multi-scale dependencies. Specifically, MH-GIN first extracts multi-scale temporal features for each attribute while preserving their intrinsic heterogeneous characteristics. Then, it constructs a multi-scale heterogeneous graph to explicitly model dependencies between heterogeneous attributes to enable more accurate imputation of missing values through graph propagation. Experimental results on two real-world datasets find that MH-GIN is capable of an average 57% reduction in imputation errors compared to state-of-the-art methods, while maintaining computational efficiency. The source code and implementation details of MH-GIN are publicly available https://github.com/hyLiu1994/MH-GIN.

## 📝 요약

이 논문은 자동식별시스템(AIS)의 위치 추적 데이터에서 발생하는 결측값 문제를 해결하기 위해 MH-GIN이라는 다중 스케일 이질 그래프 기반 보간 네트워크를 제안합니다. 기존 방법들은 속성 간 업데이트 속도가 유사하다고 가정하여 정확도가 제한되었으나, MH-GIN은 속성 간의 다중 스케일 의존성을 포착하여 보간 정확도를 향상시킵니다. 실험 결과, MH-GIN은 최신 기법 대비 평균 57%의 보간 오류 감소를 달성하며, 계산 효율성도 유지합니다. 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 자동 식별 시스템의 위치 추적 데이터는 해양 안전 및 모니터링 응용 프로그램에 중요한 역할을 하지만, 누락된 값으로 인해 문제를 겪고 있습니다.
- 2. 기존의 보간 방법은 속성 간의 업데이트 비율이 유사하다고 가정하여 다중 스케일 종속성을 제대로 포착하지 못해 정확도가 제한됩니다.
- 3. MH-GIN은 속성의 내재된 이질적 특성을 유지하면서 다중 스케일의 시간적 특징을 추출하여 보간 정확도를 향상시킵니다.
- 4. MH-GIN은 이질적 속성 간의 종속성을 명시적으로 모델링하는 다중 스케일 이질 그래프를 구축하여 그래프 전파를 통해 누락된 값을 더 정확하게 보간합니다.
- 5. 실험 결과, MH-GIN은 최신 방법에 비해 평균 57%의 보간 오류 감소를 달성하면서 계산 효율성을 유지합니다.


---

*Generated on 2025-09-24 02:47:56*