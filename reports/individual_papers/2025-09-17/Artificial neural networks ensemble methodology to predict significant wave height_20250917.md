# Artificial neural networks ensemble methodology to predict significant wave height

**Korean Title:** 인공 신경망 앙상블 방법론을 이용한 유의 파고 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Felipe Crivellaro Minuzzi|Felipe Crivellaro Minuzzi]] [[authors/Leandro Farina|Leandro Farina]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⭐ Unique Technical**: Hybrid CNN-LSTM

## 🔗 유사한 논문
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (79.3% similar)
- [[FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (79.3% similar)
- [[Towards Trustworthy Vital Sign Forecasting_ Leveraging Uncertainty for Prediction Intervals_20250918|Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (78.2% similar)
- [[H-Alpha Anomalyzer_ An Explainable Anomaly Detector for Solar H-Alpha Observations_20250917|H-Alpha Anomalyzer An Explainable Anomaly Detector for Solar H-Alpha Observations]] (77.8% similar)
- [[Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models_20250919|Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models]] (77.4% similar)

## 📋 저자 정보

**Authors:** Felipe Crivellaro Minuzzi, Leandro Farina

## 📄 Abstract (원문)

The forecast of wave variables are important for several applications that
depend on a better description of the ocean state. Due to the chaotic behaviour
of the differential equations which model this problem, a well know strategy to
overcome the difficulties is basically to run several simulations, by for
instance, varying the initial condition, and averaging the result of each of
these, creating an ensemble. Moreover, in the last few years, considering the
amount of available data and the computational power increase, machine learning
algorithms have been applied as surrogate to traditional numerical models,
yielding comparative or better results. In this work, we present a methodology
to create an ensemble of different artificial neural networks architectures,
namely, MLP, RNN, LSTM, CNN and a hybrid CNN-LSTM, which aims to predict
significant wave height on six different locations in the Brazilian coast. The
networks are trained using NOAA's numerical reforecast data and target the
residual between observational data and the numerical model output. A new
strategy to create the training and target datasets is demonstrated. Results
show that our framework is capable of producing high efficient forecast, with
an average accuracy of $80\%$, that can achieve up to $88\%$ in the best case
scenario, which means $5\%$ reduction in error metrics if compared to NOAA's
numerical model, and a increasingly reduction of computational cost.

## 🔍 Abstract (한글 번역)

파랑 변수의 예측은 해양 상태의 더 나은 설명에 의존하는 여러 응용 분야에 중요합니다. 이 문제를 모델링하는 미분 방정식의 혼돈적 특성 때문에, 어려움을 극복하기 위한 잘 알려진 전략은 기본적으로 초기 조건을 변화시키는 등의 방법으로 여러 시뮬레이션을 실행하고 각 결과를 평균화하여 앙상블을 생성하는 것입니다. 게다가, 최근 몇 년 동안 이용 가능한 데이터의 양과 컴퓨팅 파워의 증가를 고려하여, 기계 학습 알고리즘이 전통적인 수치 모델의 대체물로 적용되어 비교할 만한 또는 더 나은 결과를 내고 있습니다. 이 연구에서는 MLP, RNN, LSTM, CNN 및 하이브리드 CNN-LSTM이라는 다양한 인공 신경망 아키텍처의 앙상블을 생성하는 방법론을 제시하며, 이는 브라질 해안의 여섯 가지 다른 위치에서 유의 파고를 예측하는 것을 목표로 합니다. 이 네트워크는 NOAA의 수치 재예측 데이터를 사용하여 학습되며, 관측 데이터와 수치 모델 출력 간의 잔차를 목표로 합니다. 학습 및 목표 데이터셋을 생성하는 새로운 전략이 제시됩니다. 결과는 우리의 프레임워크가 평균 정확도 80%로 높은 효율의 예측을 생성할 수 있으며, 최상의 경우 88%까지 도달할 수 있음을 보여줍니다. 이는 NOAA의 수치 모델과 비교했을 때 오류 지표에서 5%의 감소를 의미하며, 계산 비용의 점진적인 감소를 가져옵니다.

## 📝 요약

이 연구는 브라질 해안의 6개 지역에서 유의파고를 예측하기 위해 다양한 인공신경망(MLP, RNN, LSTM, CNN, CNN-LSTM 하이브리드) 아키텍처로 구성된 앙상블을 제안합니다. NOAA의 수치 재예측 데이터를 사용하여 신경망을 훈련하고, 관측 데이터와 수치 모델 출력 간의 잔차를 목표로 삼습니다. 새로운 데이터셋 생성 전략을 통해 평균 80%의 정확도를 달성하며, 최고 88%까지 도달할 수 있습니다. 이는 NOAA의 수치 모델 대비 오차를 5% 줄이고, 계산 비용도 감소시킵니다.

## 🎯 주요 포인트

- 1. 파도 변수를 예측하기 위해 여러 인공신경망 아키텍처를 사용한 앙상블 방법론을 제시합니다.

- 2. 제안된 모델은 브라질 해안의 여섯 위치에서 유의 파고를 예측하는 데 중점을 둡니다.

- 3. NOAA의 수치 재예측 데이터를 사용하여 네트워크를 훈련하고, 관측 데이터와 수치 모델 출력 간의 잔차를 목표로 합니다.

- 4. 새로운 데이터셋 생성 전략을 통해 평균 80%의 예측 정확도를 달성하며, 최고 88%의 정확도를 기록합니다.

- 5. 제안된 프레임워크는 NOAA의 수치 모델에 비해 5%의 오류 감소와 계산 비용 절감을 이룹니다.

---

*Generated on 2025-09-20 09:18:27*