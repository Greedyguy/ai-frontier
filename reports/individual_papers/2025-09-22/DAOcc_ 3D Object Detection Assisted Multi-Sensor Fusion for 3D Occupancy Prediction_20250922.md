---
keywords:
  - 3D Object Detection
  - Multimodal Learning
  - Autonomous Driving
  - BEV View Range Extension
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2409.19972
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:28:31.810505",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Object Detection",
    "Multimodal Learning",
    "Autonomous Driving",
    "BEV View Range Extension"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Object Detection": 0.78,
    "Multimodal Learning": 0.82,
    "Autonomous Driving": 0.77,
    "BEV View Range Extension": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Object Detection",
        "canonical": "3D Object Detection",
        "aliases": [
          "3D Detection"
        ],
        "category": "specific_connectable",
        "rationale": "3D Object Detection is crucial for understanding spatial environments in autonomous systems, linking well with topics in robotics and computer vision.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-sensor Fusion",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Sensor Fusion"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-sensor fusion is a key aspect of multimodal learning, enhancing connectivity with other sensor-based approaches.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Autonomous Driving",
        "canonical": "Autonomous Driving",
        "aliases": [
          "Self-driving Cars"
        ],
        "category": "unique_technical",
        "rationale": "Autonomous driving is a unique application domain that connects various AI and robotics research areas.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "BEV View Range Extension",
        "canonical": "BEV View Range Extension",
        "aliases": [
          "Bird's Eye View Extension"
        ],
        "category": "unique_technical",
        "rationale": "This technique is specific to enhancing perception in lower-resolution settings, relevant for linking to perception strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Object Detection",
      "resolved_canonical": "3D Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-sensor Fusion",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Autonomous Driving",
      "resolved_canonical": "Autonomous Driving",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "BEV View Range Extension",
      "resolved_canonical": "BEV View Range Extension",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction

**Korean Title:** DAOcc: 3D 점유 예측을 위한 3D 객체 탐지 지원 다중 센서 융합

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2409.19972.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2409.19972](https://arxiv.org/abs/2409.19972)

## 🔗 유사한 논문
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (84.7% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (83.2% similar)
- [[2025-09-18/Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (82.8% similar)
- [[2025-09-18/BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (82.7% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/3D Object Detection|3D Object Detection]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Autonomous Driving|Autonomous Driving]], [[keywords/BEV View Range Extension|BEV View Range Extension]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.19972v4 Announce Type: replace 
Abstract: Multi-sensor fusion significantly enhances the accuracy and robustness of 3D semantic occupancy prediction, which is crucial for autonomous driving and robotics. However, most existing approaches depend on high-resolution images and complex networks to achieve top performance, hindering their deployment in practical scenarios. Moreover, current multi-sensor fusion approaches mainly focus on improving feature fusion while largely neglecting effective supervision strategies for those features. To address these issues, we propose DAOcc, a novel multi-modal occupancy prediction framework that leverages 3D object detection supervision to assist in achieving superior performance, while using a deployment-friendly image backbone and practical input resolution. In addition, we introduce a BEV View Range Extension strategy to mitigate performance degradation caused by lower image resolution. Extensive experiments demonstrate that DAOcc achieves new state-of-the-art results on both the Occ3D-nuScenes and Occ3D-Waymo benchmarks, and outperforms previous state-of-the-art methods by a significant margin using only a ResNet-50 backbone and 256*704 input resolution. With TensorRT optimization, DAOcc reaches 104.9 FPS while maintaining 54.2 mIoU on an NVIDIA RTX 4090 GPU. Code is available at https://github.com/AlphaPlusTT/DAOcc.

## 🔍 Abstract (한글 번역)

arXiv:2409.19972v4 발표 유형: 교체  
초록: 다중 센서 융합은 자율 주행 및 로봇 공학에 있어 중요한 3D 의미 점유 예측의 정확성과 견고성을 크게 향상시킵니다. 그러나 대부분의 기존 접근 방식은 최고 성능을 달성하기 위해 고해상도 이미지와 복잡한 네트워크에 의존하여 실제 시나리오에서의 배포를 방해합니다. 게다가, 현재의 다중 센서 융합 접근 방식은 주로 특징 융합의 개선에 초점을 맞추고 있으며, 이러한 특징에 대한 효과적인 감독 전략을 크게 간과하고 있습니다. 이러한 문제를 해결하기 위해, 우리는 3D 객체 탐지 감독을 활용하여 우수한 성능을 달성하도록 돕는 새로운 다중 모달 점유 예측 프레임워크인 DAOcc를 제안합니다. 이 프레임워크는 배포 친화적인 이미지 백본과 실용적인 입력 해상도를 사용합니다. 또한, 낮은 이미지 해상도로 인한 성능 저하를 완화하기 위해 BEV View Range Extension 전략을 도입합니다. 광범위한 실험을 통해 DAOcc가 Occ3D-nuScenes와 Occ3D-Waymo 벤치마크에서 새로운 최첨단 결과를 달성하고, ResNet-50 백본과 256*704 입력 해상도만을 사용하여 이전 최첨단 방법들을 상당한 차이로 능가함을 보여줍니다. TensorRT 최적화를 통해 DAOcc는 NVIDIA RTX 4090 GPU에서 104.9 FPS를 달성하면서도 54.2 mIoU를 유지합니다. 코드는 https://github.com/AlphaPlusTT/DAOcc에서 확인할 수 있습니다.

## 📝 요약

DAOcc는 3D 객체 탐지 감독을 활용하여 성능을 향상시키는 새로운 멀티모달 점유 예측 프레임워크입니다. 이는 실용적인 이미지 백본과 입력 해상도를 사용하여 배포 가능성을 높였습니다. 또한, BEV View Range Extension 전략을 도입하여 낮은 이미지 해상도로 인한 성능 저하를 완화합니다. DAOcc는 Occ3D-nuScenes와 Occ3D-Waymo 벤치마크에서 최첨단 성과를 달성했으며, ResNet-50 백본과 256x704 입력 해상도만으로도 이전 방법들을 능가합니다. TensorRT 최적화를 통해 NVIDIA RTX 4090 GPU에서 104.9 FPS와 54.2 mIoU를 유지합니다.

## 🎯 주요 포인트

- 1. DAOcc는 3D 객체 탐지 감독을 활용하여 성능을 향상시키는 새로운 멀티모달 점유 예측 프레임워크입니다.
- 2. 실용적인 입력 해상도와 배포 친화적인 이미지 백본을 사용하여 실제 시나리오에 적합한 솔루션을 제공합니다.
- 3. BEV View Range Extension 전략을 도입하여 낮은 이미지 해상도로 인한 성능 저하를 완화합니다.
- 4. DAOcc는 Occ3D-nuScenes 및 Occ3D-Waymo 벤치마크에서 새로운 최첨단 결과를 달성하며, ResNet-50 백본과 256*704 입력 해상도만으로 이전 방법들을 능가합니다.
- 5. TensorRT 최적화를 통해 NVIDIA RTX 4090 GPU에서 104.9 FPS를 유지하면서 54.2 mIoU를 달성합니다.


---

*Generated on 2025-09-23 12:28:31*