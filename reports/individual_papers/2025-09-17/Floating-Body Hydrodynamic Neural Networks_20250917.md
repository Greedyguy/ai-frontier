---
keywords:
  - Floating-Body Hydrodynamic Neural Networks
  - Neural ODEs
  - Hamiltonian and Lagrangian Neural Networks
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:54:38.039961",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Floating-Body Hydrodynamic Neural Networks",
    "Neural ODEs",
    "Hamiltonian and Lagrangian Neural Networks"
  ],
  "rejected_keywords": [
    "Fluid-Structure Interaction"
  ],
  "similarity_scores": {
    "Floating-Body Hydrodynamic Neural Networks": 0.85,
    "Neural ODEs": 0.8,
    "Hamiltonian and Lagrangian Neural Networks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Floating-Body Hydrodynamic Neural Networks

**Korean Title:** 부체 유체역학 신경망

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural ODEs|Neural ODEs]], [[keywords/Hamiltonian and Lagrangian Neural Networks|Hamiltonian and Lagrangian neural networks]]
**⚡ Unique Technical**: [[keywords/Floating-Body Hydrodynamic Neural Networks|Floating-Body Hydrodynamic Neural Networks]]

## 🔗 유사한 논문
- [[A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (81.1% similar)
- [[An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (80.9% similar)
- [[Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (79.2% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (78.1% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (78.0% similar)

## 📋 저자 정보

**Authors:** Tianshuo Zhang, Wenzhe Zhai, Rui Yann, Jia Gao, He Cao, Xianglei Xing

## 📄 Abstract (원문)

Fluid-structure interaction is common in engineering and natural systems,
where floating-body motion is governed by added mass, drag, and background
flows. Modeling these dissipative dynamics is difficult: black-box neural
models regress state derivatives with limited interpretability and unstable
long-horizon predictions. We propose Floating-Body Hydrodynamic Neural Networks
(FHNN), a physics-structured framework that predicts interpretable hydrodynamic
parameters such as directional added masses, drag coefficients, and a
streamfunction-based flow, and couples them with analytic equations of motion.
This design constrains the hypothesis space, enhances interpretability, and
stabilizes integration. On synthetic vortex datasets, FHNN achieves up to an
order-of-magnitude lower error than Neural ODEs, recovers physically consistent
flow fields. Compared with Hamiltonian and Lagrangian neural networks, FHNN
more effectively handles dissipative dynamics while preserving
interpretability, which bridges the gap between black-box learning and
transparent system identification.

## 🔍 Abstract (한글 번역)

유체-구조 상호작용은 공학 및 자연 시스템에서 흔히 발생하며, 부유체의 운동은 부가 질량, 항력, 그리고 배경 흐름에 의해 지배됩니다. 이러한 소산적 동역학을 모델링하는 것은 어렵습니다. 블랙박스 신경망 모델은 상태 도함수를 회귀하지만 해석 가능성이 제한적이며 장기 예측이 불안정합니다. 우리는 해석 가능한 유체역학적 매개변수(방향성 부가 질량, 항력 계수, 스트림 함수 기반의 흐름 등)를 예측하고 이를 운동 방정식과 결합하는 물리 구조적 프레임워크인 부유체 유체역학 신경망(FHNN)을 제안합니다. 이 설계는 가설 공간을 제한하고 해석 가능성을 높이며 통합을 안정화합니다. 합성 와류 데이터셋에서 FHNN은 신경 ODE보다 최대 한 자릿수 낮은 오류를 달성하고 물리적으로 일관된 흐름장을 복원합니다. 해밀토니안 및 라그랑지안 신경망과 비교할 때, FHNN은 해석 가능성을 유지하면서 소산적 동역학을 보다 효과적으로 처리하여 블랙박스 학습과 투명한 시스템 식별 간의 격차를 해소합니다.

## 📝 요약

이 논문은 공학 및 자연 시스템에서의 유체-구조 상호작용을 다루며, 부체의 운동을 예측하는 새로운 방법론인 부체 유체역학 신경망(FHNN)을 제안합니다. FHNN은 방향성 부가 질량, 항력 계수, 흐름 함수 기반의 유동을 예측하며, 이를 운동 방정식과 결합하여 해석 가능성을 높이고 예측의 안정성을 강화합니다. 합성 소용돌이 데이터셋에서 FHNN은 기존의 신경 ODE보다 최대 10배 낮은 오류를 기록하며, 물리적으로 일관된 유동장을 복원합니다. FHNN은 해밀토니안 및 라그랑지안 신경망보다 소산적 동역학을 효과적으로 처리하면서도 해석 가능성을 유지하여 블랙박스 학습과 투명한 시스템 식별 간의 격차를 줄입니다.

## 🎯 주요 포인트

- 1. FHNN은 방향성 부가 질량, 항력 계수, 스트림 함수 기반 흐름 등 해석 가능한 수치 예측을 통해 물리적 구조를 갖춘 프레임워크를 제공합니다.

- 2. FHNN은 해석 가능한 운동 방정식과 결합하여 가설 공간을 제한하고 해석 가능성을 높이며 통합의 안정성을 강화합니다.

- 3. 합성 소용돌이 데이터셋에서 FHNN은 Neural ODEs보다 최대 한 자릿수 낮은 오류를 달성하고 물리적으로 일관된 흐름 필드를 복원합니다.

- 4. FHNN은 해밀토니안 및 라그랑지안 신경망과 비교하여 해석 가능성을 유지하면서 소산 동역학을 더 효과적으로 처리합니다.

- 5. FHNN은 블랙박스 학습과 투명한 시스템 식별 간의 격차를 해소합니다.

---

*Generated on 2025-09-20 09:33:20*