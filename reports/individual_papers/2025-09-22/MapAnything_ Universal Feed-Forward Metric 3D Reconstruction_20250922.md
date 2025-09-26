---
keywords:
  - Transformer
  - 3D Scene Geometry
  - Camera Localization
  - Depth Estimation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.13414
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:14:30.252716",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "3D Scene Geometry",
    "Camera Localization",
    "Depth Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "3D Scene Geometry": 0.78,
    "Camera Localization": 0.82,
    "Depth Estimation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based feed-forward model",
        "canonical": "Transformer",
        "aliases": [
          "Transformer model"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology in modern machine learning, connecting to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Metric 3D scene geometry",
        "canonical": "3D Scene Geometry",
        "aliases": [
          "3D geometry",
          "Scene geometry"
        ],
        "category": "unique_technical",
        "rationale": "This term captures the unique focus on metric 3D reconstruction, linking to specialized 3D vision research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Camera localization",
        "canonical": "Camera Localization",
        "aliases": [
          "Camera positioning"
        ],
        "category": "specific_connectable",
        "rationale": "Camera localization is a critical task in computer vision, connecting to research on spatial awareness and navigation.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Monocular depth estimation",
        "canonical": "Depth Estimation",
        "aliases": [
          "Monocular depth"
        ],
        "category": "specific_connectable",
        "rationale": "Depth estimation is a key component of 3D reconstruction, linking to various vision tasks and datasets.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "feed-forward",
      "model",
      "training"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based feed-forward model",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Metric 3D scene geometry",
      "resolved_canonical": "3D Scene Geometry",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Camera localization",
      "resolved_canonical": "Camera Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Monocular depth estimation",
      "resolved_canonical": "Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MapAnything: Universal Feed-Forward Metric 3D Reconstruction

**Korean Title:** MapAnything: 범용 피드포워드 메트릭 3D 재구성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13414.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.13414](https://arxiv.org/abs/2509.13414)

## 🔗 유사한 논문
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.3% similar)
- [[2025-09-18/Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (81.3% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.9% similar)
- [[2025-09-19/Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration_20250919|Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration]] (80.4% similar)
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Camera Localization|Camera Localization]], [[keywords/Depth Estimation|Depth Estimation]]
**⚡ Unique Technical**: [[keywords/3D Scene Geometry|3D Scene Geometry]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13414v2 Announce Type: replace-cross 
Abstract: We introduce MapAnything, a unified transformer-based feed-forward model that ingests one or more images along with optional geometric inputs such as camera intrinsics, poses, depth, or partial reconstructions, and then directly regresses the metric 3D scene geometry and cameras. MapAnything leverages a factored representation of multi-view scene geometry, i.e., a collection of depth maps, local ray maps, camera poses, and a metric scale factor that effectively upgrades local reconstructions into a globally consistent metric frame. Standardizing the supervision and training across diverse datasets, along with flexible input augmentation, enables MapAnything to address a broad range of 3D vision tasks in a single feed-forward pass, including uncalibrated structure-from-motion, calibrated multi-view stereo, monocular depth estimation, camera localization, depth completion, and more. We provide extensive experimental analyses and model ablations demonstrating that MapAnything outperforms or matches specialist feed-forward models while offering more efficient joint training behavior, thus paving the way toward a universal 3D reconstruction backbone.

## 🔍 Abstract (한글 번역)

arXiv:2509.13414v2 발표 유형: 교차 교체  
초록: 우리는 MapAnything을 소개합니다. 이는 하나 이상의 이미지를 카메라 내재 매개변수, 자세, 깊이 또는 부분 재구성과 같은 선택적 기하학적 입력과 함께 수용한 후, 메트릭 3D 장면 기하학과 카메라를 직접 회귀하는 통합된 트랜스포머 기반 피드포워드 모델입니다. MapAnything은 다중 시점 장면 기하학의 분해된 표현, 즉 깊이 맵, 국소 광선 맵, 카메라 자세, 그리고 국소 재구성을 전역적으로 일관된 메트릭 프레임으로 효과적으로 업그레이드하는 메트릭 스케일 팩터의 집합을 활용합니다. 다양한 데이터셋에 걸쳐 감독과 훈련을 표준화하고 유연한 입력 증강을 통해 MapAnything은 비보정 구조-이동, 보정된 다중 시점 스테레오, 단안 깊이 추정, 카메라 위치 추정, 깊이 완성 등 단일 피드포워드 패스로 광범위한 3D 비전 작업을 처리할 수 있습니다. 우리는 MapAnything이 전문 피드포워드 모델을 능가하거나 일치하면서도 더 효율적인 공동 훈련 행동을 제공함을 보여주는 광범위한 실험 분석과 모델 소거를 제공합니다. 이는 보편적인 3D 재구성 백본으로 나아가는 길을 열어줍니다.

## 📝 요약

MapAnything는 하나 이상의 이미지와 카메라 내부 매개변수, 자세, 깊이, 부분 재구성 등의 기하학적 입력을 받아 3D 장면 기하학과 카메라를 직접 예측하는 통합된 트랜스포머 기반 모델입니다. 이 모델은 다중 뷰 장면 기하학의 요소별 표현을 활용하여, 지역적 재구성을 전역적으로 일관된 메트릭 프레임으로 업그레이드합니다. 다양한 데이터셋에 걸쳐 표준화된 감독과 훈련, 유연한 입력 보강을 통해 MapAnything은 비보정 구조-이동, 보정된 다중 뷰 스테레오, 단안 깊이 추정, 카메라 위치 추정, 깊이 보완 등 다양한 3D 비전 작업을 단일 피드포워드 패스로 처리할 수 있습니다. 실험 분석과 모델 제거 실험을 통해 MapAnything이 전문 피드포워드 모델과 동등하거나 우수한 성능을 보이며, 효율적인 공동 훈련을 가능하게 함을 입증했습니다. 이는 범용 3D 재구성 백본으로의 발전을 위한 길을 열어줍니다.

## 🎯 주요 포인트

- 1. MapAnything는 하나 이상의 이미지와 카메라 내재 매개변수, 포즈, 깊이, 부분 재구성 등의 기하학적 입력을 처리하여 3D 장면 기하학과 카메라를 직접 회귀하는 통합된 트랜스포머 기반 모델입니다.
- 2. 이 모델은 다중 뷰 장면 기하학의 요소화된 표현을 활용하여 지역적 재구성을 전역적으로 일관된 메트릭 프레임으로 업그레이드합니다.
- 3. 다양한 데이터셋에 대한 표준화된 감독과 훈련, 유연한 입력 증강을 통해 MapAnything은 단일 피드포워드 패스로 다양한 3D 비전 작업을 처리할 수 있습니다.
- 4. 실험 분석과 모델 소거를 통해 MapAnything이 전문 피드포워드 모델을 능가하거나 동등한 성능을 보이면서도 더 효율적인 공동 훈련을 제공함을 입증했습니다.
- 5. MapAnything은 범용 3D 재구성 백본으로의 발전 가능성을 제시합니다.


---

*Generated on 2025-09-23 10:14:30*