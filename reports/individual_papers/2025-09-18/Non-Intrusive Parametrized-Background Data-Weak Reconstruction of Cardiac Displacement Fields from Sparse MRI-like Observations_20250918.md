# Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations

**Korean Title:** 희소 MRI 유사 관측으로부터 심장 변위장을 비침습적 매개변수화된 배경 데이터 약한 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Francesco C. Mantegazza|Francesco C. Mantegazza]] [[authors/Federica Caforio|Federica Caforio]] [[authors/Christoph Augustin|Christoph Augustin]] [[authors/Matthias A. F. Gsell|Matthias A. F. Gsell]] [[authors/Gundolf Haase|Gundolf Haase]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sparse Measurement Reconstruction

## 🔗 유사한 논문
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (80.1% similar)
- [[Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (79.8% similar)
- [[Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease_20250918|Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease]] (79.4% similar)
- [[Inspired by machine learning optimization_ can gradient-based optimizers solve cycle skipping in full waveform inversion given sufficient iterations_20250918|Inspired by machine learning optimization can gradient-based optimizers solve cycle skipping in full waveform inversion given sufficient iterations]] (79.4% similar)
- [[Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (79.3% similar)

## 📋 저자 정보

**Authors:** Francesco C. Mantegazza, Federica Caforio, Christoph Augustin, Matthias A. F. Gsell, Gundolf Haase, Elias Karabelas

## 📄 Abstract (원문)

Personalized cardiac diagnostics require accurate reconstruction of
myocardial displacement fields from sparse clinical imaging data, yet current
methods often demand intrusive access to computational models. In this work, we
apply the non-intrusive Parametrized-Background Data-Weak (PBDW) approach to
three-dimensional (3D) cardiac displacement field reconstruction from limited
Magnetic Resonance Image (MRI)-like observations. Our implementation requires
only solution snapshots -- no governing equations, assembly routines, or solver
access -- enabling immediate deployment across commercial and research codes
using different constitutive models. Additionally, we introduce two
enhancements: an H-size minibatch worst-case Orthogonal Matching Pursuit (wOMP)
algorithm that improves Sensor Selection (SS) computational efficiency while
maintaining reconstruction accuracy, and memory optimization techniques
exploiting block matrix structures in vectorial problems. We demonstrate the
effectiveness of the method through validation on a 3D left ventricular model
with simulated scar tissue. Starting with noise-free reconstruction, we
systematically incorporate Gaussian noise and spatial sparsity mimicking
realistic MRI acquisition protocols. Results show exceptional accuracy in
noise-free conditions (relative L2 error of order O(1e-5)), robust performance
with 10% noise (relative L2 error of order O(1e-2)), and effective
reconstruction from sparse measurements (relative L2 error of order O(1e-2)).
The online reconstruction achieves four-order-of-magnitude computational
speed-up compared to full Finite Element (FE) simulations, with reconstruction
times under one tenth of second for sparse scenarios, demonstrating significant
potential for integration into clinical cardiac modeling workflows.

## 🔍 Abstract (한글 번역)

개인 맞춤형 심장 진단은 희소한 임상 영상 데이터로부터 심근 변위장을 정확하게 재구성하는 것을 요구하지만, 현재의 방법들은 종종 계산 모델에 대한 침습적인 접근을 필요로 합니다. 본 연구에서는 제한된 자기공명영상(MRI) 유사 관측치로부터 3차원(3D) 심장 변위장 재구성을 위해 비침습적 매개변수화된 배경 데이터 약화(PBDW) 접근법을 적용하였습니다. 우리의 구현은 해법 스냅샷만을 필요로 하며, 지배 방정식, 조립 루틴, 또는 해법 접근이 필요하지 않아 다양한 구성 모델을 사용하는 상용 및 연구 코드에 즉각적인 배포가 가능합니다. 추가적으로, 우리는 두 가지 개선점을 소개합니다: 센서 선택(SS) 계산 효율성을 향상시키면서 재구성 정확성을 유지하는 H-크기 미니배치 최악의 경우 직교 매칭 추구(wOMP) 알고리즘과 벡터 문제에서 블록 행렬 구조를 활용한 메모리 최적화 기술입니다. 우리는 시뮬레이션된 흉터 조직을 가진 3D 좌심실 모델에 대한 검증을 통해 방법의 효과성을 입증합니다. 잡음이 없는 재구성에서 시작하여, 우리는 체계적으로 현실적인 MRI 획득 프로토콜을 모방한 가우시안 잡음과 공간적 희소성을 통합합니다. 결과는 잡음이 없는 조건에서의 뛰어난 정확성(상대 L2 오차 O(1e-5) 수준), 10% 잡음에서의 강건한 성능(상대 L2 오차 O(1e-2) 수준), 그리고 희소한 측정에서의 효과적인 재구성(상대 L2 오차 O(1e-2) 수준)을 보여줍니다. 온라인 재구성은 전체 유한 요소(FE) 시뮬레이션과 비교하여 네 자리 수의 계산 속도 향상을 달성하며, 희소 시나리오에서 재구성 시간이 0.1초 미만으로 임상 심장 모델링 워크플로우에 통합될 수 있는 상당한 잠재력을 보여줍니다.

## 📝 요약

이 논문은 제한된 MRI 데이터를 활용하여 심근 변위장을 정확히 재구성하는 방법을 제안합니다. 기존 방법의 복잡성을 줄이기 위해 비침습적 PBDW 접근 방식을 사용하여 다양한 모델에 즉시 적용할 수 있습니다. 주요 기여로는 H-크기 미니배치 wOMP 알고리즘을 통한 센서 선택 효율성 향상과 블록 행렬 구조를 활용한 메모리 최적화가 있습니다. 3D 좌심실 모델을 통해 검증한 결과, 잡음 없는 조건에서 높은 정확도를 보였고, 10% 잡음 및 희소한 측정에서도 강력한 성능을 발휘했습니다. 이 방법은 기존의 유한 요소 시뮬레이션보다 1만 배 빠른 속도를 자랑하며, 임상 심장 모델링에 유망한 통합 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 제한된 MRI 유사 관측치로부터 3D 심장 변위장 재구성을 위해 비침습적 PBDW 접근법을 적용하였다.

- 2. 제안된 방법은 해석 스냅샷만 필요로 하며, 다양한 구성 모델을 사용하는 상용 및 연구 코드에 즉시 적용 가능하다.

- 3. H-size 미니배치 wOMP 알고리즘을 도입하여 센서 선택의 계산 효율성을 개선하면서도 재구성 정확성을 유지하였다.

- 4. 메모리 최적화 기법을 통해 벡터 문제의 블록 행렬 구조를 활용하였다.

- 5. 제안된 방법은 잡음이 없는 조건에서 높은 정확도와 10% 잡음 및 희소 측정에서도 강력한 성능을 보이며, 임상 심장 모델링 워크플로우에 통합될 잠재력을 입증하였다.

---

*Generated on 2025-09-20 02:47:51*