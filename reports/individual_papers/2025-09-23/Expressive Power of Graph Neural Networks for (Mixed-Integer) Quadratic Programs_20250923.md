---
keywords:
  - Graph Neural Network
  - Quadratic Programming
  - Message-Passing Graph Neural Networks
  - Mixed-Integer Quadratic Programming
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2406.05938
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:32:49.475006",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Quadratic Programming",
    "Message-Passing Graph Neural Networks",
    "Mixed-Integer Quadratic Programming"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Quadratic Programming": 0.79,
    "Message-Passing Graph Neural Networks": 0.77,
    "Mixed-Integer Quadratic Programming": 0.75
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
        "rationale": "Graph Neural Networks are central to the paper's exploration of solving quadratic programs, making them a key node for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Quadratic Programming",
        "canonical": "Quadratic Programming",
        "aliases": [
          "QP",
          "Quadratic Programs"
        ],
        "category": "unique_technical",
        "rationale": "Quadratic Programming is the primary problem domain explored in the paper, providing a unique technical focus for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Message-Passing GNNs",
        "canonical": "Message-Passing Graph Neural Networks",
        "aliases": [
          "MP-GNNs"
        ],
        "category": "unique_technical",
        "rationale": "Message-Passing GNNs are highlighted for their theoretical capabilities in the paper, offering a specific technical concept for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mixed-Integer Quadratic Programs",
        "canonical": "Mixed-Integer Quadratic Programming",
        "aliases": [
          "MIQP"
        ],
        "category": "unique_technical",
        "rationale": "The paper addresses challenges in Mixed-Integer Quadratic Programs, making it a unique technical area for connection.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "real-time solutions",
      "matrix decomposition",
      "preconditioned conjugate gradient method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Quadratic Programming",
      "resolved_canonical": "Quadratic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Message-Passing GNNs",
      "resolved_canonical": "Message-Passing Graph Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mixed-Integer Quadratic Programs",
      "resolved_canonical": "Mixed-Integer Quadratic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Expressive Power of Graph Neural Networks for (Mixed-Integer) Quadratic Programs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2406.05938.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2406.05938](https://arxiv.org/abs/2406.05938)

## 🔗 유사한 논문
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (83.7% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (83.1% similar)
- [[2025-09-23/Unrolled Graph Neural Networks for Constrained Optimization_20250923|Unrolled Graph Neural Networks for Constrained Optimization]] (82.9% similar)
- [[2025-09-18/Towards Pre-trained Graph Condensation via Optimal Transport_20250918|Towards Pre-trained Graph Condensation via Optimal Transport]] (81.2% similar)
- [[2025-09-18/Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Quadratic Programming|Quadratic Programming]], [[keywords/Message-Passing Graph Neural Networks|Message-Passing Graph Neural Networks]], [[keywords/Mixed-Integer Quadratic Programming|Mixed-Integer Quadratic Programming]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.05938v2 Announce Type: replace 
Abstract: Quadratic programming (QP) is the most widely applied category of problems in nonlinear programming. Many applications require real-time/fast solutions, though not necessarily with high precision. Existing methods either involve matrix decomposition or use the preconditioned conjugate gradient method. For relatively large instances, these methods cannot achieve the real-time requirement unless there is an effective preconditioner. Recently, graph neural networks (GNNs) opened new possibilities for QP. Some promising empirical studies of applying GNNs for QP tasks show that GNNs can capture key characteristics of an optimization instance and provide adaptive guidance accordingly to crucial configurations during the solving process, or directly provide an approximate solution. However, the theoretical understanding of GNNs in this context remains limited. Specifically, it is unclear what GNNs can and cannot achieve for QP tasks in theory. This work addresses this gap in the context of linearly constrained QP tasks. In the continuous setting, we prove that message-passing GNNs can universally represent fundamental properties of convex quadratic programs, including feasibility, optimal objective values, and optimal solutions. In the more challenging mixed-integer setting, while GNNs are not universal approximators, we identify a subclass of QP problems that GNNs can reliably represent.

## 📝 요약

이 논문은 그래프 신경망(GNN)을 활용한 이차 계획법(QP) 문제 해결에 대한 이론적 이해를 제공하고자 합니다. 기존의 QP 해결 방법은 실시간 요구를 충족시키기 어려운 반면, GNN은 최적화 문제의 핵심 특성을 포착하여 적응형 지침을 제공하거나 근사 해를 제시할 수 있습니다. 이 연구는 선형 제약이 있는 QP 문제에서 메시지 전달 GNN이 볼록 이차 프로그램의 기본 속성인 타당성, 최적 목표 값, 최적 해를 보편적으로 표현할 수 있음을 증명합니다. 또한, 혼합 정수 설정에서는 GNN이 보편적 근사자는 아니지만, GNN이 신뢰성 있게 표현할 수 있는 QP 문제의 하위 클래스를 식별합니다.

## 🎯 주요 포인트

- 1. 이 논문은 비선형 프로그래밍에서 가장 널리 적용되는 문제인 이차 프로그래밍(QP)의 실시간 해결을 위한 새로운 접근법으로 그래프 신경망(GNN)의 가능성을 탐구합니다.
- 2. 기존 방법들은 행렬 분해나 사전 조건화된 켤레 기울기 방법을 사용하지만, 큰 문제에서는 실시간 요구를 충족하기 어렵습니다.
- 3. GNN은 최적화 인스턴스의 주요 특성을 포착하고 해결 과정에서 중요한 설정에 적응적 지침을 제공하거나 근사 해를 직접 제공할 수 있습니다.
- 4. 이 연구는 선형 제약이 있는 QP 문제에서 메시지 전달 GNN이 볼록 이차 프로그램의 기본 속성을 보편적으로 표현할 수 있음을 증명합니다.
- 5. 혼합 정수 설정에서는 GNN이 보편적 근사자가 아니지만, GNN이 신뢰할 수 있게 표현할 수 있는 QP 문제의 하위 클래스를 식별합니다.


---

*Generated on 2025-09-24 02:32:49*