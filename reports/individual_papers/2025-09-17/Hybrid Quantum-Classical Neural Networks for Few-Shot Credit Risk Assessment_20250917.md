---
keywords:
  - Neural Networks
  - Hybrid Quantum-Classical Systems
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:53:21.815733",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Networks",
    "Hybrid Quantum-Classical Systems",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [
    "Quantum Machine Learning"
  ],
  "similarity_scores": {
    "Neural Networks": 0.82,
    "Hybrid Quantum-Classical Systems": 0.77,
    "Few-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment

**Korean Title:** 하이브리드 양자-고전 신경망을 이용한 소수 샷 신용 위험 평가

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Quantum Neural Network]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Credit Risk Assessment]]
**🚀 Evolved Concepts**: [[keywords/Hybrid Quantum-Classical Systems|Hybrid Quantum-Classical Workflow]]

## 🔗 유사한 논문
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (82.2% similar)
- [[Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (82.1% similar)
- [[Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (81.5% similar)
- [[Synthesizing Behaviorally-Grounded Reasoning Chains_ A Data-Generation Framework for Personal Finance LLMs_20250917|Synthesizing Behaviorally-Grounded Reasoning Chains A Data-Generation Framework for Personal Finance LLMs]] (80.9% similar)
- [[QLook_Quantum-Driven Viewport Prediction for Virtual Reality_20250919|QLookQuantum-Driven Viewport Prediction for Virtual Reality]] (80.3% similar)

## 📋 저자 정보

**Authors:** Zheng-an Wang, Yanbo J. Wang, Jiachi Zhang, Qi Xu, Yilun Zhao, Jintao Li, Yipeng Zhang, Bo Yang, Xinkai Gao, Xiaofeng Cao, Kai Xu, Pengpeng Hao, Xuan Yang, Heng Fan

## 📄 Abstract (원문)

Quantum Machine Learning (QML) offers a new paradigm for addressing complex
financial problems intractable for classical methods. This work specifically
tackles the challenge of few-shot credit risk assessment, a critical issue in
inclusive finance where data scarcity and imbalance limit the effectiveness of
conventional models. To address this, we design and implement a novel hybrid
quantum-classical workflow. The methodology first employs an ensemble of
classical machine learning models (Logistic Regression, Random Forest, XGBoost)
for intelligent feature engineering and dimensionality reduction. Subsequently,
a Quantum Neural Network (QNN), trained via the parameter-shift rule, serves as
the core classifier. This framework was evaluated through numerical simulations
and deployed on the Quafu Quantum Cloud Platform's ScQ-P21 superconducting
processor. On a real-world credit dataset of 279 samples, our QNN achieved a
robust average AUC of 0.852 +/- 0.027 in simulations and yielded an impressive
AUC of 0.88 in the hardware experiment. This performance surpasses a suite of
classical benchmarks, with a particularly strong result on the recall metric.
This study provides a pragmatic blueprint for applying quantum computing to
data-constrained financial scenarios in the NISQ era and offers valuable
empirical evidence supporting its potential in high-stakes applications like
inclusive finance.

## 🔍 Abstract (한글 번역)

양자 기계 학습(QML)은 고전적 방법으로는 해결하기 어려운 복잡한 금융 문제를 해결하기 위한 새로운 패러다임을 제공합니다. 본 연구는 특히 데이터 부족과 불균형으로 인해 기존 모델의 효과가 제한되는 포용적 금융에서의 중요한 문제인 소수 샷 신용 위험 평가의 도전에 초점을 맞추고 있습니다. 이를 해결하기 위해, 우리는 새로운 하이브리드 양자-고전적 워크플로우를 설계하고 구현했습니다. 이 방법론은 먼저 로지스틱 회귀, 랜덤 포레스트, XGBoost와 같은 고전적 기계 학습 모델의 앙상블을 사용하여 지능적인 특징 공학과 차원 축소를 수행합니다. 그 후, 매개변수 이동 규칙을 통해 훈련된 양자 신경망(QNN)이 핵심 분류기로 작동합니다. 이 프레임워크는 수치 시뮬레이션을 통해 평가되었으며, Quafu Quantum Cloud Platform의 ScQ-P21 초전도 프로세서에서 구현되었습니다. 279개의 샘플로 구성된 실제 신용 데이터셋에서, 우리의 QNN은 시뮬레이션에서 평균 AUC 0.852 +/- 0.027을 달성했으며, 하드웨어 실험에서는 인상적인 AUC 0.88을 기록했습니다. 이 성능은 특히 재현율 지표에서 강력한 결과를 보이며, 고전적 벤치마크를 능가합니다. 본 연구는 NISQ 시대의 데이터 제약 금융 시나리오에 양자 컴퓨팅을 적용하기 위한 실용적인 청사진을 제공하며, 포용적 금융과 같은 고위험 응용 분야에서의 잠재력을 뒷받침하는 귀중한 실증적 증거를 제공합니다.

## 📝 요약

이 연구는 양자 기계 학습(QML)을 활용하여 전통적 방법으로는 해결하기 어려운 금융 문제, 특히 데이터 부족과 불균형으로 인해 기존 모델의 효과가 제한되는 포용 금융의 소액 신용 위험 평가 문제를 다룹니다. 이를 위해 새로운 하이브리드 양자-고전 워크플로를 설계하고 구현했습니다. 먼저 로지스틱 회귀, 랜덤 포레스트, XGBoost 등 고전적 기계 학습 모델을 사용하여 특징 공학과 차원 축소를 수행한 후, 양자 신경망(QNN)을 핵심 분류기로 사용합니다. 이 프레임워크는 수치 시뮬레이션과 Quafu Quantum Cloud Platform의 ScQ-P21 초전도 프로세서를 통해 평가되었습니다. 279개의 실제 신용 데이터셋에서 QNN은 시뮬레이션에서 평균 AUC 0.852 +/- 0.027을, 하드웨어 실험에서는 AUC 0.88을 기록하며, 기존의 고전적 벤치마크를 능가하는 성과를 보였습니다. 이 연구는 NISQ 시대의 데이터 제약 금융 시나리오에 양자 컴퓨팅을 적용하는 실용적 청사진을 제공하며, 포용 금융과 같은 고위험 응용 분야에서의 잠재력을 입증합니다.

## 🎯 주요 포인트

- 1. 양자 기계 학습(QML)은 복잡한 금융 문제를 해결하기 위한 새로운 패러다임을 제공합니다.

- 2. 본 연구는 데이터 부족과 불균형 문제를 해결하기 위해 하이브리드 양자-고전 워크플로우를 설계 및 구현했습니다.

- 3. 고전적 기계 학습 모델을 활용한 지능형 특징 공학 및 차원 축소 후, 양자 신경망(QNN)을 핵심 분류기로 사용합니다.

- 4. 실제 신용 데이터셋에서 QNN은 시뮬레이션에서 평균 AUC 0.852 +/- 0.027, 하드웨어 실험에서 AUC 0.88을 기록했습니다.

- 5. 본 연구는 NISQ 시대의 데이터 제약 금융 시나리오에 양자 컴퓨팅을 적용하기 위한 실용적인 청사진을 제공합니다.

---

*Generated on 2025-09-20 09:30:58*