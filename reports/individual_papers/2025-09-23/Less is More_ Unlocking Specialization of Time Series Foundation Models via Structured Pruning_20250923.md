---
keywords:
  - Time Series Foundation Models
  - structured pruning
  - Zero-Shot Learning
  - fine-tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.23195
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:03:39.520660",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Time Series Foundation Models",
    "structured pruning",
    "Zero-Shot Learning",
    "fine-tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Time Series Foundation Models": 0.78,
    "structured pruning": 0.77,
    "Zero-Shot Learning": 0.8,
    "fine-tuning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Time Series Foundation Models",
        "canonical": "Time Series Foundation Models",
        "aliases": [
          "TSFMs"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a specialized model type, enhancing specificity in time series forecasting discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "structured pruning",
        "canonical": "structured pruning",
        "aliases": [
          "prune-then-finetune"
        ],
        "category": "unique_technical",
        "rationale": "Structured pruning is a novel approach in the paper, crucial for optimizing model performance, thus offering a unique link opportunity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "zero-shot forecasting",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot forecasting is a specific application of zero-shot learning, linking to broader discussions on model generalization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "fine-tuning",
        "canonical": "fine-tuning",
        "aliases": [
          "model adaptation"
        ],
        "category": "broad_technical",
        "rationale": "Fine-tuning is a widely applicable concept in machine learning, crucial for adapting pre-trained models to specific tasks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "forecasting performance",
      "empirical studies",
      "source code"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Time Series Foundation Models",
      "resolved_canonical": "Time Series Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "structured pruning",
      "resolved_canonical": "structured pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "zero-shot forecasting",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "fine-tuning",
      "resolved_canonical": "fine-tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23195.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.23195](https://arxiv.org/abs/2505.23195)

## 🔗 유사한 논문
- [[2025-09-17/TFMAdapter_ Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates_20250917|TFMAdapter: Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates]] (85.5% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (81.8% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (81.8% similar)
- [[2025-09-22/Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting_20250922|Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting]] (81.7% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/fine-tuning|fine-tuning]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Time Series Foundation Models|Time Series Foundation Models]], [[keywords/structured pruning|structured pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23195v2 Announce Type: replace-cross 
Abstract: Scaling laws motivate the development of Time Series Foundation Models (TSFMs) that pre-train vast parameters and achieve remarkable zero-shot forecasting performance. Surprisingly, even after fine-tuning, TSFMs cannot consistently outperform smaller, specialized models trained on full-shot downstream data. A key question is how to realize effective adaptation of TSFMs for a target forecasting task. Through empirical studies on various TSFMs, the pre-trained models often exhibit inherent sparsity and redundancy in computation, suggesting that TSFMs have learned to activate task-relevant network substructures to accommodate diverse forecasting tasks. To preserve this valuable prior knowledge, we propose a structured pruning method to regularize the subsequent fine-tuning process by focusing it on a more relevant and compact parameter space. Extensive experiments on seven TSFMs and six benchmarks demonstrate that fine-tuning a smaller, pruned TSFM significantly improves forecasting performance compared to fine-tuning original models. This prune-then-finetune paradigm often enables TSFMs to achieve state-of-the-art performance and surpass strong specialized baselines. Source code is made publicly available at https://github.com/SJTU-DMTai/Prune-then-Finetune.

## 📝 요약

이 논문은 대규모 파라미터를 사전 학습하여 뛰어난 예측 성능을 보이는 시계열 기초 모델(TSFM)의 효과적인 적응 방법을 제안합니다. 연구 결과, TSFM은 내재된 계산의 희소성과 중복성을 보여주며, 다양한 예측 작업에 적합한 네트워크 하위 구조를 활성화하는 능력을 학습한 것으로 나타났습니다. 이를 바탕으로, 사전 학습된 모델의 유용한 사전 지식을 보존하기 위해 구조적 가지치기 방법을 제안하여, 후속 미세 조정 과정을 더 관련성 있고 압축된 파라미터 공간에 집중시킵니다. 7개의 TSFM과 6개의 벤치마크를 대상으로 한 실험에서, 가지치기 후 미세 조정된 TSFM이 원래 모델보다 예측 성능이 크게 향상됨을 확인했습니다. 제안된 방법은 TSFM이 최첨단 성능을 달성하고 강력한 특화 모델을 능가하도록 합니다. 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. TSFMs는 대규모 매개변수를 사전 학습하여 뛰어난 제로샷 예측 성능을 달성하지만, 세밀한 조정 후에도 전문화된 소형 모델을 일관되게 능가하지 못함.
- 2. TSFMs의 효과적인 적응을 위해, 사전 학습된 모델들이 다양한 예측 작업에 적합한 네트워크 하위 구조를 활성화하는 능력을 학습했음을 발견.
- 3. 기존의 사전 지식을 보존하기 위해, 구조적 가지치기 방법을 제안하여 보다 관련성 있고 압축된 매개변수 공간에 초점을 맞춰 세밀한 조정 과정을 규제.
- 4. 7개의 TSFMs와 6개의 벤치마크에 대한 실험 결과, 가지치기 후 세밀한 조정된 TSFM이 원래 모델을 조정한 것보다 예측 성능을 크게 향상시킴.
- 5. 제안된 가지치기 후 세밀 조정 패러다임은 TSFMs가 최첨단 성능을 달성하고 강력한 전문화된 기준선을 능가할 수 있도록 함.


---

*Generated on 2025-09-24 01:03:39*