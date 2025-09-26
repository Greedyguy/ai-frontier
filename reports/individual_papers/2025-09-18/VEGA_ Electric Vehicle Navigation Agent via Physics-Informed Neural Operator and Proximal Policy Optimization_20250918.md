---
keywords:
  - Reinforcement Learning
  - Proximal Policy Optimization
  - Electric Vehicle Navigation
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13386
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:01:57.857770",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Proximal Policy Optimization",
    "Electric Vehicle Navigation"
  ],
  "rejected_keywords": [
    "Physics-Informed Neural Operator"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.9,
    "Proximal Policy Optimization": 0.85,
    "Electric Vehicle Navigation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# VEGA: Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization

**Korean Title:** 다음은 해당 학술 텍스트의 한국어 번역입니다:

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Electric Vehicle Navigation|Electric Vehicle Navigation]]

## 🔗 유사한 논문
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (79.4% similar)
- [[Occupancy-aware_Trajectory_Planning_for_Autonomous_Valet_Parking_in_Uncertain_Dynamic_Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (77.9% similar)
- [[FSR-VLN Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (77.3% similar)
- [[NavMoE Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (77.2% similar)
- [[CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (76.9% similar)

VEGA: 물리 정보 기반 신경 연산자와 근접 정책 최적화를 통한 전기차 내비게이션 에이전트

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13386v1 Announce Type: cross 
Abstract: Demands for software-defined vehicles (SDV) are rising and electric vehicles (EVs) are increasingly being equipped with powerful computers. This enables onboard AI systems to optimize charge-aware path optimization customized to reflect vehicle's current condition and environment. We present VEGA, a charge-aware EV navigation agent that plans over a charger-annotated road graph using Proximal Policy Optimization (PPO) with budgeted A* teacher-student guidance under state-of-charge (SoC) feasibility. VEGA consists of two modules. First, a physics-informed neural operator (PINO), trained on real vehicle speed and battery-power logs, uses recent vehicle speed logs to estimate aerodynamic drag, rolling resistance, mass, motor and regenerative-braking efficiencies, and auxiliary load by learning a vehicle-custom dynamics. Second, a Reinforcement Learning (RL) agent uses these dynamics to optimize a path with optimal charging stops and dwell times under SoC constraints. VEGA requires no additional sensors and uses only vehicle speed signals. It may serve as a virtual sensor for power and efficiency to potentially reduce EV cost. In evaluation on long routes like San Francisco to New York, VEGA's stops, dwell times, SoC management, and total travel time closely track Tesla Trip Planner while being slightly more conservative, presumably due to real vehicle conditions such as vehicle parameter drift due to deterioration. Although trained only in U.S. regions, VEGA was able to compute optimal charge-aware paths in France and Japan, demonstrating generalizability. It achieves practical integration of physics-informed learning and RL for EV eco-routing.

## 🔍 Abstract (한글 번역)

arXiv:2509.13386v1 발표 유형: 교차 분야
초록: 소프트웨어 정의 차량(SDV)에 대한 수요가 증가하고 있으며, 전기차(EV)에는 점점 더 강력한 컴퓨터가 탑재되고 있다. 이는 차량의 현재 상태와 환경을 반영하도록 맞춤화된 충전 인식 경로 최적화를 위한 온보드 AI 시스템을 가능하게 한다. 본 연구에서는 충전소 주석이 달린 도로 그래프에서 충전상태(SoC) 실현가능성 하에서 예산 제약 A* 교사-학생 지도를 통한 근접 정책 최적화(PPO)를 사용하여 계획을 수립하는 충전 인식 전기차 내비게이션 에이전트인 VEGA를 제시한다. VEGA는 두 개의 모듈로 구성된다. 첫째, 실제 차량 속도 및 배터리 전력 로그로 훈련된 물리학 정보 기반 신경 연산자(PINO)는 최근의 차량 속도 로그를 사용하여 차량별 맞춤 동역학을 학습함으로써 공기역학적 항력, 구름 저항, 질량, 모터 및 회생제동 효율성, 보조 부하를 추정한다. 둘째, 강화학습(RL) 에이전트는 이러한 동역학을 사용하여 SoC 제약 조건 하에서 최적의 충전 정차지와 체류 시간을 가진 경로를 최적화한다. VEGA는 추가 센서가 필요하지 않으며 차량 속도 신호만을 사용한다. 이는 전력과 효율성에 대한 가상 센서 역할을 하여 잠재적으로 전기차 비용을 줄일 수 있다. 샌프란시스코에서 뉴욕까지와 같은 장거리 경로에 대한 평가에서, VEGA의 정차지, 체류 시간, SoC 관리, 총 이동 시간은 Tesla Trip Planner와 밀접하게 일치하면서도 약간 더 보수적인 결과를 보였는데, 이는 노화로 인한 차량 매개변수 편향과 같은 실제 차량 조건 때문인 것으로 추정된다. 미국 지역에서만 훈련되었음에도 불구하고, VEGA는 프랑스와 일본에서 최적의 충전 인식 경로를 계산할 수 있었으며, 이는 일반화 가능성을 보여준다. 이는 전기차 친환경 경로 설정을 위한 물리학 정보 기반 학습과 강화학습의 실용적 통합을 달성한다.

## 📝 요약

소프트웨어 정의 차량(SDV)과 전기차(EV)의 발전으로, 차량의 현재 상태와 환경을 반영한 최적 경로 탐색이 가능해졌습니다. 본 논문에서는 VEGA라는 충전 인식 EV 내비게이션 에이전트를 소개합니다. VEGA는 충전소가 표시된 도로 그래프에서 Proximal Policy Optimization(PPO)과 예산화된 A* 교사-학생 지도를 사용하여 경로를 계획합니다. VEGA는 두 가지 모듈로 구성됩니다. 첫 번째 모듈은 실제 차량 속도 및 배터리 전력 로그를 기반으로 훈련된 물리 정보 기반 신경 연산자(PINO)로, 차량의 동적 특성을 학습하여 공기역학적 항력, 구름 저항, 질량, 모터 및 회생 제동 효율, 보조 부하를 추정합니다. 두 번째 모듈은 강화 학습(RL) 에이전트로, SoC 제약 하에 최적의 경로와 충전 정지 및 대기 시간을 최적화합니다. VEGA는 추가 센서 없이 차량 속도 신호만 사용하며, 전력 및 효율성의 가상 센서로 활용될 수 있습니다. 샌프란시스코에서 뉴욕까지의 장거리 경로 평가에서 VEGA는 테슬라 트립 플래너와 유사한 결과를 보였으며, 차량 파라미터 변화로 인한 보수적 경향을 나타냈습니다. 미국에서만 훈련되었음에도 불구하고 프랑스와 일본에서도 최적 경로를 계산할 수 있어 일반화 가능성을 입증했습니다. VEGA는 물리 정보 학습과 RL을 통합하여 EV 에코 라우팅을 실현합니다.

## 🎯 주요 포인트

- 1. 소프트웨어 정의 차량(SDV)과 전기차(EV)의 수요 증가에 따라 VEGA라는 충전 인식 EV 내비게이션 에이전트가 개발되었습니다.

- 2. VEGA는 Proximal Policy Optimization(PPO)과 예산화된 A* 교사-학생 지도를 사용하여 충전소가 주석된 도로 그래프를 기반으로 경로를 계획합니다.

- 3. VEGA는 물리학 기반 신경 연산자(PINO)와 강화 학습(RL) 에이전트로 구성되어, 차량의 동적 특성을 학습하고 최적의 충전 정차와 체류 시간을 최적화합니다.

- 4. VEGA는 추가 센서 없이 차량 속도 신호만을 사용하여 전력과 효율성을 가상 센서로 제공함으로써 EV 비용 절감을 도모할 수 있습니다.

- 5. VEGA는 미국에서만 훈련되었음에도 불구하고 프랑스와 일본에서도 최적의 충전 인식 경로를 계산할 수 있어 일반화 가능성을 입증했습니다.

---

*Generated on 2025-09-19 11:26:01*