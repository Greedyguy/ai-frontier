---
keywords:
  - Kernel K-means Clustering
  - Reproducing Kernel Hilbert Space
  - Kernel Mean Embedding
  - Synthetic Aperture Radar
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18037
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:29:47.424274",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kernel K-means Clustering",
    "Reproducing Kernel Hilbert Space",
    "Kernel Mean Embedding",
    "Synthetic Aperture Radar"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kernel K-means Clustering": 0.78,
    "Reproducing Kernel Hilbert Space": 0.85,
    "Kernel Mean Embedding": 0.8,
    "Synthetic Aperture Radar": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kernel K-means",
        "canonical": "Kernel K-means Clustering",
        "aliases": [
          "Kernel K-means"
        ],
        "category": "unique_technical",
        "rationale": "Kernel K-means Clustering is a specific method that enhances traditional K-means by using kernel methods, making it a unique technical concept in clustering.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reproducing Kernel Hilbert Space",
        "canonical": "Reproducing Kernel Hilbert Space",
        "aliases": [
          "RKHS"
        ],
        "category": "specific_connectable",
        "rationale": "RKHS is a fundamental concept in machine learning and signal processing, providing a framework for kernel methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Kernel Mean Embedding",
        "canonical": "Kernel Mean Embedding",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Kernel Mean Embedding is a novel technique for embedding distributions into RKHS, crucial for the proposed clustering method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Synthetic Aperture Radar images",
        "canonical": "Synthetic Aperture Radar",
        "aliases": [
          "SAR"
        ],
        "category": "specific_connectable",
        "rationale": "Synthetic Aperture Radar is a specific application domain where the clustering method is demonstrated, linking to remote sensing and image analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "clustering",
      "sample",
      "procedure"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kernel K-means",
      "resolved_canonical": "Kernel K-means Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reproducing Kernel Hilbert Space",
      "resolved_canonical": "Reproducing Kernel Hilbert Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Kernel Mean Embedding",
      "resolved_canonical": "Kernel Mean Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Synthetic Aperture Radar images",
      "resolved_canonical": "Synthetic Aperture Radar",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Kernel K-means clustering of distributional data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18037.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18037](https://arxiv.org/abs/2509.18037)

## 🔗 유사한 논문
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC: Federated Heat Kernel Multi-View Clustering]] (80.8% similar)
- [[2025-09-22/Personalized Federated Learning with Heat-Kernel Enhanced Tensorized Multi-View Clustering_20250922|Personalized Federated Learning with Heat-Kernel Enhanced Tensorized Multi-View Clustering]] (80.7% similar)
- [[2025-09-22/Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution_20250922|Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution]] (79.4% similar)
- [[2025-09-23/EMPEROR_ Efficient Moment-Preserving Representation of Distributions_20250923|EMPEROR: Efficient Moment-Preserving Representation of Distributions]] (78.9% similar)
- [[2025-09-23/Fast, Accurate and Interpretable Graph Classification with Topological Kernels_20250923|Fast, Accurate and Interpretable Graph Classification with Topological Kernels]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reproducing Kernel Hilbert Space|Reproducing Kernel Hilbert Space]], [[keywords/Synthetic Aperture Radar|Synthetic Aperture Radar]]
**⚡ Unique Technical**: [[keywords/Kernel K-means Clustering|Kernel K-means Clustering]], [[keywords/Kernel Mean Embedding|Kernel Mean Embedding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18037v1 Announce Type: cross 
Abstract: We consider the problem of clustering a sample of probability distributions from a random distribution on $\mathbb R^p$. Our proposed partitioning method makes use of a symmetric, positive-definite kernel $k$ and its associated reproducing kernel Hilbert space (RKHS) $\mathcal H$. By mapping each distribution to its corresponding kernel mean embedding in $\mathcal H$, we obtain a sample in this RKHS where we carry out the $K$-means clustering procedure, which provides an unsupervised classification of the original sample. The procedure is simple and computationally feasible even for dimension $p>1$. The simulation studies provide insight into the choice of the kernel and its tuning parameter. The performance of the proposed clustering procedure is illustrated on a collection of Synthetic Aperture Radar (SAR) images.

## 📝 요약

이 논문은 확률 분포 샘플을 클러스터링하는 문제를 다룹니다. 제안된 방법은 대칭적이고 양의 정부호인 커널과 관련된 재생 커널 힐베르트 공간(RKHS)을 활용합니다. 각 분포를 커널 평균 임베딩으로 매핑하여 RKHS에서 샘플을 얻고, 여기서 K-평균 클러스터링을 수행하여 원래 샘플을 비지도 학습으로 분류합니다. 이 방법은 차원이 1보다 큰 경우에도 간단하고 계산적으로 효율적입니다. 시뮬레이션 연구를 통해 커널 선택과 조정 매개변수에 대한 통찰을 제공하며, 제안된 클러스터링 방법의 성능은 합성 개구 레이더(SAR) 이미지 모음에서 입증되었습니다.

## 🎯 주요 포인트

- 1. 확률 분포 샘플을 클러스터링하기 위해 대칭 양의 정부호 커널과 관련된 재생 커널 힐베르트 공간(RKHS)을 활용하는 방법을 제안합니다.
- 2. 각 분포를 커널 평균 임베딩으로 매핑하여 RKHS에서 $K$-means 클러스터링을 수행함으로써 원래 샘플의 비지도 분류를 제공합니다.
- 3. 제안된 방법은 차원이 $p>1$인 경우에도 간단하고 계산적으로 실행 가능합니다.
- 4. 시뮬레이션 연구를 통해 커널 선택과 조정 매개변수에 대한 통찰을 제공합니다.
- 5. 제안된 클러스터링 절차의 성능은 합성 개구 레이더(SAR) 이미지 모음에서 입증되었습니다.


---

*Generated on 2025-09-24 02:29:47*