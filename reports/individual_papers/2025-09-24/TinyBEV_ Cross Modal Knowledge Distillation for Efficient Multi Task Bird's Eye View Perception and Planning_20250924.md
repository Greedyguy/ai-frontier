<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:58:10.319392",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bird's Eye View Perception",
    "Knowledge Distillation",
    "Multimodal Learning",
    "Motion Forecasting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bird's Eye View Perception": 0.78,
    "Knowledge Distillation": 0.82,
    "Multimodal Learning": 0.8,
    "Motion Forecasting": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bird's Eye View",
        "canonical": "Bird's Eye View Perception",
        "aliases": [
          "BEV"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding the spatial perception approach used in autonomous driving.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the model's ability to transfer knowledge from a larger model to a smaller one.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi Task Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MTL"
        ],
        "category": "specific_connectable",
        "rationale": "Relates to the integration of multiple tasks within a single framework.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Motion Forecasting",
        "canonical": "Motion Forecasting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific task within the perception and planning framework that is critical for autonomous systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "autonomy stack",
      "streamlined backbone"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bird's Eye View",
      "resolved_canonical": "Bird's Eye View Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi Task Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Motion Forecasting",
      "resolved_canonical": "Motion Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# TinyBEV: Cross Modal Knowledge Distillation for Efficient Multi Task Bird's Eye View Perception and Planning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18372.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18372](https://arxiv.org/abs/2509.18372)

## 🔗 유사한 논문
- [[2025-09-18/BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (84.2% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (83.0% similar)
- [[2025-09-19/VLM-E2E_ Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion_20250919|VLM-E2E: Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (82.8% similar)
- [[2025-09-23/CoBEVMoE_ Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception_20250923|CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception]] (82.7% similar)
- [[2025-09-18/FishBEV_ Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras_20250918|FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Knowledge Distillation|Knowledge Distillation]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Bird's Eye View Perception|Bird's Eye View Perception]], [[keywords/Motion Forecasting|Motion Forecasting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18372v1 Announce Type: new 
Abstract: We present TinyBEV, a unified, camera only Bird's Eye View (BEV) framework that distills the full-stack capabilities of a large planning-oriented teacher (UniAD [19]) into a compact, real-time student model. Unlike prior efficient camera only baselines such as VAD[23] and VADv2[7], TinyBEV supports the complete autonomy stack 3D detection, HD-map segmentation, motion forecasting, occupancy prediction, and goal-directed planning within a streamlined 28M-parameter backbone, achieving a 78% reduction in parameters over UniAD [19]. Our model-agnostic, multi-stage distillation strategy combines feature-level, output-level, and adaptive region-aware supervision to effectively transfer high-capacity multi-modal knowledge to a lightweight BEV representation. On nuScenes[4], Tiny-BEV achieves 39.0 mAP for detection, 1.08 minADE for motion forecasting, and a 0.32 collision rate, while running 5x faster (11 FPS) and requiring only camera input. These results demonstrate that full-stack driving intelligence can be retained in resource-constrained settings, bridging the gap between large-scale, multi-modal perception-planning models and deployment-ready real-time autonomy.

## 📝 요약

TinyBEV는 대규모 계획 지향 모델인 UniAD의 기능을 소형 실시간 모델로 압축한 카메라 기반 Bird's Eye View(BEV) 프레임워크입니다. 기존의 VAD와 VADv2와 달리, TinyBEV는 3D 탐지, HD 지도 분할, 모션 예측, 점유 예측, 목표 지향 계획을 포함한 완전한 자율주행 스택을 지원합니다. 28M 파라미터 백본을 통해 UniAD 대비 78%의 파라미터를 줄였으며, 모델에 구애받지 않는 다단계 증류 전략을 통해 고용량 멀티모달 지식을 경량 BEV 표현으로 효과적으로 전이합니다. nuScenes 데이터셋에서 TinyBEV는 39.0 mAP의 탐지 성능, 1.08 minADE의 모션 예측 성능, 0.32의 충돌률을 기록하며, 카메라 입력만으로 11 FPS의 속도로 5배 빠르게 작동합니다. 이는 제한된 자원 환경에서도 대규모 멀티모달 모델의 지능을 유지할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. TinyBEV는 카메라만을 사용하여 Bird's Eye View(BEV) 프레임워크를 구현하며, 대형 계획 지향 모델인 UniAD의 기능을 소형 실시간 모델로 압축합니다.
- 2. TinyBEV는 3D 탐지, HD-맵 분할, 모션 예측, 점유 예측, 목표 지향 계획을 포함한 완전한 자율주행 스택을 지원하며, UniAD 대비 78%의 파라미터를 절감합니다.
- 3. 모델에 구애받지 않는 다단계 증류 전략을 통해 고용량 다중 모달 지식을 경량화된 BEV 표현으로 효과적으로 전이합니다.
- 4. nuScenes 데이터셋에서 TinyBEV는 39.0 mAP의 탐지 성능과 1.08 minADE의 모션 예측 성능, 0.32의 충돌률을 기록하며, 11 FPS로 5배 빠르게 실행됩니다.
- 5. TinyBEV는 대규모 다중 모달 인식-계획 모델과 실시간 자율주행 배포 간의 격차를 줄이며, 자원 제약 환경에서도 완전한 주행 지능을 유지할 수 있음을 입증합니다.


---

*Generated on 2025-09-24 15:58:10*