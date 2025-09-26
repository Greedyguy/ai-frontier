---
keywords:
  - Large Language Model
  - SHAP
  - Retrieval Augmented Generation
  - Actor-Critic Reinforcement Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.21179
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:31:56.300476",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SHAP",
    "Retrieval Augmented Generation",
    "Actor-Critic Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "SHAP": 0.78,
    "Retrieval Augmented Generation": 0.77,
    "Actor-Critic Reinforcement Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the framework's cross-modal reasoning capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "SHapley Additive exPlanations",
        "canonical": "SHAP",
        "aliases": [
          "SHAP",
          "SHapley Additive exPlanations"
        ],
        "category": "specific_connectable",
        "rationale": "SHAP is used for feature-level attribution, crucial for interpretability in the framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.79,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG",
          "Retrieval-Augmented Generation"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is employed for case-based inference, enhancing the framework's decision-making process.",
        "novelty_score": 0.68,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Actor-Critic Reinforcement Learning",
        "canonical": "Actor-Critic Reinforcement Learning",
        "aliases": [
          "Actor-Critic RL"
        ],
        "category": "unique_technical",
        "rationale": "This technique is pivotal for guiding LLM reasoning over SHAP-based inputs.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "sarcopenia",
      "diagnosis",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "SHapley Additive exPlanations",
      "resolved_canonical": "SHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.79,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Actor-Critic Reinforcement Learning",
      "resolved_canonical": "Actor-Critic Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# CANDLE: A Cross-Modal Agentic Knowledge Distillation Framework for Interpretable Sarcopenia Diagnosis

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.21179.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.21179](https://arxiv.org/abs/2507.21179)

## 🔗 유사한 논문
- [[2025-09-25/MACD_ Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM_20250925|MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM]] (86.2% similar)
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (86.0% similar)
- [[2025-09-24/Brittleness and Promise_ Knowledge Graph Based Reward Modeling for Diagnostic Reasoning_20250924|Brittleness and Promise: Knowledge Graph Based Reward Modeling for Diagnostic Reasoning]] (85.8% similar)
- [[2025-09-24/Model selection meets clinical semantics_ Optimizing ICD-10-CM prediction via LLM-as-Judge evaluation, redundancy-aware sampling, and section-aware fine-tuning_20250924|Model selection meets clinical semantics: Optimizing ICD-10-CM prediction via LLM-as-Judge evaluation, redundancy-aware sampling, and section-aware fine-tuning]] (84.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/SHAP|SHAP]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Actor-Critic Reinforcement Learning|Actor-Critic Reinforcement Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.21179v2 Announce Type: replace-cross 
Abstract: Background and Aims: Large language models (LLMs) have shown remarkable generalization and transfer capabilities by learning from vast corpora of text and web data. Their semantic representations allow cross-task knowledge transfer and reasoning, offering promising opportunities for data-scarce and heterogeneous domains such as clinical medicine. Yet, in diagnostic tasks like sarcopenia, major challenges remain: interpretability, transparency, and deployment efficiency. Traditional machine learning (TML) models provide stable performance and feature-level attribution, ensuring traceable and auditable decision logic, but lack semantic breadth. Conversely, LLMs enable flexible inference but often function as opaque predictors. Existing integration strategies remain shallow, rarely embedding the structured reasoning of TML into LLM inference. Methods: Using sarcopenia diagnosis as a case study, SHapley Additive exPlanations (SHAP) were extracted from a baseline XGBoost model and transformed into structured, LLM-compatible representations. An actor-critic reinforcement learning (RL) strategy guided the LLM to reason over these SHAP-based inputs, producing calibrated rationales and refined decision rules. The distilled reasoning was consolidated into a structured knowledge repository and deployed via retrieval-augmented generation (RAG) for case-based inference. Results: (Omitted here.) Conclusion: By coupling SHAP-derived statistical evidence with reinforcement-trained LLM reasoning, CANDLE mitigates the interpretability-performance trade-off, enhances predictive accuracy, and preserves high decision consistency. The framework offers a scalable approach to knowledge assetization of TML models, enabling interpretable, reproducible, and clinically aligned decision support in sarcopenia and potentially broader medical domains.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 일반화 및 전이 능력을 활용하여 의료 분야, 특히 근감소증 진단에서의 해석 가능성과 효율성을 개선하는 방법을 제안합니다. 전통적 기계 학습(TML) 모델의 안정성과 추적 가능성을 유지하면서도 LLM의 유연한 추론 능력을 결합하기 위해, SHapley Additive exPlanations(SHAP)을 XGBoost 모델에서 추출하여 LLM이 이해할 수 있는 구조로 변환했습니다. 이 과정에서 강화 학습(RL) 전략을 사용하여 LLM이 SHAP 기반 입력을 통해 합리적인 추론을 하도록 유도했습니다. 결과적으로, 이 방법은 해석 가능성과 성능 간의 균형을 맞추고 예측 정확성을 높이며 일관된 의사 결정을 지원합니다. 이 프레임워크는 TML 모델의 지식 자산화를 통해 근감소증 및 기타 의료 분야에서 해석 가능하고 재현 가능한 의사 결정 지원을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 방대한 텍스트와 웹 데이터를 학습하여 일반화 및 전이 능력을 보여주며, 임상 의학과 같은 데이터가 부족하고 이질적인 분야에서 유망한 기회를 제공합니다.
- 2. 전통적인 기계 학습(TML) 모델은 안정적인 성능과 기능 수준의 설명 가능성을 제공하지만, 의미적 폭이 부족합니다.
- 3. SHapley Additive exPlanations(SHAP)을 사용하여 XGBoost 모델에서 추출된 정보를 LLM과 호환되는 구조로 변환하고, 강화 학습(RL) 전략을 통해 LLM이 이를 기반으로 추론하도록 유도했습니다.
- 4. SHAP 기반 통계 증거와 강화 학습된 LLM 추론을 결합하여 해석 가능성과 성능 간의 균형을 맞추고, 예측 정확성을 향상시키며 높은 의사 결정 일관성을 유지합니다.
- 5. 이 프레임워크는 TML 모델의 지식 자산화를 가능하게 하여, 해석 가능하고 재현 가능하며 임상적으로 정렬된 의사 결정 지원을 제공합니다.


---

*Generated on 2025-09-25 16:31:56*