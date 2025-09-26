---
keywords:
  - Graph Neural Network
  - Spatiotemporal Dependencies
  - Causality
  - Attention Mechanism
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15481
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:26:19.729101",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Spatiotemporal Dependencies",
    "Causality",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.82,
    "Spatiotemporal Dependencies": 0.78,
    "Causality": 0.75,
    "Attention Mechanism": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph-Transformer Approach",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph Transformer",
          "Graph-Transformer"
        ],
        "category": "specific_connectable",
        "rationale": "Combining graph neural networks with transformers highlights a novel approach to modeling spatiotemporal dependencies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Spatiotemporal Dependencies",
        "canonical": "Spatiotemporal Dependencies",
        "aliases": [
          "Spatiotemporal Relations",
          "Spatiotemporal Patterns"
        ],
        "category": "unique_technical",
        "rationale": "Understanding spatiotemporal dependencies is crucial for accurate solar forecasting and links to other temporal modeling work.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Causality",
        "canonical": "Causality",
        "aliases": [
          "Causal Inference",
          "Causal Modeling"
        ],
        "category": "broad_technical",
        "rationale": "Causality is a foundational concept that enhances the understanding of dependencies in solar forecasting.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.67,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gated Transformer",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Gated Transformer Model",
          "Gated Attention"
        ],
        "category": "specific_connectable",
        "rationale": "The gated transformer is a variant of the attention mechanism, which is central to modern neural networks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "SolarCAST",
      "Solcast",
      "GHI"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph-Transformer Approach",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Spatiotemporal Dependencies",
      "resolved_canonical": "Spatiotemporal Dependencies",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Causality",
      "resolved_canonical": "Causality",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.67,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gated Transformer",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies

**Korean Title:** 태양광 예측의 인과성: 시공간적 종속성에 대한 그래프-트랜스포머 접근법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15481.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15481](https://arxiv.org/abs/2509.15481)

## 🔗 유사한 논문
- [[2025-09-22/SolarCrossFormer_ Improving day-ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors_20250922|SolarCrossFormer: Improving day-ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors]] (86.3% similar)
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations: 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (82.6% similar)
- [[2025-09-22/Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments_20250922|Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments]] (81.0% similar)
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (80.1% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Causality|Causality]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Spatiotemporal Dependencies|Spatiotemporal Dependencies]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15481v1 Announce Type: new 
Abstract: Accurate solar forecasting underpins effective renewable energy management. We present SolarCAST, a causally informed model predicting future global horizontal irradiance (GHI) at a target site using only historical GHI from site X and nearby stations S - unlike prior work that relies on sky-camera or satellite imagery requiring specialized hardware and heavy preprocessing. To deliver high accuracy with only public sensor data, SolarCAST models three classes of confounding factors behind X-S correlations using scalable neural components: (i) observable synchronous variables (e.g., time of day, station identity), handled via an embedding module; (ii) latent synchronous factors (e.g., regional weather patterns), captured by a spatio-temporal graph neural network; and (iii) time-lagged influences (e.g., cloud movement across stations), modeled with a gated transformer that learns temporal shifts. It outperforms leading time-series and multimodal baselines across diverse geographical conditions, and achieves a 25.9% error reduction over the top commercial forecaster, Solcast. SolarCAST offers a lightweight, practical, and generalizable solution for localized solar forecasting.

## 🔍 Abstract (한글 번역)

arXiv:2509.15481v1 발표 유형: 신규  
초록: 정확한 태양광 예측은 효과적인 재생 에너지 관리의 기반이 됩니다. 우리는 SolarCAST를 소개합니다. 이 모델은 사이트 X와 인근 관측소 S의 과거 글로벌 수평 일사량(GHI)만을 사용하여 목표 지점의 미래 GHI를 예측하는 인과적으로 정보가 제공된 모델입니다. 이는 특수 하드웨어와 대량의 전처리가 필요한 하늘 카메라나 위성 이미지를 활용하는 기존 연구와 다릅니다. 공공 센서 데이터만으로 높은 정확도를 제공하기 위해, SolarCAST는 X-S 상관관계의 세 가지 유형의 혼란 요인을 확장 가능한 신경 구성 요소를 사용하여 모델링합니다: (i) 동기화된 관측 변수(예: 시간, 관측소 식별)를 임베딩 모듈을 통해 처리; (ii) 잠재적 동기화 요인(예: 지역 기상 패턴)을 시공간 그래프 신경망으로 포착; (iii) 시간 지연 영향을 게이트 트랜스포머로 모델링하여 시간적 변화를 학습합니다. 이는 다양한 지리적 조건에서 선도적인 시계열 및 다중 모달 기준을 능가하며, 상업적 예측자 Solcast에 비해 25.9%의 오류 감소를 달성합니다. SolarCAST는 지역화된 태양광 예측을 위한 경량, 실용적, 그리고 일반화 가능한 솔루션을 제공합니다.

## 📝 요약

SolarCAST는 역사적 전역 수평면 일사량(GHI) 데이터만을 사용하여 특정 지역의 미래 GHI를 예측하는 모델로, 기존의 하드웨어 의존적인 방법과 달리 공공 센서 데이터를 활용합니다. 이 모델은 X와 S 간의 상관관계에 영향을 미치는 세 가지 요인을 다루기 위해 확장 가능한 신경망을 사용합니다: (i) 동기 변수는 임베딩 모듈로 처리하고, (ii) 잠재적인 동기 요인은 시공간 그래프 신경망으로 포착하며, (iii) 시간 지연 영향은 게이트 트랜스포머로 학습합니다. 다양한 지리적 조건에서 기존의 시계열 및 다중 모달 베이스라인을 능가하며, 상업적 예측기 Solcast 대비 25.9%의 오류 감소를 달성합니다. SolarCAST는 경량화된 실용적 솔루션으로, 지역화된 태양광 예측에 기여합니다.

## 🎯 주요 포인트

- 1. SolarCAST는 역사적 GHI 데이터만을 사용하여 목표 지점의 미래 GHI를 예측하는 모델로, 특수 하드웨어나 복잡한 전처리가 필요하지 않습니다.
- 2. 이 모델은 X-S 상관관계의 혼란 요인을 세 가지 범주로 나누어 처리하며, 각각을 확장 가능한 신경망 구성 요소로 모델링합니다.
- 3. SolarCAST는 다양한 지리적 조건에서 기존의 시계열 및 멀티모달 기준 모델을 능가하며, 상업용 예측기 Solcast에 비해 25.9%의 오차 감소를 달성했습니다.
- 4. 이 모델은 가벼우면서도 실용적이며, 지역화된 태양광 예측에 일반적으로 적용 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-23 10:26:19*