---
keywords:
  - Deep Learning
  - Configurable Modular Segmentation Network
  - Kamino Dataset
  - Semantic Segmentation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19378
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:52:05.229250",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Configurable Modular Segmentation Network",
    "Kamino Dataset",
    "Semantic Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Configurable Modular Segmentation Network": 0.8,
    "Kamino Dataset": 0.78,
    "Semantic Segmentation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the proposed perception system, linking it to broader AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "CMSNet",
        "canonical": "Configurable Modular Segmentation Network",
        "aliases": [
          "CMSNet"
        ],
        "category": "unique_technical",
        "rationale": "CMSNet is a unique framework introduced in the paper, crucial for understanding the system's architecture.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Kamino dataset",
        "canonical": "Kamino Dataset",
        "aliases": [
          "Kamino"
        ],
        "category": "unique_technical",
        "rationale": "The Kamino dataset is a novel contribution, providing a valuable resource for off-road autonomous vehicle research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Semantic Segmentation is a key process in the system for identifying drivable regions, linking to image processing research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "autonomous vehicles",
      "off-road environment",
      "real-time inference"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "CMSNet",
      "resolved_canonical": "Configurable Modular Segmentation Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Kamino dataset",
      "resolved_canonical": "Kamino Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Vision-Based Perception for Autonomous Vehicles in Off-Road Environment Using Deep Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19378.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19378](https://arxiv.org/abs/2509.19378)

## 🔗 유사한 논문
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (83.9% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (83.8% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (83.1% similar)
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (82.9% similar)
- [[2025-09-23/A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments_20250923|A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Semantic Segmentation|Semantic Segmentation]]
**⚡ Unique Technical**: [[keywords/Configurable Modular Segmentation Network|Configurable Modular Segmentation Network]], [[keywords/Kamino Dataset|Kamino Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19378v1 Announce Type: cross 
Abstract: Low-latency intelligent systems are required for autonomous driving on non-uniform terrain in open-pit mines and developing countries. This work proposes a perception system for autonomous vehicles on unpaved roads and off-road environments, capable of navigating rough terrain without a predefined trail. The Configurable Modular Segmentation Network (CMSNet) framework is proposed, facilitating different architectural arrangements. CMSNet configurations were trained to segment obstacles and trafficable ground on new images from unpaved/off-road scenarios with adverse conditions (night, rain, dust). We investigated applying deep learning to detect drivable regions without explicit track boundaries, studied algorithm behavior under visibility impairment, and evaluated field tests with real-time semantic segmentation. A new dataset, Kamino, is presented with almost 12,000 images from an operating vehicle with eight synchronized cameras. The Kamino dataset has a high number of labeled pixels compared to similar public collections and includes images from an off-road proving ground emulating a mine under adverse visibility. To achieve real-time inference, CMSNet CNN layers were methodically removed and fused using TensorRT, C++, and CUDA. Empirical experiments on two datasets validated the proposed system's effectiveness.

## 📝 요약

이 연구는 비포장 도로와 오프로드 환경에서 자율 주행 차량을 위한 인지 시스템을 제안합니다. CMSNet이라는 구성 가능한 모듈식 세분화 네트워크 프레임워크를 통해 다양한 아키텍처 구성을 가능하게 하며, 새로운 이미지에서 장애물과 주행 가능한 지면을 세분화하도록 훈련되었습니다. 특히, 명확한 경계가 없는 주행 가능 지역을 심층 학습으로 탐지하고, 가시성이 저하된 상황에서 알고리즘의 동작을 연구했습니다. 실제 환경에서 실시간 의미론적 세분화 테스트를 통해 시스템의 효과를 검증했습니다. 새로운 데이터셋인 Kamino는 8개의 동기화된 카메라로 촬영된 약 12,000장의 이미지를 포함하며, 가시성이 열악한 조건을 모사한 오프로드 시험장에서 수집되었습니다. 실시간 추론을 위해 CMSNet의 CNN 레이어를 TensorRT, C++, CUDA를 사용하여 최적화했습니다. 두 개의 데이터셋을 통한 실험으로 시스템의 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. 비포장 도로 및 오프로드 환경에서 자율 주행 차량을 위한 인지 시스템을 제안하였습니다.
- 2. CMSNet 프레임워크를 통해 다양한 건축적 배열을 지원하며, 장애물 및 주행 가능한 지면을 분할하는 학습을 수행했습니다.
- 3. 새로운 데이터셋인 Kamino를 소개하였으며, 이는 가혹한 가시성 조건을 모방한 오프로드 시험장에서 수집된 약 12,000장의 이미지로 구성되어 있습니다.
- 4. 실시간 추론을 위해 CMSNet의 CNN 레이어를 TensorRT, C++, CUDA를 사용하여 제거 및 융합하였습니다.
- 5. 두 개의 데이터셋을 통한 실험을 통해 제안된 시스템의 효과성을 검증하였습니다.


---

*Generated on 2025-09-25 16:52:05*