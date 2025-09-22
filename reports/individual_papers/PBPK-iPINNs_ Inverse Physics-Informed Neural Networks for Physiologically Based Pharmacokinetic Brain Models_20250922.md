# PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models

**Korean Title:** PBPK-iPINNs: 생리학적 기반 약물동태학적 뇌 모델을 위한 역물리정보 신경망

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Inverse Problem Solving|Inverse Problem Solving]] [[keywords/specific/Physics-Informed Neural Networks|Physics-Informed Neural Networks]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/broad/Differential Equations|Differential Equations]] [[keywords/unique/PBPK-iPINN|PBPK-iPINN]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (85.6% similar) [[2025-09-19/Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (85.0% similar) [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Physiologically Based Pharmacokinetic Modeling
**🔗 Specific Connectable**: Inverse Problem Solving
**🔬 Broad Technical**: Physics-Informed Neural Networks
**⭐ Unique Technical**: PBPK-iPINN
## 🔗 유사한 논문
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (85.6% similar)
- [[2025-09-19/Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (85.0% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (82.8% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks A Second-Order Optimization Perspective]] (81.8% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (81.5% similar)


**ArXiv ID**: [2509.12666](https://arxiv.org/abs/2509.12666)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.12666.pdf)


**ArXiv ID**: [2509.12666](https://arxiv.org/abs/2509.12666)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.12666.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Inverse PINNs
**🔗 Specific Connectable**: Physiologically Based Pharmacokinetic Modeling
**⭐ Unique Technical**: PBPK-iPINN
**🔬 Broad Technical**: Physics-Informed Neural Networks

## 🏷️ 추출된 키워드



`Machine Learning` • 

`Differential Equations` • 

`Physics-Informed Neural Networks` • 

`PBPK-iPINN` • 

`Inverse Problem Solving`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12666v2 Announce Type: replace-cross 
Abstract: Physics-Informed Neural Networks (PINNs) leverage machine learning with differential equations to solve direct and inverse problems, ensuring predictions follow physical laws. Physiologically based pharmacokinetic (PBPK) modeling advances beyond classical compartmental approaches by using a mechanistic, physiology focused framework. A PBPK model is based on a system of ODEs, with each equation representing the mass balance of a drug in a compartment, such as an organ or tissue. These ODEs include parameters that reflect physiological, biochemical, and drug-specific characteristics to simulate how the drug moves through the body. In this paper, we introduce PBPK-iPINN, a method to estimate drug-specific or patient-specific parameters and drug concentration profiles in PBPK brain compartment models using inverse PINNs. We demonstrate that, for the inverse problem to converge to the correct solution, the loss function components (data loss, initial conditions loss, and residual loss) must be appropriately weighted, and parameters (including number of layers, number of neurons, activation functions, learning rate, optimizer, and collocation points) must be carefully tuned. The performance of the PBPK-iPINN approach is then compared with established traditional numerical and statistical methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.12666v2 발표 유형: 교차 대체  
초록: 물리학 정보 신경망(Physics-Informed Neural Networks, PINNs)은 기계 학습과 미분 방정식을 결합하여 직·역 문제를 해결하며, 예측이 물리 법칙을 따르도록 보장합니다. 생리학 기반 약물동태학(Physiologically Based Pharmacokinetic, PBPK) 모델링은 기계적이고 생리학에 중점을 둔 프레임워크를 사용하여 고전적인 구획 접근 방식을 넘어섭니다. PBPK 모델은 ODE(상미분 방정식) 시스템을 기반으로 하며, 각 방정식은 장기나 조직과 같은 구획 내 약물의 질량 균형을 나타냅니다. 이러한 ODE는 약물이 신체를 통해 이동하는 방식을 시뮬레이션하기 위해 생리학적, 생화학적, 약물 특성을 반영하는 매개변수를 포함합니다. 본 논문에서는 역 PINNs를 사용하여 PBPK 뇌 구획 모델에서 약물 특성 또는 환자 특성 매개변수와 약물 농도 프로파일을 추정하는 방법인 PBPK-iPINN을 소개합니다. 역 문제의 올바른 해로 수렴하기 위해 손실 함수 구성 요소(데이터 손실, 초기 조건 손실, 잔차 손실)가 적절히 가중치가 부여되어야 하며, 매개변수(레이어 수, 뉴런 수, 활성화 함수, 학습률, 최적화기, 배치 점 포함)가 신중하게 조정되어야 함을 보여줍니다. 이후 PBPK-iPINN 접근법의 성능을 기존의 전통적인 수치 및 통계적 방법과 비교합니다.

## 📝 요약

이 논문에서는 물리 정보 신경망(PINNs)을 활용하여 약리학적 기반 생리학 모델(PBPK)에서 약물 농도 프로파일과 환자별 매개변수를 추정하는 PBPK-iPINN 방법을 제안합니다. PBPK 모델은 약물이 신체를 통과하는 과정을 시뮬레이션하기 위해 각 장기나 조직의 질량 균형을 나타내는 상미분방정식(ODEs) 시스템을 기반으로 합니다. 이 연구는 역문제 해결 시 손실 함수의 구성 요소(데이터 손실, 초기 조건 손실, 잔차 손실)의 적절한 가중치 설정과 모델 매개변수(층 수, 뉴런 수, 활성화 함수, 학습률, 최적화기, 배치점)의 세심한 조정이 필요함을 보여줍니다. PBPK-iPINN의 성능은 기존의 수치적, 통계적 방법과 비교됩니다.

## 🎯 주요 포인트


- 1. Physics-Informed Neural Networks (PINNs)는 물리 법칙을 따르는 예측을 보장하며, 미분 방정식을 활용하여 직접 및 역문제를 해결한다.

- 2. 생리학 기반 약물동태학(PBPK) 모델링은 기계적이고 생리학에 초점을 맞춘 프레임워크를 사용하여 고전적 구획 접근법을 넘어선다.

- 3. PBPK-iPINN은 역 PINNs를 사용하여 PBPK 뇌 구획 모델에서 약물 또는 환자 특유의 매개변수와 약물 농도 프로파일을 추정하는 방법을 제안한다.

- 4. 역문제가 올바른 해로 수렴하기 위해서는 손실 함수의 구성 요소(데이터 손실, 초기 조건 손실, 잔차 손실)가 적절히 가중되어야 하며, 매개변수(레이어 수, 뉴런 수, 활성화 함수, 학습률, 최적화기, 배치점)도 신중히 조정되어야 한다.

- 5. PBPK-iPINN 접근법의 성능은 기존의 전통적인 수치 및 통계 방법과 비교된다.


---

*Generated on 2025-09-22 16:17:11*