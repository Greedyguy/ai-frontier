---
keywords:
  - Reinforcement Learning
  - Autonomous UAV Navigation
  - Gym-compatible training environment
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13943
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:13:43.364774",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Autonomous UAV Navigation",
    "Gym-compatible training environment"
  ],
  "rejected_keywords": [
    "Robot Operating System"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.9,
    "Autonomous UAV Navigation": 0.78,
    "Gym-compatible training environment": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Reinforcement Learning for Autonomous Point-to-Point UAV Navigation

**Korean Title:** 자율적인 지점 간 UAV 항법을 위한 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Autonomous UAV Navigation|Autonomous UAV Navigation]], [[keywords/Gym-compatible training environment|Gym-compatible training environment]]

## 🔗 유사한 논문
- [[Maximizing UAV Cellular Connectivity with Reinforcement Learning for BVLoS Path Planning]] (87.3% similar)
- [[Agentic_UAVs_LLM-Driven_Autonomy_with_Integrated_Tool-Calling_and_Cognitive_Reasoning_20250918|Agentic UAVs: LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning]] (82.9% similar)
- [[Dual Actor DDPG for Airborne STAR-RIS Assisted Communications]] (81.4% similar)
- [[Language_Conditioning_Improves_Accuracy_of_Aircraft_Goal_Prediction_in_Untowered_Airspace_20250918|Language Conditioning Improves Accuracy of Aircraft Goal Prediction in Untowered Airspace]] (80.6% similar)
- [[FlightDiffusion_Revolutionising_Autonomous_Drone_Training_with_Diffusion_Models_Generating_FPV_Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13943v1 Announce Type: new 
Abstract: Unmanned Aerial Vehicles (UAVs) are increasingly used in automated inspection, delivery, and navigation tasks that require reliable autonomy. This project develops a reinforcement learning (RL) approach to enable a single UAV to autonomously navigate between predefined points without manual intervention. The drone learns navigation policies through trial-and-error interaction, using a custom reward function that encourages goal-reaching efficiency while penalizing collisions and unsafe behavior. The control system integrates ROS with a Gym-compatible training environment, enabling flexible deployment and testing. After training, the learned policy is deployed on a real UAV platform and evaluated under practical conditions. Results show that the UAV can successfully perform autonomous navigation with minimal human oversight, demonstrating the viability of RL-based control for point-to-point drone operations in real-world scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.13943v1 발표 유형: 새로운
요약: 무인 항공기 (UAVs)는 신뢰할 수 있는 자율성이 필요한 자동 검사, 배송 및 항법 작업에서 점점 더 많이 사용되고 있습니다. 본 프로젝트는 단일 UAV가 수동 개입 없이 미리 정의된 지점 사이를 자율적으로 항해할 수 있도록 강화 학습 (RL) 접근 방식을 개발합니다. 드론은 사용자 정의 보상 함수를 사용하여 시행착오 상호작용을 통해 항해 정책을 학습하며, 이 함수는 목표 달성 효율성을 촉진하고 충돌 및 안전하지 않은 행동을 처벌합니다. 제어 시스템은 ROS를 Gym 호환 훈련 환경과 통합하여 유연한 배포와 테스트를 가능하게 합니다. 훈련 후, 학습된 정책은 실제 UAV 플랫폼에 배포되어 실제 조건에서 평가됩니다. 결과는 UAV가 최소한의 인간 감독으로 자율 항해를 성공적으로 수행할 수 있음을 보여주며, 실제 세계 시나리오에서 지점 간 드론 작업을 위한 RL 기반 제어의 실현 가능성을 입증합니다.

## 📝 요약

한 UAV가 수동 개입 없이 미리 정의된 지점 간을 자율적으로 항해할 수 있도록 하는 강화 학습(RL) 접근법을 개발하였다. 드론은 목표 달성 효율성을 장려하고 충돌 및 불안전 행동을 처벌하는 사용자 정의 보상 함수를 사용하여 항해 정책을 학습한다. 제어 시스템은 ROS를 Gym과 호환되는 훈련 환경과 통합하여 유연한 배포 및 테스트를 가능하게 한다. 훈련 후 학습된 정책은 실제 UAV 플랫폼에 배포되어 현실적인 조건에서 평가되었으며, 결과는 UAV가 최소한의 인간 감독으로 자율 항해를 성공적으로 수행할 수 있음을 보여주며, 실제 상황에서 RL 기반 제어의 실용성을 입증한다.

## 🎯 주요 포인트

- 1. 무인 항공기는 신뢰할 수 있는 자율성이 필요한 자동 검사, 배송 및 항법 작업에 점점 더 많이 사용되고 있습니다.

- 2. 이 연구는 보상 함수를 사용하여 항법 정책을 학습하는 강화 학습 접근 방식을 개발했습니다.

- 3. 제어 시스템은 ROS를 Gym 호환 훈련 환경과 통합하여 유연한 배포 및 테스트를 가능하게 합니다.

---

*Generated on 2025-09-18 17:15:57*