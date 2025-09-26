---
keywords:
  - Edge-Type Decoupled Network
  - Attention Mechanism
  - Temporal Graph
  - Driver-Intention Prediction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.03251
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:31:10.307937",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Edge-Type Decoupled Network",
    "Attention Mechanism",
    "Temporal Graph",
    "Driver-Intention Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Edge-Type Decoupled Network": 0.78,
    "Attention Mechanism": 0.82,
    "Temporal Graph": 0.75,
    "Driver-Intention Prediction": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Edge-Type Decoupled Network",
        "canonical": "Edge-Type Decoupled Network",
        "aliases": [
          "ETDNet"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel architecture introduced in the paper, providing a unique approach to temporal reasoning in graphs.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph-Attention Module",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Graph Attention"
        ],
        "category": "specific_connectable",
        "rationale": "This module is a specific application of the attention mechanism within graph structures, linking to broader attention-based models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Temporal-Graph Representation",
        "canonical": "Temporal Graph",
        "aliases": [
          "Temporal Graph Representation"
        ],
        "category": "specific_connectable",
        "rationale": "Temporal graphs are crucial for modeling evolving interactions, connecting with existing graph-based temporal models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Driver-Intention Prediction",
        "canonical": "Driver-Intention Prediction",
        "aliases": [
          "Driver Intention"
        ],
        "category": "unique_technical",
        "rationale": "This application area is specific to the paper's experiments and connects to broader predictive modeling tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
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
      "candidate_surface": "Edge-Type Decoupled Network",
      "resolved_canonical": "Edge-Type Decoupled Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph-Attention Module",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Temporal-Graph Representation",
      "resolved_canonical": "Temporal Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Driver-Intention Prediction",
      "resolved_canonical": "Driver-Intention Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.03251.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.03251](https://arxiv.org/abs/2508.03251)

## 🔗 유사한 논문
- [[2025-09-22/EvoBrain_ Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network_20250922|EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network]] (83.2% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (82.6% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (81.9% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (81.8% similar)
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Temporal Graph|Temporal Graph]]
**⚡ Unique Technical**: [[keywords/Edge-Type Decoupled Network|Edge-Type Decoupled Network]], [[keywords/Driver-Intention Prediction|Driver-Intention Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.03251v2 Announce Type: replace 
Abstract: Modeling evolving interactions among entities is critical in many real-world tasks. For example, predicting driver maneuvers in traffic requires tracking how neighboring vehicles accelerate, brake, and change lanes relative to one another over consecutive frames. Likewise, detecting financial fraud hinges on following the flow of funds through successive transactions as they propagate through the network. Unlike classic time-series forecasting, these settings demand reasoning over who interacts with whom and when, calling for a temporal-graph representation that makes both the relations and their evolution explicit. Existing temporal-graph methods typically use snapshot graphs to encode temporal evolution. We introduce a full-history graph that instantiates one node for every entity at every time step and separates two edge sets: (i) intra-time-step edges that capture relations within a single frame and (ii) inter-time-step edges that connect an entity to itself at consecutive steps. To learn on this graph we design an Edge-Type Decoupled Network (ETDNet) with parallel modules: a graph-attention module aggregates information along intra-time-step edges, a multi-head temporal-attention module attends over an entity's inter-time-step history, and a fusion module combines the two messages after every layer. Evaluated on driver-intention prediction (Waymo) and Bitcoin fraud detection (Elliptic++), ETDNet consistently surpasses strong baselines, lifting Waymo joint accuracy to 75.6\% (vs. 74.1\%) and raising Elliptic++ illicit-class F1 to 88.1\% (vs. 60.4\%). These gains demonstrate the benefit of representing structural and temporal relations as distinct edges in a single graph.

## 📝 요약

이 논문은 시간에 따라 변화하는 상호작용을 모델링하는 새로운 방법론을 제안합니다. 기존의 시간 그래프 방법론은 스냅샷 그래프를 사용하지만, 본 연구에서는 모든 시간 단계에서 각 엔티티에 대해 노드를 생성하고, 두 종류의 엣지를 구분하는 전체 역사 그래프를 도입합니다. 이를 학습하기 위해 ETDNet이라는 네트워크를 설계하였으며, 이는 그래프 주의 모듈과 다중 헤드 시간 주의 모듈을 통해 정보를 수집하고 결합합니다. 제안된 방법은 운전자 의도 예측과 비트코인 사기 탐지에서 기존의 강력한 기준을 능가하며, 각각의 정확도와 F1 점수를 크게 향상시켰습니다. 이러한 성과는 구조적 및 시간적 관계를 명확히 구분하여 단일 그래프 내에서 표현하는 것의 이점을 보여줍니다.

## 🎯 주요 포인트

- 1. 실세계의 다양한 과제에서 진화하는 상호작용을 모델링하는 것이 중요하며, 이는 시간-그래프 표현을 통해 관계와 그 진화를 명시적으로 나타내야 한다.
- 2. 기존의 시간-그래프 방법은 스냅샷 그래프를 사용하지만, 본 연구는 모든 시간 단계에서 각 엔티티에 대해 노드를 생성하고 두 가지 엣지 집합을 분리하는 전체 역사 그래프를 도입한다.
- 3. ETDNet은 그래프-어텐션 모듈, 다중 헤드 시간-어텐션 모듈, 그리고 융합 모듈로 구성되어 있으며, 이는 구조적 및 시간적 관계를 단일 그래프에서 명확히 구분하여 학습한다.
- 4. ETDNet은 Waymo 운전자 의도 예측과 Elliptic++ 비트코인 사기 탐지에서 강력한 기준 모델을 능가하며, 각각 75.6%와 88.1%의 성능을 달성하였다.
- 5. 이러한 성능 향상은 구조적 및 시간적 관계를 단일 그래프에서 별도의 엣지로 표현하는 것의 이점을 보여준다.


---

*Generated on 2025-09-24 00:31:10*