---
keywords:
  - 3D Cell Segmentation
  - Geo-Wasserstein Divergence
  - Transfer Learning
  - Pre-trained Classifier
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.01890
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:00:33.174219",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Cell Segmentation",
    "Geo-Wasserstein Divergence",
    "Transfer Learning",
    "Pre-trained Classifier"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Cell Segmentation": 0.78,
    "Geo-Wasserstein Divergence": 0.82,
    "Transfer Learning": 0.75,
    "Pre-trained Classifier": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D cell segmentation",
        "canonical": "3D Cell Segmentation",
        "aliases": [
          "three-dimensional cell segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's focus on correcting oversegmentation errors.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Geo-Wasserstein divergence",
        "canonical": "Geo-Wasserstein Divergence",
        "aliases": [
          "geometric Wasserstein divergence"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric for quantifying changes in 2D geometries, pivotal to the paper's methodology.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "transfer learning",
        "canonical": "Transfer Learning",
        "aliases": [
          "knowledge transfer"
        ],
        "category": "broad_technical",
        "rationale": "This is a widely recognized concept that connects the paper's application to out-of-domain datasets.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "pre-trained classifier",
        "canonical": "Pre-trained Classifier",
        "aliases": [
          "pretrained model"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of pre-trained models, a common technique in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D cell segmentation",
      "resolved_canonical": "3D Cell Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Geo-Wasserstein divergence",
      "resolved_canonical": "Geo-Wasserstein Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "transfer learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "pre-trained classifier",
      "resolved_canonical": "Pre-trained Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# 3D Cell Oversegmentation Correction via Geo-Wasserstein Divergence

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01890.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.01890](https://arxiv.org/abs/2502.01890)

## 🔗 유사한 논문
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut: Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (80.9% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (80.6% similar)
- [[2025-09-23/Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge_20250923|Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge]] (80.6% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (80.5% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**🔗 Specific Connectable**: [[keywords/Pre-trained Classifier|Pre-trained Classifier]]
**⚡ Unique Technical**: [[keywords/3D Cell Segmentation|3D Cell Segmentation]], [[keywords/Geo-Wasserstein Divergence|Geo-Wasserstein Divergence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01890v3 Announce Type: replace-cross 
Abstract: 3D cell segmentation methods are often hindered by \emph{oversegmentation}, where a single cell is incorrectly split into multiple fragments. This degrades the final segmentation quality and is notoriously difficult to resolve, as oversegmentation errors often resemble natural gaps between adjacent cells. Our work makes two key contributions. First, for 3D cell segmentation, we are the first work to formulate oversegmentation as a concrete problem and propose a geometric framework to identify and correct these errors. Our approach builds a pre-trained classifier using both 2D geometric and 3D topological features extracted from flawed 3D segmentation results. Second, we introduce a novel metric, Geo-Wasserstein divergence, to quantify changes in 2D geometries. This captures the evolving trends of cell mask shape in a geometry-aware manner. We validate our method through extensive experiments on in-domain plant datasets, including both synthesized and real oversegmented cases, as well as on out-of-domain animal datasets to demonstrate transfer learning performance. An ablation study further highlights the contribution of the Geo-Wasserstein divergence. A clear pipeline is provided for end-users to build pre-trained models to any labeled dataset.

## 📝 요약

이 논문은 3D 세포 분할에서 발생하는 과분할 문제를 해결하기 위한 새로운 접근법을 제안합니다. 첫 번째 기여는 과분할을 구체적인 문제로 정의하고, 이를 식별하고 수정하기 위한 기하학적 프레임워크를 제시한 것입니다. 이 방법은 결함이 있는 3D 분할 결과에서 2D 기하학적 및 3D 위상적 특징을 추출하여 사전 학습된 분류기를 구축합니다. 두 번째로, 2D 기하학의 변화를 정량화하기 위해 Geo-Wasserstein 발산이라는 새로운 지표를 도입하여 세포 마스크 형태의 변화를 기하학적으로 포착합니다. 이 방법은 식물 데이터셋과 동물 데이터셋에서의 실험을 통해 검증되었으며, 전이 학습 성능도 입증되었습니다. Geo-Wasserstein 발산의 기여도는 절제 연구를 통해 강조됩니다. 최종 사용자가 사전 학습 모델을 구축할 수 있는 명확한 절차도 제공됩니다.

## 🎯 주요 포인트

- 1. 3D 세포 분할에서 과분할 문제를 구체적으로 정의하고 이를 해결하기 위한 기하학적 프레임워크를 제안했습니다.
- 2. 과분할 오류를 식별하고 수정하기 위해 2D 기하학적 및 3D 위상적 특징을 활용한 사전 학습된 분류기를 구축했습니다.
- 3. 2D 기하학의 변화를 정량화하기 위한 새로운 지표인 Geo-Wasserstein divergence를 도입했습니다.
- 4. 제안된 방법은 식물 데이터셋과 동물 데이터셋을 포함한 다양한 실험을 통해 검증되었습니다.
- 5. 최종 사용자가 어떤 레이블이 있는 데이터셋에도 사전 학습된 모델을 구축할 수 있는 명확한 파이프라인을 제공합니다.


---

*Generated on 2025-09-24 03:00:33*