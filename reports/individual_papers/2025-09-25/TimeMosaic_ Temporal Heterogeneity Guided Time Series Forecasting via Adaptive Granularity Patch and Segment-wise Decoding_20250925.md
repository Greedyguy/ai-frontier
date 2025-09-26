---
keywords:
  - TimeMosaic
  - Adaptive Patch Embedding
  - Segment-wise Decoding
  - Time Series Forecasting
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19406
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:35:10.167349",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "TimeMosaic",
    "Adaptive Patch Embedding",
    "Segment-wise Decoding",
    "Time Series Forecasting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "TimeMosaic": 0.8,
    "Adaptive Patch Embedding": 0.78,
    "Segment-wise Decoding": 0.77,
    "Time Series Forecasting": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "TimeMosaic",
        "canonical": "TimeMosaic",
        "aliases": [
          "Temporal Heterogeneity Guided Forecasting"
        ],
        "category": "unique_technical",
        "rationale": "TimeMosaic is a novel framework specifically designed for addressing temporal heterogeneity in time series forecasting, offering a unique approach not covered by existing canonical terms.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "adaptive patch embedding",
        "canonical": "Adaptive Patch Embedding",
        "aliases": [
          "Dynamic Granularity Adjustment"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to TimeMosaic's approach, allowing for dynamic adjustment of data granularity, which is crucial for capturing temporal heterogeneity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "segment-wise decoding",
        "canonical": "Segment-wise Decoding",
        "aliases": [
          "Horizon-specific Decoding"
        ],
        "category": "unique_technical",
        "rationale": "Segment-wise decoding addresses the heterogeneity of forecasting by adapting to horizon-specific requirements, enhancing the model's adaptability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "multivariate time series forecasting",
        "canonical": "Time Series Forecasting",
        "aliases": [
          "TSF",
          "Multivariate Forecasting"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental domain relevant to the study, providing a broad technical context for the framework's application.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "fixed-length segmentation",
      "information-dense regions",
      "benchmark datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "TimeMosaic",
      "resolved_canonical": "TimeMosaic",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adaptive patch embedding",
      "resolved_canonical": "Adaptive Patch Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "segment-wise decoding",
      "resolved_canonical": "Segment-wise Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "multivariate time series forecasting",
      "resolved_canonical": "Time Series Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# TimeMosaic: Temporal Heterogeneity Guided Time Series Forecasting via Adaptive Granularity Patch and Segment-wise Decoding

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19406.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19406](https://arxiv.org/abs/2509.19406)

## 🔗 유사한 논문
- [[2025-09-24/MOMEMTO_ Patch-based Memory Gate Model in Time Series Foundation Model_20250924|MOMEMTO: Patch-based Memory Gate Model in Time Series Foundation Model]] (85.6% similar)
- [[2025-09-24/AdaMixT_ Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting_20250924|AdaMixT: Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting]] (84.8% similar)
- [[2025-09-23/MTM_ A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification_20250923|MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification]] (83.6% similar)
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (83.1% similar)
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Time Series Forecasting|Time Series Forecasting]]
**⚡ Unique Technical**: [[keywords/TimeMosaic|TimeMosaic]], [[keywords/Adaptive Patch Embedding|Adaptive Patch Embedding]], [[keywords/Segment-wise Decoding|Segment-wise Decoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19406v1 Announce Type: cross 
Abstract: Multivariate time series forecasting is essential in domains such as finance, transportation, climate, and energy. However, existing patch-based methods typically adopt fixed-length segmentation, overlooking the heterogeneity of local temporal dynamics and the decoding heterogeneity of forecasting. Such designs lose details in information-dense regions, introduce redundancy in stable segments, and fail to capture the distinct complexities of short-term and long-term horizons. We propose TimeMosaic, a forecasting framework that aims to address temporal heterogeneity. TimeMosaic employs adaptive patch embedding to dynamically adjust granularity according to local information density, balancing motif reuse with structural clarity while preserving temporal continuity. In addition, it introduces segment-wise decoding that treats each prediction horizon as a related subtask and adapts to horizon-specific difficulty and information requirements, rather than applying a single uniform decoder. Extensive evaluations on benchmark datasets demonstrate that TimeMosaic delivers consistent improvements over existing methods, and our model trained on the large-scale corpus with 321 billion observations achieves performance competitive with state-of-the-art TSFMs.

## 📝 요약

TimeMosaic은 금융, 교통, 기후, 에너지 분야에서 중요한 다변량 시계열 예측을 개선하기 위한 새로운 프레임워크입니다. 기존의 고정 길이 세분화 방식의 한계를 극복하기 위해, TimeMosaic은 지역 정보 밀도에 따라 적응적으로 패치 임베딩을 조정하여 시간적 이질성을 처리합니다. 또한, 각 예측 지평선을 관련된 하위 작업으로 취급하는 세그먼트별 디코딩을 도입하여 지평선별 난이도와 정보 요구에 적응합니다. 벤치마크 데이터셋을 통한 평가 결과, TimeMosaic은 기존 방법들보다 일관된 성능 향상을 보여주었으며, 3210억 개의 관측치로 학습된 모델은 최신 시계열 예측 모델들과 경쟁할 만한 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. TimeMosaic는 지역 정보 밀도에 따라 적응적으로 패치 임베딩을 조정하여 시간적 이질성을 해결하는 예측 프레임워크입니다.
- 2. 이 프레임워크는 모티프 재사용과 구조적 명확성을 균형 있게 유지하면서 시간적 연속성을 보존합니다.
- 3. TimeMosaic는 각 예측 지평선을 관련된 하위 작업으로 처리하고, 지평선별 난이도와 정보 요구에 적응하는 세그먼트별 디코딩을 도입합니다.
- 4. 벤치마크 데이터셋에 대한 광범위한 평가에서 TimeMosaic는 기존 방법들보다 일관된 성능 향상을 보여줍니다.
- 5. 3210억 개의 관측치로 구성된 대규모 코퍼스에서 훈련된 모델은 최첨단 시계열 예측 모델들과 경쟁력 있는 성능을 달성합니다.


---

*Generated on 2025-09-25 15:35:10*