# Exploring multimodal implicit behavior learning for vehicle navigation in simulated cities

**Korean Title:** 시뮬레이션된 도시에서 차량 내비게이션을 위한 다중 모달 암묵적 행동 학습 탐구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Derivative-Free Inference

## 🔗 유사한 논문
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (81.2% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (79.3% similar)
- [[2025-09-19/VLM-E2E_ Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion_20250919|VLM-E2E Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (78.9% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections A Multi-Agent Reinforcement Learning Approach]] (78.7% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (78.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15400v1 Announce Type: cross 
Abstract: Standard Behavior Cloning (BC) fails to learn multimodal driving decisions, where multiple valid actions exist for the same scenario. We explore Implicit Behavioral Cloning (IBC) with Energy-Based Models (EBMs) to better capture this multimodality. We propose Data-Augmented IBC (DA-IBC), which improves learning by perturbing expert actions to form the counterexamples of IBC training and using better initialization for derivative-free inference. Experiments in the CARLA simulator with Bird's-Eye View inputs demonstrate that DA-IBC outperforms standard IBC in urban driving tasks designed to evaluate multimodal behavior learning in a test environment. The learned energy landscapes are able to represent multimodal action distributions, which BC fails to achieve.

## 🔍 Abstract (한글 번역)

arXiv:2509.15400v1 발표 유형: 교차  
초록: 표준 행동 복제(Behavior Cloning, BC)는 동일한 상황에서 여러 유효한 행동이 존재하는 다중 모드 운전 결정을 학습하는 데 실패합니다. 우리는 에너지 기반 모델(EBM)을 사용한 암시적 행동 복제(Implicit Behavioral Cloning, IBC)를 탐구하여 이러한 다중 모드를 더 잘 포착하고자 합니다. 우리는 IBC 훈련의 반례를 형성하기 위해 전문가의 행동을 변형하고, 파생물 없는 추론을 위한 더 나은 초기화를 사용하여 학습을 개선하는 데이터 증강 IBC(Data-Augmented IBC, DA-IBC)를 제안합니다. Bird's-Eye View 입력을 사용하는 CARLA 시뮬레이터 실험에서 DA-IBC는 테스트 환경에서 다중 모드 행동 학습을 평가하기 위해 설계된 도시 운전 과제에서 표준 IBC보다 우수한 성능을 보였습니다. 학습된 에너지 지형은 BC가 달성하지 못한 다중 모드 행동 분포를 나타낼 수 있습니다.

## 📝 요약

이 논문은 표준 행동 복제(BC)가 다양한 운전 결정을 학습하는 데 실패하는 문제를 다룹니다. 이를 해결하기 위해 에너지 기반 모델(EBM)을 활용한 암시적 행동 복제(IBC)를 탐구합니다. 저자들은 데이터 증강 IBC(DA-IBC)를 제안하여, 전문가의 행동을 변형하여 IBC 훈련의 반례를 만들고 파생이 없는 추론을 위한 초기화를 개선함으로써 학습을 향상시킵니다. CARLA 시뮬레이터 실험 결과, DA-IBC는 도시 운전 과제에서 표준 IBC보다 뛰어난 성능을 보였으며, 학습된 에너지 지형은 BC가 달성하지 못한 다중 모드 행동 분포를 효과적으로 표현할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 표준 행동 복제(BC)는 동일한 상황에서 여러 유효한 행동이 존재하는 다중 모달 운전 결정을 학습하는 데 실패합니다.

- 2. 에너지 기반 모델(EBM)을 활용한 암묵적 행동 복제(IBC)는 다중 모달성을 더 잘 포착할 수 있습니다.

- 3. 데이터 증강 IBC(DA-IBC)는 전문가 행동을 교란하여 IBC 훈련의 반례를 형성하고 파생 없는 추론을 위한 더 나은 초기화를 사용하여 학습을 개선합니다.

- 4. CARLA 시뮬레이터에서 Bird's-Eye View 입력을 사용한 실험 결과, DA-IBC는 테스트 환경에서 다중 모달 행동 학습을 평가하기 위해 설계된 도시 운전 작업에서 표준 IBC보다 우수한 성능을 보였습니다.

- 5. 학습된 에너지 지형은 BC가 달성하지 못하는 다중 모달 행동 분포를 나타낼 수 있습니다.

---

*Generated on 2025-09-22 13:55:01*