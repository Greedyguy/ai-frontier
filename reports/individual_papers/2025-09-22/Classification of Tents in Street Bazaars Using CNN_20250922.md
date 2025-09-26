---
keywords:
  - Neural Network
  - EfficientNet
  - Transfer Learning
  - Street Bazaars
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2506.17946
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:36:44.352118",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "EfficientNet",
    "Transfer Learning",
    "Street Bazaars"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "EfficientNet": 0.79,
    "Transfer Learning": 0.82,
    "Street Bazaars": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "CNN"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are fundamental to the classification task discussed in the paper, linking to broader machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "EfficientNetB0",
        "canonical": "EfficientNet",
        "aliases": [
          "EfficientNet B0"
        ],
        "category": "unique_technical",
        "rationale": "EfficientNetB0 is a specific model variant that highlights the use of transfer learning in the study, connecting to advancements in model architecture.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Transfer Learning",
        "canonical": "Transfer Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Transfer Learning is a key technique used to improve classification accuracy, relevant to many machine learning applications.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Street Bazaars",
        "canonical": "Street Bazaars",
        "aliases": [
          "Market Bazaars"
        ],
        "category": "unique_technical",
        "rationale": "Street Bazaars are the unique context of the study, providing a specific application domain for the classification task.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "accuracy",
      "precision",
      "recall",
      "F1 score",
      "mean average precision"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convolutional Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "EfficientNetB0",
      "resolved_canonical": "EfficientNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Transfer Learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Street Bazaars",
      "resolved_canonical": "Street Bazaars",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Classification of Tents in Street Bazaars Using CNN

