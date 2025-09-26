---
keywords:
  - Transformer
  - Irregular Multivariate Time Series
  - Token Mixing
  - Attention Mechanism
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17809
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:57:23.513126",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Irregular Multivariate Time Series",
    "Token Mixing",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Irregular Multivariate Time Series": 0.8,
    "Token Mixing": 0.78,
    "Attention Mechanism": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, relevant for understanding the MTM architecture.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Irregular Multivariate Time Series",
        "canonical": "Irregular Multivariate Time Series",
        "aliases": [
          "IMTS"
        ],
        "category": "unique_technical",
        "rationale": "IMTS is a specific problem domain addressed by the MTM model, crucial for understanding its application.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Token Mixing",
        "canonical": "Token Mixing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Token Mixing is a novel mechanism in MTM that enhances channel-wise learning, central to the paper's contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are integral to the MTM model's ability to handle channel-wise asynchrony.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "classification",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Irregular Multivariate Time Series",
      "resolved_canonical": "Irregular Multivariate Time Series",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Token Mixing",
      "resolved_canonical": "Token Mixing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17809.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17809](https://arxiv.org/abs/2509.17809)

## 🔗 유사한 논문
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (84.5% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (82.8% similar)
- [[2025-09-22/MTS-DMAE_ Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning_20250922|MTS-DMAE: Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning]] (82.8% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.0% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Irregular Multivariate Time Series|Irregular Multivariate Time Series]], [[keywords/Token Mixing|Token Mixing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17809v1 Announce Type: new 
Abstract: Irregular multivariate time series (IMTS) is characterized by the lack of synchronized observations across its different channels. In this paper, we point out that this channel-wise asynchrony can lead to poor channel-wise modeling of existing deep learning methods. To overcome this limitation, we propose MTM, a multi-scale token mixing transformer for the classification of IMTS. We find that the channel-wise asynchrony can be alleviated by down-sampling the time series to coarser timescales, and propose to incorporate a masked concat pooling in MTM that gradually down-samples IMTS to enhance the channel-wise attention modules. Meanwhile, we propose a novel channel-wise token mixing mechanism which proactively chooses important tokens from one channel and mixes them with other channels, to further boost the channel-wise learning of our model. Through extensive experiments on real-world datasets and comparison with state-of-the-art methods, we demonstrate that MTM consistently achieves the best performance on all the benchmarks, with improvements of up to 3.8% in AUPRC for classification.

## 📝 요약

이 논문에서는 비동기적인 관측으로 특징지어지는 불규칙 다변량 시계열(IMTS)의 문제를 해결하기 위해 MTM이라는 다중 스케일 토큰 믹싱 트랜스포머를 제안합니다. 기존 딥러닝 방법의 채널별 모델링 한계를 극복하기 위해, 시계열을 더 거친 시간 척도로 다운샘플링하고, 마스킹된 컨캣 풀링을 도입하여 채널별 주의 모듈을 강화합니다. 또한, 새로운 채널별 토큰 믹싱 메커니즘을 통해 한 채널의 중요한 토큰을 다른 채널과 혼합하여 학습 성능을 향상시킵니다. 실제 데이터셋과의 비교 실험에서 MTM은 모든 벤치마크에서 최고 성능을 기록하며, AUPRC 기준 최대 3.8%의 성능 향상을 보여줍니다.

## 🎯 주요 포인트

- 1. 불규칙 다변량 시계열(IMTS)은 채널 간 비동기화된 관측으로 인해 기존 딥러닝 방법의 채널별 모델링 성능이 저하될 수 있다.
- 2. MTM은 IMTS 분류를 위한 다중 스케일 토큰 믹싱 트랜스포머로, 채널별 비동기화를 완화하기 위해 시계열을 더 거친 시간 척도로 다운샘플링한다.
- 3. MTM은 마스크드 콘캣 풀링을 도입하여 IMTS를 점진적으로 다운샘플링하고 채널별 주의 모듈을 강화한다.
- 4. 새로운 채널별 토큰 믹싱 메커니즘을 통해 한 채널에서 중요한 토큰을 선택하고 다른 채널과 혼합하여 채널별 학습을 향상시킨다.
- 5. 실제 데이터셋과의 광범위한 실험을 통해 MTM이 모든 벤치마크에서 일관되게 최고 성능을 달성하며, AUPRC 기준으로 최대 3.8%의 성능 향상을 보였다.


---

*Generated on 2025-09-24 01:57:23*