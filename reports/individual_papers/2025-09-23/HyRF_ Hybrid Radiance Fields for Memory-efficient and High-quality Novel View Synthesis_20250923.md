---
keywords:
  - Hybrid Radiance Fields
  - 3D Gaussian Splatting
  - Neural Network
  - View-dependent Effects
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17083
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:44:43.194644",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hybrid Radiance Fields",
    "3D Gaussian Splatting",
    "Neural Network",
    "View-dependent Effects"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hybrid Radiance Fields": 0.8,
    "3D Gaussian Splatting": 0.75,
    "Neural Network": 0.7,
    "View-dependent Effects": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hybrid Radiance Fields",
        "canonical": "Hybrid Radiance Fields",
        "aliases": [
          "HyRF"
        ],
        "category": "unique_technical",
        "rationale": "This is a new scene representation method combining explicit Gaussians and neural fields, offering a unique approach to view synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "A specific method for novel view synthesis that is central to the paper's discussion and comparison.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Neural Fields",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Fields"
        ],
        "category": "broad_technical",
        "rationale": "Neural fields are a form of neural networks used in the paper, linking to broader neural network discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "View-dependent effects",
        "canonical": "View-dependent Effects",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key concept in rendering techniques, relevant for linking discussions on view synthesis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
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
      "candidate_surface": "Hybrid Radiance Fields",
      "resolved_canonical": "Hybrid Radiance Fields",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Neural Fields",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "View-dependent effects",
      "resolved_canonical": "View-dependent Effects",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17083.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17083](https://arxiv.org/abs/2509.17083)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (85.0% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (84.9% similar)
- [[2025-09-22/GS-Scale_ Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading_20250922|GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading]] (83.9% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (83.4% similar)
- [[2025-09-23/MedGS_ Gaussian Splatting for Multi-Modal 3D Medical Imaging_20250923|MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/View-dependent Effects|View-dependent Effects]]
**⚡ Unique Technical**: [[keywords/Hybrid Radiance Fields|Hybrid Radiance Fields]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17083v1 Announce Type: new 
Abstract: Recently, 3D Gaussian Splatting (3DGS) has emerged as a powerful alternative to NeRF-based approaches, enabling real-time, high-quality novel view synthesis through explicit, optimizable 3D Gaussians. However, 3DGS suffers from significant memory overhead due to its reliance on per-Gaussian parameters to model view-dependent effects and anisotropic shapes. While recent works propose compressing 3DGS with neural fields, these methods struggle to capture high-frequency spatial variations in Gaussian properties, leading to degraded reconstruction of fine details. We present Hybrid Radiance Fields (HyRF), a novel scene representation that combines the strengths of explicit Gaussians and neural fields. HyRF decomposes the scene into (1) a compact set of explicit Gaussians storing only critical high-frequency parameters and (2) grid-based neural fields that predict remaining properties. To enhance representational capacity, we introduce a decoupled neural field architecture, separately modeling geometry (scale, opacity, rotation) and view-dependent color. Additionally, we propose a hybrid rendering scheme that composites Gaussian splatting with a neural field-predicted background, addressing limitations in distant scene representation. Experiments demonstrate that HyRF achieves state-of-the-art rendering quality while reducing model size by over 20 times compared to 3DGS and maintaining real-time performance. Our project page is available at https://wzpscott.github.io/hyrf/.

## 📝 요약

최근 3D Gaussian Splatting(3DGS)은 NeRF 기반 접근법의 대안으로 주목받고 있지만, 메모리 사용량이 많다는 단점이 있습니다. 이를 해결하기 위해 제안된 Hybrid Radiance Fields(HyRF)는 명시적 Gaussian과 신경 필드를 결합한 새로운 장면 표현 방식입니다. HyRF는 장면을 고주파수 매개변수를 저장하는 명시적 Gaussian과 나머지 속성을 예측하는 그리드 기반 신경 필드로 분해합니다. 또한, 기하학과 색상을 분리하여 모델링하는 신경 필드 아키텍처를 도입하고, Gaussian splatting과 신경 필드 예측 배경을 합성하는 하이브리드 렌더링 방식을 제안합니다. 실험 결과, HyRF는 3DGS 대비 모델 크기를 20배 이상 줄이면서도 실시간 성능을 유지하며 최첨단 렌더링 품질을 달성했습니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)는 실시간 고품질의 새로운 시점 합성을 가능하게 하지만, 메모리 오버헤드 문제가 있다.
- 2. HyRF는 명시적 Gaussian과 신경 필드를 결합하여 장면을 표현하며, 고주파수 매개변수는 명시적 Gaussian에, 나머지 속성은 그리드 기반 신경 필드에 저장한다.
- 3. HyRF는 기하학(크기, 불투명도, 회전)과 시점 의존 색상을 별도로 모델링하는 분리된 신경 필드 아키텍처를 도입한다.
- 4. HyRF는 Gaussian splatting과 신경 필드 예측 배경을 혼합하는 하이브리드 렌더링 방식을 제안하여 먼 장면 표현의 한계를 극복한다.
- 5. HyRF는 3DGS 대비 모델 크기를 20배 이상 줄이면서도 실시간 성능을 유지하며 최첨단 렌더링 품질을 달성한다.


---

*Generated on 2025-09-24 04:44:43*