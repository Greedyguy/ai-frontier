# Toward Efficient Influence Function: Dropout as a Compression Tool

**Korean Title:** 효율적인 영향 함수로 나아가기: 압축 도구로서의 드롭아웃

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Gradient Compression, Influence Function

## 🔗 유사한 논문
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (81.9% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (79.7% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (78.7% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (78.0% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15651v1 Announce Type: cross 
Abstract: Assessing the impact the training data on machine learning models is crucial for understanding the behavior of the model, enhancing the transparency, and selecting training data. Influence function provides a theoretical framework for quantifying the effect of training data points on model's performance given a specific test data. However, the computational and memory costs of influence function presents significant challenges, especially for large-scale models, even when using approximation methods, since the gradients involved in computation are as large as the model itself. In this work, we introduce a novel approach that leverages dropout as a gradient compression mechanism to compute the influence function more efficiently. Our method significantly reduces computational and memory overhead, not only during the influence function computation but also in gradient compression process. Through theoretical analysis and empirical validation, we demonstrate that our method could preserves critical components of the data influence and enables its application to modern large-scale models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15651v1 발표 유형: 교차  
초록: 머신 러닝 모델의 학습 데이터가 모델에 미치는 영향을 평가하는 것은 모델의 행동을 이해하고, 투명성을 높이며, 학습 데이터를 선택하는 데 있어 매우 중요합니다. 영향 함수는 특정 테스트 데이터가 주어졌을 때 학습 데이터 포인트가 모델 성능에 미치는 영향을 정량화할 수 있는 이론적 틀을 제공합니다. 그러나 영향 함수의 계산 및 메모리 비용은 특히 대규모 모델의 경우 상당한 도전 과제를 제시합니다. 근사 방법을 사용하더라도 계산에 관련된 기울기가 모델 자체만큼 크기 때문입니다. 본 연구에서는 드롭아웃을 기울기 압축 메커니즘으로 활용하여 영향 함수를 보다 효율적으로 계산하는 새로운 접근 방식을 소개합니다. 우리의 방법은 영향 함수 계산뿐만 아니라 기울기 압축 과정에서도 계산 및 메모리 오버헤드를 크게 줄입니다. 이론적 분석과 실증적 검증을 통해 우리의 방법이 데이터 영향의 중요한 요소를 보존하고 현대 대규모 모델에 적용할 수 있음을 입증합니다.

## 📝 요약

이 논문은 머신러닝 모델의 훈련 데이터가 모델 성능에 미치는 영향을 평가하는 방법을 제시합니다. 기존의 영향 함수는 계산 비용과 메모리 사용량이 커 대규모 모델에 적용하기 어려웠습니다. 본 연구에서는 드롭아웃을 활용한 새로운 접근법을 통해 영향 함수 계산의 효율성을 높였습니다. 이 방법은 계산 및 메모리 부담을 줄이면서도 데이터 영향의 중요한 요소를 유지하여, 대규모 모델에도 적용 가능함을 이론적 분석과 실험을 통해 입증했습니다.

## 🎯 주요 포인트

- 1. 머신러닝 모델의 훈련 데이터가 모델 성능에 미치는 영향을 평가하는 것은 모델의 행동을 이해하고 투명성을 높이며 훈련 데이터를 선택하는 데 중요하다.

- 2. 영향 함수는 특정 테스트 데이터에 대해 훈련 데이터 포인트가 모델 성능에 미치는 영향을 정량화하는 이론적 틀을 제공한다.

- 3. 본 연구는 드롭아웃을 활용한 새로운 접근법을 제안하여 영향 함수를 보다 효율적으로 계산하고자 한다.

- 4. 제안된 방법은 영향 함수 계산과 그래디언트 압축 과정에서의 계산 및 메모리 부담을 크게 줄인다.

- 5. 이 방법은 대규모 모델에 적용 가능하며, 데이터 영향의 중요한 요소를 보존함을 이론적 분석과 실증적 검증을 통해 입증하였다.

---

*Generated on 2025-09-22 14:06:26*