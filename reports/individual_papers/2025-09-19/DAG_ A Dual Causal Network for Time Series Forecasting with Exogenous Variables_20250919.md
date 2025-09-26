---
keywords:
  - Exogenous Variables
  - Causal Network
  - Temporal Causal Module
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14933
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:50:44.450112",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Exogenous Variables",
    "Causal Network",
    "Temporal Causal Module"
  ],
  "rejected_keywords": [
    "Time Series Forecasting",
    "Channel Causal Module"
  ],
  "similarity_scores": {
    "Exogenous Variables": 0.82,
    "Causal Network": 0.8,
    "Temporal Causal Module": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DAG: A Dual Causal Network for Time Series Forecasting with Exogenous Variables

**Korean Title:** DAG: 외생 변수를 활용한 시계열 예측을 위한 이중 인과 네트워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Exogenous Variables|Exogenous Variables]], [[keywords/Causal Network|Causal Network]], [[keywords/Temporal Causal Module|Temporal Causal Module]]

## 🔗 유사한 논문
- [[TFMAdapter Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates]] (78.3% similar)
- [[Diffusion-Based_Scenario_Tree_Generation_for_Multivariate_Time_Series_Prediction_and_Multistage_Stochastic_Optimization_20250919|Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization]] (77.0% similar)
- [[From Distributional to Quantile Neural Basis Models the case of Electricity Price Forecasting]] (76.9% similar)
- [[Empowering Time Series Analysis with Foundation Models A Comprehensive Survey]] (76.6% similar)
- [[DECAMP Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (75.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14933v1 Announce Type: new 
Abstract: Time series forecasting is crucial in various fields such as economics, traffic, and AIOps. However, in real-world applications, focusing solely on the endogenous variables (i.e., target variables), is often insufficient to ensure accurate predictions. Considering exogenous variables (i.e., covariates) provides additional predictive information, thereby improving forecasting accuracy. However, existing methods for time series forecasting with exogenous variables (TSF-X) have the following shortcomings: 1) they do not leverage future exogenous variables, 2) they fail to account for the causal relationships between endogenous and exogenous variables. As a result, their performance is suboptimal. In this study, to better leverage exogenous variables, especially future exogenous variable, we propose a general framework DAG, which utilizes dual causal network along both the temporal and channel dimensions for time series forecasting with exogenous variables. Specifically, we first introduce the Temporal Causal Module, which includes a causal discovery module to capture how historical exogenous variables affect future exogenous variables. Following this, we construct a causal injection module that incorporates the discovered causal relationships into the process of forecasting future endogenous variables based on historical endogenous variables. Next, we propose the Channel Causal Module, which follows a similar design principle. It features a causal discovery module models how historical exogenous variables influence historical endogenous variables, and a causal injection module incorporates the discovered relationships to enhance the prediction of future endogenous variables based on future exogenous variables.

## 🔍 Abstract (한글 번역)

arXiv:2509.14933v1 발표 유형: 신규  
초록: 시계열 예측은 경제학, 교통, AIOps 등 다양한 분야에서 매우 중요합니다. 그러나 실제 응용에서 내생 변수(즉, 목표 변수)에만 집중하는 것은 정확한 예측을 보장하기에 종종 불충분합니다. 외생 변수(즉, 공변량)를 고려하면 추가적인 예측 정보를 제공하여 예측 정확도를 향상시킬 수 있습니다. 그러나 외생 변수를 포함한 시계열 예측(TSF-X)에 대한 기존 방법에는 다음과 같은 단점이 있습니다: 1) 미래의 외생 변수를 활용하지 못한다, 2) 내생 변수와 외생 변수 간의 인과 관계를 고려하지 않는다. 그 결과, 이들의 성능은 최적이 아닙니다. 본 연구에서는 외생 변수, 특히 미래의 외생 변수를 더 잘 활용하기 위해, 외생 변수를 포함한 시계열 예측을 위한 시간 및 채널 차원에서 이중 인과 네트워크를 활용하는 일반적인 프레임워크 DAG를 제안합니다. 구체적으로, 우리는 먼저 역사적 외생 변수가 미래의 외생 변수에 어떻게 영향을 미치는지를 포착하기 위한 인과 발견 모듈을 포함하는 시간 인과 모듈을 소개합니다. 그 후, 역사적 내생 변수를 기반으로 미래의 내생 변수를 예측하는 과정에 발견된 인과 관계를 통합하는 인과 주입 모듈을 구성합니다. 다음으로, 우리는 유사한 설계 원칙을 따르는 채널 인과 모듈을 제안합니다. 이는 역사적 외생 변수가 역사적 내생 변수에 어떻게 영향을 미치는지를 모델링하는 인과 발견 모듈과, 미래의 외생 변수를 기반으로 미래의 내생 변수 예측을 향상시키기 위해 발견된 관계를 통합하는 인과 주입 모듈을 특징으로 합니다.

## 📝 요약

이 논문은 시계열 예측에서 외생 변수의 중요성을 강조하며, 기존 방법들이 미래 외생 변수를 활용하지 못하고 내생 변수와 외생 변수 간의 인과 관계를 고려하지 않는다는 한계를 지적합니다. 이를 개선하기 위해, 저자들은 시간 및 채널 차원에서 이중 인과 네트워크를 활용하는 일반적인 프레임워크인 DAG를 제안합니다. 이 프레임워크는 과거 외생 변수가 미래 외생 변수에 미치는 영향을 포착하는 '시간 인과 모듈'과, 발견된 인과 관계를 바탕으로 미래 내생 변수를 예측하는 '채널 인과 모듈'을 포함합니다. 이러한 접근 방식은 예측 정확도를 향상시킵니다.

## 🎯 주요 포인트

- 1. 시계열 예측에서 외생 변수(공변량)를 고려하면 예측 정확도를 향상시킬 수 있습니다.

- 2. 기존의 외생 변수를 활용한 시계열 예측 방법은 미래 외생 변수를 활용하지 못하고, 내생 변수와 외생 변수 간의 인과 관계를 고려하지 못하는 한계가 있습니다.

- 3. 본 연구에서는 외생 변수를 효과적으로 활용하기 위해 시간 및 채널 차원에서 이중 인과 네트워크를 활용하는 일반적인 프레임워크 DAG를 제안합니다.

- 4. Temporal Causal Module은 역사적 외생 변수가 미래 외생 변수에 미치는 영향을 포착하는 인과 발견 모듈과, 발견된 인과 관계를 예측 과정에 통합하는 인과 주입 모듈로 구성됩니다.

- 5. Channel Causal Module은 역사적 외생 변수가 역사적 내생 변수에 미치는 영향을 모델링하고, 발견된 관계를 통해 미래 내생 변수 예측을 향상시키는 인과 주입 모듈을 포함합니다.

---

*Generated on 2025-09-19 15:28:17*