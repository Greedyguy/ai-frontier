
# Tabular Data Generation Models: An In-Depth Survey and Performance Benchmarks with Extensive Tuning

**Korean Title:** 표 형식 데이터 생성 모델: 철저한 조사 및 성능 벤치마킹과 포괄적인 튜닝

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Dataset-specific Tuning|Dataset-specific Tuning]] [[keywords/broad/Generative Models|Generative Models]] [[keywords/broad/Tabular Data|Tabular Data]] [[keywords/specific/Diffusion-based Models|Diffusion-based Models]] [[keywords/unique/Feature Encodings|Feature Encodings]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dataset-specific Tuning
**🔬 Broad Technical**: Generative Models, Tabular Data
**🔗 Specific Connectable**: Diffusion-based Models
**⭐ Unique Technical**: Feature Encodings

**ArXiv ID**: [2406.12945](https://arxiv.org/abs/2406.12945)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2406.12945.pdf)


## 🏷️ 추출된 키워드



`Generative Models` • 

`Tabular Data` • 

`Diffusion-based Models` • 

`Feature Encodings` • 

`Dataset-specific Tuning`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.12945v4 Announce Type: replace 
Abstract: The ability to train generative models that produce realistic, safe and useful tabular data is essential for data privacy, imputation, oversampling, explainability or simulation. However, generating tabular data is not straightforward due to its heterogeneity, non-smooth distributions, complex dependencies and imbalanced categorical features. Although diverse methods have been proposed in the literature, there is a need for a unified evaluation, under the same conditions, on a variety of datasets. This study addresses this need by fully considering the optimization of: hyperparameters, feature encodings, and architectures. We investigate the impact of dataset-specific tuning on five recent model families for tabular data generation through an extensive benchmark on 16 datasets. These datasets vary in terms of size (an average of 80,000 rows), data types, and domains. We also propose a reduced search space for each model that allows for quick optimization, achieving nearly equivalent performance at a significantly lower cost. Our benchmark demonstrates that, for most models, large-scale dataset-specific tuning substantially improves performance compared to the original configurations. Furthermore, we confirm that diffusion-based models generally outperform other models on tabular data. However, this advantage is not significant when the entire tuning and training process is restricted to the same GPU budget.

## 🔍 Abstract (한글 번역)

arXiv:2406.12945v4 발표 유형: 대체
요약: 현실적이고 안전하며 유용한 테이블 데이터를 생성하는 생성 모델을 훈련하는 능력은 데이터 프라이버시, 대체, 오버샘플링, 설명 가능성 또는 시뮬레이션에 중요합니다. 그러나 테이블 데이터를 생성하는 것은 그의 이질성, 비부드러운 분포, 복잡한 의존성 및 불균형한 범주형 특징으로 인해 간단하지 않습니다. 문헌에서 다양한 방법이 제안되었지만, 다양한 데이터셋에 대해 동일한 조건에서 통합 평가가 필요합니다. 본 연구는 하이퍼파라미터, 특징 인코딩 및 아키텍처의 최적화를 완전히 고려하여 이러한 필요를 다룹니다. 우리는 16개의 데이터셋에 대한 광범위한 벤치마킹을 통해 테이블 데이터 생성을 위한 다섯 가지 최근 모델 패밀리에 대한 데이터셋별 튜닝의 영향을 조사합니다. 이러한 데이터셋은 크기(평균 80,000행), 데이터 유형 및 도메인 측면에서 다양합니다. 또한 각 모델에 대한 축소된 탐색 공간을 제안하여 빠른 최적화를 가능하게 하며, 상당히 낮은 비용으로 거의 동등한 성능을 달성합니다. 우리의 벤치마크는 대부분의 모델에 대해 대규모 데이터셋별 튜닝이 원래 구성보다 성능을 크게 향상시킨다는 것을 보여줍니다. 또한 확산 기반 모델이 일반적으로 다른 모델보다 테이블 데이터에서 우수한 성능을 보여준다는 것을 확인합니다. 그러나 전체 튜닝 및 훈련 프로세스를 동일한 GPU 예산으로 제한할 때 이 이점은 중요하지 않습니다.

## 📝 요약

본 연구는 다양한 데이터셋에 대해 하이퍼파라미터, 특성 인코딩, 아키텍처 최적화를 고려하여 탭러 데이터 생성을 평가하였다. 16가지 데이터셋을 대상으로 최근 모델 패밀리 5가지의 영향을 조사하였고, 대부분의 모델에서 대규모 데이터셋 특정 튜닝이 성능을 크게 향상시킨다는 것을 확인하였다. 확산 기반 모델이 다른 모델보다 일반적으로 우수한 성능을 보이지만, 동일한 GPU 예산 내에서 튜닝 및 훈련 과정을 제한할 경우 이 우위는 크지 않음을 확인하였다. 이를 통해 빠른 최적화를 허용하는 각 모델의 축소된 탐색 공간을 제안하였다.

## 🎯 주요 포인트


- 실제적이고 안전하며 유용한 타블러 데이터를 생성하는 생성 모델 훈련이 중요하다.

- 다양한 데이터셋에 대해 동일한 조건 하에 통합된 평가가 필요하다.

- 대규모 데이터셋에 대한 튜닝은 성능을 크게 향상시킬 수 있다.


---

*Generated on 2025-09-18 16:46:06*