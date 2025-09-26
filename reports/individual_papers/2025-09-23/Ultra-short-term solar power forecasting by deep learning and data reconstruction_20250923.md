---
keywords:
  - Deep Learning
  - Ultra-Short-Term Solar Power Forecasting
  - CEEMDAN
  - Meteorological Data Integration
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:43:53.423693",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Ultra-Short-Term Solar Power Forecasting",
    "CEEMDAN",
    "Meteorological Data Integration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Ultra-Short-Term Solar Power Forecasting": 0.8,
    "CEEMDAN": 0.78,
    "Meteorological Data Integration": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "deep-learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the proposed method, linking it to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "ultra-short-term solar power prediction",
        "canonical": "Ultra-Short-Term Solar Power Forecasting",
        "aliases": [
          "short-term solar forecasting"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application of forecasting, highlighting the paper's focus and connecting to niche research areas.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "ensemble empirical model decomposition with adaptive noise",
        "canonical": "CEEMDAN",
        "aliases": [
          "ensemble empirical mode decomposition"
        ],
        "category": "unique_technical",
        "rationale": "CEEMDAN is a specialized technique for data decomposition, crucial for understanding the methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "meteorological data integration",
        "canonical": "Meteorological Data Integration",
        "aliases": [
          "weather data integration"
        ],
        "category": "specific_connectable",
        "rationale": "Integrating meteorological data is key for accurate solar power forecasting, linking to environmental data studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "grid stability",
      "energy scheduling",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "deep-learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ultra-short-term solar power prediction",
      "resolved_canonical": "Ultra-Short-Term Solar Power Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ensemble empirical model decomposition with adaptive noise",
      "resolved_canonical": "CEEMDAN",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "meteorological data integration",
      "resolved_canonical": "Meteorological Data Integration",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Ultra-short-term solar power forecasting by deep learning and data reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17095.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17095](https://arxiv.org/abs/2509.17095)

## 🔗 유사한 논문
- [[2025-09-22/SolarCrossFormer_ Improving day-ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors_20250922|SolarCrossFormer: Improving day-ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors]] (84.2% similar)
- [[2025-09-22/Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure_20250922|Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure]] (83.5% similar)
- [[2025-09-22/Solar Forecasting with Causality_ A Graph-Transformer Approach to Spatiotemporal Dependencies_20250922|Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies]] (83.1% similar)
- [[2025-09-23/Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model_20250923|Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model]] (81.4% similar)
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Meteorological Data Integration|Meteorological Data Integration]]
**⚡ Unique Technical**: [[keywords/Ultra-Short-Term Solar Power Forecasting|Ultra-Short-Term Solar Power Forecasting]], [[keywords/CEEMDAN|CEEMDAN]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17095v1 Announce Type: cross 
Abstract: The integration of solar power has been increasing as the green energy transition rolls out. The penetration of solar power challenges the grid stability and energy scheduling, due to its intermittent energy generation. Accurate and near real-time solar power prediction is of critical importance to tolerant and support the permeation of distributed and volatile solar power production in the energy system. In this paper, we propose a deep-learning based ultra-short-term solar power prediction with data reconstruction. We decompose the data for the prediction to facilitate extensive exploration of the spatial and temporal dependencies within the data. Particularly, we reconstruct the data into low- and high-frequency components, using ensemble empirical model decomposition with adaptive noise (CEEMDAN). We integrate meteorological data with those two components, and employ deep-learning models to capture long- and short-term dependencies towards the target prediction period. In this way, we excessively exploit the features in historical data in predicting a ultra-short-term solar power production. Furthermore, as ultra-short-term prediction is vulnerable to local optima, we modify the optimization in our deep-learning training by penalizing long prediction intervals. Numerical experiments with diverse settings demonstrate that, compared to baseline models, the proposed method achieves improved generalization in data reconstruction and higher prediction accuracy for ultra-short-term solar power production.

## 📝 요약

이 논문은 태양광 발전의 변동성을 극복하기 위해 초단기 태양광 발전량을 예측하는 딥러닝 기반 방법론을 제안합니다. 데이터의 공간적, 시간적 의존성을 탐색하기 위해 CEEMDAN 기법을 사용하여 데이터를 저주파 및 고주파 성분으로 분해하고, 기상 데이터를 통합하여 딥러닝 모델로 장단기 의존성을 포착합니다. 또한, 예측의 최적화를 위해 긴 예측 간격에 페널티를 부여하여 지역 최적화를 방지합니다. 다양한 실험 결과, 제안된 방법은 데이터 재구성의 일반화와 초단기 예측 정확도에서 기존 모델보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 태양광 발전의 간헐적인 에너지 생성으로 인해 전력망 안정성과 에너지 스케줄링에 도전 과제가 발생하고 있습니다.
- 2. 본 논문에서는 데이터 재구성을 통한 딥러닝 기반 초단기 태양광 발전 예측 방법을 제안합니다.
- 3. CEEMDAN을 사용하여 데이터를 저주파 및 고주파 성분으로 재구성하고, 기상 데이터를 통합하여 딥러닝 모델로 장단기 의존성을 포착합니다.
- 4. 초단기 예측의 국소 최적화 문제를 해결하기 위해 긴 예측 간격을 페널티로 부여하는 최적화 방법을 수정했습니다.
- 5. 다양한 설정의 수치 실험 결과, 제안된 방법이 초단기 태양광 발전 예측에서 데이터 재구성의 일반화와 예측 정확도를 향상시켰음을 보여줍니다.


---

*Generated on 2025-09-23 23:43:53*