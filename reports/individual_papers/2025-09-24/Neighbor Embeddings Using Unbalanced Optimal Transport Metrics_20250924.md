<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:18:21.288868",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hellinger--Kantorovich Metric",
    "Unbalanced Optimal Transport",
    "Dimensionality Reduction",
    "MedMNIST"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hellinger--Kantorovich Metric": 0.78,
    "Unbalanced Optimal Transport": 0.77,
    "Dimensionality Reduction": 0.72,
    "MedMNIST": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hellinger--Kantorovich metric",
        "canonical": "Hellinger--Kantorovich Metric",
        "aliases": [
          "HK metric"
        ],
        "category": "unique_technical",
        "rationale": "The Hellinger--Kantorovich metric is a unique technical concept central to the paper's methodology, offering potential for new research connections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "unbalanced optimal transport",
        "canonical": "Unbalanced Optimal Transport",
        "aliases": [
          "UOT"
        ],
        "category": "unique_technical",
        "rationale": "Unbalanced optimal transport is a specific technical approach that enhances dimensionality reduction techniques, relevant for specialized research discussions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "dimensionality reduction",
        "canonical": "Dimensionality Reduction",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Dimensionality reduction is a fundamental concept in machine learning, facilitating connections across various technical domains.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "MedMNIST datasets",
        "canonical": "MedMNIST",
        "aliases": [
          "MedMNIST dataset"
        ],
        "category": "specific_connectable",
        "rationale": "MedMNIST is a specific dataset used for benchmarking, providing a concrete link to empirical research in medical imaging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hellinger--Kantorovich metric",
      "resolved_canonical": "Hellinger--Kantorovich Metric",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "unbalanced optimal transport",
      "resolved_canonical": "Unbalanced Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "dimensionality reduction",
      "resolved_canonical": "Dimensionality Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "MedMNIST datasets",
      "resolved_canonical": "MedMNIST",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Neighbor Embeddings Using Unbalanced Optimal Transport Metrics

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19226.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19226](https://arxiv.org/abs/2509.19226)

## 🔗 유사한 논문
- [[2025-09-23/HOTA_ Hamiltonian framework for Optimal Transport Advection_20250923|HOTA: Hamiltonian framework for Optimal Transport Advection]] (84.2% similar)
- [[2025-09-22/Fast OTSU Thresholding Using Bisection Method_20250922|Fast OTSU Thresholding Using Bisection Method]] (80.0% similar)
- [[2025-09-23/Optimal Transport for Handwritten Text Recognition in a Low-Resource Regime_20250923|Optimal Transport for Handwritten Text Recognition in a Low-Resource Regime]] (79.9% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (79.3% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading: An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dimensionality Reduction|Dimensionality Reduction]]
**🔗 Specific Connectable**: [[keywords/MedMNIST|MedMNIST]]
**⚡ Unique Technical**: [[keywords/Hellinger--Kantorovich Metric|Hellinger--Kantorovich Metric]], [[keywords/Unbalanced Optimal Transport|Unbalanced Optimal Transport]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19226v1 Announce Type: cross 
Abstract: This paper proposes the use of the Hellinger--Kantorovich metric from unbalanced optimal transport (UOT) in a dimensionality reduction and learning (supervised and unsupervised) pipeline. The performance of UOT is compared to that of regular OT and Euclidean-based dimensionality reduction methods on several benchmark datasets including MedMNIST. The experimental results demonstrate that, on average, UOT shows improvement over both Euclidean and OT-based methods as verified by statistical hypothesis tests. In particular, on the MedMNIST datasets, UOT outperforms OT in classification 81\% of the time. For clustering MedMNIST, UOT outperforms OT 83\% of the time and outperforms both other metrics 58\% of the time.

## 📝 요약

이 논문은 불균형 최적 수송(UOT)의 Hellinger--Kantorovich 거리를 차원 축소 및 학습(지도 및 비지도) 파이프라인에 적용하는 방법을 제안합니다. UOT의 성능은 일반적인 OT 및 유클리드 기반 차원 축소 방법과 비교되었으며, 여러 벤치마크 데이터셋에서 실험 결과를 통해 UOT가 평균적으로 더 나은 성능을 보임을 통계적 가설 검정을 통해 확인했습니다. 특히 MedMNIST 데이터셋에서 UOT는 분류에서 81%의 경우 OT를 능가했으며, 클러스터링에서는 83%의 경우 OT를, 58%의 경우 다른 두 메트릭 모두를 능가했습니다.

## 🎯 주요 포인트

- 1. 이 논문은 불균형 최적 수송(UOT)의 Hellinger--Kantorovich 메트릭을 차원 축소 및 학습 파이프라인에 사용하는 방법을 제안합니다.
- 2. UOT는 MedMNIST를 포함한 여러 벤치마크 데이터셋에서 일반적인 OT 및 유클리드 기반 차원 축소 방법과 비교됩니다.
- 3. 실험 결과, UOT는 통계적 가설 검증을 통해 유클리드 및 OT 기반 방법보다 평균적으로 개선된 성능을 보였습니다.
- 4. MedMNIST 데이터셋에서 UOT는 분류 작업에서 OT보다 81% 더 우수한 성능을 보였습니다.
- 5. MedMNIST 클러스터링 작업에서 UOT는 OT보다 83%, 다른 두 메트릭보다 58% 더 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 15:18:21*