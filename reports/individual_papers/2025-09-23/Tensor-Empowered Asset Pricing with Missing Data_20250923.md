---
keywords:
  - Tensor Completion
  - Latent Factor Model
  - Risk-Adjusted Returns
  - Temporal Smoothing
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.01861
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:17:37.495311",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tensor Completion",
    "Latent Factor Model",
    "Risk-Adjusted Returns",
    "Temporal Smoothing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Tensor Completion": 0.78,
    "Latent Factor Model": 0.81,
    "Risk-Adjusted Returns": 0.79,
    "Temporal Smoothing": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "tensor completion framework",
        "canonical": "Tensor Completion",
        "aliases": [
          "tensor imputation",
          "tensor framework"
        ],
        "category": "unique_technical",
        "rationale": "Tensor Completion is a specialized technique relevant to the paper's focus on handling missing data in multi-dimensional financial panels.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "latent factor model",
        "canonical": "Latent Factor Model",
        "aliases": [
          "factor model",
          "latent model"
        ],
        "category": "specific_connectable",
        "rationale": "Latent Factor Models are crucial for understanding the imputed data's impact on financial decision-making, linking it to broader financial modeling techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.84,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      },
      {
        "surface": "risk-adjusted returns",
        "canonical": "Risk-Adjusted Returns",
        "aliases": [
          "adjusted returns",
          "risk returns"
        ],
        "category": "specific_connectable",
        "rationale": "Risk-Adjusted Returns are a key metric for evaluating the practical utility of financial models, enhancing connectivity with financial performance analysis.",
        "novelty_score": 0.52,
        "connectivity_score": 0.87,
        "specificity_score": 0.71,
        "link_intent_score": 0.79
      },
      {
        "surface": "temporal smoothing",
        "canonical": "Temporal Smoothing",
        "aliases": [
          "time smoothing",
          "temporal filter"
        ],
        "category": "unique_technical",
        "rationale": "Temporal Smoothing is a novel approach in the context of the paper, addressing noise in financial data and linking to time-series analysis.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "financial panels",
      "imputation accuracy",
      "investment strategies"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "tensor completion framework",
      "resolved_canonical": "Tensor Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "latent factor model",
      "resolved_canonical": "Latent Factor Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.84,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "risk-adjusted returns",
      "resolved_canonical": "Risk-Adjusted Returns",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.87,
        "specificity": 0.71,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "temporal smoothing",
      "resolved_canonical": "Temporal Smoothing",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Tensor-Empowered Asset Pricing with Missing Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.01861.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.01861](https://arxiv.org/abs/2508.01861)

## 🔗 유사한 논문
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (81.0% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.3% similar)
- [[2025-09-23/Enhancing Financial RAG with Agentic AI and Multi-HyDE_ A Novel Approach to Knowledge Retrieval and Hallucination Reduction_20250923|Enhancing Financial RAG with Agentic AI and Multi-HyDE: A Novel Approach to Knowledge Retrieval and Hallucination Reduction]] (79.9% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space: TACE is all you need]] (79.5% similar)
- [[2025-09-17/Synthesizing Behaviorally-Grounded Reasoning Chains_ A Data-Generation Framework for Personal Finance LLMs_20250917|Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation Framework for Personal Finance LLMs]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Latent Factor Model|Latent Factor Model]], [[keywords/Risk-Adjusted Returns|Risk-Adjusted Returns]]
**⚡ Unique Technical**: [[keywords/Tensor Completion|Tensor Completion]], [[keywords/Temporal Smoothing|Temporal Smoothing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.01861v2 Announce Type: replace-cross 
Abstract: Missing data in financial panels presents a critical obstacle, undermining asset-pricing models and reducing the effectiveness of investment strategies. Such panels are often inherently multi-dimensional, spanning firms, time, and financial variables, which adds complexity to the imputation task. Conventional imputation methods often fail by flattening the data's multidimensional structure, struggling with heterogeneous missingness patterns, or overfitting in the face of extreme data sparsity. To address these limitations, we introduce an Adaptive, Cluster-based Temporal smoothing tensor completion framework (ACT-Tensor) tailored for severely and heterogeneously missing multi-dimensional financial data panels. ACT-Tensor incorporates two key innovations: a cluster-based completion module that captures cross-sectional heterogeneity by learning group-specific latent structures; and a temporal smoothing module that proactively removes short-lived noise while preserving slow-moving fundamental trends. Extensive experiments show that ACT-Tensor consistently outperforms state-of-the-art benchmarks in terms of imputation accuracy across a range of missing data regimes, including extreme sparsity scenarios. To assess its practical financial utility, we evaluate the imputed data with a latent factor model tailored for tensor-structured financial data. Results show that ACT-Tensor not only achieves accurate return forecasting but also significantly improves risk-adjusted returns of the constructed portfolio. These findings confirm that our method delivers highly accurate and informative imputations, offering substantial value for financial decision-making.

## 📝 요약

이 논문은 금융 패널의 결측 데이터를 효과적으로 처리하기 위한 새로운 방법론인 ACT-Tensor를 제안합니다. 기존 방법들이 다차원 구조를 단순화하거나 데이터 희소성에 취약한 반면, ACT-Tensor는 클러스터 기반의 보완 모듈과 시간적 평활화 모듈을 통해 이러한 문제를 해결합니다. 클러스터 기반 모듈은 그룹별 잠재 구조를 학습하여 이질성을 포착하고, 시간적 평활화 모듈은 단기적 노이즈를 제거하면서 장기적 추세를 유지합니다. 실험 결과, ACT-Tensor는 다양한 결측 데이터 상황에서 높은 보완 정확도를 보였으며, 금융 모델 평가에서도 높은 수익 예측 정확도와 포트폴리오의 위험 조정 수익률을 개선하는 데 기여했습니다. 이는 금융 의사결정에 있어 ACT-Tensor의 높은 유용성을 입증합니다.

## 🎯 주요 포인트

- 1. 금융 패널의 누락 데이터 문제를 해결하기 위해 다차원적 구조를 유지하는 ACT-Tensor 프레임워크를 제안합니다.
- 2. ACT-Tensor는 군집 기반의 보완 모듈과 시간적 평활화 모듈을 통해 이질적인 누락 패턴과 데이터 희소성을 효과적으로 처리합니다.
- 3. 실험 결과, ACT-Tensor는 다양한 누락 데이터 환경에서 최첨단 기준을 능가하는 보완 정확성을 보여줍니다.
- 4. ACT-Tensor를 활용한 잠재 요인 모델 평가에서 정확한 수익 예측과 포트폴리오의 위험 조정 수익 개선이 확인되었습니다.
- 5. 제안된 방법은 금융 의사 결정에 있어 높은 정확성과 정보성을 제공하여 실질적인 가치를 창출합니다.


---

*Generated on 2025-09-24 01:17:37*