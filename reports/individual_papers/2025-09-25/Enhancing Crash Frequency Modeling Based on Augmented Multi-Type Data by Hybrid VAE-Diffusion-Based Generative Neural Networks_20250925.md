---
keywords:
  - Hybrid VAE-Diffusion Neural Network
  - Crash Frequency Modeling
  - Synthetic Data
  - Traffic Safety
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2501.10017
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:09:32.220452",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hybrid VAE-Diffusion Neural Network",
    "Crash Frequency Modeling",
    "Synthetic Data",
    "Traffic Safety"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hybrid VAE-Diffusion Neural Network": 0.78,
    "Crash Frequency Modeling": 0.79,
    "Synthetic Data": 0.75,
    "Traffic Safety": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hybrid VAE-Diffusion Neural Network",
        "canonical": "Hybrid VAE-Diffusion Neural Network",
        "aliases": [
          "VAE-Diffusion Model"
        ],
        "category": "unique_technical",
        "rationale": "This model represents a novel approach in crash frequency modeling, enhancing connectivity with research on generative models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Crash Frequency Modeling",
        "canonical": "Crash Frequency Modeling",
        "aliases": [
          "Crash Prediction"
        ],
        "category": "specific_connectable",
        "rationale": "A central theme of the paper, linking to studies on traffic safety and predictive analytics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Synthetic Data",
        "canonical": "Synthetic Data",
        "aliases": [
          "Generated Data"
        ],
        "category": "broad_technical",
        "rationale": "Synthetic data is crucial for improving model predictions and is widely applicable in data augmentation research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Traffic Safety",
        "canonical": "Traffic Safety",
        "aliases": [
          "Road Safety"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area of the research, connecting to policy-making and safety improvement studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Crash Occurrences",
      "Model Accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hybrid VAE-Diffusion Neural Network",
      "resolved_canonical": "Hybrid VAE-Diffusion Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Crash Frequency Modeling",
      "resolved_canonical": "Crash Frequency Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Synthetic Data",
      "resolved_canonical": "Synthetic Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Traffic Safety",
      "resolved_canonical": "Traffic Safety",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Enhancing Crash Frequency Modeling Based on Augmented Multi-Type Data by Hybrid VAE-Diffusion-Based Generative Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.10017.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2501.10017](https://arxiv.org/abs/2501.10017)

## 🔗 유사한 논문
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (85.1% similar)
- [[2025-09-24/Investigating Traffic Accident Detection Using Multimodal Large Language Models_20250924|Investigating Traffic Accident Detection Using Multimodal Large Language Models]] (82.2% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (82.2% similar)
- [[2025-09-17/Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction_20250917|Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (81.6% similar)
- [[2025-09-24/Model-Based Transfer Learning for Real-Time Damage Assessment of Bridge Networks_20250924|Model-Based Transfer Learning for Real-Time Damage Assessment of Bridge Networks]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Synthetic Data|Synthetic Data]]
**🔗 Specific Connectable**: [[keywords/Crash Frequency Modeling|Crash Frequency Modeling]], [[keywords/Traffic Safety|Traffic Safety]]
**⚡ Unique Technical**: [[keywords/Hybrid VAE-Diffusion Neural Network|Hybrid VAE-Diffusion Neural Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.10017v2 Announce Type: replace 
Abstract: Crash frequency modelling analyzes the impact of factors like traffic volume, road geometry, and environmental conditions on crash occurrences. Inaccurate predictions can distort our understanding of these factors, leading to misguided policies and wasted resources, which jeopardize traffic safety. A key challenge in crash frequency modelling is the prevalence of excessive zero observations, caused by underreporting, the low probability of crashes, and high data collection costs. These zero observations often reduce model accuracy and introduce bias, complicating safety decision making. While existing approaches, such as statistical methods, data aggregation, and resampling, attempt to address this issue, they either rely on restrictive assumptions or result in significant information loss, distorting crash data. To overcome these limitations, we propose a hybrid VAE-Diffusion neural network, designed to reduce zero observations and handle the complexities of multi-type tabular crash data (count, ordinal, nominal, and real-valued variables). We assess the synthetic data quality generated by this model through metrics like similarity, accuracy, diversity, and structural consistency, and compare its predictive performance against traditional statistical models. Our findings demonstrate that the hybrid VAE-Diffusion model outperforms baseline models across all metrics, offering a more effective approach to augmenting crash data and improving the accuracy of crash frequency predictions. This study highlights the potential of synthetic data to enhance traffic safety by improving crash frequency modelling and informing better policy decisions.

## 📝 요약

이 논문은 교통사고 빈도 모델링의 정확성을 높이기 위해 하이브리드 VAE-Diffusion 신경망을 제안합니다. 기존 모델은 과도한 0 관측치로 인해 정확도가 떨어지고 편향이 발생하는 문제가 있었습니다. 제안된 모델은 다양한 유형의 사고 데이터(카운트, 서열, 명목, 실수형 변수)를 효과적으로 처리하여 0 관측치를 줄이고, 유사성, 정확성, 다양성, 구조적 일관성 등의 지표에서 기존 통계 모델보다 뛰어난 성능을 보였습니다. 이 연구는 합성 데이터를 활용하여 교통사고 빈도 예측의 정확성을 높이고, 더 나은 정책 결정을 지원할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 교통사고 발생 빈도 모델링에서 과도한 0 관측값이 모델 정확도를 감소시키고 편향을 초래하여 안전 의사결정을 복잡하게 만든다.
- 2. 기존의 통계적 방법, 데이터 집계, 리샘플링은 제한적인 가정에 의존하거나 정보 손실을 초래하여 사고 데이터를 왜곡한다.
- 3. 제안된 하이브리드 VAE-Diffusion 신경망은 다중 유형의 표 형식 사고 데이터를 처리하고 0 관측값을 줄여 모델의 예측 성능을 향상시킨다.
- 4. 하이브리드 VAE-Diffusion 모델은 유사성, 정확성, 다양성, 구조적 일관성 등의 지표에서 기존 통계 모델을 능가한다.
- 5. 본 연구는 합성 데이터가 사고 빈도 모델링을 개선하고 더 나은 정책 결정을 지원하여 교통 안전을 향상시킬 잠재력을 강조한다.


---

*Generated on 2025-09-25 16:09:32*