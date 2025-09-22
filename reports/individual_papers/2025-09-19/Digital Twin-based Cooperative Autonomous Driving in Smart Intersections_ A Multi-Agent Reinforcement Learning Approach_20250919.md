
# Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach

**Korean Title:** 스마트 교차로에서 디지털 트윈 기반 협력 자율 주행: 다중 에이전트 강화 학습 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Proximal Policy Optimization, Behavior Cloning

## 🔗 유사한 논문
- [[Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (85.6% similar)
- [[AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (84.5% similar)
- [[Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (84.5% similar)
- [[Mining the Long Tail A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (83.3% similar)
- [[Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15099v1 Announce Type: new 
Abstract: Unsignalized intersections pose safety and efficiency challenges due to complex traffic flows and blind spots. In this paper, a digital twin (DT)-based cooperative driving system with roadside unit (RSU)-centric architecture is proposed for enhancing safety and efficiency at unsignalized intersections. The system leverages comprehensive bird-eye-view (BEV) perception to eliminate blind spots and employs a hybrid reinforcement learning (RL) framework combining offline pre-training with online fine-tuning. Specifically, driving policies are initially trained using conservative Q-learning (CQL) with behavior cloning (BC) on real datasets, then fine-tuned using multi-agent proximal policy optimization (MAPPO) with self-attention mechanisms to handle dynamic multi-agent coordination. The RSU implements real-time commands via vehicle-to-infrastructure (V2I) communications. Experimental results show that the proposed method yields failure rates below 0.03\% coordinating up to three connected autonomous vehicles (CAVs), significantly outperforming traditional methods. In addition, the system exhibits sub-linear computational scaling with inference times under 40 ms. Furthermore, it demonstrates robust generalization across diverse unsignalized intersection scenarios, indicating its practicality and readiness for real-world deployment.

## 🔍 Abstract (한글 번역)

arXiv:2509.15099v1 발표 유형: 신규  
초록: 비신호 교차로는 복잡한 교통 흐름과 사각지대 때문에 안전 및 효율성 문제를 제기합니다. 본 논문에서는 비신호 교차로에서의 안전성과 효율성을 향상시키기 위해 도로변 장치(RSU) 중심의 아키텍처를 갖춘 디지털 트윈(DT) 기반 협력 주행 시스템을 제안합니다. 이 시스템은 종합적인 조감도(BEV) 인식을 활용하여 사각지대를 제거하고, 오프라인 사전 학습과 온라인 미세 조정을 결합한 하이브리드 강화 학습(RL) 프레임워크를 사용합니다. 구체적으로, 주행 정책은 실제 데이터셋에서 행동 복제를 통한 보수적 Q-학습(CQL)을 사용하여 초기 학습을 진행한 후, 동적 다중 에이전트 조정을 처리하기 위해 자기 주의 메커니즘을 갖춘 다중 에이전트 근접 정책 최적화(MAPPO)를 사용하여 미세 조정됩니다. RSU는 차량-인프라(V2I) 통신을 통해 실시간 명령을 구현합니다. 실험 결과에 따르면, 제안된 방법은 최대 세 대의 연결된 자율 주행 차량(CAV)을 조정하는 데 있어 실패율이 0.03% 이하로, 전통적인 방법을 크게 능가합니다. 또한, 이 시스템은 40ms 이하의 추론 시간으로 준선형 계산 확장성을 나타냅니다. 더 나아가, 다양한 비신호 교차로 시나리오에서 강력한 일반화 능력을 보여주어 실제 환경에 대한 실용성과 준비성을 나타냅니다.

## 📝 요약

이 논문은 비신호 교차로에서의 안전성과 효율성을 개선하기 위해 도로변 장치(RSU) 중심의 디지털 트윈(DT) 기반 협력 주행 시스템을 제안합니다. 이 시스템은 조감도(BEV) 인식을 활용하여 사각지대를 제거하고, 오프라인 사전 학습과 온라인 미세 조정을 결합한 하이브리드 강화 학습(RL) 프레임워크를 사용합니다. 구체적으로, 주행 정책은 실제 데이터셋을 기반으로 보수적 Q-러닝(CQL)과 행동 복제(BC)를 통해 초기 학습한 후, 다중 에이전트 근접 정책 최적화(MAPPO)와 자기 주의 메커니즘을 사용하여 동적 다중 에이전트 조정을 처리합니다. RSU는 차량-인프라(V2I) 통신을 통해 실시간 명령을 수행합니다. 실험 결과, 제안된 방법은 최대 3대의 연결된 자율 차량(CAV)을 조정할 때 실패율이 0.03% 미만으로, 기존 방법보다 뛰어난 성능을 보였습니다. 또한, 다양한 비신호 교차로 시나리오에서 강력한 일반화 능력을 보여 실용성과 실세계 적용 가능성을 입증했습니다.

## 🎯 주요 포인트

- 1. 비신호 교차로의 안전성과 효율성을 높이기 위해 디지털 트윈 기반의 협력 운전 시스템이 제안되었습니다.

- 2. 이 시스템은 조류 시야(BEV) 인식을 활용하여 사각지대를 제거하고, 오프라인 사전 학습과 온라인 미세 조정을 결합한 하이브리드 강화 학습 프레임워크를 사용합니다.

- 3. 제안된 방법은 최대 세 대의 연결된 자율주행차(CAV)를 조정할 때 실패율이 0.03% 이하로, 전통적인 방법보다 성능이 뛰어납니다.

- 4. 시스템은 다양한 비신호 교차로 시나리오에서 강력한 일반화 능력을 보여주며, 실시간 명령을 차량-인프라(V2I) 통신을 통해 구현합니다.

- 5. 추론 시간이 40ms 이하로, 시스템의 계산 확장성이 준선형적이며 실세계 배치를 위한 실용성과 준비성을 나타냅니다.

---

*Generated on 2025-09-19 16:44:52*