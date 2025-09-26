---
keywords:
  - Long Short-Term Memory Networks
  - Electricity Demand Forecasting
  - Exogenous Variables in Forecasting
  - Model Interpretability
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19374
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:51:50.058663",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Long Short-Term Memory Networks",
    "Electricity Demand Forecasting",
    "Exogenous Variables in Forecasting",
    "Model Interpretability"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Long Short-Term Memory Networks": 0.85,
    "Electricity Demand Forecasting": 0.78,
    "Exogenous Variables in Forecasting": 0.77,
    "Model Interpretability": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LSTM networks",
        "canonical": "Long Short-Term Memory Networks",
        "aliases": [
          "LSTM",
          "LSTM Network"
        ],
        "category": "broad_technical",
        "rationale": "LSTM networks are a fundamental deep learning architecture relevant for time series forecasting, linking to broader neural network discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "electricity demand forecasting",
        "canonical": "Electricity Demand Forecasting",
        "aliases": [
          "power demand prediction",
          "energy demand forecasting"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that connects to energy management and optimization strategies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "exogenous variables",
        "canonical": "Exogenous Variables in Forecasting",
        "aliases": [
          "external factors",
          "external variables"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding the role of exogenous variables is crucial for improving model accuracy and can link to broader forecasting methodologies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "interpretability study",
        "canonical": "Model Interpretability",
        "aliases": [
          "interpretability analysis",
          "explainability study"
        ],
        "category": "specific_connectable",
        "rationale": "Model interpretability is essential for understanding model decisions, linking to discussions on transparency in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.68,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "deep learning model",
      "predictive precision",
      "operational relevance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LSTM networks",
      "resolved_canonical": "Long Short-Term Memory Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "electricity demand forecasting",
      "resolved_canonical": "Electricity Demand Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "exogenous variables",
      "resolved_canonical": "Exogenous Variables in Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "interpretability study",
      "resolved_canonical": "Model Interpretability",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.68,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Short-Term Regional Electricity Demand Forecasting in Argentina Using LSTM Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19374.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19374](https://arxiv.org/abs/2509.19374)

## 🔗 유사한 논문
- [[2025-09-23/A Hybrid PCA-PR-Seq2Seq-Adam-LSTM Framework for Time-Series Power Outage Prediction_20250923|A Hybrid PCA-PR-Seq2Seq-Adam-LSTM Framework for Time-Series Power Outage Prediction]] (83.5% similar)
- [[2025-09-23/Machine Learning for Campus Energy Resilience_ Clustering and Time-Series Forecasting in Intelligent Load Shedding_20250923|Machine Learning for Campus Energy Resilience: Clustering and Time-Series Forecasting in Intelligent Load Shedding]] (82.9% similar)
- [[2025-09-23/Time Series Forecasting Using a Hybrid Deep Learning Method_ A Bi-LSTM Embedding Denoising Auto Encoder Transformer_20250923|Time Series Forecasting Using a Hybrid Deep Learning Method: A Bi-LSTM Embedding Denoising Auto Encoder Transformer]] (81.4% similar)
- [[2025-09-25/STL-FFT-STFT-TCN-LSTM_ An Effective Wave Height High Accuracy Prediction Model Fusing Time-Frequency Domain Features_20250925|STL-FFT-STFT-TCN-LSTM: An Effective Wave Height High Accuracy Prediction Model Fusing Time-Frequency Domain Features]] (81.0% similar)
- [[2025-09-23/Ultra-short-term solar power forecasting by deep learning and data reconstruction_20250923|Ultra-short-term solar power forecasting by deep learning and data reconstruction]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Long Short-Term Memory Networks|Long Short-Term Memory Networks]]
**🔗 Specific Connectable**: [[keywords/Exogenous Variables in Forecasting|Exogenous Variables in Forecasting]], [[keywords/Model Interpretability|Model Interpretability]]
**⚡ Unique Technical**: [[keywords/Electricity Demand Forecasting|Electricity Demand Forecasting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19374v1 Announce Type: cross 
Abstract: This study presents the development and optimization of a deep learning model based on Long Short-Term Memory (LSTM) networks to predict short-term hourly electricity demand in C\'ordoba, Argentina. Integrating historical consumption data with exogenous variables (climatic factors, temporal cycles, and demographic statistics), the model achieved high predictive precision, with a mean absolute percentage error of 3.20\% and a determination coefficient of 0.95. The inclusion of periodic temporal encodings and weather variables proved crucial to capture seasonal patterns and extreme consumption events, enhancing the robustness and generalizability of the model. In addition to the design and hyperparameter optimization of the LSTM architecture, two complementary analyses were carried out: (i) an interpretability study using Random Forest regression to quantify the relative importance of exogenous drivers, and (ii) an evaluation of model performance in predicting the timing of daily demand maxima and minima, achieving exact-hour accuracy in more than two-thirds of the test days and within abs(1) hour in over 90\% of cases. Together, these results highlight both the predictive accuracy and operational relevance of the proposed framework, providing valuable insights for grid operators seeking optimized planning and control strategies under diverse demand scenarios.

## 📝 요약

이 연구는 아르헨티나 코르도바의 단기 시간별 전력 수요 예측을 위해 LSTM 네트워크 기반의 딥러닝 모델을 개발하고 최적화했습니다. 역사적 소비 데이터와 기후, 시간 주기, 인구 통계 등의 외생 변수를 통합하여 평균 절대 백분율 오차 3.20%와 결정 계수 0.95의 높은 예측 정확도를 달성했습니다. 주기적 시간 인코딩과 기상 변수의 포함은 계절적 패턴과 극단적 소비 사건을 포착하는 데 중요했습니다. LSTM 아키텍처의 설계 및 하이퍼파라미터 최적화 외에도, 랜덤 포레스트 회귀를 사용한 해석 가능성 연구와 일일 수요 최대 및 최소 시점 예측 성능 평가를 수행했습니다. 이 모델은 테스트 일의 3분의 2 이상에서 정확한 시간 예측을, 90% 이상의 경우에서 1시간 이내의 정확도를 보였습니다. 이러한 결과는 제안된 프레임워크의 예측 정확도와 운영상의 중요성을 강조하며, 다양한 수요 시나리오에서 최적화된 계획 및 제어 전략을 찾는 그리드 운영자에게 유용한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 LSTM 네트워크 기반의 딥러닝 모델을 개발하여 아르헨티나 코르도바의 단기 시간별 전력 수요를 예측하는 데 초점을 맞추었습니다.
- 2. 기후 요인, 시간 주기, 인구 통계 등의 외생 변수를 통합하여 평균 절대 백분율 오차 3.20%와 결정 계수 0.95의 높은 예측 정확도를 달성했습니다.
- 3. 주기적 시간 인코딩과 기상 변수의 포함은 계절적 패턴과 극단적 소비 사건을 포착하는 데 중요하여 모델의 강건성과 일반화 가능성을 향상시켰습니다.
- 4. LSTM 아키텍처의 설계 및 하이퍼파라미터 최적화 외에도 외생 요인의 상대적 중요성을 정량화하기 위한 랜덤 포레스트 회귀를 사용한 해석 가능성 연구와 일일 수요 최대 및 최소 시점 예측 성능 평가가 수행되었습니다.
- 5. 제안된 프레임워크는 예측 정확도와 운영상의 중요성을 강조하며, 다양한 수요 시나리오에서 최적의 계획 및 제어 전략을 모색하는 그리드 운영자에게 유용한 통찰력을 제공합니다.


---

*Generated on 2025-09-25 16:51:50*