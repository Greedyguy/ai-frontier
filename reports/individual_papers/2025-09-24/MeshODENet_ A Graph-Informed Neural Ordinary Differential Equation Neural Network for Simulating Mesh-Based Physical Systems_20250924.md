<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:51:19.545646",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Neural Ordinary Differential Equations",
    "Mesh-Based Physical Systems",
    "Structural Mechanics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.9,
    "Neural Ordinary Differential Equations": 0.85,
    "Mesh-Based Physical Systems": 0.8,
    "Structural Mechanics": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's methodology and connect well with existing knowledge on neural network architectures.",
        "novelty_score": 0.45,
        "connectivity_score": 0.95,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Neural Ordinary Differential Equations",
        "canonical": "Neural Ordinary Differential Equations",
        "aliases": [
          "Neural ODEs",
          "NODE"
        ],
        "category": "unique_technical",
        "rationale": "Neural ODEs are a key component of the proposed framework, offering a novel approach to continuous-time modeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mesh-Based Physical Systems",
        "canonical": "Mesh-Based Physical Systems",
        "aliases": [
          "Mesh Systems",
          "Discretized Mesh"
        ],
        "category": "unique_technical",
        "rationale": "The focus on mesh-based systems is crucial for understanding the application domain of the proposed method.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structural Mechanics",
        "canonical": "Structural Mechanics",
        "aliases": [
          "Structural Analysis",
          "Mechanics of Structures"
        ],
        "category": "broad_technical",
        "rationale": "Structural mechanics is a broad technical field relevant to the paper's application area.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
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
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.95,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Neural Ordinary Differential Equations",
      "resolved_canonical": "Neural Ordinary Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Mesh-Based Physical Systems",
      "resolved_canonical": "Mesh-Based Physical Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structural Mechanics",
      "resolved_canonical": "Structural Mechanics",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MeshODENet: A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18445.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18445](https://arxiv.org/abs/2509.18445)

## 🔗 유사한 논문
- [[2025-09-17/An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (82.5% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.8% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.8% similar)
- [[2025-09-23/Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks_20250923|Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks]] (81.2% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Structural Mechanics|Structural Mechanics]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Neural Ordinary Differential Equations|Neural Ordinary Differential Equations]], [[keywords/Mesh-Based Physical Systems|Mesh-Based Physical Systems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18445v1 Announce Type: new 
Abstract: The simulation of complex physical systems using a discretized mesh is a cornerstone of applied mechanics, but traditional numerical solvers are often computationally prohibitive for many-query tasks. While Graph Neural Networks (GNNs) have emerged as powerful surrogate models for mesh-based data, their standard autoregressive application for long-term prediction is often plagued by error accumulation and instability. To address this, we introduce MeshODENet, a general framework that synergizes the spatial reasoning of GNNs with the continuous-time modeling of Neural Ordinary Differential Equations. We demonstrate the framework's effectiveness and versatility on a series of challenging structural mechanics problems, including one- and two-dimensional elastic bodies undergoing large, non-linear deformations. The results demonstrate that our approach significantly outperforms baseline models in long-term predictive accuracy and stability, while achieving substantial computational speed-ups over traditional solvers. This work presents a powerful and generalizable approach for developing data-driven surrogates to accelerate the analysis and modeling of complex structural systems.

## 📝 요약

MeshODENet은 복잡한 물리 시스템의 시뮬레이션을 위한 새로운 프레임워크로, 그래프 신경망(GNN)의 공간 추론과 신경 상미분 방정식(Neural ODE)의 연속 시간 모델링을 결합합니다. 이 방법은 전통적인 수치 해석기의 계산 비용 문제를 해결하며, 특히 긴 시간 예측에서 발생하는 오류 누적과 불안정성을 개선합니다. 구조 역학 문제에서 MeshODENet은 기존 모델보다 예측 정확성과 안정성이 뛰어나며, 계산 속도도 크게 향상됩니다. 이 연구는 복잡한 구조 시스템 분석 및 모델링을 가속화할 수 있는 강력하고 일반화 가능한 데이터 기반 대리 모델을 제시합니다.

## 🎯 주요 포인트

- 1. MeshODENet은 GNN의 공간 추론과 신경망 상미분방정식의 연속 시간 모델링을 결합한 일반적인 프레임워크입니다.
- 2. MeshODENet은 장기 예측 정확성과 안정성에서 기존 모델을 능가하며, 전통적인 해법에 비해 계산 속도를 크게 향상시킵니다.
- 3. 이 프레임워크는 복잡한 구조 역학 문제, 특히 큰 비선형 변형을 겪는 1차원 및 2차원 탄성체 문제에서 효과적이고 다재다능함을 입증했습니다.
- 4. 본 연구는 복잡한 구조 시스템의 분석 및 모델링을 가속화하기 위한 데이터 기반 대체 모델 개발에 강력하고 일반화 가능한 접근 방식을 제시합니다.


---

*Generated on 2025-09-24 14:51:19*