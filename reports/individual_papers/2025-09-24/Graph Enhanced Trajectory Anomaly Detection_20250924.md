<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:47:32.688055",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Transformer",
    "Confidence Weighted Negative Log Likelihood",
    "road network topology"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Transformer": 0.8,
    "Confidence Weighted Negative Log Likelihood": 0.78,
    "road network topology": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Attention Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Attention Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the proposed framework, enhancing connectivity with existing graph-based methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Transformer-based decoder",
        "canonical": "Transformer",
        "aliases": [
          "Transformer decoder"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are widely used in sequence modeling, linking to a broad range of machine learning applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Confidence Weighted Negative Log Likelihood",
        "canonical": "Confidence Weighted Negative Log Likelihood",
        "aliases": [
          "CW NLL"
        ],
        "category": "unique_technical",
        "rationale": "This novel scoring function is specific to the paper's anomaly detection approach, offering unique insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "road network topology",
        "canonical": "road network topology",
        "aliases": [
          "road topology",
          "network topology"
        ],
        "category": "unique_technical",
        "rationale": "Understanding road network topology is crucial for trajectory modeling, providing a unique perspective on spatial constraints.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "trajectory anomaly detection",
      "movement patterns",
      "real-world datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Attention Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Transformer-based decoder",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Confidence Weighted Negative Log Likelihood",
      "resolved_canonical": "Confidence Weighted Negative Log Likelihood",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "road network topology",
      "resolved_canonical": "road network topology",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Graph Enhanced Trajectory Anomaly Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18386.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18386](https://arxiv.org/abs/2509.18386)

## 🔗 유사한 논문
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (83.8% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (83.7% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (83.1% similar)
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (82.8% similar)
- [[2025-09-18/TFLAG_Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph_20250918|TFLAG:Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Confidence Weighted Negative Log Likelihood|Confidence Weighted Negative Log Likelihood]], [[keywords/road network topology|road network topology]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18386v1 Announce Type: cross 
Abstract: Trajectory anomaly detection is essential for identifying unusual and unexpected movement patterns in applications ranging from intelligent transportation systems to urban safety and fraud prevention.
  Existing methods only consider limited aspects of the trajectory nature and its movement space by treating trajectories as sequences of sampled locations, with sampling determined by positioning technology, e.g., GPS, or by high-level abstractions such as staypoints. Trajectories are analyzed in Euclidean space, neglecting the constraints and connectivity information of the underlying movement network, e.g., road or transit networks.
  The proposed Graph Enhanced Trajectory Anomaly Detection (GETAD) framework tightly integrates road network topology, segment semantics, and historical travel patterns to model trajectory data. GETAD uses a Graph Attention Network to learn road-aware embeddings that capture both physical attributes and transition behavior, and augments these with graph-based positional encodings that reflect the spatial layout of the road network.
  A Transformer-based decoder models sequential movement, while a multiobjective loss function combining autoregressive prediction and supervised link prediction ensures realistic and structurally coherent representations.
  To improve the robustness of anomaly detection, we introduce Confidence Weighted Negative Log Likelihood (CW NLL), an anomaly scoring function that emphasizes high-confidence deviations.
  Experiments on real-world and synthetic datasets demonstrate that GETAD achieves consistent improvements over existing methods, particularly in detecting subtle anomalies in road-constrained environments. These results highlight the benefits of incorporating graph structure and contextual semantics into trajectory modeling, enabling more precise and context-aware anomaly detection.

## 📝 요약

이 논문은 비정상적인 이동 패턴을 식별하기 위한 새로운 방법론인 Graph Enhanced Trajectory Anomaly Detection (GETAD)을 제안합니다. 기존 방법들은 경로를 단순히 위치의 연속으로 취급하여 제한적인 정보를 사용하지만, GETAD는 도로 네트워크의 구조와 역사적 이동 패턴을 통합하여 경로 데이터를 모델링합니다. Graph Attention Network를 활용해 도로 인식 임베딩을 학습하고, 공간적 배치를 반영하는 그래프 기반 위치 인코딩을 추가합니다. Transformer 기반 디코더와 다목적 손실 함수를 통해 현실적이고 구조적으로 일관된 표현을 보장합니다. 또한, Confidence Weighted Negative Log Likelihood (CW NLL)를 도입하여 높은 신뢰도의 이상치를 강조합니다. 실험 결과, GETAD는 기존 방법보다 도로 제약 환경에서 미세한 이상치를 더 효과적으로 감지하며, 그래프 구조와 문맥적 의미를 통합한 경로 모델링의 이점을 보여줍니다.

## 🎯 주요 포인트

- 1. GETAD 프레임워크는 도로 네트워크의 위상, 세그먼트 의미, 역사적 이동 패턴을 통합하여 경로 데이터를 모델링합니다.
- 2. Graph Attention Network를 활용하여 도로 인식 임베딩을 학습하고, 그래프 기반 위치 인코딩을 통해 도로 네트워크의 공간 레이아웃을 반영합니다.
- 3. Transformer 기반 디코더와 다목적 손실 함수를 사용하여 현실적이고 구조적으로 일관된 경로 표현을 보장합니다.
- 4. CW NLL을 도입하여 높은 신뢰도의 편차를 강조하는 이상 탐지 점수 함수를 제공합니다.
- 5. 실험 결과, GETAD는 기존 방법보다 도로 제약 환경에서 미세한 이상 탐지를 더 효과적으로 수행함을 보여줍니다.


---

*Generated on 2025-09-24 13:47:32*