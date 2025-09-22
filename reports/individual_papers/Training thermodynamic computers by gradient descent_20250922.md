# Training thermodynamic computers by gradient descent

**Korean Title:** 열역학 컴퓨터의 경사 하강법을 통한 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Neural Network Dynamics

## 🔗 유사한 논문
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (83.4% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.7% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (80.3% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks A Second-Order Optimization Perspective]] (80.2% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15324v1 Announce Type: cross 
Abstract: We show how to adjust the parameters of a thermodynamic computer by gradient descent in order to perform a desired computation at a specified observation time. Within a digital simulation of a thermodynamic computer, training proceeds by maximizing the probability with which the computer would generate an idealized dynamical trajectory. The idealized trajectory is designed to reproduce the activations of a neural network trained to perform the desired computation. This teacher-student scheme results in a thermodynamic computer whose finite-time dynamics enacts a computation analogous to that of the neural network. The parameters identified in this way can be implemented in the hardware realization of the thermodynamic computer, which will perform the desired computation automatically, driven by thermal noise. We demonstrate the method on a standard image-classification task, and estimate the thermodynamic advantage -- the ratio of energy costs of the digital and thermodynamic implementations -- to exceed seven orders of magnitude. Our results establish gradient descent as a viable training method for thermodynamic computing, enabling application of the core methodology of machine learning to this emerging field.

## 🔍 Abstract (한글 번역)

arXiv:2509.15324v1 발표 유형: 교차  
초록: 우리는 지정된 관찰 시간에 원하는 계산을 수행하기 위해 열역학적 컴퓨터의 매개변수를 경사 하강법으로 조정하는 방법을 보여줍니다. 열역학적 컴퓨터의 디지털 시뮬레이션 내에서, 훈련은 컴퓨터가 이상적인 동적 궤적을 생성할 확률을 최대화함으로써 진행됩니다. 이상적인 궤적은 원하는 계산을 수행하도록 훈련된 신경망의 활성화를 재현하도록 설계되었습니다. 이 교사-학생 체계는 유한 시간 동역학이 신경망의 계산과 유사한 계산을 수행하는 열역학적 컴퓨터를 결과로 낳습니다. 이렇게 식별된 매개변수는 열역학적 컴퓨터의 하드웨어 구현에 적용될 수 있으며, 이는 열잡음에 의해 자동으로 원하는 계산을 수행할 것입니다. 우리는 표준 이미지 분류 작업에서 이 방법을 시연하고, 디지털 및 열역학적 구현의 에너지 비용 비율인 열역학적 이점을 7차 이상의 크기로 초과한다고 추정합니다. 우리의 결과는 열역학적 컴퓨팅을 위한 실현 가능한 훈련 방법으로서 경사 하강법을 확립하며, 이 신흥 분야에 기계 학습의 핵심 방법론을 적용할 수 있게 합니다.

## 📝 요약

이 논문은 열역학적 컴퓨터의 매개변수를 경사 하강법을 통해 조정하여 특정 시간에 원하는 계산을 수행하는 방법을 제시합니다. 디지털 시뮬레이션 내에서, 컴퓨터가 이상적인 동적 궤적을 생성할 확률을 최대화하여 훈련이 진행됩니다. 이 궤적은 신경망의 활성화를 재현하도록 설계되었으며, 이를 통해 열역학적 컴퓨터가 신경망과 유사한 계산을 수행할 수 있게 합니다. 이러한 매개변수는 하드웨어에 구현되어 열잡음에 의해 자동으로 원하는 계산을 수행합니다. 표준 이미지 분류 작업에서 이 방법을 시연하였으며, 디지털 구현과 열역학적 구현의 에너지 비용 비율이 7자릿수 이상임을 추정했습니다. 이 결과는 열역학적 컴퓨팅에서 경사 하강법이 유효한 훈련 방법임을 입증하며, 기계 학습의 핵심 방법론을 이 새로운 분야에 적용할 수 있게 합니다.

## 🎯 주요 포인트

- 1. 열역학적 컴퓨터의 매개변수를 경사 하강법을 통해 조정하여 원하는 계산을 수행할 수 있도록 하는 방법을 제시합니다.

- 2. 디지털 시뮬레이션에서 열역학적 컴퓨터의 훈련은 이상적인 동적 궤적을 생성할 확률을 최대화하는 방식으로 진행됩니다.

- 3. 이 방법은 신경망의 계산을 모방하는 열역학적 컴퓨터를 구현하며, 하드웨어에서 자동으로 원하는 계산을 수행할 수 있도록 합니다.

- 4. 표준 이미지 분류 작업에 이 방법을 적용하여 디지털 구현과 열역학적 구현의 에너지 비용 비율이 7자릿수 이상임을 추정합니다.

- 5. 경사 하강법이 열역학적 컴퓨팅의 유효한 훈련 방법임을 입증하여, 기계 학습의 핵심 방법론을 이 새로운 분야에 적용할 수 있게 합니다.

---

*Generated on 2025-09-22 15:37:06*