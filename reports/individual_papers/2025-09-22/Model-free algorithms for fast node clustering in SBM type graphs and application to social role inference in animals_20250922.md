---
keywords:
  - Stochastic Block Model
  - Node Clustering
  - Behavioral Ecology
  - Community Detection
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15989
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:55:49.831714",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Block Model",
    "Node Clustering",
    "Behavioral Ecology",
    "Community Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Block Model": 0.91,
    "Node Clustering": 0.79,
    "Behavioral Ecology": 0.77,
    "Community Detection": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Stochastic Block Model",
        "canonical": "Stochastic Block Model",
        "aliases": [
          "SBM"
        ],
        "category": "specific_connectable",
        "rationale": "The Stochastic Block Model is a fundamental concept in community detection, providing strong connectivity to graph theory and network analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.91
      },
      {
        "surface": "node clustering",
        "canonical": "Node Clustering",
        "aliases": [
          "graph clustering"
        ],
        "category": "unique_technical",
        "rationale": "Node clustering is a specific technique relevant to graph analysis, offering potential links to various clustering algorithms.",
        "novelty_score": 0.67,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "behavioral ecology",
        "canonical": "Behavioral Ecology",
        "aliases": [
          "animal behavior studies"
        ],
        "category": "unique_technical",
        "rationale": "Behavioral ecology is a unique application area for the discussed algorithms, connecting ecological studies with computational methods.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "community detection",
        "canonical": "Community Detection",
        "aliases": [
          "network community analysis"
        ],
        "category": "broad_technical",
        "rationale": "Community detection is a broad technical area that connects to various graph and network analysis techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "parameter inference",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Stochastic Block Model",
      "resolved_canonical": "Stochastic Block Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.91
      }
    },
    {
      "candidate_surface": "node clustering",
      "resolved_canonical": "Node Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "behavioral ecology",
      "resolved_canonical": "Behavioral Ecology",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "community detection",
      "resolved_canonical": "Community Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Model-free algorithms for fast node clustering in SBM type graphs and application to social role inference in animals

**Korean Title:** SBM 유형 그래프에서 빠른 노드 클러스터링을 위한 모델 프리 알고리즘 및 동물의 사회적 역할 추론에의 응용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15989.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15989](https://arxiv.org/abs/2509.15989)

## 🔗 유사한 논문
- [[2025-09-22/Phase Transition for Stochastic Block Model with more than $\sqrt{n}$ Communities_20250922|Phase Transition for Stochastic Block Model with more than $\sqrt{n}$ Communities]] (81.7% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (81.5% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (78.5% similar)
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (78.4% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Community Detection|Community Detection]]
**🔗 Specific Connectable**: [[keywords/Stochastic Block Model|Stochastic Block Model]]
**⚡ Unique Technical**: [[keywords/Node Clustering|Node Clustering]], [[keywords/Behavioral Ecology|Behavioral Ecology]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15989v1 Announce Type: cross 
Abstract: We propose a novel family of model-free algorithms for node clustering and parameter inference in graphs generated from the Stochastic Block Model (SBM), a fundamental framework in community detection. Drawing inspiration from the Lloyd algorithm for the $k$-means problem, our approach extends to SBMs with general edge weight distributions. We establish the consistency of our estimator under a natural identifiability condition. Through extensive numerical experiments, we benchmark our methods against state-of-the-art techniques, demonstrating significantly faster computation times with the lower order of estimation error. Finally, we validate the practical relevance of our algorithms by applying them to empirical network data from behavioral ecology.

## 🔍 Abstract (한글 번역)

arXiv:2509.15989v1 발표 유형: 교차  
초록: 우리는 커뮤니티 탐지의 기본적인 틀인 확률적 블록 모델(SBM)에서 생성된 그래프의 노드 클러스터링 및 매개변수 추론을 위한 새로운 모델 자유 알고리즘 계열을 제안합니다. $k$-평균 문제를 위한 Lloyd 알고리즘에서 영감을 받아, 우리의 접근법은 일반적인 엣지 가중치 분포를 가진 SBM으로 확장됩니다. 우리는 자연스러운 식별 가능성 조건 하에서 우리의 추정기의 일관성을 확립합니다. 광범위한 수치 실험을 통해, 우리는 최첨단 기법들과 우리의 방법을 비교하여, 추정 오류의 낮은 차수와 함께 계산 시간이 현저히 빠름을 보여줍니다. 마지막으로, 행동 생태학의 실증적 네트워크 데이터에 우리의 알고리즘을 적용하여 실질적인 관련성을 검증합니다.

## 📝 요약

이 논문은 확률적 블록 모델(SBM)에서 노드 군집화와 매개변수 추론을 위한 새로운 모델-프리 알고리즘을 제안합니다. $k$-평균 문제의 Lloyd 알고리즘에서 영감을 받아, 일반적인 엣지 가중치 분포를 가진 SBM으로 확장한 것이 특징입니다. 자연스러운 식별 가능성 조건 하에서 추정기의 일관성을 입증하였으며, 광범위한 수치 실험을 통해 최신 기법과 비교하여 계산 속도가 훨씬 빠르고 추정 오류가 낮음을 보여주었습니다. 마지막으로, 행동 생태학의 실증적 네트워크 데이터에 적용하여 알고리즘의 실용성을 검증했습니다.

## 🎯 주요 포인트

- 1. 새로운 모델 프리 알고리즘을 제안하여 확률적 블록 모델(SBM)에서 노드 클러스터링과 매개변수 추론을 수행합니다.
- 2. $k$-평균 문제의 Lloyd 알고리즘에서 영감을 받아 일반적인 엣지 가중치 분포를 가진 SBM으로 확장합니다.
- 3. 자연스러운 식별 가능성 조건 하에서 제안된 추정기의 일관성을 확립합니다.
- 4. 광범위한 수치 실험을 통해 최신 기법들과 비교하여 계산 시간이 크게 단축되고 추정 오류가 낮음을 입증합니다.
- 5. 행동 생태학의 실증적 네트워크 데이터에 알고리즘을 적용하여 실용성을 검증합니다.


---

*Generated on 2025-09-23 10:55:49*