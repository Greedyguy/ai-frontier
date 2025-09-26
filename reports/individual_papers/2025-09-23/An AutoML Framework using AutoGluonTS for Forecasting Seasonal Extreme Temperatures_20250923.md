---
keywords:
  - AutoGluonTS
  - Meteorological Forecasting
  - Maximum Temperature Prediction
  - Temporal Classification
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17734
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:56:02.623343",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AutoGluonTS",
    "Meteorological Forecasting",
    "Maximum Temperature Prediction",
    "Temporal Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AutoGluonTS": 0.78,
    "Meteorological Forecasting": 0.65,
    "Maximum Temperature Prediction": 0.75,
    "Temporal Classification": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AutoGluonTS",
        "canonical": "AutoGluonTS",
        "aliases": [
          "AutoGluon Time Series"
        ],
        "category": "unique_technical",
        "rationale": "AutoGluonTS is a specific AutoML tool used for time series forecasting, which is central to the study's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "forecasting meteorological variables",
        "canonical": "Meteorological Forecasting",
        "aliases": [
          "weather forecasting"
        ],
        "category": "broad_technical",
        "rationale": "Meteorological forecasting is a broad technical domain relevant to the study's focus on temperature prediction.",
        "novelty_score": 0.45,
        "connectivity_score": 0.72,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "maximum daily temperatures",
        "canonical": "Maximum Temperature Prediction",
        "aliases": [
          "max temperature forecasting"
        ],
        "category": "specific_connectable",
        "rationale": "Predicting maximum temperatures is a specific challenge addressed in the study, linking to climatological research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "temporal classification problem",
        "canonical": "Temporal Classification",
        "aliases": [
          "time series classification"
        ],
        "category": "specific_connectable",
        "rationale": "Temporal classification is a key methodological approach in the study, relevant for linking to machine learning techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "deep learning architectures",
      "large historical dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AutoGluonTS",
      "resolved_canonical": "AutoGluonTS",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "forecasting meteorological variables",
      "resolved_canonical": "Meteorological Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.72,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "maximum daily temperatures",
      "resolved_canonical": "Maximum Temperature Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "temporal classification problem",
      "resolved_canonical": "Temporal Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# An AutoML Framework using AutoGluonTS for Forecasting Seasonal Extreme Temperatures

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17734.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17734](https://arxiv.org/abs/2509.17734)

## 🔗 유사한 논문
- [[2025-09-23/Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model_20250923|Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model]] (80.8% similar)
- [[2025-09-23/Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts_20250923|Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts]] (79.9% similar)
- [[2025-09-22/Solar Forecasting with Causality_ A Graph-Transformer Approach to Spatiotemporal Dependencies_20250922|Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies]] (79.5% similar)
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations: 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (79.4% similar)
- [[2025-09-22/ArchesClimate_ Probabilistic Decadal Ensemble Generation With Flow Matching_20250922|ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Meteorological Forecasting|Meteorological Forecasting]]
**🔗 Specific Connectable**: [[keywords/Maximum Temperature Prediction|Maximum Temperature Prediction]], [[keywords/Temporal Classification|Temporal Classification]]
**⚡ Unique Technical**: [[keywords/AutoGluonTS|AutoGluonTS]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17734v1 Announce Type: new 
Abstract: In recent years, great progress has been made in the field of forecasting meteorological variables. Recently, deep learning architectures have made a major breakthrough in forecasting the daily average temperature over a ten-day horizon. However, advances in forecasting events related to the maximum temperature over short horizons remain a challenge for the community. A problem that is even more complex consists in making predictions of the maximum daily temperatures in the short, medium, and long term. In this work, we focus on forecasting events related to the maximum daily temperature over medium-term periods (90 days). Therefore, instead of addressing the problem from a meteorological point of view, this article tackles it from a climatological point of view. Due to the complexity of this problem, a common approach is to frame the study as a temporal classification problem with the classes: maximum temperature "above normal", "normal" or "below normal". From a practical point of view, we created a large historical dataset (from 1981 to 2018) collecting information from weather stations located in South America. In addition, we also integrated exogenous information from the Pacific, Atlantic, and Indian Ocean basins. We applied the AutoGluonTS platform to solve the above-mentioned problem. This AutoML tool shows competitive forecasting performance with respect to large operational platforms dedicated to tackling this climatological problem; but with a "relatively" low computational cost in terms of time and resources.

## 📝 요약

이 논문은 중기(90일) 최대 일일 기온 예측을 다루며, 기상학적 관점이 아닌 기후학적 관점에서 접근합니다. 연구는 남미 기상 관측소의 1981년부터 2018년까지의 대규모 역사적 데이터셋과 태평양, 대서양, 인도양의 외부 정보를 통합하여 최대 기온을 "정상 이상", "정상", "정상 이하"로 분류하는 문제로 설정했습니다. AutoGluonTS 플랫폼을 사용하여 이 문제를 해결했으며, 이는 대규모 운영 플랫폼과 비교해 경쟁력 있는 성능을 보이면서도 시간과 자원 측면에서 상대적으로 낮은 계산 비용을 제공합니다.

## 🎯 주요 포인트

- 1. 최근 심층 학습 구조는 10일 간격의 일평균 기온 예측에서 주요한 돌파구를 마련했습니다.
- 2. 최대 기온과 관련된 단기 예측 이벤트는 여전히 도전 과제로 남아 있습니다.
- 3. 본 연구는 중기(90일) 최대 일일 기온 예측에 초점을 맞추고 있으며, 기상학적 관점이 아닌 기후학적 관점에서 문제를 접근합니다.
- 4. 1981년부터 2018년까지 남미 기상 관측소의 데이터를 수집하여 대규모 역사적 데이터셋을 구축하였습니다.
- 5. AutoGluonTS 플랫폼을 사용하여 예측 문제를 해결했으며, 이는 시간 및 자원 측면에서 상대적으로 낮은 계산 비용으로 경쟁력 있는 성능을 보여줍니다.


---

*Generated on 2025-09-24 01:56:02*