# Aircraft Fuel Flow Modelling with Ageing Effects: From Parametric Corrections to Neural Networks

**Korean Title:** 항공기 연료 흐름 모델링의 노화 효과: 매개변수 보정에서 신경망까지

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Engine Ageing Effects Integration

## 🔗 유사한 논문
- [[2025-09-22/Partial Column Generation with Graph Neural Networks for Team Formation and Routing_20250922|Partial Column Generation with Graph Neural Networks for Team Formation and Routing]] (76.7% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (76.6% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (75.9% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (75.7% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (75.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15736v1 Announce Type: new 
Abstract: Accurate modelling of aircraft fuel-flow is crucial for both operational planning and environmental impact assessment, yet standard parametric models often neglect performance deterioration that occurs as aircraft age. This paper investigates multiple approaches to integrate engine ageing effects into fuel-flow prediction for the Airbus A320-214, using a comprehensive dataset of approximately nineteen thousand Quick Access Recorder flights from nine distinct airframes with varying years in service. We systematically evaluate classical physics-based models, empirical correction coefficients, and data-driven neural network architectures that incorporate age either as an input feature or as an explicit multiplicative bias. Results demonstrate that while baseline models consistently underestimate fuel consumption for older aircraft, the use of age-dependent correction factors and neural models substantially reduces bias and improves prediction accuracy. Nevertheless, limitations arise from the small number of airframes and the lack of detailed maintenance event records, which constrain the representativeness and generalization of age-based corrections. This study emphasizes the importance of accounting for the effects of ageing in parametric and machine learning frameworks to improve the reliability of operational and environmental assessments. The study also highlights the need for more diverse datasets that can capture the complexity of real-world engine deterioration.

## 🔍 Abstract (한글 번역)

arXiv:2509.15736v1 발표 유형: 신규  
초록: 항공기 연료 흐름의 정확한 모델링은 운영 계획과 환경 영향 평가 모두에 있어 매우 중요하지만, 표준 매개변수 모델은 항공기가 노후화됨에 따라 발생하는 성능 저하를 종종 간과합니다. 본 논문은 약 19,000회의 Quick Access Recorder 비행 데이터를 사용하여 Airbus A320-214의 연료 흐름 예측에 엔진 노후화 효과를 통합하는 여러 접근 방식을 조사합니다. 이 데이터는 서비스 연수가 다양한 9개의 서로 다른 기체에서 수집되었습니다. 우리는 고전적인 물리 기반 모델, 경험적 보정 계수, 그리고 나이를 입력 특징 또는 명시적인 곱셈 편향으로 통합하는 데이터 기반 신경망 구조를 체계적으로 평가합니다. 결과는 기본 모델이 오래된 항공기의 연료 소비를 지속적으로 과소평가하는 반면, 나이 의존적인 보정 계수와 신경망 모델의 사용이 편향을 크게 줄이고 예측 정확성을 향상시킨다는 것을 보여줍니다. 그럼에도 불구하고, 기체의 수가 적고 상세한 유지보수 이벤트 기록이 부족하여 나이 기반 보정의 대표성과 일반화에 제약이 따릅니다. 본 연구는 운영 및 환경 평가의 신뢰성을 향상시키기 위해 매개변수 및 기계 학습 프레임워크에서 노후화 효과를 고려하는 것이 중요하다는 점을 강조합니다. 또한, 실제 엔진 열화의 복잡성을 포착할 수 있는 보다 다양한 데이터 세트의 필요성을 강조합니다.

## 📝 요약

이 논문은 에어버스 A320-214 항공기의 연료 흐름 예측에 엔진 노후화 효과를 통합하는 여러 접근법을 조사합니다. 약 19,000개의 비행 데이터를 사용하여, 물리 기반 모델, 경험적 보정 계수, 나이 정보를 포함한 데이터 기반 신경망 구조를 평가했습니다. 결과적으로, 나이에 따른 보정 계수와 신경망 모델이 예측 정확도를 향상시키는 데 효과적임을 발견했습니다. 그러나 소수의 항공기 데이터와 유지보수 기록 부족은 한계로 작용했습니다. 이 연구는 노후화 효과를 고려한 모델링의 중요성을 강조하며, 보다 다양한 데이터셋의 필요성을 제기합니다.

## 🎯 주요 포인트

- 1. 항공기 연료 소모 모델링에서 엔진 노후화 효과를 통합하는 것이 중요하며, 이는 에어버스 A320-214의 연료 소모 예측에 적용되었다.

- 2. 나이 의존적 보정 계수와 신경망 모델을 사용하면 노후 항공기의 연료 소비 예측 정확도가 크게 향상된다.

- 3. 소수의 기체와 유지보수 이벤트 기록 부족은 나이 기반 보정의 대표성과 일반화를 제한한다.

- 4. 노후화 효과를 고려한 모델링은 운영 및 환경 평가의 신뢰성을 높이는 데 중요하다.

- 5. 실제 엔진 열화의 복잡성을 포착할 수 있는 보다 다양한 데이터셋의 필요성이 강조된다.

---

*Generated on 2025-09-22 15:22:41*