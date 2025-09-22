# Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks

**Korean Title:** 양자 변분 활성화 함수가 콜모고로프-아르놀드 네트워크를 강화하다

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Jiun-Cheng Jiang|Jiun-Cheng Jiang]] [[authors/Morris Yu-Chao Huang|Morris Yu-Chao Huang]] [[authors/Tianlong Chen|Tianlong Chen]] [[authors/Hsi-Sheng Goan|Hsi-Sheng Goan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Quantum Inspired Kolmogorov Arnold Networks

## 🔗 유사한 논문
- [[Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (83.0% similar)
- [[Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (81.1% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (80.9% similar)
- [[Efficiently learning depth-3 circuits via quantum agnostic boosting_20250917|Efficiently learning depth-3 circuits via quantum agnostic boosting]] (80.4% similar)
- [[TITAN_ A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE_20250918|TITAN A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE]] (78.5% similar)

## 📋 저자 정보

**Authors:** Jiun-Cheng Jiang, Morris Yu-Chao Huang, Tianlong Chen, Hsi-Sheng Goan

## 📄 Abstract (원문)

Variational quantum circuits (VQCs) are central to quantum machine learning,
while recent progress in Kolmogorov-Arnold networks (KANs) highlights the power
of learnable activation functions. We unify these directions by introducing
quantum variational activation functions (QVAFs), realized through single-qubit
data re-uploading circuits called DatA Re-Uploading ActivatioNs (DARUANs). We
show that DARUAN with trainable weights in data pre-processing possesses an
exponentially growing frequency spectrum with data repetitions, enabling an
exponential reduction in parameter size compared with Fourier-based activations
without loss of expressivity. Embedding DARUAN into KANs yields
quantum-inspired KANs (QKANs), which retain the interpretability of KANs while
improving their parameter efficiency, expressivity, and generalization. We
further introduce two novel techniques to enhance scalability, feasibility and
computational efficiency, such as layer extension and hybrid QKANs (HQKANs) as
drop-in replacements of multi-layer perceptrons (MLPs) for feed-forward
networks in large-scale models. We provide theoretical analysis and extensive
experiments on function regression, image classification, and autoregressive
generative language modeling, demonstrating the efficiency and scalability of
QKANs. DARUANs and QKANs offer a promising direction for advancing quantum
machine learning on both noisy intermediate-scale quantum (NISQ) hardware and
classical quantum simulators.

## 🔍 Abstract (한글 번역)

변분 양자 회로(VQCs)는 양자 기계 학습의 중심에 있으며, 최근 콜모고로프-아르놀드 네트워크(KANs)의 발전은 학습 가능한 활성화 함수의 강력함을 강조합니다. 우리는 단일 큐빗 데이터 재업로드 회로인 데이터 재업로드 활성화(DARUANs)를 통해 양자 변분 활성화 함수(QVAFs)를 도입하여 이러한 방향을 통합합니다. 데이터 전처리에서 학습 가능한 가중치를 가진 DARUAN은 데이터 반복과 함께 지수적으로 증가하는 주파수 스펙트럼을 가지며, 이는 표현력을 잃지 않으면서도 푸리에 기반 활성화에 비해 매개변수 크기를 지수적으로 줄일 수 있게 합니다. DARUAN을 KANs에 내장하면 양자 영감을 받은 KANs(QKANs)가 생성되며, 이는 KANs의 해석 가능성을 유지하면서 매개변수 효율성, 표현력 및 일반화를 개선합니다. 우리는 또한 확장성, 실행 가능성 및 계산 효율성을 향상시키기 위한 두 가지 새로운 기술을 소개합니다. 예를 들어, 대규모 모델의 피드포워드 네트워크에서 다층 퍼셉트론(MLPs)을 대체할 수 있는 계층 확장 및 하이브리드 QKANs(HQKANs) 등이 있습니다. 우리는 함수 회귀, 이미지 분류 및 자기회귀 생성 언어 모델링에 대한 이론적 분석과 광범위한 실험을 제공하여 QKANs의 효율성과 확장성을 입증합니다. DARUANs와 QKANs는 소음이 있는 중간 규모 양자(NISQ) 하드웨어와 고전적인 양자 시뮬레이터 모두에서 양자 기계 학습을 발전시키기 위한 유망한 방향을 제공합니다.

## 📝 요약

이 논문은 양자 기계 학습의 핵심인 변분 양자 회로(VQC)와 학습 가능한 활성화 함수의 강점을 가진 Kolmogorov-Arnold 네트워크(KAN)를 통합하여, 양자 변분 활성화 함수(QVAF)를 소개합니다. 이는 단일 큐빗 데이터 재업로드 회로인 DARUAN을 통해 구현됩니다. DARUAN은 데이터 전처리에서 학습 가능한 가중치를 사용하여, 데이터 반복 시 지수적으로 증가하는 주파수 스펙트럼을 가지며, Fourier 기반 활성화 함수와 비교해 매개변수 크기를 지수적으로 줄일 수 있습니다. DARUAN을 KAN에 통합한 QKAN은 KAN의 해석 가능성을 유지하면서 매개변수 효율성, 표현력, 일반화를 향상시킵니다. 또한, 대규모 모델에서 다층 퍼셉트론(MLP)을 대체할 수 있는 레이어 확장 및 하이브리드 QKAN(HQKAN) 기술을 도입하여 확장성과 계산 효율성을 높였습니다. 이론적 분석과 함수 회귀, 이미지 분류, 자기회귀 생성 언어 모델링에 대한 실험을 통해 QKAN의 효율성과 확장성을 입증하였습니다. DARUAN과 QKAN은 NISQ 하드웨어 및 고전적 양자 시뮬레이터에서 양자 기계 학습을 발전시킬 유망한 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 양자 변분 활성 함수(QVAFs)는 단일 큐비트 데이터 재업로드 회로를 통해 구현되어 매개변수 크기를 지수적으로 줄이면서도 표현력을 유지합니다.

- 2. DARUAN을 Kolmogorov-Arnold 네트워크(KANs)에 삽입하면 해석 가능성을 유지하면서 매개변수 효율성, 표현력, 일반화를 개선하는 QKANs를 형성합니다.

- 3. QKANs는 대규모 모델의 피드포워드 네트워크에서 다층 퍼셉트론(MLP)을 대체할 수 있는 확장성, 실현 가능성 및 계산 효율성을 향상시키는 레이어 확장 및 하이브리드 QKANs(HQKANs) 기술을 도입합니다.

- 4. DARUANs와 QKANs는 NISQ 하드웨어와 고전적 양자 시뮬레이터 모두에서 양자 기계 학습을 발전시키기 위한 유망한 방향을 제시합니다.

- 5. 이론적 분석과 함수 회귀, 이미지 분류, 자기 회귀 생성 언어 모델링에 대한 광범위한 실험을 통해 QKANs의 효율성과 확장성을 입증합니다.

---

*Generated on 2025-09-20 09:17:06*