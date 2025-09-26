---
keywords:
  - Multi-Robot Connectivity-Aware Planner
  - Vehicle Routing Problem
  - Hierarchical Coverage Path Planning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14941
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:33:09.443422",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Robot Connectivity-Aware Planner",
    "Vehicle Routing Problem",
    "Hierarchical Coverage Path Planning"
  ],
  "rejected_keywords": [
    "Adjacency Graph"
  ],
  "similarity_scores": {
    "Multi-Robot Connectivity-Aware Planner": 0.8,
    "Vehicle Routing Problem": 0.78,
    "Hierarchical Coverage Path Planning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Multi-CAP: A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments

**Korean Title:** 멀티-CAP: 미지의 환경을 위한 다중 로봇 연결 인식 계층적 커버리지 경로 계획 알고리즘

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vehicle Routing Problem|Vehicle Routing Problem]]
**⚡ Unique Technical**: [[keywords/Multi-Robot Connectivity-Aware Planner|Multi-Robot Connectivity-Aware Planner]], [[keywords/Hierarchical Coverage Path Planning|Hierarchical Coverage Path Planning]]

## 🔗 유사한 논문
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (84.4% similar)
- [[AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (82.0% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (82.0% similar)
- [[Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (82.0% similar)
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14941v1 Announce Type: new 
Abstract: Efficient coordination of multiple robots for coverage of large, unknown environments is a significant challenge that involves minimizing the total coverage path length while reducing inter-robot conflicts. In this paper, we introduce a Multi-robot Connectivity-Aware Planner (Multi-CAP), a hierarchical coverage path planning algorithm that facilitates multi-robot coordination through a novel connectivity-aware approach. The algorithm constructs and dynamically maintains an adjacency graph that represents the environment as a set of connected subareas. Critically, we make the assumption that the environment, while unknown, is bounded. This allows for incremental refinement of the adjacency graph online to ensure its structure represents the physical layout of the space, both in observed and unobserved areas of the map as robots explore the environment. We frame the task of assigning subareas to robots as a Vehicle Routing Problem (VRP), a well-studied problem for finding optimal routes for a fleet of vehicles. This is used to compute disjoint tours that minimize redundant travel, assigning each robot a unique, non-conflicting set of subareas. Each robot then executes its assigned tour, independently adapting its coverage strategy within each subarea to minimize path length based on real-time sensor observations of the subarea. We demonstrate through simulations and multi-robot hardware experiments that Multi-CAP significantly outperforms state-of-the-art methods in key metrics, including coverage time, total path length, and path overlap ratio. Ablation studies further validate the critical role of our connectivity-aware graph and the global tour planner in achieving these performance gains.

## 🔍 Abstract (한글 번역)

arXiv:2509.14941v1 발표 유형: 신규  
초록: 대규모, 미지의 환경을 커버하기 위한 다중 로봇의 효율적인 협력은 총 커버리지 경로 길이를 최소화하면서 로봇 간 충돌을 줄이는 중요한 과제입니다. 본 논문에서는 다중 로봇 협력을 촉진하기 위해 새로운 연결 인식 접근 방식을 사용하는 계층적 커버리지 경로 계획 알고리즘인 다중 로봇 연결 인식 플래너(Multi-CAP)를 소개합니다. 이 알고리즘은 환경을 연결된 하위 영역 집합으로 나타내는 인접 그래프를 구성하고 동적으로 유지합니다. 중요한 점은 환경이 미지의 상태이지만 경계가 있다는 가정을 합니다. 이는 로봇이 환경을 탐색함에 따라 인접 그래프의 구조가 공간의 물리적 레이아웃을 나타내도록 온라인에서 점진적으로 정제할 수 있게 합니다. 하위 영역을 로봇에 할당하는 작업을 차량 경로 문제(VRP)로 설정하여 차량 함대의 최적 경로를 찾는 잘 연구된 문제를 활용합니다. 이를 통해 중복 이동을 최소화하는 분리된 투어를 계산하여 각 로봇에 고유하고 충돌 없는 하위 영역 집합을 할당합니다. 각 로봇은 할당된 투어를 실행하며, 각 하위 영역 내에서 실시간 센서 관측에 기반하여 경로 길이를 최소화하는 커버리지 전략을 독립적으로 조정합니다. 시뮬레이션 및 다중 로봇 하드웨어 실험을 통해 Multi-CAP이 커버리지 시간, 총 경로 길이, 경로 중복 비율을 포함한 주요 지표에서 최첨단 방법을 크게 능가함을 입증합니다. 또한, 절제 연구를 통해 이러한 성능 향상에 있어 연결 인식 그래프와 글로벌 투어 플래너의 중요한 역할을 검증합니다.

## 📝 요약

이 논문에서는 대규모 미지의 환경에서 다중 로봇의 효율적인 협력을 위한 Multi-robot Connectivity-Aware Planner (Multi-CAP)을 제안합니다. 이 알고리즘은 연결성을 고려한 새로운 접근 방식을 통해 로봇 간의 조율을 용이하게 하며, 환경을 연결된 하위 영역으로 나타내는 인접 그래프를 동적으로 유지합니다. 환경이 제한적이라는 가정 하에, 로봇이 탐색하면서 관찰된 및 미관찰된 영역을 포함하여 그래프를 점진적으로 개선합니다. 하위 영역 할당은 차량 경로 문제(VRP)로 설정하여 각 로봇이 중복되지 않는 경로를 따라 이동하도록 합니다. 시뮬레이션 및 하드웨어 실험 결과, Multi-CAP은 최신 방법들보다 커버리지 시간, 총 경로 길이, 경로 중복률에서 우수한 성능을 보였습니다. 연결성을 고려한 그래프와 글로벌 투어 계획의 중요성도 입증되었습니다.

## 🎯 주요 포인트

- 1. Multi-CAP은 다중 로봇의 효율적인 협력을 위해 연결 인식 접근 방식을 사용하는 계층적 커버리지 경로 계획 알고리즘입니다.

- 2. 알고리즘은 환경을 연결된 하위 영역 집합으로 나타내는 인접 그래프를 동적으로 유지 관리합니다.

- 3. 하위 영역 할당 문제를 차량 경로 문제(VRP)로 설정하여 로봇 간의 경로 중복을 최소화합니다.

- 4. 각 로봇은 실시간 센서 관측을 기반으로 하위 영역 내에서 경로 길이를 최소화하는 전략을 독립적으로 적용합니다.

- 5. 시뮬레이션 및 하드웨어 실험을 통해 Multi-CAP이 최신 방법들보다 커버리지 시간, 총 경로 길이, 경로 중복 비율에서 우수한 성능을 보임을 입증했습니다.

---

*Generated on 2025-09-19 16:33:49*