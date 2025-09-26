---
keywords:
  - Entropic Causal Inference
  - Causal Graph
  - Bivariate Entropic Tests
  - Sequential Peeling Algorithm
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16463
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:21:22.985045",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Entropic Causal Inference",
    "Causal Graph",
    "Bivariate Entropic Tests",
    "Sequential Peeling Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Entropic Causal Inference": 0.78,
    "Causal Graph": 0.85,
    "Bivariate Entropic Tests": 0.72,
    "Sequential Peeling Algorithm": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "entropic causal inference",
        "canonical": "Entropic Causal Inference",
        "aliases": [
          "entropic causality",
          "causal entropy"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework specific to the paper's approach to causal graph learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "causal graph",
        "canonical": "Causal Graph",
        "aliases": [
          "causal network",
          "causal structure"
        ],
        "category": "specific_connectable",
        "rationale": "Causal graphs are central to understanding the paper's methodology and results.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "bivariate entropic tests",
        "canonical": "Bivariate Entropic Tests",
        "aliases": [
          "bivariate entropy tests"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method used in the paper to determine ancestrality in graphs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "sequential peeling algorithm",
        "canonical": "Sequential Peeling Algorithm",
        "aliases": [
          "peeling algorithm"
        ],
        "category": "unique_technical",
        "rationale": "A key algorithm introduced in the paper for causal graph identification.",
        "novelty_score": 0.78,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "observational data",
      "synthetic data",
      "real-world datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "entropic causal inference",
      "resolved_canonical": "Entropic Causal Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "causal graph",
      "resolved_canonical": "Causal Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "bivariate entropic tests",
      "resolved_canonical": "Bivariate Entropic Tests",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "sequential peeling algorithm",
      "resolved_canonical": "Sequential Peeling Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Entropic Causal Inference: Graph Identifiability

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16463.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16463](https://arxiv.org/abs/2509.16463)

## 🔗 유사한 논문
- [[2025-09-22/Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components_20250922|Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components]] (80.6% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (79.2% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation: A Robustness Analysis]] (78.8% similar)
- [[2025-09-22/Generalized Deep Multi-view Clustering via Causal Learning with Partially Aligned Cross-view Correspondence_20250922|Generalized Deep Multi-view Clustering via Causal Learning with Partially Aligned Cross-view Correspondence]] (78.3% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Causal Graph|Causal Graph]]
**⚡ Unique Technical**: [[keywords/Entropic Causal Inference|Entropic Causal Inference]], [[keywords/Bivariate Entropic Tests|Bivariate Entropic Tests]], [[keywords/Sequential Peeling Algorithm|Sequential Peeling Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16463v1 Announce Type: cross 
Abstract: Entropic causal inference is a recent framework for learning the causal graph between two variables from observational data by finding the information-theoretically simplest structural explanation of the data, i.e., the model with smallest entropy. In our work, we first extend the causal graph identifiability result in the two-variable setting under relaxed assumptions. We then show the first identifiability result using the entropic approach for learning causal graphs with more than two nodes. Our approach utilizes the property that ancestrality between a source node and its descendants can be determined using the bivariate entropic tests. We provide a sound sequential peeling algorithm for general graphs that relies on this property. We also propose a heuristic algorithm for small graphs that shows strong empirical performance. We rigorously evaluate the performance of our algorithms on synthetic data generated from a variety of models, observing improvement over prior work. Finally we test our algorithms on real-world datasets.

## 📝 요약

이 논문은 정보 이론적 접근을 통해 관찰 데이터로부터 변수 간의 인과 그래프를 학습하는 엔트로피 인과 추론 방법을 제안합니다. 저자들은 두 변수 간의 인과 그래프 식별 가능성을 완화된 가정 하에서 확장하고, 두 개 이상의 노드를 포함하는 인과 그래프에 대한 첫 번째 식별 가능성 결과를 제시합니다. 이 접근법은 소스 노드와 후손 간의 조상 관계를 이변량 엔트로피 테스트를 통해 결정할 수 있는 성질을 활용합니다. 일반 그래프에 대해 이 성질을 기반으로 한 순차적 필링 알고리즘을 제안하며, 작은 그래프에 대해서는 강력한 성능을 보이는 휴리스틱 알고리즘도 제안합니다. 다양한 모델에서 생성된 합성 데이터를 통해 알고리즘의 성능을 평가한 결과, 기존 연구보다 개선된 성과를 보였으며, 실제 데이터셋에서도 테스트를 수행했습니다.

## 🎯 주요 포인트

- 1. 엔트로피적 인과 추론은 관찰 데이터를 통해 두 변수 간의 인과 그래프를 학습하는 최근의 프레임워크로, 정보 이론적으로 가장 간단한 구조적 설명을 찾는 것을 목표로 한다.
- 2. 본 연구에서는 두 변수 설정에서 인과 그래프 식별 가능성 결과를 완화된 가정 하에 확장하였다.
- 3. 두 개 이상의 노드를 가진 인과 그래프를 학습하기 위한 엔트로피적 접근법을 사용한 최초의 식별 가능성 결과를 제시하였다.
- 4. 소스 노드와 그 자손 간의 조상 관계를 이변량 엔트로피 테스트를 통해 결정할 수 있는 속성을 활용하였다.
- 5. 일반 그래프에 대해 이 속성에 의존하는 순차적 필링 알고리즘과 소규모 그래프에 대한 경험적 성능이 우수한 휴리스틱 알고리즘을 제안하였다.


---

*Generated on 2025-09-23 23:21:22*