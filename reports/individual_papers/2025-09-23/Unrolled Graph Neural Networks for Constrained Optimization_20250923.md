---
keywords:
  - Graph Neural Network
  - Constrained Optimization
  - Dual Ascent Algorithm
  - Lagrangian Saddle Point
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17156
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:47:38.666965",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Constrained Optimization",
    "Dual Ascent Algorithm",
    "Lagrangian Saddle Point"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Constrained Optimization": 0.75,
    "Dual Ascent Algorithm": 0.78,
    "Lagrangian Saddle Point": 0.72
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
          "Graph NN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's approach, facilitating connections with other works using GNNs.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Constrained Optimization",
        "canonical": "Constrained Optimization",
        "aliases": [
          "Optimization under Constraints"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on solving constrained optimization problems, which is a specific technical challenge.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Dual Ascent Algorithm",
        "canonical": "Dual Ascent Algorithm",
        "aliases": [
          "DA Algorithm"
        ],
        "category": "unique_technical",
        "rationale": "The dual ascent algorithm is a unique approach discussed in the paper, relevant for optimization techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Lagrangian Saddle Point",
        "canonical": "Lagrangian Saddle Point",
        "aliases": [
          "Saddle Point of Lagrangian"
        ],
        "category": "unique_technical",
        "rationale": "Finding a Lagrangian saddle point is key to the optimization process described in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
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
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Constrained Optimization",
      "resolved_canonical": "Constrained Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Dual Ascent Algorithm",
      "resolved_canonical": "Dual Ascent Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Lagrangian Saddle Point",
      "resolved_canonical": "Lagrangian Saddle Point",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Unrolled Graph Neural Networks for Constrained Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17156.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17156](https://arxiv.org/abs/2509.17156)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (81.4% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (80.8% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (80.8% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.4% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Constrained Optimization|Constrained Optimization]], [[keywords/Dual Ascent Algorithm|Dual Ascent Algorithm]], [[keywords/Lagrangian Saddle Point|Lagrangian Saddle Point]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17156v1 Announce Type: new 
Abstract: In this paper, we unroll the dynamics of the dual ascent (DA) algorithm in two coupled graph neural networks (GNNs) to solve constrained optimization problems. The two networks interact with each other at the layer level to find a saddle point of the Lagrangian. The primal GNN finds a stationary point for a given dual multiplier, while the dual network iteratively refines its estimates to reach an optimal solution. We force the primal and dual networks to mirror the dynamics of the DA algorithm by imposing descent and ascent constraints. We propose a joint training scheme that alternates between updating the primal and dual networks. Our numerical experiments demonstrate that our approach yields near-optimal near-feasible solutions and generalizes well to out-of-distribution (OOD) problems.

## 📝 요약

이 논문에서는 제약 최적화 문제를 해결하기 위해 두 개의 결합된 그래프 신경망(GNN)에서 이중 상승(DA) 알고리즘의 동작을 펼칩니다. 두 네트워크는 계층 수준에서 상호작용하여 라그랑지안의 안장점을 찾습니다. 기본 GNN은 주어진 이중 승수에 대해 정지점을 찾고, 이중 네트워크는 최적의 해를 찾기 위해 추정치를 반복적으로 개선합니다. 우리는 DA 알고리즘의 동작을 반영하도록 기본 및 이중 네트워크에 하강 및 상승 제약을 부과합니다. 기본 및 이중 네트워크를 번갈아 업데이트하는 공동 학습 방식을 제안합니다. 수치 실험 결과, 제안된 방법이 거의 최적에 가까운 해를 제공하며 분포 외 문제에도 잘 일반화됨을 보여줍니다.

## 🎯 주요 포인트

- 1. 이 논문에서는 두 개의 그래프 신경망(GNN)을 활용하여 제약 최적화 문제를 해결하는 이중 상승(DA) 알고리즘의 동작을 설명합니다.
- 2. 두 네트워크는 계층 수준에서 상호작용하여 라그랑지안의 안장점을 찾습니다.
- 3. 기본 GNN은 주어진 이중 승수에 대해 정지점을 찾고, 이중 네트워크는 최적의 해를 찾기 위해 추정치를 반복적으로 개선합니다.
- 4. 기본 및 이중 네트워크가 DA 알고리즘의 동작을 반영하도록 하강 및 상승 제약을 부과합니다.
- 5. 제안된 공동 학습 방식은 기본 및 이중 네트워크를 번갈아 업데이트하며, 실험 결과는 거의 최적에 가까운 해를 제공하고 분포 외 문제에 잘 일반화됨을 보여줍니다.


---

*Generated on 2025-09-24 01:47:38*