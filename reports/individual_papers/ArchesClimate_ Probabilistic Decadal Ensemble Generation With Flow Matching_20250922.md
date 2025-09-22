# ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching

**Korean Title:** ArchesClimate: 흐름 매칭을 통한 확률적 10년 주기 앙상블 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Climate Model Emulator

## 🔗 유사한 논문
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (78.9% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.2% similar)
- [[2025-09-17/Artificial neural networks ensemble methodology to predict significant wave height_20250917|Artificial neural networks ensemble methodology to predict significant wave height]] (78.0% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (77.3% similar)
- [[2025-09-19/Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization_20250919|Diffusion-Based Scenario Tree Generation for Multivariate Time Series Prediction and Multistage Stochastic Optimization]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15942v1 Announce Type: cross 
Abstract: Climate projections have uncertainties related to components of the climate system and their interactions. A typical approach to quantifying these uncertainties is to use climate models to create ensembles of repeated simulations under different initial conditions. Due to the complexity of these simulations, generating such ensembles of projections is computationally expensive. In this work, we present ArchesClimate, a deep learning-based climate model emulator that aims to reduce this cost. ArchesClimate is trained on decadal hindcasts of the IPSL-CM6A-LR climate model at a spatial resolution of approximately 2.5x1.25 degrees. We train a flow matching model following ArchesWeatherGen, which we adapt to predict near-term climate. Once trained, the model generates states at a one-month lead time and can be used to auto-regressively emulate climate model simulations of any length. We show that for up to 10 years, these generations are stable and physically consistent. We also show that for several important climate variables, ArchesClimate generates simulations that are interchangeable with the IPSL model. This work suggests that climate model emulators could significantly reduce the cost of climate model simulations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15942v1 발표 유형: 교차  
초록: 기후 예측에는 기후 시스템의 구성 요소와 그 상호작용에 관련된 불확실성이 존재합니다. 이러한 불확실성을 정량화하는 일반적인 접근 방식은 기후 모델을 사용하여 다양한 초기 조건 하에서 반복 시뮬레이션의 앙상블을 생성하는 것입니다. 이러한 시뮬레이션의 복잡성으로 인해, 이러한 예측 앙상블을 생성하는 것은 계산 비용이 많이 듭니다. 본 연구에서는 이러한 비용을 줄이기 위한 딥러닝 기반 기후 모델 에뮬레이터인 ArchesClimate를 제시합니다. ArchesClimate는 약 2.5x1.25도의 공간 해상도로 IPSL-CM6A-LR 기후 모델의 10년간의 힌드캐스트에 대해 학습됩니다. 우리는 ArchesWeatherGen을 따르는 흐름 매칭 모델을 학습하여 단기 기후를 예측하도록 조정합니다. 학습이 완료되면, 모델은 한 달의 리드 타임으로 상태를 생성하며, 임의의 길이의 기후 모델 시뮬레이션을 자동 회귀적으로 에뮬레이트하는 데 사용할 수 있습니다. 우리는 최대 10년 동안 이러한 생성이 안정적이고 물리적으로 일관됨을 보여줍니다. 또한 여러 중요한 기후 변수에 대해 ArchesClimate가 IPSL 모델과 상호 교환 가능한 시뮬레이션을 생성함을 보여줍니다. 이 연구는 기후 모델 에뮬레이터가 기후 모델 시뮬레이션의 비용을 크게 줄일 수 있음을 시사합니다.

## 📝 요약

이 연구는 기후 예측의 불확실성을 줄이기 위해 ArchesClimate라는 딥러닝 기반 기후 모델 에뮬레이터를 제안합니다. ArchesClimate는 IPSL-CM6A-LR 기후 모델의 10년간의 예측 데이터를 학습하여, 복잡하고 비용이 많이 드는 기후 모델 시뮬레이션을 대체할 수 있도록 설계되었습니다. 이 모델은 1개월 앞의 기후 상태를 예측하고, 자가 회귀적으로 긴 기간의 기후 모델 시뮬레이션을 모방할 수 있습니다. 연구 결과, ArchesClimate는 최대 10년 동안 안정적이고 물리적으로 일관된 시뮬레이션을 생성하며, 여러 중요한 기후 변수에 대해 기존 모델과 상호 교환 가능함을 보여줍니다. 이 연구는 기후 모델 에뮬레이터가 시뮬레이션 비용을 크게 줄일 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. ArchesClimate는 딥러닝 기반의 기후 모델 에뮬레이터로, 기후 예측 시뮬레이션의 비용을 절감하는 것을 목표로 한다.

- 2. 이 모델은 IPSL-CM6A-LR 기후 모델의 10년 단위 예측 데이터를 기반으로 학습되었으며, 약 2.5x1.25도의 공간 해상도를 갖는다.

- 3. ArchesClimate는 한 달 앞서 기후 상태를 예측할 수 있으며, 자가 회귀적으로 어떤 길이의 기후 모델 시뮬레이션도 에뮬레이트할 수 있다.

- 4. 최대 10년 동안의 예측에서 ArchesClimate의 생성 결과는 안정적이고 물리적으로 일관성이 있는 것으로 나타났다.

- 5. ArchesClimate는 여러 중요한 기후 변수에 대해 IPSL 모델과 상호 교환 가능한 시뮬레이션을 생성할 수 있다.

---

*Generated on 2025-09-22 14:18:29*