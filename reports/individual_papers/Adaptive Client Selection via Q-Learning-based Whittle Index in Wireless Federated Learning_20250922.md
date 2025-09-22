# Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning

**Korean Title:** 적응형 클라이언트 선택을 위한 Q-러닝 기반 휘틀 지수 적용 무선 연합 학습

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Adaptive Client Selection|Adaptive Client Selection]] [[keywords/specific/Restless Multi-armed Bandit|Restless Multi-armed Bandit]] [[keywords/specific/Q-learning|Q-learning]] [[keywords/broad/Federated Learning|Federated Learning]] [[keywords/unique/Whittle Index Learning in Federated Q-learning|Whittle Index Learning in Federated Q-learning]] [[categories/cs.LG|cs.LG]] [[2025-09-17/Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning_20250917|Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning]] (99.0% similar) [[2025-09-19/Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (81.8% similar) [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Restless Multi-armed Bandit, Q-learning
**🔬 Broad Technical**: Federated Learning, Wireless Communication
**⭐ Unique Technical**: Whittle Index Learning in Federated Q-learning
## 🔗 유사한 논문
- [[2025-09-17/Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning_20250917|Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning]] (99.0% similar)
- [[2025-09-19/Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (81.8% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (79.7% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (78.9% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (78.4% similar)


**ArXiv ID**: [2509.13933](https://arxiv.org/abs/2509.13933)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13933.pdf)


**ArXiv ID**: [2509.13933](https://arxiv.org/abs/2509.13933)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13933.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Client Selection
**🔗 Specific Connectable**: Restless Multi-armed Bandit, Q-learning
**⭐ Unique Technical**: Whittle Index Learning in Federated Q-learning
**🔬 Broad Technical**: Federated Learning

## 🏷️ 추출된 키워드



`Federated Learning` • 

`Restless Multi-armed Bandit` • 

`Q-Learning` • 

`Whittle Index Learning in Federated Q-learning` • 

`Adaptive Client Selection`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13933v2 Announce Type: replace 
Abstract: We consider the client selection problem in wireless Federated Learning (FL), with the objective of reducing the total required time to achieve a certain level of learning accuracy. Since the server cannot observe the clients' dynamic states that can change their computation and communication efficiency, we formulate client selection as a restless multi-armed bandit problem. We propose a scalable and efficient approach called the Whittle Index Learning in Federated Q-learning (WILF-Q), which uses Q-learning to adaptively learn and update an approximated Whittle index associated with each client, and then selects the clients with the highest indices. Compared to existing approaches, WILF-Q does not require explicit knowledge of client state transitions or data distributions, making it well-suited for deployment in practical FL settings. Experiment results demonstrate that WILF-Q significantly outperforms existing baseline policies in terms of learning efficiency, providing a robust and efficient approach to client selection in wireless FL.

## 🔍 Abstract (한글 번역)

arXiv:2509.13933v2 발표 유형: 교체  
초록: 우리는 무선 연합 학습(FL)에서 클라이언트 선택 문제를 고려하며, 특정 수준의 학습 정확도를 달성하기 위한 총 소요 시간을 줄이는 것을 목표로 합니다. 서버는 클라이언트의 계산 및 통신 효율성을 변화시킬 수 있는 동적 상태를 관찰할 수 없기 때문에, 우리는 클라이언트 선택을 불안정한 다중 무장 강도 문제로 공식화합니다. 우리는 연합 Q-학습에서 휘틀 지수 학습(WILF-Q)이라는 확장 가능하고 효율적인 접근 방식을 제안합니다. 이 접근 방식은 Q-학습을 사용하여 각 클라이언트와 관련된 근사 휘틀 지수를 적응적으로 학습하고 업데이트하며, 가장 높은 지수를 가진 클라이언트를 선택합니다. 기존 접근 방식과 비교할 때, WILF-Q는 클라이언트 상태 전환이나 데이터 분포에 대한 명시적 지식이 필요하지 않으므로 실제 FL 환경에 배포하기에 적합합니다. 실험 결과에 따르면, WILF-Q는 학습 효율성 측면에서 기존의 기준 정책을 크게 능가하여 무선 FL에서 클라이언트 선택에 대한 견고하고 효율적인 접근 방식을 제공합니다.

## 📝 요약

이 논문은 무선 연합 학습(FL)에서 클라이언트 선택 문제를 다룹니다. 목표는 특정 학습 정확도 수준을 달성하기 위한 총 시간을 줄이는 것입니다. 서버는 클라이언트의 동적 상태를 관찰할 수 없기 때문에, 클라이언트 선택을 '휴식 없는 다중 슬롯 머신 문제'로 공식화했습니다. 이를 해결하기 위해, Q-러닝을 활용하여 각 클라이언트에 대한 근사 Whittle 지수를 적응적으로 학습하고 업데이트하는 WILF-Q라는 방법론을 제안합니다. WILF-Q는 클라이언트 상태 전이나 데이터 분포에 대한 명시적 지식이 필요하지 않아 실용적인 FL 환경에 적합합니다. 실험 결과, WILF-Q는 기존의 기준 정책들보다 학습 효율성 면에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트


- 1. 무선 연합 학습(FL)에서 클라이언트 선택 문제를 해결하기 위해 총 학습 시간을 줄이는 것을 목표로 한다.

- 2. 클라이언트 선택을 restless multi-armed bandit 문제로 공식화하여 클라이언트의 동적 상태를 관찰할 수 없는 문제를 해결한다.

- 3. WILF-Q는 Q-learning을 사용하여 각 클라이언트에 대한 근사 Whittle 지수를 학습하고 업데이트하여 가장 높은 지수를 가진 클라이언트를 선택한다.

- 4. WILF-Q는 클라이언트 상태 전환이나 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에 적합하다.

- 5. 실험 결과, WILF-Q는 기존의 기준 정책보다 학습 효율성 면에서 뛰어난 성능을 보여준다.


---

*Generated on 2025-09-22 16:04:09*