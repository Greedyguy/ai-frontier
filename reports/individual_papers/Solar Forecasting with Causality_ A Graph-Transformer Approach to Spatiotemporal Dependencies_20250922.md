# Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies

**Korean Title:** 태양 예측과 인과성: 시공간적 종속성에 대한 그래프-트랜스포머 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Causality in Solar Forecasting

## 🔗 유사한 논문
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (82.6% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (79.6% similar)
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (78.4% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (78.3% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (78.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15481v1 Announce Type: new 
Abstract: Accurate solar forecasting underpins effective renewable energy management. We present SolarCAST, a causally informed model predicting future global horizontal irradiance (GHI) at a target site using only historical GHI from site X and nearby stations S - unlike prior work that relies on sky-camera or satellite imagery requiring specialized hardware and heavy preprocessing. To deliver high accuracy with only public sensor data, SolarCAST models three classes of confounding factors behind X-S correlations using scalable neural components: (i) observable synchronous variables (e.g., time of day, station identity), handled via an embedding module; (ii) latent synchronous factors (e.g., regional weather patterns), captured by a spatio-temporal graph neural network; and (iii) time-lagged influences (e.g., cloud movement across stations), modeled with a gated transformer that learns temporal shifts. It outperforms leading time-series and multimodal baselines across diverse geographical conditions, and achieves a 25.9% error reduction over the top commercial forecaster, Solcast. SolarCAST offers a lightweight, practical, and generalizable solution for localized solar forecasting.

## 🔍 Abstract (한글 번역)

arXiv:2509.15481v1 발표 유형: 신규  
초록: 정확한 태양 예측은 효과적인 재생 가능 에너지 관리를 뒷받침합니다. 우리는 SolarCAST를 소개합니다. 이 모델은 하늘 카메라나 위성 이미지와 같은 특수 하드웨어와 복잡한 전처리를 필요로 하는 이전 연구와 달리, 사이트 X와 인근 관측소 S의 과거 전역 수평 일사량(GHI)만을 사용하여 목표 지점의 미래 GHI를 예측하는 인과적으로 정보가 제공된 모델입니다. 공개된 센서 데이터만으로 높은 정확도를 제공하기 위해, SolarCAST는 X-S 상관관계의 세 가지 유형의 교란 요인을 확장 가능한 신경 구성 요소를 사용하여 모델링합니다: (i) 관측 가능한 동시 변수(예: 시간대, 관측소 식별), 임베딩 모듈을 통해 처리; (ii) 잠재 동시 요인(예: 지역 날씨 패턴), 시공간 그래프 신경망으로 포착; (iii) 시간 지연 영향(예: 관측소 간 구름 이동), 시간적 변화를 학습하는 게이트 트랜스포머로 모델링. 다양한 지리적 조건에서 선도적인 시계열 및 다중 모달 기준을 능가하며, 상업적 예측 1위인 Solcast에 비해 25.9%의 오류 감소를 달성합니다. SolarCAST는 지역화된 태양 예측을 위한 경량, 실용적, 일반화 가능한 솔루션을 제공합니다.

## 📝 요약

SolarCAST는 역사적 글로벌 수평면 일사량(GHI) 데이터만을 이용해 특정 지역의 미래 GHI를 예측하는 모델로, 기존의 하드웨어 의존적인 방법을 대체합니다. 이 모델은 세 가지 혼란 요인을 다루기 위해 확장 가능한 신경망 구성 요소를 사용합니다: (i) 관측 가능한 동기 변수는 임베딩 모듈로 처리하고, (ii) 잠재적인 동기 요인은 시공간 그래프 신경망으로 포착하며, (iii) 시간 지연 영향은 게이트 트랜스포머로 모델링합니다. 다양한 지리적 조건에서 기존의 시계열 및 다중 모달 기법을 능가하며, 상업적 예측 모델 Solcast 대비 25.9%의 오류 감소를 달성합니다. SolarCAST는 경량화된 실용적이고 일반화 가능한 지역 태양광 예측 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. SolarCAST는 역사적 GHI 데이터만을 사용하여 목표 지점의 미래 GHI를 예측하는 모델로, 전문 하드웨어나 복잡한 전처리가 필요하지 않습니다.

- 2. 이 모델은 X-S 상관관계의 혼란 요인을 세 가지 범주로 나누어 처리하며, 각각을 확장 가능한 신경망 구성 요소로 모델링합니다.

- 3. SolarCAST는 다양한 지리적 조건에서 기존의 시계열 및 다중 모달 베이스라인을 능가하며, 상업용 예측기 Solcast 대비 25.9%의 오류 감소를 달성했습니다.

- 4. 이 모델은 지역화된 태양 예측을 위한 경량, 실용적, 일반화 가능한 솔루션을 제공합니다.

---

*Generated on 2025-09-22 15:15:33*