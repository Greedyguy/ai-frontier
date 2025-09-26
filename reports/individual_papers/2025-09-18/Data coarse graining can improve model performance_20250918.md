---
keywords:
  - Data Coarse Graining
  - High-Pass Scheme
  - Ridge-Regularized Linear Regression
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:33:38.696919",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Data Coarse Graining",
    "High-Pass Scheme",
    "Ridge-Regularized Linear Regression"
  ],
  "rejected_keywords": [
    "Renormalization Group"
  ],
  "similarity_scores": {
    "Data Coarse Graining": 0.78,
    "High-Pass Scheme": 0.75,
    "Ridge-Regularized Linear Regression": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Data coarse graining can improve model performance

**Korean Title:** 데이터 거칠기(coarse graining)는 모델 성능을 향상시킬 수 있습니다.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Ridge-Regularized Linear Regression|ridge-regularized linear regression]]
**⚡ Unique Technical**: [[keywords/Data Coarse Graining|data coarse graining]], [[keywords/High-Pass Scheme|high-pass scheme]]

## 🔗 유사한 논문
- [[Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (81.8% similar)
- [[CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (81.3% similar)
- [[Not All Degradations Are Equal_ A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution_20250918|Not All Degradations Are Equal A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution]] (80.7% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (80.6% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.5% similar)

## 📋 저자 정보

**Authors:** Alex Nguyen, David J. Schwab, Vudtiwat Ngampruetikorn

## 📄 Abstract (원문)

Lossy data transformations by definition lose information. Yet, in modern
machine learning, methods like data pruning and lossy data augmentation can
help improve generalization performance. We study this paradox using a solvable
model of high-dimensional, ridge-regularized linear regression under 'data
coarse graining.' Inspired by the renormalization group in statistical physics,
we analyze coarse-graining schemes that systematically discard features based
on their relevance to the learning task. Our results reveal a nonmonotonic
dependence of the prediction risk on the degree of coarse graining. A
'high-pass' scheme--which filters out less relevant, lower-signal features--can
help models generalize better. By contrast, a 'low-pass' scheme that integrates
out more relevant, higher-signal features is purely detrimental. Crucially,
using optimal regularization, we demonstrate that this nonmonotonicity is a
distinct effect of data coarse graining and not an artifact of double descent.
Our framework offers a clear, analytical explanation for why careful data
augmentation works: it strips away less relevant degrees of freedom and
isolates more predictive signals. Our results highlight a complex, nonmonotonic
risk landscape shaped by the structure of the data, and illustrate how ideas
from statistical physics provide a principled lens for understanding modern
machine learning phenomena.

## 🔍 Abstract (한글 번역)

손실 데이터 변환은 정의상 정보를 잃습니다. 그러나 현대 기계 학습에서는 데이터 가지치기 및 손실 데이터 증강과 같은 방법이 일반화 성능을 향상시키는 데 도움이 될 수 있습니다. 우리는 '데이터 거칠기' 하에서 고차원, 릿지 정규화 선형 회귀의 해결 가능한 모델을 사용하여 이 역설을 연구합니다. 통계 물리학의 재규격화 군에서 영감을 받아, 학습 과제와의 관련성에 따라 체계적으로 특징을 버리는 거칠기 방식을 분석합니다. 우리의 결과는 예측 위험이 거칠기 정도에 따라 비단조적으로 의존함을 보여줍니다. '고역 통과' 방식—덜 관련성 있는, 낮은 신호 특징을 걸러내는 방식—은 모델이 더 잘 일반화하는 데 도움이 될 수 있습니다. 반대로, 더 관련성 있는, 높은 신호 특징을 통합하는 '저역 통과' 방식은 순전히 해롭습니다. 중요한 것은, 최적의 정규화를 사용하여, 우리는 이러한 비단조성이 데이터 거칠기의 독특한 효과이며 이중 하강의 산물이 아님을 입증합니다. 우리의 프레임워크는 왜 신중한 데이터 증강이 효과적인지를 명확하고 분석적으로 설명합니다: 덜 관련성 있는 자유도를 제거하고 더 예측적인 신호를 고립시킵니다. 우리의 결과는 데이터 구조에 의해 형성된 복잡하고 비단조적인 위험 지형을 강조하며, 통계 물리학의 아이디어가 현대 기계 학습 현상을 이해하는 데 원칙적인 렌즈를 제공함을 보여줍니다.

## 📝 요약

이 논문은 정보 손실을 수반하는 데이터 변환이 어떻게 머신러닝의 일반화 성능을 향상시킬 수 있는지를 고차원 릿지 정규화 선형 회귀 모델을 통해 분석합니다. 통계 물리학의 재규격화 군에서 영감을 받아, 학습 과제와 관련된 특징을 체계적으로 버리는 '데이터 조잡화' 방법을 연구했습니다. 연구 결과, 예측 위험이 조잡화 정도에 따라 비단조적으로 변화하며, 덜 중요한 특징을 제거하는 '고역통과' 방식이 모델의 일반화 성능을 향상시킬 수 있음을 발견했습니다. 반면, 중요한 특징을 제거하는 '저역통과' 방식은 해롭습니다. 최적의 정규화를 통해 이러한 비단조성이 데이터 조잡화의 고유한 효과임을 입증했습니다. 이 연구는 데이터 구조에 의해 형성된 복잡한 위험 지형을 강조하며, 통계 물리학의 개념이 현대 머신러닝 현상을 이해하는 데 유용함을 보여줍니다.

## 🎯 주요 포인트

- 1. 정보 손실을 수반하는 데이터 변환이 일반화 성능을 향상시킬 수 있음을 연구했습니다.

- 2. 데이터의 관련성에 따라 특징을 체계적으로 버리는 '데이터 조대화' 방식을 분석했습니다.

- 3. '하이패스' 방식은 덜 관련 있는 특징을 걸러내어 모델의 일반화를 돕습니다.

- 4. '로우패스' 방식은 더 관련 있는 특징을 통합하여 모델 성능에 해롭습니다.

- 5. 최적의 정규화를 사용하면 데이터 조대화의 비단조적 효과가 두드러지며, 이는 이중 하강의 인공물이 아님을 입증했습니다.

---

*Generated on 2025-09-20 05:54:13*