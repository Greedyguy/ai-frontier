# Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution

**Korean Title:** 개선된 분포 하에서 반공간 기준 클래스를 학습하여 개인화된 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized Prediction

## 🔗 유사한 논문
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (79.7% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (79.6% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (79.6% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.5% similar)
- [[2025-09-22/Probabilistic Conformal Coverage Guarantees in Small-Data Settings_20250922|Probabilistic Conformal Coverage Guarantees in Small-Data Settings]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15592v1 Announce Type: new 
Abstract: In machine learning applications, predictive models are trained to serve future queries across the entire data distribution. Real-world data often demands excessively complex models to achieve competitive performance, however, sacrificing interpretability. Hence, the growing deployment of machine learning models in high-stakes applications, such as healthcare, motivates the search for methods for accurate and explainable predictions. This work proposes a Personalized Prediction scheme, where an easy-to-interpret predictor is learned per query. In particular, we wish to produce a "sparse linear" classifier with competitive performance specifically on some sub-population that includes the query point. The goal of this work is to study the PAC-learnability of this prediction model for sub-populations represented by "halfspaces" in a label-agnostic setting. We first give a distribution-specific PAC-learning algorithm for learning reference classes for personalized prediction. By leveraging both the reference-class learning algorithm and a list learner of sparse linear representations, we prove the first upper bound, $O(\mathrm{opt}^{1/4} )$, for personalized prediction with sparse linear classifiers and homogeneous halfspace subsets. We also evaluate our algorithms on a variety of standard benchmark data sets.

## 🔍 Abstract (한글 번역)

arXiv:2509.15592v1 발표 유형: 신규  
초록: 기계 학습 응용 분야에서 예측 모델은 전체 데이터 분포에 걸쳐 미래의 쿼리를 처리하도록 훈련됩니다. 실제 데이터는 경쟁력 있는 성능을 달성하기 위해 지나치게 복잡한 모델을 요구하는 경우가 많지만, 이는 해석 가능성을 희생합니다. 따라서 의료와 같은 고위험 응용 분야에서 기계 학습 모델의 사용이 증가함에 따라 정확하고 설명 가능한 예측 방법을 찾는 것이 중요해졌습니다. 본 연구는 쿼리마다 해석하기 쉬운 예측기를 학습하는 개인화된 예측 방식을 제안합니다. 특히, 우리는 쿼리 포인트를 포함하는 일부 하위 인구에서 경쟁력 있는 성능을 가진 "희소 선형" 분류기를 생성하고자 합니다. 이 연구의 목표는 레이블에 무관한 설정에서 "반공간"으로 표현되는 하위 인구에 대한 이 예측 모델의 PAC 학습 가능성을 연구하는 것입니다. 우리는 먼저 개인화된 예측을 위한 참조 클래스를 학습하기 위한 분포 특화 PAC 학습 알고리즘을 제시합니다. 참조 클래스 학습 알고리즘과 희소 선형 표현의 리스트 학습기를 활용하여, 희소 선형 분류기와 동질적 반공간 하위 집합을 사용한 개인화된 예측에 대한 최초의 상한선, $O(\mathrm{opt}^{1/4} )$, 을 증명합니다. 또한 다양한 표준 벤치마크 데이터 세트에서 우리의 알고리즘을 평가합니다.

## 📝 요약

이 연구는 고위험 분야에서의 기계 학습 모델의 해석 가능성과 정확성을 개선하기 위해 개인화된 예측 방식을 제안합니다. 각 쿼리에 대해 해석이 쉬운 예측기를 학습하여, 특정 하위 집단에서 경쟁력 있는 성능을 발휘하는 "희소 선형" 분류기를 생성하는 것이 목표입니다. 이 연구는 레이블에 무관한 설정에서 하위 집단을 나타내는 "반공간"에 대한 PAC-학습 가능성을 조사합니다. 연구 결과, 개인화된 예측을 위한 참조 클래스 학습 알고리즘과 희소 선형 표현의 목록 학습기를 활용하여, 희소 선형 분류기와 동질적 반공간 하위 집합을 사용하는 개인화된 예측에 대해 최초의 상한선 $O(\mathrm{opt}^{1/4} )$을 증명했습니다. 다양한 표준 벤치마크 데이터 세트에서 알고리즘을 평가했습니다.

## 🎯 주요 포인트

- 1. 머신러닝 모델의 복잡성은 성능을 높이지만 해석 가능성을 희생시킨다.

- 2. 이 연구는 각 쿼리에 대해 해석이 쉬운 예측기를 학습하는 개인화된 예측 방식을 제안한다.

- 3. 쿼리 포인트를 포함하는 하위 인구 집단에 대해 경쟁력 있는 성능을 가진 "희소 선형" 분류기를 생성하는 것이 목표이다.

- 4. 개인화된 예측을 위한 PAC-학습 가능성을 연구하며, 레이블에 무관한 설정에서 "반공간"으로 표현된 하위 인구 집단을 대상으로 한다.

- 5. 제안된 알고리즘은 다양한 표준 벤치마크 데이터 세트에서 평가되었다.

---

*Generated on 2025-09-22 15:20:50*