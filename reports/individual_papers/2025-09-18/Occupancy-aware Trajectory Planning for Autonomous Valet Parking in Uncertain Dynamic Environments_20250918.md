
# Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments

**Korean Title:** 불확실한 동적 환경에서 자율 주차를 위한 점유 인식 궤적 계획

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Exploratory Navigation

## 🔗 유사한 논문
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (83.0% similar)
- [[Disturbance-Aware_Dynamical_Trajectory_Planning_for_Air-Land_Bimodal_Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (82.9% similar)
- [[Meta-Optimization_and_Program_Search_using_Language_Models_for_Task_and_Motion_Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (81.0% similar)
- [[DECAMP: Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (80.6% similar)
- [[Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09206v2 Announce Type: replace 
Abstract: Autonomous Valet Parking (AVP) requires planning under partial observability, where parking spot availability evolves as dynamic agents enter and exit spots. Existing approaches either rely only on instantaneous spot availability or make static assumptions, thereby limiting foresight and adaptability. We propose an approach that estimates probability of future spot occupancy by distinguishing initially vacant and occupied spots while leveraging nearby dynamic agent motion. We propose a probabilistic estimator that integrates partial, noisy observations from a limited Field-of-View, with the evolving uncertainty of unobserved spots. Coupled with the estimator, we design a strategy planner that balances goal-directed parking maneuvers with exploratory navigation based on information gain, and incorporates wait-and-go behaviors at promising spots. Through randomized simulations emulating large parking lots, we demonstrate that our framework significantly improves parking efficiency and trajectory smoothness over existing approaches, while maintaining safety margins.

## 🔍 Abstract (한글 번역)

arXiv: 2509.09206v2 발표 유형: 대체
요약: 자율 주차 시스템(Autonomous Valet Parking, AVP)은 주차 공간의 가용성이 동적 에이전트가 주차 공간에 들어오고 나가면서 변하는 부분 관측 상태에서 계획이 필요합니다. 기존 접근 방식은 순간적인 주차 공간의 가용성에만 의존하거나 정적 가정을 하므로 선견지명과 적응성이 제한됩니다. 우리는 초기에 빈 공간과 점령된 공간을 구별하고 주변 동적 에이전트의 움직임을 활용하여 미래 주차 공간 점유 확률을 추정하는 접근 방식을 제안합니다. 우리는 제한된 시야(Field-of-View)에서의 부분적이고 잡음이 있는 관측을 통합하고 관측되지 않은 공간의 불확실성을 추정하는 확률적 추정기를 제안합니다. 추정기와 결합하여, 우리는 목표 지향적 주차 조작과 정보 획득에 기반한 탐사적 탐색을 균형있게 조합하고 유망한 주차 공간에서의 대기 및 이동 행동을 통합하는 전략 계획자를 설계합니다. 대규모 주차장을 모방하는 무작위 시뮬레이션을 통해, 우리의 프레임워크가 기존 접근 방식보다 주차 효율성과 궤적 부드러움을 크게 향상시킨다는 것을 입증하면서 안전 여유 공간을 유지합니다.

## 📝 요약

자율 주차 기술은 주차 공간의 가용성이 동적으로 변하는 상황에서 계획이 필요하다. 기존 방법은 순간적인 주차 공간 가용성에만 의존하거나 정적 가정을 하므로 선견지명과 적응성이 제한된다. 본 연구는 주변 동적 요소의 움직임을 활용하여 미래 주차 공간 점유 확률을 추정하는 방법을 제안한다. 제안된 확률 추정기는 제한된 시야각에서의 부분적이고 노이즈가 있는 관측을 통합하며, 관측되지 않은 공간의 불확실성을 고려한다. 이를 통해 목표 지향적인 주차 조작과 정보 획득에 기반한 탐험적 탐색을 균형 있게 계획하는 전략을 설계하였다. 대규모 주차장을 모방한 무작위 시뮬레이션을 통해, 본 프레임워크가 기존 방법보다 주차 효율성과 경로 부드러움을 현저히 향상시키는 것을 보여주었다.

## 🎯 주요 포인트

- 1. 자율 주차 기능은 부분적으로 관찰 가능한 상황에서 계획이 필요하며, 주차 공간의 가용성이 동적으로 변화함을 고려해야 한다.

- 2. 새로운 접근 방식은 미래 주차 공간 점유 확률을 추정하고, 인근 동적 요소의 움직임을 활용하여 주차 효율성을 향상시킨다.

- 3. 확률적 추정기와 전략 계획자를 결합하여 목표 지향적 주차 조작과 정보 획득에 기반한 탐험적 탐색을 조화롭게 조절한다.

---

*Generated on 2025-09-18 17:21:01*