# Differentially private federated learning for localized control of infectious disease dynamics

**Korean Title:** 전염병 역학의 지역적 제어를 위한 차등 프라이버시 연합 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Raouf Kerkouche|Raouf Kerkouche]] [[authors/Henrik Zunker|Henrik Zunker]] [[authors/Mario Fritz|Mario Fritz]] [[authors/Martin J. Kühn|Martin J. Kühn]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Client-level Differential Privacy

## 🔗 유사한 논문
- [[Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning Mitigating Inference Attacks with Randomized Response]] (82.3% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (80.0% similar)
- [[Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking_20250918|Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking]] (79.2% similar)
- [[SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench A Benchmark for Differentially Private Text Generation]] (78.8% similar)
- [[Towards Trustworthy Vital Sign Forecasting_ Leveraging Uncertainty for Prediction Intervals_20250918|Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (78.3% similar)

## 📋 저자 정보

**Authors:** Raouf Kerkouche, Henrik Zunker, Mario Fritz, Martin J. Kühn

## 📄 Abstract (원문)

In times of epidemics, swift reaction is necessary to mitigate epidemic
spreading. For this reaction, localized approaches have several advantages,
limiting necessary resources and reducing the impact of interventions on a
larger scale. However, training a separate machine learning (ML) model on a
local scale is often not feasible due to limited available data. Centralizing
the data is also challenging because of its high sensitivity and privacy
constraints. In this study, we consider a localized strategy based on the
German counties and communities managed by the related local health authorities
(LHA). For the preservation of privacy to not oppose the availability of
detailed situational data, we propose a privacy-preserving forecasting method
that can assist public health experts and decision makers. ML methods with
federated learning (FL) train a shared model without centralizing raw data.
Considering the counties, communities or LHAs as clients and finding a balance
between utility and privacy, we study a FL framework with client-level
differential privacy (DP). We train a shared multilayer perceptron on sliding
windows of recent case counts to forecast the number of cases, while clients
exchange only norm-clipped updates and the server aggregated updates with DP
noise. We evaluate the approach on COVID-19 data on county-level during two
phases. As expected, very strict privacy yields unstable, unusable forecasts.
At a moderately strong level, the DP model closely approaches the non-DP model:
$R^2= 0.94$ (vs. 0.95) and mean absolute percentage error (MAPE) of 26 % in
November 2020; $R^2= 0.88$ (vs. 0.93) and MAPE of 21 % in March 2022. Overall,
client-level DP-FL can deliver useful county-level predictions with strong
privacy guarantees, and viable privacy budgets depend on epidemic phase,
allowing privacy-compliant collaboration among health authorities for local
forecasting.

## 🔍 Abstract (한글 번역)

전염병 발생 시, 전염병 확산을 완화하기 위해 신속한 대응이 필요합니다. 이러한 대응을 위해, 지역화된 접근 방식은 필요한 자원을 제한하고 대규모 개입의 영향을 줄이는 등 여러 가지 장점을 가지고 있습니다. 그러나 지역 규모에서 별도의 기계 학습(ML) 모델을 훈련하는 것은 가용 데이터가 제한되어 있어 종종 실행 가능하지 않습니다. 데이터의 중앙 집중화 또한 높은 민감성과 개인정보 보호 제약 때문에 어려움을 겪습니다. 본 연구에서는 관련 지역 보건 당국(LHA)이 관리하는 독일의 군(counties)과 커뮤니티를 기반으로 한 지역화 전략을 고려합니다. 개인정보 보호가 상세한 상황 데이터의 가용성을 방해하지 않도록, 우리는 공중 보건 전문가와 의사 결정자를 지원할 수 있는 개인정보 보호 예측 방법을 제안합니다. 연합 학습(FL)을 활용한 ML 방법은 원시 데이터를 중앙 집중화하지 않고 공유 모델을 훈련합니다. 군, 커뮤니티 또는 LHA를 클라이언트로 간주하고 유용성과 개인정보 보호 사이의 균형을 찾기 위해, 우리는 클라이언트 수준 차등 개인정보 보호(DP)를 적용한 FL 프레임워크를 연구합니다. 최근 사례 수의 슬라이딩 윈도우에서 공유 다층 퍼셉트론을 훈련하여 사례 수를 예측하며, 클라이언트는 노름 절단된 업데이트만 교환하고 서버는 DP 노이즈로 업데이트를 집계합니다. 우리는 두 단계에 걸쳐 군 수준의 COVID-19 데이터를 바탕으로 접근 방식을 평가합니다. 예상대로, 매우 엄격한 개인정보 보호는 불안정하고 사용 불가능한 예측을 초래합니다. 중간 강도의 수준에서는 DP 모델이 비-DP 모델에 근접합니다: 2020년 11월에 $R^2= 0.94$ (vs. 0.95) 및 평균 절대 백분율 오차(MAPE) 26%; 2022년 3월에 $R^2= 0.88$ (vs. 0.93) 및 MAPE 21%. 전반적으로, 클라이언트 수준의 DP-FL은 강력한 개인정보 보호 보장을 제공하면서 유용한 군 수준 예측을 제공할 수 있으며, 실행 가능한 개인정보 보호 예산은 전염병 단계에 따라 달라져, 지역 예측을 위한 보건 당국 간의 개인정보 보호 준수 협업을 허용합니다.

## 📝 요약

이 연구는 전염병 확산을 완화하기 위한 지역 기반 접근법을 제안합니다. 독일의 지역 보건 당국을 중심으로, 민감한 데이터를 중앙화하지 않고도 프라이버시를 보장하는 예측 방법을 개발했습니다. 연합 학습(FL)과 클라이언트 수준 차등 프라이버시(DP)를 활용하여, 각 지역을 클라이언트로 간주하고, 최근 사례 수를 기반으로 다층 퍼셉트론을 훈련하여 사례 수를 예측합니다. COVID-19 데이터를 사용한 실험에서, 적절한 프라이버시 수준에서 DP 모델은 비-DP 모델과 유사한 성능을 보였습니다. 이 방법은 강력한 프라이버시 보장을 제공하면서도 유용한 예측을 가능하게 하며, 전염병 단계에 따라 적절한 프라이버시 예산을 설정할 수 있습니다.

## 🎯 주요 포인트

- 1. 전염병 확산을 완화하기 위해서는 신속한 대응이 필요하며, 지역화된 접근 방식이 자원 절약과 개입의 대규모 영향을 줄이는 데 유리하다.

- 2. 중앙집중식 데이터 수집의 어려움을 해결하기 위해, 독일의 지역 보건 당국을 기반으로 한 지역화된 전략을 제안한다.

- 3. 프라이버시를 보장하면서도 상세한 상황 데이터를 활용하기 위해, 연합 학습(FL)과 클라이언트 수준의 차등 프라이버시(DP)를 적용한 예측 방법을 제안한다.

- 4. COVID-19 데이터를 활용한 실험에서, 적절한 수준의 프라이버시 모델은 비프라이버시 모델과 유사한 예측 성능을 보였다.

- 5. 클라이언트 수준의 DP-FL은 강력한 프라이버시 보장을 제공하면서도 유용한 지역 예측을 가능하게 하며, 전염병 단계에 따라 적절한 프라이버시 예산이 필요하다.

---

*Generated on 2025-09-20 09:18:02*