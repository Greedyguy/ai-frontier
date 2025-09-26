---
keywords:
  - Alternating Least Squares
  - Low-Rank Matrix Factorization
  - Recommender Systems
  - Sparse Matrix Operations
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18024
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:29:31.805113",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Alternating Least Squares",
    "Low-Rank Matrix Factorization",
    "Recommender Systems",
    "Sparse Matrix Operations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Alternating Least Squares": 0.8,
    "Low-Rank Matrix Factorization": 0.75,
    "Recommender Systems": 0.7,
    "Sparse Matrix Operations": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "alternating least squares",
        "canonical": "Alternating Least Squares",
        "aliases": [
          "ALS"
        ],
        "category": "unique_technical",
        "rationale": "Alternating Least Squares is a specific algorithm central to the paper's proposed method, enhancing connectivity with related computational techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "low-rank matrix factorization",
        "canonical": "Low-Rank Matrix Factorization",
        "aliases": [
          "matrix factorization"
        ],
        "category": "specific_connectable",
        "rationale": "Low-Rank Matrix Factorization is a key concept in the paper, linking to broader topics in matrix computations and data science.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "recommender systems",
        "canonical": "Recommender Systems",
        "aliases": [
          "recommendation systems"
        ],
        "category": "broad_technical",
        "rationale": "Recommender Systems are a major application area for the discussed methods, providing a broad technical context for linking.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "sparse matrix operations",
        "canonical": "Sparse Matrix Operations",
        "aliases": [
          "sparse operations"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse Matrix Operations are crucial for the efficiency improvements in the proposed method, connecting to computational optimizations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "efficiency",
      "applications"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "alternating least squares",
      "resolved_canonical": "Alternating Least Squares",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "low-rank matrix factorization",
      "resolved_canonical": "Low-Rank Matrix Factorization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "recommender systems",
      "resolved_canonical": "Recommender Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "sparse matrix operations",
      "resolved_canonical": "Sparse Matrix Operations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Core-elements Subsampling for Alternating Least Squares

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18024.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18024](https://arxiv.org/abs/2509.18024)

## 🔗 유사한 논문
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (80.9% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.4% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (78.7% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (78.5% similar)
- [[2025-09-22/Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization_20250922|Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Recommender Systems|Recommender Systems]]
**🔗 Specific Connectable**: [[keywords/Low-Rank Matrix Factorization|Low-Rank Matrix Factorization]], [[keywords/Sparse Matrix Operations|Sparse Matrix Operations]]
**⚡ Unique Technical**: [[keywords/Alternating Least Squares|Alternating Least Squares]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18024v1 Announce Type: cross 
Abstract: In this paper, we propose a novel element-wise subset selection method for the alternating least squares (ALS) algorithm, focusing on low-rank matrix factorization involving matrices with missing values, as commonly encountered in recommender systems. While ALS is widely used for providing personalized recommendations based on user-item interaction data, its high computational cost, stemming from repeated regression operations, poses significant challenges for large-scale datasets. To enhance the efficiency of ALS, we propose a core-elements subsampling method that selects a representative subset of data and leverages sparse matrix operations to approximate ALS estimations efficiently. We establish theoretical guarantees for the approximation and convergence of the proposed approach, showing that it achieves similar accuracy with significantly reduced computational time compared to full-data ALS. Extensive simulations and real-world applications demonstrate the effectiveness of our method in various scenarios, emphasizing its potential in large-scale recommendation systems.

## 📝 요약

이 논문에서는 추천 시스템에서 자주 사용되는 행렬의 결측값을 포함한 저랭크 행렬 분해를 위한 교대 최소자승(ALS) 알고리즘의 새로운 요소별 부분집합 선택 방법을 제안합니다. ALS는 사용자-아이템 상호작용 데이터를 기반으로 개인화된 추천을 제공하는 데 널리 사용되지만, 반복적인 회귀 연산으로 인해 대규모 데이터셋에서 높은 계산 비용이 발생합니다. 이를 개선하기 위해, 우리는 대표적인 데이터 부분집합을 선택하고 희소 행렬 연산을 활용하여 ALS 추정을 효율적으로 근사하는 핵심 요소 서브샘플링 방법을 제안합니다. 제안된 방법의 근사 및 수렴에 대한 이론적 보장을 제공하며, 전체 데이터 ALS와 유사한 정확도를 유지하면서 계산 시간을 크게 줄일 수 있음을 보여줍니다. 광범위한 시뮬레이션과 실제 응용을 통해 대규모 추천 시스템에서의 방법의 효과를 입증합니다.

## 🎯 주요 포인트

- 1. 본 논문은 ALS 알고리즘의 효율성을 높이기 위해 요소별 부분집합 선택 방법을 제안합니다.
- 2. 제안된 방법은 데이터의 대표적인 부분집합을 선택하고 희소 행렬 연산을 활용하여 ALS 추정을 효율적으로 근사합니다.
- 3. 이 접근법은 전체 데이터 ALS와 유사한 정확성을 유지하면서 계산 시간을 크게 줄이는 이점을 제공합니다.
- 4. 이론적 보장을 통해 제안된 방법의 근사 및 수렴성을 입증하였습니다.
- 5. 다양한 시뮬레이션과 실제 응용을 통해 대규모 추천 시스템에서의 효과성을 강조합니다.


---

*Generated on 2025-09-24 02:29:31*