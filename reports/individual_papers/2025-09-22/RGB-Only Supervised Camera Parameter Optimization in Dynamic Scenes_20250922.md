---
keywords:
  - Camera Parameter Optimization
  - Dynamic Scenes
  - RGB-Only Supervision
  - 4D Reconstruction
  - Patch-wise Tracking Filters
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15123
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:41:16.895967",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Camera Parameter Optimization",
    "Dynamic Scenes",
    "RGB-Only Supervision",
    "4D Reconstruction",
    "Patch-wise Tracking Filters"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Camera Parameter Optimization": 0.75,
    "Dynamic Scenes": 0.7,
    "RGB-Only Supervision": 0.72,
    "4D Reconstruction": 0.78,
    "Patch-wise Tracking Filters": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Camera Parameter Optimization",
        "canonical": "Camera Parameter Optimization",
        "aliases": [
          "Camera Optimization",
          "Camera Parameters"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, linking to advancements in camera technology and optimization techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Dynamic Scenes",
        "canonical": "Dynamic Scenes",
        "aliases": [
          "Moving Scenes",
          "Non-static Scenes"
        ],
        "category": "specific_connectable",
        "rationale": "Essential context for understanding the challenges in camera optimization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      },
      {
        "surface": "RGB-Only Supervision",
        "canonical": "RGB-Only Supervision",
        "aliases": [
          "RGB Supervision",
          "Single RGB Video"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the novel approach of using only RGB data for supervision, relevant for linking to methods using minimal data.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "4D Reconstruction",
        "canonical": "4D Reconstruction",
        "aliases": [
          "Four-Dimensional Reconstruction"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to broader topics in reconstruction and modeling, enhancing the understanding of application outcomes.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Patch-wise Tracking Filters",
        "canonical": "Patch-wise Tracking Filters",
        "aliases": [
          "Tracking Filters",
          "Patch Tracking"
        ],
        "category": "unique_technical",
        "rationale": "A novel component of the proposed method, relevant for linking to tracking and filtering techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.68
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
      "candidate_surface": "Camera Parameter Optimization",
      "resolved_canonical": "Camera Parameter Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Dynamic Scenes",
      "resolved_canonical": "Dynamic Scenes",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "RGB-Only Supervision",
      "resolved_canonical": "RGB-Only Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "4D Reconstruction",
      "resolved_canonical": "4D Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Patch-wise Tracking Filters",
      "resolved_canonical": "Patch-wise Tracking Filters",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes

**Korean Title:** 동적 장면에서 RGB 전용 감독 하의 카메라 매개변수 최적화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15123.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15123](https://arxiv.org/abs/2509.15123)

## 🔗 유사한 논문
- [[2025-09-19/Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration_20250919|Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration]] (84.9% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (83.0% similar)
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (82.5% similar)
- [[2025-09-18/Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (82.0% similar)
- [[2025-09-22/Camera Splatting for Continuous View Optimization_20250922|Camera Splatting for Continuous View Optimization]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Dynamic Scenes|Dynamic Scenes]], [[keywords/4D Reconstruction|4D Reconstruction]]
**⚡ Unique Technical**: [[keywords/Camera Parameter Optimization|Camera Parameter Optimization]], [[keywords/RGB-Only Supervision|RGB-Only Supervision]], [[keywords/Patch-wise Tracking Filters|Patch-wise Tracking Filters]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15123v2 Announce Type: replace 
Abstract: Although COLMAP has long remained the predominant method for camera parameter optimization in static scenes, it is constrained by its lengthy runtime and reliance on ground truth (GT) motion masks for application to dynamic scenes. Many efforts attempted to improve it by incorporating more priors as supervision such as GT focal length, motion masks, 3D point clouds, camera poses, and metric depth, which, however, are typically unavailable in casually captured RGB videos. In this paper, we propose a novel method for more accurate and efficient camera parameter optimization in dynamic scenes solely supervised by a single RGB video, dubbed ROS-Cam. Our method consists of three key components: (1) Patch-wise Tracking Filters, to establish robust and maximally sparse hinge-like relations across the RGB video. (2) Outlier-aware Joint Optimization, for efficient camera parameter optimization by adaptive down-weighting of moving outliers, without reliance on motion priors. (3) A Two-stage Optimization Strategy, to enhance stability and optimization speed by a trade-off between the Softplus limits and convex minima in losses. We visually and numerically evaluate our camera estimates. To further validate accuracy, we feed the camera estimates into a 4D reconstruction method and assess the resulting 3D scenes, and rendered 2D RGB and depth maps. We perform experiments on 4 real-world datasets (NeRF-DS, DAVIS, iPhone, and TUM-dynamics) and 1 synthetic dataset (MPI-Sintel), demonstrating that our method estimates camera parameters more efficiently and accurately with a single RGB video as the only supervision.

## 🔍 Abstract (한글 번역)

arXiv:2509.15123v2 발표 유형: 교체  
초록: COLMAP은 정적 장면에서 카메라 매개변수 최적화의 주요 방법으로 오랫동안 자리 잡아왔지만, 긴 실행 시간과 동적 장면에 적용하기 위한 실제 운동 마스크(GT)에 대한 의존성으로 인해 제한이 있습니다. 많은 연구들이 GT 초점 거리, 운동 마스크, 3D 포인트 클라우드, 카메라 자세 및 메트릭 깊이와 같은 추가적인 사전 정보를 감독으로 통합하여 이를 개선하려고 시도했지만, 이러한 정보는 일반적으로 일상적으로 촬영된 RGB 비디오에서는 사용할 수 없습니다. 본 논문에서는 단일 RGB 비디오만으로 감독되는 동적 장면에서 보다 정확하고 효율적인 카메라 매개변수 최적화를 위한 새로운 방법인 ROS-Cam을 제안합니다. 우리의 방법은 세 가지 주요 구성 요소로 이루어져 있습니다: (1) 패치 단위 추적 필터, RGB 비디오 전반에 걸쳐 견고하고 최대한 희소한 경첩과 같은 관계를 설정하기 위해. (2) 이상치 인식 공동 최적화, 운동 사전 정보에 의존하지 않고 이동하는 이상치의 가중치를 적응적으로 낮추어 효율적인 카메라 매개변수 최적화를 위해. (3) 손실의 소프트플러스 한계와 볼록 최소값 간의 균형을 통해 안정성과 최적화 속도를 향상시키기 위한 2단계 최적화 전략. 우리는 시각적 및 수치적으로 우리의 카메라 추정치를 평가합니다. 정확성을 추가로 검증하기 위해, 카메라 추정치를 4D 재구성 방법에 입력하고 결과로 얻어진 3D 장면 및 렌더링된 2D RGB 및 깊이 맵을 평가합니다. 우리는 4개의 실제 데이터셋(NeRF-DS, DAVIS, iPhone, TUM-dynamics)과 1개의 합성 데이터셋(MPI-Sintel)에서 실험을 수행하여, 우리의 방법이 단일 RGB 비디오만을 감독으로 사용하여 카메라 매개변수를 보다 효율적이고 정확하게 추정함을 입증합니다.

## 📝 요약

이 논문에서는 동적 장면에서 단일 RGB 비디오만으로 카메라 매개변수를 더 정확하고 효율적으로 최적화하는 새로운 방법인 ROS-Cam을 제안합니다. 주요 기여는 다음과 같습니다: (1) 패치 기반 추적 필터를 통해 RGB 비디오 전반에 걸쳐 강력하고 희소한 관계를 설정합니다. (2) 움직이는 이상치를 적응적으로 가중치를 낮추어 모션 프라이어 없이 효율적인 카메라 매개변수 최적화를 수행합니다. (3) Softplus 한계와 볼록 최소값 간의 균형을 통해 안정성과 최적화 속도를 향상시키는 두 단계 최적화 전략을 사용합니다. 이 방법은 4개의 실제 데이터셋과 1개의 합성 데이터셋에서 실험을 통해 단일 RGB 비디오만으로 카메라 매개변수를 더 효율적이고 정확하게 추정함을 입증했습니다.

## 🎯 주요 포인트

- 1. 기존의 COLMAP 방법은 정적 장면에서 카메라 매개변수 최적화에 주로 사용되지만, 동적 장면에서는 긴 실행 시간과 GT 모션 마스크 의존성 때문에 제약이 있다.
- 2. ROS-Cam은 단일 RGB 비디오만으로 동적 장면에서 더 정확하고 효율적인 카메라 매개변수 최적화를 가능하게 한다.
- 3. 제안된 방법은 패치 기반 추적 필터, 이상치 인식 공동 최적화, 그리고 2단계 최적화 전략의 세 가지 주요 구성 요소로 이루어져 있다.
- 4. 실험 결과, 제안된 방법은 단일 RGB 비디오를 유일한 감독으로 사용하여 카메라 매개변수를 더 효율적이고 정확하게 추정한다.
- 5. 4D 재구성 방법에 카메라 추정치를 입력하여 3D 장면과 렌더링된 2D RGB 및 깊이 맵을 평가함으로써 정확성을 추가로 검증하였다.


---

*Generated on 2025-09-23 12:41:16*