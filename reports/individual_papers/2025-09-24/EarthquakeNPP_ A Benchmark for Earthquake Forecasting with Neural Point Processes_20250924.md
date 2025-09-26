<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:31:10.953024",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Point Processes",
    "Epidemic-Type Aftershock Sequence model",
    "Earthquake Forecasting",
    "Benchmark Datasets"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Point Processes": 0.78,
    "Epidemic-Type Aftershock Sequence model": 0.72,
    "Earthquake Forecasting": 0.7,
    "Benchmark Datasets": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Point Processes",
        "canonical": "Neural Point Processes",
        "aliases": [
          "NPPs"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific advancement in earthquake forecasting, linking machine learning with seismology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Epidemic-Type Aftershock Sequence model",
        "canonical": "Epidemic-Type Aftershock Sequence model",
        "aliases": [
          "ETAS model"
        ],
        "category": "unique_technical",
        "rationale": "ETAS is a well-established model in seismology, providing a baseline for comparing new methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Earthquake Forecasting",
        "canonical": "Earthquake Forecasting",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This is a central theme of the paper, connecting seismology with predictive modeling.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Benchmark Datasets",
        "canonical": "Benchmark Datasets",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Benchmark datasets are crucial for evaluating and comparing forecasting models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "classical point process models",
      "forecasting models",
      "seismology"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Point Processes",
      "resolved_canonical": "Neural Point Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Epidemic-Type Aftershock Sequence model",
      "resolved_canonical": "Epidemic-Type Aftershock Sequence model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Earthquake Forecasting",
      "resolved_canonical": "Earthquake Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Benchmark Datasets",
      "resolved_canonical": "Benchmark Datasets",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# EarthquakeNPP: A Benchmark for Earthquake Forecasting with Neural Point Processes

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2410.08226.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2410.08226](https://arxiv.org/abs/2410.08226)

## 🔗 유사한 논문
- [[2025-09-23/Revealing Hidden Precursors to Earthquakes via a Stress-Sensitive Transformation of Seismic Noise_20250923|Revealing Hidden Precursors to Earthquakes via a Stress-Sensitive Transformation of Seismic Noise]] (80.1% similar)
- [[2025-09-23/Sequential-NIAH_ A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts_20250923|Sequential-NIAH: A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts]] (77.7% similar)
- [[2025-09-23/Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts_20250923|Improving Medium Range Severe Weather Prediction through Transformer Post-processing of AI Weather Forecasts]] (77.7% similar)
- [[2025-09-19/STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP: Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (77.5% similar)
- [[2025-09-24/AdaMixT_ Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting_20250924|AdaMixT: Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Earthquake Forecasting|Earthquake Forecasting]]
**🔗 Specific Connectable**: [[keywords/Benchmark Datasets|Benchmark Datasets]]
**⚡ Unique Technical**: [[keywords/Neural Point Processes|Neural Point Processes]], [[keywords/Epidemic-Type Aftershock Sequence model|Epidemic-Type Aftershock Sequence model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.08226v2 Announce Type: replace-cross 
Abstract: For decades, classical point process models, such as the epidemic-type aftershock sequence (ETAS) model, have been widely used for forecasting the event times and locations of earthquakes. Recent advances have led to Neural Point Processes (NPPs), which promise greater flexibility and improvements over such classical models. However, the currently-used benchmark for NPPs does not represent an up-to-date challenge in the seismological community, since it contains data leakage and omits the largest earthquake sequence from the region. Additionally, initial earthquake forecasting benchmarks fail to compare NPPs with state-of-the-art forecasting models commonly used in seismology. To address these gaps, we introduce EarthquakeNPP: a collection of benchmark datasets to facilitate testing of NPPs on earthquake data, accompanied by an implementation of the state-of-the-art forecasting model: ETAS. The datasets cover a range of small to large target regions within California, dating from 1971 to 2021, and include different methodologies for dataset generation. Benchmarking experiments, using both log-likelihood and generative evaluation metrics widely recognised in seismology, show that none of the five NPPs tested outperform ETAS. These findings suggest that current NPP implementations are not yet suitable for practical earthquake forecasting. Nonetheless, EarthquakeNPP provides a platform to foster future collaboration between the seismology and machine learning communities.

## 📝 요약

이 논문은 지진 예측을 위한 새로운 벤치마크 데이터셋인 EarthquakeNPP를 소개합니다. 기존의 신경망 점 과정(NPP) 모델은 데이터 누출 문제와 대규모 지진 시퀀스 누락으로 인해 최신 지진학적 도전 과제를 반영하지 못했습니다. EarthquakeNPP는 1971년부터 2021년까지 캘리포니아 지역의 다양한 크기의 지진 데이터를 포함하며, 최신 예측 모델인 ETAS와의 비교를 통해 NPP의 성능을 평가합니다. 실험 결과, 테스트된 NPP 모델들이 ETAS를 능가하지 못했으며, 이는 현재의 NPP 구현이 실용적인 지진 예측에 적합하지 않음을 시사합니다. 그러나 EarthquakeNPP는 지진학과 기계 학습 커뮤니티 간의 협력을 촉진할 수 있는 플랫폼을 제공합니다.

## 🎯 주요 포인트

- 1. 전통적인 점 과정 모델인 ETAS 모델은 지진 발생 시점과 위치 예측에 널리 사용되어 왔습니다.
- 2. Neural Point Processes(NPPs)는 기존 모델보다 유연성과 성능 향상을 약속하지만, 현재의 벤치마크는 최신 지진학 커뮤니티의 도전을 반영하지 못합니다.
- 3. EarthquakeNPP는 지진 데이터에 대한 NPP 테스트를 용이하게 하기 위한 벤치마크 데이터셋 모음으로, 최신 예측 모델인 ETAS의 구현을 포함합니다.
- 4. 벤치마킹 실험 결과, 테스트된 5개의 NPP 중 어느 것도 ETAS를 능가하지 못했으며, 이는 현재 NPP 구현이 실질적인 지진 예측에 적합하지 않음을 시사합니다.
- 5. EarthquakeNPP는 지진학과 기계 학습 커뮤니티 간의 미래 협력을 촉진할 플랫폼을 제공합니다.


---

*Generated on 2025-09-24 15:31:10*