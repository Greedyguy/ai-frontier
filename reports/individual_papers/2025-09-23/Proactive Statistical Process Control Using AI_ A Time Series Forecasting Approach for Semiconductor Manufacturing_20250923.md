---
keywords:
  - Statistical Process Control
  - Time Series Forecasting
  - Facebook Prophet
  - Semiconductor Manufacturing
  - Machine Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16431
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:49:08.800568",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Statistical Process Control",
    "Time Series Forecasting",
    "Facebook Prophet",
    "Semiconductor Manufacturing",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Statistical Process Control": 0.8,
    "Time Series Forecasting": 0.75,
    "Facebook Prophet": 0.78,
    "Semiconductor Manufacturing": 0.72,
    "Machine Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Statistical Process Control",
        "canonical": "Statistical Process Control",
        "aliases": [
          "SPC"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's approach, linking traditional SPC with AI enhances connectivity.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Time Series Forecasting",
        "canonical": "Time Series Forecasting",
        "aliases": [
          "Time-Series Prediction"
        ],
        "category": "broad_technical",
        "rationale": "Key method used in the paper, relevant for linking with other forecasting techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Facebook Prophet",
        "canonical": "Facebook Prophet",
        "aliases": [
          "Prophet"
        ],
        "category": "unique_technical",
        "rationale": "Specific tool used for forecasting, providing a direct link to similar AI tools.",
        "novelty_score": 0.6,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semiconductor Manufacturing",
        "canonical": "Semiconductor Manufacturing",
        "aliases": [
          "Chip Production"
        ],
        "category": "unique_technical",
        "rationale": "Specific application domain, useful for linking with industry-specific studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.72
      },
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Broad technical category that connects with a wide range of AI-related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "manufacturing industry",
      "process control"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Statistical Process Control",
      "resolved_canonical": "Statistical Process Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Time Series Forecasting",
      "resolved_canonical": "Time Series Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Facebook Prophet",
      "resolved_canonical": "Facebook Prophet",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semiconductor Manufacturing",
      "resolved_canonical": "Semiconductor Manufacturing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Proactive Statistical Process Control Using AI: A Time Series Forecasting Approach for Semiconductor Manufacturing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16431.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16431](https://arxiv.org/abs/2509.16431)

## 🔗 유사한 논문
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (82.8% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (79.7% similar)
- [[2025-09-22/A Comparative Study of Rule-Based and Data-Driven Approaches in Industrial Monitoring_20250922|A Comparative Study of Rule-Based and Data-Driven Approaches in Industrial Monitoring]] (79.3% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (78.7% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Time Series Forecasting|Time Series Forecasting]], [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Statistical Process Control|Statistical Process Control]], [[keywords/Facebook Prophet|Facebook Prophet]], [[keywords/Semiconductor Manufacturing|Semiconductor Manufacturing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16431v1 Announce Type: new 
Abstract: In the manufacturing industry, it is very important to keep machines and processes running smoothly and without unexpected problems. One of the most common tools used to check if everything is working properly is called Statistical Process Control (SPC). Traditional SPC methods work by checking whether recent measurements are within acceptable limits. However, they only react after a problem has already occurred. This can lead to wasted materials, machine downtime, and increased costs. In this paper, we present a smarter way to use SPC. Instead of just reacting to issues after they happen, our system can predict future problems before they occur. We use a machine learning tool called Facebook Prophet, which is designed to work with time-series data (data that changes over time). Prophet looks at past data and forecasts what the next value will be. Then, we use SPC rules to decide if the predicted value is in a Safe zone (no problem), a Warning zone (needs attention), or a Critical zone (may require shutting down the process). We applied this system to real data from a semiconductor manufacturing company. One of the challenges with this data is that the measurements are not taken at regular time intervals. This makes it harder to predict future values accurately. Despite this, our model was able to make strong predictions and correctly classify the risk level of future measurements. The main benefit of our system is that it gives engineers and technicians a chance to act early - before something goes wrong. This helps reduce unexpected failures and improves the overall stability and reliability of the production process. By combining machine learning with traditional SPC, we make quality control more proactive, accurate, and useful for modern industry.

## 📝 요약

이 논문은 제조업에서 기계와 공정의 원활한 운영을 위해 기존의 통계적 공정 관리(SPC)를 개선한 방법을 제안합니다. 기존 SPC는 문제 발생 후에만 반응하지만, 본 연구는 페이스북 Prophet이라는 머신러닝 도구를 활용해 미래의 문제를 예측합니다. Prophet은 시계열 데이터를 분석하여 미래 값을 예측하고, 이를 SPC 규칙에 따라 안전, 경고, 위기 구역으로 분류합니다. 반도체 제조업체의 불규칙한 데이터에 적용한 결과, 예측 정확도가 높았으며, 문제 발생 전 사전 대응이 가능해져 생산 공정의 안정성과 신뢰성을 향상시켰습니다. 머신러닝과 SPC의 결합으로 품질 관리가 더욱 능동적이고 정확해졌습니다.

## 🎯 주요 포인트

- 1. 전통적인 통계적 공정 관리(SPC)는 문제가 발생한 후에만 반응하여 자재 낭비와 기계 가동 중단을 초래할 수 있다.
- 2. 본 논문에서는 Facebook Prophet을 활용하여 미래의 문제를 예측하는 스마트한 SPC 시스템을 제안한다.
- 3. 제안된 시스템은 반도체 제조업체의 실제 데이터를 통해 예측 정확성과 위험 수준 분류의 효과를 입증했다.
- 4. 불규칙한 시간 간격으로 측정된 데이터에서도 강력한 예측 성능을 보여주었다.
- 5. 이 시스템은 엔지니어와 기술자에게 사전 대응 기회를 제공하여 생산 공정의 안정성과 신뢰성을 향상시킨다.


---

*Generated on 2025-09-23 22:49:08*