---
keywords:
  - Differentially Private Synthetic Graphs
  - Triangle-Motif Cuts
  - Graph Clustering
  - Local Sensitivity of Triangles
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2507.14835
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:07:15.070784",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Differentially Private Synthetic Graphs",
    "Triangle-Motif Cuts",
    "Graph Clustering",
    "Local Sensitivity of Triangles"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Differentially Private Synthetic Graphs": 0.78,
    "Triangle-Motif Cuts": 0.77,
    "Graph Clustering": 0.75,
    "Local Sensitivity of Triangles": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Differentially Private Synthetic Graphs",
        "canonical": "Differentially Private Synthetic Graphs",
        "aliases": [
          "DP Synthetic Graphs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and represents a novel approach in graph privacy.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Triangle-Motif Cuts",
        "canonical": "Triangle-Motif Cuts",
        "aliases": [
          "Triangle Cuts",
          "Motif Cuts"
        ],
        "category": "unique_technical",
        "rationale": "The concept is specific to graph theory and essential for understanding the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Graph Clustering",
        "canonical": "Graph Clustering",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Graph clustering is a widely used technique in network analysis, relevant to the paper's context.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Local Sensitivity of Triangles",
        "canonical": "Local Sensitivity of Triangles",
        "aliases": [
          "Triangle Sensitivity"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the privacy mechanism described in the paper.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "algorithm",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Differentially Private Synthetic Graphs",
      "resolved_canonical": "Differentially Private Synthetic Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Triangle-Motif Cuts",
      "resolved_canonical": "Triangle-Motif Cuts",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Graph Clustering",
      "resolved_canonical": "Graph Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Local Sensitivity of Triangles",
      "resolved_canonical": "Local Sensitivity of Triangles",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Differentially Private Synthetic Graphs Preserving Triangle-Motif Cuts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.14835.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2507.14835](https://arxiv.org/abs/2507.14835)

## 🔗 유사한 논문
- [[2025-09-22/DP-GTR_ Differentially Private Prompt Protection via Group Text Rewriting_20250922|DP-GTR: Differentially Private Prompt Protection via Group Text Rewriting]] (81.0% similar)
- [[2025-09-23/Preserving Node-level Privacy in Graph Neural Networks_20250923|Preserving Node-level Privacy in Graph Neural Networks]] (80.9% similar)
- [[2025-09-22/Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph_20250922|Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph]] (80.4% similar)
- [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench: A Benchmark for Differentially Private Text Generation]] (79.9% similar)
- [[2025-09-23/Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming_20250923|Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Graph Clustering|Graph Clustering]]
**⚡ Unique Technical**: [[keywords/Differentially Private Synthetic Graphs|Differentially Private Synthetic Graphs]], [[keywords/Triangle-Motif Cuts|Triangle-Motif Cuts]], [[keywords/Local Sensitivity of Triangles|Local Sensitivity of Triangles]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.14835v2 Announce Type: replace-cross 
Abstract: We study the problem of releasing a differentially private (DP) synthetic graph $G'$ that well approximates the triangle-motif sizes of all cuts of any given graph $G$, where a motif in general refers to a frequently occurring subgraph within complex networks. Non-private versions of such graphs have found applications in diverse fields such as graph clustering, graph sparsification, and social network analysis. Specifically, we present the first $(\varepsilon,\delta)$-DP mechanism that, given an input graph $G$ with $n$ vertices, $m$ edges and local sensitivity of triangles $\ell_{3}(G)$, generates a synthetic graph $G'$ in polynomial time, approximating the triangle-motif sizes of all cuts $(S,V\setminus S)$ of the input graph $G$ up to an additive error of $\tilde{O}(\sqrt{m\ell_{3}(G)}n/\varepsilon^{3/2})$. Additionally, we provide a lower bound of $\Omega(\sqrt{mn}\ell_{3}(G)/\varepsilon)$ on the additive error for any DP algorithm that answers the triangle-motif size queries of all $(S,T)$-cut of $G$. Finally, our algorithm generalizes to weighted graphs, and our lower bound extends to any $K_h$-motif cut for any constant $h\geq 2$.

## 📝 요약

이 논문은 주어진 그래프 $G$의 삼각형 모티프 크기를 잘 근사하는 차등 사생활 보호(DP) 합성 그래프 $G'$를 생성하는 문제를 다룹니다. 이는 그래프 클러스터링, 그래프 희소화, 소셜 네트워크 분석 등 다양한 분야에 응용될 수 있습니다. 저자들은 입력 그래프 $G$의 삼각형 모티프 크기를 모든 컷에 대해 근사하는 최초의 $(\varepsilon,\delta)$-DP 메커니즘을 제안합니다. 이 메커니즘은 다항 시간 내에 작동하며, 근사 오차는 $\tilde{O}(\sqrt{m\ell_{3}(G)}n/\varepsilon^{3/2})$입니다. 또한, 모든 DP 알고리즘에 대한 하한선은 $\Omega(\sqrt{mn}\ell_{3}(G)/\varepsilon)$로 제시됩니다. 이 알고리즘은 가중치 그래프로 일반화되며, 하한선은 모든 $K_h$-모티프 컷에 확장됩니다.

## 🎯 주요 포인트

- 1. 본 연구는 차등 프라이버시(DP)를 만족하는 합성 그래프 $G'$를 생성하여 주어진 그래프 $G$의 모든 컷의 삼각형 모티프 크기를 잘 근사하는 문제를 다룹니다.
- 2. 제안된 $(\varepsilon,\delta)$-DP 메커니즘은 입력 그래프 $G$의 삼각형의 지역 민감도 $\ell_{3}(G)$를 고려하여, 다항 시간 내에 합성 그래프 $G'$를 생성합니다.
- 3. 제안된 알고리즘은 모든 컷 $(S,V\setminus S)$의 삼각형 모티프 크기를 $\tilde{O}(\sqrt{m\ell_{3}(G)}n/\varepsilon^{3/2})$의 추가 오차 내에서 근사합니다.
- 4. 본 연구는 모든 DP 알고리즘에 대해 삼각형 모티프 크기 쿼리의 추가 오차에 대한 하한을 $\Omega(\sqrt{mn}\ell_{3}(G)/\varepsilon)$로 제공합니다.
- 5. 제안된 알고리즘은 가중 그래프로 일반화되며, 하한은 임의의 상수 $h\geq 2$에 대한 $K_h$-모티프 컷으로 확장됩니다.


---

*Generated on 2025-09-24 03:07:15*