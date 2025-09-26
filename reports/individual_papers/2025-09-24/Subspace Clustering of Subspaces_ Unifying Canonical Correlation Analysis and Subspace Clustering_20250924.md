<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:54:14.300131",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Subspace Clustering of Subspaces",
    "Generalized Canonical Correlation Analysis",
    "Block Term Decomposition",
    "Hyperspectral Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Subspace Clustering of Subspaces": 0.78,
    "Generalized Canonical Correlation Analysis": 0.81,
    "Block Term Decomposition": 0.75,
    "Hyperspectral Imaging": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Subspace Clustering of Subspaces",
        "canonical": "Subspace Clustering of Subspaces",
        "aliases": [
          "SCoS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept distinct from traditional subspace clustering, enhancing understanding of matrix-based clustering.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Generalized Canonical Correlation Analysis",
        "canonical": "Generalized Canonical Correlation Analysis",
        "aliases": [
          "GCCA"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing concepts in statistical analysis, facilitating connections with related methodologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "Block Term Decomposition",
        "canonical": "Block Term Decomposition",
        "aliases": [
          "BTD"
        ],
        "category": "unique_technical",
        "rationale": "Key technique for tensor decomposition, relevant for understanding the mathematical foundation of the approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Hyperspectral Imaging",
        "canonical": "Hyperspectral Imaging",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Represents a practical application domain, useful for linking to real-world datasets and challenges.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "matrix",
      "data sample",
      "noise",
      "interference"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Subspace Clustering of Subspaces",
      "resolved_canonical": "Subspace Clustering of Subspaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Generalized Canonical Correlation Analysis",
      "resolved_canonical": "Generalized Canonical Correlation Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Block Term Decomposition",
      "resolved_canonical": "Block Term Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Hyperspectral Imaging",
      "resolved_canonical": "Hyperspectral Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Subspace Clustering of Subspaces: Unifying Canonical Correlation Analysis and Subspace Clustering

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18653.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18653](https://arxiv.org/abs/2509.18653)

## 🔗 유사한 논문
- [[2025-09-23/Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images_20250923|Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images]] (85.3% similar)
- [[2025-09-23/Kernel K-means clustering of distributional data_20250923|Kernel K-means clustering of distributional data]] (81.3% similar)
- [[2025-09-22/Personalized Federated Learning with Heat-Kernel Enhanced Tensorized Multi-View Clustering_20250922|Personalized Federated Learning with Heat-Kernel Enhanced Tensorized Multi-View Clustering]] (81.2% similar)
- [[2025-09-24/Hyperbolic Coarse-to-Fine Few-Shot Class-Incremental Learning_20250924|Hyperbolic Coarse-to-Fine Few-Shot Class-Incremental Learning]] (81.1% similar)
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generalized Canonical Correlation Analysis|Generalized Canonical Correlation Analysis]], [[keywords/Hyperspectral Imaging|Hyperspectral Imaging]]
**⚡ Unique Technical**: [[keywords/Subspace Clustering of Subspaces|Subspace Clustering of Subspaces]], [[keywords/Block Term Decomposition|Block Term Decomposition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18653v1 Announce Type: new 
Abstract: We introduce a novel framework for clustering a collection of tall matrices based on their column spaces, a problem we term Subspace Clustering of Subspaces (SCoS). Unlike traditional subspace clustering methods that assume vectorized data, our formulation directly models each data sample as a matrix and clusters them according to their underlying subspaces. We establish conceptual links to Subspace Clustering and Generalized Canonical Correlation Analysis (GCCA), and clarify key differences that arise in this more general setting. Our approach is based on a Block Term Decomposition (BTD) of a third-order tensor constructed from the input matrices, enabling joint estimation of cluster memberships and partially shared subspaces. We provide the first identifiability results for this formulation and propose scalable optimization algorithms tailored to large datasets. Experiments on real-world hyperspectral imaging datasets demonstrate that our method achieves superior clustering accuracy and robustness, especially under high noise and interference, compared to existing subspace clustering techniques. These results highlight the potential of the proposed framework in challenging high-dimensional applications where structure exists beyond individual data vectors.

## 📝 요약

이 논문은 열 공간을 기반으로 하는 긴 행렬 모음의 클러스터링을 위한 새로운 프레임워크인 SCoS(Subspace Clustering of Subspaces)를 소개합니다. 전통적인 방법과 달리, 각 데이터 샘플을 행렬로 모델링하여 기저 부분 공간에 따라 클러스터링합니다. 이 방법은 입력 행렬로부터 생성된 3차 텐서의 블록 항 분해(BTD)를 기반으로 하며, 클러스터 멤버십과 부분적으로 공유되는 부분 공간을 공동 추정할 수 있습니다. 이론적 식별 가능성을 처음으로 제시하고, 대규모 데이터셋에 적합한 최적화 알고리즘을 제안합니다. 실제 고광도 영상 데이터셋 실험에서, 높은 노이즈와 간섭 상황에서도 기존 방법보다 우수한 클러스터링 정확도와 견고성을 보였습니다. 이 프레임워크는 고차원 응용 분야에서의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 새로운 프레임워크 SCoS는 열 공간을 기반으로 한 긴 행렬 집합의 클러스터링 문제를 해결합니다.
- 2. 기존의 벡터화된 데이터 가정과 달리, 각 데이터 샘플을 행렬로 모델링하여 기저 부분 공간에 따라 클러스터링합니다.
- 3. 입력 행렬로부터 구성된 3차 텐서의 블록 항 분해(BTD)를 통해 클러스터 멤버십과 부분적으로 공유된 부분 공간을 공동 추정합니다.
- 4. 이 접근법은 대규모 데이터셋에 적합한 확장 가능한 최적화 알고리즘을 제안하며, 최초의 식별 가능성 결과를 제공합니다.
- 5. 실제 하이퍼스펙트럼 이미징 데이터셋 실험에서, 높은 노이즈와 간섭 하에서도 기존 기법보다 우수한 클러스터링 정확도와 견고성을 보여줍니다.


---

*Generated on 2025-09-24 14:54:14*