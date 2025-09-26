---
keywords:
  - Time Series Forecasting
  - BI-LSTM Embedding Denoising Autoencoder
  - Transformer
  - EV Charging Load Prediction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17165
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:46:05.747848",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Time Series Forecasting",
    "BI-LSTM Embedding Denoising Autoencoder",
    "Transformer",
    "EV Charging Load Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Time Series Forecasting": 0.78,
    "BI-LSTM Embedding Denoising Autoencoder": 0.82,
    "Transformer": 0.79,
    "EV Charging Load Prediction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Time Series Forecasting",
        "canonical": "Time Series Forecasting",
        "aliases": [
          "Time Series Prediction"
        ],
        "category": "broad_technical",
        "rationale": "Time Series Forecasting is a fundamental concept in predictive analytics, linking to various forecasting models and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "BI-LSTM Embedding Denoising Autoencoder",
        "canonical": "BI-LSTM Embedding Denoising Autoencoder",
        "aliases": [
          "BDM"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel model proposed in the paper, offering a unique approach to time series forecasting.",
        "novelty_score": 0.85,
        "connectivity_score": 0.64,
        "specificity_score": 0.92,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture in deep learning, relevant for comparing different forecasting methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Electric Vehicle Charging Load Prediction",
        "canonical": "EV Charging Load Prediction",
        "aliases": [
          "Electric Vehicle Load Forecasting"
        ],
        "category": "specific_connectable",
        "rationale": "This specific application of time series forecasting is crucial for energy management and infrastructure planning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Time Series Forecasting",
      "resolved_canonical": "Time Series Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "BI-LSTM Embedding Denoising Autoencoder",
      "resolved_canonical": "BI-LSTM Embedding Denoising Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.64,
        "specificity": 0.92,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Electric Vehicle Charging Load Prediction",
      "resolved_canonical": "EV Charging Load Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Time Series Forecasting Using a Hybrid Deep Learning Method: A Bi-LSTM Embedding Denoising Auto Encoder Transformer

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17165.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17165](https://arxiv.org/abs/2509.17165)

## 🔗 유사한 논문
- [[2025-09-23/A Hybrid PCA-PR-Seq2Seq-Adam-LSTM Framework for Time-Series Power Outage Prediction_20250923|A Hybrid PCA-PR-Seq2Seq-Adam-LSTM Framework for Time-Series Power Outage Prediction]] (82.0% similar)
- [[2025-09-23/Ultra-short-term solar power forecasting by deep learning and data reconstruction_20250923|Ultra-short-term solar power forecasting by deep learning and data reconstruction]] (80.9% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (80.6% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.2% similar)
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Time Series Forecasting|Time Series Forecasting]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/EV Charging Load Prediction|EV Charging Load Prediction]]
**⚡ Unique Technical**: [[keywords/BI-LSTM Embedding Denoising Autoencoder|BI-LSTM Embedding Denoising Autoencoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17165v1 Announce Type: cross 
Abstract: Time series data is a prevalent form of data found in various fields. It consists of a series of measurements taken over time. Forecasting is a crucial application of time series models, where future values are predicted based on historical data. Accurate forecasting is essential for making well-informed decisions across industries. When it comes to electric vehicles (EVs), precise predictions play a key role in planning infrastructure development, load balancing, and energy management. This study introduces a BI-LSTM embedding denoising autoencoder model (BDM) designed to address time series problems, focusing on short-term EV charging load prediction. The performance of the proposed model is evaluated by comparing it with benchmark models like Transformer, CNN, RNN, LSTM, and GRU. Based on the results of the study, the proposed model outperforms the benchmark models in four of the five-time steps, demonstrating its effectiveness for time series forecasting. This research makes a significant contribution to enhancing time series forecasting, thereby improving decision-making processes.

## 📝 요약

이 연구는 전기차(EV) 충전 부하의 단기 예측을 위한 BI-LSTM 임베딩 디노이징 오토인코더 모델(BDM)을 제안합니다. 제안된 모델은 Transformer, CNN, RNN, LSTM, GRU 등 기존 모델과 비교하여 성능을 평가했으며, 다섯 개의 시점 중 네 개에서 더 우수한 성능을 보였습니다. 이를 통해 시계열 예측의 정확성을 높여 의사결정 과정을 개선하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 본 연구는 전기차(EV) 충전 부하 예측을 위한 BI-LSTM 임베딩 잡음 제거 오토인코더 모델(BDM)을 제안합니다.
- 2. 제안된 모델은 Transformer, CNN, RNN, LSTM, GRU 등 벤치마크 모델과 비교하여 성능 평가를 진행했습니다.
- 3. 연구 결과, 제안된 모델은 5개의 시간 단계 중 4개에서 벤치마크 모델을 능가하는 성능을 보였습니다.
- 4. 이 연구는 시계열 예측을 향상시켜 의사 결정 과정을 개선하는 데 중요한 기여를 합니다.
- 5. 전기차 관련 인프라 개발, 부하 균형, 에너지 관리에서 정확한 예측이 중요합니다.


---

*Generated on 2025-09-23 23:46:05*