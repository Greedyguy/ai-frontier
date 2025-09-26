---
keywords:
  - Variational Quantum Eigensolver
  - Barren Plateaus
  - Deep Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:07:06.321139",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Quantum Eigensolver",
    "Barren Plateaus",
    "Deep Learning"
  ],
  "rejected_keywords": [
    "Transverse-Field Ising Models"
  ],
  "similarity_scores": {
    "Variational Quantum Eigensolver": 0.85,
    "Barren Plateaus": 0.8,
    "Deep Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# TITAN: A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE

**Korean Title:** TITAN: 대규모 VQE에서 적응형 매개변수 동결을 위한 궤적 정보 기반 기법

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|deep learning framework]]
**⚡ Unique Technical**: [[keywords/Variational Quantum Eigensolver|Variational Quantum Eigensolver]], [[keywords/Barren Plateaus|barren plateaus]]

## 🔗 유사한 논문
- [[Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.8% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (78.6% similar)
- [[QLook_Quantum-Driven Viewport Prediction for Virtual Reality_20250919|QLookQuantum-Driven Viewport Prediction for Virtual Reality]] (77.3% similar)
- [[eIQ Neutron_ Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations_20250919|eIQ Neutron Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations]] (76.3% similar)
- [[MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (75.9% similar)

## 📋 저자 정보

**Authors:** Yifeng Peng, Xinyi Li, Samuel Yen-Chi Chen, Kaining Zhang, Zhiding Liang, Ying Wang, Yuxuan Du

## 📄 Abstract (원문)

Variational quantum Eigensolver (VQE) is a leading candidate for harnessing
quantum computers to advance quantum chemistry and materials simulations, yet
its training efficiency deteriorates rapidly for large Hamiltonians. Two issues
underlie this bottleneck: (i) the no-cloning theorem imposes a linear growth in
circuit evaluations with the number of parameters per gradient step; and (ii)
deeper circuits encounter barren plateaus (BPs), leading to exponentially
increasing measurement overheads. To address these challenges, here we propose
a deep learning framework, dubbed Titan, which identifies and freezes inactive
parameters of a given ansatze at initialization for a specific class of
Hamiltonians, reducing the optimization overhead without sacrificing accuracy.
The motivation of Titan starts with our empirical findings that a subset of
parameters consistently has a negligible influence on training dynamics. Its
design combines a theoretically grounded data construction strategy, ensuring
each training example is informative and BP-resilient, with an adaptive neural
architecture that generalizes across ansatze of varying sizes. Across benchmark
transverse-field Ising models, Heisenberg models, and multiple molecule systems
up to 30 qubits, Titan achieves up to 3 times faster convergence and 40% to 60%
fewer circuit evaluations than state-of-the-art baselines, while matching or
surpassing their estimation accuracy. By proactively trimming parameter space,
Titan lowers hardware demands and offers a scalable path toward utilizing VQE
to advance practical quantum chemistry and materials science.

## 🔍 Abstract (한글 번역)

변분 양자 고유값 솔버(VQE)는 양자 컴퓨터를 활용하여 양자 화학 및 재료 시뮬레이션을 발전시키기 위한 유력한 후보이지만, 큰 해밀토니안에 대해서는 학습 효율성이 급격히 저하됩니다. 이 병목 현상의 두 가지 주요 원인은 다음과 같습니다: (i) 복제 불가능 정리에 의해 매개변수당 기울기 단계에서 회로 평가가 선형적으로 증가하며, (ii) 더 깊은 회로는 불모의 고원(Barren Plateaus, BP)에 직면하여 측정 오버헤드가 지수적으로 증가합니다. 이러한 문제를 해결하기 위해, 우리는 특정 해밀토니안 클래스에 대해 초기화 시 주어진 앤사츠의 비활성 매개변수를 식별하고 고정하는 딥러닝 프레임워크인 Titan을 제안합니다. 이는 정확성을 희생하지 않고 최적화 오버헤드를 줄입니다. Titan의 동기는 학습 동역학에 일관되게 미미한 영향을 미치는 매개변수의 하위 집합이 있다는 우리의 경험적 발견에서 시작됩니다. Titan의 설계는 이론적으로 근거 있는 데이터 구성 전략을 결합하여 각 학습 예제가 정보성이 있고 BP에 강하도록 하며, 다양한 크기의 앤사츠에 걸쳐 일반화할 수 있는 적응형 신경 아키텍처를 제공합니다. 기준 횡장 이징 모델, 하이젠베르크 모델 및 최대 30 큐빗의 여러 분자 시스템에 걸쳐, Titan은 최첨단 기준선보다 최대 3배 빠른 수렴 속도와 40%에서 60% 적은 회로 평가를 달성하며, 그들의 추정 정확성과 맞먹거나 이를 능가합니다. 매개변수 공간을 사전에 줄임으로써, Titan은 하드웨어 요구 사항을 낮추고 VQE를 활용하여 실용적인 양자 화학 및 재료 과학을 발전시키기 위한 확장 가능한 경로를 제공합니다.

## 📝 요약

Variational Quantum Eigensolver(VQE)는 양자 화학 및 재료 시뮬레이션을 위한 유망한 방법이지만, 큰 해밀토니안에서는 효율성이 저하됩니다. 이러한 문제를 해결하기 위해, 본 연구에서는 Titan이라는 딥러닝 프레임워크를 제안합니다. Titan은 초기화 단계에서 비활성 매개변수를 식별하고 고정하여 최적화 부담을 줄이면서도 정확성을 유지합니다. 이 방법은 매개변수 중 일부가 훈련에 거의 영향을 미치지 않는다는 경험적 발견에서 출발하였습니다. Titan은 정보가 풍부하고 BP에 강한 데이터를 생성하는 전략과 다양한 크기의 ansatze에 일반화 가능한 적응형 신경망 구조를 결합합니다. 실험 결과, Titan은 최대 3배 빠른 수렴 속도와 40%에서 60% 적은 회로 평가 횟수를 달성하며, 기존 방법들과 동등하거나 더 나은 정확성을 보였습니다. Titan은 매개변수 공간을 능동적으로 줄여 하드웨어 요구를 낮추고, VQE를 활용한 실용적인 양자 화학 및 재료 과학 발전의 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. Variational quantum Eigensolver(VQE)의 효율성 문제를 해결하기 위해 Titan이라는 딥러닝 프레임워크를 제안합니다.

- 2. Titan은 초기화 단계에서 비활성 매개변수를 식별하고 고정하여 최적화 오버헤드를 줄입니다.

- 3. Titan은 정보성이 높고 barren plateaus(BP)에 강한 학습 예제를 생성하는 데이터 구성 전략을 사용합니다.

- 4. Titan은 다양한 크기의 ansatze에 일반화 가능한 적응형 신경망 구조를 결합하여 최대 3배 빠른 수렴 속도를 달성합니다.

- 5. Titan은 최대 30 큐빗의 다양한 모델에서 기존 최첨단 기법보다 40%에서 60% 적은 회로 평가를 통해 정확도를 유지하거나 초과합니다.

---

*Generated on 2025-09-20 00:52:57*