---
keywords:
  - Visual Difference Predictor
  - Camera-based Reconstruction Pipeline
  - Display Non-uniformity Evaluation
  - Defective Pixel Detection
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.08947
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:37:02.654871",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Visual Difference Predictor",
    "Camera-based Reconstruction Pipeline",
    "Display Non-uniformity Evaluation",
    "Defective Pixel Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Visual Difference Predictor": 0.78,
    "Camera-based Reconstruction Pipeline": 0.77,
    "Display Non-uniformity Evaluation": 0.74,
    "Defective Pixel Detection": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Visual Difference Predictor",
        "canonical": "Visual Difference Predictor",
        "aliases": [
          "VDP"
        ],
        "category": "unique_technical",
        "rationale": "This is a core component of the proposed system, crucial for linking perceptual assessment with display evaluation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Camera-based Reconstruction Pipeline",
        "canonical": "Camera-based Reconstruction Pipeline",
        "aliases": [
          "Camera Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This pipeline is central to the paper's methodology, enabling precise display measurements.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Display Non-uniformity Evaluation",
        "canonical": "Display Non-uniformity Evaluation",
        "aliases": [
          "Non-uniformity Assessment"
        ],
        "category": "specific_connectable",
        "rationale": "This evaluation is a key application of the framework, relevant for linking to display technology topics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      },
      {
        "surface": "Defective Pixel Detection",
        "canonical": "Defective Pixel Detection",
        "aliases": [
          "Pixel Defect Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This application demonstrates the practical utility of the framework, linking to quality control in display manufacturing.",
        "novelty_score": 0.66,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Visual Difference Predictor",
      "resolved_canonical": "Visual Difference Predictor",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Camera-based Reconstruction Pipeline",
      "resolved_canonical": "Camera-based Reconstruction Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Display Non-uniformity Evaluation",
      "resolved_canonical": "Display Non-uniformity Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Defective Pixel Detection",
      "resolved_canonical": "Defective Pixel Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# CameraVDP: Perceptual Display Assessment with Uncertainty Estimation via Camera and Visual Difference Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08947.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.08947](https://arxiv.org/abs/2509.08947)

## 🔗 유사한 논문
- [[2025-09-19/Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration_20250919|Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration]] (85.6% similar)
- [[2025-09-23/Subjective Camera 1.0_ Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion_20250923|Subjective Camera 1.0: Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion]] (83.2% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (82.9% similar)
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (82.5% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Display Non-uniformity Evaluation|Display Non-uniformity Evaluation]], [[keywords/Defective Pixel Detection|Defective Pixel Detection]]
**⚡ Unique Technical**: [[keywords/Visual Difference Predictor|Visual Difference Predictor]], [[keywords/Camera-based Reconstruction Pipeline|Camera-based Reconstruction Pipeline]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08947v2 Announce Type: replace-cross 
Abstract: Accurate measurement of images produced by electronic displays is critical for the evaluation of both traditional and computational displays. Traditional display measurement methods based on sparse radiometric sampling and fitting a model are inadequate for capturing spatially varying display artifacts, as they fail to capture high-frequency and pixel-level distortions. While cameras offer sufficient spatial resolution, they introduce optical, sampling, and photometric distortions. Furthermore, the physical measurement must be combined with a model of a visual system to assess whether the distortions are going to be visible. To enable perceptual assessment of displays, we propose a combination of a camera-based reconstruction pipeline with a visual difference predictor, which account for both the inaccuracy of camera measurements and visual difference prediction. The reconstruction pipeline combines HDR image stacking, MTF inversion, vignetting correction, geometric undistortion, homography transformation, and color correction, enabling cameras to function as precise display measurement instruments. By incorporating a Visual Difference Predictor (VDP), our system models the visibility of various stimuli under different viewing conditions for the human visual system. We validate the proposed CameraVDP framework through three applications: defective pixel detection, color fringing awareness, and display non-uniformity evaluation. Our uncertainty analysis framework enables the estimation of the theoretical upper bound for defect pixel detection performance and provides confidence intervals for VDP quality scores.

## 📝 요약

이 논문은 전자 디스플레이의 이미지를 정확하게 측정하기 위한 새로운 방법론을 제안합니다. 기존의 희소 방사 측정 방식은 공간적으로 변하는 디스플레이 결함을 포착하기에 부족하며, 카메라를 활용한 방법은 왜곡을 초래할 수 있습니다. 이를 해결하기 위해, 카메라 기반 재구성 파이프라인과 시각적 차이 예측기를 결합한 시스템을 제안합니다. 이 시스템은 HDR 이미지 스태킹, MTF 반전, 비네팅 보정, 기하학적 왜곡 수정, 호모그래피 변환, 색 보정을 포함하여 카메라를 정밀한 디스플레이 측정 도구로 활용합니다. 또한, 시각적 차이 예측기를 통해 다양한 자극의 가시성을 모델링합니다. 제안된 CameraVDP 프레임워크는 결함 픽셀 감지, 색 번짐 인식, 디스플레이 불균일성 평가에 유용하며, 불확실성 분석을 통해 결함 픽셀 감지 성능의 이론적 상한을 추정하고 VDP 품질 점수에 대한 신뢰 구간을 제공합니다.

## 🎯 주요 포인트

- 1. 전통적인 디스플레이 측정 방법은 공간적으로 변하는 디스플레이 결함을 포착하는 데 한계가 있다.
- 2. 카메라는 충분한 공간 해상도를 제공하지만 광학적, 샘플링, 광도 왜곡을 초래할 수 있다.
- 3. 제안된 시스템은 카메라 기반 재구성 파이프라인과 시각적 차이 예측기를 결합하여 디스플레이의 지각적 평가를 가능하게 한다.
- 4. CameraVDP 프레임워크는 결함 픽셀 감지, 색상 프린징 인식, 디스플레이 비균일성 평가에 활용된다.
- 5. 불확실성 분석 프레임워크는 결함 픽셀 감지 성능의 이론적 상한을 추정하고 VDP 품질 점수에 대한 신뢰 구간을 제공한다.


---

*Generated on 2025-09-24 05:37:02*