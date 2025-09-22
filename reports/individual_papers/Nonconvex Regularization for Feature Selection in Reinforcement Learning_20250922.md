# Nonconvex Regularization for Feature Selection in Reinforcement Learning

**Korean Title:** 비볼록 정규화 기법을 활용한 강화 학습에서의 특징 선택

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Forward-Reflected-Backward Splitting

## 🔗 유사한 논문
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (82.9% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (82.5% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.1% similar)
- [[2025-09-22/Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations_20250922|Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations]] (82.0% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15652v1 Announce Type: new 
Abstract: This work proposes an efficient batch algorithm for feature selection in reinforcement learning (RL) with theoretical convergence guarantees. To mitigate the estimation bias inherent in conventional regularization schemes, the first contribution extends policy evaluation within the classical least-squares temporal-difference (LSTD) framework by formulating a Bellman-residual objective regularized with the sparsity-inducing, nonconvex projected minimax concave (PMC) penalty. Owing to the weak convexity of the PMC penalty, this formulation can be interpreted as a special instance of a general nonmonotone-inclusion problem. The second contribution establishes novel convergence conditions for the forward-reflected-backward splitting (FRBS) algorithm to solve this class of problems. Numerical experiments on benchmark datasets demonstrate that the proposed approach substantially outperforms state-of-the-art feature-selection methods, particularly in scenarios with many noisy features.

## 🔍 Abstract (한글 번역)

arXiv:2509.15652v1 발표 유형: 신규  
초록: 본 연구는 이론적 수렴 보장을 갖춘 강화 학습(RL)에서의 효율적인 배치 알고리즘을 제안합니다. 기존의 정규화 방식에 내재된 추정 편향을 완화하기 위해, 첫 번째 기여는 고전적인 최소자승 시차차이(LSTD) 프레임워크 내에서 정책 평가를 확장하여, 희소성을 유도하는 비볼록 투영 극소 오목(PMC) 패널티로 정규화된 벨만 잔차 목적을 공식화합니다. PMC 패널티의 약한 볼록성 덕분에, 이 공식은 일반적인 비단조 포함 문제의 특별한 사례로 해석될 수 있습니다. 두 번째 기여는 이 클래스의 문제를 해결하기 위한 전진-반사-후진 분할(FRBS) 알고리즘에 대한 새로운 수렴 조건을 확립합니다. 벤치마크 데이터셋에 대한 수치 실험은 제안된 접근 방식이 특히 많은 잡음이 있는 특징이 있는 시나리오에서 최첨단 특징 선택 방법을 상당히 능가함을 보여줍니다.

## 📝 요약

이 연구는 강화 학습에서 효율적인 특성 선택을 위한 배치 알고리즘을 제안하며, 이론적 수렴 보장을 제공합니다. 첫 번째 기여는 기존의 정규화 방식의 추정 편향을 줄이기 위해, 고전적인 최소자승 시차차이(LSTD) 프레임워크 내에서 벨만 잔차 목표를 희소성을 유도하는 비볼록 PMC 페널티로 정규화하여 정책 평가를 확장한 것입니다. 두 번째 기여는 이러한 문제를 해결하기 위한 FRBS 알고리즘의 새로운 수렴 조건을 제시한 것입니다. 벤치마크 데이터셋에 대한 실험 결과, 제안된 방법이 특히 많은 잡음이 있는 특성 시나리오에서 최신 특성 선택 방법보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 강화 학습에서 효율적인 특징 선택을 위한 배치 알고리즘을 제안하고 이론적 수렴 보장을 제공한다.

- 2. 기존 정규화 방식의 추정 편향을 완화하기 위해, 비볼록 PMC 페널티를 사용한 벨만 잔차 목적을 공식화하여 LSTD 프레임워크 내에서 정책 평가를 확장한다.

- 3. PMC 페널티의 약한 볼록성 덕분에, 이 공식화는 일반적인 비단조 포함 문제의 특수한 사례로 해석될 수 있다.

- 4. FRBS 알고리즘을 사용하여 이 문제를 해결하기 위한 새로운 수렴 조건을 확립한다.

- 5. 벤치마크 데이터셋에 대한 수치 실험에서 제안된 접근법이 특히 많은 잡음이 있는 특징이 있는 시나리오에서 최첨단 특징 선택 방법을 능가함을 입증한다.

---

*Generated on 2025-09-22 15:21:37*