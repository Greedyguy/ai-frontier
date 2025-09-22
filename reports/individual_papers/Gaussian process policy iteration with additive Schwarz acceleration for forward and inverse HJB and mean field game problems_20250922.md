# Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems

**Korean Title:** 가우시안 프로세스 정책 반복법과 전방 및 역방향 해밀턴-야코비-벨만(HJB) 및 평균장 게임 문제에 대한 가산 슈바르츠 가속화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Hamilton Jacobi Bellman Equations|Hamilton Jacobi Bellman Equations]] [[keywords/broad/Gaussian Process|Gaussian Process]] [[keywords/broad/Mean Field Games|Mean Field Games]] [[keywords/unique/Additive Schwarz Acceleration|Additive Schwarz Acceleration]] [[categories/cs.LG|cs.LG]] [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (82.3% similar) [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (82.1% similar) [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Policy Iteration, Hamilton Jacobi Bellman Equations
**🔬 Broad Technical**: Gaussian Process, Mean Field Games
**⭐ Unique Technical**: Additive Schwarz Acceleration
## 🔗 유사한 논문
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (82.3% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (82.1% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (80.6% similar)
- [[2025-09-22/Kernel Model Validation_ How To Do It, And Why You Should Care_20250922|Kernel Model Validation How To Do It, And Why You Should Care]] (80.5% similar)
- [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (80.3% similar)


**ArXiv ID**: [2505.00909](https://arxiv.org/abs/2505.00909)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.00909.pdf)


**ArXiv ID**: [2505.00909](https://arxiv.org/abs/2505.00909)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.00909.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Inverse HJB Problems
**🔗 Specific Connectable**: Policy Iteration
**⭐ Unique Technical**: Additive Schwarz Acceleration
**🔬 Broad Technical**: Gaussian Process, Mean Field Games

## 🏷️ 추출된 키워드



`Gaussian Process` • 

`Mean Field Games` • 

`Policy Iteration` • 

`Hamilton Jacobi Bellman Equations` • 

`Additive Schwarz Acceleration`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.00909v2 Announce Type: replace 
Abstract: We propose a Gaussian Process (GP)-based policy iteration framework for addressing both forward and inverse problems in Hamilton--Jacobi--Bellman (HJB) equations and mean field games (MFGs). Policy iteration is formulated as an alternating procedure between solving the value function under a fixed control policy and updating the policy based on the resulting value function. By exploiting the linear structure of GPs for function approximation, each policy evaluation step admits an explicit closed-form solution, eliminating the need for numerical optimization. To improve convergence, we incorporate the additive Schwarz acceleration as a preconditioning step following each policy update. Numerical experiments demonstrate the effectiveness of Schwarz acceleration in improving computational efficiency.

## 🔍 Abstract (한글 번역)

arXiv:2505.00909v2 발표 유형: 교체  
초록: 우리는 해밀턴-자코비-벨만(HJB) 방정식과 평균장 게임(MFG)의 순방향 및 역방향 문제를 해결하기 위한 가우시안 프로세스(GP) 기반의 정책 반복 프레임워크를 제안합니다. 정책 반복은 고정된 제어 정책 하에서 가치 함수를 해결하는 단계와 결과 가치 함수에 기반하여 정책을 갱신하는 단계를 번갈아 수행하는 절차로 구성됩니다. 함수 근사를 위한 GP의 선형 구조를 활용함으로써, 각 정책 평가 단계는 명시적인 닫힌 형태의 해를 허용하여 수치 최적화의 필요성을 제거합니다. 수렴을 개선하기 위해, 우리는 각 정책 갱신 후 전처리 단계로서 가산 슈바르츠 가속을 도입합니다. 수치 실험은 계산 효율성을 향상시키는 데 있어 슈바르츠 가속의 효과를 입증합니다.

## 📝 요약

이 논문은 해밀턴-야코비-벨만(HJB) 방정식과 평균장 게임(MFG)의 순방향 및 역방향 문제를 해결하기 위해 가우시안 프로세스(GP) 기반의 정책 반복 프레임워크를 제안합니다. 정책 반복은 고정된 제어 정책 하에서 가치 함수를 해결하고, 그 결과를 바탕으로 정책을 갱신하는 절차로 구성됩니다. GP의 선형 구조를 활용하여 각 정책 평가 단계에서 명시적인 해를 제공함으로써 수치 최적화가 필요하지 않습니다. 수렴 속도를 개선하기 위해 각 정책 업데이트 후에 슈바르츠 가속 기법을 사전 조건화 단계로 도입했습니다. 수치 실험 결과, 슈바르츠 가속이 계산 효율성을 향상시키는 데 효과적임을 보여줍니다.

## 🎯 주요 포인트


- 1. Gaussian Process(GP)를 기반으로 한 정책 반복 프레임워크를 제안하여 Hamilton-Jacobi-Bellman(HJB) 방정식과 평균장 게임(MFG)의 순방향 및 역방향 문제를 해결합니다.

- 2. 정책 반복은 고정된 제어 정책 하에서 가치 함수를 해결하고, 결과 가치 함수에 기반하여 정책을 갱신하는 절차로 구성됩니다.

- 3. 함수 근사화를 위한 GP의 선형 구조를 활용하여 각 정책 평가 단계에서 명시적인 폐쇄형 해를 얻을 수 있어 수치 최적화가 필요하지 않습니다.

- 4. 수렴성을 개선하기 위해 각 정책 갱신 후 전처리 단계로 Schwarz 가속을 추가합니다.

- 5. 수치 실험을 통해 Schwarz 가속이 계산 효율성을 향상시키는 데 효과적임을 입증합니다.


---

*Generated on 2025-09-22 15:58:20*