<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:10:59.409077",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Transfer Learning",
    "Histopathological Image Analysis",
    "Cancer Diagnostics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.82,
    "Transfer Learning": 0.78,
    "Histopathological Image Analysis": 0.7,
    "Cancer Diagnostics": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Vision Transformers are a significant evolution in the Transformer architecture applied to image processing, linking well with existing Transformer research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transfer Learning",
        "canonical": "Transfer Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Transfer Learning is crucial for adapting pre-trained models to new tasks, enhancing connectivity with other machine learning studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Histopathological Image Datasets",
        "canonical": "Histopathological Image Analysis",
        "aliases": [
          "Histopathology Images"
        ],
        "category": "unique_technical",
        "rationale": "This specific application of image analysis in cancer diagnostics is novel and highly specific, providing unique insights into medical imaging.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Oncological Diagnostics",
        "canonical": "Cancer Diagnostics",
        "aliases": [
          "Cancer Detection"
        ],
        "category": "unique_technical",
        "rationale": "Focusing on cancer diagnostics offers a specialized link to medical applications of machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "preprocessing pipeline",
      "model performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transfer Learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Histopathological Image Datasets",
      "resolved_canonical": "Histopathological Image Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Oncological Diagnostics",
      "resolved_canonical": "Cancer Diagnostics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Efficient Breast and Ovarian Cancer Classification via ViT-Based Preprocessing and Transfer Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18553.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18553](https://arxiv.org/abs/2509.18553)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (84.3% similar)
- [[2025-09-23/Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification_20250923|Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification]] (84.3% similar)
- [[2025-09-23/Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification_20250923|Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification]] (84.0% similar)
- [[2025-09-23/Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability_20250923|Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability]] (83.8% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Transfer Learning|Transfer Learning]]
**⚡ Unique Technical**: [[keywords/Histopathological Image Analysis|Histopathological Image Analysis]], [[keywords/Cancer Diagnostics|Cancer Diagnostics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18553v1 Announce Type: cross 
Abstract: Cancer is one of the leading health challenges for women, specifically breast and ovarian cancer. Early detection can help improve the survival rate through timely intervention and treatment. Traditional methods of detecting cancer involve manually examining mammograms, CT scans, ultrasounds, and other imaging types. However, this makes the process labor-intensive and requires the expertise of trained pathologists. Hence, making it both time-consuming and resource-intensive. In this paper, we introduce a novel vision transformer (ViT)-based method for detecting and classifying breast and ovarian cancer. We use a pre-trained ViT-Base-Patch16-224 model, which is fine-tuned for both binary and multi-class classification tasks using publicly available histopathological image datasets. Further, we use a preprocessing pipeline that converts raw histophological images into standardized PyTorch tensors, which are compatible with the ViT architecture and also help improve the model performance. We evaluated the performance of our model on two benchmark datasets: the BreakHis dataset for binary classification and the UBC-OCEAN dataset for five-class classification without any data augmentation. Our model surpasses existing CNN, ViT, and topological data analysis-based approaches in binary classification. For multi-class classification, it is evaluated against recent topological methods and demonstrates superior performance. Our study highlights the effectiveness of Vision Transformer-based transfer learning combined with efficient preprocessing in oncological diagnostics.

## 📝 요약

이 논문은 유방암과 난소암의 조기 발견을 위한 새로운 비전 트랜스포머(ViT) 기반 방법을 제안합니다. 기존의 암 진단 방법은 수작업과 전문가의 경험이 필요하여 시간과 자원이 많이 소모됩니다. 본 연구에서는 사전 학습된 ViT-Base-Patch16-224 모델을 사용하여 이진 및 다중 클래스 분류 작업에 맞게 미세 조정하였으며, 공개된 병리학적 이미지 데이터셋을 활용했습니다. 또한, 원시 이미지를 ViT 아키텍처와 호환되는 표준 PyTorch 텐서로 변환하는 전처리 파이프라인을 도입하여 모델 성능을 향상시켰습니다. BreakHis와 UBC-OCEAN 데이터셋을 사용한 성능 평가 결과, 이진 분류에서는 기존의 CNN, ViT, 위상 데이터 분석 기반 접근법을 능가했으며, 다중 클래스 분류에서도 최신 위상 방법보다 우수한 성능을 보였습니다. 본 연구는 비전 트랜스포머 기반 전이 학습과 효율적인 전처리가 암 진단에서 효과적임을 강조합니다.

## 🎯 주요 포인트

- 1. 본 논문은 유방암 및 난소암 진단을 위한 새로운 비전 트랜스포머(ViT) 기반 방법을 제안합니다.
- 2. 사전 훈련된 ViT-Base-Patch16-224 모델을 사용하여 이진 및 다중 클래스 분류 작업을 수행합니다.
- 3. 원시 병리 이미지를 표준화된 PyTorch 텐서로 변환하는 전처리 파이프라인을 통해 모델 성능을 향상시킵니다.
- 4. 제안된 모델은 BreakHis 및 UBC-OCEAN 데이터셋에서 기존 CNN, ViT, 위상 데이터 분석 기반 접근법을 능가하는 성능을 보였습니다.
- 5. 비전 트랜스포머 기반 전이 학습과 효율적인 전처리의 결합이 암 진단에서 효과적임을 강조합니다.


---

*Generated on 2025-09-24 15:10:59*