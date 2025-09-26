---
keywords:
  - Large Language Model
  - Neurosymbolic Reasoning
  - First-Order Logic
  - Counterfactual Variants
  - Chain-of-Thought Prompting
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17377
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:23:40.458192",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Neurosymbolic Reasoning",
    "First-Order Logic",
    "Counterfactual Variants",
    "Chain-of-Thought Prompting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Neurosymbolic Reasoning": 0.8,
    "First-Order Logic": 0.82,
    "Counterfactual Variants": 0.78,
    "Chain-of-Thought Prompting": 0.79
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
          "Large Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on reasoning capabilities and robustness.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neurosymbolic Reasoning",
        "canonical": "Neurosymbolic Reasoning",
        "aliases": [
          "NS Reasoning",
          "Neurosymbolic"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, offering a novel approach to integrate symbolic and neural methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "First-Order Logic",
        "canonical": "First-Order Logic",
        "aliases": [
          "FOL"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the logical framework used in the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Counterfactual Variants",
        "canonical": "Counterfactual Variants",
        "aliases": [
          "Counterfactual Tasks",
          "Counterfactuals"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the method used to test robustness in reasoning systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Chain-of-Thought Prompting",
        "canonical": "Chain-of-Thought Prompting",
        "aliases": [
          "CoT Prompting",
          "Chain-of-Thought"
        ],
        "category": "specific_connectable",
        "rationale": "Important technique discussed for enhancing reasoning in LLMs.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "robustness",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neurosymbolic Reasoning",
      "resolved_canonical": "Neurosymbolic Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "First-Order Logic",
      "resolved_canonical": "First-Order Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Counterfactual Variants",
      "resolved_canonical": "Counterfactual Variants",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Chain-of-Thought Prompting",
      "resolved_canonical": "Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Robustness of Neurosymbolic Reasoners on First-Order Logic Problems

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17377.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17377](https://arxiv.org/abs/2509.17377)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (85.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.4% similar)
- [[2025-09-23/Correlation or Causation_ Analyzing the Causal Structures of LLM and LRM Reasoning Process_20250923|Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process]] (85.0% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.8% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE: Faithful Logic-Aided Reasoning and Exploration]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/First-Order Logic|First-Order Logic]], [[keywords/Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
**⚡ Unique Technical**: [[keywords/Neurosymbolic Reasoning|Neurosymbolic Reasoning]], [[keywords/Counterfactual Variants|Counterfactual Variants]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17377v1 Announce Type: new 
Abstract: Recent trends in NLP aim to improve reasoning capabilities in Large Language Models (LLMs), with key focus on generalization and robustness to variations in tasks. Counterfactual task variants introduce minimal but semantically meaningful changes to otherwise valid first-order logic (FOL) problem instances altering a single predicate or swapping roles of constants to probe whether a reasoning system can maintain logical consistency under perturbation. Previous studies showed that LLMs becomes brittle on counterfactual variations, suggesting that they often rely on spurious surface patterns to generate responses. In this work, we explore if a neurosymbolic (NS) approach that integrates an LLM and a symbolic logical solver could mitigate this problem. Experiments across LLMs of varying sizes show that NS methods are more robust but perform worse overall that purely neural methods. We then propose NSCoT that combines an NS method and Chain-of-Thought (CoT) prompting and demonstrate that while it improves performance, NSCoT still lags behind standard CoT. Our analysis opens research directions for future work.

## 📝 요약

최근 NLP 분야에서는 대형 언어 모델(LLM)의 추론 능력을 향상시키기 위해 일반화와 작업 변형에 대한 강건성을 중점으로 연구하고 있습니다. 반사실적 작업 변형은 논리적 일관성을 유지할 수 있는지를 조사하기 위해 FOL 문제의 일부를 미세하게 변경합니다. 기존 연구에 따르면 LLM은 이러한 변형에 취약하여 표면적 패턴에 의존하는 경향이 있습니다. 본 연구는 LLM과 논리적 해결기를 통합한 신경-기호(NS) 접근법이 이 문제를 완화할 수 있는지를 탐구하였습니다. 다양한 크기의 LLM을 대상으로 한 실험 결과, NS 방법이 더 강건하지만 전반적인 성능은 순수 신경 방법보다 낮았습니다. 이에 NS 방법과 Chain-of-Thought(CoT) 프롬프트를 결합한 NSCoT를 제안하였으며, 성능은 향상되었지만 여전히 표준 CoT보다 뒤처졌습니다. 이 분석은 향후 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 최근 NLP 연구는 대형 언어 모델(LLM)의 추론 능력을 향상시키기 위해 일반화 및 과제 변동에 대한 견고성에 중점을 두고 있다.
- 2. 반사실적 과제 변형은 최소한의 변화로 의미 있는 변화를 도입하여 논리적 일관성을 유지할 수 있는지 평가한다.
- 3. 이전 연구에 따르면 LLM은 반사실적 변형에 취약하며, 종종 표면적 패턴에 의존하여 응답을 생성한다.
- 4. 신경-기호적(NS) 접근법이 이러한 문제를 완화할 수 있는지 탐구했으며, NS 방법이 더 견고하지만 순수 신경 방법보다 성능이 떨어진다는 것을 발견했다.
- 5. NSCoT는 NS 방법과 Chain-of-Thought(CoT) 프롬프트를 결합하여 성능을 개선하지만, 여전히 표준 CoT보다 뒤처진다.


---

*Generated on 2025-09-24 03:23:40*