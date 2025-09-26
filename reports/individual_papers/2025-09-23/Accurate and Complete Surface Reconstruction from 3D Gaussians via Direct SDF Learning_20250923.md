---
keywords:
  - 3D Gaussian Splatting
  - Signed Distance Field
  - Geometry-guided Grid Growth
  - View Synthesis
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.07493
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:31:28.035247",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Signed Distance Field",
    "Geometry-guided Grid Growth",
    "View Synthesis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Signed Distance Field": 0.85,
    "Geometry-guided Grid Growth": 0.7,
    "View Synthesis": 0.65
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
        "rationale": "This is a novel approach in the field of 3D reconstruction, providing a unique perspective on photorealistic view synthesis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Signed Distance Field",
        "canonical": "Signed Distance Field",
        "aliases": [
          "SDF"
        ],
        "category": "specific_connectable",
        "rationale": "SDF is a crucial concept for understanding surface reconstruction techniques and is widely used in geometry processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Geometry-guided Grid Growth",
        "canonical": "Geometry-guided Grid Growth",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is specific to the paper and enhances the distribution of Gaussians, making it a unique contribution to the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "View Synthesis",
        "canonical": "View Synthesis",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "View synthesis is a broad technical concept that connects to various rendering and visualization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Signed Distance Field",
      "resolved_canonical": "Signed Distance Field",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Geometry-guided Grid Growth",
      "resolved_canonical": "Geometry-guided Grid Growth",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "View Synthesis",
      "resolved_canonical": "View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.07493.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.07493](https://arxiv.org/abs/2509.07493)

## 🔗 유사한 논문
- [[2025-09-23/MedGS_ Gaussian Splatting for Multi-Modal 3D Medical Imaging_20250923|MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging]] (86.3% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (86.1% similar)
- [[2025-09-23/GeoSplat_ A Deep Dive into Geometry-Constrained Gaussian Splatting_20250923|GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting]] (86.1% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (85.6% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/View Synthesis|View Synthesis]]
**🔗 Specific Connectable**: [[keywords/Signed Distance Field|Signed Distance Field]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Geometry-guided Grid Growth|Geometry-guided Grid Growth]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07493v2 Announce Type: replace 
Abstract: 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for photorealistic view synthesis, representing scenes with spatially distributed Gaussian primitives. While highly effective for rendering, achieving accurate and complete surface reconstruction remains challenging due to the unstructured nature of the representation and the absence of explicit geometric supervision. In this work, we propose DiGS, a unified framework that embeds Signed Distance Field (SDF) learning directly into the 3DGS pipeline, thereby enforcing strong and interpretable surface priors. By associating each Gaussian with a learnable SDF value, DiGS explicitly aligns primitives with underlying geometry and improves cross-view consistency. To further ensure dense and coherent coverage, we design a geometry-guided grid growth strategy that adaptively distributes Gaussians along geometry-consistent regions under a multi-scale hierarchy. Extensive experiments on standard benchmarks, including DTU, Mip-NeRF 360, and Tanks& Temples, demonstrate that DiGS consistently improves reconstruction accuracy and completeness while retaining high rendering fidelity.

## 📝 요약

3D Gaussian Splatting(3DGS)은 사실적인 뷰 합성을 위한 강력한 방법이지만, 표면 재구성에는 한계가 있습니다. 이를 해결하기 위해, 우리는 DiGS라는 프레임워크를 제안합니다. DiGS는 3DGS 파이프라인에 서명 거리 필드(SDF) 학습을 통합하여 강력한 표면 사전 정보를 제공합니다. 각 가우시안에 학습 가능한 SDF 값을 연결하여 기하학적 일관성을 개선하고, 기하학적 일관성이 있는 영역에 가우시안을 분배하는 그리드 성장 전략을 도입했습니다. 실험 결과, DiGS는 DTU, Mip-NeRF 360, Tanks & Temples 등의 벤치마크에서 재구성 정확도와 완전성을 향상시키면서도 높은 렌더링 품질을 유지했습니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)은 공간적으로 분포된 가우시안 프리미티브로 장면을 표현하여 사실적인 뷰 합성을 가능하게 합니다.
- 2. DiGS는 3DGS 파이프라인에 서명 거리 필드(SDF) 학습을 통합하여 강력하고 해석 가능한 표면 사전 정보를 제공합니다.
- 3. 각 가우시안에 학습 가능한 SDF 값을 연결함으로써, DiGS는 프리미티브를 기하학과 명시적으로 정렬하고 뷰 간 일관성을 향상시킵니다.
- 4. 기하학적 일관성을 유지하기 위해, DiGS는 다중 스케일 계층 구조 하에서 기하학적으로 일관된 영역에 가우시안을 적응적으로 분포시키는 그리드 성장 전략을 설계합니다.
- 5. DTU, Mip-NeRF 360, Tanks & Temples 등의 표준 벤치마크 실험에서 DiGS는 높은 렌더링 충실도를 유지하면서도 재구성 정확성과 완전성을 지속적으로 개선합니다.


---

*Generated on 2025-09-24 05:31:28*