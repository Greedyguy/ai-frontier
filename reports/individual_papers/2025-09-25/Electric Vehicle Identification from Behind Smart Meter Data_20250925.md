---
keywords:
  - Electric Vehicle Charging Detection
  - Smart Meter Data
  - Temporal Convolutional Network
  - Anomaly Detection
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19316
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:50:23.247152",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Electric Vehicle Charging Detection",
    "Smart Meter Data",
    "Temporal Convolutional Network",
    "Anomaly Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Electric Vehicle Charging Detection": 0.85,
    "Smart Meter Data": 0.9,
    "Temporal Convolutional Network": 0.8,
    "Anomaly Detection": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Electric Vehicle Charging Load Identification",
        "canonical": "Electric Vehicle Charging Detection",
        "aliases": [
          "EV Charging Load Detection",
          "EV Load Identification"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and connects to energy management and smart grid topics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Smart Meter Data",
        "canonical": "Smart Meter Data",
        "aliases": [
          "Smart Meter Readings",
          "Meter Data"
        ],
        "category": "specific_connectable",
        "rationale": "Smart meter data is a key element in energy management and smart grid systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Deep Temporal Convolution Encoding Decoding Network",
        "canonical": "Temporal Convolutional Network",
        "aliases": [
          "TAE Network",
          "Temporal AE"
        ],
        "category": "broad_technical",
        "rationale": "This network type is relevant to deep learning and time-series analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Anomaly Detection Technique",
        "canonical": "Anomaly Detection",
        "aliases": [
          "Outlier Detection"
        ],
        "category": "specific_connectable",
        "rationale": "Anomaly detection is a widely applicable technique in unsupervised learning and data analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "energy distributors",
      "Distribution Network Operators",
      "Victorian households"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Electric Vehicle Charging Load Identification",
      "resolved_canonical": "Electric Vehicle Charging Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Smart Meter Data",
      "resolved_canonical": "Smart Meter Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Deep Temporal Convolution Encoding Decoding Network",
      "resolved_canonical": "Temporal Convolutional Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Anomaly Detection Technique",
      "resolved_canonical": "Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Electric Vehicle Identification from Behind Smart Meter Data

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19316.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19316](https://arxiv.org/abs/2509.19316)

## 🔗 유사한 논문
- [[2025-09-23/Time Series Forecasting Using a Hybrid Deep Learning Method_ A Bi-LSTM Embedding Denoising Auto Encoder Transformer_20250923|Time Series Forecasting Using a Hybrid Deep Learning Method: A Bi-LSTM Embedding Denoising Auto Encoder Transformer]] (83.3% similar)
- [[2025-09-18/VEGA_ Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization_20250918|VEGA: Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization]] (79.9% similar)
- [[2025-09-24/Anomaly Detection in Electric Vehicle Charging Stations Using Federated Learning_20250924|Anomaly Detection in Electric Vehicle Charging Stations Using Federated Learning]] (79.4% similar)
- [[2025-09-23/Ultra-short-term solar power forecasting by deep learning and data reconstruction_20250923|Ultra-short-term solar power forecasting by deep learning and data reconstruction]] (79.2% similar)
- [[2025-09-23/SeqBattNet_ A Discrete-State Physics-Informed Neural Network with Aging Adaptation for Battery Modeling_20250923|SeqBattNet: A Discrete-State Physics-Informed Neural Network with Aging Adaptation for Battery Modeling]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Temporal Convolutional Network|Temporal Convolutional Network]]
**🔗 Specific Connectable**: [[keywords/Smart Meter Data|Smart Meter Data]], [[keywords/Anomaly Detection|Anomaly Detection]]
**⚡ Unique Technical**: [[keywords/Electric Vehicle Charging Detection|Electric Vehicle Charging Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19316v1 Announce Type: cross 
Abstract: Electric vehicle (EV) charging loads identification from behind smart meter recordings is an indispensable aspect that enables effective decision-making for energy distributors to reach an informed and intelligent decision about the power grid's reliability. When EV charging happens behind the meter (BTM), the charging occurs on the customer side of the meter, which measures the overall electricity consumption. In other words, the charging of the EV is considered part of the customer's load and not separately measured by the Distribution Network Operators (DNOs). DNOs require complete knowledge about the EV presence in their network. Identifying the EV charging demand is essential to better plan and manage the distribution grid. Unlike supervised methods, this paper addresses the problem of EV charging load identification in a non-nonintrusive manner from low-frequency smart meter using an unsupervised learning approach based on anomaly detection technique. Our approach does not require prior knowledge of EV charging profiles. It only requires real power consumption data of non-EV users, which are abundant in practice. We propose a deep temporal convolution encoding decoding (TAE) network. The TAE is applied to power consumption from smart BTM from Victorian households in Australia, and the TAE shows superior performance in identifying households with EVs.

## 📝 요약

이 논문은 스마트 미터 기록에서 전기차(EV) 충전 부하를 식별하는 방법을 제안합니다. 이는 에너지 배급자들이 전력망의 신뢰성을 판단하는 데 필수적입니다. 기존의 감독 학습 방법과 달리, 이 연구는 비침입적 방식으로 저주파 스마트 미터 데이터를 활용하여 비지도 학습 기반의 이상 탐지 기법을 사용합니다. 제안된 심층 시계열 컨볼루션 인코딩 디코딩(TAE) 네트워크는 EV 충전 프로필에 대한 사전 지식 없이도 비EV 사용자들의 실제 전력 소비 데이터를 활용하여 EV 충전 수요를 효과적으로 식별합니다. 호주의 빅토리아 가정의 데이터를 통해 TAE 네트워크는 EV를 보유한 가정을 정확히 식별하는 데 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 스마트 미터 기록에서 전기차(EV) 충전 부하 식별은 전력망의 신뢰성을 위한 에너지 배급자의 효과적인 의사결정에 필수적입니다.
- 2. EV 충전은 고객 측에서 이루어지며, 배전 네트워크 운영자(DNO)에 의해 별도로 측정되지 않습니다.
- 3. 이 논문은 비감독 학습 접근법을 사용하여 저주파 스마트 미터에서 비침입적으로 EV 충전 부하를 식별하는 문제를 다룹니다.
- 4. 제안된 심층 시계열 컨볼루션 인코딩 디코딩(TAE) 네트워크는 EV 사용자가 아닌 실제 전력 소비 데이터만 필요로 합니다.
- 5. TAE 네트워크는 호주 빅토리아 가정의 스마트 BTM 전력 소비에 적용되어 EV가 있는 가정을 식별하는 데 우수한 성능을 보였습니다.


---

*Generated on 2025-09-25 16:50:23*