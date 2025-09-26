---
keywords:
  - Convolutional Neural Networks
  - Optimization
  - EEG Frequency Bands
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:54:52.074003",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convolutional Neural Networks",
    "Optimization",
    "EEG Frequency Bands"
  ],
  "rejected_keywords": [
    "Deep Dense Network"
  ],
  "similarity_scores": {
    "Convolutional Neural Networks": 0.88,
    "Optimization": 0.78,
    "EEG Frequency Bands": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques

**Korean Title:** 뇌 반구 상태와 주파수 대역 간의 관계를 심층 학습 최적화 기법을 통해 탐구하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Adagrad Optimizer]]
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|Convolutional Neural Network]]
**⚡ Unique Technical**: [[keywords/EEG Frequency Bands|EEG Frequency Bands]]

## 🔗 유사한 논문
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (80.1% similar)
- [[HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C Efficient Medical Data Classification for Embedded Devices]] (79.5% similar)
- [[Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (79.4% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (78.8% similar)
- [[UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (78.2% similar)

## 📋 저자 정보

**Authors:** Robiul Islam, Dmitry I. Ignatov, Karl Kaberg, Roman Nabatchikov

## 📄 Abstract (원문)

This study investigates classifier performance across EEG frequency bands
using various optimizers and evaluates efficient class prediction for the left
and right hemispheres. Three neural network architectures - a deep dense
network, a shallow three-layer network, and a convolutional neural network
(CNN) - are implemented and compared using the TensorFlow and PyTorch
frameworks. Results indicate that the Adagrad and RMSprop optimizers
consistently perform well across different frequency bands, with Adadelta
exhibiting robust performance in cross-model evaluations. Specifically, Adagrad
excels in the beta band, while RMSprop achieves superior performance in the
gamma band. Conversely, SGD and FTRL exhibit inconsistent performance. Among
the models, the CNN demonstrates the second highest accuracy, particularly in
capturing spatial features of EEG data. The deep dense network shows
competitive performance in learning complex patterns, whereas the shallow
three-layer network, sometimes being less accurate, provides computational
efficiency. SHAP (Shapley Additive Explanations) plots are employed to identify
efficient class prediction, revealing nuanced contributions of EEG frequency
bands to model accuracy. Overall, the study highlights the importance of
optimizer selection, model architecture, and EEG frequency band analysis in
enhancing classifier performance and understanding feature importance in
neuroimaging-based classification tasks.

## 🔍 Abstract (한글 번역)

이 연구는 다양한 최적화 기법을 사용하여 EEG 주파수 대역에서의 분류기 성능을 조사하고, 좌우 반구에 대한 효율적인 클래스 예측을 평가합니다. 세 가지 신경망 아키텍처 - 심층 밀집 네트워크, 얕은 3층 네트워크, 그리고 합성곱 신경망(CNN) - 가 TensorFlow와 PyTorch 프레임워크를 사용하여 구현되고 비교됩니다. 결과에 따르면, Adagrad와 RMSprop 최적화 기법은 다양한 주파수 대역에서 일관되게 우수한 성능을 보이며, Adadelta는 모델 간 평가에서 견고한 성능을 나타냅니다. 구체적으로, Adagrad는 베타 대역에서 뛰어난 성능을 보이며, RMSprop은 감마 대역에서 우수한 성능을 달성합니다. 반면, SGD와 FTRL은 일관되지 않은 성능을 보입니다. 모델 중에서, CNN은 특히 EEG 데이터의 공간적 특징을 포착하는 데 있어 두 번째로 높은 정확도를 보입니다. 심층 밀집 네트워크는 복잡한 패턴을 학습하는 데 경쟁력 있는 성능을 보이는 반면, 얕은 3층 네트워크는 때때로 덜 정확하지만 계산 효율성을 제공합니다. SHAP(Shapley Additive Explanations) 플롯은 효율적인 클래스 예측을 식별하는 데 사용되며, EEG 주파수 대역이 모델 정확도에 미치는 미묘한 기여를 드러냅니다. 전반적으로, 이 연구는 분류기 성능을 향상시키고 신경영상 기반 분류 작업에서 특징의 중요성을 이해하는 데 있어 최적화 기법 선택, 모델 아키텍처, EEG 주파수 대역 분석의 중요성을 강조합니다.

## 📝 요약

이 연구는 EEG 주파수 대역에서 다양한 최적화 기법을 사용하여 분류기 성능을 조사하고, 좌우 뇌반구에 대한 효율적인 클래스 예측을 평가합니다. 딥 밀집 네트워크, 얕은 3층 네트워크, CNN의 세 가지 신경망 구조를 TensorFlow와 PyTorch로 구현하여 비교했습니다. 결과적으로 Adagrad와 RMSprop 최적화 기법이 주파수 대역 전반에서 일관된 성능을 보였으며, Adadelta는 모델 간 평가에서 강력한 성능을 나타냈습니다. Adagrad는 베타 대역에서, RMSprop은 감마 대역에서 우수한 성능을 발휘했습니다. CNN은 EEG 데이터의 공간적 특징을 잘 포착하여 두 번째로 높은 정확도를 보였고, 깊은 밀집 네트워크는 복잡한 패턴 학습에서 경쟁력을 보였습니다. SHAP 플롯을 통해 EEG 주파수 대역이 모델 정확도에 미치는 기여도를 분석했습니다. 이 연구는 최적화 기법 선택, 모델 구조, EEG 주파수 대역 분석의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. Adagrad와 RMSprop 최적화 알고리즘은 다양한 EEG 주파수 대역에서 일관된 성능을 보이며, 특히 Adagrad는 베타 대역에서, RMSprop은 감마 대역에서 우수한 성능을 발휘합니다.

- 2. CNN 모델은 EEG 데이터의 공간적 특징을 포착하는 데 뛰어나며, 두 번째로 높은 정확도를 기록했습니다.

- 3. 깊은 밀집 네트워크는 복잡한 패턴 학습에서 경쟁력 있는 성능을 보였으며, 얕은 3층 네트워크는 정확도는 다소 낮지만 계산 효율성을 제공합니다.

- 4. SHAP 플롯을 통해 EEG 주파수 대역이 모델 정확도에 미치는 미세한 기여도를 파악하여 효율적인 클래스 예측을 식별했습니다.

- 5. 연구는 최적화 알고리즘 선택, 모델 아키텍처, EEG 주파수 대역 분석이 신경영상 기반 분류 작업의 분류기 성능 향상과 특징 중요성 이해에 중요함을 강조합니다.

---

*Generated on 2025-09-20 07:48:59*