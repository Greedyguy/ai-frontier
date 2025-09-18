
# TFMAdapter: Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates

**Korean Title:** TFMAdapter: 가벼운 인스턴스 수준의 코베리에이트를 활용한 Foundation 모델 예측 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Non-parametric Cascade|Non-parametric Cascade]] [[keywords/broad/Time Series Foundation Models|Time Series Foundation Models]] [[keywords/broad/Covariates|Covariates]] [[keywords/specific/Instance-Level Adaptation|Instance-Level Adaptation]] [[keywords/unique/TFMAdapter|TFMAdapter]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Two-stage Method
**🔬 Broad Technical**: Time Series Foundation Models, Covariates
**🔗 Specific Connectable**: Instance-Level Adaptation
**⭐ Unique Technical**: TFMAdapter

**ArXiv ID**: [2509.13906](https://arxiv.org/abs/2509.13906)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13906.pdf)


## 🏷️ 추출된 키워드



`Time Series Foundation Models` • 

`Covariates` • 

`Instance-Level Adaptation` • 

`TFMAdapter` • 

`Two-stage Method`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13906v1 Announce Type: new 
Abstract: Time Series Foundation Models (TSFMs) have recently achieved state-of-the-art performance in univariate forecasting on new time series simply by conditioned on a brief history of past values. Their success demonstrates that large-scale pretraining across diverse domains can acquire the inductive bias to generalize from temporal patterns in a brief history. However, most TSFMs are unable to leverage covariates -- future-available exogenous variables critical for accurate forecasting in many applications -- due to their domain-specific nature and the lack of associated inductive bias. We propose TFMAdapter, a lightweight, instance-level adapter that augments TSFMs with covariate information without fine-tuning. Instead of retraining, TFMAdapter operates on the limited history provided during a single model call, learning a non-parametric cascade that combines covariates with univariate TSFM forecasts. However, such learning would require univariate forecasts at all steps in the history, requiring too many calls to the TSFM. To enable training on the full historical context while limiting TSFM invocations, TFMAdapter uses a two-stage method: (1) generating pseudo-forecasts with a simple regression model, and (2) training a Gaussian Process regressor to refine predictions using both pseudo- and TSFM forecasts alongside covariates. Extensive experiments on real-world datasets demonstrate that TFMAdapter consistently outperforms both foundation models and supervised baselines, achieving a 24-27\% improvement over base foundation models with minimal data and computational overhead. Our results highlight the potential of lightweight adapters to bridge the gap between generic foundation models and domain-specific forecasting needs.

## 🔍 Abstract (한글 번역)

arXiv:2509.13906v1 발표 유형: 새로운
요약: 최근에는 시계열 기반 모델(Time Series Foundation Models, TSFMs)이 단순히 과거 값의 간단한 기록에 의존하여 새로운 시계열에서 단변량 예측에서 최첨단 성능을 달성했습니다. 그들의 성공은 다양한 도메인에서 대규모 사전 훈련이 간단한 기록의 시간적 패턴으로부터 일반화하기 위한 귀납 편향을 습득할 수 있다는 것을 보여줍니다. 그러나 대부분의 TSFMs는 도메인 특정성과 관련된 귀납 편향의 부재로 인해 정확한 예측을 위한 매우 중요한 미래 가능한 외생 변수를 활용할 수 없습니다. 우리는 TFMAdapter를 제안합니다. 이는 TSFMs에 미세 조정 없이 외생 변수 정보를 보완하는 가벼운 인스턴스 수준 어댑터입니다. 재훈련 대신, TFMAdapter는 단일 모델 호출 중에 제공된 제한된 기록을 기반으로 작동하여 외생 변수와 단변량 TSFM 예측을 결합하는 비모수적 카스케이드를 학습합니다. 그러나 이러한 학습은 모든 단계에서 단변량 예측을 필요로 하기 때문에 TSFM에 너무 많은 호출이 필요합니다. TSFM 호출을 제한하면서 전체 역사적 맥락에서 훈련할 수 있도록 하기 위해 TFMAdapter는 두 단계 방법을 사용합니다: (1) 간단한 회귀 모델을 사용하여 가상 예측 생성 및 (2) 가상 및 TSFM 예측과 외생 변수를 함께 사용하여 예측을 정교화하기 위해 가우시안 프로세스 회귀자를 훈련합니다. 실제 데이터셋에서의 광범위한 실험 결과는 TFMAdapter가 기초 모델과 지도 기준선을 일관되게 능가하며, 최소한의 데이터 및 계산 오버헤드로 기초 모델에 대해 24-27%의 개선을 달성한다는 것을 보여줍니다. 우리의 결과는 가벼운 어댑터의 잠재력을 강조하여 일반적인 기초 모델과 도메인 특정 예측 요구 사이의 간극을 줄일 수 있다.

## 📝 요약

최근에는 시계열 기반 모델(Time Series Foundation Models, TSFMs)이 과거 값의 간단한 이력에 의존하여 새로운 시계열의 단변량 예측에서 최고 수준의 성능을 달성했습니다. 이들의 성공은 다양한 도메인에서 대규모 사전 훈련이 간단한 이력의 시간적 패턴으로부터 일반화의 편향을 습득할 수 있다는 것을 보여줍니다. 그러나 대부분의 TSFM은 도메인별 특성과 관련된 추론 편향의 부재로 인해 많은 응용 프로그램에서 정확한 예측을 위해 중요한 미래 가능한 외생 변수를 활용할 수 없습니다. 우리는 TSFM에 세부 정보를 덧붙이는 경량의 인스턴스 수준 어댑터인 TFMAdapter를 제안합니다. TFMAdapter는 재훈련 없이 TSFM을 외생 변수 정보로 보강합니다. TFMAdapter는 한 모델 호출 중에 제공된 제한된 이력에서 작동하며, 외생 변수와 단변량 TSFM 예측을 결합하는 비모수적 캐스케이드를 학습합니다.

## 🎯 주요 포인트


- 1. 시계열 기반 모델(TSFMs)은 다양한 도메인에서 사전 훈련을 통해 시간 패턴을 일반화하는 인지 편향을 습득하여 최근 단변량 예측에서 최고 수준의 성능을 달성했다.

- 2. TFMAdapter는 도메인 특정성과 관련된 인지 편향의 부족으로 인해 많은 응용 프로그램에서 정확한 예측에 중요한 미래 가능한 외생 변수를 활용하지 못하는 TSFMs를 보완하는 경량의 인스턴스 수준 어댑터를 제안한다.

- 3. TFMAdapter는 TSFMs에 외생 변수 정보를 추가하여 기존 모델을 성능 향상시키고, 단변량 예측에서 24-27%의 개선을 실현하는 것으로 나타났다.


---

*Generated on 2025-09-18 16:39:24*