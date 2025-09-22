# Dynamic Policy Fusion for User Alignment Without Re-Interaction

**Korean Title:** 사용자 재상호작용 없이 사용자 정렬을 위한 동적 정책 융합

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Zero-shot Alignment

## 🔗 유사한 논문
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (83.4% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (82.5% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (81.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.7% similar)
- [[2025-09-19/Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.20016v4 Announce Type: replace 
Abstract: Deep reinforcement learning (RL) policies, although optimal in terms of task rewards, may not align with the personal preferences of human users. To ensure this alignment, a naive solution would be to retrain the agent using a reward function that encodes the user's specific preferences. However, such a reward function is typically not readily available, and as such, retraining the agent from scratch can be prohibitively expensive. We propose a more practical approach - to adapt the already trained policy to user-specific needs with the help of human feedback. To this end, we infer the user's intent through trajectory-level feedback and combine it with the trained task policy via a theoretically grounded dynamic policy fusion approach. As our approach collects human feedback on the very same trajectories used to learn the task policy, it does not require any additional interactions with the environment, making it a zero-shot approach. We empirically demonstrate in a number of environments that our proposed dynamic policy fusion approach consistently achieves the intended task while simultaneously adhering to user-specific needs.

## 🔍 Abstract (한글 번역)

arXiv:2409.20016v4 발표 유형: 교체  
초록: 심층 강화 학습(RL) 정책은 과제 보상 측면에서 최적일지라도 인간 사용자의 개인적 선호와 일치하지 않을 수 있습니다. 이러한 일치를 보장하기 위한 단순한 해결책은 사용자의 특정 선호를 암호화한 보상 함수를 사용하여 에이전트를 재훈련하는 것입니다. 그러나 이러한 보상 함수는 일반적으로 쉽게 구할 수 없으며, 따라서 에이전트를 처음부터 재훈련하는 것은 비용이 많이 들 수 있습니다. 우리는 이미 훈련된 정책을 인간의 피드백을 통해 사용자 특정 요구에 맞게 조정하는 보다 실용적인 접근 방식을 제안합니다. 이를 위해 우리는 궤적 수준의 피드백을 통해 사용자의 의도를 추론하고, 이를 이론적으로 기반을 둔 동적 정책 융합 접근 방식을 통해 훈련된 과제 정책과 결합합니다. 우리의 접근 방식은 과제 정책을 학습하는 데 사용된 동일한 궤적에 대한 인간의 피드백을 수집하므로 환경과의 추가적인 상호작용이 필요하지 않으며, 이는 제로샷 접근 방식입니다. 우리는 여러 환경에서 제안된 동적 정책 융합 접근 방식이 사용자 특정 요구를 충족하면서 의도된 과제를 일관되게 달성함을 실증적으로 입증합니다.

## 📝 요약

이 논문은 심층 강화 학습(RL) 정책이 사용자 개인의 선호와 일치하지 않을 수 있는 문제를 다룹니다. 기존의 정책을 사용자 요구에 맞게 조정하기 위해 사용자 피드백을 활용하는 방법을 제안합니다. 사용자 의도를 경로 수준의 피드백을 통해 추론하고, 이를 이론적으로 기반한 동적 정책 융합 방법으로 기존 학습된 정책과 결합합니다. 이 접근법은 환경과의 추가 상호작용 없이 사용자 피드백을 수집하여, 제로샷 방식으로 사용자 요구를 반영합니다. 여러 환경에서 실험한 결과, 제안된 방법은 사용자 요구를 충족하면서도 과제를 성공적으로 수행함을 입증했습니다.

## 🎯 주요 포인트

- 1. 심층 강화 학습 정책은 사용자 개인의 선호도와 항상 일치하지 않을 수 있다.

- 2. 사용자 선호도를 반영하기 위해 기존 정책을 사용자 요구에 맞게 인간의 피드백을 활용하여 적응시키는 방법을 제안한다.

- 3. 제안된 방법은 경로 수준의 피드백을 통해 사용자의 의도를 추론하고, 이를 학습된 정책과 이론적으로 결합한다.

- 4. 이 접근법은 환경과의 추가 상호작용 없이 동일한 경로에서 피드백을 수집하여 제로샷 방식으로 작동한다.

- 5. 다양한 환경에서 제안된 동적 정책 융합 접근법이 사용자 요구를 충족하면서도 의도된 작업을 일관되게 수행함을 실증적으로 입증하였다.

---

*Generated on 2025-09-22 14:28:29*