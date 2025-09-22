# Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning

**Korean Title:** 대규모 다중 에이전트 강화 학습에서의 취약 에이전트 식별

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vulnerable Agent Identification

## 🔗 유사한 논문
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (84.8% similar)
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (84.8% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.9% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (82.0% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (81.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15103v2 Announce Type: replace-cross 
Abstract: Partial agent failure becomes inevitable when systems scale up, making it crucial to identify the subset of agents whose compromise would most severely degrade overall performance. In this paper, we study this Vulnerable Agent Identification (VAI) problem in large-scale multi-agent reinforcement learning (MARL). We frame VAI as a Hierarchical Adversarial Decentralized Mean Field Control (HAD-MFC), where the upper level involves an NP-hard combinatorial task of selecting the most vulnerable agents, and the lower level learns worst-case adversarial policies for these agents using mean-field MARL. The two problems are coupled together, making HAD-MFC difficult to solve. To solve this, we first decouple the hierarchical process by Fenchel-Rockafellar transform, resulting a regularized mean-field Bellman operator for upper level that enables independent learning at each level, thus reducing computational complexity. We then reformulate the upper-level combinatorial problem as a MDP with dense rewards from our regularized mean-field Bellman operator, enabling us to sequentially identify the most vulnerable agents by greedy and RL algorithms. This decomposition provably preserves the optimal solution of the original HAD-MFC. Experiments show our method effectively identifies more vulnerable agents in large-scale MARL and the rule-based system, fooling system into worse failures, and learns a value function that reveals the vulnerability of each agent.

## 🔍 Abstract (한글 번역)

arXiv:2509.15103v2 발표 유형: 교체-크로스  
초록: 시스템이 확장됨에 따라 부분적인 에이전트 실패는 불가피해지며, 전체 성능을 가장 심각하게 저하시키는 에이전트의 하위 집합을 식별하는 것이 중요해집니다. 본 논문에서는 대규모 다중 에이전트 강화 학습(MARL)에서 이 취약 에이전트 식별(VAI) 문제를 연구합니다. 우리는 VAI를 계층적 적대적 분산 평균장 제어(HAD-MFC)로 구성하며, 상위 수준에서는 가장 취약한 에이전트를 선택하는 NP-난해한 조합 문제를 포함하고, 하위 수준에서는 평균장 MARL을 사용하여 이러한 에이전트에 대한 최악의 경우 적대적 정책을 학습합니다. 이 두 문제는 서로 결합되어 있어 HAD-MFC를 해결하기 어렵게 만듭니다. 이를 해결하기 위해, 우리는 먼저 Fenchel-Rockafellar 변환을 통해 계층적 프로세스를 분리하여, 상위 수준에서 독립적인 학습을 가능하게 하는 정규화된 평균장 벨만 연산자를 도출하여 계산 복잡성을 줄입니다. 그런 다음, 상위 수준의 조합 문제를 정규화된 평균장 벨만 연산자로부터의 밀집 보상을 가진 MDP로 재구성하여, 탐욕적 및 RL 알고리즘을 통해 가장 취약한 에이전트를 순차적으로 식별할 수 있게 합니다. 이 분해는 원래 HAD-MFC의 최적 솔루션을 보존함을 증명합니다. 실험 결과, 우리의 방법은 대규모 MARL 및 규칙 기반 시스템에서 더 많은 취약 에이전트를 효과적으로 식별하여 시스템을 더 심각한 실패로 유도하고, 각 에이전트의 취약성을 드러내는 가치 함수를 학습함을 보여줍니다.

## 📝 요약

이 논문은 대규모 다중 에이전트 강화 학습(MARL)에서 시스템 성능 저하를 초래할 수 있는 취약 에이전트를 식별하는 문제를 다룹니다. 이를 위해 계층적 적대적 분산 평균장 제어(HAD-MFC)라는 프레임워크를 제안합니다. 상위 단계에서는 NP-난해한 조합 최적화 문제를 해결하여 가장 취약한 에이전트를 선택하고, 하위 단계에서는 평균장 MARL을 통해 최악의 경우에 대한 적대적 정책을 학습합니다. 이 두 문제를 분리하기 위해 Fenchel-Rockafellar 변환을 사용하여 각 단계에서 독립적인 학습이 가능하도록 하여 계산 복잡성을 줄였습니다. 상위 단계의 문제를 밀집 보상을 갖는 MDP로 재구성하여 탐욕적 알고리즘과 강화 학습을 통해 취약 에이전트를 식별합니다. 실험 결과, 제안된 방법이 대규모 MARL에서 더 많은 취약 에이전트를 효과적으로 식별하고, 시스템의 취약성을 드러내는 가치 함수를 학습함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대규모 시스템에서 부분적인 에이전트 실패는 불가피하며, 전체 성능을 가장 심각하게 저하시키는 에이전트를 식별하는 것이 중요하다.

- 2. 취약 에이전트 식별 문제(VAI)를 대규모 다중 에이전트 강화 학습(MARL)에서 연구하고, 이를 계층적 적대적 분산 평균장 제어(HAD-MFC)로 구성하였다.

- 3. Fenchel-Rockafellar 변환을 사용하여 계층적 과정을 분리하고, 각 수준에서 독립적인 학습을 가능하게 하여 계산 복잡성을 줄였다.

- 4. 상위 수준의 조합 문제를 MDP로 재구성하여, 탐욕적 및 강화 학습 알고리즘을 통해 가장 취약한 에이전트를 순차적으로 식별할 수 있게 하였다.

- 5. 실험 결과, 제안된 방법이 대규모 MARL 및 규칙 기반 시스템에서 더 많은 취약 에이전트를 효과적으로 식별하고, 각 에이전트의 취약성을 드러내는 가치 함수를 학습함을 보여준다.

---

*Generated on 2025-09-22 15:08:24*