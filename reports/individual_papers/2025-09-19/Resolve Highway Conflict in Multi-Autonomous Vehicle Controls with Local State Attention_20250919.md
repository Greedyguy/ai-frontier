
# Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention

**Korean Title:** 다중 자율 차량 제어에서 지역 상태 주의력을 통한 고속도로 충돌 해결

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Reinforcement Learning

## 🔗 유사한 논문
- [[AI-Driven_Multi-Agent_Vehicular_Planning_for_Battery_Efficiency_and_QoS_in_6G_Smart_Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (83.8% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (82.6% similar)
- [[An_Explainable_AI_Framework_for_Dynamic_Resource_Management_in_Vehicular_Network_Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (82.4% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (81.8% similar)
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11445v1 Announce Type: cross 
Abstract: In mixed-traffic environments, autonomous vehicles must adapt to human-controlled vehicles and other unusual driving situations. This setting can be framed as a multi-agent reinforcement learning (MARL) environment with full cooperative reward among the autonomous vehicles. While methods such as Multi-agent Proximal Policy Optimization can be effective in training MARL tasks, they often fail to resolve local conflict between agents and are unable to generalize to stochastic events. In this paper, we propose a Local State Attention module to assist the input state representation. By relying on the self-attention operator, the module is expected to compress the essential information of nearby agents to resolve the conflict in traffic situations. Utilizing a simulated highway merging scenario with the priority vehicle as the unexpected event, our approach is able to prioritize other vehicles' information to manage the merging process. The results demonstrate significant improvements in merging efficiency compared to popular baselines, especially in high-density traffic settings.

## 🔍 Abstract (한글 번역)

arXiv:2506.11445v1 발표 유형: 교차  
초록: 혼합 교통 환경에서 자율 주행 차량은 인간이 조작하는 차량 및 기타 비정상적인 운전 상황에 적응해야 합니다. 이러한 환경은 자율 주행 차량 간의 완전한 협력 보상을 포함한 다중 에이전트 강화 학습(MARL) 환경으로 구성될 수 있습니다. 다중 에이전트 근접 정책 최적화(Multi-agent Proximal Policy Optimization)와 같은 방법은 MARL 작업을 훈련하는 데 효과적일 수 있지만, 에이전트 간의 지역적 충돌을 해결하지 못하고 확률적 사건에 일반화할 수 없습니다. 본 논문에서는 입력 상태 표현을 지원하기 위해 로컬 상태 주의 모듈(Local State Attention module)을 제안합니다. 자기 주의 연산자(self-attention operator)에 의존하여, 이 모듈은 교통 상황에서의 충돌을 해결하기 위해 주변 에이전트의 필수 정보를 압축할 것으로 기대됩니다. 우선 차량이 예기치 않은 사건으로 등장하는 시뮬레이션된 고속도로 합류 시나리오를 활용하여, 우리의 접근 방식은 합류 과정을 관리하기 위해 다른 차량의 정보를 우선시할 수 있습니다. 결과는 특히 고밀도 교통 환경에서 인기 있는 기준선과 비교하여 합류 효율성에서 상당한 개선을 보여줍니다.

## 📝 요약

이 논문은 혼합 교통 환경에서 자율주행차가 인간 운전 차량 및 비정상적인 주행 상황에 적응하는 문제를 다룹니다. 이를 위해 다중 에이전트 강화 학습(MARL) 환경에서 자율주행차 간의 완전 협력적 보상을 설정합니다. 기존의 방법들은 에이전트 간의 지역적 갈등 해결과 확률적 사건에 대한 일반화에 한계가 있습니다. 본 연구에서는 입력 상태 표현을 돕기 위해 Local State Attention 모듈을 제안합니다. 이 모듈은 셀프 어텐션 연산자를 활용하여 인근 에이전트의 중요한 정보를 압축해 교통 상황의 갈등을 해결합니다. 시뮬레이션된 고속도로 합류 시나리오에서 이 접근법은 우선 차량의 정보를 우선시하여 합류 과정을 관리하며, 특히 고밀도 교통 상황에서 합류 효율성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 혼합 교통 환경에서 자율 주행 차량은 인간이 조작하는 차량과 비정상적인 주행 상황에 적응해야 한다.

- 2. 본 논문은 자율 주행 차량 간의 완전한 협력 보상을 전제로 한 다중 에이전트 강화 학습 환경을 제안한다.

- 3. 기존의 다중 에이전트 근접 정책 최적화 방법은 에이전트 간의 지역적 갈등을 해결하지 못하고 확률적 사건에 일반화되지 않는다.

- 4. 제안된 로컬 상태 주의 모듈은 자가 주의 연산자를 활용하여 인접 에이전트의 필수 정보를 압축하여 교통 상황의 갈등을 해결한다.

- 5. 시뮬레이션된 고속도로 합류 시나리오에서 제안된 방법은 합류 효율성을 크게 향상시켰으며, 특히 고밀도 교통 환경에서 두드러진 성과를 보였다.

---

*Generated on 2025-09-19 15:33:26*