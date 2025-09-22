# Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems

**Korean Title:** 비선형 동적 시스템의 데이터 기반 모델링을 위한 데이터 노이즈 제거 및 미분 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Jiaqi Yao|Jiaqi Yao]] [[authors/Lewis Mitchell|Lewis Mitchell]] [[authors/John Maclean|John Maclean]] [[authors/Hemanth Saratchandran|Hemanth Saratchandran]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Automatic Differentiation, Sparse Identification of Nonlinear Dynamics

## 🔗 유사한 논문
- [[Out-of-Sight Trajectories_ Tracking, Fusion, and Prediction_20250919|Out-of-Sight Trajectories Tracking, Fusion, and Prediction]] (78.2% similar)
- [[Not All Degradations Are Equal_ A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution_20250918|Not All Degradations Are Equal A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution]] (77.9% similar)
- [[DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (77.8% similar)
- [[A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (77.2% similar)
- [[Efficient Conformal Prediction for Regression Models under Label Noise_20250918|Efficient Conformal Prediction for Regression Models under Label Noise]] (77.1% similar)

## 📋 저자 정보

**Authors:** Jiaqi Yao, Lewis Mitchell, John Maclean, Hemanth Saratchandran

## 📄 Abstract (원문)

Data-driven modeling of nonlinear dynamical systems is often hampered by
measurement noise. We propose a denoising framework, called Runge-Kutta and
Total Variation Based Implicit Neural Representation (RKTV-INR), that
represents the state trajectory with an implicit neural representation (INR)
fitted directly to noisy observations. Runge-Kutta integration and total
variation are imposed as constraints to ensure that the reconstructed state is
a trajectory of a dynamical system that remains close to the original data. The
trained INR yields a clean, continuous trajectory and provides accurate
first-order derivatives via automatic differentiation. These denoised states
and derivatives are then supplied to Sparse Identification of Nonlinear
Dynamics (SINDy) to recover the governing equations. Experiments demonstrate
effective noise suppression, precise derivative estimation, and reliable system
identification.

## 🔍 Abstract (한글 번역)

비선형 동적 시스템의 데이터 기반 모델링은 종종 측정 노이즈로 인해 어려움을 겪습니다. 우리는 Runge-Kutta 및 총 변동 기반 암시적 신경 표현(RKTV-INR)이라는 디노이징 프레임워크를 제안합니다. 이 프레임워크는 암시적 신경 표현(INR)을 사용하여 노이즈가 있는 관측치에 직접 맞추어 상태 궤적을 표현합니다. Runge-Kutta 적분과 총 변동은 재구성된 상태가 원래 데이터에 가까운 동적 시스템의 궤적이 되도록 제약 조건으로 부과됩니다. 훈련된 INR은 깨끗하고 연속적인 궤적을 제공하며, 자동 미분을 통해 정확한 1차 도함수를 제공합니다. 이러한 디노이즈된 상태와 도함수는 비선형 동역학의 희소 식별(SINDy)에 공급되어 지배 방정식을 복원합니다. 실험 결과는 효과적인 노이즈 억제, 정밀한 도함수 추정 및 신뢰할 수 있는 시스템 식별을 보여줍니다.

## 📝 요약

이 논문은 비선형 동적 시스템의 데이터 기반 모델링에서 측정 노이즈 문제를 해결하기 위해 RKTV-INR이라는 새로운 프레임워크를 제안합니다. 이 방법은 노이즈가 있는 관측값에 직접 적합한 암시적 신경 표현(INR)을 사용하여 상태 궤적을 나타냅니다. Runge-Kutta 적분과 총 변동을 제약 조건으로 사용하여 재구성된 상태가 원래 데이터에 가까운 동적 시스템의 궤적이 되도록 합니다. 훈련된 INR은 깨끗하고 연속적인 궤적을 제공하며, 자동 미분을 통해 정확한 1차 도함수를 제공합니다. 이러한 노이즈가 제거된 상태와 도함수는 SINDy에 공급되어 지배 방정식을 복원합니다. 실험 결과, 효과적인 노이즈 억제, 정확한 도함수 추정 및 신뢰할 수 있는 시스템 식별이 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. RKTV-INR은 측정 노이즈가 있는 비선형 동적 시스템의 상태 궤적을 암묵적 신경 표현(INR)으로 나타내는 비소음화 프레임워크를 제안합니다.

- 2. Runge-Kutta 적분과 총 변동 제약을 통해 재구성된 상태가 원래 데이터에 가까운 동적 시스템의 궤적이 되도록 보장합니다.

- 3. 훈련된 INR은 깨끗하고 연속적인 궤적을 제공하며, 자동 미분을 통해 정확한 1차 도함수를 제공합니다.

- 4. 비소음화된 상태와 도함수는 SINDy에 공급되어 지배 방정식을 복원합니다.

- 5. 실험 결과는 효과적인 노이즈 억제, 정밀한 도함수 추정 및 신뢰할 수 있는 시스템 식별을 보여줍니다.

---

*Generated on 2025-09-20 07:42:31*