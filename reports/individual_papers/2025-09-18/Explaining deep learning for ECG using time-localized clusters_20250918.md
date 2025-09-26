---
keywords:
  - Convolutional Neural Networks
  - Deep Learning
  - ECG Analysis
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:29:17.955299",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convolutional Neural Networks",
    "Deep Learning",
    "ECG Analysis"
  ],
  "rejected_keywords": [
    "Uncertainty Quantification"
  ],
  "similarity_scores": {
    "Convolutional Neural Networks": 0.88,
    "Deep Learning": 0.85,
    "ECG Analysis": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Explaining deep learning for ECG using time-localized clusters

**Korean Title:** ECG에 대한 심층 학습을 시간-국소화된 클러스터를 사용하여 설명하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep learning]]
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|Convolutional neural networks]]
**⚡ Unique Technical**: [[keywords/ECG Analysis|ECG analysis]]

## 🔗 유사한 논문
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (82.4% similar)
- [[Multimodal signal fusion for stress detection using deep neural networks_ a novel approach for converting 1D signals to unified 2D images_20250918|Multimodal signal fusion for stress detection using deep neural networks a novel approach for converting 1D signals to unified 2D images]] (80.4% similar)
- [[Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis_20250919|Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis]] (80.2% similar)
- [[UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (80.0% similar)
- [[Towards Trustworthy Vital Sign Forecasting_ Leveraging Uncertainty for Prediction Intervals_20250918|Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (79.8% similar)

## 📋 저자 정보

**Authors:** Ahcène Boubekki, Konstantinos Patlatzoglou, Joseph Barker, Fu Siong Ng, Antônio H. Ribeiro

## 📄 Abstract (원문)

Deep learning has significantly advanced electrocardiogram (ECG) analysis,
enabling automatic annotation, disease screening, and prognosis beyond
traditional clinical capabilities. However, understanding these models remains
a challenge, limiting interpretation and gaining knowledge from these
developments. In this work, we propose a novel interpretability method for
convolutional neural networks applied to ECG analysis. Our approach extracts
time-localized clusters from the model's internal representations, segmenting
the ECG according to the learned characteristics while quantifying the
uncertainty of these representations. This allows us to visualize how different
waveform regions contribute to the model's predictions and assess the certainty
of its decisions. By providing a structured and interpretable view of deep
learning models for ECG, our method enhances trust in AI-driven diagnostics and
facilitates the discovery of clinically relevant electrophysiological patterns.

## 🔍 Abstract (한글 번역)

딥러닝은 심전도(ECG) 분석을 크게 발전시켜 자동 주석, 질병 선별 및 예후를 전통적인 임상 능력을 넘어 가능하게 했습니다. 그러나 이러한 모델을 이해하는 것은 여전히 도전 과제로 남아 있으며, 이러한 발전으로부터 해석과 지식을 얻는 데 한계가 있습니다. 본 연구에서는 ECG 분석에 적용된 합성곱 신경망에 대한 새로운 해석 가능성 방법을 제안합니다. 우리의 접근 방식은 모델의 내부 표현에서 시간에 국한된 클러스터를 추출하여 학습된 특성에 따라 ECG를 분할하고 이러한 표현의 불확실성을 정량화합니다. 이를 통해 서로 다른 파형 영역이 모델의 예측에 어떻게 기여하는지 시각화하고, 그 결정의 확실성을 평가할 수 있습니다. ECG에 대한 딥러닝 모델의 구조적이고 해석 가능한 관점을 제공함으로써, 우리의 방법은 AI 기반 진단에 대한 신뢰를 향상시키고 임상적으로 관련 있는 전기생리학적 패턴의 발견을 촉진합니다.

## 📝 요약

이 연구는 심전도(ECG) 분석에 적용된 심층 학습 모델의 해석 가능성을 높이는 새로운 방법을 제안합니다. 제안된 방법은 모델의 내부 표현에서 시간에 국한된 클러스터를 추출하여 ECG를 학습된 특성에 따라 세분화하고, 이러한 표현의 불확실성을 정량화합니다. 이를 통해 모델의 예측에 기여하는 다양한 파형 영역을 시각화하고, 결정의 확실성을 평가할 수 있습니다. 이 방법은 AI 기반 진단에 대한 신뢰를 높이고, 임상적으로 중요한 전기생리학적 패턴의 발견을 촉진합니다.

## 🎯 주요 포인트

- 1. 심전도(ECG) 분석에서 딥러닝의 해석 가능성을 높이기 위한 새로운 방법을 제안합니다.

- 2. 제안된 방법은 모델의 내부 표현에서 시간에 국한된 클러스터를 추출하여 ECG를 학습된 특성에 따라 세분화합니다.

- 3. 이 방법은 모델의 예측에 기여하는 다양한 파형 영역을 시각화하고 결정의 확실성을 평가할 수 있게 합니다.

- 4. 딥러닝 모델의 구조적이고 해석 가능한 시각을 제공하여 AI 기반 진단에 대한 신뢰성을 높입니다.

- 5. 임상적으로 관련 있는 전기생리학적 패턴의 발견을 촉진합니다.

---

*Generated on 2025-09-20 00:51:29*