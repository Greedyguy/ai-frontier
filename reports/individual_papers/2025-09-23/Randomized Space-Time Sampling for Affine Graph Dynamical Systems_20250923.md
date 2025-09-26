---
keywords:
  - Dynamical Sampling
  - Graph Signals
  - Spectral Graph Coherence
  - Restricted Isometry Property
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16818
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:16:39.603252",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamical Sampling",
    "Graph Signals",
    "Spectral Graph Coherence",
    "Restricted Isometry Property"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamical Sampling": 0.78,
    "Graph Signals": 0.82,
    "Spectral Graph Coherence": 0.77,
    "Restricted Isometry Property": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dynamical sampling",
        "canonical": "Dynamical Sampling",
        "aliases": [
          "dynamic sampling"
        ],
        "category": "unique_technical",
        "rationale": "Dynamical sampling is central to the paper's contribution and offers a novel approach to signal processing on graphs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "graph signals",
        "canonical": "Graph Signals",
        "aliases": [
          "graph-based signals"
        ],
        "category": "specific_connectable",
        "rationale": "Graph signals are integral to understanding the paper's context within graph theory and signal processing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "spectral graph weighted coherence",
        "canonical": "Spectral Graph Coherence",
        "aliases": [
          "graph coherence"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for the analysis of sampling distribution and graph structure interplay.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Restricted Isometry Property",
        "canonical": "Restricted Isometry Property",
        "aliases": [
          "RIP"
        ],
        "category": "broad_technical",
        "rationale": "RIP is a fundamental concept in signal processing and compressive sensing, relevant to the paper's stability analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "system matrix",
      "sampling design"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "dynamical sampling",
      "resolved_canonical": "Dynamical Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "graph signals",
      "resolved_canonical": "Graph Signals",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "spectral graph weighted coherence",
      "resolved_canonical": "Spectral Graph Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Restricted Isometry Property",
      "resolved_canonical": "Restricted Isometry Property",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Randomized Space-Time Sampling for Affine Graph Dynamical Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16818.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16818](https://arxiv.org/abs/2509.16818)

## 🔗 유사한 논문
- [[2025-09-18/Sampling Method for Generalized Graph Signals with Pre-selected Vertices via DC Optimization_20250918|Sampling Method for Generalized Graph Signals with Pre-selected Vertices via DC Optimization]] (84.4% similar)
- [[2025-09-22/Permutation recovery of spikes in noisy high-dimensional tensor estimation_20250922|Permutation recovery of spikes in noisy high-dimensional tensor estimation]] (82.0% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (79.7% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation: A Robustness Analysis]] (79.7% similar)
- [[2025-09-23/Sublinear Time Quantum Sensitivity Sampling_20250923|Sublinear Time Quantum Sensitivity Sampling]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Restricted Isometry Property|Restricted Isometry Property]]
**🔗 Specific Connectable**: [[keywords/Graph Signals|Graph Signals]]
**⚡ Unique Technical**: [[keywords/Dynamical Sampling|Dynamical Sampling]], [[keywords/Spectral Graph Coherence|Spectral Graph Coherence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16818v1 Announce Type: cross 
Abstract: This paper investigates the problem of dynamical sampling for graph signals influenced by a constant source term. We consider signals evolving over time according to a linear dynamical system on a graph, where both the initial state and the source term are bandlimited. We introduce two random space-time sampling regimes and analyze the conditions under which stable recovery is achievable. While our framework extends recent work on homogeneous dynamics, it addresses a fundamentally different setting where the evolution includes a constant source term. This results in a non-orthogonal-diagonalizable system matrix, rendering classical spectral techniques inapplicable and introducing new challenges in sampling design, stability analysis, and joint recovery of both the initial state and the forcing term. A key component of our analysis is the spectral graph weighted coherence, which characterizes the interplay between the sampling distribution and the graph structure. We establish sampling complexity bounds ensuring stable recovery via the Restricted Isometry Property (RIP), and develop a robust recovery algorithm with provable error guarantees. The effectiveness of our method is validated through extensive experiments on both synthetic and real-world datasets.

## 📝 요약

이 논문은 일정한 소스 항에 의해 영향을 받는 그래프 신호의 동적 샘플링 문제를 연구합니다. 초기 상태와 소스 항이 밴드 제한된 선형 동적 시스템을 고려하며, 두 가지 랜덤 시공간 샘플링 체계를 도입하여 안정적인 복구 조건을 분석합니다. 기존의 균질 동역학 연구를 확장하면서도 상수 소스 항을 포함하는 비정형 시스템 행렬을 다루어 새로운 샘플링 설계, 안정성 분석, 초기 상태 및 소스 항의 공동 복구 문제를 해결합니다. 스펙트럼 그래프 가중치 일관성을 통해 샘플링 분포와 그래프 구조 간의 상호작용을 특성화하고, 제한된 등각성 속성을 통해 안정적 복구를 보장하는 샘플링 복잡성 경계를 설정합니다. 또한, 오류 보장이 있는 강력한 복구 알고리즘을 개발하고, 이를 합성 및 실제 데이터셋을 통해 검증합니다.

## 🎯 주요 포인트

- 1. 본 논문은 일정한 소스 항에 의해 영향을 받는 그래프 신호의 동적 샘플링 문제를 연구합니다.
- 2. 초기 상태와 소스 항이 밴드 제한된 선형 동적 시스템에서 신호의 시간적 진화를 고려합니다.
- 3. 두 가지 랜덤 시공간 샘플링 체계를 도입하고 안정적인 복구가 가능한 조건을 분석합니다.
- 4. 기존의 균질 동역학 연구를 확장하면서도 상수 소스 항을 포함하는 비정형 설정을 다룹니다.
- 5. 제한된 등방성 속성(RIP)을 통해 안정적인 복구를 보장하는 샘플링 복잡도 경계를 확립하고, 오류 보장이 있는 강력한 복구 알고리즘을 개발합니다.


---

*Generated on 2025-09-24 02:16:39*