<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:53:52.760711",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Time-Series Generation",
    "Distributional Bias",
    "Hierarchical Denoising Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Time-Series Generation": 0.79,
    "Distributional Bias": 0.75,
    "Hierarchical Denoising Mechanism": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion Process",
          "Diffusion Framework"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are central to the paper's methodology and are widely applicable across various domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Time-Series Generation",
        "canonical": "Time-Series Generation",
        "aliases": [
          "Time-Series Synthesis",
          "Time-Series Modeling"
        ],
        "category": "specific_connectable",
        "rationale": "The focus on generating time-series data is a specific application that connects to various modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Distributional Bias",
        "canonical": "Distributional Bias",
        "aliases": [
          "Data Bias",
          "Bias in Data"
        ],
        "category": "unique_technical",
        "rationale": "Addressing distributional bias is crucial for improving model accuracy and fairness in generated data.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Hierarchical Denoising Mechanism",
        "canonical": "Hierarchical Denoising Mechanism",
        "aliases": [
          "THD",
          "Hierarchical Denoising"
        ],
        "category": "unique_technical",
        "rationale": "This mechanism is a novel aspect of the proposed model, enhancing interpretability and reducing bias.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "model biases",
      "inference process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Time-Series Generation",
      "resolved_canonical": "Time-Series Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Distributional Bias",
      "resolved_canonical": "Distributional Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Hierarchical Denoising Mechanism",
      "resolved_canonical": "Hierarchical Denoising Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DS-Diffusion: Data Style-Guided Diffusion Model for Time-Series Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18584.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18584](https://arxiv.org/abs/2509.18584)

## 🔗 유사한 논문
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (84.3% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (83.5% similar)
- [[2025-09-23/Extract and Diffuse_ Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement_20250923|Extract and Diffuse: Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement]] (83.3% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (83.3% similar)
- [[2025-09-23/Absorb and Converge_ Provable Convergence Guarantee for Absorbing Discrete Diffusion Models_20250923|Absorb and Converge: Provable Convergence Guarantee for Absorbing Discrete Diffusion Models]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Time-Series Generation|Time-Series Generation]]
**⚡ Unique Technical**: [[keywords/Distributional Bias|Distributional Bias]], [[keywords/Hierarchical Denoising Mechanism|Hierarchical Denoising Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18584v1 Announce Type: new 
Abstract: Diffusion models are the mainstream approach for time series generation tasks. However, existing diffusion models for time series generation require retraining the entire framework to introduce specific conditional guidance. There also exists a certain degree of distributional bias between the generated data and the real data, which leads to potential model biases in downstream tasks. Additionally, the complexity of diffusion models and the latent spaces leads to an uninterpretable inference process. To address these issues, we propose the data style-guided diffusion model (DS-Diffusion). In the DS-Diffusion, a diffusion framework based on style-guided kernels is developed to avoid retraining for specific conditions. The time-information based hierarchical denoising mechanism (THD) is developed to reduce the distributional bias between the generated data and the real data. Furthermore, the generated samples can clearly indicate the data style from which they originate. We conduct comprehensive evaluations using multiple public datasets to validate our approach. Experimental results show that, compared to the state-of-the-art model such as ImagenTime, the predictive score and the discriminative score decrease by 5.56% and 61.55%, respectively. The distributional bias between the generated data and the real data is further reduced, the inference process is also more interpretable. Moreover, by eliminating the need to retrain the diffusion model, the flexibility and adaptability of the model to specific conditions are also enhanced.

## 📝 요약

이 논문에서는 시계열 생성 작업을 위한 새로운 접근법인 데이터 스타일 유도 확산 모델(DS-Diffusion)을 제안합니다. 기존 확산 모델의 재훈련 필요성과 생성 데이터와 실제 데이터 간의 분포 편향 문제를 해결하기 위해 스타일 유도 커널 기반의 확산 프레임워크와 시간 정보 기반의 계층적 디노이징 메커니즘(THD)을 도입했습니다. 이를 통해 생성된 샘플이 원래 데이터 스타일을 명확히 나타낼 수 있습니다. 여러 공공 데이터셋을 사용한 실험 결과, DS-Diffusion은 기존 최첨단 모델인 ImagenTime에 비해 예측 점수와 판별 점수가 각각 5.56%와 61.55% 감소했으며, 분포 편향이 줄어들고 추론 과정이 더 해석 가능해졌습니다. 또한, 모델 재훈련이 필요 없어 특정 조건에 대한 유연성과 적응성이 향상되었습니다.

## 🎯 주요 포인트

- 1. 기존 시계열 생성 확산 모델은 특정 조건 도입 시 재훈련이 필요하지만, DS-Diffusion은 스타일-가이드 커널을 통해 이를 피할 수 있습니다.
- 2. DS-Diffusion은 시간 정보 기반 계층적 디노이징 메커니즘(THD)을 통해 생성 데이터와 실제 데이터 간의 분포 편향을 줄입니다.
- 3. DS-Diffusion은 생성된 샘플이 기원한 데이터 스타일을 명확히 나타낼 수 있습니다.
- 4. 실험 결과, DS-Diffusion은 ImagenTime 등 최신 모델 대비 예측 점수와 판별 점수가 각각 5.56%, 61.55% 감소했습니다.
- 5. DS-Diffusion은 재훈련 없이도 특정 조건에 대한 모델의 유연성과 적응성을 향상시킵니다.


---

*Generated on 2025-09-24 14:53:52*