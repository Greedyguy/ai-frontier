---
keywords:
  - Boosting Algorithms
  - SHAP Method
  - Optuna
  - Breast Cancer Prediction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2403.09548
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:05:52.959778",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Boosting Algorithms",
    "SHAP Method",
    "Optuna",
    "Breast Cancer Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Boosting Algorithms": 0.85,
    "SHAP Method": 0.8,
    "Optuna": 0.79,
    "Breast Cancer Prediction": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gradient Boosting Algorithms",
        "canonical": "Boosting Algorithms",
        "aliases": [
          "Gradient Boosting",
          "Boosting Methods"
        ],
        "category": "broad_technical",
        "rationale": "Boosting algorithms are a fundamental machine learning technique, crucial for understanding the study's methodology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "SHAP",
        "canonical": "SHAP Method",
        "aliases": [
          "SHapley Additive exPlanations"
        ],
        "category": "specific_connectable",
        "rationale": "SHAP is a specific technique for model interpretability, linking to broader discussions on explainable AI.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optuna",
        "canonical": "Optuna",
        "aliases": [
          "Hyperparameter Optimization Library"
        ],
        "category": "unique_technical",
        "rationale": "Optuna is a unique tool for hyperparameter optimization, enhancing model performance.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Breast Cancer Prediction",
        "canonical": "Breast Cancer Prediction",
        "aliases": [
          "Breast Cancer Detection",
          "Breast Cancer Diagnosis"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the study, linking to medical applications of machine learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.85,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "cancer",
      "detection",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gradient Boosting Algorithms",
      "resolved_canonical": "Boosting Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SHAP",
      "resolved_canonical": "SHAP Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optuna",
      "resolved_canonical": "Optuna",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Breast Cancer Prediction",
      "resolved_canonical": "Breast Cancer Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.85,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2403.09548.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2403.09548](https://arxiv.org/abs/2403.09548)

## 🔗 유사한 논문
- [[2025-09-22/From Data to Diagnosis_ A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction_20250922|From Data to Diagnosis: A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction]] (82.1% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (81.9% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX: Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (81.8% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.2% similar)
- [[2025-09-19/Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models_20250919|Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Boosting Algorithms|Boosting Algorithms]]
**🔗 Specific Connectable**: [[keywords/SHAP Method|SHAP Method]], [[keywords/Breast Cancer Prediction|Breast Cancer Prediction]]
**⚡ Unique Technical**: [[keywords/Optuna|Optuna]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2403.09548v3 Announce Type: cross 
Abstract: Cancer is one of the diseases that kill the most women in the world, with breast cancer being responsible for the highest number of cancer cases and consequently deaths. However, it can be prevented by early detection and, consequently, early treatment. Any development for detection or perdition this kind of cancer is important for a better healthy life. Many studies focus on a model with high accuracy in cancer prediction, but sometimes accuracy alone may not always be a reliable metric. This study implies an investigative approach to studying the performance of different machine learning algorithms based on boosting to predict breast cancer focusing on the recall metric. Boosting machine learning algorithms has been proven to be an effective tool for detecting medical diseases. The dataset of the University of California, Irvine (UCI) repository has been utilized to train and test the model classifier that contains their attributes. The main objective of this study is to use state-of-the-art boosting algorithms such as AdaBoost, XGBoost, CatBoost and LightGBM to predict and diagnose breast cancer and to find the most effective metric regarding recall, ROC-AUC, and confusion matrix. Furthermore, our study is the first to use these four boosting algorithms with Optuna, a library for hyperparameter optimization, and the SHAP method to improve the interpretability of our model, which can be used as a support to identify and predict breast cancer. We were able to improve AUC or recall for all the models and reduce the False Negative for AdaBoost and LigthGBM the final AUC were more than 99.41\% for all models.

## 📝 요약

이 연구는 유방암 예측을 위해 다양한 부스팅 기계 학습 알고리즘의 성능을 조사합니다. 주요 목표는 AdaBoost, XGBoost, CatBoost, LightGBM 등의 최신 부스팅 알고리즘을 활용하여 유방암을 진단하고, 재현율, ROC-AUC, 혼동 행렬을 기반으로 가장 효과적인 지표를 찾는 것입니다. UCI 데이터셋을 사용하여 모델을 학습 및 테스트하였으며, Optuna와 SHAP 방법을 통해 모델의 해석 가능성을 높였습니다. 모든 모델에서 AUC와 재현율을 개선하였고, 특히 AdaBoost와 LightGBM에서 거짓 음성을 줄여 최종 AUC가 99.41% 이상을 기록했습니다.

## 🎯 주요 포인트

- 1. 유방암은 조기 발견과 조기 치료를 통해 예방할 수 있으며, 이를 위한 예측 모델 개발이 중요합니다.
- 2. 본 연구는 부스팅 기법을 활용한 머신러닝 알고리즘을 통해 유방암 예측에서 재현율(recall) 지표에 중점을 두고 성능을 조사합니다.
- 3. AdaBoost, XGBoost, CatBoost, LightGBM과 같은 최신 부스팅 알고리즘을 사용하여 유방암을 예측하고 진단하며, 재현율, ROC-AUC, 혼동 행렬 등의 효과적인 지표를 찾는 것이 주요 목표입니다.
- 4. Optuna와 SHAP 방법을 활용하여 하이퍼파라미터 최적화 및 모델 해석 가능성을 개선하였으며, 모든 모델에서 AUC 또는 재현율을 향상시키고 AdaBoost와 LightGBM의 경우 False Negative를 줄였습니다.
- 5. 최종적으로 모든 모델에서 AUC가 99.41% 이상으로 개선되었습니다.


---

*Generated on 2025-09-23 23:05:52*