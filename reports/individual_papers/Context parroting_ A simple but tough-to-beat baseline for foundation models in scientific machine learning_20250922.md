# Context parroting: A simple but tough-to-beat baseline for foundation models in scientific machine learning

**Korean Title:** 맥락 패로팅: 과학적 기계 학습에서 기초 모델을 위한 간단하지만 뛰어넘기 어려운 기준점

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/In-context Learning Strategies|In-context Learning Strategies]] [[keywords/specific/Zero-shot Forecasting|Zero-shot Forecasting]] [[keywords/broad/Time Series Forecasting|Time Series Forecasting]] [[keywords/unique/Context Parroting|Context Parroting]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Deep Learning Foundation and Pattern Models_ Challenges in Hydrological Time Series_20250922|Deep Learning Foundation and Pattern Models: Challenges in Hydrological Time Series]] (81.3% similar) [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.6% similar) [[2025-09-22/Foundation Models as World Models_ A Foundational Study in Text-Based GridWorlds_20250922|Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: In-context Learning Strategies
**🔗 Specific Connectable**: Zero-shot Forecasting
**🔬 Broad Technical**: Time Series Forecasting
**⭐ Unique Technical**: Context Parroting
## 🔗 유사한 논문
- [[2025-09-22/Deep Learning Foundation and Pattern Models_ Challenges in Hydrological Time Series_20250922|Deep Learning Foundation and Pattern Models Challenges in Hydrological Time Series]] (81.3% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.6% similar)
- [[2025-09-22/Foundation Models as World Models_ A Foundational Study in Text-Based GridWorlds_20250922|Foundation Models as World Models A Foundational Study in Text-Based GridWorlds]] (80.3% similar)
- [[2025-09-17/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future Distribution-Aware Alignment for Time Series Forecasting]] (79.9% similar)
- [[2025-09-18/Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (79.9% similar)


**ArXiv ID**: [2505.11349](https://arxiv.org/abs/2505.11349)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.11349.pdf)


**ArXiv ID**: [2505.11349](https://arxiv.org/abs/2505.11349)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.11349.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: In-context Learning Strategies
**🔗 Specific Connectable**: Zero-shot Forecasting
**⭐ Unique Technical**: Context Parroting
**🔬 Broad Technical**: Time Series Forecasting

## 🏷️ 추출된 키워드



`Time Series Forecasting` • 

`Zero-shot Forecasting` • 

`Context Parroting` • 

`In-context Learning Strategies`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11349v2 Announce Type: replace 
Abstract: Recent time-series foundation models exhibit strong abilities to predict physical systems. These abilities include zero-shot forecasting, in which a model forecasts future states of a system given only a short trajectory as context, without knowledge of the underlying physics. Here, we show that foundation models often forecast through a simple parroting strategy, and when they are not parroting they exhibit some shared failure modes such as converging to the mean. As a result, a naive context parroting model that copies directly from the context scores higher than leading time-series foundation models on predicting a diverse range of dynamical systems, including low-dimensional chaos, turbulence, coupled oscillators, and electrocardiograms -- and at a tiny fraction of the computational cost. We draw a parallel between context parroting and induction heads, which explains recent works showing that large language models can often be repurposed for time series forecasting. Our dynamical systems perspective also ties the scaling between forecast accuracy and context length to the fractal dimension of the underlying chaotic attractor, providing insight into previously observed in-context neural scaling laws. By revealing the performance gaps and failure modes of current time-series foundation models, context parroting can guide the design of future foundation models and help identify in-context learning strategies beyond parroting.

## 🔍 Abstract (한글 번역)

arXiv:2505.11349v2 발표 유형: 교체  
초록: 최근의 시계열 기반 모델들은 물리 시스템을 예측하는 데 강력한 능력을 보여주고 있습니다. 이러한 능력에는 기저 물리학에 대한 지식 없이 짧은 궤적만을 맥락으로 제공받아 시스템의 미래 상태를 예측하는 제로샷 예측이 포함됩니다. 여기서 우리는 기반 모델들이 종종 단순한 앵무새 전략을 통해 예측을 수행하며, 앵무새 전략을 사용하지 않을 때는 평균으로 수렴하는 것과 같은 공통적인 실패 모드를 보인다는 것을 보여줍니다. 그 결과, 맥락에서 직접 복사하는 단순한 맥락 앵무새 모델이 저차원 혼돈, 난류, 결합된 진동자, 심전도 등 다양한 동적 시스템을 예측하는 데 있어 선도적인 시계열 기반 모델보다 높은 점수를 얻으며, 계산 비용도 극히 적게 듭니다. 우리는 맥락 앵무새와 귀납적 머리(induction heads) 사이의 유사성을 그려내어, 대형 언어 모델이 시계열 예측에 종종 재활용될 수 있음을 보여주는 최근 연구를 설명합니다. 우리의 동적 시스템 관점은 예측 정확도와 맥락 길이 사이의 스케일링을 기저 혼돈 끌개의 프랙탈 차원과 연결하여, 이전에 관찰된 맥락 내 신경 스케일링 법칙에 대한 통찰을 제공합니다. 현재 시계열 기반 모델의 성능 격차와 실패 모드를 드러냄으로써, 맥락 앵무새는 미래의 기반 모델 설계를 안내하고 앵무새를 넘어선 맥락 내 학습 전략을 식별하는 데 도움을 줄 수 있습니다.

## 📝 요약

최근 시계열 기반 모델들은 물리 시스템 예측에서 강력한 성능을 보이고 있습니다. 본 연구에서는 이러한 모델들이 주로 단순한 '따라하기' 전략을 통해 예측을 수행하며, 그렇지 않을 경우 평균으로 수렴하는 등의 공통적인 실패 패턴을 보인다는 점을 밝혔습니다. 이에 따라, 단순히 주어진 데이터를 복사하는 '컨텍스트 따라하기' 모델이 다양한 동적 시스템 예측에서 기존 모델들보다 더 높은 성능을 보이며, 계산 비용도 훨씬 적게 듭니다. 또한, 이러한 따라하기 전략이 대형 언어 모델의 시계열 예측 재활용과 관련이 있음을 설명합니다. 본 연구는 예측 정확도와 컨텍스트 길이 사이의 관계를 혼돈 매력자의 프랙탈 차원과 연결지어, 기존의 신경망 스케일링 법칙에 대한 통찰을 제공합니다. 이를 통해 현재 시계열 모델의 성능 격차와 실패 패턴을 밝히고, 미래 모델 설계와 새로운 학습 전략 개발에 기여할 수 있습니다.

## 🎯 주요 포인트


- 1. 최근 시계열 기반 모델들은 물리 시스템을 예측하는 강력한 능력을 보이며, 짧은 경로만으로도 미래 상태를 예측하는 제로샷 예측을 수행할 수 있다.

- 2. 이러한 모델들은 종종 단순한 '따라하기' 전략을 통해 예측하며, 그렇지 않을 때는 평균으로 수렴하는 등의 공통된 실패 패턴을 보인다.

- 3. 단순한 문맥 따라하기 모델이 다양한 동적 시스템 예측에서 더 높은 성능을 보이며, 이는 계산 비용이 매우 적게 든다.

- 4. 문맥 따라하기와 유도 헤드 사이의 유사성을 통해 대형 언어 모델이 시계열 예측에 재사용될 수 있음을 설명한다.

- 5. 문맥 따라하기는 현재 시계열 기반 모델의 성능 격차와 실패 패턴을 드러내며, 미래 모델 설계와 새로운 학습 전략 개발에 기여할 수 있다.


---

*Generated on 2025-09-22 15:58:46*