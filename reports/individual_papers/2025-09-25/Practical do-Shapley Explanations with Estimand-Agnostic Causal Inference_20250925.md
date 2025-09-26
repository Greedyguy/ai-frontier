---
keywords:
  - do-SHAP
  - Causal Inference
  - Estimand-Agnostic Methods
  - Data Generating Processes
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20211
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:46:19.561232",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "do-SHAP",
    "Causal Inference",
    "Estimand-Agnostic Methods",
    "Data Generating Processes"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "do-SHAP": 0.78,
    "Causal Inference": 0.82,
    "Estimand-Agnostic Methods": 0.7,
    "Data Generating Processes": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "do-SHAP",
        "canonical": "do-SHAP",
        "aliases": [
          "interventional SHAP"
        ],
        "category": "unique_technical",
        "rationale": "do-SHAP represents a novel extension of SHAP that incorporates causal inference, making it a unique technical contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "causal inference",
        "canonical": "Causal Inference",
        "aliases": [
          "causal analysis"
        ],
        "category": "broad_technical",
        "rationale": "Causal inference is a fundamental concept that connects to various methodologies in machine learning and statistics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "estimand-agnostic approaches",
        "canonical": "Estimand-Agnostic Methods",
        "aliases": [
          "estimand-free methods"
        ],
        "category": "unique_technical",
        "rationale": "These approaches allow for flexible estimation across models, which is a novel contribution to causal inference techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Data Generating Processes",
        "canonical": "Data Generating Processes",
        "aliases": [
          "DGP"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding and explaining data generating processes is crucial for model interpretability and causal analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "explanation",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "do-SHAP",
      "resolved_canonical": "do-SHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "causal inference",
      "resolved_canonical": "Causal Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "estimand-agnostic approaches",
      "resolved_canonical": "Estimand-Agnostic Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Data Generating Processes",
      "resolved_canonical": "Data Generating Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Practical do-Shapley Explanations with Estimand-Agnostic Causal Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20211.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20211](https://arxiv.org/abs/2509.20211)

## 🔗 유사한 논문
- [[2025-09-24/Losing is for Cherishing_ Data Valuation Based on Machine Unlearning and Shapley Value_20250924|Losing is for Cherishing: Data Valuation Based on Machine Unlearning and Shapley Value]] (80.5% similar)
- [[2025-09-24/An Information-Flow Perspective on Explainability Requirements_ Specification and Verification_20250924|An Information-Flow Perspective on Explainability Requirements: Specification and Verification]] (79.1% similar)
- [[2025-09-25/CANDLE_ A Cross-Modal Agentic Knowledge Distillation Framework for Interpretable Sarcopenia Diagnosis_20250925|CANDLE: A Cross-Modal Agentic Knowledge Distillation Framework for Interpretable Sarcopenia Diagnosis]] (78.9% similar)
- [[2025-09-23/SalaMAnder_ Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning_20250923|SalaMAnder: Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning]] (78.9% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Causal Inference|Causal Inference]]
**🔗 Specific Connectable**: [[keywords/Data Generating Processes|Data Generating Processes]]
**⚡ Unique Technical**: [[keywords/do-SHAP|do-SHAP]], [[keywords/Estimand-Agnostic Methods|Estimand-Agnostic Methods]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20211v1 Announce Type: new 
Abstract: Among explainability techniques, SHAP stands out as one of the most popular, but often overlooks the causal structure of the problem. In response, do-SHAP employs interventional queries, but its reliance on estimands hinders its practical application. To address this problem, we propose the use of estimand-agnostic approaches, which allow for the estimation of any identifiable query from a single model, making do-SHAP feasible on complex graphs. We also develop a novel algorithm to significantly accelerate its computation at a negligible cost, as well as a method to explain inaccessible Data Generating Processes. We demonstrate the estimation and computational performance of our approach, and validate it on two real-world datasets, highlighting its potential in obtaining reliable explanations.

## 📝 요약

이 논문은 설명 가능성 기법 중 하나인 SHAP의 한계를 극복하기 위해 do-SHAP을 개선한 연구를 다룹니다. 기존 do-SHAP은 개입적 쿼리를 사용하지만, 추정량에 의존하여 실용성이 떨어지는 문제를 가지고 있었습니다. 이를 해결하기 위해, 저자들은 추정량에 구애받지 않는 접근법을 제안하여 복잡한 그래프에서도 do-SHAP을 적용할 수 있도록 했습니다. 또한, 계산 속도를 크게 향상시키는 알고리즘과 접근할 수 없는 데이터 생성 과정을 설명하는 방법을 개발했습니다. 이 접근법은 두 개의 실제 데이터셋에서 검증되었으며, 신뢰할 수 있는 설명을 제공할 수 있는 잠재력을 보여주었습니다.

## 🎯 주요 포인트

- 1. SHAP 기법은 인과 구조를 간과하는 경향이 있으며, 이를 보완하기 위해 do-SHAP이 도입되었으나, 추정량에 대한 의존성이 실용성을 저해합니다.
- 2. 추정량 비의존적 접근법을 제안하여 복잡한 그래프에서도 do-SHAP을 적용 가능하게 합니다.
- 3. 새로운 알고리즘을 개발하여 계산 속도를 크게 향상시키면서 비용을 거의 들이지 않습니다.
- 4. 접근할 수 없는 데이터 생성 과정을 설명할 수 있는 방법을 제안합니다.
- 5. 두 개의 실제 데이터셋을 통해 제안된 접근법의 추정 및 계산 성능을 검증하고 신뢰할 수 있는 설명을 얻을 수 있는 잠재력을 강조합니다.


---

*Generated on 2025-09-25 16:46:19*