---
keywords:
  - Tensor Atomic Cluster Expansion
  - Tensor Moment Potential
  - Latent Ewald Summation
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:04:03.530446",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tensor Atomic Cluster Expansion",
    "Tensor Moment Potential",
    "Latent Ewald Summation"
  ],
  "rejected_keywords": [
    "Machine Learning"
  ],
  "similarity_scores": {
    "Tensor Atomic Cluster Expansion": 0.8,
    "Tensor Moment Potential": 0.75,
    "Latent Ewald Summation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Towards universal property prediction in Cartesian space: TACE is all you need

**Korean Title:** 카르테시안 공간에서의 보편적 특성 예측을 향하여: TACE가 당신에게 필요한 전부입니다.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Tensor Atomic Cluster Expansion|Tensor Atomic Cluster Expansion]], [[keywords/Tensor Moment Potential|Tensor Moment Potential]], [[keywords/Latent Ewald Summation|Latent Ewald Summation]]

## 🔗 유사한 논문
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (79.3% similar)
- [[TITAN_ A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE_20250918|TITAN A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE]] (78.9% similar)
- [[STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (78.9% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (77.7% similar)
- [[Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (77.4% similar)

## 📋 저자 정보

**Authors:** Zemin Xu, Wenbo Xie, Daiqian Xie, P. Hu

## 📄 Abstract (원문)

Machine learning has revolutionized atomistic simulations and materials
science, yet current approaches often depend on spherical-harmonic
representations. Here we introduce the Tensor Atomic Cluster Expansion and
Tensor Moment Potential, the first unified framework formulated entirely in
Cartesian space for the systematic prediction of arbitrary structure-determined
tensorial properties. TACE achieves this by decomposing atomic environments
into a complete hierarchy of (irreducible) Cartesian tensors, ensuring
symmetry-consistent representations that naturally encode invariance and
equivariance constraints. Beyond geometry, TACE incorporates universal
embeddings that flexibly integrate diverse attributes including basis sets,
charges, magnetic moments and field perturbations. This allows explicit control
over external invariants and equivariants in the prediction process. Long-range
interactions are also accurately described through the Latent Ewald Summation
module within the short-range approximation, providing a rigorous yet
computationally efficient treatment of electrostatic interactions. We
demonstrate that TACE attains accuracy, stability, and efficiency on par with
or surpassing leading equivariant frameworks across finite molecules and
extended materials, including in-domain and out-of-domain benchmarks, spectra,
hessians, external-field response, charged systems, magnetic systems,
multi-fidelity training, and heterogeneous catalytic systems. Crucially, TACE
bridges scalar and tensorial modeling and establishes a Cartesian-space
paradigm that unifies and extends beyond the design space of
spherical-harmonic-based methods. This work lays the foundation for a new
generation of universal atomistic machine learning models capable of
systematically capturing the rich interplay of geometry, fields and material
properties within a single coherent framework.

## 🔍 Abstract (한글 번역)

기계 학습은 원자 수준의 시뮬레이션과 재료 과학을 혁신적으로 변화시켰지만, 현재의 접근 방식은 종종 구면 조화 표현에 의존합니다. 여기에서 우리는 Tensor Atomic Cluster Expansion(TACE)와 Tensor Moment Potential을 소개합니다. 이는 임의의 구조에 의해 결정되는 텐서적 특성을 체계적으로 예측하기 위해 전적으로 직교 좌표계에서 공식화된 최초의 통합 프레임워크입니다. TACE는 원자 환경을 (비가환) 직교 텐서의 완전한 계층 구조로 분해하여 대칭 일관성을 보장하는 표현을 통해 불변성과 동변성 제약 조건을 자연스럽게 인코딩합니다. 기하학을 넘어, TACE는 기저 집합, 전하, 자기 모멘트 및 필드 변동을 포함한 다양한 속성을 유연하게 통합하는 보편적 임베딩을 포함합니다. 이는 예측 과정에서 외부 불변성과 동변성에 대한 명시적 제어를 가능하게 합니다. 장거리 상호작용은 짧은 거리 근사 내에서 잠재적 에발드 합산 모듈을 통해 정확하게 설명되며, 이는 전기적 상호작용에 대한 엄밀하면서도 계산적으로 효율적인 처리를 제공합니다. 우리는 TACE가 유한 분자와 확장된 재료, 도메인 내 및 도메인 외 벤치마크, 스펙트럼, 헤시안, 외부 필드 반응, 전하 시스템, 자기 시스템, 다중 신뢰도 학습, 이종 촉매 시스템을 포함하여 주요 동변성 프레임워크와 동등하거나 그 이상의 정확성, 안정성 및 효율성을 달성함을 입증합니다. 중요한 것은 TACE가 스칼라 및 텐서 모델링을 연결하고 구면 조화 기반 방법의 설계 공간을 통합하고 확장하는 직교 좌표계 패러다임을 확립한다는 것입니다. 이 연구는 기하학, 필드 및 재료 특성의 풍부한 상호작용을 단일 일관된 프레임워크 내에서 체계적으로 포착할 수 있는 새로운 세대의 보편적 원자 수준 기계 학습 모델의 기초를 마련합니다.

## 📝 요약

이 논문은 기계 학습을 활용한 원자적 시뮬레이션 및 재료 과학에서의 혁신적인 접근법인 Tensor Atomic Cluster Expansion(TACE)와 Tensor Moment Potential을 소개합니다. 이 방법론은 기존의 구면 조화 표현 대신 완전히 직교 좌표계에서 작동하며, 구조에 의해 결정되는 다양한 텐서적 성질을 예측할 수 있는 통합된 틀을 제공합니다. TACE는 원자 환경을 직교 텐서로 분해하여 대칭성을 유지하며, 다양한 속성을 유연하게 통합할 수 있는 보편적 임베딩을 포함합니다. 또한, Latent Ewald Summation 모듈을 통해 장거리 상호작용을 정확히 설명합니다. TACE는 기존의 방법들과 비교하여 분자 및 확장된 재료의 다양한 벤치마크에서 높은 정확도와 효율성을 보여주며, 스칼라 및 텐서 모델링을 연결하는 새로운 패러다임을 제시합니다. 이 연구는 기하학, 장, 재료 특성의 복잡한 상호작용을 포괄하는 차세대 원자적 기계 학습 모델의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. Tensor Atomic Cluster Expansion(TACE)와 Tensor Moment Potential은 카르테시안 공간에서 구조에 의해 결정되는 텐서적 특성을 예측하는 통합 프레임워크를 제공합니다.

- 2. TACE는 원자 환경을 카르테시안 텐서로 분해하여 대칭 일관성을 유지하며 불변성과 동변성 제약을 자연스럽게 인코딩합니다.

- 3. TACE는 보편적 임베딩을 통해 기초 집합, 전하, 자기 모멘트 및 장 교란을 포함한 다양한 속성을 유연하게 통합합니다.

- 4. Latent Ewald Summation 모듈을 통해 장거리 상호작용을 정확하게 설명하며, 전기적 상호작용을 효율적으로 처리합니다.

- 5. TACE는 스펙트럼, 헤시안, 외부 필드 반응, 전하 및 자기 시스템 등 다양한 벤치마크에서 기존의 동변성 프레임워크와 동등하거나 그 이상의 정확도, 안정성, 효율성을 달성합니다.

---

*Generated on 2025-09-20 01:41:26*