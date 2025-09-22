# Assessing invariance to affine transformations in image quality metrics

**Korean Title:** 이미지 품질 지표에서 아핀 변환에 대한 불변성 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Affine Transformations

## 🔗 유사한 논문
- [[2025-09-19/On the Role of Individual Differences in Current Approaches to Computational Image Aesthetics_20250919|On the Role of Individual Differences in Current Approaches to Computational Image Aesthetics]] (79.0% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence Label Quality, Domain Shift, Bias and Evaluation Challenges]] (78.8% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (78.8% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (78.2% similar)
- [[2025-09-17/Deconstructing Intraocular Pressure_ A Non-invasive Multi-Stage Probabilistic Inverse Framework_20250917|Deconstructing Intraocular Pressure A Non-invasive Multi-Stage Probabilistic Inverse Framework]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.17927v3 Announce Type: replace-cross 
Abstract: Subjective image quality metrics are usually evaluated according to the correlation with human opinion in databases with distortions that may appear in digital media. However, these oversee affine transformations which may represent better the changes in the images actually happening in natural conditions. Humans can be particularly invariant to these natural transformations, as opposed to the digital ones.
  In this work, we propose a methodology to evaluate any image quality metric by assessing their invariance to affine transformations, specifically: rotation, translation, scaling, and changes in spectral illumination. Here, invariance refers to the fact that certain distances should be neglected if their values are below a threshold. This is what we call invisibility threshold of a metric. Our methodology consists of two elements: (1) the determination of a visibility threshold in a subjective representation common to every metric, and (2) a transduction from the distance values of the metric and this common representation. This common representation is based on subjective ratings of readily available image quality databases. We determine the threshold in such common representation (the first element) using accurate psychophysics. Then, the transduction (the second element) can be trivially fitted for any metric: with the provided threshold extension of the method to any metric is straightforward. We test our methodology with some well-established metrics and find that none of them show human-like invisibility thresholds.
  This means that tuning the models exclusively to predict the visibility of generic distortions may disregard other properties of human vision as for instance invariances or invisibility thresholds. The data and code are publicly available to test other metrics.

## 🔍 Abstract (한글 번역)

arXiv:2407.17927v3 발표 유형: 교차 대체  
초록: 주관적인 이미지 품질 메트릭은 일반적으로 디지털 미디어에서 나타날 수 있는 왜곡이 있는 데이터베이스에서 인간의 의견과의 상관관계에 따라 평가됩니다. 그러나 이러한 메트릭은 실제 자연 조건에서 이미지에서 발생하는 변화를 더 잘 나타낼 수 있는 아핀 변환을 간과합니다. 인간은 디지털 변환과는 달리 이러한 자연 변환에 특히 불변일 수 있습니다.  
이 연구에서는 아핀 변환, 특히 회전, 평행 이동, 스케일링 및 스펙트럼 조명 변화에 대한 불변성을 평가하여 이미지 품질 메트릭을 평가하는 방법론을 제안합니다. 여기서 불변성은 특정 거리가 임계값 이하일 경우 무시되어야 한다는 사실을 의미합니다. 이를 메트릭의 비가시성 임계값이라고 합니다. 우리의 방법론은 두 가지 요소로 구성됩니다: (1) 모든 메트릭에 공통적인 주관적 표현에서 가시성 임계값의 결정, 그리고 (2) 메트릭의 거리 값과 이 공통 표현 간의 변환. 이 공통 표현은 쉽게 접근할 수 있는 이미지 품질 데이터베이스의 주관적 평가를 기반으로 합니다. 우리는 정확한 심리물리학을 사용하여 이러한 공통 표현에서의 임계값(첫 번째 요소)을 결정합니다. 그런 다음, 변환(두 번째 요소)은 모든 메트릭에 대해 간단히 적용할 수 있습니다: 제공된 임계값 확장을 통해 메트릭에 대한 방법의 적용이 간단합니다. 우리는 몇 가지 잘 확립된 메트릭으로 우리의 방법론을 테스트하였고, 그 중 어느 것도 인간과 유사한 비가시성 임계값을 보여주지 않는다는 것을 발견했습니다.  
이는 일반적인 왜곡의 가시성을 예측하기 위해 모델을 조정하는 것만으로는 예를 들어 불변성이나 비가시성 임계값과 같은 인간 시각의 다른 특성을 무시할 수 있음을 의미합니다. 데이터와 코드는 다른 메트릭을 테스트하기 위해 공개되어 있습니다.

## 📝 요약

이 논문은 주관적 이미지 품질 평가에서 인간의 시각적 불변성을 고려한 새로운 방법론을 제안합니다. 기존의 디지털 왜곡 중심 평가에서 벗어나 회전, 이동, 크기 조정, 조명 변화와 같은 자연적 변환에 대한 불변성을 평가합니다. 저자들은 '불가시성 임계값' 개념을 도입하여, 특정 거리 값이 임계값 이하일 경우 무시할 수 있는지를 평가합니다. 이 방법론은 두 가지 요소로 구성됩니다: (1) 모든 지표에 공통된 주관적 표현에서의 가시성 임계값 결정, (2) 지표의 거리 값과 이 공통 표현 간의 변환. 실험 결과, 기존의 잘 알려진 지표들은 인간과 유사한 불가시성 임계값을 보여주지 못했습니다. 이는 일반적인 왜곡 예측에만 초점을 맞추는 것이 인간 시각의 다른 특성, 예를 들어 불변성이나 불가시성 임계값을 간과할 수 있음을 시사합니다. 데이터와 코드는 다른 지표 테스트를 위해 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 주관적 이미지 품질 지표는 인간의 의견과의 상관관계를 통해 평가되지만, 자연 조건에서 실제로 발생하는 이미지 변화는 잘 반영하지 못한다.

- 2. 본 연구는 이미지 품질 지표의 아핀 변환에 대한 불변성을 평가하는 방법론을 제안하며, 회전, 이동, 스케일링, 스펙트럼 조명 변화 등을 포함한다.

- 3. 불변성은 특정 거리 값이 임계값 이하일 때 무시되어야 한다는 개념으로, 이를 '지표의 비가시성 임계값'이라고 정의한다.

- 4. 제안된 방법론은 모든 지표에 공통된 주관적 표현에서의 가시성 임계값 결정과 지표의 거리 값과 이 공통 표현 간의 변환으로 구성된다.

- 5. 실험 결과, 기존의 잘 확립된 지표들은 인간과 유사한 비가시성 임계값을 보여주지 못하며, 이는 일반적인 왜곡의 가시성 예측에만 초점을 맞춘 모델 튜닝이 인간 시각의 다른 특성을 간과할 수 있음을 시사한다.

---

*Generated on 2025-09-22 14:36:54*