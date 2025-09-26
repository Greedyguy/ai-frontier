---
keywords:
  - Multi-Robot Task Allocation
  - Robot Coalitions
  - Network Flow Algorithms
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15052
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:31:24.945007",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Robot Task Allocation",
    "Robot Coalitions",
    "Network Flow Algorithms"
  ],
  "rejected_keywords": [
    "Task Precedence Relationships"
  ],
  "similarity_scores": {
    "Multi-Robot Task Allocation": 0.78,
    "Robot Coalitions": 0.75,
    "Network Flow Algorithms": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships

**Korean Title:** 온라인 다중 로봇 조정 및 협력: 작업 우선순위 관계

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Network Flow Algorithms|network flow-based algorithms]]
**⚡ Unique Technical**: [[keywords/Multi-Robot Task Allocation|multi-robot task allocation]], [[keywords/Robot Coalitions|robot coalitions]]

## 🔗 유사한 논문
- [[Multi-Quadruped Cooperative Object Transport Learning Decentralized Pinch-Lift-Move]] (81.2% similar)
- [[Multi-CAP A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (81.0% similar)
- [[CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (81.0% similar)
- [[Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (80.6% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15052v1 Announce Type: new 
Abstract: We propose a new formulation for the multi-robot task allocation problem that incorporates (a) complex precedence relationships between tasks, (b) efficient intra-task coordination, and (c) cooperation through the formation of robot coalitions. A task graph specifies the tasks and their relationships, and a set of reward functions models the effects of coalition size and preceding task performance. Maximizing task rewards is NP-hard; hence, we propose network flow-based algorithms to approximate solutions efficiently. A novel online algorithm performs iterative re-allocation, providing robustness to task failures and model inaccuracies to achieve higher performance than offline approaches. We comprehensively evaluate the algorithms in a testbed with random missions and reward functions and compare them to a mixed-integer solver and a greedy heuristic. Additionally, we validate the overall approach in an advanced simulator, modeling reward functions based on realistic physical phenomena and executing the tasks with realistic robot dynamics. Results establish efficacy in modeling complex missions and efficiency in generating high-fidelity task plans while leveraging task relationships.

## 🔍 Abstract (한글 번역)

arXiv:2509.15052v1 발표 유형: 신규  
초록: 우리는 (a) 작업 간의 복잡한 선행 관계, (b) 효율적인 작업 내 조정, (c) 로봇 연합 형성을 통한 협력을 포함하는 다중 로봇 작업 할당 문제에 대한 새로운 공식화를 제안합니다. 작업 그래프는 작업과 그 관계를 명시하며, 보상 함수 집합은 연합 크기와 선행 작업 성과의 영향을 모델링합니다. 작업 보상을 최대화하는 것은 NP-난해하므로, 우리는 효율적으로 해를 근사하기 위해 네트워크 흐름 기반 알고리즘을 제안합니다. 새로운 온라인 알고리즘은 반복적인 재할당을 수행하여 작업 실패와 모델 부정확성에 대한 강건성을 제공하며, 오프라인 접근법보다 높은 성능을 달성합니다. 우리는 무작위 임무와 보상 함수가 포함된 테스트베드에서 알고리즘을 종합적으로 평가하고, 이를 혼합 정수 해법 및 탐욕적 휴리스틱과 비교합니다. 또한, 현실적인 물리적 현상에 기반한 보상 함수를 모델링하고 현실적인 로봇 동역학으로 작업을 실행하는 고급 시뮬레이터에서 전체 접근법을 검증합니다. 결과는 복잡한 임무를 모델링하는 데 있어 효과적이며, 작업 관계를 활용하여 높은 충실도의 작업 계획을 생성하는 데 있어 효율적임을 입증합니다.

## 📝 요약

이 논문은 다중 로봇 작업 할당 문제를 해결하기 위해 새로운 접근 방식을 제안합니다. 주요 기여는 (a) 복잡한 작업 선행 관계, (b) 효율적인 작업 내 조정, (c) 로봇 연합을 통한 협력을 포함합니다. 작업 그래프와 보상 함수 세트를 사용하여 작업과 관계를 모델링하며, 보상 최대화 문제는 NP-난해하므로 네트워크 흐름 기반 알고리즘으로 효율적인 근사 해법을 제시합니다. 새로운 온라인 알고리즘은 반복적인 재할당을 통해 작업 실패와 모델 부정확성에 강건성을 제공하여 오프라인 접근법보다 높은 성능을 달성합니다. 알고리즘은 무작위 임무와 보상 함수로 구성된 테스트베드에서 평가되었으며, 혼합 정수 해법 및 탐욕적 기법과 비교되었습니다. 또한, 현실적인 물리적 현상을 기반으로 한 보상 함수와 로봇 동역학을 사용하여 고급 시뮬레이터에서 접근 방식을 검증했습니다. 결과적으로 복잡한 임무를 효과적으로 모델링하고 고품질의 작업 계획을 생성하는 데 효율적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 다중 로봇 작업 할당 문제를 해결하기 위해 복잡한 작업 선행 관계, 작업 내 효율적 조정, 로봇 연합 형성을 포함하는 새로운 공식을 제안합니다.

- 2. 작업 그래프와 보상 함수 세트를 사용하여 연합 크기와 선행 작업 성과의 영향을 모델링합니다.

- 3. 작업 보상 최대화 문제는 NP-난해하므로 네트워크 흐름 기반 알고리즘을 통해 효율적으로 근사 해를 제공합니다.

- 4. 새로운 온라인 알고리즘은 반복적인 재할당을 수행하여 작업 실패와 모델 부정확성에 대한 강건성을 제공하고 오프라인 접근법보다 높은 성능을 달성합니다.

- 5. 고급 시뮬레이터에서 현실적인 로봇 역학을 기반으로 한 보상 함수 모델링을 통해 전체 접근법을 검증하고, 복잡한 임무 모델링과 고품질 작업 계획 생성의 효율성을 입증합니다.

---

*Generated on 2025-09-19 16:35:49*