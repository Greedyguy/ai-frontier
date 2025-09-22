# Circuit realization and hardware linearization of monotone operator equilibrium networks

**Korean Title:** 단조 연산자 평형 네트워크의 회로 구현 및 하드웨어 선형화

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Thomas Chaffey|Thomas Chaffey]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hardware Linearization

## 🔗 유사한 논문
- [[A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (80.6% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (78.5% similar)
- [[MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (77.4% similar)
- [[Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation A Robustness Analysis]] (76.8% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (76.7% similar)

## 📋 저자 정보

**Authors:** Thomas Chaffey

## 📄 Abstract (원문)

It is shown that the port behavior of a resistor-diode network corresponds to
the solution of a ReLU monotone operator equilibrium network (a neural network
in the limit of infinite depth), giving a parsimonious construction of a neural
network in analog hardware. We furthermore show that the gradient of such a
circuit can be computed directly in hardware, using a procedure we call
hardware linearization. This allows the network to be trained in hardware,
which we demonstrate with a device-level circuit simulation. We extend the
results to cascades of resistor-diode networks, which can be used to implement
feedforward and other asymmetric networks. We finally show that different
nonlinear elements give rise to different activation functions, and introduce
the novel diode ReLU which is induced by a non-ideal diode model.

## 🔍 Abstract (한글 번역)

저항-다이오드 네트워크의 포트 동작이 ReLU 단조 연산자 평형 네트워크(무한 깊이의 한계에서의 신경망)의 해와 일치함을 보여주며, 이는 아날로그 하드웨어에서 신경망의 간결한 구성을 제공합니다. 또한, 이러한 회로의 기울기를 하드웨어에서 직접 계산할 수 있는 절차인 하드웨어 선형화를 제안합니다. 이를 통해 네트워크를 하드웨어에서 학습할 수 있으며, 우리는 이를 소자 수준의 회로 시뮬레이션을 통해 입증합니다. 우리는 결과를 저항-다이오드 네트워크의 계단식 구조로 확장하여 피드포워드 및 기타 비대칭 네트워크를 구현할 수 있음을 보여줍니다. 마지막으로, 서로 다른 비선형 요소가 서로 다른 활성화 함수를 유도함을 보여주고, 비이상적인 다이오드 모델에 의해 유도되는 새로운 다이오드 ReLU를 소개합니다.

## 📝 요약

이 논문은 저항-다이오드 네트워크의 포트 동작이 ReLU 단조 연산자 평형 네트워크(무한 깊이의 신경망)의 해와 대응함을 보여주며, 이를 통해 아날로그 하드웨어에서 신경망을 간결하게 구현할 수 있음을 제시합니다. 또한, 하드웨어 선형화라는 절차를 통해 이러한 회로의 기울기를 하드웨어에서 직접 계산할 수 있어, 하드웨어에서 네트워크를 훈련할 수 있음을 입증했습니다. 이 결과를 저항-다이오드 네트워크의 연쇄로 확장하여 피드포워드 및 비대칭 네트워크 구현에 활용할 수 있음을 보였습니다. 마지막으로, 다양한 비선형 요소가 서로 다른 활성화 함수를 유도하며, 비이상적인 다이오드 모델에 의해 유도되는 새로운 다이오드 ReLU를 소개합니다.

## 🎯 주요 포인트

- 1. 저항-다이오드 네트워크의 포트 동작이 ReLU 단조 연산자 평형 네트워크의 해와 일치함을 보였습니다.

- 2. 하드웨어 선형화 절차를 통해 이러한 회로의 그래디언트를 하드웨어에서 직접 계산할 수 있음을 증명했습니다.

- 3. 하드웨어에서 네트워크를 학습시킬 수 있으며, 이를 장치 수준의 회로 시뮬레이션으로 입증했습니다.

- 4. 저항-다이오드 네트워크의 연쇄를 확장하여 피드포워드 및 비대칭 네트워크를 구현할 수 있음을 보였습니다.

- 5. 다양한 비선형 요소가 서로 다른 활성화 함수를 유도하며, 비이상적인 다이오드 모델에 의해 유도된 새로운 다이오드 ReLU를 소개했습니다.

---

*Generated on 2025-09-20 09:31:51*