---
keywords:
  - 3D Gaussian Splatting
  - Co-Adaptation Score
  - Sparse-View 3D Gaussian Splatting
  - Random Gaussian Dropout
  - Multiplicative Noise Injection
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2508.12720
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:29:28.290090",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Co-Adaptation Score",
    "Sparse-View 3D Gaussian Splatting",
    "Random Gaussian Dropout",
    "Multiplicative Noise Injection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.82,
    "Co-Adaptation Score": 0.78,
    "Sparse-View 3D Gaussian Splatting": 0.75,
    "Random Gaussian Dropout": 0.73,
    "Multiplicative Noise Injection": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a specific technique in 3D rendering.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Co-Adaptation Score",
        "canonical": "Co-Adaptation Score",
        "aliases": [
          "CA Score"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric for evaluating Gaussian entanglement, crucial for understanding the paper's contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse-View 3DGS",
        "canonical": "Sparse-View 3D Gaussian Splatting",
        "aliases": [
          "Sparse-View 3DGS"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a specific application of 3D Gaussian Splatting under sparse conditions, which is a key focus of the research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Random Gaussian Dropout",
        "canonical": "Random Gaussian Dropout",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A proposed strategy to mitigate co-adaptation, directly contributing to the paper's methodological advancements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.73
      },
      {
        "surface": "Multiplicative Noise Injection",
        "canonical": "Multiplicative Noise Injection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Another proposed strategy that enhances the understanding and application of 3DGS techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "appearance artifacts",
      "training views",
      "novel views"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Co-Adaptation Score",
      "resolved_canonical": "Co-Adaptation Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse-View 3DGS",
      "resolved_canonical": "Sparse-View 3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Random Gaussian Dropout",
      "resolved_canonical": "Random Gaussian Dropout",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "Multiplicative Noise Injection",
      "resolved_canonical": "Multiplicative Noise Injection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.12720.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2508.12720](https://arxiv.org/abs/2508.12720)

## 🔗 유사한 논문
- [[2025-09-23/Multi-viewregulated gaussian splatting for novel view synthesis_20250923|Multi-viewregulated gaussian splatting for novel view synthesis]] (86.2% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (84.0% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (83.6% similar)
- [[2025-09-23/HyRF_ Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis_20250923|HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis]] (83.0% similar)
- [[2025-09-23/From Restoration to Reconstruction_ Rethinking 3D Gaussian Splatting for Underwater Scenes_20250923|From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sparse-View 3D Gaussian Splatting|Sparse-View 3D Gaussian Splatting]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Co-Adaptation Score|Co-Adaptation Score]], [[keywords/Random Gaussian Dropout|Random Gaussian Dropout]], [[keywords/Multiplicative Noise Injection|Multiplicative Noise Injection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.12720v3 Announce Type: replace 
Abstract: 3D Gaussian Splatting (3DGS) has demonstrated impressive performance in novel view synthesis under dense-view settings. However, in sparse-view scenarios, despite the realistic renderings in training views, 3DGS occasionally manifests appearance artifacts in novel views. This paper investigates the appearance artifacts in sparse-view 3DGS and uncovers a core limitation of current approaches: the optimized Gaussians are overly-entangled with one another to aggressively fit the training views, which leads to a neglect of the real appearance distribution of the underlying scene and results in appearance artifacts in novel views. The analysis is based on a proposed metric, termed Co-Adaptation Score (CA), which quantifies the entanglement among Gaussians, i.e., co-adaptation, by computing the pixel-wise variance across multiple renderings of the same viewpoint, with different random subsets of Gaussians. The analysis reveals that the degree of co-adaptation is naturally alleviated as the number of training views increases. Based on the analysis, we propose two lightweight strategies to explicitly mitigate the co-adaptation in sparse-view 3DGS: (1) random gaussian dropout; (2) multiplicative noise injection to the opacity. Both strategies are designed to be plug-and-play, and their effectiveness is validated across various methods and benchmarks. We hope that our insights into the co-adaptation effect will inspire the community to achieve a more comprehensive understanding of sparse-view 3DGS.

## 📝 요약

이 논문은 3D Gaussian Splatting(3DGS)의 희소 뷰 상황에서 발생하는 외관 아티팩트를 조사합니다. 기존 방법의 한계는 최적화된 가우시안들이 훈련 뷰에 과도하게 맞춰져 새로운 뷰에서의 외관 분포를 무시한다는 점입니다. 이를 해결하기 위해 Co-Adaptation Score(CA)라는 새로운 지표를 제안하여 가우시안 간의 얽힘 정도를 측정합니다. 분석 결과, 훈련 뷰가 많아질수록 얽힘이 자연스럽게 완화됨을 발견했습니다. 이를 기반으로, 희소 뷰 3DGS에서의 얽힘을 줄이기 위한 두 가지 경량 전략을 제안합니다: (1) 랜덤 가우시안 드롭아웃, (2) 불투명도에 곱셈적 노이즈 주입. 이 전략들은 다양한 방법과 벤치마크에서 효과가 입증되었습니다. 이러한 통찰이 희소 뷰 3DGS에 대한 이해를 높이는 데 기여하길 바랍니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)는 밀집된 뷰 설정에서 새로운 뷰 합성에 뛰어난 성능을 보이지만, 희소한 뷰에서는 새로운 뷰에서 외관 아티팩트가 발생할 수 있다.
- 2. 희소한 뷰에서의 3DGS 외관 아티팩트 문제는 최적화된 가우시안들이 훈련 뷰에 과도하게 맞춰져 실제 장면의 외관 분포를 간과하는 데서 기인한다.
- 3. 제안된 Co-Adaptation Score(CA) 지표를 통해 가우시안 간의 얽힘 정도를 정량화하여 분석한 결과, 훈련 뷰의 수가 증가하면 얽힘 정도가 자연스럽게 완화된다.
- 4. 희소한 뷰의 3DGS에서 얽힘 문제를 완화하기 위해 두 가지 경량 전략인 랜덤 가우시안 드롭아웃과 불투명도에 대한 곱셈적 노이즈 주입을 제안한다.
- 5. 제안된 전략들은 다양한 방법과 벤치마크에서 효과가 검증되었으며, 희소한 뷰 3DGS에 대한 더 포괄적인 이해를 도모하는 데 기여할 것으로 기대된다.


---

*Generated on 2025-09-24 05:29:28*