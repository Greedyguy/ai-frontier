---
keywords:
  - 3D Gaussian Splatting
  - Confidence-Weighted Fusion
  - RGB-only Reconstruction
  - DROID-SLAM
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16863
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:36:36.496826",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Confidence-Weighted Fusion",
    "RGB-only Reconstruction",
    "DROID-SLAM"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Confidence-Weighted Fusion": 0.77,
    "RGB-only Reconstruction": 0.72,
    "DROID-SLAM": 0.75
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
        "rationale": "This is a novel technique central to the paper's contributions and not widely referenced elsewhere.",
        "novelty_score": 0.85,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Confidence-Weighted Fusion",
        "canonical": "Confidence-Weighted Fusion",
        "aliases": [
          "Confidence Fusion"
        ],
        "category": "unique_technical",
        "rationale": "This mechanism is a core innovation in the paper, enhancing depth estimation accuracy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "RGB-only Reconstruction",
        "canonical": "RGB-only Reconstruction",
        "aliases": [
          "RGB Reconstruction"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area for the proposed method, linking to broader computer vision tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "DROID-SLAM",
        "canonical": "DROID-SLAM",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a specific SLAM framework referenced in the paper, useful for linking to related SLAM research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "SLAM",
      "depth estimation",
      "reconstruction accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Confidence-Weighted Fusion",
      "resolved_canonical": "Confidence-Weighted Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "RGB-only Reconstruction",
      "resolved_canonical": "RGB-only Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "DROID-SLAM",
      "resolved_canonical": "DROID-SLAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16863.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16863](https://arxiv.org/abs/2509.16863)

## 🔗 유사한 논문
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (88.5% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.0% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (83.5% similar)
- [[2025-09-23/ST-GS_ Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting_20250923|ST-GS: Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting]] (82.9% similar)
- [[2025-09-22/FingerSplat_ Contactless Fingerprint 3D Reconstruction and Generation based on 3D Gaussian Splatting_20250922|FingerSplat: Contactless Fingerprint 3D Reconstruction and Generation based on 3D Gaussian Splatting]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/RGB-only Reconstruction|RGB-only Reconstruction]], [[keywords/DROID-SLAM|DROID-SLAM]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Confidence-Weighted Fusion|Confidence-Weighted Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16863v1 Announce Type: new 
Abstract: We introduce ConfidentSplat, a novel 3D Gaussian Splatting (3DGS)-based SLAM system for robust, highfidelity RGB-only reconstruction. Addressing geometric inaccuracies in existing RGB-only 3DGS SLAM methods that stem from unreliable depth estimation, ConfidentSplat incorporates a core innovation: a confidence-weighted fusion mechanism. This mechanism adaptively integrates depth cues from multiview geometry with learned monocular priors (Omnidata ViT), dynamically weighting their contributions based on explicit reliability estimates-derived predominantly from multi-view geometric consistency-to generate high-fidelity proxy depth for map supervision. The resulting proxy depth guides the optimization of a deformable 3DGS map, which efficiently adapts online to maintain global consistency following pose updates from a DROID-SLAM-inspired frontend and backend optimizations (loop closure, global bundle adjustment). Extensive validation on standard benchmarks (TUM-RGBD, ScanNet) and diverse custom mobile datasets demonstrates significant improvements in reconstruction accuracy (L1 depth error) and novel view synthesis fidelity (PSNR, SSIM, LPIPS) over baselines, particularly in challenging conditions. ConfidentSplat underscores the efficacy of principled, confidence-aware sensor fusion for advancing state-of-the-art dense visual SLAM.

## 📝 요약

ConfidentSplat은 3D Gaussian Splatting 기반의 새로운 SLAM 시스템으로, RGB 데이터만을 사용하여 높은 정확도의 3D 재구성을 제공합니다. 기존의 RGB 기반 3DGS SLAM 방법에서 발생하는 깊이 추정의 불확실성을 해결하기 위해, ConfidentSplat은 신뢰도 가중치 융합 메커니즘을 도입했습니다. 이 메커니즘은 다중 뷰 기하학과 학습된 단안 사전 정보(Omnidata ViT)를 신뢰도에 따라 가중치를 부여하여 통합함으로써, 높은 정확도의 깊이 정보를 생성합니다. 이 깊이 정보는 변형 가능한 3DGS 맵의 최적화를 지도하며, DROID-SLAM에서 영감을 받은 프론트엔드 및 백엔드 최적화(루프 클로저, 글로벌 번들 조정)를 통해 전역 일관성을 유지합니다. TUM-RGBD, ScanNet 등의 표준 벤치마크와 다양한 모바일 데이터셋에서 검증한 결과, ConfidentSplat은 재구성 정확도와 새로운 뷰 생성의 품질에서 상당한 향상을 보여주었습니다. 이 연구는 신뢰도 기반 센서 융합의 효과를 입증하며, 고밀도 비주얼 SLAM의 발전에 기여합니다.

## 🎯 주요 포인트

- 1. ConfidentSplat은 3D Gaussian Splatting 기반의 새로운 SLAM 시스템으로, 신뢰도 가중치 융합 메커니즘을 도입하여 RGB 전용 3D 재구성을 개선합니다.
- 2. 이 시스템은 다중 뷰 기하학과 학습된 단안 사전 정보의 깊이 단서를 신뢰도에 따라 가중치를 부여하여 융합함으로써 높은 충실도의 프록시 깊이를 생성합니다.
- 3. 생성된 프록시 깊이는 변형 가능한 3DGS 맵의 최적화를 안내하며, 이는 DROID-SLAM에서 영감을 받은 프론트엔드 및 백엔드 최적화와 함께 글로벌 일관성을 유지합니다.
- 4. TUM-RGBD, ScanNet 등 표준 벤치마크와 다양한 모바일 데이터셋에서의 검증을 통해 기존 방법들보다 재구성 정확도와 새로운 뷰 합성 충실도가 크게 향상됨을 보여줍니다.
- 5. ConfidentSplat은 신뢰도 기반의 센서 융합이 밀집형 비주얼 SLAM의 최첨단 기술 발전에 효과적임을 입증합니다.


---

*Generated on 2025-09-24 04:36:36*