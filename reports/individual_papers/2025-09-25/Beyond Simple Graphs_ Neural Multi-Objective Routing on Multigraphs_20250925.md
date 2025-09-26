---
keywords:
  - Graph Neural Network
  - Multigraph
  - Multi-Objective Routing
  - Pruning Strategy
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2506.22095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:29:24.471717",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Multigraph",
    "Multi-Objective Routing",
    "Pruning Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Multigraph": 0.78,
    "Multi-Objective Routing": 0.77,
    "Pruning Strategy": 0.72
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
        "rationale": "Graph Neural Networks are central to the proposed methods and connect well with existing literature on neural approaches to graph problems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multigraph",
        "canonical": "Multigraph",
        "aliases": [
          "Multi-graph",
          "Multi graph"
        ],
        "category": "unique_technical",
        "rationale": "Multigraphs are a unique focus of the paper, distinguishing it from typical graph-based studies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-Objective Routing",
        "canonical": "Multi-Objective Routing",
        "aliases": [
          "Multiobjective Routing",
          "Multi Objective Routing"
        ],
        "category": "unique_technical",
        "rationale": "The paper's primary contribution is in the domain of multi-objective routing, which is a specialized topic within routing algorithms.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Pruning Strategy",
        "canonical": "Pruning Strategy",
        "aliases": [
          "Graph Pruning",
          "Pruning Method"
        ],
        "category": "specific_connectable",
        "rationale": "Pruning strategies are crucial for simplifying multigraphs, a key step in the proposed scalable method.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multigraph",
      "resolved_canonical": "Multigraph",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-Objective Routing",
      "resolved_canonical": "Multi-Objective Routing",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Pruning Strategy",
      "resolved_canonical": "Pruning Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Beyond Simple Graphs: Neural Multi-Objective Routing on Multigraphs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.22095.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2506.22095](https://arxiv.org/abs/2506.22095)

## 🔗 유사한 논문
- [[2025-09-23/Unrolled Graph Neural Networks for Constrained Optimization_20250923|Unrolled Graph Neural Networks for Constrained Optimization]] (82.0% similar)
- [[2025-09-24/Graph Enhanced Trajectory Anomaly Detection_20250924|Graph Enhanced Trajectory Anomaly Detection]] (81.5% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (81.2% similar)
- [[2025-09-23/From domain-landmark graph learning to problem-landmark graph generation_20250923|From domain-landmark graph learning to problem-landmark graph generation]] (80.9% similar)
- [[2025-09-22/Partial Column Generation with Graph Neural Networks for Team Formation and Routing_20250922|Partial Column Generation with Graph Neural Networks for Team Formation and Routing]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Pruning Strategy|Pruning Strategy]]
**⚡ Unique Technical**: [[keywords/Multigraph|Multigraph]], [[keywords/Multi-Objective Routing|Multi-Objective Routing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.22095v3 Announce Type: replace-cross 
Abstract: Learning-based methods for routing have gained significant attention in recent years, both in single-objective and multi-objective contexts. Yet, existing methods are unsuitable for routing on multigraphs, which feature multiple edges with distinct attributes between node pairs, despite their strong relevance in real-world scenarios. In this paper, we propose two graph neural network-based methods to address multi-objective routing on multigraphs. Our first approach operates directly on the multigraph by autoregressively selecting edges until a tour is completed. The second model, which is more scalable, first simplifies the multigraph via a learned pruning strategy and then performs autoregressive routing on the resulting simple graph. We evaluate both models empirically, across a wide range of problems and graph distributions, and demonstrate their competitive performance compared to strong heuristics and neural baselines.

## 📝 요약

이 논문은 다중 그래프에서의 다중 목표 경로 문제를 해결하기 위해 두 가지 그래프 신경망 기반 방법을 제안합니다. 첫 번째 방법은 다중 그래프에서 자동 회귀적으로 경로를 선택하며, 두 번째 방법은 학습된 가지치기 전략을 통해 그래프를 단순화한 후 경로를 찾습니다. 두 모델 모두 다양한 문제와 그래프 분포에서 실험적으로 평가되었으며, 기존의 강력한 휴리스틱 및 신경망 기반 방법들과 비교해 경쟁력 있는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 최근 학습 기반 경로 설정 방법이 단일 및 다중 목표 상황에서 주목받고 있지만, 기존 방법은 다중 그래프에서의 경로 설정에 적합하지 않습니다.
- 2. 본 논문에서는 다중 그래프에서의 다중 목표 경로 설정을 해결하기 위해 두 가지 그래프 신경망 기반 방법을 제안합니다.
- 3. 첫 번째 방법은 다중 그래프에서 직접적으로 작동하며, 자동 회귀적으로 간선을 선택하여 투어를 완성합니다.
- 4. 두 번째 방법은 학습된 가지치기 전략을 통해 다중 그래프를 단순화한 후, 단순화된 그래프에서 자동 회귀 경로 설정을 수행합니다.
- 5. 제안된 두 모델은 다양한 문제와 그래프 분포에 대해 실증적으로 평가되었으며, 강력한 휴리스틱 및 신경망 기반 모델과 비교하여 경쟁력 있는 성능을 보였습니다.


---

*Generated on 2025-09-25 16:29:24*