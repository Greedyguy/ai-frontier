---
keywords:
  - Cross-Frequency Transfer Learning
  - Foundation Forecasting Models
  - Neural Network
  - Synthetic Dataset Pre-training
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19465
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:36:30.202173",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cross-Frequency Transfer Learning",
    "Foundation Forecasting Models",
    "Neural Network",
    "Synthetic Dataset Pre-training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cross-Frequency Transfer Learning": 0.78,
    "Foundation Forecasting Models": 0.77,
    "Neural Network": 0.7,
    "Synthetic Dataset Pre-training": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cross-Frequency Transfer Learning",
        "canonical": "Cross-Frequency Transfer Learning",
        "aliases": [
          "CFTL"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's methodology, offering a unique perspective on transfer learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Foundation Forecasting Models",
        "canonical": "Foundation Forecasting Models",
        "aliases": [
          "FFMs"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving these models, making them a key concept for linking related research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Neural Forecasting Networks",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Forecasting Models"
        ],
        "category": "broad_technical",
        "rationale": "These networks are adapted for the CFTL setup, linking to broader neural network research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Synthetic Dataset Pre-training",
        "canonical": "Synthetic Dataset Pre-training",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is shown to improve model accuracy, making it a valuable link to data preparation strategies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.73,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmarking practices",
      "summary statistics",
      "test leakage"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cross-Frequency Transfer Learning",
      "resolved_canonical": "Cross-Frequency Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Foundation Forecasting Models",
      "resolved_canonical": "Foundation Forecasting Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Neural Forecasting Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Synthetic Dataset Pre-training",
      "resolved_canonical": "Synthetic Dataset Pre-training",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.73,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Realistic Evaluation of Cross-Frequency Transfer Learning and Foundation Forecasting Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19465.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19465](https://arxiv.org/abs/2509.19465)

## 🔗 유사한 논문
- [[2025-09-23/Less is More_ Unlocking Specialization of Time Series Foundation Models via Structured Pruning_20250923|Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning]] (83.6% similar)
- [[2025-09-22/Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting_20250922|Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting]] (83.0% similar)
- [[2025-09-17/TFMAdapter_ Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates_20250917|TFMAdapter: Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates]] (82.4% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.4% similar)
- [[2025-09-24/MOMEMTO_ Patch-based Memory Gate Model in Time Series Foundation Model_20250924|MOMEMTO: Patch-based Memory Gate Model in Time Series Foundation Model]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Synthetic Dataset Pre-training|Synthetic Dataset Pre-training]]
**⚡ Unique Technical**: [[keywords/Cross-Frequency Transfer Learning|Cross-Frequency Transfer Learning]], [[keywords/Foundation Forecasting Models|Foundation Forecasting Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19465v1 Announce Type: cross 
Abstract: Cross-frequency transfer learning (CFTL) has emerged as a popular framework for curating large-scale time series datasets to pre-train foundation forecasting models (FFMs). Although CFTL has shown promise, current benchmarking practices fall short of accurately assessing its performance. This shortcoming stems from many factors: an over-reliance on small-scale evaluation datasets; inadequate treatment of sample size when computing summary statistics; reporting of suboptimal statistical models; and failing to account for non-negligible risks of overlap between pre-training and test datasets. To address these limitations, we introduce a unified reimplementation of widely-adopted neural forecasting networks, adapting them for the CFTL setup; we pre-train only on proprietary and synthetic data, being careful to prevent test leakage; and we evaluate on 15 large, diverse public forecast competition datasets. Our empirical analysis reveals that statistical models' accuracy is frequently underreported. Notably, we confirm that statistical models and their ensembles consistently outperform existing FFMs by more than 8.2% in sCRPS, and by more than 20% MASE, across datasets. However, we also find that synthetic dataset pre-training does improve the accuracy of a FFM by 7% percent.

## 📝 요약

이 논문은 대규모 시계열 데이터셋을 활용한 기초 예측 모델(FFM) 사전 학습을 위한 교차 주파수 전이 학습(CFTL)의 성능 평가 문제를 다룹니다. 기존 평가 방식의 한계를 극복하기 위해, 저자들은 널리 사용되는 신경망 예측 모델을 CFTL에 맞게 재구현하고, 사전 학습 시 테스트 데이터 누출을 방지하며, 15개의 대규모 공공 예측 대회 데이터셋에서 평가를 수행했습니다. 그 결과, 통계 모델의 정확도가 자주 과소평가되었으며, 통계 모델과 그 앙상블이 기존 FFM보다 평균적으로 8.2% 이상의 sCRPS와 20% 이상의 MASE에서 우수한 성능을 보였습니다. 또한, 합성 데이터셋을 통한 사전 학습이 FFM의 정확성을 7% 향상시킨다는 사실도 확인했습니다.

## 🎯 주요 포인트

- 1. CFTL은 대규모 시계열 데이터셋을 활용하여 예측 모델을 사전 훈련하는 인기 있는 프레임워크로 부상하고 있다.
- 2. 현재의 벤치마킹 관행은 CFTL의 성능을 정확히 평가하지 못하고 있다.
- 3. 다양한 요인들이 이러한 평가의 한계를 초래하며, 특히 소규모 평가 데이터셋에 대한 과도한 의존과 샘플 크기 처리의 부적절함 등이 문제로 지적된다.
- 4. 연구에서는 CFTL 설정에 맞게 신경망 예측 모델을 통합 재구현하고, 독점적 및 합성 데이터로만 사전 훈련을 수행하여 테스트 누출을 방지하였다.
- 5. 실증 분석 결과, 통계 모델과 그 앙상블이 기존 FFMs보다 sCRPS에서 8.2% 이상, MASE에서 20% 이상 더 우수한 성능을 보였다.


---

*Generated on 2025-09-25 15:36:30*