# SolarCrossFormer: Improving day-ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors

**Korean Title:** 솔라크로스포머: 위성 이미지와 지상 센서를 통합하여 일일 태양 복사 예측 개선

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Probabilistic Forecasting

## 🔗 유사한 논문
- [[2025-09-22/Solar Forecasting with Causality_ A Graph-Transformer Approach to Spatiotemporal Dependencies_20250922|Solar Forecasting with Causality A Graph-Transformer Approach to Spatiotemporal Dependencies]] (86.3% similar)
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (79.0% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (78.0% similar)
- [[2025-09-22/ArchesClimate_ Probabilistic Decadal Ensemble Generation With Flow Matching_20250922|ArchesClimate Probabilistic Decadal Ensemble Generation With Flow Matching]] (77.5% similar)
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (77.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15827v1 Announce Type: new 
Abstract: Accurate day-ahead forecasts of solar irradiance are required for the large-scale integration of solar photovoltaic (PV) systems into the power grid. However, current forecasting solutions lack the temporal and spatial resolution required by system operators. In this paper, we introduce SolarCrossFormer, a novel deep learning model for day-ahead irradiance forecasting, that combines satellite images and time series from a ground-based network of meteorological stations. SolarCrossFormer uses novel graph neural networks to exploit the inter- and intra-modal correlations of the input data and improve the accuracy and resolution of the forecasts. It generates probabilistic forecasts for any location in Switzerland with a 15-minute resolution for horizons up to 24 hours ahead. One of the key advantages of SolarCrossFormer its robustness in real life operations. It can incorporate new time-series data without retraining the model and, additionally, it can produce forecasts for locations without input data by using only their coordinates. Experimental results over a dataset of one year and 127 locations across Switzerland show that SolarCrossFormer yield a normalized mean absolute error of 6.1 % over the forecasting horizon. The results are competitive with those achieved by a commercial numerical weather prediction service.

## 🔍 Abstract (한글 번역)

arXiv:2509.15827v1 발표 유형: 신규  
초록: 태양광 발전 시스템을 전력망에 대규모로 통합하기 위해서는 정확한 일일 태양 복사 예측이 필요합니다. 그러나 현재의 예측 솔루션은 시스템 운영자가 요구하는 시간적 및 공간적 해상도가 부족합니다. 본 논문에서는 위성 이미지와 지상 기상 관측소 네트워크의 시계열 데이터를 결합하여 일일 태양 복사 예측을 수행하는 새로운 심층 학습 모델인 SolarCrossFormer를 소개합니다. SolarCrossFormer는 입력 데이터의 상호 및 내부 모달 상관관계를 활용하여 예측의 정확성과 해상도를 향상시키기 위해 새로운 그래프 신경망을 사용합니다. 이 모델은 스위스 내의 모든 위치에 대해 최대 24시간 앞을 내다보는 15분 해상도의 확률적 예측을 생성합니다. SolarCrossFormer의 주요 장점 중 하나는 실제 운영에서의 견고성입니다. 모델을 재훈련하지 않고 새로운 시계열 데이터를 통합할 수 있으며, 추가적으로 좌표만을 사용하여 입력 데이터가 없는 위치에 대한 예측도 생성할 수 있습니다. 스위스 전역 127개 위치에 대한 1년간의 데이터셋을 대상으로 한 실험 결과, SolarCrossFormer는 예측 기간 동안 6.1%의 정규화된 평균 절대 오차를 나타냈습니다. 이 결과는 상업적 수치 기상 예측 서비스가 달성한 결과와 경쟁력이 있습니다.

## 📝 요약

이 논문에서는 대규모 태양광 발전 시스템의 전력망 통합을 위한 일일 태양 복사 예측을 개선하기 위해 SolarCrossFormer라는 새로운 딥러닝 모델을 소개합니다. 이 모델은 위성 이미지와 지상 기상 관측소의 시계열 데이터를 결합하여 예측의 정확성과 해상도를 높입니다. 특히, 새로운 그래프 신경망을 활용하여 입력 데이터의 상호 및 내부 모드 상관성을 활용합니다. SolarCrossFormer는 스위스 전역의 임의 위치에 대해 15분 간격으로 최대 24시간까지의 확률적 예측을 생성할 수 있으며, 새로운 시계열 데이터를 재학습 없이 통합할 수 있는 강점이 있습니다. 또한, 입력 데이터가 없는 위치에서도 좌표만으로 예측이 가능합니다. 스위스 127개 위치의 1년간 데이터 실험 결과, 예측 오차가 6.1%로 상업적 수치 예보 서비스와 경쟁력 있는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. SolarCrossFormer는 위성 이미지와 지상 기상 관측소의 시계열 데이터를 결합하여 일일 태양 복사 예측을 수행하는 새로운 딥러닝 모델입니다.

- 2. 이 모델은 입력 데이터의 상호 및 내부 모드 상관성을 활용하여 예측의 정확성과 해상도를 개선하는 그래프 신경망을 사용합니다.

- 3. SolarCrossFormer는 스위스 내 모든 위치에 대해 최대 24시간 앞을 예측하며, 15분 간격의 확률적 예측을 생성합니다.

- 4. 모델은 새로운 시계열 데이터를 추가 학습 없이 통합할 수 있으며, 좌표만으로 입력 데이터가 없는 위치의 예측도 가능합니다.

- 5. 실험 결과, SolarCrossFormer는 스위스 127개 위치에서 1년간의 데이터셋을 통해 6.1%의 정규화된 평균 절대 오차를 기록하며 상업적 수치 예보 서비스와 경쟁력 있는 성과를 보였습니다.

---

*Generated on 2025-09-22 15:25:14*