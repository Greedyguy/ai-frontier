---
keywords:
  - Monocular Visual-Inertial Motion and Depth Estimation
  - Dense Metric Depth Estimation
  - MSCKF-based Motion Tracking
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19713
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:03:40.786195",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Monocular Visual-Inertial Motion and Depth Estimation",
    "Dense Metric Depth Estimation",
    "MSCKF-based Motion Tracking",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Monocular Visual-Inertial Motion and Depth Estimation": 0.92,
    "Dense Metric Depth Estimation": 0.85,
    "MSCKF-based Motion Tracking": 0.8,
    "Zero-Shot Learning": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "monocular visual-inertial motion and depth",
        "canonical": "Monocular Visual-Inertial Motion and Depth Estimation",
        "aliases": [
          "VIMD"
        ],
        "category": "unique_technical",
        "rationale": "This is the core focus of the paper, representing a novel framework that integrates visual and inertial data for depth estimation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "dense metric depth estimation",
        "canonical": "Dense Metric Depth Estimation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a key technical term that connects to the broader field of 3D visual perception in robotics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "MSCKF-based monocular visual-inertial motion tracking",
        "canonical": "MSCKF-based Motion Tracking",
        "aliases": [
          "MSCKF"
        ],
        "category": "unique_technical",
        "rationale": "This specific method is central to the paper's approach and is a unique application of MSCKF in this context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "zero-shot generalization",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "This term connects to the trending concept of zero-shot learning, highlighting the framework's adaptability.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "3D visual perception",
      "resource constrained settings"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "monocular visual-inertial motion and depth",
      "resolved_canonical": "Monocular Visual-Inertial Motion and Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "dense metric depth estimation",
      "resolved_canonical": "Dense Metric Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "MSCKF-based monocular visual-inertial motion tracking",
      "resolved_canonical": "MSCKF-based Motion Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "zero-shot generalization",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# VIMD: Monocular Visual-Inertial Motion and Depth Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19713.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19713](https://arxiv.org/abs/2509.19713)

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (87.3% similar)
- [[2025-09-24/Zero-shot Monocular Metric Depth for Endoscopic Images_20250924|Zero-shot Monocular Metric Depth for Endoscopic Images]] (83.7% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (83.7% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (83.6% similar)
- [[2025-09-24/RS3DBench_ A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing_20250924|RS3DBench: A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Dense Metric Depth Estimation|Dense Metric Depth Estimation]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Monocular Visual-Inertial Motion and Depth Estimation|Monocular Visual-Inertial Motion and Depth Estimation]], [[keywords/MSCKF-based Motion Tracking|MSCKF-based Motion Tracking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19713v1 Announce Type: new 
Abstract: Accurate and efficient dense metric depth estimation is crucial for 3D visual perception in robotics and XR. In this paper, we develop a monocular visual-inertial motion and depth (VIMD) learning framework to estimate dense metric depth by leveraging accurate and efficient MSCKF-based monocular visual-inertial motion tracking. At the core the proposed VIMD is to exploit multi-view information to iteratively refine per-pixel scale, instead of globally fitting an invariant affine model as in the prior work. The VIMD framework is highly modular, making it compatible with a variety of existing depth estimation backbones. We conduct extensive evaluations on the TartanAir and VOID datasets and demonstrate its zero-shot generalization capabilities on the AR Table dataset. Our results show that VIMD achieves exceptional accuracy and robustness, even with extremely sparse points as few as 10-20 metric depth points per image. This makes the proposed VIMD a practical solution for deployment in resource constrained settings, while its robust performance and strong generalization capabilities offer significant potential across a wide range of scenarios.

## 📝 요약

이 논문은 로봇 공학과 XR에서 중요한 3D 시각 인식을 위해 정확하고 효율적인 밀집 메트릭 깊이 추정을 목표로 하는 단안 비주얼-관성 모션 및 깊이(VIMD) 학습 프레임워크를 제안합니다. 기존의 전역 불변 아핀 모델 대신, 다중 뷰 정보를 활용하여 픽셀 단위로 스케일을 반복적으로 개선하는 방법론을 채택했습니다. VIMD는 다양한 깊이 추정 백본과 호환 가능한 모듈식 구조를 가지고 있으며, TartanAir와 VOID 데이터셋에서의 평가와 AR Table 데이터셋에서의 제로샷 일반화 능력을 입증했습니다. 결과적으로, VIMD는 이미지당 10-20개의 매우 희소한 메트릭 깊이 점에서도 뛰어난 정확성과 강인함을 보여주며, 자원이 제한된 환경에서도 실용적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. VIMD 학습 프레임워크는 MSCKF 기반의 단안 시각-관성 모션 추적을 활용하여 밀집 메트릭 깊이를 정확하고 효율적으로 추정합니다.
- 2. VIMD는 다중 뷰 정보를 활용하여 픽셀 단위로 스케일을 반복적으로 개선하며, 기존의 전역 불변 아핀 모델을 대체합니다.
- 3. VIMD 프레임워크는 모듈화되어 있어 다양한 기존 깊이 추정 백본과 호환이 가능합니다.
- 4. TartanAir 및 VOID 데이터셋에서 광범위한 평가를 통해 VIMD의 제로샷 일반화 능력을 입증하였으며, AR Table 데이터셋에서도 뛰어난 성능을 보였습니다.
- 5. VIMD는 이미지당 10-20개의 메트릭 깊이 포인트와 같은 극도로 희소한 점에서도 뛰어난 정확도와 강인함을 보여주며, 자원 제한 환경에서의 실용적인 솔루션을 제공합니다.


---

*Generated on 2025-09-26 09:03:40*