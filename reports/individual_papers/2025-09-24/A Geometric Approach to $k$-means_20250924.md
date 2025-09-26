<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:20:13.495719",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "k-means Clustering",
    "Nonconvex Optimization",
    "Global Solution",
    "Geometric Perspective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "k-means Clustering": 0.88,
    "Nonconvex Optimization": 0.78,
    "Global Solution": 0.8,
    "Geometric Perspective": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "k-means clustering",
        "canonical": "k-means Clustering",
        "aliases": [
          "kmeans",
          "k-means"
        ],
        "category": "unique_technical",
        "rationale": "A fundamental clustering algorithm that is central to the paper's approach and widely used in various domains.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "nonconvex optimization",
        "canonical": "Nonconvex Optimization",
        "aliases": [
          "non-convex optimization"
        ],
        "category": "broad_technical",
        "rationale": "Describes the nature of the optimization problem addressed in the paper, relevant to many machine learning tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "global solution",
        "canonical": "Global Solution",
        "aliases": [
          "global optimum"
        ],
        "category": "unique_technical",
        "rationale": "Key outcome of the proposed algorithmic framework, distinguishing it from local solutions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "geometric perspective",
        "canonical": "Geometric Perspective",
        "aliases": [
          "geometric approach"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's novel approach, offering a new viewpoint on existing algorithms.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "framework",
      "solution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "k-means clustering",
      "resolved_canonical": "k-means Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "nonconvex optimization",
      "resolved_canonical": "Nonconvex Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "global solution",
      "resolved_canonical": "Global Solution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "geometric perspective",
      "resolved_canonical": "Geometric Perspective",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# A Geometric Approach to $k$-means

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2201.04822.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2201.04822](https://arxiv.org/abs/2201.04822)

## 🔗 유사한 논문
- [[2025-09-24/Graph-based Clustering Revisited_ A Relaxation of Kernel $k$-Means Perspective_20250924|Graph-based Clustering Revisited: A Relaxation of Kernel $k$-Means Perspective]] (84.0% similar)
- [[2025-09-23/Kernel K-means clustering of distributional data_20250923|Kernel K-means clustering of distributional data]] (81.6% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.0% similar)
- [[2025-09-24/Subspace Clustering of Subspaces_ Unifying Canonical Correlation Analysis and Subspace Clustering_20250924|Subspace Clustering of Subspaces: Unifying Canonical Correlation Analysis and Subspace Clustering]] (80.3% similar)
- [[2025-09-23/A geometric framework for momentum-based optimizers for low-rank training_20250923|A geometric framework for momentum-based optimizers for low-rank training]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonconvex Optimization|Nonconvex Optimization]]
**⚡ Unique Technical**: [[keywords/k-means Clustering|k-means Clustering]], [[keywords/Global Solution|Global Solution]], [[keywords/Geometric Perspective|Geometric Perspective]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2201.04822v2 Announce Type: replace 
Abstract: \kmeans clustering is a fundamental problem in many scientific and engineering domains. The optimization problem associated with \kmeans clustering is nonconvex, for which standard algorithms are only guaranteed to find a local optimum. Leveraging the hidden structure of local solutions, we propose a general algorithmic framework for escaping undesirable local solutions and recovering the global solution or the ground truth clustering. This framework consists of iteratively alternating between two steps: (i) detect mis-specified clusters in a local solution, and (ii) improve the local solution by non-local operations. We discuss specific implementation of these steps, and elucidate how the proposed framework unifies many existing variants of \kmeans algorithms through a geometric perspective. We also present two natural variants of the proposed framework, where the initial number of clusters may be over- or under-specified. We provide theoretical justifications and extensive experiments to demonstrate the efficacy of the proposed approach.

## 📝 요약

이 논문은 \kmeans 클러스터링 문제에서 비선형 최적화 문제로 인해 발생하는 지역 최적해를 극복하고 전역 최적해를 찾기 위한 알고리즘적 프레임워크를 제안합니다. 제안된 방법론은 두 단계로 구성되며, 첫째, 잘못 지정된 클러스터를 감지하고, 둘째, 비지역적 연산을 통해 지역 솔루션을 개선합니다. 이 프레임워크는 기존의 다양한 \kmeans 알고리즘을 통합하며, 초기 클러스터 수가 과대 또는 과소 지정된 경우에 대한 두 가지 변형도 제시합니다. 이 접근법의 효과는 이론적 근거와 실험을 통해 입증되었습니다.

## 🎯 주요 포인트

- 1. \kmeans 클러스터링 문제는 비볼록 최적화 문제로, 표준 알고리즘은 지역 최적해만 보장합니다.
- 2. 숨겨진 구조를 활용하여, 바람직하지 않은 지역 해를 탈출하고 전역 해를 회복하는 알고리즘 프레임워크를 제안합니다.
- 3. 제안된 프레임워크는 잘못 지정된 클러스터를 감지하고 비지역적 연산으로 지역 해를 개선하는 두 단계로 구성됩니다.
- 4. 이 프레임워크는 \kmeans 알고리즘의 여러 변형을 기하학적 관점에서 통합합니다.
- 5. 클러스터 수가 과소 또는 과대 지정된 경우를 포함한 두 가지 변형을 제시하고, 이 접근법의 효능을 이론적, 실험적으로 입증합니다.


---

*Generated on 2025-09-24 15:20:13*