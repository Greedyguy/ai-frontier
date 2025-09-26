---
keywords:
  - Machine Learning
  - XGBoost
  - SHAP
  - MIMIC-IV
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17674
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:25:40.249276",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "XGBoost",
    "SHAP",
    "MIMIC-IV"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.78,
    "XGBoost": 0.81,
    "SHAP": 0.8,
    "MIMIC-IV": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Interpretable Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "Explainable AI",
          "Transparent AI"
        ],
        "category": "broad_technical",
        "rationale": "Links to broader discussions on machine learning methodologies and their interpretability.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Extreme Gradient Boosting",
        "canonical": "XGBoost",
        "aliases": [
          "Extreme Gradient Boosting",
          "eXtreme Gradient Boosting"
        ],
        "category": "specific_connectable",
        "rationale": "XGBoost is a popular machine learning algorithm, facilitating connections with other works using similar methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Shapley Additive Explanations",
        "canonical": "SHAP",
        "aliases": [
          "Shapley Values",
          "SHAP"
        ],
        "category": "specific_connectable",
        "rationale": "SHAP is a key method for interpreting machine learning models, relevant for linking to interpretability studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "MIMIC-IV database",
        "canonical": "MIMIC-IV",
        "aliases": [
          "MIMIC-IV dataset",
          "Medical Information Mart for Intensive Care IV"
        ],
        "category": "unique_technical",
        "rationale": "MIMIC-IV is a specific dataset, crucial for linking studies utilizing the same data source.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "recursive feature elimination",
      "bootstrapped 95% confidence intervals"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Interpretable Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Extreme Gradient Boosting",
      "resolved_canonical": "XGBoost",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Shapley Additive Explanations",
      "resolved_canonical": "SHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "MIMIC-IV database",
      "resolved_canonical": "MIMIC-IV",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Predicting Chest Radiograph Findings from Electrocardiograms Using Interpretable Machine Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17674.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17674](https://arxiv.org/abs/2509.17674)

## 🔗 유사한 논문
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.3% similar)
- [[2025-09-23/Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability_20250923|Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability]] (82.0% similar)
- [[2025-09-18/Explainable AI for Infection Prevention and Control_ Modeling CPE Acquisition and Patient Outcomes in an Irish Hospital with Transformers_20250918|Explainable AI for Infection Prevention and Control: Modeling CPE Acquisition and Patient Outcomes in an Irish Hospital with Transformers]] (81.7% similar)
- [[2025-09-23/Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach_20250923|Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach]] (80.7% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/XGBoost|XGBoost]], [[keywords/SHAP|SHAP]]
**⚡ Unique Technical**: [[keywords/MIMIC-IV|MIMIC-IV]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17674v1 Announce Type: cross 
Abstract: Purpose: Chest X-rays are essential for diagnosing pulmonary conditions, but limited access in resource-constrained settings can delay timely diagnosis. Electrocardiograms (ECGs), in contrast, are widely available, non-invasive, and often acquired earlier in clinical workflows. This study aims to assess whether ECG features and patient demographics can predict chest radiograph findings using an interpretable machine learning approach.
  Methods: Using the MIMIC-IV database, Extreme Gradient Boosting (XGBoost) classifiers were trained to predict diverse chest radiograph findings from ECG-derived features and demographic variables. Recursive feature elimination was performed independently for each target to identify the most predictive features. Model performance was evaluated using the area under the receiver operating characteristic curve (AUROC) with bootstrapped 95% confidence intervals. Shapley Additive Explanations (SHAP) were applied to interpret feature contributions.
  Results: Models successfully predicted multiple chest radiograph findings with varying accuracy. Feature selection tailored predictors to each target, and including demographic variables consistently improved performance. SHAP analysis revealed clinically meaningful contributions from ECG features to radiographic predictions.
  Conclusion: ECG-derived features combined with patient demographics can serve as a proxy for certain chest radiograph findings, enabling early triage or pre-screening in settings where radiographic imaging is limited. Interpretable machine learning demonstrates potential to support radiology workflows and improve patient care.

## 📝 요약

이 연구는 ECG(심전도) 특징과 환자 인구통계학적 정보를 통해 흉부 X-ray 소견을 예측할 수 있는지 평가합니다. MIMIC-IV 데이터베이스를 활용하여 XGBoost 분류기를 훈련시켰으며, 각 목표에 대해 재귀적 특징 제거를 통해 가장 예측력이 높은 특징을 식별했습니다. 모델 성능은 AUROC로 평가되었고, SHAP 분석을 통해 특징 기여도를 해석했습니다. 연구 결과, ECG 특징과 인구통계학적 정보가 결합되어 다양한 흉부 X-ray 소견을 성공적으로 예측할 수 있었으며, 이는 자원이 제한된 환경에서 조기 선별에 유용할 수 있음을 시사합니다. 이 연구는 해석 가능한 머신러닝이 방사선학적 워크플로를 지원하고 환자 치료를 개선할 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. ECG와 환자 인구통계학적 정보로 흉부 X-ray 소견을 예측할 수 있는 가능성을 평가했습니다.
- 2. MIMIC-IV 데이터베이스를 활용하여 XGBoost 분류기를 사용해 다양한 흉부 X-ray 소견을 예측하는 모델을 개발했습니다.
- 3. SHAP 분석을 통해 ECG 특징이 방사선 소견 예측에 임상적으로 의미 있는 기여를 한다는 것을 확인했습니다.
- 4. 인구통계학적 변수를 포함하면 모델의 성능이 일관되게 향상되었습니다.
- 5. 해석 가능한 머신러닝은 방사선학 워크플로를 지원하고 환자 치료를 개선할 잠재력을 가지고 있습니다.


---

*Generated on 2025-09-24 02:25:40*