**Korean Title:** 거리 시장에서의 텐트 분류를 위한 CNN 사용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.17946.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2506.17946](https://arxiv.org/abs/2506.17946)

## 🔗 유사한 논문
- [[2025-09-22/Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles_20250922|Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles]] (79.4% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (78.4% similar)
- [[2025-09-22/TSCAN_ Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis_20250922|TSCAN: Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis]] (77.9% similar)
- [[2025-09-22/Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings_20250922|Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings]] (77.4% similar)
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (77.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Transfer Learning|Transfer Learning]]
**⚡ Unique Technical**: [[keywords/EfficientNet|EfficientNet]], [[keywords/Street Bazaars|Street Bazaars]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.17946v2 Announce Type: replace 
Abstract: This research paper proposes an improved deep learning model for classifying tents in street bazaars, comparing a custom Convolutional Neural Network (CNN) with EfficientNetB0. This is a critical task for market organization with a tent classification, but manual methods in the past have been inefficient. Street bazaars represent a vital economic hub in many regions, yet their unstructured nature poses significant challenges for the automated classification of market infrastructure, such as tents. In Kyrgyzstan, more than a quarter of the country's GDP is derived from bazaars. While CNNs have been widely applied to object recognition, their application to bazaar-specific tasks remains underexplored. Here, we build upon our original approach by training on an extended set of 126 original photographs that were augmented to generate additional images. This dataset is publicly available for download on Kaggle. A variety of performance metrics, such as accuracy, precision, recall, F1 score, and mean average precision (mAP), were used to assess the models comparatively, providing a more extensive analysis of classification performance.
  The results show that the CNN custom model achieved 92.8% accuracy, and EfficientNetB0 showed 98.4% accuracy results, confirming the effectiveness of transfer learning in the bazaar image classification. Also, when analyzing the confusion matrix, the analysis reveals the weaknesses and strengths of each model. These findings suggest that using a pre-trained model such as EfficientNetB0 significantly improves classification accuracy and generalization.

## 🔍 Abstract (한글 번역)

arXiv:2506.17946v2 발표 유형: 교체  
초록: 이 연구 논문은 거리 시장에서 텐트를 분류하기 위한 개선된 딥러닝 모델을 제안하며, 맞춤형 합성곱 신경망(CNN)과 EfficientNetB0을 비교합니다. 텐트 분류는 시장 조직에 있어 중요한 작업이지만, 과거의 수작업 방법은 비효율적이었습니다. 거리 시장은 많은 지역에서 중요한 경제 허브를 나타내지만, 그 비구조적인 특성은 텐트와 같은 시장 인프라의 자동 분류에 상당한 도전을 제기합니다. 키르기스스탄에서는 국가 GDP의 4분의 1 이상이 시장에서 파생됩니다. CNN은 객체 인식에 널리 적용되었지만, 시장 특유의 작업에 대한 적용은 아직 충분히 탐구되지 않았습니다. 여기서 우리는 126개의 원본 사진을 확장하여 추가 이미지를 생성한 데이터셋을 학습함으로써 원래 접근 방식을 기반으로 구축합니다. 이 데이터셋은 Kaggle에서 공개적으로 다운로드할 수 있습니다. 정확도, 정밀도, 재현율, F1 점수, 평균 평균 정밀도(mAP)와 같은 다양한 성능 지표를 사용하여 모델을 비교 평가하며, 분류 성능에 대한 보다 광범위한 분석을 제공합니다.  
결과는 CNN 맞춤형 모델이 92.8%의 정확도를 달성했으며, EfficientNetB0은 98.4%의 정확도를 보여주어 시장 이미지 분류에서 전이 학습의 효과를 확인했습니다. 또한, 혼동 행렬을 분석할 때 각 모델의 약점과 강점을 드러냅니다. 이러한 결과는 EfficientNetB0와 같은 사전 학습된 모델을 사용하는 것이 분류 정확도와 일반화를 크게 향상시킨다는 것을 시사합니다.

## 📝 요약

이 연구 논문은 거리 시장에서 텐트를 분류하기 위한 개선된 딥러닝 모델을 제안합니다. 커스텀 CNN과 EfficientNetB0을 비교하여, 시장 조직에 중요한 텐트 분류 작업에서 효율성을 높이고자 했습니다. 키르기스스탄의 경우, 시장이 GDP의 상당 부분을 차지하고 있어 자동화된 분류의 필요성이 큽니다. 연구에서는 126장의 원본 사진을 증강하여 데이터셋을 확장하였고, 이 데이터셋은 Kaggle에서 공개되었습니다. 성능 평가는 정확도, 정밀도, 재현율, F1 점수, 평균 정밀도(mAP) 등을 통해 이루어졌습니다. 결과적으로, 커스텀 CNN은 92.8%의 정확도를, EfficientNetB0은 98.4%의 정확도를 기록하여 전이 학습의 효과를 입증했습니다. 혼동 행렬 분석을 통해 각 모델의 강점과 약점도 파악할 수 있었습니다. EfficientNetB0와 같은 사전 학습된 모델을 사용하면 분류 정확도와 일반화가 크게 향상됨을 시사합니다.

## 🎯 주요 포인트

- 1. 이 연구는 거리 시장의 텐트 분류를 위한 개선된 딥러닝 모델을 제안하며, 커스텀 CNN과 EfficientNetB0를 비교합니다.
- 2. 키르기스스탄에서 시장은 GDP의 25% 이상을 차지하는 중요한 경제 허브로, 텐트와 같은 시장 인프라의 자동 분류가 도전 과제로 남아 있습니다.
- 3. 연구에서는 126장의 원본 사진을 증강하여 생성한 추가 이미지로 학습을 진행하였으며, 이 데이터셋은 Kaggle에서 공개적으로 다운로드 가능합니다.
- 4. 커스텀 CNN 모델은 92.8%의 정확도를, EfficientNetB0는 98.4%의 정확도를 보여주며, 전이 학습의 효과성을 확인했습니다.
- 5. 혼동 행렬 분석을 통해 각 모델의 강점과 약점을 파악할 수 있었으며, EfficientNetB0와 같은 사전 학습된 모델 사용이 분류 정확도와 일반화에 크게 기여함을 시사합니다.


---

*Generated on 2025-09-23 12:36:44*