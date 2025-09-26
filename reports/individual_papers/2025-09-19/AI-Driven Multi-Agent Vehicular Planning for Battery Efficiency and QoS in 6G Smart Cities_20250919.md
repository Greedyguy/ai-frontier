---
keywords:
  - Reinforcement Learning
  - Machine Learning
  - Vehicular IoT
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14877
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:58:47.914388",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Machine Learning",
    "Vehicular IoT"
  ],
  "rejected_keywords": [
    "Osmotic Computing"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.78,
    "Machine Learning": 0.85,
    "Vehicular IoT": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities

**Korean Title:** AI 기반 다중 에이전트 차량 계획: 6G 스마트 시티에서의 배터리 효율성과 QoS를 위한 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Machine Learning|AI algorithms]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|dynamic agent planning]]
**⚡ Unique Technical**: [[keywords/Vehicular IoT|vehicular IoT nodes]]

## 🔗 유사한 논문
- [[VEGA Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization]] (81.3% similar)
- [[Occupancy-aware_Trajectory_Planning_for_Autonomous_Valet_Parking_in_Uncertain_Dynamic_Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (81.2% similar)
- [[TeraSim-World Worldwide Safety-Critical Data Synthesis for End-to-End Autonomous Driving]] (81.2% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.8% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14877v1 Announce Type: cross 
Abstract: While simulators exist for vehicular IoT nodes communicating with the Cloud through Edge nodes in a fully-simulated osmotic architecture, they often lack support for dynamic agent planning and optimisation to minimise vehicular battery consumption while ensuring fair communication times. Addressing these challenges requires extending current simulator architectures with AI algorithms for both traffic prediction and dynamic agent planning. This paper presents an extension of SimulatorOrchestrator (SO) to meet these requirements. Preliminary results over a realistic urban dataset show that utilising vehicular planning algorithms can lead to improved battery and QoS performance compared with traditional shortest path algorithms. The additional inclusion of desirability areas enabled more ambulances to be routed to their target destinations while utilising less energy to do so, compared to traditional and weighted algorithms without desirability considerations.

## 🔍 Abstract (한글 번역)

arXiv:2509.14877v1 발표 유형: 교차  
초록: 차량 IoT 노드가 에지 노드를 통해 클라우드와 통신하는 완전 시뮬레이션된 삼투 아키텍처를 위한 시뮬레이터가 존재하지만, 이들은 종종 차량 배터리 소비를 최소화하면서 공정한 통신 시간을 보장하기 위한 동적 에이전트 계획 및 최적화 지원이 부족합니다. 이러한 문제를 해결하기 위해서는 교통 예측 및 동적 에이전트 계획을 위한 AI 알고리즘으로 현재의 시뮬레이터 아키텍처를 확장해야 합니다. 본 논문은 이러한 요구 사항을 충족하기 위해 SimulatorOrchestrator (SO)의 확장을 제시합니다. 현실적인 도시 데이터셋을 기반으로 한 초기 결과는 차량 계획 알고리즘을 활용하면 전통적인 최단 경로 알고리즘에 비해 배터리 및 QoS 성능이 향상될 수 있음을 보여줍니다. 추가적으로, 선호 지역을 포함함으로써 전통적 및 가중치 알고리즘에서 선호도를 고려하지 않은 경우보다 더 많은 구급차가 더 적은 에너지를 사용하여 목표 목적지로 경로를 설정할 수 있었습니다.

## 📝 요약

이 논문은 차량 IoT 노드가 엣지 노드를 통해 클라우드와 통신하는 완전 시뮬레이션된 삼투 아키텍처에서의 배터리 소모 최소화와 공정한 통신 시간을 보장하기 위한 동적 에이전트 계획 및 최적화의 필요성을 강조합니다. 이를 해결하기 위해 현재 시뮬레이터 아키텍처에 AI 알고리즘을 확장하여 교통 예측 및 동적 에이전트 계획을 가능하게 합니다. 논문은 SimulatorOrchestrator(SO)의 확장을 제안하며, 초기 실험 결과는 현실적인 도시 데이터셋에서 차량 계획 알고리즘이 전통적인 최단 경로 알고리즘보다 배터리 및 QoS 성능을 향상시킬 수 있음을 보여줍니다. 또한, 선호 지역을 고려한 알고리즘은 전통적 및 가중치 알고리즘보다 적은 에너지를 사용하여 더 많은 구급차를 목표지로 안내할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 기존 시뮬레이터는 차량 IoT 노드의 배터리 소비를 최소화하면서 공정한 통신 시간을 보장하는 동적 에이전트 계획 및 최적화를 지원하지 못한다.

- 2. 현재 시뮬레이터 아키텍처에 AI 알고리즘을 추가하여 교통 예측 및 동적 에이전트 계획을 수행해야 한다.

- 3. SimulatorOrchestrator(SO)의 확장을 통해 차량 계획 알고리즘을 활용하면 전통적인 최단 경로 알고리즘보다 배터리 및 QoS 성능이 향상될 수 있다.

- 4. 선호 지역을 고려한 알고리즘을 추가하면 전통적인 가중치 알고리즘보다 적은 에너지를 사용하여 더 많은 구급차를 목표 목적지로 라우팅할 수 있다.

---

*Generated on 2025-09-19 15:01:53*