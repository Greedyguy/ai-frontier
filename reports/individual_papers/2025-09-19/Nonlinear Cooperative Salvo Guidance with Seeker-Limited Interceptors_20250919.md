---
keywords:
  - Cooperative Guidance
  - Sliding Mode Consensus Protocol
  - Deviated Pursuit Guidance
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15136
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:32:27.929315",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cooperative Guidance",
    "Sliding Mode Consensus Protocol",
    "Deviated Pursuit Guidance"
  ],
  "rejected_keywords": [
    "Fixed-Time Distributed Observer"
  ],
  "similarity_scores": {
    "Cooperative Guidance": 0.78,
    "Sliding Mode Consensus Protocol": 0.75,
    "Deviated Pursuit Guidance": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors

**Korean Title:** 비선형 협력 일제 유도: 탐색기 제한 요격기와 함께

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Cooperative Guidance|cooperative guidance strategy]], [[keywords/Sliding Mode Consensus Protocol|higher-order sliding mode consensus protocol]], [[keywords/Deviated Pursuit Guidance|deviated pursuit guidance]]

## 🔗 유사한 논문
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (82.4% similar)
- [[Barometer-Aided Attitude Estimation_20250918|Barometer-Aided Attitude Estimation]] (79.6% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.3% similar)
- [[Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (78.8% similar)
- [[Rethinking Reference Trajectories in Agile Drone Racing A Unified Reference-Free Model-Based Controller via MPPI]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15136v1 Announce Type: cross 
Abstract: This paper presents a cooperative guidance strategy for the simultaneous interception of a constant-velocity, non-maneuvering target, addressing the realistic scenario where only a subset of interceptors are equipped with onboard seekers. To overcome the resulting heterogeneity in target observability, a fixed-time distributed observer is employed, enabling seeker-less interceptors to estimate the target state using information from seeker-equipped agents and local neighbors over a directed communication topology. Departing from conventional strategies that approximate time-to-go via linearization or small-angle assumptions, the proposed approach leverages deviated pursuit guidance where the time-to-go expression is exact for such a target. Moreover, a higher-order sliding mode consensus protocol is utilized to establish time-to-go consensus within a finite time. The effectiveness of the proposed guidance and estimation architecture is demonstrated through simulations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15136v1 발표 유형: 교차  
초록: 이 논문은 일정 속도로 움직이며 기동하지 않는 표적을 동시에 요격하기 위한 협력 유도 전략을 제시하며, 요격기 중 일부만이 온보드 탐지기를 장착한 현실적인 시나리오를 다룹니다. 표적 관측 가능성의 이질성을 극복하기 위해 고정 시간 분산 관측자를 사용하여, 탐지기가 없는 요격기들이 탐지기가 장착된 요격기와 지역 이웃으로부터의 정보를 통해 표적 상태를 추정할 수 있도록 합니다. 시간-도달을 선형화나 소각 가정으로 근사하는 기존 전략에서 벗어나, 제안된 접근법은 그러한 표적에 대해 정확한 시간-도달 표현을 제공하는 편향 추적 유도를 활용합니다. 또한, 고차 슬라이딩 모드 합의 프로토콜을 사용하여 유한 시간 내에 시간-도달 합의를 설정합니다. 제안된 유도 및 추정 아키텍처의 효과는 시뮬레이션을 통해 입증됩니다.

## 📝 요약

이 논문은 일정 속도로 움직이는 비기동 표적을 동시에 요격하기 위한 협력 유도 전략을 제안합니다. 모든 요격기가 탐지기를 장착하지 않은 현실적인 상황을 고려하여, 탐지기가 없는 요격기가 탐지기가 장착된 요격기와 이웃으로부터 정보를 받아 표적 상태를 추정할 수 있도록 고정 시간 분산 관측자를 사용합니다. 기존의 선형화나 소각 가정에 의존하는 방법과 달리, 제안된 접근법은 정확한 시간 계산이 가능한 편향 추적 유도를 활용합니다. 또한, 고차 슬라이딩 모드 합의 프로토콜을 통해 유한 시간 내에 시간 합의를 달성합니다. 제안된 유도 및 추정 구조의 효과는 시뮬레이션을 통해 입증되었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 일정 속도의 비기동 표적을 동시에 요격하기 위한 협력 유도 전략을 제안합니다.

- 2. 일부 요격기만 탐색기를 장착한 현실적인 시나리오에서 표적 관측의 이질성을 극복하기 위해 고정 시간 분산 관측기를 사용합니다.

- 3. 탐색기가 없는 요격기는 탐색기가 장착된 요격기와 지역 이웃의 정보를 통해 표적 상태를 추정할 수 있습니다.

- 4. 기존의 선형화 또는 소각 가정에 의존하는 방법과 달리, 본 접근법은 정확한 시간-도달 표현을 활용합니다.

- 5. 제안된 유도 및 추정 아키텍처의 효과는 시뮬레이션을 통해 입증되었습니다.

---

*Generated on 2025-09-19 16:36:43*