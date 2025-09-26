---
keywords:
  - Trajectory Optimization
  - Disturbance Observer
  - Bimodal Vehicles
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2508.05972
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:32:24.426516",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Trajectory Optimization",
    "Disturbance Observer",
    "Bimodal Vehicles"
  ],
  "rejected_keywords": [
    "Disturbance-Aware Motion Planning"
  ],
  "similarity_scores": {
    "Trajectory Optimization": 0.8,
    "Disturbance Observer": 0.79,
    "Bimodal Vehicles": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles

**Korean Title:** 공기 - 지상 이중 모드 차량을 위한 방해 인식 동적 궤적 계획

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Trajectory Optimization|trajectory optimization]]
**🔗 Specific Connectable**: [[keywords/Disturbance Observer|disturbance observer]]
**⚡ Unique Technical**: [[keywords/Bimodal Vehicles|bimodal vehicles]]

## 🔗 유사한 논문
- [[Occupancy-aware_Trajectory_Planning_for_Autonomous_Valet_Parking_in_Uncertain_Dynamic_Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (82.9% similar)
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (82.2% similar)
- [[One-Step_Model_Predictive_Path_Integral_for_Manipulator_Motion_Planning_Using_Configuration_Space_Distance_Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (82.1% similar)
- [[FlightDiffusion_Revolutionising_Autonomous_Drone_Training_with_Diffusion_Models_Generating_FPV_Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (81.9% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.05972v2 Announce Type: replace 
Abstract: Air-land bimodal vehicles provide a promising solution for navigating complex environments by combining the flexibility of aerial locomotion with the energy efficiency of ground mobility. However, planning dynamically feasible, smooth, collision-free, and energy-efficient trajectories remains challenging due to two key factors: 1) unknown dynamic disturbances in both aerial and terrestrial domains, and 2) the inherent complexity of managing bimodal dynamics with distinct constraint characteristics. This paper proposes a disturbance-aware motion-planning framework that addresses this challenge through real-time disturbance estimation and adaptive trajectory generation. The framework comprises two key components: 1) a disturbance-adaptive safety boundary adjustment mechanism that dynamically determines the feasible region of dynamic constraints for both air and land modes based on estimated disturbances via a disturbance observer, and 2) a constraint-adaptive bimodal motion planner that integrates disturbance-aware path searching to guide trajectories toward regions with reduced disturbances and B-spline-based trajectory optimization to refine trajectories within the established feasible constraint boundaries. Experimental validation on a self-developed air-land bimodal vehicle demonstrates substantial performance improvements across three representative disturbance scenarios, achieving an average 33.9% reduction in trajectory tracking error while still maintaining superior time-energy trade-offs compared to existing methods.

## 🔍 Abstract (한글 번역)

arXiv:2508.05972v2 발표 유형: 대체
요약: 공기-지상 이중 모드 차량은 공기 이동의 유연성과 지상 이동의 에너지 효율성을 결합하여 복잡한 환경을 탐색하는 유망한 솔루션을 제공합니다. 그러나, 동적으로 실행 가능하고 부드럽고 충돌이 없으며 에너지 효율적인 궤적을 계획하는 것은 두 가지 주요 요인으로 인해 여전히 어려움이 남아 있습니다: 1) 공기 및 지상 영역에서의 알려지지 않은 동적 장애물, 그리고 2) 서로 다른 제약 특성을 가진 이중 모드 동역학을 관리하는 본질적인 복잡성. 본 논문은 실시간 장애물 추정 및 적응적 궤적 생성을 통해 이러한 도전에 대처하는 장애물 인식 모션 플래닝 프레임워크를 제안합니다. 이 프레임워크는 두 가지 주요 구성 요소로 구성되어 있습니다: 1) 장애물 적응형 안전 경계 조정 메커니즘은 장애물 관측자를 통해 추정된 장애물에 기초하여 공기 및 지상 모드의 동적 제약 조건의 실행 가능한 영역을 동적으로 결정하고, 2) 제약 적응형 이중 모드 모션 플래너는 장애물 인식 경로 탐색을 통합하여 궤적을 장애물이 줄어든 영역으로 안내하고, B-스플라인 기반의 궤적 최적화를 통해 설정된 실행 가능한 제약 경계 내에서 궤적을 정제합니다. 자체 개발한 공기-지상 이중 모드 차량에서의 실험적 검증은 세 가지 대표적인 장애물 시나리오에서 상당한 성능 향상을 보여주며, 기존 방법과 비교하여 평균 33.9%의 궤적 추적 오차 감소 및 우수한 시간-에너지 교환을 유지합니다.

## 📝 요약

이 논문은 공중 및 지상 이동성의 유연성을 결합하여 복잡한 환경을 탐험하는 공지-지 양상 차량이 제공하는 유망한 솔루션에 대해 다룬다. 그러나, 공중 및 지상 도메인의 알려지지 않은 동적 장애물과 구별된 제약 특성을 가진 양상 동역학을 관리하는 복잡성으로 인해 동적으로 실행 가능하고 부드럽고 충돌이 없으며 에너지 효율적인 궤적을 계획하는 것은 여전히 어렵다. 본 논문은 실시간 장애물 추정 및 적응형 궤적 생성을 통해 이러한 도전에 대처하는 장애물 인식 모션 플래닝 프레임워크를 제안한다. 실험 결과, 기존 방법과 비교하여 궤적 추적 오차의 평균 33.9% 감소 및 우수한 시간-에너지 교환을 유지하면서 성능이 크게 향상되었다.

## 🎯 주요 포인트

- 1. 공중 및 지상 이동성의 유연성과 에너지 효율성을 결합한 공기 - 지상 이중 모드 차량은 복잡한 환경에서 항해하는 유망한 솔루션을 제공한다.

- 2. 미지의 동적 방해 및 이중 모드 역학을 관리하는 복잡성으로 인해 원활하고 충돌 없는 에너지 효율적인 경로를 계획하는 것은 여전히 어렵다.

- 3. 실시간 방해 추정 및 적응적 궤적 생성을 통해 이러한 도전에 대처하는 방해 인식 모션 플래닝 프레임워크를 제안한다.

---

*Generated on 2025-09-18 17:20:13*