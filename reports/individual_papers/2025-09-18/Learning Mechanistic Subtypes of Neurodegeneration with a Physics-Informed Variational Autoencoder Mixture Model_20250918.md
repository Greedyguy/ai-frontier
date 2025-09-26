---
keywords:
  - Generative Models
  - Neurodegenerative Disease Subtypes
  - Physics-Informed Machine Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:22:17.193970",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Models",
    "Neurodegenerative Disease Subtypes",
    "Physics-Informed Machine Learning"
  ],
  "rejected_keywords": [
    "Partial Differential Equations"
  ],
  "similarity_scores": {
    "Generative Models": 0.8,
    "Neurodegenerative Disease Subtypes": 0.78,
    "Physics-Informed Machine Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model

**Korean Title:** 신경퇴행성 질환의 기계적 아형 학습을 위한 물리 기반 변분 오토인코더 혼합 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generative Models|Variational Autoencoder Mixture Model]]
**⚡ Unique Technical**: [[keywords/Neurodegenerative Disease Subtypes|Neurodegenerative Disease Subtypes]], [[keywords/Physics-Informed Machine Learning|Physics-Informed Machine Learning]]

## 🔗 유사한 논문
- [[Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2 Atypical Mitosis Classification]] (81.7% similar)
- [[Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease_20250918|Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease]] (80.6% similar)
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (80.5% similar)
- [[Scattering approach to diffusion quantifies axonal damage in brain injury_20250918|Scattering approach to diffusion quantifies axonal damage in brain injury]] (79.7% similar)
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (79.7% similar)

## 📋 저자 정보

**Authors:** Sanduni Pinnawala, Annabelle Hartanto, Ivor J. A. Simpson, Peter A. Wijeratne

## 📄 Abstract (원문)

Modelling the underlying mechanisms of neurodegenerative diseases demands
methods that capture heterogeneous and spatially varying dynamics from sparse,
high-dimensional neuroimaging data. Integrating partial differential equation
(PDE) based physics knowledge with machine learning provides enhanced
interpretability and utility over classic numerical methods. However, current
physics-integrated machine learning methods are limited to considering a single
PDE, severely limiting their application to diseases where multiple mechanisms
are responsible for different groups (i.e., subtypes) and aggravating problems
with model misspecification and degeneracy. Here, we present a deep generative
model for learning mixtures of latent dynamic models governed by physics-based
PDEs, going beyond traditional approaches that assume a single PDE structure.
Our method integrates reaction-diffusion PDEs within a variational autoencoder
(VAE) mixture model framework, supporting inference of subtypes of
interpretable latent variables (e.g. diffusivity and reaction rates) from
neuroimaging data. We evaluate our method on synthetic benchmarks and
demonstrate its potential for uncovering mechanistic subtypes of Alzheimer's
disease progression from positron emission tomography (PET) data.

## 🔍 Abstract (한글 번역)

신경퇴행성 질환의 근본적인 메커니즘을 모델링하기 위해서는 희소하고 고차원적인 신경영상 데이터에서 이질적이고 공간적으로 변화하는 동역학을 포착할 수 있는 방법이 필요합니다. 부분 미분 방정식(PDE) 기반의 물리학 지식을 기계 학습과 통합하면 기존의 수치적 방법에 비해 해석 가능성과 유용성이 향상됩니다. 그러나 현재의 물리학 통합 기계 학습 방법은 단일 PDE만을 고려하는 데 제한되어 있어, 여러 메커니즘이 서로 다른 그룹(즉, 아형)에 대해 책임이 있는 질병에 적용하는 데 심각한 제한이 있으며, 모델의 잘못된 명세와 퇴행성 문제를 악화시킵니다. 여기서 우리는 물리학 기반 PDE에 의해 지배되는 잠재적 동적 모델의 혼합을 학습하기 위한 심층 생성 모델을 제시하며, 단일 PDE 구조를 가정하는 전통적인 접근 방식을 넘어섭니다. 우리의 방법은 변분 오토인코더(VAE) 혼합 모델 프레임워크 내에서 반응-확산 PDE를 통합하여 신경영상 데이터로부터 해석 가능한 잠재 변수(예: 확산성 및 반응 속도)의 아형 추론을 지원합니다. 우리는 합성 벤치마크에서 우리의 방법을 평가하고 양전자 방출 단층촬영(PET) 데이터를 통해 알츠하이머병 진행의 기계적 아형을 발견할 수 있는 잠재력을 입증합니다.

## 📝 요약

이 논문은 신경퇴행성 질환의 기저 메커니즘을 모델링하기 위해, 희소하고 고차원적인 신경영상 데이터를 다루는 방법론을 제안합니다. 기존의 물리 기반 머신러닝은 단일 편미분 방정식(PDE)만을 고려하여 다양한 메커니즘을 가진 질환에 한계가 있었습니다. 본 연구는 반응-확산 PDE를 변분 오토인코더(VAE) 혼합 모델에 통합하여, 다양한 잠재적 동적 모델을 학습할 수 있는 심층 생성 모델을 제안합니다. 이를 통해 해석 가능한 잠재 변수의 아형을 추론할 수 있으며, 특히 알츠하이머병의 진행을 양전자 방출 단층촬영(PET) 데이터를 통해 분석하여 그 잠재력을 입증했습니다.

## 🎯 주요 포인트

- 1. 신경퇴행성 질환의 기저 메커니즘을 모델링하기 위해서는 희소하고 고차원적인 신경영상 데이터를 활용하여 이질적이고 공간적으로 변화하는 동역학을 포착하는 방법이 필요합니다.

- 2. 부분 미분 방정식(PDE) 기반의 물리학 지식을 기계 학습과 통합하면 기존의 수치적 방법보다 해석 가능성과 유용성이 향상됩니다.

- 3. 본 연구는 물리학 기반 PDE에 의해 지배되는 잠재적 동적 모델의 혼합을 학습하기 위한 심층 생성 모델을 제시하여 단일 PDE 구조를 가정하는 전통적 접근 방식을 넘어섭니다.

- 4. 반응-확산 PDE를 변분 오토인코더(VAE) 혼합 모델 프레임워크에 통합하여 신경영상 데이터로부터 해석 가능한 잠재 변수의 아형(예: 확산성 및 반응 속도)을 추론할 수 있도록 지원합니다.

- 5. 본 방법은 합성 벤치마크에서 평가되었으며, 양전자 방출 단층촬영(PET) 데이터를 통해 알츠하이머병 진행의 기계적 아형을 발견할 가능성을 보여줍니다.

---

*Generated on 2025-09-20 00:58:17*