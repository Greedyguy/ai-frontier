# DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation

**Korean Title:** DIVEBATCH: 기울기 다양성 인식 배치 크기 적응을 통한 모델 훈련 가속화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Adaptive Batch Size, Gradient Diversity

## 🔗 유사한 논문
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (83.1% similar)
- [[2025-09-22/Generalization and Optimization of SGD with Lookahead_20250922|Generalization and Optimization of SGD with Lookahead]] (82.1% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (79.8% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.7% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16173v1 Announce Type: new 
Abstract: The goal of this paper is to accelerate the training of machine learning models, a critical challenge since the training of large-scale deep neural models can be computationally expensive. Stochastic gradient descent (SGD) and its variants are widely used to train deep neural networks. In contrast to traditional approaches that focus on tuning the learning rate, we propose a novel adaptive batch size SGD algorithm, DiveBatch, that dynamically adjusts the batch size. Adapting the batch size is challenging: using large batch sizes is more efficient due to parallel computation, but small-batch training often converges in fewer epochs and generalizes better. To address this challenge, we introduce a data-driven adaptation based on gradient diversity, enabling DiveBatch to maintain the generalization performance of small-batch training while improving convergence speed and computational efficiency. Gradient diversity has a strong theoretical justification: it emerges from the convergence analysis of SGD. Evaluations of DiveBatch on synthetic and CiFar-10, CiFar-100, and Tiny-ImageNet demonstrate that DiveBatch converges significantly faster than standard SGD and AdaBatch (1.06 -- 5.0x), with a slight trade-off in performance.

## 🔍 Abstract (한글 번역)

arXiv:2509.16173v1 발표 유형: 신규  
초록: 이 논문의 목표는 대규모 심층 신경망 모델의 훈련이 계산적으로 비용이 많이 들 수 있기 때문에 기계 학습 모델의 훈련을 가속화하는 것입니다. 확률적 경사 하강법(SGD) 및 그 변형은 심층 신경망을 훈련하는 데 널리 사용됩니다. 학습률 조정에 중점을 둔 전통적인 접근 방식과 달리, 우리는 배치 크기를 동적으로 조정하는 새로운 적응형 배치 크기 SGD 알고리즘인 DiveBatch를 제안합니다. 배치 크기를 조정하는 것은 도전적입니다: 큰 배치 크기는 병렬 계산 덕분에 더 효율적이지만, 작은 배치 훈련은 종종 더 적은 에포크에서 수렴하고 일반화 성능이 더 좋습니다. 이 문제를 해결하기 위해, 우리는 그래디언트 다양성에 기반한 데이터 기반 적응을 도입하여 DiveBatch가 작은 배치 훈련의 일반화 성능을 유지하면서 수렴 속도와 계산 효율성을 향상시킬 수 있도록 합니다. 그래디언트 다양성은 강력한 이론적 근거를 가지고 있습니다: 이는 SGD의 수렴 분석에서 나타납니다. DiveBatch를 합성 데이터 및 CiFar-10, CiFar-100, Tiny-ImageNet에서 평가한 결과, DiveBatch는 표준 SGD 및 AdaBatch보다 상당히 빠르게 수렴하며(1.06 -- 5.0배), 성능에 약간의 절충이 있음을 보여줍니다.

## 📝 요약

이 논문은 대규모 심층 신경망 모델의 학습을 가속화하기 위한 새로운 방법론을 제안합니다. 기존의 학습률 조정 대신, 이 논문에서는 배치 크기를 동적으로 조절하는 새로운 적응형 배치 크기 SGD 알고리즘인 DiveBatch를 소개합니다. DiveBatch는 그래디언트 다양성을 기반으로 배치 크기를 조정하여, 작은 배치 크기의 일반화 성능을 유지하면서도 수렴 속도와 계산 효율성을 향상시킵니다. 이 방법은 이론적으로도 SGD의 수렴 분석에서 유도된 그래디언트 다양성에 의해 뒷받침됩니다. DiveBatch는 CiFar-10, CiFar-100, Tiny-ImageNet 등에서 표준 SGD와 AdaBatch보다 최대 5배 빠르게 수렴하며, 성능에서 약간의 절충이 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 대규모 심층 신경망 모델의 훈련을 가속화하기 위한 새로운 적응형 배치 크기 SGD 알고리즘인 DiveBatch를 제안합니다.

- 2. DiveBatch는 배치 크기를 동적으로 조정하여 작은 배치 훈련의 일반화 성능을 유지하면서도 수렴 속도와 계산 효율성을 개선합니다.

- 3. DiveBatch는 경사 다양성에 기반한 데이터 기반 적응을 도입하여, 이론적으로도 SGD의 수렴 분석에서 그 정당성을 확보합니다.

- 4. DiveBatch는 CiFar-10, CiFar-100, Tiny-ImageNet 등의 평가에서 표준 SGD 및 AdaBatch보다 1.06배에서 5.0배까지 빠르게 수렴합니다.

- 5. DiveBatch는 성능에서 약간의 트레이드오프가 있지만, 수렴 속도와 계산 효율성에서 큰 개선을 보여줍니다.

---

*Generated on 2025-09-22 15:34:15*