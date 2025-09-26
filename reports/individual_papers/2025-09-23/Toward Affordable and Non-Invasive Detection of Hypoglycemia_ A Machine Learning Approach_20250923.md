---
keywords:
  - Machine Learning
  - Galvanic Skin Response
  - Wearables
  - Hypoglycemia Detection
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17842
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:26:31.560706",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Galvanic Skin Response",
    "Wearables",
    "Hypoglycemia Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Galvanic Skin Response": 0.8,
    "Wearables": 0.77,
    "Hypoglycemia Detection": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Machine Learning is a central technique used in the study, connecting it to a wide range of technical literature.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Galvanic Skin Response",
        "canonical": "Galvanic Skin Response",
        "aliases": [
          "GSR"
        ],
        "category": "unique_technical",
        "rationale": "Galvanic Skin Response is a unique biosignal used for non-invasive monitoring, making it a specific technical focus of the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Wearables",
        "canonical": "Wearables",
        "aliases": [
          "Wearable Devices"
        ],
        "category": "specific_connectable",
        "rationale": "Wearables are crucial for implementing the proposed non-invasive monitoring method, linking to broader discussions on health technology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hypoglycemia Detection",
        "canonical": "Hypoglycemia Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The focus on hypoglycemia detection is a unique contribution of the paper, relevant for specialized medical and technical research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Continuous Glucose Monitors",
      "OhioT1DM"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Galvanic Skin Response",
      "resolved_canonical": "Galvanic Skin Response",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Wearables",
      "resolved_canonical": "Wearables",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hypoglycemia Detection",
      "resolved_canonical": "Hypoglycemia Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Toward Affordable and Non-Invasive Detection of Hypoglycemia: A Machine Learning Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17842.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17842](https://arxiv.org/abs/2509.17842)

## 🔗 유사한 논문
- [[2025-09-23/Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach_20250923|Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach]] (81.6% similar)
- [[2025-09-19/Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes_20250919|Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes]] (80.8% similar)
- [[2025-09-23/Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability_20250923|Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability]] (80.3% similar)
- [[2025-09-23/FairTune_ A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG_20250923|FairTune: A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG]] (80.2% similar)
- [[2025-09-18/HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C: Efficient Medical Data Classification for Embedded Devices]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Wearables|Wearables]]
**⚡ Unique Technical**: [[keywords/Galvanic Skin Response|Galvanic Skin Response]], [[keywords/Hypoglycemia Detection|Hypoglycemia Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17842v1 Announce Type: cross 
Abstract: Diabetes mellitus is a growing global health issue, with Type 1 Diabetes (T1D) requiring constant monitoring to avoid hypoglycemia. Although Continuous Glucose Monitors (CGMs) are effective, their cost and invasiveness limit access, particularly in low-resource settings. This paper proposes a non-invasive method to classify glycemic states using Galvanic Skin Response (GSR), a biosignal commonly captured by wearable sensors. We use the merged OhioT1DM 2018 and 2020 datasets to build a machine learning pipeline that detects hypoglycemia (glucose < 70 mg/dl) and normoglycemia (glucose > 70 mg/dl) with GSR alone. Seven models are trained and evaluated: Random Forest, XGBoost, MLP, CNN, LSTM, Logistic Regression, and K-Nearest Neighbors. Validation sets and 95% confidence intervals are reported to increase reliability and assess robustness. Results show that the LSTM model achieves a perfect hypoglycemia recall (1.00) with an F1-score confidence interval of [0.611-0.745], while XGBoost offers strong performance with a recall of 0.54 even under class imbalance. This approach highlights the potential for affordable, wearable-compatible glucose monitoring tools suitable for settings with limited CGM availability using GSR data.
  Index Terms: Hypoglycemia Detection, Galvanic Skin Response, Non Invasive Monitoring, Wearables, Machine Learning, Confidence Intervals.

## 📝 요약

이 논문은 비침습적으로 혈당 상태를 분류하기 위해 갈바닉 피부 반응(GSR)을 사용하는 방법을 제안합니다. 이는 주로 착용 가능한 센서로 포착되는 생체 신호입니다. OhioT1DM 2018 및 2020 데이터셋을 활용하여 저혈당(혈당 < 70 mg/dl)과 정상혈당(혈당 > 70 mg/dl)을 GSR만으로 감지하는 기계 학습 파이프라인을 구축했습니다. 랜덤 포레스트, XGBoost, MLP, CNN, LSTM, 로지스틱 회귀, K-최근접 이웃 등 7개의 모델을 훈련 및 평가했습니다. LSTM 모델은 저혈당 재현율 1.00을 달성했으며, XGBoost는 클래스 불균형 상황에서도 0.54의 재현율을 보였습니다. 이 접근법은 GSR 데이터를 사용하여 저비용의 착용 가능한 혈당 모니터링 도구의 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 제안된 방법은 Galvanic Skin Response(GSR)를 사용하여 비침습적으로 혈당 상태를 분류하는 것이다.
- 2. OhioT1DM 2018 및 2020 데이터셋을 활용하여 저혈당과 정상혈당을 GSR만으로 감지하는 머신러닝 파이프라인을 구축하였다.
- 3. LSTM 모델은 저혈당 감지에서 완벽한 재현율(1.00)을 달성하였으며, F1-스코어의 신뢰 구간은 [0.611-0.745]이다.
- 4. XGBoost 모델은 클래스 불균형 상황에서도 0.54의 재현율을 보여 강력한 성능을 발휘하였다.
- 5. 이 접근법은 GSR 데이터를 사용하여 저비용의 착용 가능한 혈당 모니터링 도구의 가능성을 제시한다.


---

*Generated on 2025-09-24 02:26:31*