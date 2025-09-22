# Deep Reinforcement Learning with Gradient Eligibility Traces

**Korean Title:** 깊이 강화 학습에서의 그래디언트 적격성 추적

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multistep Credit Assignment

## 🔗 유사한 논문
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (85.5% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (83.5% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (82.9% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks A Second-Order Optimization Perspective]] (82.7% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09087v2 Announce Type: replace-cross 
Abstract: Achieving fast and stable off-policy learning in deep reinforcement learning (RL) is challenging. Most existing methods rely on semi-gradient temporal-difference (TD) methods for their simplicity and efficiency, but are consequently susceptible to divergence. While more principled approaches like Gradient TD (GTD) methods have strong convergence guarantees, they have rarely been used in deep RL. Recent work introduced the generalized Projected Bellman Error ($\overline{\text{PBE}}$), enabling GTD methods to work efficiently with nonlinear function approximation. However, this work is limited to one-step methods, which are slow at credit assignment and require a large number of samples. In this paper, we extend the generalized $\overline{\text{PBE}}$ objective to support multistep credit assignment based on the $\lambda$-return and derive three gradient-based methods that optimize this new objective. We provide both a forward-view formulation compatible with experience replay and a backward-view formulation compatible with streaming algorithms. Finally, we evaluate the proposed algorithms and show that they outperform both PPO and StreamQ in MuJoCo and MinAtar environments, respectively. Code available at https://github.com/esraaelelimy/gtd\_algos

## 🔍 Abstract (한글 번역)

arXiv:2507.09087v2 발표 유형: 교차 교체  
초록: 심층 강화 학습(RL)에서 빠르고 안정적인 오프-정책 학습을 달성하는 것은 도전적입니다. 대부분의 기존 방법은 단순성과 효율성 때문에 반-구배 시차-차이(TD) 방법에 의존하지만, 그 결과 발산에 취약합니다. 반면에 Gradient TD(GTD) 방법과 같은 더 원칙적인 접근법은 강력한 수렴 보장을 제공하지만, 심층 RL에서는 거의 사용되지 않았습니다. 최근 연구에서는 일반화된 투영 벨만 오류($\overline{\text{PBE}}$)를 도입하여 GTD 방법이 비선형 함수 근사와 효율적으로 작동할 수 있도록 했습니다. 그러나 이 연구는 신용 할당이 느리고 많은 샘플을 필요로 하는 일단계 방법에 제한됩니다. 본 논문에서는 일반화된 $\overline{\text{PBE}}$ 목표를 $\lambda$-반환을 기반으로 한 다단계 신용 할당을 지원하도록 확장하고, 이 새로운 목표를 최적화하는 세 가지 구배 기반 방법을 도출합니다. 경험 재생과 호환되는 전방-보기 공식과 스트리밍 알고리즘과 호환되는 후방-보기 공식을 모두 제공합니다. 마지막으로 제안된 알고리즘을 평가하고, MuJoCo 및 MinAtar 환경에서 각각 PPO와 StreamQ를 능가함을 보여줍니다. 코드: https://github.com/esraaelelimy/gtd\_algos

## 📝 요약

이 논문은 심층 강화 학습에서 빠르고 안정적인 오프-정책 학습을 목표로 합니다. 기존의 방법들은 반-기울기 TD 방법에 의존하여 수렴 문제를 겪지만, GTD 방법은 수렴 보장이 강력합니다. 최근 연구에서는 비선형 함수 근사와 함께 효율적으로 작동하는 일반화된 투영 벨만 오류($\overline{\text{PBE}}$)를 도입했으나, 이는 느린 신용 할당의 단점이 있습니다. 본 연구는 $\lambda$-리턴을 기반으로 다단계 신용 할당을 지원하는 $\overline{\text{PBE}}$ 목표를 확장하고, 이를 최적화하는 세 가지 기울기 기반 방법을 제안합니다. 제안된 알고리즘은 MuJoCo와 MinAtar 환경에서 PPO와 StreamQ를 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 기존의 심층 강화 학습 방법들은 반정규화 TD 방법에 의존하여 수렴성에 취약하다.

- 2. Gradient TD (GTD) 방법은 수렴 보장이 강하지만 심층 강화 학습에서는 거의 사용되지 않았다.

- 3. 일반화된 Projected Bellman Error($\overline{\text{PBE}}$)는 비선형 함수 근사와 함께 GTD 방법을 효율적으로 사용할 수 있게 한다.

- 4. 본 연구는 $\lambda$-return을 기반으로 다단계 신용 할당을 지원하는 일반화된 $\overline{\text{PBE}}$ 목표를 확장하였다.

- 5. 제안된 알고리즘은 MuJoCo와 MinAtar 환경에서 PPO와 StreamQ를 능가하는 성능을 보였다.

---

*Generated on 2025-09-22 14:56:41*