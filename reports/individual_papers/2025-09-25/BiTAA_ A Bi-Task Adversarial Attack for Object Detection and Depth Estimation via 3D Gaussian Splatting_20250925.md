---
keywords:
  - 3D Gaussian Splatting
  - Adversarial Attack
  - Monocular Depth Estimation
  - Cross-task Transfer
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19793
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:07:07.842073",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Adversarial Attack",
    "Monocular Depth Estimation",
    "Cross-task Transfer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Adversarial Attack": 0.8,
    "Monocular Depth Estimation": 0.82,
    "Cross-task Transfer": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel technique central to the paper's proposed attack method, offering unique insights into adversarial attacks in 3D space.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial Attack",
        "canonical": "Adversarial Attack",
        "aliases": [
          "Adversarial Manipulation"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in the paper, linking to broader discussions on security in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monocular Depth Estimation",
        "canonical": "Monocular Depth Estimation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific task affected by the proposed attack, relevant for linking to computer vision applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Cross-task Transfer",
        "canonical": "Cross-task Transfer",
        "aliases": [
          "Cross-task Interaction"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the novel aspect of the attack affecting multiple tasks, crucial for understanding multi-task interactions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Camera-based Perception",
      "Autonomous Driving"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial Attack",
      "resolved_canonical": "Adversarial Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monocular Depth Estimation",
      "resolved_canonical": "Monocular Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Cross-task Transfer",
      "resolved_canonical": "Cross-task Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# BiTAA: A Bi-Task Adversarial Attack for Object Detection and Depth Estimation via 3D Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19793.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19793](https://arxiv.org/abs/2509.19793)

## 🔗 유사한 논문
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (83.7% similar)
- [[2025-09-23/Stabilizing Information Flow Entropy_ Regularization for Safe and Interpretable Autonomous Driving Perception_20250923|Stabilizing Information Flow Entropy: Regularization for Safe and Interpretable Autonomous Driving Perception]] (82.5% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (82.4% similar)
- [[2025-09-23/Depth Edge Alignment Loss_ DEALing with Depth in Weakly Supervised Semantic Segmentation_20250923|Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation]] (81.5% similar)
- [[2025-09-24/Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable_20250924|Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Adversarial Attack|Adversarial Attack]]
**🔗 Specific Connectable**: [[keywords/Monocular Depth Estimation|Monocular Depth Estimation]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Cross-task Transfer|Cross-task Transfer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19793v1 Announce Type: new 
Abstract: Camera-based perception is critical to autonomous driving yet remains vulnerable to task-specific adversarial manipulations in object detection and monocular depth estimation. Most existing 2D/3D attacks are developed in task silos, lack mechanisms to induce controllable depth bias, and offer no standardized protocol to quantify cross-task transfer, leaving the interaction between detection and depth underexplored. We present BiTAA, a bi-task adversarial attack built on 3D Gaussian Splatting that yields a single perturbation capable of simultaneously degrading detection and biasing monocular depth. Specifically, we introduce a dual-model attack framework that supports both full-image and patch settings and is compatible with common detectors and depth estimators, with optional expectation-over-transformation (EOT) for physical reality. In addition, we design a composite loss that couples detection suppression with a signed, magnitude-controlled log-depth bias within regions of interest (ROIs) enabling controllable near or far misperception while maintaining stable optimization across tasks. We also propose a unified evaluation protocol with cross-task transfer metrics and real-world evaluations, showing consistent cross-task degradation and a clear asymmetry between Det to Depth and from Depth to Det transfer. The results highlight practical risks for multi-task camera-only perception and motivate cross-task-aware defenses in autonomous driving scenarios.

## 📝 요약

이 논문은 자율주행에서 카메라 기반 인식의 취약점을 다루며, 객체 탐지와 단안 깊이 추정에 대한 공격을 제시합니다. BiTAA라는 새로운 공격 기법은 3D Gaussian Splatting을 활용하여 탐지 성능을 저하시키고 깊이 추정에 편향을 유도합니다. 이 방법은 전체 이미지와 패치 설정 모두에서 작동하며, 일반적인 탐지기와 깊이 추정기에 호환됩니다. 또한, 탐지 억제와 깊이 편향을 결합한 손실 함수를 설계하여, 관심 영역 내에서 조절 가능한 왜곡을 유도합니다. 평가 프로토콜을 통해 탐지와 깊이 추정 간의 상호작용을 분석하고, 실제 환경에서의 성능 저하를 확인했습니다. 연구 결과는 자율주행에서 다중 작업 인식의 위험성을 강조하며, 이에 대한 방어책 개발의 필요성을 제기합니다.

## 🎯 주요 포인트

- 1. BiTAA는 3D Gaussian Splatting을 기반으로 한 이중 과제 적대적 공격으로, 객체 탐지와 단안 깊이 추정을 동시에 저하시킬 수 있는 단일 교란을 제공합니다.
- 2. 이 연구는 전체 이미지와 패치 설정을 지원하는 이중 모델 공격 프레임워크를 도입하여 일반적인 탐지기와 깊이 추정기와 호환되며, 물리적 현실을 위한 EOT 옵션을 제공합니다.
- 3. 복합 손실 설계를 통해 관심 영역 내에서 탐지 억제와 서명된 크기 제어 로그 깊이 편향을 결합하여, 안정적인 최적화를 유지하면서 근거리 또는 원거리 오인식을 제어할 수 있습니다.
- 4. 통합 평가 프로토콜을 제안하여 교차 과제 전이 메트릭과 실제 평가를 통해 일관된 교차 과제 저하와 탐지에서 깊이로, 깊이에서 탐지로의 전이 간 명확한 비대칭성을 보여줍니다.
- 5. 연구 결과는 다중 과제 카메라 기반 인식의 실질적인 위험성을 강조하며, 자율 주행 시나리오에서 교차 과제 인식 방어의 필요성을 제기합니다.


---

*Generated on 2025-09-26 09:07:07*