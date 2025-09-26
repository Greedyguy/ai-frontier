<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:43:58.371280",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Scale Expert Transformers",
    "Time Series Forecasting",
    "Gating Network",
    "General Pre-trained Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Scale Expert Transformers": 0.8,
    "Time Series Forecasting": 0.85,
    "Gating Network": 0.78,
    "General Pre-trained Models": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Scale Expert Transformers",
        "canonical": "Multi-Scale Expert Transformers",
        "aliases": [
          "AdaMixT"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel architecture specifically designed for time series forecasting, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Time Series Forecasting",
        "canonical": "Time Series Forecasting",
        "aliases": [
          "TSF"
        ],
        "category": "specific_connectable",
        "rationale": "A key application domain of the proposed method, linking to broader research in predictive modeling.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Gating Network",
        "canonical": "Gating Network",
        "aliases": [
          "Dynamic Gating"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism is crucial for the adaptive feature of the model, enhancing its connectivity with other adaptive systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      },
      {
        "surface": "General Pre-trained Models",
        "canonical": "General Pre-trained Models",
        "aliases": [
          "GPM"
        ],
        "category": "broad_technical",
        "rationale": "These models are widely used in machine learning, providing a link to pre-existing knowledge bases.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Scale Expert Transformers",
      "resolved_canonical": "Multi-Scale Expert Transformers",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Time Series Forecasting",
      "resolved_canonical": "Time Series Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Gating Network",
      "resolved_canonical": "Gating Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "General Pre-trained Models",
      "resolved_canonical": "General Pre-trained Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# AdaMixT: Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18107.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18107](https://arxiv.org/abs/2509.18107)

## 🔗 유사한 논문
- [[2025-09-23/MTM_ A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification_20250923|MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification]] (86.2% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (84.8% similar)
- [[2025-09-23/Conv-like Scale-Fusion Time Series Transformer_ A Multi-Scale Representation for Variable-Length Long Time Series_20250923|Conv-like Scale-Fusion Time Series Transformer: A Multi-Scale Representation for Variable-Length Long Time Series]] (84.5% similar)
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (84.0% similar)
- [[2025-09-24/SDGF_ Fusing Static and Multi-Scale Dynamic Correlations for Multivariate Time Series Forecasting_20250924|SDGF: Fusing Static and Multi-Scale Dynamic Correlations for Multivariate Time Series Forecasting]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/General Pre-trained Models|General Pre-trained Models]]
**🔗 Specific Connectable**: [[keywords/Time Series Forecasting|Time Series Forecasting]], [[keywords/Gating Network|Gating Network]]
**⚡ Unique Technical**: [[keywords/Multi-Scale Expert Transformers|Multi-Scale Expert Transformers]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18107v1 Announce Type: new 
Abstract: Multivariate time series forecasting involves predicting future values based on historical observations. However, existing approaches primarily rely on predefined single-scale patches or lack effective mechanisms for multi-scale feature fusion. These limitations hinder them from fully capturing the complex patterns inherent in time series, leading to constrained performance and insufficient generalizability. To address these challenges, we propose a novel architecture named Adaptive Weighted Mixture of Multi-Scale Expert Transformers (AdaMixT). Specifically, AdaMixT introduces various patches and leverages both General Pre-trained Models (GPM) and Domain-specific Models (DSM) for multi-scale feature extraction. To accommodate the heterogeneity of temporal features, AdaMixT incorporates a gating network that dynamically allocates weights among different experts, enabling more accurate predictions through adaptive multi-scale fusion. Comprehensive experiments on eight widely used benchmarks, including Weather, Traffic, Electricity, ILI, and four ETT datasets, consistently demonstrate the effectiveness of AdaMixT in real-world scenarios.

## 📝 요약

이 논문은 다변량 시계열 예측의 성능 향상을 위해 새로운 아키텍처인 AdaMixT를 제안합니다. 기존 방법들이 단일 스케일 패치에 의존하거나 다중 스케일 특징 융합 메커니즘이 부족한 점을 극복하고자, AdaMixT는 다양한 패치를 도입하고 일반 사전 학습 모델(GPM)과 도메인 특화 모델(DSM)을 활용하여 다중 스케일 특징을 추출합니다. 또한, 이질적인 시간적 특징을 수용하기 위해 게이팅 네트워크를 통해 전문가들 간의 가중치를 동적으로 할당하여 더 정확한 예측을 가능하게 합니다. 8개의 널리 사용되는 벤치마크 데이터셋에서의 실험 결과, AdaMixT의 효과성이 입증되었습니다.

## 🎯 주요 포인트

- 1. 기존의 다변량 시계열 예측 방법은 단일 스케일 패치에 의존하거나 다중 스케일 특징 융합 메커니즘이 부족하여 복잡한 패턴을 충분히 포착하지 못합니다.
- 2. AdaMixT는 다양한 패치를 도입하고, 일반 사전 학습 모델(GPM)과 도메인 특화 모델(DSM)을 활용하여 다중 스케일 특징을 추출합니다.
- 3. AdaMixT는 게이팅 네트워크를 통해 다양한 전문가들 간의 가중치를 동적으로 할당하여 적응형 다중 스케일 융합을 통해 더 정확한 예측을 가능하게 합니다.
- 4. 8개의 널리 사용되는 벤치마크(Weather, Traffic, Electricity, ILI, 4개의 ETT 데이터셋)에서의 실험 결과, AdaMixT의 실효성을 일관되게 입증하였습니다.


---

*Generated on 2025-09-24 14:43:58*