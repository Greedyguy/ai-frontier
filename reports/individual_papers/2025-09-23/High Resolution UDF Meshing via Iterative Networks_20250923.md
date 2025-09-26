---
keywords:
  - Unsigned Distance Fields
  - Neural Network
  - Surface Recovery
  - High Resolution Meshing
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17212
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:11:39.903304",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Unsigned Distance Fields",
    "Neural Network",
    "Surface Recovery",
    "High Resolution Meshing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Unsigned Distance Fields": 0.78,
    "Neural Network": 0.8,
    "Surface Recovery": 0.77,
    "High Resolution Meshing": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Unsigned Distance Fields",
        "canonical": "Unsigned Distance Fields",
        "aliases": [
          "UDF",
          "Distance Fields"
        ],
        "category": "unique_technical",
        "rationale": "Key concept in the paper, essential for understanding the specific technical challenge addressed.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Iterative Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "Iterative Networks"
        ],
        "category": "broad_technical",
        "rationale": "Central to the method proposed, linking to broader neural network concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Surface Recovery",
        "canonical": "Surface Recovery",
        "aliases": [
          "Mesh Recovery",
          "Surface Extraction"
        ],
        "category": "specific_connectable",
        "rationale": "Describes the primary goal of the method, connecting to related surface processing techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "High Resolution Meshing",
        "canonical": "High Resolution Meshing",
        "aliases": [
          "High-Res Meshing",
          "Detailed Meshing"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on the resolution aspect, crucial for linking to high-detail modeling techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
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
      "candidate_surface": "Unsigned Distance Fields",
      "resolved_canonical": "Unsigned Distance Fields",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Iterative Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Surface Recovery",
      "resolved_canonical": "Surface Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "High Resolution Meshing",
      "resolved_canonical": "High Resolution Meshing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# High Resolution UDF Meshing via Iterative Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17212.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17212](https://arxiv.org/abs/2509.17212)

## 🔗 유사한 논문
- [[2025-09-22/Graph-based Point Cloud Surface Reconstruction using B-Splines_20250922|Graph-based Point Cloud Surface Reconstruction using B-Splines]] (81.9% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (81.9% similar)
- [[2025-09-23/Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling_20250923|Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling]] (81.6% similar)
- [[2025-09-23/GeoSVR_ Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction_20250923|GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction]] (81.4% similar)
- [[2025-09-23/DT-NeRF_ A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction_20250923|DT-NeRF: A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Surface Recovery|Surface Recovery]]
**⚡ Unique Technical**: [[keywords/Unsigned Distance Fields|Unsigned Distance Fields]], [[keywords/High Resolution Meshing|High Resolution Meshing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17212v1 Announce Type: cross 
Abstract: Unsigned Distance Fields (UDFs) are a natural implicit representation for open surfaces but, unlike Signed Distance Fields (SDFs), are challenging to triangulate into explicit meshes. This is especially true at high resolutions where neural UDFs exhibit higher noise levels, which makes it hard to capture fine details. Most current techniques perform within single voxels without reference to their neighborhood, resulting in missing surface and holes where the UDF is ambiguous or noisy. We show that this can be remedied by performing several passes and by reasoning on previously extracted surface elements to incorporate neighborhood information. Our key contribution is an iterative neural network that does this and progressively improves surface recovery within each voxel by spatially propagating information from increasingly distant neighbors. Unlike single-pass methods, our approach integrates newly detected surfaces, distance values, and gradients across multiple iterations, effectively correcting errors and stabilizing extraction in challenging regions. Experiments on diverse 3D models demonstrate that our method produces significantly more accurate and complete meshes than existing approaches, particularly for complex geometries, enabling UDF surface extraction at higher resolutions where traditional methods fail.

## 📝 요약

이 논문은 열린 표면을 암시적으로 표현하는 비부호 거리장(UDF)의 삼각화 문제를 해결하기 위한 새로운 방법을 제안합니다. 기존 방법들은 개별 복셀 내에서만 작동하여 표면이 누락되거나 구멍이 발생하는 문제를 겪습니다. 본 연구의 주요 기여는 인접 정보를 활용하여 복셀 내 표면 복구를 점진적으로 개선하는 반복적 신경망을 개발한 것입니다. 이 방법은 여러 번의 반복을 통해 새롭게 감지된 표면, 거리 값, 기울기를 통합하여 오류를 수정하고 복잡한 영역에서의 추출을 안정화합니다. 다양한 3D 모델 실험 결과, 제안된 방법은 특히 복잡한 기하학적 구조에서 기존 방법보다 더 정확하고 완전한 메쉬를 생성하며, 높은 해상도에서도 효과적으로 작동함을 보여줍니다.

## 🎯 주요 포인트

- 1. UDFs는 열린 표면을 표현하는 자연스러운 암시적 표현이지만, SDFs와 달리 명시적 메쉬로 삼각화하기 어렵습니다.
- 2. 고해상도에서 신경망 기반 UDF는 높은 노이즈 수준을 보여 세부 사항을 포착하기 어렵습니다.
- 3. 기존 기법은 단일 복셀 내에서만 작동하여 UDF가 모호하거나 노이즈가 있는 경우 표면이 누락되거나 구멍이 발생합니다.
- 4. 제안된 방법은 여러 번의 패스를 통해 이웃 정보를 통합하여 표면 복구를 점진적으로 개선합니다.
- 5. 실험 결과, 제안된 방법은 기존 접근 방식보다 복잡한 기하학적 구조에서도 더 정확하고 완전한 메쉬를 생성합니다.


---

*Generated on 2025-09-24 05:11:39*