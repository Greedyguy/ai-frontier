---
keywords:
  - Quantum Machine Learning
  - Variational Quantum Circuit
  - AC Power Flow
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.03495
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:22:32.200378",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Machine Learning",
    "Variational Quantum Circuit",
    "AC Power Flow"
  ],
  "rejected_keywords": [
    "Hybrid Classical/Quantum Computing"
  ],
  "similarity_scores": {
    "Quantum Machine Learning": 0.79,
    "Variational Quantum Circuit": 0.78,
    "AC Power Flow": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit

**Korean Title:** 데이터 의존적 변분 양자 회로를 사용한 교류 전력 흐름 솔루션 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Variational Quantum Circuit|Variational Quantum Circuit]], [[keywords/AC Power Flow|AC Power Flow]]
**🚀 Evolved Concepts**: [[keywords/Quantum Machine Learning|Quantum Machine Learning]]

## 🔗 유사한 논문
- [[Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (81.7% similar)
- [[Learning quantum many-body data locally: A provably scalable framework]] (80.4% similar)
- [[From Distributional to Quantile Neural Basis Models: the case of Electricity Price Forecasting]] (79.7% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.7% similar)
- [[Post-Hoc_Split-Point_Self-Consistency_Verification_for_Efficient,_Unified_Quantification_of_Aleatoric_and_Epistemic_Uncertainty_in_Deep_Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (77.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.03495v2 Announce Type: replace-cross 
Abstract: Interconnection studies require solving numerous instances of the AC load or power flow (AC PF) problem to simulate diverse scenarios as power systems navigate the ongoing energy transition. To expedite such studies, this work leverages recent advances in quantum computing to find or predict AC PF solutions using a variational quantum circuit (VQC). VQCs are trainable models that run on modern-day noisy intermediate-scale quantum (NISQ) hardware to accomplish elaborate optimization and machine learning (ML) tasks. Our first contribution is to pose a single instance of the AC PF as a nonlinear least-squares fit over the VQC trainable parameters (weights) and solve it using a hybrid classical/quantum computing approach. The second contribution is to feed PF specifications as features into a data-embedded VQC and train the resultant quantum ML (QML) model to predict general PF solutions. The third contribution is to develop a novel protocol to efficiently measure AC-PF quantum observables by exploiting the graph structure of a power network. Preliminary numerical tests indicate that the proposed VQC models attain enhanced prediction performance over a deep neural network despite using much fewer weights. The proposed quantum AC-PF framework sets the foundations for addressing more elaborate grid tasks via quantum computing.

## 🔍 Abstract (한글 번역)

arXiv:2509.03495v2 발표 유형: replace-cross
요약: 상호연결 연구는 전력 시스템이 지속적인 에너지 전환을 탐색하는 동안 다양한 시나리오를 시뮬레이션하기 위해 국부 또는 전력 흐름 (AC PF) 문제의 다수 인스턴스를 해결해야 합니다. 이러한 연구를 가속화하기 위해 본 연구는 양자 컴퓨팅의 최근 발전을 활용하여 변분 양자 회로 (VQC)를 사용하여 AC PF 솔루션을 찾거나 예측합니다. VQC는 현대의 소음 중간 규모 양자 (NISQ) 하드웨어에서 실행되는 학습 가능한 모델로, 복잡한 최적화 및 기계 학습 (ML) 작업을 수행합니다. 첫 번째 기여는 AC PF의 단일 인스턴스를 VQC 학습 가능한 매개변수 (가중치)에 대한 비선형 최소 제곱 적합으로 제시하고 하이브리드 고전적/양자 컴퓨팅 접근법을 사용하여 해결하는 것입니다. 두 번째 기여는 PF 사양을 특징으로 사용하여 데이터 포함 VQC에 공급하고 결과 양자 ML (QML) 모델을 훈련하여 일반적인 PF 솔루션을 예측하는 것입니다. 세 번째 기여는 전력망의 그래프 구조를 활용하여 AC-PF 양자 관측값을 효율적으로 측정하기 위한 새로운 프로토콜을 개발하는 것입니다. 초기적인 수치 실험 결과, 제안된 VQC 모델이 훨씬 적은 가중치를 사용하더라도 심층 신경망보다 향상된 예측 성능을 달성한다는 것을 보여줍니다. 제안된 양자 AC-PF 프레임워크는 양자 컴퓨팅을 통해 보다 복잡한 그리드 작업을 다루기 위한 기초를 마련합니다.

## 📝 요약

본 연구는 전력 시스템이 지속적인 에너지 전환을 경유하는 동안 다양한 시나리오를 시뮬레이션하기 위해 교차 연결 연구가 필요하다. 이를 가속화하기 위해 본 연구는 양자 컴퓨팅의 최근 발전을 활용하여 변분 양자 회로(VQC)를 사용하여 AC 전력 흐름 문제를 해결하거나 예측한다. VQC는 현대의 소음 중간 규모 양자(NISQ) 하드웨어에서 실행되는 학습 가능한 모델로, 복잡한 최적화 및 기계 학습(ML) 작업을 수행한다. 본 연구의 주요 기여는 AC 전력 흐름의 단일 인스턴스를 VQC 학습 가능 매개변수(가중치)에 대한 비선형 최소 제곱 적합으로 제시하고 하이브리드 고전적/양자 컴퓨팅 접근법을 사용하여 해결하는 것이다. 두 번째 기여는 PF 사양을 특징으로 사용하여 데이터 포함 VQC에 공급하고 결과적인 양자 ML(QML) 모델을 훈련시켜 일반 PF 솔루션을 예측하는 것이다. 세 번째 기여는 전력 네트워크의 그래프 구조를 활용하여 AC-PF 양자 관측값을 효율적으로 측정하는 새로운 프로토콜을 개발하는 것이다. 초기 수치 실험 결과, 제안된 VQC 모델이 훨씬 적은 가중치를 사용하더라도 심층 신경망보다 향상된 예측 성능을 달성한다. 제안된 양자 AC-PF 프레임워크는 양자 컴퓨팅을 통해 보다 복잡한 그리드 작업을 다루기 위한 기초를 마련한다.

## 🎯 주요 포인트

- 1. 전력 시스템이 에너지 전환을 진행하는 동안 다양한 시나리오를 시뮬레이션하기 위해 AC 전력 흐름 문제를 해결하는 데 양자 컴퓨팅을 활용한다.

- 2. AC 전력 흐름 문제를 비선형 최소 자승 문제로 제시하고 하이브리드 고전적/양자 컴퓨팅 방식으로 해결한다.

- 3. 전력 네트워크의 그래프 구조를 활용하여 AC-PF 양자 관측값을 효율적으로 측정하는 새로운 프로토콜을 개발한다.

---

*Generated on 2025-09-18 16:49:59*