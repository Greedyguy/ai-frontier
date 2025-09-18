
# Physics-based deep kernel learning for parameter estimation in high dimensional PDEs

**Korean Title:** 고차원 PDE에서 매개변수 추정을 위한 물리학 기반 딥 커널 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Inverse PDE Problems|Inverse PDE Problems]] [[keywords/broad/Physics-based Deep Kernel Learning|Physics-based Deep Kernel Learning]] [[keywords/broad/Hamiltonian Monte Carlo|Hamiltonian Monte Carlo]] [[keywords/specific/Neural Network Feature Extractor|Neural Network Feature Extractor]] [[keywords/unique/Sparse Exact Observations|Sparse Exact Observations]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Inverse PDE problems
**🔬 Broad Technical**: Physics-based deep kernel learning, Hamiltonian Monte Carlo
**🔗 Specific Connectable**: Neural network feature extractor
**⭐ Unique Technical**: Sparse observations

**ArXiv ID**: [2509.14054](https://arxiv.org/abs/2509.14054)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.14054.pdf)


## 🏷️ 추출된 키워드



`Physics-based deep kernel learning` • 

`Hamiltonian Monte Carlo` • 

`Neural network feature extractor` • 

`Sparse observations` • 

`Full Bayesian framework`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14054v1 Announce Type: cross 
Abstract: Inferring parameters of high-dimensional partial differential equations (PDEs) poses significant computational and inferential challenges, primarily due to the curse of dimensionality and the inherent limitations of traditional numerical methods. This paper introduces a novel two-stage Bayesian framework that synergistically integrates training, physics-based deep kernel learning (DKL) with Hamiltonian Monte Carlo (HMC) to robustly infer unknown PDE parameters and quantify their uncertainties from sparse, exact observations. The first stage leverages physics-based DKL to train a surrogate model, which jointly yields an optimized neural network feature extractor and robust initial estimates for the PDE parameters. In the second stage, with the neural network weights fixed, HMC is employed within a full Bayesian framework to efficiently sample the joint posterior distribution of the kernel hyperparameters and the PDE parameters. Numerical experiments on canonical and high-dimensional inverse PDE problems demonstrate that our framework accurately estimates parameters, provides reliable uncertainty estimates, and effectively addresses challenges of data sparsity and model complexity, offering a robust and scalable tool for diverse scientific and engineering applications.

## 🔍 Abstract (한글 번역)

arXiv:2509.14054v1 발표 유형: 교차
요약: 고차원 편미분방정식(PDEs)의 매개변수를 추론하는 것은 차원의 저주와 전통적인 수치 방법의 본질적인 한계로 인해 중요한 계산 및 추론적 도전을 제기합니다. 본 논문은 희소한 정확한 관측값으로부터 알려지지 않은 PDE 매개변수를 견고하게 추론하고 그 불확실성을 양적화하기 위해 훈련, 물리학 기반의 딥 커널 학습(DKL)과 해밀토니안 몬테 카를로(HMC)를 시너지적으로 통합하는 혁신적인 두 단계 베이지안 프레임워크를 소개합니다. 첫 번째 단계에서는 물리학 기반의 DKL을 활용하여 대리 모델을 훈련시키는데, 이는 최적화된 신경망 특징 추출기와 PDE 매개변수에 대한 견고한 초기 추정치를 동시에 제공합니다. 두 번째 단계에서는 신경망 가중치를 고정한 상태에서 HMC가 전체 베이지안 프레임워크 내에서 커널 초모수와 PDE 매개변수의 결합 사후 분포를 효율적으로 샘플링합니다. 대표적이고 고차원 역 PDE 문제에 대한 수치 실험은 우리의 프레임워크가 매개변수를 정확하게 추정하고 신뢰할 수 있는 불확실성 추정을 제공하며 데이터 희소성과 모델 복잡성의 도전을 효과적으로 해결하며 다양한 과학 및 공학 응용에 대한 견고하고 확장 가능한 도구를 제공함을 보여줍니다.

## 📝 요약

고차원 편미분 방정식의 매개변수를 추론하는 것은 차원의 저주와 전통적인 수치 방법의 한계로 인해 중요한 계산 및 추론적 도전을 제기한다. 본 논문은 미지의 PDE 매개변수를 견고하게 추정하고 희소한 정확한 관측으로부터 그들의 불확실성을 양적으로하는 혁신적인 두 단계 베이지안 프레임워크를 소개한다. 첫 번째 단계에서 물리학 기반 DKL을 활용하여 대리 모델을 훈련시키고 PDE 매개변수에 대한 강화된 초기 추정치를 동시에 제공한다. 두 번째 단계에서는 신경망 가중치가 고정된 상태에서 HMC를 사용하여 커널 초모수와 PDE 매개변수의 결합 사후 분포를 효율적으로 샘플링한다. 수치 실험 결과, 본 프레임워크가 매개변수를 정확하게 추정하고 신뢰할 수 있는 불확실성 추정을 제공하며 데이터 희소성과 모델 복잡성의 도전을 효과적으로 해결함을 보여준다.

## 🎯 주요 포인트


- 고차원 편미분 방정식의 매개변수를 추정하는 새로운 베이지안 프레임워크 소개

- 물리학 기반 딥 커널 학습과 해밀토니안 몬테 카를로를 통합하여 불확실성을 양적화

- 수치 실험 결과, 매개변수를 정확하게 추정하고 신뢰할 수 있는 불확실성을 제공함

- 데이터 희소성과 모델 복잡성의 도전을 효과적으로 해결하여 다양한 과학 및 공학 응용에 강력하고 확장 가능한 도구 제공


---

*Generated on 2025-09-18 16:45:36*