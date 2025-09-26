---
keywords:
  - Self-Supervised Learning
  - Transformer Architecture
  - Multivariate Anomaly Detection
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:37:20.407951",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-Supervised Learning",
    "Transformer Architecture",
    "Multivariate Anomaly Detection"
  ],
  "rejected_keywords": [
    "Spatio-Temporal Patterns"
  ],
  "similarity_scores": {
    "Self-Supervised Learning": 0.82,
    "Transformer Architecture": 0.8,
    "Multivariate Anomaly Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Beyond Marginals: Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection

**Korean Title:** 한계점을 넘어서: 다변량 이상 탐지를 위한 공동 시공간 패턴 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-Supervised Learning|Self-supervised contrastive learning]], [[keywords/Transformer Architecture|Transformer encoder]]
**⚡ Unique Technical**: [[keywords/Multivariate Anomaly Detection|Multivariate anomaly detection]]

## 🔗 유사한 논문
- [[AnoF-Diff_ One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use_20250918|AnoF-Diff One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use]] (82.1% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (79.2% similar)
- [[Preference Isolation Forest for Structure-based Anomaly Detection_20250919|Preference Isolation Forest for Structure-based Anomaly Detection]] (78.3% similar)
- [[DAG_ A Dual Causal Network for Time Series Forecasting with Exogenous Variables_20250919|DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (78.2% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.9% similar)

## 📋 저자 정보

**Authors:** Padmaksha Roy, Almuatazbellah Boker, Lamine Mili

## 📄 Abstract (원문)

In this paper, we aim to improve multivariate anomaly detection (AD) by
modeling the \textit{time-varying non-linear spatio-temporal correlations}
found in multivariate time series data . In multivariate time series data, an
anomaly may be indicated by the simultaneous deviation of interrelated time
series from their expected collective behavior, even when no individual time
series exhibits a clearly abnormal pattern on its own. In many existing
approaches, time series variables are assumed to be (conditionally)
independent, which oversimplifies real-world interactions. Our approach
addresses this by modeling joint dependencies in the latent space and
decoupling the modeling of \textit{marginal distributions, temporal dynamics,
and inter-variable dependencies}. We use a transformer encoder to capture
temporal patterns, and to model spatial (inter-variable) dependencies, we fit a
multi-variate likelihood and a copula. The temporal and the spatial components
are trained jointly in a latent space using a self-supervised contrastive
learning objective to learn meaningful feature representations to separate
normal and anomaly samples.

## 🔍 Abstract (한글 번역)

이 논문에서는 다변량 시계열 데이터에서 발견되는 \textit{시간에 따라 변하는 비선형 시공간 상관관계}를 모델링하여 다변량 이상 탐지(AD)를 개선하고자 합니다. 다변량 시계열 데이터에서 이상 현상은 개별 시계열이 명확한 비정상 패턴을 보이지 않더라도 상호 관련된 시계열이 예상되는 집합적 행동에서 동시에 벗어날 때 나타날 수 있습니다. 많은 기존 접근 방식에서는 시계열 변수가 (조건부로) 독립적이라고 가정하여 실제 상호작용을 지나치게 단순화합니다. 우리의 접근 방식은 잠재 공간에서의 공동 종속성을 모델링하고 \textit{한계 분포, 시간적 역학, 변수 간 종속성}의 모델링을 분리함으로써 이를 해결합니다. 우리는 트랜스포머 인코더를 사용하여 시간적 패턴을 포착하고, 공간적(변수 간) 종속성을 모델링하기 위해 다변량 가능성과 코풀라를 맞춥니다. 시간적 및 공간적 구성 요소는 잠재 공간에서 자기 지도 대조 학습 목표를 사용하여 정상 샘플과 이상 샘플을 구분할 수 있는 의미 있는 특징 표현을 학습하도록 공동으로 훈련됩니다.

## 📝 요약

이 논문은 다변량 시계열 데이터에서 시간에 따라 변화하는 비선형 시공간 상관관계를 모델링하여 다변량 이상 탐지를 개선하는 방법을 제안합니다. 기존 방법들은 시계열 변수를 독립적으로 가정하여 실제 상호작용을 과도하게 단순화하는 문제를 갖고 있습니다. 본 연구는 잠재 공간에서의 공동 의존성을 모델링하고, 주변 분포, 시간적 역학, 변수 간 의존성의 모델링을 분리하여 이를 해결합니다. 시계열 패턴을 포착하기 위해 트랜스포머 인코더를 사용하고, 공간적 의존성을 모델링하기 위해 다변량 가능성과 코퓰라를 적용합니다. 시간적 및 공간적 구성 요소는 자기 지도 대조 학습 목표를 통해 잠재 공간에서 공동으로 훈련되어 정상 및 이상 샘플을 구분하는 의미 있는 특징 표현을 학습합니다.

## 🎯 주요 포인트

- 1. 본 논문은 다변량 시계열 데이터에서 시간에 따라 변하는 비선형 시공간 상관관계를 모델링하여 다변량 이상 탐지를 개선하고자 한다.

- 2. 기존 접근법은 시계열 변수가 독립적이라고 가정하지만, 이는 실제 상호작용을 과도하게 단순화한다.

- 3. 제안된 방법은 잠재 공간에서의 공동 의존성을 모델링하고 주변 분포, 시간적 동역학, 변수 간 의존성의 모델링을 분리한다.

- 4. 시간적 패턴을 포착하기 위해 트랜스포머 인코더를 사용하고, 공간적(변수 간) 의존성을 모델링하기 위해 다변량 가능성과 코풀라를 적용한다.

- 5. 시간적 및 공간적 구성 요소는 자기 지도 대조 학습 목표를 사용하여 잠재 공간에서 정상 및 이상 샘플을 구분할 수 있는 의미 있는 특징 표현을 학습하도록 공동으로 훈련된다.

---

*Generated on 2025-09-20 01:09:06*