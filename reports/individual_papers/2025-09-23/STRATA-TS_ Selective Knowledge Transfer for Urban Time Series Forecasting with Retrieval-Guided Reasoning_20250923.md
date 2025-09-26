---
keywords:
  - Selective Knowledge Transfer
  - Large Language Model
  - Retrieval-Guided Reasoning
  - Patch-based Temporal Encoder
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2508.18635
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:50:56.976677",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Selective Knowledge Transfer",
    "Large Language Model",
    "Retrieval-Guided Reasoning",
    "Patch-based Temporal Encoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Selective Knowledge Transfer": 0.85,
    "Large Language Model": 0.8,
    "Retrieval-Guided Reasoning": 0.82,
    "Patch-based Temporal Encoder": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Selective Knowledge Transfer",
        "canonical": "Selective Knowledge Transfer",
        "aliases": [
          "Target-aware Retrieval",
          "Transfer Learning"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology, focusing on improving transfer learning by selectively retrieving relevant data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are crucial for the reasoning process described in the paper, linking it to broader AI advancements.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Retrieval-Guided Reasoning",
        "canonical": "Retrieval-Guided Reasoning",
        "aliases": [
          "Retrieval-Augmented Generation"
        ],
        "category": "specific_connectable",
        "rationale": "This technique enhances the model's reasoning capabilities by integrating retrieval mechanisms, aligning with recent trends in AI.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Patch-based Temporal Encoder",
        "canonical": "Patch-based Temporal Encoder",
        "aliases": [
          "Temporal Encoder"
        ],
        "category": "unique_technical",
        "rationale": "This component is a novel contribution to the model architecture, crucial for aligning source and target data.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "urban forecasting",
      "data imbalance",
      "negative transfer"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Selective Knowledge Transfer",
      "resolved_canonical": "Selective Knowledge Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Retrieval-Guided Reasoning",
      "resolved_canonical": "Retrieval-Guided Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Patch-based Temporal Encoder",
      "resolved_canonical": "Patch-based Temporal Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# STRATA-TS: Selective Knowledge Transfer for Urban Time Series Forecasting with Retrieval-Guided Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.18635.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2508.18635](https://arxiv.org/abs/2508.18635)

## 🔗 유사한 논문
- [[2025-09-17/ST-LINK_ Spatially-Aware Large Language Models for Spatio-Temporal Forecasting_20250917|ST-LINK: Spatially-Aware Large Language Models for Spatio-Temporal Forecasting]] (81.8% similar)
- [[2025-09-17/Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction_20250917|Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (81.6% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (81.4% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.9% similar)
- [[2025-09-22/Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments_20250922|Integrating Spatiotemporal Vision Transformer into Digital Twins for High-Resolution Heat Stress Forecasting in Campus Environments]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval-Guided Reasoning|Retrieval-Guided Reasoning]]
**⚡ Unique Technical**: [[keywords/Selective Knowledge Transfer|Selective Knowledge Transfer]], [[keywords/Patch-based Temporal Encoder|Patch-based Temporal Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.18635v2 Announce Type: replace 
Abstract: Urban forecasting models often face a severe data imbalance problem: only a few cities have dense, long-span records, while many others expose short or incomplete histories. Direct transfer from data-rich to data-scarce cities is unreliable because only a limited subset of source patterns truly benefits the target domain, whereas indiscriminate transfer risks introducing noise and negative transfer. We present STRATA-TS (Selective TRAnsfer via TArget-aware retrieval for Time Series), a framework that combines domain-adapted retrieval with reasoning-capable large models to improve forecasting in scarce data regimes. STRATA-TS employs a patch-based temporal encoder to identify source subsequences that are semantically and dynamically aligned with the target query. These retrieved exemplars are then injected into a retrieval-guided reasoning stage, where an LLM performs structured inference over target inputs and retrieved support. To enable efficient deployment, we distill the reasoning process into a compact open model via supervised fine-tuning. Extensive experiments on three parking availability datasets across Singapore, Nottingham, and Glasgow demonstrate that STRATA-TS consistently outperforms strong forecasting and transfer baselines, while providing interpretable knowledge transfer pathways.

## 📝 요약

이 논문은 도시 예측 모델의 데이터 불균형 문제를 해결하기 위해 STRATA-TS라는 프레임워크를 제안합니다. 많은 도시들이 짧거나 불완전한 데이터 기록을 가지고 있어, 데이터가 풍부한 도시에서 부족한 도시로의 직접적인 전이는 신뢰할 수 없습니다. STRATA-TS는 도메인 적응 검색과 대규모 모델을 결합하여 데이터가 부족한 환경에서 예측 성능을 향상시킵니다. 이 프레임워크는 패치 기반의 시간 인코더를 사용하여 대상 쿼리와 의미적, 동적으로 일치하는 소스 하위 시퀀스를 식별하고, 이를 검색 기반 추론 단계에 주입하여 대규모 언어 모델(LLM)이 구조화된 추론을 수행합니다. 실험 결과, STRATA-TS는 싱가포르, 노팅엄, 글래스고의 주차 가능성 데이터셋에서 기존의 예측 및 전이 모델보다 우수한 성능을 보였으며, 해석 가능한 지식 전이 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 도시 예측 모델은 데이터 불균형 문제에 직면하며, 데이터가 풍부한 도시에서 데이터가 부족한 도시로의 직접 전이는 신뢰할 수 없습니다.
- 2. STRATA-TS는 대상 인식 검색을 통해 시간 시계열 데이터를 선택적으로 전이하여 예측을 개선하는 프레임워크입니다.
- 3. 이 프레임워크는 패치 기반의 시간 인코더를 사용하여 대상 쿼리와 의미적, 동적으로 정렬된 소스 하위 시퀀스를 식별합니다.
- 4. 검색된 예시는 검색 안내 추론 단계에 주입되어 대형 언어 모델(LLM)이 구조화된 추론을 수행합니다.
- 5. STRATA-TS는 싱가포르, 노팅엄, 글래스고의 주차 가능성 데이터셋 실험에서 강력한 예측 및 전이 기준을 지속적으로 능가합니다.


---

*Generated on 2025-09-24 02:50:56*