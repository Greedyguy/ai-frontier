# Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem

**Korean Title:** 완전 탈중앙화된 협력적 다중 에이전트 강화 학습은 맥락 모델링 문제이다.

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Decentralized Cooperative Learning

## 🔗 유사한 논문
- [[2025-09-19/Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity_20250919|Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity]] (85.7% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (82.8% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (82.7% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.4% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15519v1 Announce Type: new 
Abstract: This paper studies fully decentralized cooperative multi-agent reinforcement learning, where each agent solely observes the states, its local actions, and the shared rewards. The inability to access other agents' actions often leads to non-stationarity during value function updates and relative overgeneralization during value function estimation, hindering effective cooperative policy learning. However, existing works fail to address both issues simultaneously, due to their inability to model the joint policy of other agents in a fully decentralized setting. To overcome this limitation, we propose a novel method named Dynamics-Aware Context (DAC), which formalizes the task, as locally perceived by each agent, as an Contextual Markov Decision Process, and further addresses both non-stationarity and relative overgeneralization through dynamics-aware context modeling. Specifically, DAC attributes the non-stationary local task dynamics of each agent to switches between unobserved contexts, each corresponding to a distinct joint policy. Then, DAC models the step-wise dynamics distribution using latent variables and refers to them as contexts. For each agent, DAC introduces a context-based value function to address the non-stationarity issue during value function update. For value function estimation, an optimistic marginal value is derived to promote the selection of cooperative actions, thereby addressing the relative overgeneralization issue. Experimentally, we evaluate DAC on various cooperative tasks (including matrix game, predator and prey, and SMAC), and its superior performance against multiple baselines validates its effectiveness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15519v1 발표 유형: 신규  
초록: 본 논문은 각 에이전트가 상태, 자신의 지역적 행동 및 공유 보상만을 관찰하는 완전 분산 협력 다중 에이전트 강화 학습을 연구합니다. 다른 에이전트의 행동에 접근할 수 없는 것은 종종 가치 함수 업데이트 시 비정상성을 초래하고 가치 함수 추정 시 상대적 과일반화를 초래하여 효과적인 협력 정책 학습을 방해합니다. 그러나 기존 연구들은 완전 분산 설정에서 다른 에이전트의 공동 정책을 모델링할 수 없기 때문에 두 가지 문제를 동시에 해결하지 못합니다. 이러한 한계를 극복하기 위해, 우리는 Dynamics-Aware Context (DAC)라는 새로운 방법을 제안합니다. 이는 각 에이전트가 지역적으로 인식하는 작업을 문맥적 마르코프 결정 과정으로 형식화하고, 동적 인식 문맥 모델링을 통해 비정상성과 상대적 과일반화 문제를 모두 해결합니다. 구체적으로, DAC는 각 에이전트의 비정상적인 지역 작업 동태를 관찰되지 않은 문맥 간의 전환으로 귀속시키며, 각 문맥은 독특한 공동 정책에 해당합니다. 그런 다음 DAC는 잠재 변수를 사용하여 단계별 동태 분포를 모델링하고 이를 문맥으로 지칭합니다. 각 에이전트에 대해 DAC는 가치 함수 업데이트 시 비정상성 문제를 해결하기 위해 문맥 기반 가치 함수를 도입합니다. 가치 함수 추정을 위해, 협력적 행동 선택을 촉진하기 위한 낙관적 한계 가치를 도출하여 상대적 과일반화 문제를 해결합니다. 실험적으로, 우리는 다양한 협력 작업(행렬 게임, 포식자와 먹이, SMAC 포함)에서 DAC를 평가하였으며, 여러 기준선에 대한 우수한 성능은 그 효과성을 입증합니다.

## 📝 요약

이 논문은 완전한 분산형 협력 다중 에이전트 강화 학습을 연구하며, 각 에이전트는 상태, 로컬 행동, 공유 보상만을 관찰합니다. 다른 에이전트의 행동을 알 수 없어 가치 함수 업데이트 시 비정상성과 상대적 과일반화가 발생하여 협력 정책 학습이 어려워집니다. 이를 해결하기 위해, 본 연구는 'Dynamics-Aware Context (DAC)'라는 새로운 방법을 제안합니다. DAC는 각 에이전트가 인식하는 과제를 맥락적 마르코프 결정 과정으로 공식화하고, 비정상성과 상대적 과일반화를 해결합니다. DAC는 숨겨진 맥락의 전환으로 비정상적 로컬 과제 동태를 설명하고, 잠재 변수를 사용해 단계별 동태 분포를 모델링합니다. 각 에이전트에 대해, DAC는 비정상성 문제를 해결하기 위해 맥락 기반 가치 함수를 도입하고, 협력 행동 선택을 촉진하는 낙관적 한계 가치를 도출하여 상대적 과일반화를 해결합니다. 실험 결과, DAC는 다양한 협력 과제에서 기존 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 완전한 탈중앙화 협력 다중 에이전트 강화 학습을 연구하며, 각 에이전트는 상태, 지역적 행동, 공유 보상만을 관찰합니다.

- 2. 기존 연구들은 완전한 탈중앙화 설정에서 다른 에이전트의 공동 정책을 모델링하지 못해 비정상성과 상대적 과일반화 문제를 동시에 해결하지 못합니다.

- 3. 제안된 Dynamics-Aware Context (DAC) 방법은 각 에이전트가 인지하는 과제를 맥락적 마르코프 결정 과정으로 형식화하고, 비정상성과 상대적 과일반화 문제를 동적 인식 맥락 모델링을 통해 해결합니다.

- 4. DAC는 비정상성 문제를 해결하기 위해 맥락 기반 가치 함수를 도입하고, 협력적 행동 선택을 촉진하기 위해 낙관적 한계 가치를 도출하여 상대적 과일반화 문제를 해결합니다.

- 5. 다양한 협력 과제에서 DAC의 실험적 평가 결과, 여러 기준선 대비 우수한 성능을 보여 그 효과성을 입증하였습니다.

---

*Generated on 2025-09-22 15:18:13*