---
keywords:
  - Foundation Models
  - Transformer Architecture
  - Physics Foundation Model
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:43:41.467225",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Transformer Architecture",
    "Physics Foundation Model"
  ],
  "rejected_keywords": [
    "General Physics Transformer",
    "In-Context Learning"
  ],
  "similarity_scores": {
    "Foundation Models": 0.8,
    "Transformer Architecture": 0.82,
    "Physics Foundation Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Towards a Physics Foundation Model

**Korean Title:** 물리학 기초 모델을 향하여

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer Architecture]]
**⚡ Unique Technical**: [[keywords/Physics Foundation Model|Physics Foundation Model]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Foundation Models]]

## 🔗 유사한 논문
- [[An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (80.8% similar)
- [[ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (79.4% similar)
- [[Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator_20250917|Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator]] (78.9% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (78.1% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (77.7% similar)

## 📋 저자 정보

**Authors:** Florian Wiesner, Matthias Wessling, Stephen Baek

## 📄 Abstract (원문)

Foundation models have revolutionized natural language processing through a
``train once, deploy anywhere'' paradigm, where a single pre-trained model
adapts to countless downstream tasks without retraining. Access to a Physics
Foundation Model (PFM) would be transformative -- democratizing access to
high-fidelity simulations, accelerating scientific discovery, and eliminating
the need for specialized solver development. Yet current physics-aware machine
learning approaches remain fundamentally limited to single, narrow domains and
require retraining for each new system. We present the General Physics
Transformer (GPhyT), trained on 1.8 TB of diverse simulation data, that
demonstrates foundation model capabilities are achievable for physics. Our key
insight is that transformers can learn to infer governing dynamics from
context, enabling a single model to simulate fluid-solid interactions, shock
waves, thermal convection, and multi-phase dynamics without being told the
underlying equations. GPhyT achieves three critical breakthroughs: (1) superior
performance across multiple physics domains, outperforming specialized
architectures by up to 29x, (2) zero-shot generalization to entirely unseen
physical systems through in-context learning, and (3) stable long-term
predictions through 50-timestep rollouts. By establishing that a single model
can learn generalizable physical principles from data alone, this work opens
the path toward a universal PFM that could transform computational science and
engineering.

## 🔍 Abstract (한글 번역)

기초 모델은 "한 번 훈련하고 어디서나 배포한다"는 패러다임을 통해 자연어 처리를 혁신했습니다. 이 패러다임에서는 단일 사전 훈련된 모델이 재훈련 없이 수많은 다운스트림 작업에 적응합니다. 물리학 기초 모델(Physics Foundation Model, PFM)에 대한 접근은 고품질 시뮬레이션에 대한 접근을 민주화하고, 과학적 발견을 가속화하며, 특수한 해법 개발의 필요성을 제거함으로써 변혁적일 것입니다. 그러나 현재의 물리학 인식 기계 학습 접근법은 근본적으로 단일하고 좁은 도메인에 제한되며, 각 새로운 시스템에 대해 재훈련이 필요합니다. 우리는 1.8TB의 다양한 시뮬레이션 데이터로 훈련된 일반 물리학 변환기(General Physics Transformer, GPhyT)를 소개하며, 이를 통해 물리학에서도 기초 모델의 역량이 달성 가능하다는 것을 보여줍니다. 우리의 핵심 통찰은 변환기가 맥락에서 지배적인 역학을 추론하는 것을 학습할 수 있으며, 이를 통해 단일 모델이 기본 방정식을 알려주지 않고도 유체-고체 상호작용, 충격파, 열 대류 및 다상 역학을 시뮬레이션할 수 있다는 것입니다. GPhyT는 세 가지 중요한 돌파구를 달성했습니다: (1) 여러 물리학 도메인에서의 우수한 성능으로, 특수 아키텍처보다 최대 29배 더 우수한 성능을 보입니다, (2) 맥락 학습을 통해 완전히 보지 못한 물리적 시스템에 대한 제로샷 일반화, (3) 50-타임스텝 롤아웃을 통한 안정적인 장기 예측. 단일 모델이 데이터만으로 일반화 가능한 물리적 원리를 학습할 수 있음을 입증함으로써, 이 연구는 계산 과학 및 공학을 변혁할 수 있는 보편적 PFM으로 가는 길을 열었습니다.

## 📝 요약

이 논문은 물리학 분야에서 기초 모델의 가능성을 보여주는 General Physics Transformer (GPhyT)를 소개합니다. GPhyT는 1.8TB의 다양한 시뮬레이션 데이터를 학습하여, 물리학의 여러 분야에서 뛰어난 성능을 발휘하며, 특정 시스템에 대한 재학습 없이도 다양한 물리 시스템을 시뮬레이션할 수 있습니다. 주요 기여는 다음과 같습니다: (1) 여러 물리학 분야에서 최대 29배 뛰어난 성능을 보임, (2) 새로운 물리 시스템에 대한 제로샷 일반화, (3) 50단계 롤아웃을 통한 안정적인 장기 예측. 이 연구는 데이터만으로 일반화 가능한 물리 원리를 학습할 수 있는 단일 모델의 가능성을 제시하며, 물리학 기초 모델 개발의 길을 열었습니다.

## 🎯 주요 포인트

- 1. GPhyT는 다양한 물리 시뮬레이션 데이터를 학습하여 물리 분야에서도 파운데이션 모델의 가능성을 입증했습니다.

- 2. 이 모델은 맥락을 통해 지배적인 동역학을 추론할 수 있어, 다양한 물리적 상호작용을 단일 모델로 시뮬레이션할 수 있습니다.

- 3. GPhyT는 여러 물리 분야에서 최대 29배 성능 향상을 이루며, 특화된 아키텍처를 능가하는 성과를 보였습니다.

- 4. 새로운 물리 시스템에 대한 제로샷 일반화를 통해, 사전 학습 없이도 새로운 시스템에 적용할 수 있습니다.

- 5. 50단계 롤아웃을 통한 안정적인 장기 예측을 가능하게 하여, 범용 물리 파운데이션 모델의 가능성을 열었습니다.

---

*Generated on 2025-09-20 09:31:25*