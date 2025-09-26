<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:35:40.641957",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "STL-GRU Combined Model",
    "Neural Network",
    "STL Method",
    "Metro Passenger Flow Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "STL-GRU Combined Model": 0.8,
    "Neural Network": 0.85,
    "STL Method": 0.78,
    "Metro Passenger Flow Prediction": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "STL-GRU combined model",
        "canonical": "STL-GRU Combined Model",
        "aliases": [
          "Seasonal and Trend decomposition using Loess and Gated Recurrent Unit"
        ],
        "category": "unique_technical",
        "rationale": "This model is a novel integration of time series decomposition and neural networks, providing a unique approach to metro transportation flow prediction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gated Recurrent Unit",
        "canonical": "Neural Network",
        "aliases": [
          "GRU"
        ],
        "category": "broad_technical",
        "rationale": "GRU is a type of neural network that is widely used in sequence prediction tasks, connecting to the broader field of deep learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Seasonal and Trend decomposition using Loess",
        "canonical": "STL Method",
        "aliases": [
          "STL"
        ],
        "category": "specific_connectable",
        "rationale": "The STL method is crucial for time series analysis, offering a strong link to statistical decomposition techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "metro transfer passenger flow prediction",
        "canonical": "Metro Passenger Flow Prediction",
        "aliases": [
          "transfer passenger flow prediction"
        ],
        "category": "unique_technical",
        "rationale": "This specific application of prediction models is key to optimizing metro operations, providing a unique technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "operation plans",
      "transportation efficiency",
      "prediction accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "STL-GRU combined model",
      "resolved_canonical": "STL-GRU Combined Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gated Recurrent Unit",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Seasonal and Trend decomposition using Loess",
      "resolved_canonical": "STL Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "metro transfer passenger flow prediction",
      "resolved_canonical": "Metro Passenger Flow Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Research on Metro Transportation Flow Prediction Based on the STL-GRU Combined Model

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18130.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18130](https://arxiv.org/abs/2509.18130)

## 🔗 유사한 논문
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (83.8% similar)
- [[2025-09-23/STRATA-TS_ Selective Knowledge Transfer for Urban Time Series Forecasting with Retrieval-Guided Reasoning_20250923|STRATA-TS: Selective Knowledge Transfer for Urban Time Series Forecasting with Retrieval-Guided Reasoning]] (81.1% similar)
- [[2025-09-17/ST-LINK_ Spatially-Aware Large Language Models for Spatio-Temporal Forecasting_20250917|ST-LINK: Spatially-Aware Large Language Models for Spatio-Temporal Forecasting]] (80.8% similar)
- [[2025-09-24/Synthesizing Attitudes, Predicting Actions (SAPA)_ Behavioral Theory-Guided LLMs for Ridesourcing Mode Choice Modeling_20250924|Synthesizing Attitudes, Predicting Actions (SAPA): Behavioral Theory-Guided LLMs for Ridesourcing Mode Choice Modeling]] (80.6% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/STL Method|STL Method]]
**⚡ Unique Technical**: [[keywords/STL-GRU Combined Model|STL-GRU Combined Model]], [[keywords/Metro Passenger Flow Prediction|Metro Passenger Flow Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18130v1 Announce Type: cross 
Abstract: In the metro intelligent transportation system, accurate transfer passenger flow prediction is a key link in optimizing operation plans and improving transportation efficiency. To further improve the theory of metro internal transfer passenger flow prediction and provide more reliable support for intelligent operation decisions, this paper innovatively proposes a metro transfer passenger flow prediction model that integrates the Seasonal and Trend decomposition using Loess (STL) method and Gated Recurrent Unit (GRU).In practical application, the model first relies on the deep learning library Keras to complete the construction and training of the GRU model, laying the foundation for subsequent prediction; then preprocesses the original metro card swiping data, uses the graph-based depth-first search algorithm to identify passengers' travel paths, and further constructs the transfer passenger flow time series; subsequently adopts the STL time series decomposition algorithm to decompose the constructed transfer passenger flow time series into trend component, periodic component and residual component, and uses the 3{\sigma} principle to eliminate and fill the outliers in the residual component, and finally completes the transfer passenger flow prediction.Taking the transfer passenger flow data of a certain metro station as the research sample, the validity of the model is verified. The results show that compared with Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and the combined model of STL time series decomposition method and Long Short-Term Memory (STL-LSTM), the STL-GRU combined prediction model significantly improves the prediction accuracy of transfer passenger flow on weekdays (excluding Fridays), Fridays and rest days, with the mean absolute percentage error (MAPE) of the prediction results reduced by at least 2.3, 1.36 and 6.42 percentage points respectively.

## 📝 요약

이 논문은 지하철 내 환승 승객 흐름 예측을 위한 새로운 모델을 제안합니다. 제안된 모델은 Loess를 이용한 계절 및 추세 분해(STL) 방법과 게이트 순환 유닛(GRU)을 결합하여 구성됩니다. Keras를 활용해 GRU 모델을 구축하고, 지하철 카드 데이터를 전처리하여 승객의 이동 경로를 식별한 후, 환승 승객 흐름 시계열을 구성합니다. STL 알고리즘을 통해 시계열을 분해하고, 이상치를 제거하여 예측을 수행합니다. 실험 결과, 제안된 STL-GRU 모델은 기존의 LSTM, GRU 및 STL-LSTM 모델에 비해 예측 정확도가 크게 향상되었으며, 평균 절대 백분율 오차(MAPE)가 평일, 금요일, 휴일에 각각 최소 2.3, 1.36, 6.42% 포인트 감소했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 지하철 환승 승객 흐름 예측을 위해 STL 방법과 GRU를 통합한 예측 모델을 제안합니다.
- 2. GRU 모델의 구축 및 훈련은 Keras 딥러닝 라이브러리를 사용하여 수행됩니다.
- 3. 원본 지하철 카드 데이터는 그래프 기반 깊이 우선 탐색 알고리즘을 통해 승객의 이동 경로를 식별하고, 환승 승객 흐름 시계열을 구성합니다.
- 4. STL 시계열 분해 알고리즘을 사용하여 구성된 환승 승객 흐름 시계열을 트렌드, 주기, 잔차 성분으로 분해하고, 3σ 원칙을 통해 잔차 성분의 이상치를 제거 및 보완합니다.
- 5. STL-GRU 결합 예측 모델은 LSTM, GRU, STL-LSTM 모델과 비교하여 평일, 금요일, 휴일의 예측 정확도를 각각 최소 2.3, 1.36, 6.42 퍼센트 포인트 개선합니다.


---

*Generated on 2025-09-24 13:35:40*