---
keywords:
  - Hamiltonian Monte Carlo
  - Uncertainty Quantification
  - Deep Kernel Learning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:47:53.451660",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hamiltonian Monte Carlo",
    "Uncertainty Quantification",
    "Deep Kernel Learning"
  ],
  "rejected_keywords": [
    "Partial Differential Equations"
  ],
  "similarity_scores": {
    "Hamiltonian Monte Carlo": 0.82,
    "Uncertainty Quantification": 0.8,
    "Deep Kernel Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Physics-based deep kernel learning for parameter estimation in high dimensional PDEs

**Korean Title:** 고차원 편미분 방정식에서의 매개변수 추정을 위한 물리 기반 심층 커널 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hamiltonian Monte Carlo|Hamiltonian Monte Carlo]], [[keywords/Uncertainty Quantification|uncertainty quantification]]
**⚡ Unique Technical**: [[keywords/Deep Kernel Learning|deep kernel learning]]

## 🔗 유사한 논문
- [[Deconstructing Intraocular Pressure_ A Non-invasive Multi-Stage Probabilistic Inverse Framework_20250917|Deconstructing Intraocular Pressure A Non-invasive Multi-Stage Probabilistic Inverse Framework]] (81.6% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (81.0% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (79.8% similar)
- [[Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (79.8% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (79.7% similar)

## 📋 저자 정보

**Authors:** Weihao Yan, Christoph Brune, Mengwu Guo

## 📄 Abstract (원문)

Inferring parameters of high-dimensional partial differential equations
(PDEs) poses significant computational and inferential challenges, primarily
due to the curse of dimensionality and the inherent limitations of traditional
numerical methods. This paper introduces a novel two-stage Bayesian framework
that synergistically integrates training, physics-based deep kernel learning
(DKL) with Hamiltonian Monte Carlo (HMC) to robustly infer unknown PDE
parameters and quantify their uncertainties from sparse, exact observations.
The first stage leverages physics-based DKL to train a surrogate model, which
jointly yields an optimized neural network feature extractor and robust initial
estimates for the PDE parameters. In the second stage, with the neural network
weights fixed, HMC is employed within a full Bayesian framework to efficiently
sample the joint posterior distribution of the kernel hyperparameters and the
PDE parameters. Numerical experiments on canonical and high-dimensional inverse
PDE problems demonstrate that our framework accurately estimates parameters,
provides reliable uncertainty estimates, and effectively addresses challenges
of data sparsity and model complexity, offering a robust and scalable tool for
diverse scientific and engineering applications.

## 🔍 Abstract (한글 번역)

고차원 편미분 방정식(PDE)의 매개변수를 추론하는 것은 주로 차원의 저주와 전통적인 수치 해법의 내재적 한계로 인해 상당한 계산 및 추론상의 도전을 제기합니다. 본 논문은 훈련, 물리 기반 심층 커널 학습(DKL)과 해밀토니안 몬테카를로(HMC)를 시너지적으로 통합하여 희소하고 정확한 관측치로부터 미지의 PDE 매개변수를 견고하게 추론하고 그 불확실성을 정량화하는 새로운 2단계 베이지안 프레임워크를 소개합니다. 첫 번째 단계에서는 물리 기반 DKL을 활용하여 대리 모델을 훈련하며, 이는 최적화된 신경망 특징 추출기와 PDE 매개변수에 대한 견고한 초기 추정치를 공동으로 제공합니다. 두 번째 단계에서는 신경망 가중치를 고정한 상태에서 HMC를 전체 베이지안 프레임워크 내에서 사용하여 커널 하이퍼파라미터와 PDE 매개변수의 결합 사후 분포를 효율적으로 샘플링합니다. 전형적이고 고차원적인 역 PDE 문제에 대한 수치 실험은 본 프레임워크가 매개변수를 정확하게 추정하고 신뢰할 수 있는 불확실성 추정치를 제공하며, 데이터 희소성과 모델 복잡성의 문제를 효과적으로 해결하여 다양한 과학 및 공학 응용에 견고하고 확장 가능한 도구를 제공함을 보여줍니다.

## 📝 요약

이 논문은 고차원 편미분방정식(PDE)의 매개변수 추론 문제를 해결하기 위해 새로운 이단계 베이지안 프레임워크를 제안합니다. 첫 번째 단계에서는 물리 기반 심층 커널 학습(DKL)을 활용하여 대리 모델을 훈련하고, 최적화된 신경망 특징 추출기와 PDE 매개변수의 초기 추정치를 제공합니다. 두 번째 단계에서는 신경망 가중치를 고정한 상태에서 해밀토니안 몬테카를로(HMC)를 사용하여 커널 하이퍼파라미터와 PDE 매개변수의 결합 사후 분포를 효율적으로 샘플링합니다. 이 프레임워크는 데이터 희소성과 모델 복잡성 문제를 효과적으로 해결하며, 다양한 과학 및 공학 분야에 적용 가능한 강력하고 확장 가능한 도구를 제공합니다. 실험 결과, 매개변수 추정의 정확성과 불확실성 평가의 신뢰성을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 고차원 편미분 방정식(PDE) 매개변수 추론을 위한 새로운 2단계 베이지안 프레임워크를 제안합니다.

- 2. 첫 번째 단계에서는 물리 기반 딥 커널 학습(DKL)을 활용하여 대리 모델을 훈련하고, 최적화된 신경망 특징 추출기와 PDE 매개변수의 초기 추정치를 제공합니다.

- 3. 두 번째 단계에서는 신경망 가중치를 고정한 상태에서 해밀토니안 몬테카를로(HMC)를 사용하여 커널 하이퍼파라미터와 PDE 매개변수의 결합 사후 분포를 효율적으로 샘플링합니다.

- 4. 수치 실험 결과, 제안된 프레임워크는 매개변수 추정의 정확성과 불확실성 추정의 신뢰성을 제공하며, 데이터 희소성과 모델 복잡성 문제를 효과적으로 해결합니다.

- 5. 이 프레임워크는 다양한 과학 및 공학 응용 분야에 대해 견고하고 확장 가능한 도구를 제공합니다.

---

*Generated on 2025-09-20 09:14:09*