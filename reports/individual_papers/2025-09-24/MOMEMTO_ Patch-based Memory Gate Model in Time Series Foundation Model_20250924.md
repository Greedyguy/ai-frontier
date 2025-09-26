<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:55:12.057742",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MOMEMTO",
    "Time Series Foundation Model",
    "Attention Mechanism",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MOMEMTO": 0.8,
    "Time Series Foundation Model": 0.75,
    "Attention Mechanism": 0.78,
    "Few-Shot Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MOMEMTO",
        "canonical": "MOMEMTO",
        "aliases": [
          "Patch-based Memory Gate Model"
        ],
        "category": "unique_technical",
        "rationale": "MOMEMTO is a novel model specifically designed for anomaly detection in time series, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Time Series Foundation Model",
        "canonical": "Time Series Foundation Model",
        "aliases": [
          "TFM"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific type of foundation model tailored for time series data, offering a unique perspective in the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial in organizing and updating memory items, linking to broader neural network concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Few-Shot Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Few-shot learning scenarios are highlighted in the paper, providing a connection to current trends in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "reconstruction-based deep models",
      "training costs",
      "baseline methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MOMEMTO",
      "resolved_canonical": "MOMEMTO",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Time Series Foundation Model",
      "resolved_canonical": "Time Series Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
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
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Few-Shot Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MOMEMTO: Patch-based Memory Gate Model in Time Series Foundation Model

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18751.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18751](https://arxiv.org/abs/2509.18751)

## 🔗 유사한 논문
- [[2025-09-23/Less is More_ Unlocking Specialization of Time Series Foundation Models via Structured Pruning_20250923|Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning]] (84.1% similar)
- [[2025-09-22/Two Facets of the Same Optimization Coin_ Model Degradation and Representation Collapse in Graph Foundation Models_20250922|Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models]] (83.2% similar)
- [[2025-09-23/MTM_ A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification_20250923|MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification]] (83.0% similar)
- [[2025-09-18/Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (83.0% similar)
- [[2025-09-24/AdaMixT_ Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting_20250924|AdaMixT: Adaptive Weighted Mixture of Multi-Scale Expert Transformers for Time Series Forecasting]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/MOMEMTO|MOMEMTO]], [[keywords/Time Series Foundation Model|Time Series Foundation Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18751v1 Announce Type: new 
Abstract: Recently reconstruction-based deep models have been widely used for time series anomaly detection, but as their capacity and representation capability increase, these models tend to over-generalize, often reconstructing unseen anomalies accurately. Prior works have attempted to mitigate this by incorporating a memory architecture that stores prototypes of normal patterns. Nevertheless, these approaches suffer from high training costs and have yet to be effectively integrated with time series foundation models (TFMs). To address these challenges, we propose \textbf{MOMEMTO}, a TFM for anomaly detection, enhanced with a patch-based memory module to mitigate over-generalization. The memory module is designed to capture representative normal patterns from multiple domains and enables a single model to be jointly fine-tuned across multiple datasets through a multi-domain training strategy. MOMEMTO initializes memory items with latent representations from a pre-trained encoder, organizes them into patch-level units, and updates them via an attention mechanism. We evaluate our method using 23 univariate benchmark datasets. Experimental results demonstrate that MOMEMTO, as a single model, achieves higher scores on AUC and VUS metrics compared to baseline methods, and further enhances the performance of its backbone TFM, particularly in few-shot learning scenarios.

## 📝 요약

최근 시계열 이상 탐지에 재구성 기반의 딥러닝 모델이 널리 사용되고 있지만, 이 모델들은 과도한 일반화로 인해 보지 못한 이상치도 정확히 재구성하는 문제가 있습니다. 이를 해결하기 위해 기존 연구들은 정상 패턴의 프로토타입을 저장하는 메모리 구조를 도입했으나, 높은 학습 비용과 시계열 기초 모델(TFM)과의 통합 문제를 겪고 있습니다. 이러한 문제를 해결하기 위해, 우리는 이상 탐지를 위한 TFM인 \textbf{MOMEMTO}를 제안합니다. 이 모델은 패치 기반 메모리 모듈을 통해 과도한 일반화를 완화하며, 여러 도메인에서 대표적인 정상 패턴을 캡처하여 다중 도메인 학습 전략을 통해 단일 모델이 여러 데이터셋에서 공동으로 미세 조정될 수 있도록 합니다. MOMEMTO는 사전 학습된 인코더의 잠재 표현으로 메모리 항목을 초기화하고, 이를 패치 수준의 단위로 조직하며, 주의 메커니즘을 통해 업데이트합니다. 23개의 단변량 벤치마크 데이터셋을 사용한 실험 결과, MOMEMTO는 AUC 및 VUS 지표에서 기존 방법보다 높은 점수를 기록했으며, 특히 소수 샷 학습 시나리오에서 백본 TFM의 성능을 더욱 향상시켰습니다.

## 🎯 주요 포인트

- 1. 최근 재구성 기반의 딥러닝 모델은 시계열 이상 탐지에서 널리 사용되지만, 모델의 용량과 표현 능력이 증가함에 따라 미지의 이상치를 정확하게 재구성하는 경향이 있다.
- 2. 기존 연구들은 정상 패턴의 프로토타입을 저장하는 메모리 아키텍처를 도입하여 이 문제를 완화하려 했으나, 높은 훈련 비용과 시계열 기초 모델(TFM)과의 효과적인 통합에 어려움을 겪고 있다.
- 3. 제안된 MOMEMTO는 패치 기반 메모리 모듈을 통해 과도한 일반화를 완화하는 시계열 이상 탐지용 TFM으로, 여러 도메인에서 대표적인 정상 패턴을 포착하고 다중 도메인 훈련 전략을 통해 여러 데이터셋을 통합적으로 미세 조정할 수 있다.
- 4. MOMEMTO는 사전 훈련된 인코더의 잠재 표현으로 메모리 항목을 초기화하고, 패치 수준의 단위로 조직하며, 주의 메커니즘을 통해 업데이트한다.
- 5. 실험 결과, MOMEMTO는 단일 모델로서 23개의 단변량 벤치마크 데이터셋에서 AUC 및 VUS 지표에서 기존 방법보다 높은 점수를 기록하며, 특히 소수 샷 학습 시나리오에서 백본 TFM의 성능을 더욱 향상시킨다.


---

*Generated on 2025-09-24 14:55:12*