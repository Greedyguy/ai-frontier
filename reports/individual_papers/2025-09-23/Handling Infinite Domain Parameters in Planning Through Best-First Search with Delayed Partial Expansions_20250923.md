---
keywords:
  - Control Parameters in Planning
  - Best-First Search
  - Delayed Partial Expansion
  - Infinite Decision Spaces
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.03953
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:32:40.232110",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Control Parameters in Planning",
    "Best-First Search",
    "Delayed Partial Expansion",
    "Infinite Decision Spaces"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Control Parameters in Planning": 0.78,
    "Best-First Search": 0.8,
    "Delayed Partial Expansion": 0.77,
    "Infinite Decision Spaces": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "control parameters",
        "canonical": "Control Parameters in Planning",
        "aliases": [
          "decision variables",
          "numeric decision variables"
        ],
        "category": "unique_technical",
        "rationale": "Explicitly handling control parameters as decision points is a novel approach in planning, offering new connectivity opportunities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "best-first search",
        "canonical": "Best-First Search",
        "aliases": [
          "heuristic search"
        ],
        "category": "broad_technical",
        "rationale": "Best-first search is a fundamental technique in AI, linking to various search algorithms and optimization methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "delayed partial expansion",
        "canonical": "Delayed Partial Expansion",
        "aliases": [
          "incremental expansion"
        ],
        "category": "unique_technical",
        "rationale": "This technique is specific to the proposed algorithm, offering a unique link to search strategy discussions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "infinite decision spaces",
        "canonical": "Infinite Decision Spaces",
        "aliases": [
          "infinite search spaces"
        ],
        "category": "unique_technical",
        "rationale": "Handling infinite decision spaces is a unique challenge in planning, providing a specific link to complex search problems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "automated planning",
      "state-of-the-art approaches"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "control parameters",
      "resolved_canonical": "Control Parameters in Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "best-first search",
      "resolved_canonical": "Best-First Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "delayed partial expansion",
      "resolved_canonical": "Delayed Partial Expansion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "infinite decision spaces",
      "resolved_canonical": "Infinite Decision Spaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Handling Infinite Domain Parameters in Planning Through Best-First Search with Delayed Partial Expansions

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.03953.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.03953](https://arxiv.org/abs/2509.03953)

## 🔗 유사한 논문
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (80.7% similar)
- [[2025-09-18/Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (80.7% similar)
- [[2025-09-18/Meta-Optimization and Program Search using Language Models for Task and Motion Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (79.9% similar)
- [[2025-09-23/Adaptive Overclocking_ Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals_20250923|Adaptive Overclocking: Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals]] (79.8% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Best-First Search|Best-First Search]]
**⚡ Unique Technical**: [[keywords/Control Parameters in Planning|Control Parameters in Planning]], [[keywords/Delayed Partial Expansion|Delayed Partial Expansion]], [[keywords/Infinite Decision Spaces|Infinite Decision Spaces]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.03953v2 Announce Type: replace 
Abstract: In automated planning, control parameters extend standard action representations through the introduction of continuous numeric decision variables. Existing state-of-the-art approaches have primarily handled control parameters as embedded constraints alongside other temporal and numeric restrictions, and thus have implicitly treated them as additional constraints rather than as decision points in the search space. In this paper, we propose an efficient alternative that explicitly handles control parameters as true decision points within a systematic search scheme. We develop a best-first, heuristic search algorithm that operates over infinite decision spaces defined by control parameters and prove a notion of completeness in the limit under certain conditions. Our algorithm leverages the concept of delayed partial expansion, where a state is not fully expanded but instead incrementally expands a subset of its successors. Our results demonstrate that this novel search algorithm is a competitive alternative to existing approaches for solving planning problems involving control parameters.

## 📝 요약

이 논문은 자동 계획에서 연속적인 수치 결정 변수를 포함하는 제어 매개변수를 명시적으로 다루는 새로운 방법을 제안합니다. 기존 접근법은 제어 매개변수를 추가 제약으로 취급했으나, 본 연구는 이를 탐색 공간의 실제 결정 지점으로 처리하는 효율적인 대안을 제공합니다. 제안된 알고리즘은 무한한 결정 공간에서 작동하는 최선 우선 휴리스틱 탐색 알고리즘으로, 지연된 부분 확장을 활용하여 상태를 점진적으로 확장합니다. 이 알고리즘은 특정 조건 하에서 완전성을 증명하며, 제어 매개변수를 포함한 계획 문제 해결에 있어 기존 방법들과 경쟁력 있는 대안임을 실험 결과로 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 자동 계획에서 연속적인 수치 결정 변수를 도입하여 표준 행동 표현을 확장하는 제어 매개변수를 다룹니다.
- 2. 기존 방법들은 제어 매개변수를 추가 제약으로 간주했으나, 본 연구는 이를 탐색 공간의 진정한 결정 지점으로 명시적으로 처리하는 방법을 제안합니다.
- 3. 무한한 결정 공간에서 작동하는 최선 우선 휴리스틱 탐색 알고리즘을 개발하고, 특정 조건 하에서 완전성을 증명합니다.
- 4. 상태를 완전히 확장하지 않고 후속 상태의 부분 집합을 점진적으로 확장하는 지연된 부분 확장 개념을 활용합니다.
- 5. 제안된 탐색 알고리즘은 제어 매개변수를 포함한 계획 문제 해결에 있어 기존 접근법에 대한 경쟁력 있는 대안임을 입증합니다.


---

*Generated on 2025-09-24 00:32:40*