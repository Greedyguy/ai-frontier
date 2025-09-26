---
keywords:
  - ArchesClimate
  - Deep Learning
  - Climate Model Emulator
  - Flow Matching
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15942
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:22:08.634370",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ArchesClimate",
    "Deep Learning",
    "Climate Model Emulator",
    "Flow Matching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ArchesClimate": 0.78,
    "Deep Learning": 0.85,
    "Climate Model Emulator": 0.8,
    "Flow Matching": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ArchesClimate",
        "canonical": "ArchesClimate",
        "aliases": [
          "Arches Climate Model Emulator"
        ],
        "category": "unique_technical",
        "rationale": "ArchesClimate is a novel deep learning-based climate model emulator that significantly reduces computational costs, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology for the ArchesClimate model, linking it to a broad range of machine learning applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Climate Model Emulator",
        "canonical": "Climate Model Emulator",
        "aliases": [
          "Climate Emulator"
        ],
        "category": "specific_connectable",
        "rationale": "Climate Model Emulators are crucial for reducing computational costs in climate simulations, connecting this work to broader climate modeling efforts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Flow Matching",
        "canonical": "Flow Matching",
        "aliases": [
          "Flow Matching Technique"
        ],
        "category": "unique_technical",
        "rationale": "Flow Matching is a specific technique adapted in this work to predict near-term climate, offering a unique technical perspective.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "climate projections",
      "climate variables",
      "hindcasts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ArchesClimate",
      "resolved_canonical": "ArchesClimate",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Climate Model Emulator",
      "resolved_canonical": "Climate Model Emulator",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Flow Matching",
      "resolved_canonical": "Flow Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching

**Korean Title:** ArchesClimate: 흐름 매칭을 통한 확률적 10년 단위 앙상블 생성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15942.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15942](https://arxiv.org/abs/2509.15942)

## 🔗 유사한 논문
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (78.9% similar)
- [[2025-09-22/Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments_20250922|Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments]] (78.5% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.2% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (78.1% similar)
- [[2025-09-17/Artificial neural networks ensemble methodology to predict significant wave height_20250917|Artificial neural networks ensemble methodology to predict significant wave height]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Climate Model Emulator|Climate Model Emulator]]
**⚡ Unique Technical**: [[keywords/ArchesClimate|ArchesClimate]], [[keywords/Flow Matching|Flow Matching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15942v1 Announce Type: cross 
Abstract: Climate projections have uncertainties related to components of the climate system and their interactions. A typical approach to quantifying these uncertainties is to use climate models to create ensembles of repeated simulations under different initial conditions. Due to the complexity of these simulations, generating such ensembles of projections is computationally expensive. In this work, we present ArchesClimate, a deep learning-based climate model emulator that aims to reduce this cost. ArchesClimate is trained on decadal hindcasts of the IPSL-CM6A-LR climate model at a spatial resolution of approximately 2.5x1.25 degrees. We train a flow matching model following ArchesWeatherGen, which we adapt to predict near-term climate. Once trained, the model generates states at a one-month lead time and can be used to auto-regressively emulate climate model simulations of any length. We show that for up to 10 years, these generations are stable and physically consistent. We also show that for several important climate variables, ArchesClimate generates simulations that are interchangeable with the IPSL model. This work suggests that climate model emulators could significantly reduce the cost of climate model simulations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15942v1 발표 유형: 교차  
초록: 기후 예측에는 기후 시스템의 구성 요소와 그 상호작용과 관련된 불확실성이 존재합니다. 이러한 불확실성을 정량화하는 일반적인 접근 방식은 기후 모델을 사용하여 다양한 초기 조건 하에서 반복된 시뮬레이션의 앙상블을 생성하는 것입니다. 이러한 시뮬레이션의 복잡성으로 인해 이러한 예측 앙상블을 생성하는 것은 계산 비용이 많이 듭니다. 이 연구에서는 이러한 비용을 줄이기 위한 딥러닝 기반 기후 모델 에뮬레이터인 ArchesClimate를 제시합니다. ArchesClimate는 약 2.5x1.25도의 공간 해상도로 IPSL-CM6A-LR 기후 모델의 10년간의 힌드캐스트에 대해 학습됩니다. 우리는 ArchesWeatherGen을 따라 흐름 매칭 모델을 학습하며, 이를 단기 기후 예측에 맞게 조정합니다. 학습이 완료되면, 모델은 한 달 앞서 상태를 생성하며, 어떤 길이의 기후 모델 시뮬레이션도 자동 회귀적으로 에뮬레이트할 수 있습니다. 우리는 최대 10년 동안 이러한 생성이 안정적이고 물리적으로 일관됨을 보여줍니다. 또한, 여러 중요한 기후 변수에 대해 ArchesClimate가 IPSL 모델과 교환 가능한 시뮬레이션을 생성함을 보여줍니다. 이 연구는 기후 모델 에뮬레이터가 기후 모델 시뮬레이션의 비용을 크게 줄일 수 있음을 시사합니다.

## 📝 요약

이 연구는 기후 예측의 불확실성을 줄이기 위해 ArchesClimate라는 딥러닝 기반 기후 모델 에뮬레이터를 제안합니다. ArchesClimate는 IPSL-CM6A-LR 기후 모델의 10년간의 예측 데이터를 학습하여, 복잡하고 비용이 많이 드는 기후 모델 시뮬레이션을 효율적으로 대체할 수 있습니다. 이 모델은 한 달 앞의 기후 상태를 예측하고, 자동 회귀적으로 긴 기간의 기후 시뮬레이션을 생성할 수 있습니다. 연구 결과, ArchesClimate는 최대 10년 동안 안정적이고 물리적으로 일관된 시뮬레이션을 생성하며, 중요한 기후 변수에 대해 IPSL 모델과 상호 교환 가능함을 보여줍니다. 이는 기후 모델 시뮬레이션 비용을 크게 줄일 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. ArchesClimate는 딥러닝 기반의 기후 모델 에뮬레이터로, 기후 예측 시뮬레이션의 비용을 줄이는 것을 목표로 한다.
- 2. 이 모델은 IPSL-CM6A-LR 기후 모델의 10년간의 후향 예측 데이터를 기반으로 학습되었다.
- 3. ArchesClimate는 한 달 선행 예측을 생성하며, 자가 회귀 방식으로 기후 모델 시뮬레이션을 모방할 수 있다.
- 4. 최대 10년 동안 생성된 예측은 안정적이며 물리적으로 일관성을 유지한다.
- 5. ArchesClimate는 여러 중요한 기후 변수에 대해 IPSL 모델과 상호 교환 가능한 시뮬레이션을 생성할 수 있다.


---

*Generated on 2025-09-23 09:22:08*