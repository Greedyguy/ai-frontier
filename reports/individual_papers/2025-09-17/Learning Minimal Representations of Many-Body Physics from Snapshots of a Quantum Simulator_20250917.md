# Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator

**Korean Title:** 양자 시뮬레이터의 스냅샷으로부터 다체 물리학의 최소 표현 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Frederik Møller|Frederik Møller]] [[authors/Gabriel Fernández-Fernández|Gabriel Fernández-Fernández]] [[authors/Thomas Schweigler|Thomas Schweigler]] [[authors/Paulin de Schoulepnikoff|Paulin de Schoulepnikoff]] [[authors/Jörg Schmiedmayer|Jörg Schmiedmayer]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Data Driven Discovery in Quantum Systems

## 🔗 유사한 논문
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (82.3% similar)
- [[Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (81.0% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (80.3% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (80.1% similar)
- [[Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (79.2% similar)

## 📋 저자 정보

**Authors:** Frederik Møller, Gabriel Fernández-Fernández, Thomas Schweigler, Paulin de Schoulepnikoff, Jörg Schmiedmayer, Gorka Muñoz-Gil

## 📄 Abstract (원문)

Analog quantum simulators provide access to many-body dynamics beyond the
reach of classical computation. However, extracting physical insights from
experimental data is often hindered by measurement noise, limited observables,
and incomplete knowledge of the underlying microscopic model. Here, we develop
a machine learning approach based on a variational autoencoder (VAE) to analyze
interference measurements of tunnel-coupled one-dimensional Bose gases, which
realize the sine-Gordon quantum field theory. Trained in an unsupervised
manner, the VAE learns a minimal latent representation that strongly correlates
with the equilibrium control parameter of the system. Applied to
non-equilibrium protocols, the latent space uncovers signatures of frozen-in
solitons following rapid cooling, and reveals anomalous post-quench dynamics
not captured by conventional correlation-based methods. These results
demonstrate that generative models can extract physically interpretable
variables directly from noisy and sparse experimental data, providing
complementary probes of equilibrium and non-equilibrium physics in quantum
simulators. More broadly, our work highlights how machine learning can
supplement established field-theoretical techniques, paving the way for
scalable, data-driven discovery in quantum many-body systems.

## 🔍 Abstract (한글 번역)

아날로그 양자 시뮬레이터는 고전적 계산의 범위를 넘어서는 다체 역학에 접근할 수 있게 해줍니다. 그러나 실험 데이터에서 물리적 통찰을 추출하는 것은 측정 잡음, 제한된 관측 가능성, 그리고 기저 미시적 모델에 대한 불완전한 지식으로 인해 종종 방해받습니다. 여기서 우리는 터널 결합된 일차원 보즈 가스의 간섭 측정을 분석하기 위해 변분 오토인코더(VAE)에 기반한 기계 학습 접근법을 개발합니다. 이는 사인-고르돈 양자 장 이론을 실현합니다. 비지도 학습 방식으로 훈련된 VAE는 시스템의 평형 제어 매개변수와 강하게 상관된 최소한의 잠재 표현을 학습합니다. 비평형 프로토콜에 적용했을 때, 잠재 공간은 급속 냉각 후 고정된 솔리톤의 징후를 드러내고, 기존의 상관 기반 방법으로 포착되지 않는 비정상적인 쿼치 후 동역학을 밝혀냅니다. 이러한 결과는 생성 모델이 잡음이 많고 희소한 실험 데이터로부터 물리적으로 해석 가능한 변수를 직접 추출할 수 있음을 보여주며, 양자 시뮬레이터에서 평형 및 비평형 물리학의 보완적인 탐침을 제공합니다. 더 넓게는, 우리의 연구는 기계 학습이 확립된 장 이론 기법을 보완할 수 있음을 강조하며, 양자 다체 시스템에서 확장 가능한 데이터 기반 발견을 위한 길을 열어줍니다.

## 📝 요약

이 논문은 아날로그 양자 시뮬레이터의 실험 데이터를 분석하기 위해 변분 오토인코더(VAE)를 활용한 기계 학습 접근법을 제안합니다. 이 방법은 터널 결합된 1차원 보즈 기체의 간섭 측정을 분석하며, 이는 사인-고든 양자장 이론을 구현합니다. VAE는 비지도 학습을 통해 시스템의 평형 제어 매개변수와 강하게 상관된 최소한의 잠재 표현을 학습합니다. 비평형 프로토콜에 적용한 결과, 잠재 공간은 급속 냉각 후 고정된 솔리톤의 흔적과 전통적인 상관 기반 방법으로는 포착되지 않는 비정상적인 동역학을 드러냅니다. 이 연구는 생성 모델이 노이즈가 많고 희소한 실험 데이터에서 물리적으로 해석 가능한 변수를 추출할 수 있음을 보여주며, 양자 시뮬레이터에서 평형 및 비평형 물리학의 보완적 탐구를 제공합니다. 더 나아가, 기계 학습이 기존의 장 이론 기법을 보완하여 양자 다체 시스템에서 데이터 기반의 발견을 가능하게 함을 강조합니다.

## 🎯 주요 포인트

- 1. 본 연구는 변분 오토인코더(VAE)를 활용하여 터널 결합된 1차원 보즈 기체의 간섭 측정을 분석하는 기계 학습 접근법을 개발하였다.

- 2. VAE는 비지도 학습을 통해 시스템의 평형 제어 매개변수와 강하게 상관된 최소 잠재 표현을 학습한다.

- 3. 비평형 프로토콜에 적용된 잠재 공간은 급속 냉각 후 고정된 솔리톤의 징후를 발견하고, 기존 상관 기반 방법으로 포착되지 않는 비정상적인 쿼치 후 동역학을 드러낸다.

- 4. 생성 모델은 노이즈가 많고 희소한 실험 데이터로부터 물리적으로 해석 가능한 변수를 직접 추출할 수 있음을 보여준다.

- 5. 본 연구는 기계 학습이 기존의 장 이론 기법을 보완할 수 있음을 강조하며, 양자 다체 시스템에서 확장 가능하고 데이터 기반의 발견을 위한 길을 열어준다.

---

*Generated on 2025-09-20 09:30:35*