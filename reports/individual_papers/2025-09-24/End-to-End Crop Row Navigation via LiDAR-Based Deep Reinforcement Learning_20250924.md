<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:57:15.698657",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "LiDAR Technology",
    "Voxel-based Downsampling",
    "Simulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.78,
    "LiDAR Technology": 0.82,
    "Voxel-based Downsampling": 0.79,
    "Simulation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Reinforcement Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DRL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Reinforcement Learning is a subset of Deep Learning, which is a key technology in the paper's navigation system.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D LiDAR data",
        "canonical": "LiDAR Technology",
        "aliases": [
          "LiDAR",
          "3D LiDAR"
        ],
        "category": "unique_technical",
        "rationale": "LiDAR is central to the navigation system, providing critical environmental data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Voxel-based downsampling",
        "canonical": "Voxel-based Downsampling",
        "aliases": [
          "Voxel Downsampling"
        ],
        "category": "unique_technical",
        "rationale": "This technique is crucial for reducing data size and enabling efficient learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Simulation",
        "canonical": "Simulation",
        "aliases": [
          "Simulated Environment"
        ],
        "category": "specific_connectable",
        "rationale": "Simulation is a key environment for training and validating the navigation policy.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "navigation system",
      "control commands",
      "success rate"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Reinforcement Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D LiDAR data",
      "resolved_canonical": "LiDAR Technology",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Voxel-based downsampling",
      "resolved_canonical": "Voxel-based Downsampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Simulation",
      "resolved_canonical": "Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# End-to-End Crop Row Navigation via LiDAR-Based Deep Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18608.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18608](https://arxiv.org/abs/2509.18608)

## 🔗 유사한 논문
- [[2025-09-18/Reinforcement Learning for Autonomous Point-to-Point UAV Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (84.5% similar)
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (84.1% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (83.2% similar)
- [[2025-09-23/Reinforcement Learning for Decision-Level Interception Prioritization in Drone Swarm Defense_20250923|Reinforcement Learning for Decision-Level Interception Prioritization in Drone Swarm Defense]] (82.3% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Simulation|Simulation]]
**⚡ Unique Technical**: [[keywords/LiDAR Technology|LiDAR Technology]], [[keywords/Voxel-based Downsampling|Voxel-based Downsampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18608v1 Announce Type: cross 
Abstract: Reliable navigation in under-canopy agricultural environments remains a challenge due to GNSS unreliability, cluttered rows, and variable lighting. To address these limitations, we present an end-to-end learning-based navigation system that maps raw 3D LiDAR data directly to control commands using a deep reinforcement learning policy trained entirely in simulation. Our method includes a voxel-based downsampling strategy that reduces LiDAR input size by 95.83%, enabling efficient policy learning without relying on labeled datasets or manually designed control interfaces. The policy was validated in simulation, achieving a 100% success rate in straight-row plantations and showing a gradual decline in performance as row curvature increased, tested across varying sinusoidal frequencies and amplitudes.

## 📝 요약

이 논문은 GNSS 신뢰성 문제, 복잡한 농작물 줄기, 다양한 조명 조건으로 인해 어려운 농업 환경 내 내비게이션 문제를 해결하기 위해 제안된 학습 기반 내비게이션 시스템을 소개합니다. 이 시스템은 심층 강화 학습 정책을 통해 시뮬레이션에서 훈련된 방식으로, 원시 3D LiDAR 데이터를 제어 명령으로 직접 변환합니다. 제안된 방법은 LiDAR 입력 크기를 95.83% 줄이는 보컬 기반 다운샘플링 전략을 포함하여, 라벨링된 데이터셋이나 수동 설계된 제어 인터페이스 없이 효율적인 정책 학습을 가능하게 합니다. 시뮬레이션 검증 결과, 직선형 농작물 줄기 환경에서 100% 성공률을 기록했으며, 줄기의 곡률이 증가함에 따라 성능이 점진적으로 감소하는 모습을 보였습니다.

## 🎯 주요 포인트

- 1. GNSS의 신뢰성 문제와 복잡한 환경, 가변적인 조명 때문에 농업 환경에서의 내비게이션이 어려운 문제를 해결하기 위해 연구가 진행되었습니다.
- 2. 본 연구에서는 심층 강화 학습 정책을 사용하여 원시 3D LiDAR 데이터를 제어 명령으로 직접 매핑하는 학습 기반 내비게이션 시스템을 제안합니다.
- 3. LiDAR 입력 크기를 95.83% 줄이는 복셀 기반 다운샘플링 전략을 포함하여, 라벨이 있는 데이터셋이나 수동으로 설계된 제어 인터페이스에 의존하지 않고 효율적인 정책 학습을 가능하게 합니다.
- 4. 제안된 정책은 시뮬레이션에서 검증되었으며, 직선형 농장에서는 100% 성공률을 기록하였고, 행의 곡률이 증가함에 따라 성능이 점진적으로 감소하는 경향을 보였습니다.


---

*Generated on 2025-09-24 13:57:15*