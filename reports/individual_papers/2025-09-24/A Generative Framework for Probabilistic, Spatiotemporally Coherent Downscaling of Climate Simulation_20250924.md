<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:21:59.001023",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Framework",
    "Spatiotemporal Downscaling",
    "Diffusion Model",
    "Reanalysis Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Framework": 0.72,
    "Spatiotemporal Downscaling": 0.68,
    "Diffusion Model": 0.81,
    "Reanalysis Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generative Framework",
        "canonical": "Generative Framework",
        "aliases": [
          "Generative Model"
        ],
        "category": "broad_technical",
        "rationale": "This concept is central to the paper's methodology and connects to various generative modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Spatiotemporally Coherent Downscaling",
        "canonical": "Spatiotemporal Downscaling",
        "aliases": [
          "Spatiotemporal Coherence"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach that combines spatial and temporal coherence, crucial for climate modeling.",
        "novelty_score": 0.72,
        "connectivity_score": 0.64,
        "specificity_score": 0.82,
        "link_intent_score": 0.68
      },
      {
        "surface": "Score-based Diffusion Model",
        "canonical": "Diffusion Model",
        "aliases": [
          "Score-based Model"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are gaining traction in generative modeling, providing a link to recent advancements.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "High-resolution Reanalysis Data",
        "canonical": "Reanalysis Data",
        "aliases": [
          "High-resolution Data"
        ],
        "category": "specific_connectable",
        "rationale": "Reanalysis data is essential for validating climate models, offering strong connectivity to climate research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.71,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "Local climate information",
      "Coarse global climate simulations",
      "Weather patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Generative Framework",
      "resolved_canonical": "Generative Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Spatiotemporally Coherent Downscaling",
      "resolved_canonical": "Spatiotemporal Downscaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.64,
        "specificity": 0.82,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Score-based Diffusion Model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "High-resolution Reanalysis Data",
      "resolved_canonical": "Reanalysis Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.71,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Generative Framework for Probabilistic, Spatiotemporally Coherent Downscaling of Climate Simulation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2412.15361.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2412.15361](https://arxiv.org/abs/2412.15361)

## 🔗 유사한 논문
- [[2025-09-23/Are Deep Learning Methods Suitable for Downscaling Global Climate Projections? An Intercomparison for Temperature and Precipitation over Spain_20250923|Are Deep Learning Methods Suitable for Downscaling Global Climate Projections? An Intercomparison for Temperature and Precipitation over Spain]] (84.5% similar)
- [[2025-09-23/Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model_20250923|Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model]] (83.3% similar)
- [[2025-09-24/DS-Diffusion_ Data Style-Guided Diffusion Model for Time-Series Generation_20250924|DS-Diffusion: Data Style-Guided Diffusion Model for Time-Series Generation]] (82.9% similar)
- [[2025-09-24/Adaptive Learning in Spatial Agent-Based Models for Climate Risk Assessment_ A Geospatial Framework with Evolutionary Economic Agents_20250924|Adaptive Learning in Spatial Agent-Based Models for Climate Risk Assessment: A Geospatial Framework with Evolutionary Economic Agents]] (82.5% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Framework|Generative Framework]]
**🔗 Specific Connectable**: [[keywords/Diffusion Model|Diffusion Model]], [[keywords/Reanalysis Data|Reanalysis Data]]
**⚡ Unique Technical**: [[keywords/Spatiotemporal Downscaling|Spatiotemporal Downscaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.15361v4 Announce Type: replace 
Abstract: Local climate information is crucial for impact assessment and decision-making, yet coarse global climate simulations cannot capture small-scale phenomena. Current statistical downscaling methods infer these phenomena as temporally decoupled spatial patches. However, to preserve physical properties, estimating spatio-temporally coherent high-resolution weather dynamics for multiple variables across long time horizons is crucial. We present a novel generative framework that uses a score-based diffusion model trained on high-resolution reanalysis data to capture the statistical properties of local weather dynamics. After training, we condition on coarse climate model data to generate weather patterns consistent with the aggregate information. As this predictive task is inherently uncertain, we leverage the probabilistic nature of diffusion models and sample multiple trajectories. We evaluate our approach with high-resolution reanalysis information before applying it to the climate model downscaling task. We then demonstrate that the model generates spatially and temporally coherent weather dynamics that align with global climate output.

## 📝 요약

이 논문은 지역 기후 정보를 보다 정확하게 예측하기 위한 새로운 생성적 프레임워크를 제안합니다. 기존의 통계적 다운스케일링 방법은 시간적으로 분리된 공간 패턴을 추론하는 데 그쳤으나, 본 연구는 고해상도 재분석 데이터를 활용한 점수 기반 확산 모델을 통해 다변수의 장기적인 시공간 일관성을 유지하는 기상 동역학을 추정합니다. 훈련 후, 이 모델은 대규모 기후 모델 데이터를 조건으로 하여 일관된 기상 패턴을 생성합니다. 확산 모델의 확률적 특성을 활용하여 여러 경로를 샘플링하며, 고해상도 재분석 정보를 통해 접근법을 평가한 후, 기후 모델 다운스케일링에 적용하여 글로벌 기후 출력과 일치하는 시공간적으로 일관된 기상 동역학을 생성함을 입증합니다.

## 🎯 주요 포인트

- 1. 지역 기후 정보는 영향 평가와 의사 결정에 필수적이지만, 전 지구적 기후 시뮬레이션은 소규모 현상을 포착하지 못한다.
- 2. 기존의 통계적 다운스케일링 방법은 시간적으로 분리된 공간 패치를 추론하지만, 물리적 속성을 보존하기 위해서는 시공간적으로 일관된 고해상도 날씨 동역학 추정이 중요하다.
- 3. 본 연구는 고해상도 재분석 데이터를 학습한 스코어 기반 확산 모델을 활용하여 지역 날씨 동역학의 통계적 특성을 포착하는 새로운 생성 프레임워크를 제시한다.
- 4. 확산 모델의 확률적 특성을 활용하여 여러 경로를 샘플링하며, 이는 본질적으로 불확실한 예측 작업에 적합하다.
- 5. 제안된 모델은 전 지구적 기후 출력과 일치하는 시공간적으로 일관된 날씨 동역학을 생성함을 입증하였다.


---

*Generated on 2025-09-24 15:21:59*