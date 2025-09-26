---
keywords:
  - Multi-Object Tracking
  - Depth-Informed Trajectory Refinement
  - Tracking-By-Detection
  - Depth Cues
  - DETR-based Detector
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17323
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:48:44.460134",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Object Tracking",
    "Depth-Informed Trajectory Refinement",
    "Tracking-By-Detection",
    "Depth Cues",
    "DETR-based Detector"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Object Tracking": 0.82,
    "Depth-Informed Trajectory Refinement": 0.78,
    "Tracking-By-Detection": 0.75,
    "Depth Cues": 0.77,
    "DETR-based Detector": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Object Tracking",
        "canonical": "Multi-Object Tracking",
        "aliases": [
          "MOT"
        ],
        "category": "specific_connectable",
        "rationale": "A core concept in computer vision, linking to various tracking methodologies and datasets.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Depth-Informed Trajectory Refinement",
        "canonical": "Depth-Informed Trajectory Refinement",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to improve tracking accuracy by leveraging depth information.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Tracking-By-Detection",
        "canonical": "Tracking-By-Detection",
        "aliases": [
          "TBD"
        ],
        "category": "specific_connectable",
        "rationale": "A widely used paradigm in object tracking that connects to various detection methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Depth Cues",
        "canonical": "Depth Cues",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Essential for enhancing tracking robustness, especially in occlusion scenarios.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      },
      {
        "surface": "DETR-based Detector",
        "canonical": "DETR-based Detector",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific application of transformers in object detection, relevant for linking to transformer-based models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.73
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
      "candidate_surface": "Multi-Object Tracking",
      "resolved_canonical": "Multi-Object Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Depth-Informed Trajectory Refinement",
      "resolved_canonical": "Depth-Informed Trajectory Refinement",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Tracking-By-Detection",
      "resolved_canonical": "Tracking-By-Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Depth Cues",
      "resolved_canonical": "Depth Cues",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "DETR-based Detector",
      "resolved_canonical": "DETR-based Detector",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# DepTR-MOT: Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17323.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17323](https://arxiv.org/abs/2509.17323)

## 🔗 유사한 논문
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (85.9% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.4% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (82.3% similar)
- [[2025-09-23/TinyDef-DETR_ A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery_20250923|TinyDef-DETR: A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery]] (81.9% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Object Tracking|Multi-Object Tracking]], [[keywords/Tracking-By-Detection|Tracking-By-Detection]], [[keywords/Depth Cues|Depth Cues]]
**⚡ Unique Technical**: [[keywords/Depth-Informed Trajectory Refinement|Depth-Informed Trajectory Refinement]], [[keywords/DETR-based Detector|DETR-based Detector]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17323v1 Announce Type: new 
Abstract: Visual Multi-Object Tracking (MOT) is a crucial component of robotic perception, yet existing Tracking-By-Detection (TBD) methods often rely on 2D cues, such as bounding boxes and motion modeling, which struggle under occlusions and close-proximity interactions. Trackers relying on these 2D cues are particularly unreliable in robotic environments, where dense targets and frequent occlusions are common. While depth information has the potential to alleviate these issues, most existing MOT datasets lack depth annotations, leading to its underexploited role in the domain. To unveil the potential of depth-informed trajectory refinement, we introduce DepTR-MOT, a DETR-based detector enhanced with instance-level depth information. Specifically, we propose two key innovations: (i) foundation model-based instance-level soft depth label supervision, which refines depth prediction, and (ii) the distillation of dense depth maps to maintain global depth consistency. These strategies enable DepTR-MOT to output instance-level depth during inference, without requiring foundation models and without additional computational cost. By incorporating depth cues, our method enhances the robustness of the TBD paradigm, effectively resolving occlusion and close-proximity challenges. Experiments on both the QuadTrack and DanceTrack datasets demonstrate the effectiveness of our approach, achieving HOTA scores of 27.59 and 44.47, respectively. In particular, results on QuadTrack, a robotic platform MOT dataset, highlight the advantages of our method in handling occlusion and close-proximity challenges in robotic tracking. The source code will be made publicly available at https://github.com/warriordby/DepTR-MOT.

## 📝 요약

이 논문은 로봇 환경에서의 다중 객체 추적(MOT) 문제를 해결하기 위해 DepTR-MOT라는 새로운 방법을 제안합니다. 기존의 2D 기반 추적 방법은 가림 현상과 근접 상호작용에서 한계를 보입니다. 이를 개선하기 위해, 이 연구는 인스턴스 수준의 깊이 정보를 활용한 DETR 기반의 추적기를 개발했습니다. 주요 기여는 (i) 인스턴스 수준의 부드러운 깊이 레이블 감독과 (ii) 전역 깊이 일관성을 유지하기 위한 밀집 깊이 맵 증류입니다. 이러한 방법은 추가적인 계산 비용 없이 깊이 정보를 활용하여 추적의 강인성을 높입니다. QuadTrack과 DanceTrack 데이터셋 실험 결과, 각각 HOTA 점수 27.59와 44.47을 기록하며, 특히 로봇 추적에서 가림과 근접 문제를 효과적으로 해결함을 보여줍니다. 소스 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 기존의 2D 단서에 의존하는 추적 방법은 로봇 환경에서의 밀집된 타겟과 빈번한 가림 현상에 취약합니다.
- 2. DepTR-MOT는 인스턴스 수준의 깊이 정보를 활용하여 깊이 기반 궤적 개선을 목표로 하는 DETR 기반 탐지기입니다.
- 3. 제안된 방법은 인스턴스 수준의 부드러운 깊이 레이블 감독과 밀집 깊이 맵의 증류를 통해 깊이 예측을 개선합니다.
- 4. DepTR-MOT는 추가적인 계산 비용 없이 깊이 단서를 통합하여 추적의 강인성을 향상시킵니다.
- 5. QuadTrack 및 DanceTrack 데이터셋 실험에서 각각 HOTA 점수 27.59와 44.47을 기록하며, 특히 로봇 추적에서의 가림 및 근접 문제 해결에 효과적임을 보여줍니다.


---

*Generated on 2025-09-24 04:48:44*