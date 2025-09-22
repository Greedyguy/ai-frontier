# Automated Cyber Defense with Generalizable Graph-based Reinforcement Learning Agents

**Korean Title:** 일반화 가능한 그래프 기반 강화 학습 에이전트를 활용한 자동화된 사이버 방어

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Automated Cyber Defense

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.1% similar)
- [[2025-09-22/Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem_20250922|Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem]] (82.7% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (82.1% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (81.3% similar)
- [[2025-09-22/The Distribution Shift Problem in Transportation Networks using Reinforcement Learning and AI_20250922|The Distribution Shift Problem in Transportation Networks using Reinforcement Learning and AI]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16151v1 Announce Type: new 
Abstract: Deep reinforcement learning (RL) is emerging as a viable strategy for automated cyber defense (ACD). The traditional RL approach represents networks as a list of computers in various states of safety or threat. Unfortunately, these models are forced to overfit to specific network topologies, rendering them ineffective when faced with even small environmental perturbations. In this work, we frame ACD as a two-player context-based partially observable Markov decision problem with observations represented as attributed graphs. This approach allows our agents to reason through the lens of relational inductive bias. Agents learn how to reason about hosts interacting with other system entities in a more general manner, and their actions are understood as edits to the graph representing the environment. By introducing this bias, we will show that our agents can better reason about the states of networks and zero-shot adapt to new ones. We show that this approach outperforms the state-of-the-art by a wide margin, and makes our agents capable of defending never-before-seen networks against a wide range of adversaries in a variety of complex, and multi-agent environments.

## 🔍 Abstract (한글 번역)

arXiv:2509.16151v1 발표 유형: 신규  
초록: 심층 강화 학습(RL)은 자동화된 사이버 방어(ACD)를 위한 실현 가능한 전략으로 부상하고 있습니다. 전통적인 RL 접근법은 네트워크를 다양한 안전 또는 위협 상태에 있는 컴퓨터 목록으로 나타냅니다. 불행히도, 이러한 모델은 특정 네트워크 토폴로지에 과적합되도록 강요받아, 환경의 작은 변화에도 효과적이지 못합니다. 본 연구에서는 ACD를 속성 그래프로 표현된 관찰을 사용하는 두 플레이어 기반의 부분 관찰 마르코프 결정 문제로 설정합니다. 이 접근법은 에이전트가 관계적 귀납 편향의 관점에서 추론할 수 있게 합니다. 에이전트는 다른 시스템 엔티티와 상호작용하는 호스트에 대해 보다 일반적인 방식으로 추론하는 방법을 학습하며, 그들의 행동은 환경을 나타내는 그래프에 대한 편집으로 이해됩니다. 이러한 편향을 도입함으로써, 에이전트가 네트워크 상태에 대해 더 잘 추론하고 새로운 네트워크에 제로샷으로 적응할 수 있음을 보여줄 것입니다. 우리는 이 접근법이 최첨단 기술을 크게 능가하며, 다양한 복잡하고 다중 에이전트 환경에서 다양한 적에 대해 이전에 본 적 없는 네트워크를 방어할 수 있는 에이전트를 만들 수 있음을 보여줍니다.

## 📝 요약

이 논문은 심층 강화 학습(RL)을 자동화된 사이버 방어(ACD)에 적용하는 새로운 접근법을 제안합니다. 기존 RL 모델은 네트워크를 특정 토폴로지에 맞춰 과적합되기 쉬운 문제를 갖고 있습니다. 이를 해결하기 위해, 저자들은 ACD를 속성 그래프로 표현된 부분 관찰 마르코프 결정 문제로 재구성하였습니다. 이 방법은 관계적 귀납 편향을 활용하여 에이전트가 네트워크 상태를 더 일반화된 방식으로 이해하고, 새로운 네트워크에 즉각 적응할 수 있도록 합니다. 실험 결과, 이 접근법은 최신 기법보다 뛰어난 성능을 보이며, 다양한 복잡한 환경에서 새로운 네트워크에 대한 방어 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. 심층 강화 학습(RL)은 자동화된 사이버 방어(ACD)를 위한 유망한 전략으로 부상하고 있다.

- 2. 기존의 RL 접근 방식은 네트워크를 다양한 안전 또는 위협 상태의 컴퓨터 목록으로 표현하여 특정 네트워크 토폴로지에 과적합되는 문제를 가진다.

- 3. 본 연구에서는 ACD를 두 명의 플레이어가 참여하는 문맥 기반 부분 관찰 마르코프 결정 문제로 구성하고, 관찰을 속성 그래프로 표현하였다.

- 4. 제안된 접근 방식은 관계적 귀납 편향을 통해 에이전트가 네트워크 상태를 더 잘 추론하고 새로운 환경에 적응할 수 있도록 한다.

- 5. 본 연구의 접근 방식은 최신 기술을 크게 능가하며, 다양한 복잡하고 다중 에이전트 환경에서 새로운 네트워크를 방어할 수 있는 능력을 제공한다.

---

*Generated on 2025-09-22 15:33:57*