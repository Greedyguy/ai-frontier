---
keywords:
  - Distortion-aware Brushing
  - Multidimensional Projections
  - Cluster Analysis
  - Geospatial Data
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2201.06379
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:10:22.375656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Distortion-aware Brushing",
    "Multidimensional Projections",
    "Cluster Analysis",
    "Geospatial Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Distortion-aware Brushing": 0.88,
    "Multidimensional Projections": 0.82,
    "Cluster Analysis": 0.78,
    "Geospatial Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Distortion-aware brushing",
        "canonical": "Distortion-aware Brushing",
        "aliases": [
          "Distortion-aware brushing technique"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper specifically for improving cluster analysis in multidimensional projections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.92,
        "link_intent_score": 0.88
      },
      {
        "surface": "Multidimensional Projections",
        "canonical": "Multidimensional Projections",
        "aliases": [
          "MD Projections",
          "MDPs"
        ],
        "category": "specific_connectable",
        "rationale": "A key concept in the paper, essential for understanding the context of the proposed technique.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.83,
        "link_intent_score": 0.82
      },
      {
        "surface": "Cluster analysis",
        "canonical": "Cluster Analysis",
        "aliases": [
          "Clustering"
        ],
        "category": "broad_technical",
        "rationale": "Fundamental to the paper's focus, linking it to a wide range of related research in data analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Geospatial data",
        "canonical": "Geospatial Data",
        "aliases": [
          "Spatial data"
        ],
        "category": "specific_connectable",
        "rationale": "One of the use cases demonstrating the technique's effectiveness, connecting it to spatial data analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "interaction technique",
      "user studies",
      "points"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Distortion-aware brushing",
      "resolved_canonical": "Distortion-aware Brushing",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.92,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Multidimensional Projections",
      "resolved_canonical": "Multidimensional Projections",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.83,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Cluster analysis",
      "resolved_canonical": "Cluster Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Geospatial data",
      "resolved_canonical": "Geospatial Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Distortion-Aware Brushing for Reliable Cluster Analysis in Multidimensional Projections

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2201.06379.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2201.06379](https://arxiv.org/abs/2201.06379)

## 🔗 유사한 논문
- [[2025-09-24/Graph-based Clustering Revisited_ A Relaxation of Kernel $k$-Means Perspective_20250924|Graph-based Clustering Revisited: A Relaxation of Kernel $k$-Means Perspective]] (80.2% similar)
- [[2025-09-24/Subspace Clustering of Subspaces_ Unifying Canonical Correlation Analysis and Subspace Clustering_20250924|Subspace Clustering of Subspaces: Unifying Canonical Correlation Analysis and Subspace Clustering]] (79.6% similar)
- [[2025-09-23/Bilateral Distribution Compression_ Reducing Both Data Size and Dimensionality_20250923|Bilateral Distribution Compression: Reducing Both Data Size and Dimensionality]] (79.4% similar)
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC: Federated Heat Kernel Multi-View Clustering]] (79.3% similar)
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Cluster Analysis|Cluster Analysis]]
**🔗 Specific Connectable**: [[keywords/Multidimensional Projections|Multidimensional Projections]], [[keywords/Geospatial Data|Geospatial Data]]
**⚡ Unique Technical**: [[keywords/Distortion-aware Brushing|Distortion-aware Brushing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2201.06379v3 Announce Type: replace-cross 
Abstract: Brushing is a common interaction technique in 2D scatterplots, allowing users to select clustered points within a continuous, enclosed region for further analysis or filtering. However, applying conventional brushing to 2D representations of multidimensional (MD) data, i.e., Multidimensional Projections (MDPs), can lead to unreliable cluster analysis due to MDP-induced distortions that inaccurately represent the cluster structure of the original MD data. To alleviate this problem, we introduce a novel brushing technique for MDPs called Distortion-aware brushing. As users perform brushing, Distortion-aware brushing corrects distortions around the currently brushed points by dynamically relocating points in the projection, pulling data points close to the brushed points in MD space while pushing distant ones apart. This dynamic adjustment helps users brush MD clusters more accurately, leading to more reliable cluster analysis. Our user studies with 24 participants show that Distortion-aware brushing significantly outperforms previous brushing techniques for MDPs in accurately separating clusters in the MD space and remains robust against distortions. We further demonstrate the effectiveness of our technique through two use cases: (1) conducting cluster analysis of geospatial data and (2) interactively labeling MD clusters.

## 📝 요약

이 논문은 다차원 투영(MDP)에서의 왜곡 문제를 해결하기 위해 새로운 브러싱 기법인 '왜곡 인식 브러싱'을 제안합니다. 기존의 브러싱 기법은 MDP의 왜곡으로 인해 클러스터 구조를 정확히 분석하기 어려웠습니다. '왜곡 인식 브러싱'은 사용자가 브러싱을 수행할 때, 선택된 점 주변의 왜곡을 동적으로 조정하여 다차원 공간에서의 클러스터를 더 정확하게 구분할 수 있도록 합니다. 24명의 참가자를 대상으로 한 사용자 연구에서 이 기법은 기존 방법보다 클러스터를 더 정확하게 구분하고 왜곡에 강인함을 보였습니다. 이 기법의 효과는 지리 공간 데이터의 클러스터 분석과 다차원 클러스터의 상호작용적 레이블링 사례를 통해 입증되었습니다.

## 🎯 주요 포인트

- 1. 다차원 투영(MDP)에서 발생하는 왜곡 문제를 해결하기 위해 왜곡 인식 브러싱 기법을 제안합니다.
- 2. 왜곡 인식 브러싱은 브러싱 시점에 주변 포인트의 왜곡을 동적으로 수정하여 MD 공간에서의 클러스터 분석 정확성을 높입니다.
- 3. 사용자 연구 결과, 왜곡 인식 브러싱은 기존 기법보다 MD 공간에서 클러스터를 정확하게 분리하는 데 효과적임을 확인했습니다.
- 4. 제안된 기법은 지리 공간 데이터의 클러스터 분석 및 MD 클러스터의 상호작용적 레이블링에 유용하게 활용될 수 있습니다.


---

*Generated on 2025-09-25 17:10:22*