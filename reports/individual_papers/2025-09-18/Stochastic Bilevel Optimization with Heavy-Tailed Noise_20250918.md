# Stochastic Bilevel Optimization with Heavy-Tailed Noise

**Korean Title:** 확률적 이층 최적화와 두꺼운 꼬리 잡음

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Zhuanghua Liu|Zhuanghua Liu]] [[authors/Luo Luo|Luo Luo]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Nonconvex Strongly Concave Minimax Optimization

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (83.0% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (81.5% similar)
- [[Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (81.1% similar)
- [[Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (80.7% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (80.6% similar)

## 📋 저자 정보

**Authors:** Zhuanghua Liu, Luo Luo

## 📄 Abstract (원문)

This paper considers the smooth bilevel optimization in which the lower-level
problem is strongly convex and the upper-level problem is possibly nonconvex.
We focus on the stochastic setting that the algorithm can access the unbiased
stochastic gradient evaluation with heavy-tailed noise, which is prevalent in
many machine learning applications such as training large language models and
reinforcement learning. We propose a nested-loop normalized stochastic bilevel
approximation (N$^2$SBA) for finding an $\epsilon$-stationary point with the
stochastic first-order oracle (SFO) complexity of
$\tilde{\mathcal{O}}\big(\kappa^{\frac{7p-3}{p-1}} \sigma^{\frac{p}{p-1}}
\epsilon^{-\frac{4 p - 2}{p-1}}\big)$, where $\kappa$ is the condition number,
$p\in(1,2]$ is the order of central moment for the noise, and $\sigma$ is the
noise level. Furthermore, we specialize our idea to solve the
nonconvex-strongly-concave minimax optimization problem, achieving an
$\epsilon$-stationary point with the SFO complexity of $\tilde{\mathcal
O}\big(\kappa^{\frac{2p-1}{p-1}} \sigma^{\frac{p}{p-1}}
\epsilon^{-\frac{3p-2}{p-1}}\big)$. All above upper bounds match the best-known
results under the special case of the bounded variance setting, i.e., $p=2$.

## 🔍 Abstract (한글 번역)

이 논문은 하위 수준 문제가 강하게 볼록하고 상위 수준 문제가 비볼록일 수 있는 매끄러운 이수준 최적화를 고려합니다. 우리는 알고리즘이 대형 언어 모델 학습 및 강화 학습과 같은 많은 기계 학습 응용에서 일반적인 무거운 꼬리 잡음을 가진 편향되지 않은 확률적 기울기 평가에 접근할 수 있는 확률적 설정에 중점을 둡니다. 우리는 중첩 루프 정규화 확률적 이수준 근사(N$^2$SBA)를 제안하여 확률적 일차 오라클(SFO) 복잡도가 $\tilde{\mathcal{O}}\big(\kappa^{\frac{7p-3}{p-1}} \sigma^{\frac{p}{p-1}} \epsilon^{-\frac{4 p - 2}{p-1}}\big)$인 $\epsilon$-정류점($\epsilon$-stationary point)을 찾습니다. 여기서 $\kappa$는 조건 수이고, $p\in(1,2]$는 잡음의 중심 모멘트의 차수이며, $\sigma$는 잡음 수준입니다. 더욱이, 우리는 우리의 아이디어를 비볼록-강하게 오목한 미니맥스 최적화 문제를 해결하는 데 특화하여, SFO 복잡도가 $\tilde{\mathcal O}\big(\kappa^{\frac{2p-1}{p-1}} \sigma^{\frac{p}{p-1}} \epsilon^{-\frac{3p-2}{p-1}}\big)$인 $\epsilon$-정류점을 달성합니다. 위의 모든 상한은 제한된 분산 설정, 즉 $p=2$의 특수한 경우에서 가장 잘 알려진 결과와 일치합니다.

## 📝 요약

이 논문은 하위 문제가 강하게 볼록하고 상위 문제가 비볼록일 수 있는 매끄러운 이수준 최적화 문제를 다룹니다. 특히, 대규모 언어 모델 훈련 및 강화 학습과 같은 많은 기계 학습 응용에서 흔히 발생하는 무거운 꼬리 잡음이 있는 편향되지 않은 확률적 기울기 평가에 접근할 수 있는 확률적 설정에 초점을 맞춥니다. 저자들은 $\epsilon$-정지점을 찾기 위한 중첩 루프 정규화 확률적 이수준 근사(N$^2$SBA) 알고리즘을 제안하며, 이는 확률적 일차 오라클(SFO) 복잡도가 $\tilde{\mathcal{O}}\big(\kappa^{\frac{7p-3}{p-1}} \sigma^{\frac{p}{p-1}} \epsilon^{-\frac{4 p - 2}{p-1}}\big)$입니다. 또한, 비볼록-강하게 오목한 미니맥스 최적화 문제에 이 아이디어를 적용하여 $\epsilon$-정지점을 SFO 복잡도 $\tilde{\mathcal O}\big(\kappa^{\frac{2p-1}{p-1}} \sigma^{\frac{p}{p-1}} \epsilon^{-\frac{3p-2}{p-1}}\big)$로 달성합니다. 이는 제한된 분산 설정($p=2$)에서 알려진 최상의 결과와 일치합니다.

## 🎯 주요 포인트

- 1. 본 논문은 하위 문제가 강하게 볼록하고 상위 문제가 비볼록일 수 있는 매끄러운 이수준 최적화를 다룹니다.

- 2. 제안된 알고리즘은 중첩 루프 정규화 확률적 이수준 근사(N$^2$SBA)로, $\epsilon$-정류점 찾기에 사용됩니다.

- 3. 제안된 방법은 확률적 일차 오라클(SFO) 복잡도가 $\tilde{\mathcal{O}}\big(\kappa^{\frac{7p-3}{p-1}} \sigma^{\frac{p}{p-1}} \epsilon^{-\frac{4 p - 2}{p-1}}\big)$로 평가됩니다.

- 4. 비볼록-강하게 오목한 미니맥스 최적화 문제에 대해 제안된 방법을 특화하여 $\epsilon$-정류점을 달성합니다.

- 5. 제안된 방법의 상한은 제한된 분산 설정($p=2$)에서 알려진 최상의 결과와 일치합니다.

---

*Generated on 2025-09-20 01:42:24*