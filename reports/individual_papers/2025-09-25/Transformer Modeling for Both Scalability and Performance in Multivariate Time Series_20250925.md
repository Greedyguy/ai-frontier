---
keywords:
  - Transformer
  - Delegate Token Attention
  - Multivariate Time Series
  - Attention Mechanism
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19471
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:36:12.169480",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Delegate Token Attention",
    "Multivariate Time Series",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Delegate Token Attention": 0.8,
    "Multivariate Time Series": 0.78,
    "Attention Mechanism": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, crucial for linking various advancements in the field.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Delegate Token Attention",
        "canonical": "Delegate Token Attention",
        "aliases": [
          "DELTAformer"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method proposed in the paper, offering a unique approach to improving transformer scalability and performance.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multivariate Time Series",
        "canonical": "Multivariate Time Series",
        "aliases": [
          "MTS"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area for the proposed method, connecting to other works in time series analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the functioning of transformers and their variants, facilitating connections to a wide range of related research.",
        "novelty_score": 0.35,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "scalability",
      "performance",
      "noise-resilience"
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
      "candidate_surface": "Delegate Token Attention",
      "resolved_canonical": "Delegate Token Attention",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multivariate Time Series",
      "resolved_canonical": "Multivariate Time Series",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Transformer Modeling for Both Scalability and Performance in Multivariate Time Series

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19471.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19471](https://arxiv.org/abs/2509.19471)

## 🔗 유사한 논문
- [[2025-09-23/MTM_ A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification_20250923|MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification]] (84.1% similar)
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (83.0% similar)
- [[2025-09-23/Conv-like Scale-Fusion Time Series Transformer_ A Multi-Scale Representation for Variable-Length Long Time Series_20250923|Conv-like Scale-Fusion Time Series Transformer: A Multi-Scale Representation for Variable-Length Long Time Series]] (83.0% similar)
- [[2025-09-25/Mamba Modulation_ On the Length Generalization of Mamba_20250925|Mamba Modulation: On the Length Generalization of Mamba]] (82.9% similar)
- [[2025-09-23/Measure-to-measure interpolation using Transformers_20250923|Measure-to-measure interpolation using Transformers]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multivariate Time Series|Multivariate Time Series]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Delegate Token Attention|Delegate Token Attention]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19471v1 Announce Type: new 
Abstract: Variable count is among the main scalability bottlenecks for transformer modeling in multivariate time series (MTS) data. On top of this, a growing consensus in the field points to indiscriminate inter-variable mixing as a potential source of noise-accumulation and performance degradation. This is likely exacerbated by sparsity of informative signals characteristic of many MTS systems coupled with representational misalignment stemming from indiscriminate information mixing between (heterogeneous) variables. While scalability and performance are often seen as competing interests in transformer design, we show that both can be improved simultaneously in MTS by strategically constraining the representational capacity of inter-variable mixing. Our proposed method, transformer with Delegate Token Attention (DELTAformer), constrains inter-variable modeling through what we call delegate tokens which are then used to perform full, unconstrained, inter-temporal modeling. Delegate tokens act as an implicit regularizer that forces the model to be highly selective about what inter-variable information is allowed to propagate through the network. Our results show that DELTAformer scales linearly with variable-count while actually outperforming standard transformers, achieving state-of-the-art performance across benchmarks and baselines. In addition, DELTAformer can focus on relevant signals better than standard transformers in noisy MTS environments and overall exhibit superior noise-resilience. Overall, results across various experiments confirm that by aligning our model design to leverage domain-specific challenges in MTS to our advantage, DELTAformer can simultaneously achieve linear scaling while actually improving its performance against standard, quadratic transformers.

## 📝 요약

이 논문은 다변량 시계열(MTS) 데이터에서 변수가 많아질수록 성능이 저하되는 문제를 해결하기 위해 DELTAformer라는 새로운 방법을 제안합니다. DELTAformer는 대표 토큰을 사용하여 변수 간 정보 혼합을 전략적으로 제한함으로써, 모델의 성능과 확장성을 동시에 개선합니다. 이 방법은 변수 수에 따라 선형적으로 확장되며, 기존의 표준 트랜스포머보다 우수한 성능을 보입니다. 특히, 잡음이 많은 환경에서도 관련 신호를 더 잘 포착하여 뛰어난 잡음 저항성을 나타냅니다. 다양한 실험 결과, DELTAformer는 MTS의 도메인 특성을 활용하여 성능을 향상시킬 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 변수 수는 다변량 시계열(MTS) 데이터에서 트랜스포머 모델링의 주요 확장성 병목 현상 중 하나입니다.
- 2. 무차별적인 변수 간 혼합은 노이즈 축적과 성능 저하의 잠재적 원인으로 지목됩니다.
- 3. DELTAformer는 대표 토큰을 사용하여 변수 간 모델링을 제약함으로써 확장성과 성능을 동시에 개선합니다.
- 4. DELTAformer는 변수 수에 따라 선형적으로 확장되며, 표준 트랜스포머를 능가하는 성능을 보여줍니다.
- 5. DELTAformer는 노이즈가 많은 MTS 환경에서도 관련 신호에 더 집중할 수 있어 우수한 노이즈 저항성을 나타냅니다.


---

*Generated on 2025-09-25 16:36:12*