
# Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits

**Korean Title:** 비정상 멀티암드 밴딧을 위한 제약 피드백 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Non-Stationary Multi-Armed Bandits

## 🔗 유사한 논문
- [[Graph Feedback Bandits on Similar Arms With and Without Graph Structures]] (85.9% similar)
- [[Bellman_Optimality_of_Average-Reward_Robust_Markov_Decision_Processes_with_a_Constant_Gain_20250918|Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain]] (79.6% similar)
- [[Efficient Last-Iterate Convergence in Regret Minimization via Adaptive Reward Transformation]] (78.2% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (77.6% similar)
- [[Zero-sum turn games using Q-learning finite computation with security guarantees]] (77.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15073v1 Announce Type: new 
Abstract: Non-stationary multi-armed bandits enable agents to adapt to changing environments by incorporating mechanisms to detect and respond to shifts in reward distributions, making them well-suited for dynamic settings. However, existing approaches typically assume that reward feedback is available at every round - an assumption that overlooks many real-world scenarios where feedback is limited. In this paper, we take a significant step forward by introducing a new model of constrained feedback in non-stationary multi-armed bandits, where the availability of reward feedback is restricted. We propose the first prior-free algorithm - that is, one that does not require prior knowledge of the degree of non-stationarity - that achieves near-optimal dynamic regret in this setting. Specifically, our algorithm attains a dynamic regret of $\tilde{\mathcal{O}}({K^{1/3} V_T^{1/3} T }/{ B^{1/3}})$, where $T$ is the number of rounds, $K$ is the number of arms, $B$ is the query budget, and $V_T$ is the variation budget capturing the degree of non-stationarity.

## 🔍 Abstract (한글 번역)

arXiv:2509.15073v1 발표 유형: 신규  
초록: 비정상 다중 슬롯머신 문제는 보상 분포의 변화를 감지하고 대응하는 메커니즘을 통합하여 에이전트가 변화하는 환경에 적응할 수 있게 함으로써, 동적 환경에 적합합니다. 그러나 기존 접근 방식은 일반적으로 매 라운드마다 보상 피드백이 제공된다는 가정을 하며, 이는 피드백이 제한된 많은 실제 시나리오를 간과합니다. 본 논문에서는 비정상 다중 슬롯머신 문제에서 보상 피드백의 가용성이 제한된 새로운 제약 피드백 모델을 도입함으로써 중요한 진전을 이룹니다. 우리는 비정상성의 정도에 대한 사전 지식이 필요 없는 최초의 사전 정보 없는 알고리즘을 제안하며, 이 알고리즘은 이 설정에서 거의 최적의 동적 후회를 달성합니다. 구체적으로, 우리의 알고리즘은 $\tilde{\mathcal{O}}({K^{1/3} V_T^{1/3} T }/{ B^{1/3}})$의 동적 후회를 달성하며, 여기서 $T$는 라운드 수, $K$는 팔의 수, $B$는 쿼리 예산, $V_T$는 비정상성의 정도를 나타내는 변동 예산입니다.

## 📝 요약

이 논문은 제한된 피드백 환경에서 비정상 다중 슬롯머신 문제를 다루며, 보상 피드백이 제한된 상황에서도 적응할 수 있는 새로운 모델을 제안합니다. 기존 방법들은 매 라운드마다 보상 피드백이 제공된다고 가정하지만, 이 연구는 이러한 가정을 벗어나 실제 환경에 더 적합한 모델을 제공합니다. 저자들은 비정상성의 정도에 대한 사전 지식 없이도 근사 최적의 동적 후회를 달성할 수 있는 최초의 알고리즘을 제안하며, 이 알고리즘은 $\tilde{\mathcal{O}}({K^{1/3} V_T^{1/3} T }/{ B^{1/3}})$의 동적 후회를 달성합니다. 여기서 $T$는 라운드 수, $K$는 슬롯머신의 수, $B$는 쿼리 예산, $V_T$는 비정상성의 정도를 나타내는 변동 예산입니다.

## 🎯 주요 포인트

- 1. 비정상적인 멀티암드 밴딧 문제에서 보상 피드백이 제한된 새로운 모델을 제안합니다.

- 2. 제안된 알고리즘은 비정상성의 정도에 대한 사전 지식 없이도 거의 최적의 동적 후회를 달성합니다.

- 3. 알고리즘의 동적 후회는 $\tilde{\mathcal{O}}({K^{1/3} V_T^{1/3} T }/{ B^{1/3}})$로 표현되며, 여기서 $T$는 라운드 수, $K$는 팔의 수, $B$는 쿼리 예산, $V_T$는 비정상성을 나타내는 변동 예산입니다.

- 4. 이 연구는 보상 피드백이 제한된 상황에서도 비정상적인 환경에 적응할 수 있는 새로운 접근법을 제공합니다.

---

*Generated on 2025-09-19 15:30:15*