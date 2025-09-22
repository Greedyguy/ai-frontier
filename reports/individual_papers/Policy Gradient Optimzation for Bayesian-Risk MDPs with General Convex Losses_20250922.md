# Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses

**Korean Title:** 베이지안 위험 MDP에서 일반적인 볼록 손실을 고려한 정책 경사 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Episodic Setting Extension

## 🔗 유사한 논문
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (85.7% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (81.6% similar)
- [[2025-09-18/Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain_20250918|Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain]] (81.5% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (81.2% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15509v1 Announce Type: new 
Abstract: Motivated by many application problems, we consider Markov decision processes (MDPs) with a general loss function and unknown parameters. To mitigate the epistemic uncertainty associated with unknown parameters, we take a Bayesian approach to estimate the parameters from data and impose a coherent risk functional (with respect to the Bayesian posterior distribution) on the loss. Since this formulation usually does not satisfy the interchangeability principle, it does not admit Bellman equations and cannot be solved by approaches based on dynamic programming. Therefore, We propose a policy gradient optimization method, leveraging the dual representation of coherent risk measures and extending the envelope theorem to continuous cases. We then show the stationary analysis of the algorithm with a convergence rate of $O(T^{-1/2}+r^{-1/2})$, where $T$ is the number of policy gradient iterations and $r$ is the sample size of the gradient estimator. We further extend our algorithm to an episodic setting, and establish the global convergence of the extended algorithm and provide bounds on the number of iterations needed to achieve an error bound $O(\epsilon)$ in each episode.

## 🔍 Abstract (한글 번역)

arXiv:2509.15509v1 발표 유형: 신규  
초록: 다양한 응용 문제에 동기 부여되어, 일반적인 손실 함수와 미지의 매개변수를 가진 마르코프 결정 과정(MDPs)을 고려합니다. 미지의 매개변수와 관련된 인식론적 불확실성을 완화하기 위해, 우리는 데이터를 통해 매개변수를 추정하고 손실에 대해 베이지안 사후 분포에 대한 일관된 위험 함수(coherent risk functional)를 부과하는 베이지안 접근 방식을 취합니다. 이 형식은 일반적으로 교환 가능성 원칙을 충족하지 않으므로, 벨만 방정식을 허용하지 않으며 동적 프로그래밍 기반 접근법으로 해결할 수 없습니다. 따라서 우리는 일관된 위험 측정의 이중 표현을 활용하고 연속적인 경우에 대해 봉투 정리를 확장하여 정책 경사 최적화 방법을 제안합니다. 그런 다음, 우리는 알고리즘의 정적 분석을 보여주며, 정책 경사 반복 횟수 $T$와 기울기 추정기의 샘플 크기 $r$에 대해 수렴 속도가 $O(T^{-1/2}+r^{-1/2})$임을 증명합니다. 또한, 에피소드 설정으로 알고리즘을 확장하고, 확장된 알고리즘의 전역 수렴을 확립하며 각 에피소드에서 오류 경계 $O(\epsilon)$을 달성하기 위해 필요한 반복 횟수에 대한 경계를 제공합니다.

## 📝 요약

이 논문은 일반적인 손실 함수와 미지의 매개변수를 가진 마르코프 결정 과정(MDP)을 다룹니다. 미지의 매개변수로 인한 불확실성을 줄이기 위해 베이지안 접근법을 사용하여 데이터를 통해 매개변수를 추정하고, 손실에 대해 베이지안 사후 분포에 기반한 일관된 위험 함수적을 적용합니다. 이 접근법은 벨만 방정식을 만족하지 않으므로 동적 프로그래밍 기반 방법으로 해결할 수 없습니다. 따라서, 저자들은 정책 경사 최적화 방법을 제안하며, 일관된 위험 측정의 이중 표현을 활용하고 연속적인 경우로 외연 정리를 확장합니다. 알고리즘의 수렴 속도는 $O(T^{-1/2}+r^{-1/2})$이며, 여기서 $T$는 정책 경사 반복 횟수, $r$는 경사 추정기의 샘플 크기입니다. 또한, 알고리즘을 에피소드 설정으로 확장하여 글로벌 수렴성을 입증하고, 각 에피소드에서 $O(\epsilon)$의 오류 경계를 달성하기 위한 반복 횟수에 대한 경계를 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 일반적인 손실 함수와 미지의 매개변수를 가진 마르코프 결정 과정(MDPs)을 다루며, 베이지안 접근법을 통해 매개변수를 추정하고 손실에 대한 일관된 리스크 함수적을 적용합니다.

- 2. 제안된 문제는 교환 가능성 원칙을 만족하지 않아 벨만 방정식을 사용할 수 없으며, 동적 프로그래밍 기반 접근법으로 해결할 수 없습니다.

- 3. 정책 경사 최적화 방법을 제안하며, 일관된 리스크 측정의 이중 표현을 활용하고 연속적인 경우로 외피 정리를 확장합니다.

- 4. 제안된 알고리즘의 수렴 속도는 $O(T^{-1/2}+r^{-1/2})$이며, 여기서 $T$는 정책 경사 반복 횟수, $r$은 그래디언트 추정기의 샘플 크기입니다.

- 5. 알고리즘을 에피소드 설정으로 확장하여 전역 수렴성을 확립하고, 각 에피소드에서 오류 경계 $O(\epsilon)$을 달성하기 위한 반복 횟수에 대한 경계를 제공합니다.

---

*Generated on 2025-09-22 15:17:08*