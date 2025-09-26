---
keywords:
  - Temporal Dependency Alignment
  - Long-term Time Series Forecasting
  - Temporal Dependencies
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2406.04777
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:00:56.429819",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Temporal Dependency Alignment",
    "Long-term Time Series Forecasting",
    "Temporal Dependencies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Temporal Dependency Alignment": 0.88,
    "Long-term Time Series Forecasting": 0.85,
    "Temporal Dependencies": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Temporal Dependency Alignment",
        "canonical": "Temporal Dependency Alignment",
        "aliases": [
          "TDAlign"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework specifically designed to enhance LTSF methods by aligning temporal dependencies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Long-term Time Series Forecasting",
        "canonical": "Long-term Time Series Forecasting",
        "aliases": [
          "LTSF"
        ],
        "category": "specific_connectable",
        "rationale": "A critical task in various domains, providing a strong link to time series analysis and forecasting research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Temporal Dependencies within the Target",
        "canonical": "Temporal Dependencies",
        "aliases": [
          "TDT"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's contribution, focusing on improving prediction accuracy by modeling temporal dependencies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.83
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
      "candidate_surface": "Temporal Dependency Alignment",
      "resolved_canonical": "Temporal Dependency Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Long-term Time Series Forecasting",
      "resolved_canonical": "Long-term Time Series Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Temporal Dependencies within the Target",
      "resolved_canonical": "Temporal Dependencies",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting

**Korean Title:** 타겟 내의 시간적 종속성을 모델링하여 장기 시계열 예측 수행

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2406.04777.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2406.04777](https://arxiv.org/abs/2406.04777)

## 🔗 유사한 논문
- [[2025-09-17/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting]] (87.1% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.0% similar)
- [[2025-09-22/Deep Learning Foundation and Pattern Models_ Challenges in Hydrological Time Series_20250922|Deep Learning Foundation and Pattern Models: Challenges in Hydrological Time Series]] (81.5% similar)
- [[2025-09-18/Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear: A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (81.2% similar)
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Long-term Time Series Forecasting|Long-term Time Series Forecasting]], [[keywords/Temporal Dependencies|Temporal Dependencies]]
**⚡ Unique Technical**: [[keywords/Temporal Dependency Alignment|Temporal Dependency Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.04777v3 Announce Type: replace 
Abstract: Long-term time series forecasting (LTSF) is a critical task across diverse domains. Despite significant advancements in LTSF research, we identify a performance bottleneck in existing LTSF methods caused by the inadequate modeling of Temporal Dependencies within the Target (TDT). To address this issue, we propose a novel and generic temporal modeling framework, Temporal Dependency Alignment (TDAlign), that equips existing LTSF methods with TDT learning capabilities. TDAlign introduces two key innovations: 1) a loss function that aligns the change values between adjacent time steps in the predictions with those in the target, ensuring consistency with variation patterns, and 2) an adaptive loss balancing strategy that seamlessly integrates the new loss function with existing LTSF methods without introducing additional learnable parameters. As a plug-and-play framework, TDAlign enhances existing methods with minimal computational overhead, featuring only linear time complexity and constant space complexity relative to the prediction length. Extensive experiments on six strong LTSF baselines across seven real-world datasets demonstrate the effectiveness and flexibility of TDAlign. On average, TDAlign reduces baseline prediction errors by \textbf{1.47\%} to \textbf{9.19\%} and change value errors by \textbf{4.57\%} to \textbf{15.78\%}, highlighting its substantial performance improvements.

## 🔍 Abstract (한글 번역)

arXiv:2406.04777v3 발표 유형: 교체  
초록: 장기 시계열 예측(LTSF)은 다양한 분야에서 중요한 과제입니다. LTSF 연구에서 상당한 발전이 있었음에도 불구하고, 기존 LTSF 방법에서 목표 내의 시간적 종속성(TDT)을 적절히 모델링하지 못해 성능 병목 현상이 발생하는 것을 확인했습니다. 이 문제를 해결하기 위해, 우리는 기존 LTSF 방법에 TDT 학습 기능을 제공하는 새로운 일반적 시간 모델링 프레임워크인 Temporal Dependency Alignment (TDAlign)을 제안합니다. TDAlign은 두 가지 주요 혁신을 도입합니다: 1) 예측에서 인접한 시간 단계 간의 변화 값을 목표의 변화 값과 일치시키는 손실 함수를 통해 변동 패턴과의 일관성을 보장하고, 2) 새로운 손실 함수를 기존 LTSF 방법과 추가 학습 가능한 매개변수 없이 매끄럽게 통합하는 적응적 손실 균형 전략입니다. 플러그 앤 플레이 프레임워크로서, TDAlign은 예측 길이에 비례하는 선형 시간 복잡도와 상수 공간 복잡도만을 특징으로 하며 최소한의 계산 오버헤드로 기존 방법을 향상시킵니다. 7개의 실제 데이터셋에 걸쳐 6개의 강력한 LTSF 기준선에서의 광범위한 실험은 TDAlign의 효과성과 유연성을 입증합니다. 평균적으로, TDAlign은 기준선 예측 오류를 \textbf{1.47\%}에서 \textbf{9.19\%}까지, 변화 값 오류를 \textbf{4.57\%}에서 \textbf{15.78\%}까지 감소시켜 상당한 성능 향상을 강조합니다.

## 📝 요약

장기 시계열 예측(LTSF)의 성능 병목 현상을 해결하기 위해 Temporal Dependency Alignment(TDAlign)이라는 새로운 프레임워크를 제안합니다. TDAlign은 예측과 목표 간의 변화 값을 일치시키는 손실 함수와 기존 방법에 추가 매개변수 없이 통합할 수 있는 적응형 손실 균형 전략을 도입합니다. 이 프레임워크는 최소한의 계산 비용으로 기존 LTSF 방법을 강화하며, 7개의 실제 데이터셋에서 평균적으로 예측 오류를 1.47%에서 9.19%까지, 변화 값 오류를 4.57%에서 15.78%까지 감소시켰습니다.

## 🎯 주요 포인트

- 1. 장기 시계열 예측(LTSF)에서 기존 방법의 성능 병목 현상은 목표 내 시간 의존성(TDT) 모델링의 부족으로 인한 것이다.
- 2. TDAlign은 기존 LTSF 방법에 TDT 학습 기능을 제공하는 새로운 시간 모델링 프레임워크로 제안되었다.
- 3. TDAlign은 예측의 변화 값을 목표의 변화 패턴과 일치시키는 손실 함수와 적응형 손실 균형 전략을 도입한다.
- 4. TDAlign은 최소한의 계산 오버헤드로 기존 방법을 강화하며, 선형 시간 복잡도와 상수 공간 복잡도를 특징으로 한다.
- 5. 7개의 실제 데이터셋에서 6개의 강력한 LTSF 기반을 대상으로 한 실험에서 TDAlign은 평균적으로 예측 오류를 1.47%에서 9.19%까지, 변화 값 오류를 4.57%에서 15.78%까지 감소시켰다.


---

*Generated on 2025-09-23 11:00:56*