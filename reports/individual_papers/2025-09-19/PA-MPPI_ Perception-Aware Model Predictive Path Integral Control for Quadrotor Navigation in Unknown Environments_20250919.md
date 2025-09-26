---
keywords:
  - Perception-Aware MPPI
  - Model Predictive Path Integral
  - Foundation Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14978
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:30:00.343199",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Perception-Aware MPPI",
    "Model Predictive Path Integral",
    "Foundation Models"
  ],
  "rejected_keywords": [
    "Quadrotor Navigation",
    "Exploration of Unknown Regions"
  ],
  "similarity_scores": {
    "Perception-Aware MPPI": 0.8,
    "Model Predictive Path Integral": 0.78,
    "Foundation Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments

**Korean Title:** PA-MPPI: 미지의 환경에서 쿼드로터 내비게이션을 위한 인지 인식 모델 예측 경로 적분 제어

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Perception-Aware MPPI|Perception-Aware MPPI]], [[keywords/Model Predictive Path Integral|Model Predictive Path Integral]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Navigation Foundation Models]]

## 🔗 유사한 논문
- [[Rethinking Reference Trajectories in Agile Drone Racing A Unified Reference-Free Model-Based Controller via MPPI]] (86.8% similar)
- [[One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (83.9% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (82.4% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (82.4% similar)
- [[ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (82.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14978v1 Announce Type: new 
Abstract: Quadrotor navigation in unknown environments is critical for practical missions such as search-and-rescue. Solving it requires addressing three key challenges: the non-convexity of free space due to obstacles, quadrotor-specific dynamics and objectives, and the need for exploration of unknown regions to find a path to the goal. Recently, the Model Predictive Path Integral (MPPI) method has emerged as a promising solution that solves the first two challenges. By leveraging sampling-based optimization, it can effectively handle non-convex free space while directly optimizing over the full quadrotor dynamics, enabling the inclusion of quadrotor-specific costs such as energy consumption. However, its performance in unknown environments is limited, as it lacks the ability to explore unknown regions when blocked by large obstacles. To solve this issue, we introduce Perception-Aware MPPI (PA-MPPI). Here, perception-awareness is defined as adapting the trajectory online based on perception objectives. Specifically, when the goal is occluded, PA-MPPI's perception cost biases trajectories that can perceive unknown regions. This expands the mapped traversable space and increases the likelihood of finding alternative paths to the goal. Through hardware experiments, we demonstrate that PA-MPPI, running at 50 Hz with our efficient perception and mapping module, performs up to 100% better than the baseline in our challenging settings where the state-of-the-art MPPI fails. In addition, we demonstrate that PA-MPPI can be used as a safe and robust action policy for navigation foundation models, which often provide goal poses that are not directly reachable.

## 🔍 Abstract (한글 번역)

arXiv:2509.14978v1 발표 유형: 신규  
초록: 미지의 환경에서 쿼드로터 내비게이션은 수색 및 구조와 같은 실질적인 임무에 있어 매우 중요합니다. 이를 해결하기 위해서는 장애물로 인해 자유 공간이 비볼록하다는 점, 쿼드로터 특유의 동역학 및 목표, 그리고 목표 지점으로의 경로를 찾기 위해 미지의 지역을 탐색해야 한다는 세 가지 주요 과제를 해결해야 합니다. 최근에 모델 예측 경로 적분법(MPPI)이 첫 번째와 두 번째 과제를 해결하는 유망한 솔루션으로 부상했습니다. 샘플링 기반 최적화를 활용하여 비볼록 자유 공간을 효과적으로 처리할 수 있으며, 쿼드로터의 전체 동역학을 직접 최적화함으로써 에너지 소비와 같은 쿼드로터 특유의 비용을 포함할 수 있습니다. 그러나 대형 장애물에 의해 차단될 때 미지의 지역을 탐색할 수 있는 능력이 부족하여 미지의 환경에서의 성능은 제한적입니다. 이 문제를 해결하기 위해 우리는 인지 인식 MPPI(PA-MPPI)를 도입합니다. 여기서 인지 인식은 인지 목표에 기반하여 온라인으로 경로를 조정하는 것으로 정의됩니다. 특히 목표가 가려져 있을 때, PA-MPPI의 인지 비용은 미지의 지역을 인식할 수 있는 경로에 편향을 줍니다. 이는 매핑된 통행 가능한 공간을 확장하고 목표로 가는 대체 경로를 찾을 가능성을 높입니다. 하드웨어 실험을 통해, 50 Hz로 작동하는 우리의 효율적인 인지 및 매핑 모듈과 함께 PA-MPPI가 최신 MPPI가 실패하는 도전적인 환경에서 기준선보다 최대 100% 더 나은 성능을 발휘함을 입증합니다. 또한, PA-MPPI가 직접 도달할 수 없는 목표 위치를 자주 제공하는 내비게이션 기초 모델을 위한 안전하고 견고한 행동 정책으로 사용될 수 있음을 입증합니다.

## 📝 요약

이 논문은 미지의 환경에서 쿼드로터의 내비게이션 문제를 다루며, 특히 탐색 및 구조와 같은 실용적인 임무에 중요성을 강조합니다. 기존의 Model Predictive Path Integral (MPPI) 방법은 비볼록 자유 공간과 쿼드로터의 동적 특성을 효과적으로 처리하지만, 큰 장애물로 인해 탐색이 제한되는 문제점을 가지고 있습니다. 이를 해결하기 위해 저자들은 Perception-Aware MPPI (PA-MPPI)를 제안합니다. PA-MPPI는 인식 목표에 따라 실시간으로 경로를 조정하여 목표가 가려진 경우에도 미지의 영역을 탐색할 수 있도록 합니다. 하드웨어 실험 결과, PA-MPPI는 기존 MPPI 대비 최대 100% 향상된 성능을 보였으며, 안전하고 견고한 내비게이션 정책으로 활용될 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 쿼드로터의 미지 환경 내비게이션은 탐색 및 구조와 같은 실용적 임무에 필수적입니다.

- 2. Model Predictive Path Integral (MPPI) 방법은 비볼록 자유 공간과 쿼드로터 동역학 최적화를 효과적으로 처리합니다.

- 3. 기존 MPPI는 큰 장애물로 인해 탐색이 제한되지만, Perception-Aware MPPI (PA-MPPI)는 인식 목표에 따라 경로를 온라인으로 조정하여 이를 해결합니다.

- 4. PA-MPPI는 하드웨어 실험에서 기존 MPPI보다 최대 100% 향상된 성능을 보여주었습니다.

- 5. PA-MPPI는 직접 도달할 수 없는 목표 위치를 제공하는 내비게이션 기초 모델에 안전하고 견고한 행동 정책으로 사용될 수 있습니다.

---

*Generated on 2025-09-19 16:34:57*