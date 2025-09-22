# Learning to Optimize Capacity Planning in Semiconductor Manufacturing

**Korean Title:** 반도체 제조에서 용량 계획 최적화를 학습하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Machine-level Capacity Planning

## 🔗 유사한 논문
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (80.6% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (79.7% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.7% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.6% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15767v1 Announce Type: new 
Abstract: In manufacturing, capacity planning is the process of allocating production resources in accordance with variable demand. The current industry practice in semiconductor manufacturing typically applies heuristic rules to prioritize actions, such as future change lists that account for incoming machine and recipe dedications. However, while offering interpretability, heuristics cannot easily account for the complex interactions along the process flow that can gradually lead to the formation of bottlenecks. Here, we present a neural network-based model for capacity planning on the level of individual machines, trained using deep reinforcement learning. By representing the policy using a heterogeneous graph neural network, the model directly captures the diverse relationships among machines and processing steps, allowing for proactive decision-making. We describe several measures taken to achieve sufficient scalability to tackle the vast space of possible machine-level actions.
  Our evaluation results cover Intel's small-scale Minifab model and preliminary experiments using the popular SMT2020 testbed. In the largest tested scenario, our trained policy increases throughput and decreases cycle time by about 1.8% each.

## 🔍 Abstract (한글 번역)

arXiv:2509.15767v1 발표 유형: 새로운 
초록: 제조업에서 용량 계획은 가변적인 수요에 따라 생산 자원을 할당하는 과정입니다. 반도체 제조에서 현재 산업 관행은 일반적으로 휴리스틱 규칙을 적용하여, 예를 들어 기계 및 레시피 전용을 고려한 향후 변경 목록과 같은 행동을 우선시합니다. 그러나 해석 가능성을 제공하는 반면, 휴리스틱은 프로세스 흐름을 따라 점진적으로 병목 현상을 형성할 수 있는 복잡한 상호작용을 쉽게 고려할 수 없습니다. 여기에서는 개별 기계 수준에서의 용량 계획을 위한 신경망 기반 모델을 제시하며, 심층 강화 학습을 사용하여 훈련되었습니다. 이 모델은 이질적인 그래프 신경망을 사용하여 정책을 표현함으로써 기계와 처리 단계 간의 다양한 관계를 직접 포착하여 선제적인 의사 결정을 가능하게 합니다. 우리는 가능한 기계 수준의 행동 공간을 다루기 위한 충분한 확장성을 달성하기 위해 취한 여러 조치를 설명합니다.
우리의 평가 결과는 Intel의 소규모 Minifab 모델과 인기 있는 SMT2020 테스트베드를 사용한 예비 실험을 포함합니다. 가장 큰 테스트 시나리오에서, 훈련된 정책은 처리량을 약 1.8% 증가시키고 주기 시간을 약 1.8% 감소시킵니다.

## 📝 요약

이 논문은 반도체 제조에서 개별 기계 수준의 용량 계획을 위한 신경망 기반 모델을 제안합니다. 기존의 휴리스틱 방법은 해석 가능성을 제공하지만 복잡한 상호작용을 충분히 반영하지 못해 병목 현상을 초래할 수 있습니다. 본 연구에서는 이 문제를 해결하기 위해 딥 강화 학습을 활용하여 이종 그래프 신경망으로 정책을 표현함으로써 기계와 처리 단계 간의 다양한 관계를 직접 포착하고, 선제적인 의사 결정을 가능하게 합니다. 제안된 모델은 Intel의 소규모 Minifab 모델과 SMT2020 테스트베드를 통해 평가되었으며, 최대 시나리오에서 처리량과 사이클 시간을 각각 약 1.8% 향상시켰습니다.

## 🎯 주요 포인트

- 1. 반도체 제조에서 용량 계획은 변동하는 수요에 맞춰 생산 자원을 할당하는 과정이다.

- 2. 기존의 산업 관행은 휴리스틱 규칙을 적용하여 기계 및 레시피 전용을 고려한 우선순위 행동을 결정한다.

- 3. 본 연구는 개별 기계 수준에서의 용량 계획을 위한 신경망 기반 모델을 제안하며, 심층 강화 학습을 통해 훈련되었다.

- 4. 이 모델은 이질적인 그래프 신경망을 사용하여 기계와 처리 단계 간의 다양한 관계를 직접 포착한다.

- 5. 제안된 정책은 인텔의 소규모 Minifab 모델과 SMT2020 테스트베드에서 평가되었으며, 처리량과 사이클 시간을 각각 약 1.8% 증가 및 감소시켰다.

---

*Generated on 2025-09-22 15:23:46*