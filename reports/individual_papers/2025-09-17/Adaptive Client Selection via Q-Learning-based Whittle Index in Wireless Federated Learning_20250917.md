# Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning

**Korean Title:** 무선 연합 학습에서 Q-러닝 기반 Whittle 지수를 통한 적응형 클라이언트 선택

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Qiyue Li|Qiyue Li]] [[authors/Yingxin Liu|Yingxin Liu]] [[authors/Hang Qi|Hang Qi]] [[authors/Jieping Luo|Jieping Luo]] [[authors/Zhizhang Liu|Zhizhang Liu]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Restless Multi-armed Bandit

## 🔗 유사한 논문
- [[Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (80.8% similar)
- [[FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (78.7% similar)
- [[Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (77.7% similar)
- [[Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (77.5% similar)
- [[Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (77.4% similar)

## 📋 저자 정보

**Authors:** Qiyue Li, Yingxin Liu, Hang Qi, Jieping Luo, Zhizhang Liu, Jingjin Wu

## 📄 Abstract (원문)

We consider the client selection problem in wireless Federated Learning (FL),
with the objective of reducing the total required time to achieve a certain
level of learning accuracy. Since the server cannot observe the clients'
dynamic states that can change their computation and communication efficiency,
we formulate client selection as a restless multi-armed bandit problem. We
propose a scalable and efficient approach called the Whittle Index Learning in
Federated Q-learning (WILF-Q), which uses Q-learning to adaptively learn and
update an approximated Whittle index associated with each client, and then
selects the clients with the highest indices. Compared to existing approaches,
WILF-Q does not require explicit knowledge of client state transitions or data
distributions, making it well-suited for deployment in practical FL settings.
Experiment results demonstrate that WILF-Q significantly outperforms existing
baseline policies in terms of learning efficiency, providing a robust and
efficient approach to client selection in wireless FL.

## 🔍 Abstract (한글 번역)

무선 연합 학습(FL)에서 클라이언트 선택 문제를 고려하며, 특정 학습 정확도 수준을 달성하기 위한 총 소요 시간을 줄이는 것을 목표로 합니다. 서버는 클라이언트의 계산 및 통신 효율성을 변화시킬 수 있는 동적 상태를 관찰할 수 없기 때문에, 우리는 클라이언트 선택을 휴식 없는 다중 슬롯 밴디트 문제로 공식화합니다. 우리는 연합 Q-학습에서 휘틀 지수 학습(WILF-Q)이라는 확장 가능하고 효율적인 접근 방식을 제안합니다. 이 방법은 Q-학습을 사용하여 각 클라이언트와 관련된 근사 휘틀 지수를 적응적으로 학습하고 업데이트하며, 가장 높은 지수를 가진 클라이언트를 선택합니다. 기존 접근 방식과 비교하여, WILF-Q는 클라이언트 상태 전이 또는 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에 배포하기에 적합합니다. 실험 결과는 WILF-Q가 학습 효율성 측면에서 기존의 기준 정책을 크게 능가하며, 무선 FL에서 클라이언트 선택에 있어 강력하고 효율적인 접근 방식을 제공함을 보여줍니다.

## 📝 요약

이 논문은 무선 연합 학습(FL)에서 클라이언트 선택 문제를 다루며, 목표는 특정 학습 정확도에 도달하는 데 필요한 총 시간을 줄이는 것입니다. 서버가 클라이언트의 동적 상태를 관찰할 수 없기 때문에, 클라이언트 선택 문제를 지속적 멀티암드 밴딧 문제로 공식화했습니다. 이를 해결하기 위해 제안된 WILF-Q(Whittle Index Learning in Federated Q-learning)는 Q-러닝을 사용하여 각 클라이언트와 관련된 Whittle 지수를 적응적으로 학습하고 업데이트하며, 가장 높은 지수를 가진 클라이언트를 선택합니다. WILF-Q는 클라이언트 상태 전이나 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에 적합합니다. 실험 결과, WILF-Q는 기존의 기준 정책들보다 학습 효율성 면에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 무선 연합 학습(FL)에서 클라이언트 선택 문제를 학습 정확도를 일정 수준으로 달성하는 데 필요한 총 시간을 줄이는 목표로 고려합니다.

- 2. 클라이언트의 동적 상태를 서버가 관찰할 수 없기 때문에 클라이언트 선택 문제를 무정지 다중 슬롯 밴딧 문제로 공식화합니다.

- 3. WILF-Q는 Q-러닝을 사용하여 각 클라이언트와 관련된 근사 Whittle 지수를 적응적으로 학습하고 업데이트하여 가장 높은 지수를 가진 클라이언트를 선택합니다.

- 4. WILF-Q는 클라이언트 상태 전이 또는 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에 적합합니다.

- 5. 실험 결과 WILF-Q는 학습 효율성 측면에서 기존의 기준 정책을 크게 능가하여 무선 FL에서 클라이언트 선택에 대한 견고하고 효율적인 접근 방식을 제공합니다.

---

*Generated on 2025-09-20 09:23:12*