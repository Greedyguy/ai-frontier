---
keywords:
  - Sparse Voxel Representation
  - Voxel-Uncertainty Depth Constraint
  - Sparse Voxel Surface Regularization
  - Surface Reconstruction
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.18090
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:08:25.676299",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Voxel Representation",
    "Voxel-Uncertainty Depth Constraint",
    "Sparse Voxel Surface Regularization",
    "Surface Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Voxel Representation": 0.78,
    "Voxel-Uncertainty Depth Constraint": 0.77,
    "Sparse Voxel Surface Regularization": 0.79,
    "Surface Reconstruction": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Voxels",
        "canonical": "Sparse Voxel Representation",
        "aliases": [
          "Sparse Voxel",
          "Voxel-based Framework"
        ],
        "category": "unique_technical",
        "rationale": "Sparse voxels are central to the paper's approach and offer a unique perspective on surface reconstruction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Voxel-Uncertainty Depth Constraint",
        "canonical": "Voxel-Uncertainty Depth Constraint",
        "aliases": [
          "Depth Constraint",
          "Voxel Depth"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel method for improving scene convergence in voxel-based reconstruction.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Sparse Voxel Surface Regularization",
        "canonical": "Sparse Voxel Surface Regularization",
        "aliases": [
          "Voxel Surface Regularization"
        ],
        "category": "unique_technical",
        "rationale": "This technique is crucial for enhancing geometric consistency and is a key innovation of the paper.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.86,
        "link_intent_score": 0.79
      },
      {
        "surface": "Surface Reconstruction",
        "canonical": "Surface Reconstruction",
        "aliases": [
          "Reconstruction"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in computer vision that connects to various reconstruction techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Gaussian Splatting",
      "Radiance Fields"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Voxels",
      "resolved_canonical": "Sparse Voxel Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Voxel-Uncertainty Depth Constraint",
      "resolved_canonical": "Voxel-Uncertainty Depth Constraint",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Sparse Voxel Surface Regularization",
      "resolved_canonical": "Sparse Voxel Surface Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.86,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Surface Reconstruction",
      "resolved_canonical": "Surface Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18090.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.18090](https://arxiv.org/abs/2509.18090)

## 🔗 유사한 논문
- [[2025-09-23/From Restoration to Reconstruction_ Rethinking 3D Gaussian Splatting for Underwater Scenes_20250923|From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes]] (82.5% similar)
- [[2025-09-23/HyRF_ Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis_20250923|HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis]] (82.1% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (81.9% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (81.8% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Surface Reconstruction|Surface Reconstruction]]
**⚡ Unique Technical**: [[keywords/Sparse Voxel Representation|Sparse Voxel Representation]], [[keywords/Voxel-Uncertainty Depth Constraint|Voxel-Uncertainty Depth Constraint]], [[keywords/Sparse Voxel Surface Regularization|Sparse Voxel Surface Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18090v1 Announce Type: new 
Abstract: Reconstructing accurate surfaces with radiance fields has achieved remarkable progress in recent years. However, prevailing approaches, primarily based on Gaussian Splatting, are increasingly constrained by representational bottlenecks. In this paper, we introduce GeoSVR, an explicit voxel-based framework that explores and extends the under-investigated potential of sparse voxels for achieving accurate, detailed, and complete surface reconstruction. As strengths, sparse voxels support preserving the coverage completeness and geometric clarity, while corresponding challenges also arise from absent scene constraints and locality in surface refinement. To ensure correct scene convergence, we first propose a Voxel-Uncertainty Depth Constraint that maximizes the effect of monocular depth cues while presenting a voxel-oriented uncertainty to avoid quality degradation, enabling effective and robust scene constraints yet preserving highly accurate geometries. Subsequently, Sparse Voxel Surface Regularization is designed to enhance geometric consistency for tiny voxels and facilitate the voxel-based formation of sharp and accurate surfaces. Extensive experiments demonstrate our superior performance compared to existing methods across diverse challenging scenarios, excelling in geometric accuracy, detail preservation, and reconstruction completeness while maintaining high efficiency. Code is available at https://github.com/Fictionarry/GeoSVR.

## 📝 요약

GeoSVR는 희소한 복셀을 활용하여 정확하고 세밀한 표면 재구성을 가능하게 하는 명시적 복셀 기반 프레임워크입니다. 기존의 가우시안 스플래팅 기반 접근법이 표현의 한계에 부딪히는 문제를 해결하고자, 단안 깊이 단서를 최대한 활용하는 복셀 불확실성 깊이 제약을 제안하여 장면 제약을 강화하고 정확한 기하학적 구조를 유지합니다. 또한, 작은 복셀의 기하학적 일관성을 높이고 날카롭고 정확한 표면 형성을 돕는 희소 복셀 표면 정규화를 도입했습니다. 다양한 실험을 통해 GeoSVR이 기하학적 정확성, 세부 보존, 재구성 완전성에서 기존 방법보다 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. GeoSVR은 희소한 복셀을 활용하여 정확하고 상세하며 완전한 표면 재구성을 달성하는 명시적 복셀 기반 프레임워크를 제안합니다.
- 2. 복셀 불확실성 깊이 제약을 통해 단안 깊이 단서를 최대화하고, 복셀 지향 불확실성을 도입하여 장면 제약을 강화하면서도 높은 정확도의 기하학적 구조를 유지합니다.
- 3. 희소 복셀 표면 정규화를 통해 작은 복셀의 기하학적 일관성을 향상시키고, 날카롭고 정확한 표면 형성을 촉진합니다.
- 4. 다양한 도전적인 시나리오에서 기존 방법들보다 뛰어난 성능을 보이며, 기하학적 정확성, 세부 보존, 재구성 완전성에서 우수한 결과를 제공합니다.
- 5. GeoSVR의 코드는 https://github.com/Fictionarry/GeoSVR에서 제공됩니다.


---

*Generated on 2025-09-24 05:08:25*