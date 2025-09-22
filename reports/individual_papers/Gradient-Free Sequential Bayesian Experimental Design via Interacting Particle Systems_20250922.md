# Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems

**Korean Title:** 입자 상호작용 시스템을 통한 그래디언트-프리 순차 베이지안 실험 설계

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Variational Gaussian Approximation|Variational Gaussian Approximation]] [[keywords/specific/Ensemble Kalman Inversion|Ensemble Kalman Inversion]] [[keywords/specific/Affine-Invariant Langevin Dynamics|Affine-Invariant Langevin Dynamics]] [[keywords/broad/Bayesian Optimal Experimental Design|Bayesian Optimal Experimental Design]] [[keywords/unique/Gradient-Free Sequential Design|Gradient-Free Sequential Design]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (83.6% similar) [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (83.1% similar) [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Gradient-Free Design Optimization
**🔗 Specific Connectable**: Ensemble Kalman Inversion, Affine-Invariant Langevin Dynamics
**🔬 Broad Technical**: Bayesian Optimal Experimental Design
**⭐ Unique Technical**: Variational Gaussian Approximation
## 🔗 유사한 논문
- [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (83.6% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (83.1% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (81.0% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (80.9% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (79.6% similar)


**ArXiv ID**: [2504.13320](https://arxiv.org/abs/2504.13320)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2504.13320.pdf)


**ArXiv ID**: [2504.13320](https://arxiv.org/abs/2504.13320)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2504.13320.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Ensemble Kalman Inversion, Affine-Invariant Langevin Dynamics
**⭐ Unique Technical**: Variational Gaussian Approximation
**🔬 Broad Technical**: Bayesian Optimal Experimental Design

## 🏷️ 추출된 키워드



`Bayesian Optimal Experimental Design` • 

`Posterior Sampling` • 

`Ensemble Kalman Inversion` • 

`Affine-Invariant Langevin Dynamics` • 

`Variational Gaussian Approximation`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.13320v3 Announce Type: replace-cross 
Abstract: We introduce a gradient-free framework for Bayesian Optimal Experimental Design (BOED) in sequential settings, aimed at complex systems where gradient information is unavailable. Our method combines Ensemble Kalman Inversion (EKI) for design optimization with the Affine-Invariant Langevin Dynamics (ALDI) sampler for efficient posterior sampling-both of which are derivative-free and ensemble-based. To address the computational challenges posed by nested expectations in BOED, we propose variational Gaussian and parametrized Laplace approximations that provide tractable upper and lower bounds on the Expected Information Gain (EIG). These approximations enable scalable utility estimation in high-dimensional spaces and PDE-constrained inverse problems. We demonstrate the performance of our framework through numerical experiments ranging from linear Gaussian models to PDE-based inference tasks, highlighting the method's robustness, accuracy, and efficiency in information-driven experimental design.

## 🔍 Abstract (한글 번역)

arXiv:2504.13320v3 발표 유형: 교차 대체  
초록: 우리는 복잡한 시스템에서 기울기 정보가 없는 경우를 대상으로 하는 순차적 설정에서의 베이지안 최적 실험 설계(BOED)를 위한 기울기 없는 프레임워크를 소개합니다. 우리의 방법은 설계 최적화를 위한 앙상블 칼만 반전(EKI)과 효율적인 사후 샘플링을 위한 아핀-불변 랑주뱅 동역학(ALDI) 샘플러를 결합합니다. 이 두 가지 모두 파생물이 없고 앙상블 기반입니다. BOED에서 중첩된 기대값이 제기하는 계산적 문제를 해결하기 위해, 우리는 기대 정보 이득(EIG)에 대한 계산 가능한 상한과 하한을 제공하는 변분 가우시안 및 매개화된 라플라스 근사를 제안합니다. 이러한 근사는 고차원 공간 및 PDE 제약 역문제에서 확장 가능한 유틸리티 추정을 가능하게 합니다. 우리는 선형 가우시안 모델에서 PDE 기반 추론 작업에 이르는 수치 실험을 통해 우리의 프레임워크의 성능을 입증하며, 정보 기반 실험 설계에서 방법의 견고성, 정확성 및 효율성을 강조합니다.

## 📝 요약

이 논문은 복잡한 시스템에서 기울기 정보 없이 순차적 실험 설계를 위한 베이지안 최적 실험 설계(BOED) 프레임워크를 제안합니다. 설계 최적화를 위해 Ensemble Kalman Inversion(EKI)와 효율적인 사후 샘플링을 위한 Affine-Invariant Langevin Dynamics(ALDI) 샘플러를 결합하여 파생 없이도 작동합니다. BOED의 중첩 기대값 계산 문제를 해결하기 위해 변분 가우시안 및 매개화된 라플라스 근사를 제안하여 기대 정보 이득(EIG)에 대한 상하한을 제공합니다. 이 방법은 고차원 공간 및 편미분 방정식(PDE) 제약 역문제에서 유용성을 확장 가능하게 평가합니다. 수치 실험을 통해 선형 가우시안 모델부터 PDE 기반 추론 작업까지 프레임워크의 견고성, 정확성 및 효율성을 입증합니다.

## 🎯 주요 포인트


- 1. 본 연구는 복잡한 시스템에서 기울기 정보 없이도 사용할 수 있는 베이지안 최적 실험 설계(BOED)를 위한 기울기 없는 프레임워크를 제안합니다.

- 2. 제안된 방법은 설계 최적화를 위한 Ensemble Kalman Inversion(EKI)과 효율적인 사후 샘플링을 위한 Affine-Invariant Langevin Dynamics(ALDI) 샘플러를 결합하여 사용합니다.

- 3. BOED에서 중첩된 기대값 계산의 계산적 문제를 해결하기 위해, 변분 가우시안 및 매개변수화된 라플라스 근사를 제안하여 기대 정보 이득(EIG)의 상한 및 하한을 제공합니다.

- 4. 제안된 근사는 고차원 공간 및 편미분 방정식(PDE) 제약 역문제에서 확장 가능한 효용 추정을 가능하게 합니다.

- 5. 본 프레임워크의 성능은 선형 가우시안 모델부터 PDE 기반 추론 작업에 이르는 수치 실험을 통해 입증되었으며, 정보 기반 실험 설계에서의 견고성, 정확성 및 효율성을 강조합니다.


---

*Generated on 2025-09-22 16:11:11*