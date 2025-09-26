---
keywords:
  - STL-FFT-STFT-TCN-LSTM Model
  - Wave Height Prediction
  - Temporal Convolutional Network
  - Long Short-Term Memory
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19313
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:50:06.671751",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "STL-FFT-STFT-TCN-LSTM Model",
    "Wave Height Prediction",
    "Temporal Convolutional Network",
    "Long Short-Term Memory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "STL-FFT-STFT-TCN-LSTM Model": 0.8,
    "Wave Height Prediction": 0.78,
    "Temporal Convolutional Network": 0.72,
    "Long Short-Term Memory": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "STL-FFT-STFT-TCN-LSTM",
        "canonical": "STL-FFT-STFT-TCN-LSTM Model",
        "aliases": [
          "Hybrid Wave Prediction Model"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper's contribution, combining multiple techniques for wave height prediction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Significant Wave Height",
        "canonical": "Wave Height Prediction",
        "aliases": [
          "WVHT",
          "Wave Height"
        ],
        "category": "specific_connectable",
        "rationale": "Wave height prediction is a key application area for the model, linking it to broader environmental and energy studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Temporal Convolutional Network",
        "canonical": "Temporal Convolutional Network",
        "aliases": [
          "TCN"
        ],
        "category": "broad_technical",
        "rationale": "TCN is a significant component of the model, relevant to discussions on time-series analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Long Short-Term Memory",
        "canonical": "Long Short-Term Memory",
        "aliases": [
          "LSTM"
        ],
        "category": "broad_technical",
        "rationale": "LSTM is a widely used neural network architecture for sequence prediction, relevant to the model's design.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "energy",
      "model",
      "prediction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "STL-FFT-STFT-TCN-LSTM",
      "resolved_canonical": "STL-FFT-STFT-TCN-LSTM Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Significant Wave Height",
      "resolved_canonical": "Wave Height Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Temporal Convolutional Network",
      "resolved_canonical": "Temporal Convolutional Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Long Short-Term Memory",
      "resolved_canonical": "Long Short-Term Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# STL-FFT-STFT-TCN-LSTM: An Effective Wave Height High Accuracy Prediction Model Fusing Time-Frequency Domain Features

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19313.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19313](https://arxiv.org/abs/2509.19313)

## 🔗 유사한 논문
- [[2025-09-17/Artificial neural networks ensemble methodology to predict significant wave height_20250917|Artificial neural networks ensemble methodology to predict significant wave height]] (84.2% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.8% similar)
- [[2025-09-23/Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts_20250923|Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts]] (82.3% similar)
- [[2025-09-23/Ultra-short-term solar power forecasting by deep learning and data reconstruction_20250923|Ultra-short-term solar power forecasting by deep learning and data reconstruction]] (82.2% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Temporal Convolutional Network|Temporal Convolutional Network]], [[keywords/Long Short-Term Memory|Long Short-Term Memory]]
**🔗 Specific Connectable**: [[keywords/Wave Height Prediction|Wave Height Prediction]]
**⚡ Unique Technical**: [[keywords/STL-FFT-STFT-TCN-LSTM Model|STL-FFT-STFT-TCN-LSTM Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19313v1 Announce Type: cross 
Abstract: As the consumption of traditional energy sources intensifies and their adverse environmental impacts become more pronounced, wave energy stands out as a highly promising member of the renewable energy family due to its high energy density, stability, widespread distribution, and environmental friendliness. The key to its development lies in the precise prediction of Significant Wave Height (WVHT). However, wave energy signals exhibit strong nonlinearity, abrupt changes, multi-scale periodicity, data sparsity, and high-frequency noise interference; additionally, physical models for wave energy prediction incur extremely high computational costs. To address these challenges, this study proposes a hybrid model combining STL-FFT-STFT-TCN-LSTM. This model exploits the Seasonal-Trend Decomposition Procedure based on Loess (STL), Fast Fourier Transform (FFT), Short-Time Fourier Transform (STFT), Temporal Convolutional Network (TCN), and Long Short-Term Memory (LSTM) technologies. The model aims to optimize multi-scale feature fusion, capture extreme wave heights, and address issues related to high-frequency noise and periodic signals, thereby achieving efficient and accurate prediction of significant wave height. Experiments were conducted using hourly data from NOAA Station 41008 and 41047 spanning 2019 to 2022. The results showed that compared with other single models and hybrid models, the STL-FFT-STFT-TCN-LSTM model achieved significantly higher prediction accuracy in capturing extreme wave heights and suppressing high-frequency noise, with MAE reduced by 15.8\%-40.5\%, SMAPE reduced by 8.3\%-20.3\%, and R increased by 1.31\%-2.9\%; in ablation experiments, the model also demonstrated the indispensability of each component step, validating its superiority in multi-scale feature fusion.

## 📝 요약

이 연구는 파랑 에너지의 중요한 요소인 유의파고 예측을 개선하기 위해 STL-FFT-STFT-TCN-LSTM이라는 하이브리드 모델을 제안합니다. 이 모델은 비선형성, 급격한 변화, 다중 스케일 주기성, 데이터 희소성, 고주파 노이즈 등의 문제를 해결하기 위해 설계되었습니다. 제안된 모델은 다중 스케일 특징 융합을 최적화하고 극한 파고를 포착하며, 고주파 노이즈와 주기 신호 문제를 해결하여 유의파고를 효율적이고 정확하게 예측합니다. NOAA의 2019-2022년 시간별 데이터를 사용한 실험 결과, 이 모델은 다른 모델들에 비해 예측 정확도가 높았으며, MAE와 SMAPE가 각각 15.8%-40.5%, 8.3%-20.3% 감소하고, R 값이 1.31%-2.9% 증가했습니다. 또한, 각 구성 요소의 필수성을 입증하여 다중 스케일 특징 융합에서의 우수성을 확인했습니다.

## 🎯 주요 포인트

- 1. 파랑 에너지는 높은 에너지 밀도, 안정성, 환경 친화성으로 주목받는 재생 에너지원입니다.
- 2. 파랑 에너지 예측의 핵심은 유의 파고의 정확한 예측에 있으며, 이를 위해 복합 모델 STL-FFT-STFT-TCN-LSTM을 제안했습니다.
- 3. 제안된 모델은 다중 스케일 특징 융합을 최적화하고, 극단적 파고를 포착하며, 고주파 잡음 및 주기 신호 문제를 해결합니다.
- 4. NOAA 관측소 데이터를 사용한 실험 결과, 제안된 모델은 다른 모델 대비 예측 정확도가 크게 향상되었습니다.
- 5. 절제 실험에서 각 구성 요소의 필수성을 입증하며, 다중 스케일 특징 융합에서의 우수성을 확인했습니다.


---

*Generated on 2025-09-25 16:50:06*