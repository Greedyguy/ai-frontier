---
keywords:
  - Meta-Learning
  - Neural Networks
  - Hidden Proportion Metric
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:37:50.877577",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Meta-Learning",
    "Neural Networks",
    "Hidden Proportion Metric"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Meta-Learning": 0.8,
    "Neural Networks": 0.78,
    "Hidden Proportion Metric": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning

**Korean Title:** 희소 RNN의 균형 조정: 메타 학습에 유익한 하이퍼파라미터화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|sparse Recurrent Neural Networks]]
**🔗 Specific Connectable**: [[keywords/Meta-Learning|meta-learning]]
**⚡ Unique Technical**: [[keywords/Hidden Proportion Metric|hidden proportion]]

## 🔗 유사한 논문
- [[Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (79.4% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (78.9% similar)
- [[HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (78.1% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (78.0% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (77.9% similar)

## 📋 저자 정보

**Authors:** Quincy Hershey, Randy Paffenroth

## 📄 Abstract (원문)

This paper develops alternative hyperparameters for specifying sparse
Recurrent Neural Networks (RNNs). These hyperparameters allow for varying
sparsity within the trainable weight matrices of the model while improving
overall performance. This architecture enables the definition of a novel
metric, hidden proportion, which seeks to balance the distribution of unknowns
within the model and provides significant explanatory power of model
performance. Together, the use of the varied sparsity RNN architecture combined
with the hidden proportion metric generates significant performance gains while
improving performance expectations on an a priori basis. This combined approach
provides a path forward towards generalized meta-learning applications and
model optimization based on intrinsic characteristics of the data set,
including input and output dimensions.

## 🔍 Abstract (한글 번역)

이 논문은 희소 순환 신경망(RNN)을 지정하기 위한 대체 하이퍼파라미터를 개발합니다. 이러한 하이퍼파라미터는 모델의 학습 가능한 가중치 행렬 내에서 희소성을 다양하게 조정할 수 있게 하며, 전반적인 성능을 향상시킵니다. 이 아키텍처는 모델 내 미지수의 분포를 균형 있게 조정하고 모델 성능에 대한 중요한 설명력을 제공하는 새로운 지표인 '은닉 비율(hidden proportion)'을 정의할 수 있게 합니다. 다양한 희소성 RNN 아키텍처와 은닉 비율 지표의 결합 사용은 성능 기대치를 사전에 개선하면서도 상당한 성능 향상을 가져옵니다. 이러한 결합 접근법은 입력 및 출력 차원을 포함한 데이터 세트의 내재적 특성에 기반한 일반화된 메타 학습 응용 및 모델 최적화를 향한 진로를 제공합니다.

## 📝 요약

이 논문은 희소성 가중치를 가진 순환 신경망(RNN)을 위한 새로운 하이퍼파라미터를 개발했습니다. 이 하이퍼파라미터는 모델의 가중치 행렬 내 희소성을 조절하여 성능을 향상시킵니다. 또한, '숨겨진 비율'이라는 새로운 지표를 도입하여 모델 성능을 설명하는 데 중요한 역할을 합니다. 이러한 접근 방식은 다양한 희소성 RNN 아키텍처와 숨겨진 비율 지표를 결합하여 성능을 크게 향상시키고, 데이터 세트의 본질적 특성에 기반한 모델 최적화 및 메타 학습 응용에 기여합니다.

## 🎯 주요 포인트

- 1. 이 논문은 희소성을 조절할 수 있는 대체 하이퍼파라미터를 통해 희소 순환 신경망(RNN)을 개발합니다.

- 2. 새로운 메트릭인 'hidden proportion'을 정의하여 모델 내 미지수의 분포를 균형 있게 조절하고 성능 설명력을 제공합니다.

- 3. 다양한 희소성 RNN 아키텍처와 hidden proportion 메트릭의 결합은 성능 기대치를 사전에 개선하면서 성능 향상을 이끌어냅니다.

- 4. 이 접근법은 데이터 세트의 내재적 특성에 기반한 일반화된 메타 학습 응용 및 모델 최적화의 가능성을 제시합니다.

---

*Generated on 2025-09-20 01:06:19*