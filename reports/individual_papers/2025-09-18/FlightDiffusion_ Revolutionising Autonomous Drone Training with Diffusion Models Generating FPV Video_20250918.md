---
keywords:
  - Diffusion Models
  - Autonomous Drones
  - Generative Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14082
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:28:19.585956",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Autonomous Drones",
    "Generative Models"
  ],
  "rejected_keywords": [
    "First-Person View Video"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.9,
    "Autonomous Drones": 0.8,
    "Generative Models": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video

**Korean Title:** 비행 확산: FPV 비디오 생성을 통해 확산 모델을 활용한 자율 드론 훈련 혁신

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generative Models|Generative Models]]
**⚡ Unique Technical**: [[keywords/Autonomous Drones|Autonomous Drones]]
**🚀 Evolved Concepts**: [[keywords/Diffusion Models|Diffusion Models]]

## 🔗 유사한 논문
- [[PRISM-DP_Spatial_Pose-based_Observations_for_Diffusion-Policies_via_Segmentation,_Mesh_Generation,_and_Pose_Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (82.6% similar)
- [[SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (82.2% similar)
- [[Disturbance-Aware_Dynamical_Trajectory_Planning_for_Air-Land_Bimodal_Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (81.9% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.8% similar)
- [[Dual Actor DDPG for Airborne STAR-RIS Assisted Communications]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14082v1 Announce Type: new 
Abstract: We present FlightDiffusion, a diffusion-model-based framework for training autonomous drones from first-person view (FPV) video. Our model generates realistic video sequences from a single frame, enriched with corresponding action spaces to enable reasoning-driven navigation in dynamic environments. Beyond direct policy learning, FlightDiffusion leverages its generative capabilities to synthesize diverse FPV trajectories and state-action pairs, facilitating the creation of large-scale training datasets without the high cost of real-world data collection. Our evaluation demonstrates that the generated trajectories are physically plausible and executable, with a mean position error of 0.25 m (RMSE 0.28 m) and a mean orientation error of 0.19 rad (RMSE 0.24 rad). This approach enables improved policy learning and dataset scalability, leading to superior performance in downstream navigation tasks. Results in simulated environments highlight enhanced robustness, smoother trajectory planning, and adaptability to unseen conditions. An ANOVA revealed no statistically significant difference between performance in simulation and reality (F(1, 16) = 0.394, p = 0.541), with success rates of M = 0.628 (SD = 0.162) and M = 0.617 (SD = 0.177), respectively, indicating strong sim-to-real transfer. The generated datasets provide a valuable resource for future UAV research. This work introduces diffusion-based reasoning as a promising paradigm for unifying navigation, action generation, and data synthesis in aerial robotics.

## 🔍 Abstract (한글 번역)

arXiv:2509.14082v1 발표 유형: 새로운
요약: 우리는 FlightDiffusion을 제시합니다. 이는 자율 드론을 학습하기 위한 확산 모델 기반 프레임워크로, 일인칭 시점 (FPV) 비디오에서 생성된 현실적인 비디오 시퀀스를 제공합니다. 우리의 모델은 단일 프레임에서 현실적인 비디오 시퀀스를 생성하며, 해당 액션 공간을 풍부하게 제공하여 동적 환경에서의 추론 주도 항법을 가능하게 합니다. 직접적인 정책 학습 이상으로, FlightDiffusion은 생성 능력을 활용하여 다양한 FPV 경로와 상태-액션 쌍을 합성하여 대규모 훈련 데이터셋을 실제 데이터 수집의 높은 비용 없이 생성할 수 있습니다. 우리의 평가는 생성된 경로가 물리적으로 타당하고 실행 가능하며, 평균 위치 오차는 0.25m (RMSE 0.28m)이고, 평균 방향 오차는 0.19 rad (RMSE 0.24 rad)임을 보여줍니다. 이 접근 방식은 향상된 정책 학습과 데이터셋 확장성을 가능하게 하여 하류 항법 작업에서 우수한 성능을 제공합니다. 시뮬레이션 환경에서의 결과는 향상된 견고성, 부드러운 경로 계획 및 보이지 않는 조건에 대한 적응력을 강조합니다. ANOVA 분석 결과 시뮬레이션과 현실에서의 성능 간에 통계적으로 유의미한 차이가 없음을 보여주었으며 (F(1, 16) = 0.394, p = 0.541), 각각의 성공률은 M = 0.628 (SD = 0.162) 및 M = 0.617 (SD = 0.177)로, 강한 시뮬레이션에서 현실로의 전이를 나타냅니다. 생성된 데이터셋은 향후 UAV 연구에 중요한 자원을 제공합니다. 본 연구는 항공로봇학에서 항법, 액션 생성 및 데이터 합성을 통합하는 유망한 패러다임으로 확산 기반 추론을 소개합니다.

## 📝 요약

본 연구는 자율 비행 드론을 학습시키기 위한 확산 모델 기반 프레임워크인 FlightDiffusion을 제안한다. 이 모델은 실시간 비디오를 생성하고 동적 환경에서 추론 주도 항법을 가능하게 하는 행동 공간과 함께 풍부한 비디오 시퀀스를 생성한다. FlightDiffusion은 정책 학습 뿐만 아니라 다양한 FPV 궤적과 상태-행동 쌍을 합성하여 대규모 훈련 데이터셋을 생성하는 데 기여한다. 실험 결과, 생성된 궤적은 물리적으로 타당하고 실행 가능하며, 시뮬레이션과 현실 간 강한 전이 가능성을 보여준다. 이 연구는 확산 기반 추론을 통해 비행로봇학에서 항법, 행동 생성 및 데이터 합성을 통합하는 유망한 패러다임을 제시한다.

## 🎯 주요 포인트

- 1. FlightDiffusion은 FPV 비디오로부터 자율 드롐을 훈련하는데 사용되는 확산 모델 기반 프레임워크이다.

- 2. FlightDiffusion은 다양한 FPV 궤적 및 상태-행동 쌍을 합성하여 대규모 훈련 데이터셋을 생성하는 데 도움을 준다.

- 3. 생성된 궤적은 물리적으로 타당하며 실행 가능하며, 시뮬레이션과 현실 간 강한 전이 가능성을 보여준다.

---

*Generated on 2025-09-18 17:17:13*