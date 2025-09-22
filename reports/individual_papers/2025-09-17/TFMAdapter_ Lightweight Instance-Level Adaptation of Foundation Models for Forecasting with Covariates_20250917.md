# TFMAdapter: Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates

**Korean Title:** TFMAdapter: 공변량을 활용한 예측을 위한 기초 모델의 경량 인스턴스 수준 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Afrin Dange|Afrin Dange]] [[authors/Sunita Sarawagi|Sunita Sarawagi]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Instance-Level Adaptation

## 🔗 유사한 논문
- [[Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (79.5% similar)
- [[Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future Distribution-Aware Alignment for Time Series Forecasting]] (79.2% similar)
- [[FroM_ Frobenius Norm-Based Data-Free Adaptive Model Merging_20250918|FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (77.1% similar)
- [[DAG_ A Dual Causal Network for Time Series Forecasting with Exogenous Variables_20250919|DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (76.9% similar)
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (76.7% similar)

## 📋 저자 정보

**Authors:** Afrin Dange, Sunita Sarawagi

## 📄 Abstract (원문)

Time Series Foundation Models (TSFMs) have recently achieved state-of-the-art
performance in univariate forecasting on new time series simply by conditioned
on a brief history of past values. Their success demonstrates that large-scale
pretraining across diverse domains can acquire the inductive bias to generalize
from temporal patterns in a brief history. However, most TSFMs are unable to
leverage covariates -- future-available exogenous variables critical for
accurate forecasting in many applications -- due to their domain-specific
nature and the lack of associated inductive bias. We propose TFMAdapter, a
lightweight, instance-level adapter that augments TSFMs with covariate
information without fine-tuning. Instead of retraining, TFMAdapter operates on
the limited history provided during a single model call, learning a
non-parametric cascade that combines covariates with univariate TSFM forecasts.
However, such learning would require univariate forecasts at all steps in the
history, requiring too many calls to the TSFM. To enable training on the full
historical context while limiting TSFM invocations, TFMAdapter uses a two-stage
method: (1) generating pseudo-forecasts with a simple regression model, and (2)
training a Gaussian Process regressor to refine predictions using both pseudo-
and TSFM forecasts alongside covariates. Extensive experiments on real-world
datasets demonstrate that TFMAdapter consistently outperforms both foundation
models and supervised baselines, achieving a 24-27\% improvement over base
foundation models with minimal data and computational overhead. Our results
highlight the potential of lightweight adapters to bridge the gap between
generic foundation models and domain-specific forecasting needs.

## 🔍 Abstract (한글 번역)

시계열 기초 모델(TSFMs)은 최근 새로운 시계열의 단변량 예측에서 과거 값의 짧은 기록에 조건화하는 것만으로 최첨단 성능을 달성했습니다. 이들의 성공은 다양한 도메인에 걸친 대규모 사전 학습이 짧은 기록의 시간적 패턴으로부터 일반화할 수 있는 귀납적 편향을 획득할 수 있음을 보여줍니다. 그러나 대부분의 TSFMs는 도메인 특유의 특성과 관련된 귀납적 편향의 부족으로 인해 많은 응용 분야에서 정확한 예측에 중요한 미래에 사용 가능한 외생 변수를 활용할 수 없습니다. 우리는 TFMAdapter를 제안합니다. 이는 TSFMs에 대해 미세 조정 없이 공변량 정보를 보강하는 경량의 인스턴스 수준 어댑터입니다. 재학습 대신, TFMAdapter는 단일 모델 호출 동안 제공되는 제한된 기록에서 작동하여 단변량 TSFM 예측과 공변량을 결합하는 비모수적 캐스케이드를 학습합니다. 그러나 이러한 학습은 기록의 모든 단계에서 단변량 예측을 필요로 하며, 이는 TSFM에 대한 너무 많은 호출을 요구합니다. 전체 역사적 맥락에서의 학습을 가능하게 하면서 TSFM 호출을 제한하기 위해, TFMAdapter는 두 단계 방법을 사용합니다: (1) 간단한 회귀 모델로 의사 예측 생성, (2) 공변량과 함께 의사 예측 및 TSFM 예측을 사용하여 예측을 정제하기 위한 가우시안 프로세스 회귀자 학습. 실제 데이터셋에 대한 광범위한 실험은 TFMAdapter가 기초 모델과 감독된 기준 모델을 일관되게 능가하며, 최소한의 데이터 및 계산 오버헤드로 기본 기초 모델 대비 24-27%의 향상을 달성함을 보여줍니다. 우리의 결과는 경량 어댑터가 일반적인 기초 모델과 도메인 특유의 예측 요구 사이의 격차를 메울 수 있는 잠재력을 강조합니다.

## 📝 요약

Time Series Foundation Models (TSFMs)는 과거 데이터의 짧은 기록만으로도 단변량 예측에서 최첨단 성능을 보여주지만, 도메인 특유의 외생 변수(공변량)를 활용하지 못하는 한계가 있습니다. 이를 해결하기 위해, 우리는 TFMAdapter를 제안합니다. 이는 TSFM을 미세 조정 없이 공변량 정보를 통합할 수 있는 경량 어댑터로, 단일 모델 호출 시 제한된 기록을 활용하여 비모수적 방법으로 공변량과 단변량 예측을 결합합니다. TFMAdapter는 두 단계로 작동하며, 간단한 회귀 모델로 의사 예측을 생성한 후, 가우시안 프로세스 회귀를 통해 이를 정제합니다. 실제 데이터셋 실험 결과, TFMAdapter는 기존 모델 대비 24-27% 성능 향상을 보이며, 경량 어댑터가 범용 모델과 도메인 특화 예측 간의 격차를 줄일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. TSFMs는 과거 값의 짧은 기록만으로도 최신의 단변량 예측 성능을 달성했습니다.

- 2. TSFMs는 일반적으로 도메인 특화된 외생 변수를 활용하지 못하며, 이는 정확한 예측에 중요한 요소입니다.

- 3. TFMAdapter는 TSFMs에 외생 변수 정보를 추가하여 미세 조정 없이 예측 성능을 향상시킵니다.

- 4. TFMAdapter는 두 단계 방법을 사용하여 전체 역사적 맥락에서의 학습을 가능하게 합니다.

- 5. 실험 결과, TFMAdapter는 최소한의 데이터 및 계산 오버헤드로 기본 모델 대비 24-27% 성능 향상을 달성했습니다.

---

*Generated on 2025-09-20 09:24:54*