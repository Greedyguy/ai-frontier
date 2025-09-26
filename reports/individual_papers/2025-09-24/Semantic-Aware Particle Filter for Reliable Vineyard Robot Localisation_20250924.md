<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:21:57.455894",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semantic Particle Filter",
    "LiDAR",
    "Semantic Walls",
    "GPS Prior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semantic Particle Filter": 0.78,
    "LiDAR": 0.82,
    "Semantic Walls": 0.75,
    "GPS Prior": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "semantic particle filter",
        "canonical": "Semantic Particle Filter",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for robot localization in vineyards, enhancing connectivity with robotics and AI fields.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "LiDAR scans",
        "canonical": "LiDAR",
        "aliases": [
          "LiDAR-based methods"
        ],
        "category": "broad_technical",
        "rationale": "LiDAR is a fundamental technology in robotics and autonomous systems, facilitating strong technical connections.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "semantic walls",
        "canonical": "Semantic Walls",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents an innovative concept to address perceptual aliasing, relevant for linking to spatial reasoning in robotics.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "GPS prior",
        "canonical": "GPS Prior",
        "aliases": [
          "noisy GPS prior"
        ],
        "category": "specific_connectable",
        "rationale": "Enhances localization accuracy, connecting to broader discussions on sensor fusion in robotics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "semantic particle filter",
      "resolved_canonical": "Semantic Particle Filter",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LiDAR scans",
      "resolved_canonical": "LiDAR",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "semantic walls",
      "resolved_canonical": "Semantic Walls",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "GPS prior",
      "resolved_canonical": "GPS Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Semantic-Aware Particle Filter for Reliable Vineyard Robot Localisation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18342.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18342](https://arxiv.org/abs/2509.18342)

## 🔗 유사한 논문
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (85.6% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (83.1% similar)
- [[2025-09-23/SWA-PF_ Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments_20250923|SWA-PF: Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments]] (83.0% similar)
- [[2025-09-23/A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments_20250923|A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments]] (81.6% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/LiDAR|LiDAR]]
**🔗 Specific Connectable**: [[keywords/GPS Prior|GPS Prior]]
**⚡ Unique Technical**: [[keywords/Semantic Particle Filter|Semantic Particle Filter]], [[keywords/Semantic Walls|Semantic Walls]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18342v1 Announce Type: cross 
Abstract: Accurate localisation is critical for mobile robots in structured outdoor environments, yet LiDAR-based methods often fail in vineyards due to repetitive row geometry and perceptual aliasing. We propose a semantic particle filter that incorporates stable object-level detections, specifically vine trunks and support poles into the likelihood estimation process. Detected landmarks are projected into a birds eye view and fused with LiDAR scans to generate semantic observations. A key innovation is the use of semantic walls, which connect adjacent landmarks into pseudo-structural constraints that mitigate row aliasing. To maintain global consistency in headland regions where semantics are sparse, we introduce a noisy GPS prior that adaptively supports the filter. Experiments in a real vineyard demonstrate that our approach maintains localisation within the correct row, recovers from deviations where AMCL fails, and outperforms vision-based SLAM methods such as RTAB-Map.

## 📝 요약

이 논문은 포도밭과 같은 구조화된 야외 환경에서 모바일 로봇의 정확한 위치 추정을 위한 방법을 제안합니다. 기존의 LiDAR 기반 방법은 반복적인 행의 기하학적 구조와 인식 혼동으로 인해 실패할 수 있습니다. 이를 해결하기 위해, 이 연구는 포도나무 줄기와 지지대를 포함한 안정적인 객체 수준의 탐지를 활용한 의미론적 입자 필터를 제안합니다. 탐지된 랜드마크는 조감도로 투영되어 LiDAR 스캔과 결합되어 의미론적 관찰을 생성합니다. 주요 혁신은 인접 랜드마크를 연결하여 행의 혼동을 줄이는 의미론적 벽을 사용하는 것입니다. 또한, 의미가 희박한 지역에서는 적응적으로 필터를 지원하는 GPS 사전 정보를 도입하여 전역적 일관성을 유지합니다. 실제 포도밭 실험에서 이 방법은 정확한 행 내에서의 위치 추정을 유지하고, AMCL이 실패하는 경우에도 회복하며, RTAB-Map과 같은 비전 기반 SLAM 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 반복적인 행 구조와 지각적 혼동으로 인해 포도밭에서 LiDAR 기반 방법이 실패하는 문제를 해결하기 위해 안정적인 객체 수준의 검출을 활용한 의미론적 입자 필터를 제안합니다.
- 2. 포도나무 줄기와 지지대를 포함한 검출된 랜드마크를 조감도로 투영하고 LiDAR 스캔과 융합하여 의미론적 관측을 생성합니다.
- 3. 인접한 랜드마크를 연결하여 행 혼동을 줄이는 가상의 구조적 제약인 의미론적 벽을 사용하는 것이 주요 혁신입니다.
- 4. 의미가 희박한 헤드랜드 지역에서 전역 일관성을 유지하기 위해 적응적으로 필터를 지원하는 GPS 사전 정보를 도입합니다.
- 5. 실제 포도밭 실험에서 제안된 방법이 정확한 행 내에서 위치를 유지하고, AMCL이 실패하는 경우에도 복구하며, RTAB-Map과 같은 비전 기반 SLAM 방법보다 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 16:21:57*