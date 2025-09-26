---
keywords:
  - Graph Neural Network
  - Nanoporous Materials Design
  - Property Prediction
  - Symmetry-aware Design
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15908
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:20:00.388352",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Nanoporous Materials Design",
    "Property Prediction",
    "Symmetry-aware Design"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Nanoporous Materials Design": 0.78,
    "Property Prediction": 0.65,
    "Symmetry-aware Design": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's approach and connect well with existing literature on machine learning for materials design.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Nanoporous Materials Design",
        "canonical": "Nanoporous Materials Design",
        "aliases": [
          "Nanoporous Design",
          "Porous Materials Design"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized focus of the paper, offering a unique angle on materials science that is not widely covered.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Property Prediction",
        "canonical": "Property Prediction",
        "aliases": [
          "Predictive Modeling",
          "Property Forecasting"
        ],
        "category": "broad_technical",
        "rationale": "Property prediction is a key application of machine learning in materials science, providing a broad technical link.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "Symmetry-aware Design",
        "canonical": "Symmetry-aware Design",
        "aliases": [
          "Symmetry-conscious Design",
          "Symmetry-based Design"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology, offering a novel approach to materials design.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Nanoporous Materials Design",
      "resolved_canonical": "Nanoporous Materials Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Property Prediction",
      "resolved_canonical": "Property Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Symmetry-aware Design",
      "resolved_canonical": "Symmetry-aware Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# An Equivariant Graph Network for Interpretable Nanoporous Materials Design

**Korean Title:** 해석 가능한 나노다공성 물질 설계를 위한 등변 그래프 네트워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15908.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15908](https://arxiv.org/abs/2509.15908)

## 🔗 유사한 논문
- [[2025-09-17/An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (83.9% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.1% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (79.7% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (79.7% similar)
- [[2025-09-22/Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria_20250922|Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Property Prediction|Property Prediction]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Nanoporous Materials Design|Nanoporous Materials Design]], [[keywords/Symmetry-aware Design|Symmetry-aware Design]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15908v1 Announce Type: cross 
Abstract: Nanoporous materials hold promise for diverse sustainable applications, yet their vast chemical space poses challenges for efficient design. Machine learning offers a compelling pathway to accelerate the exploration, but existing models lack either interpretability or fidelity for elucidating the correlation between crystal geometry and property. Here, we report a three-dimensional periodic space sampling method that decomposes large nanoporous structures into local geometrical sites for combined property prediction and site-wise contribution quantification. Trained with a constructed database and retrieved datasets, our model achieves state-of-the-art accuracy and data efficiency for property prediction on gas storage, separation, and electrical conduction. Meanwhile, this approach enables the interpretation of the prediction and allows for accurate identification of significant local sites for targeted properties. Through identifying transferable high-performance sites across diverse nanoporous frameworks, our model paves the way for interpretable, symmetry-aware nanoporous materials design, which is extensible to other materials, like molecular crystals and beyond.

## 🔍 Abstract (한글 번역)

arXiv:2509.15908v1 발표 유형: 교차  
초록: 나노다공성 물질은 다양한 지속 가능한 응용 분야에 대한 가능성을 가지고 있지만, 그 방대한 화학적 공간은 효율적인 설계에 도전 과제를 제시합니다. 기계 학습은 탐색을 가속화할 수 있는 매력적인 경로를 제공하지만, 기존 모델은 결정 구조와 특성 간의 상관관계를 설명하는 데 있어 해석 가능성이나 충실도가 부족합니다. 여기에서는 대형 나노다공성 구조를 국부적인 기하학적 사이트로 분해하여 특성 예측과 사이트별 기여도 정량화를 결합하는 3차원 주기적 공간 샘플링 방법을 보고합니다. 구축된 데이터베이스와 검색된 데이터셋으로 훈련된 우리의 모델은 가스 저장, 분리 및 전기 전도성에 대한 특성 예측에서 최첨단 정확도와 데이터 효율성을 달성합니다. 동시에 이 접근법은 예측의 해석을 가능하게 하고, 목표 특성에 중요한 국부 사이트를 정확하게 식별할 수 있게 합니다. 다양한 나노다공성 프레임워크에서 전이 가능한 고성능 사이트를 식별함으로써, 우리의 모델은 해석 가능하고 대칭 인식이 가능한 나노다공성 물질 설계의 길을 열며, 이는 분자 결정 등 다른 물질로 확장 가능합니다.

## 📝 요약

나노다공성 물질은 다양한 지속 가능한 응용 분야에서 잠재력을 지니고 있지만, 그 광범위한 화학적 공간은 효율적인 설계에 어려움을 줍니다. 본 연구는 기계 학습을 활용하여 이러한 문제를 해결하고자 하며, 기존 모델이 해석 가능성이나 정확성에서 부족한 점을 개선하고자 합니다. 우리는 3차원 주기적 공간 샘플링 방법을 제안하여 큰 나노다공성 구조를 지역적 기하학적 사이트로 분해하고, 이를 통해 속성 예측과 사이트별 기여도 정량화를 수행합니다. 구축된 데이터베이스와 수집된 데이터셋으로 학습된 모델은 가스 저장, 분리, 전기 전도성에 대한 속성 예측에서 최첨단의 정확도와 데이터 효율성을 달성했습니다. 또한, 이 방법은 예측 해석을 가능하게 하고, 목표 속성에 중요한 지역 사이트를 정확히 식별할 수 있게 합니다. 다양한 나노다공성 프레임워크에서 전이 가능한 고성능 사이트를 식별함으로써, 우리의 모델은 해석 가능하고 대칭을 고려한 나노다공성 물질 설계의 길을 열며, 이는 분자 결정 등 다른 물질에도 확장 가능합니다.

## 🎯 주요 포인트

- 1. 나노다공성 물질의 효율적인 설계를 위해 기계 학습을 활용하여 결정 구조와 특성 간의 상관관계를 해석할 수 있는 모델을 개발했습니다.
- 2. 3차원 주기적 공간 샘플링 방법을 통해 대규모 나노다공성 구조를 지역 기하학적 사이트로 분해하여 특성 예측과 사이트별 기여도 정량화를 동시에 수행합니다.
- 3. 구축된 데이터베이스와 검색된 데이터셋으로 학습된 모델은 가스 저장, 분리, 전기 전도성에 대한 특성 예측에서 최첨단 정확도와 데이터 효율성을 달성했습니다.
- 4. 이 접근법은 예측의 해석을 가능하게 하며, 목표 특성에 중요한 지역 사이트를 정확하게 식별할 수 있게 합니다.
- 5. 다양한 나노다공성 프레임워크에서 전이 가능한 고성능 사이트를 식별하여, 해석 가능하고 대칭을 고려한 나노다공성 물질 설계의 길을 열었습니다.


---

*Generated on 2025-09-23 09:20:00*