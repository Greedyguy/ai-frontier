<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:23:30.047009",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Surfels",
    "Differentiable Light Transport",
    "Radiosity",
    "Spherical Harmonics",
    "Global Illumination"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Surfels": 0.78,
    "Differentiable Light Transport": 0.82,
    "Radiosity": 0.8,
    "Spherical Harmonics": 0.79,
    "Global Illumination": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian surfels",
        "canonical": "Gaussian Surfels",
        "aliases": [
          "Gaussian splatting"
        ],
        "category": "unique_technical",
        "rationale": "Gaussian surfels are a novel approach in light transport and geometry reconstruction, offering a unique perspective in rendering techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Differentiable light transport",
        "canonical": "Differentiable Light Transport",
        "aliases": [
          "Differentiable rendering"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology, enabling efficient relighting and geometry reconstruction.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Radiosity theory",
        "canonical": "Radiosity",
        "aliases": [
          "Radiosity method"
        ],
        "category": "specific_connectable",
        "rationale": "Radiosity is a foundational concept in computer graphics, relevant for understanding light transport in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Spherical harmonics",
        "canonical": "Spherical Harmonics",
        "aliases": [
          "SH coefficients"
        ],
        "category": "specific_connectable",
        "rationale": "Spherical harmonics are crucial for representing light transport and view-dependent reflections in the framework.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Global illumination",
        "canonical": "Global Illumination",
        "aliases": [
          "GI"
        ],
        "category": "broad_technical",
        "rationale": "Global illumination is a key component in rendering, directly related to the paper's focus on efficient light transport.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "radiance fields",
      "view synthesis",
      "geometry reconstruction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian surfels",
      "resolved_canonical": "Gaussian Surfels",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Differentiable light transport",
      "resolved_canonical": "Differentiable Light Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Radiosity theory",
      "resolved_canonical": "Radiosity",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Spherical harmonics",
      "resolved_canonical": "Spherical Harmonics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Global illumination",
      "resolved_canonical": "Global Illumination",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18497.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18497](https://arxiv.org/abs/2509.18497)

## 🔗 유사한 논문
- [[2025-09-23/Wavelet-Space Representations for Neural Super-Resolution in Rendering Pipelines_20250923|Wavelet-Space Representations for Neural Super-Resolution in Rendering Pipelines]] (81.7% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (81.6% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (81.3% similar)
- [[2025-09-24/WaveletGaussian_ Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction_20250924|WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction]] (80.9% similar)
- [[2025-09-23/GeoSVR_ Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction_20250923|GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Global Illumination|Global Illumination]]
**🔗 Specific Connectable**: [[keywords/Radiosity|Radiosity]], [[keywords/Spherical Harmonics|Spherical Harmonics]]
**⚡ Unique Technical**: [[keywords/Gaussian Surfels|Gaussian Surfels]], [[keywords/Differentiable Light Transport|Differentiable Light Transport]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18497v1 Announce Type: cross 
Abstract: Radiance fields have gained tremendous success with applications ranging from novel view synthesis to geometry reconstruction, especially with the advent of Gaussian splatting. However, they sacrifice modeling of material reflective properties and lighting conditions, leading to significant geometric ambiguities and the inability to easily perform relighting. One way to address these limitations is to incorporate physically-based rendering, but it has been prohibitively expensive to include full global illumination within the inner loop of the optimization. Therefore, previous works adopt simplifications that make the whole optimization with global illumination effects efficient but less accurate. In this work, we adopt Gaussian surfels as the primitives and build an efficient framework for differentiable light transport, inspired from the classic radiosity theory. The whole framework operates in the coefficient space of spherical harmonics, enabling both diffuse and specular materials. We extend the classic radiosity into non-binary visibility and semi-opaque primitives, propose novel solvers to efficiently solve the light transport, and derive the backward pass for gradient optimizations, which is more efficient than auto-differentiation. During inference, we achieve view-independent rendering where light transport need not be recomputed under viewpoint changes, enabling hundreds of FPS for global illumination effects, including view-dependent reflections using a spherical harmonics representation. Through extensive qualitative and quantitative experiments, we demonstrate superior geometry reconstruction, view synthesis and relighting than previous inverse rendering baselines, or data-driven baselines given relatively sparse datasets with known or unknown lighting conditions.

## 📝 요약

이 논문은 가우시안 서펠을 활용한 효율적인 차별 가능한 광 전송 프레임워크를 제안하여 기존의 방사율 필드의 한계를 극복합니다. 기존 방법들이 전역 조명을 단순화하여 정확성을 희생한 반면, 이 연구는 구면 조화 공간에서 작동하여 확산 및 반사 재질을 모두 처리할 수 있습니다. 또한, 비이진 가시성과 반투명 프리미티브를 고려한 새로운 솔버를 제안하여 효율적인 광 전송을 구현합니다. 이로 인해, 관점 변화에 관계없이 광 전송을 재계산할 필요가 없어 수백 FPS의 전역 조명 효과를 실현할 수 있습니다. 실험 결과, 기존 방법들보다 우수한 기하학적 재구성, 뷰 합성 및 재조명을 달성했습니다.

## 🎯 주요 포인트

- 1. 방사장 필드는 가우시안 스플래팅의 발전으로 새로운 시점 합성 및 기하학 재구성에서 큰 성공을 거두었으나, 재질 반사 특성과 조명 조건 모델링을 희생하여 기하학적 모호성과 재조명의 어려움을 초래한다.
- 2. 물리 기반 렌더링을 통합하여 이러한 한계를 극복할 수 있으나, 전체 글로벌 조명을 최적화의 내부 루프에 포함하는 것은 비용이 많이 든다.
- 3. 본 연구에서는 가우시안 서펠을 기본 요소로 사용하여 구면 조화 함수의 계수 공간에서 작동하는 효율적인 차별화 가능한 광 전송 프레임워크를 구축하였다.
- 4. 제안된 프레임워크는 비이진 가시성과 반투명 기본 요소를 포함하도록 고전적인 라디오시티 이론을 확장하고, 효율적인 광 전송 해결을 위한 새로운 솔버를 제안한다.
- 5. 본 연구는 기존의 역 렌더링 및 데이터 기반 기준선보다 우수한 기하학적 재구성, 시점 합성 및 재조명을 입증하였다.


---

*Generated on 2025-09-24 16:23:30*