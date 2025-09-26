---
keywords:
  - Large Language Model
  - Execution Trace
  - Semantic Information
  - Supervised Fine-Tuning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.11686
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:34:56.503964",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Execution Trace",
    "Semantic Information",
    "Supervised Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Execution Trace": 0.78,
    "Semantic Information": 0.8,
    "Supervised Fine-Tuning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Code Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "Code LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader category of language models, crucial for understanding the context of code-specific applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "execution traces",
        "canonical": "Execution Trace",
        "aliases": [
          "runtime traces"
        ],
        "category": "unique_technical",
        "rationale": "Execution traces are pivotal for understanding program behavior, a unique aspect of this study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "semantic information",
        "canonical": "Semantic Information",
        "aliases": [
          "semantic data"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic information is central to the study's exploration of enhancing reasoning in code models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "supervised fine-tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT"
        ],
        "category": "specific_connectable",
        "rationale": "Supervised fine-tuning is a key process in improving model performance, relevant to the study's findings.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "program execution behavior",
      "test time scaling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Code Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "execution traces",
      "resolved_canonical": "Execution Trace",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "semantic information",
      "resolved_canonical": "Semantic Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "supervised fine-tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11686.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.11686](https://arxiv.org/abs/2509.11686)

## 🔗 유사한 논문
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (85.5% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.4% similar)
- [[2025-09-24/LLM-based Vulnerability Discovery through the Lens of Code Metrics_20250924|LLM-based Vulnerability Discovery through the Lens of Code Metrics]] (85.4% similar)
- [[2025-09-25/Reverse Engineering User Stories from Code using Large Language Models_20250925|Reverse Engineering User Stories from Code using Large Language Models]] (85.0% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Information|Semantic Information]], [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Execution Trace|Execution Trace]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11686v3 Announce Type: replace-cross 
Abstract: Code Large Language Models (Code LLMs) have opened a new era in programming with their impressive capabilities. However, recent research has revealed critical limitations in their ability to reason about runtime behavior and understand the actual functionality of programs, which poses significant challenges for their post-training and practical deployment. Specifically, Code LLMs encounter two principal issues: (1) a lack of proficiency in reasoning about program execution behavior, as they struggle to interpret what programs actually do during runtime, and (2) the inconsistent and fragmented representation of semantic information, such as execution traces, across existing methods, which hinders their ability to generalize and reason effectively. These challenges underscore the necessity for more systematic approaches to enhance the reasoning capabilities of Code LLMs. To address these issues, we introduce a generic framework to support integrating semantic information~(e.g., execution trace) to code task-relevant prompts, and conduct a comprehensive study to explore the role of semantic information in enhancing the reasoning ability of Code LLMs accordingly. Specifically, we focus on investigating the usefulness of trace-based semantic information in boosting supervised fine-tuning~(SFT) and post-phase inference of Code LLMs. The experimental results surprisingly disagree with previous works and demonstrate that semantic information has limited usefulness for SFT and test time scaling of Code LLM.

## 📝 요약

Code LLMs는 프로그래밍에 혁신을 가져왔지만, 실행 시 프로그램의 실제 기능을 이해하는 데 한계가 있습니다. 주요 문제는 (1) 프로그램 실행 시의 행동을 추론하는 능력이 부족하고, (2) 기존 방법들이 실행 추적과 같은 의미 정보를 일관되게 표현하지 못한다는 점입니다. 이를 해결하기 위해, 우리는 코드 관련 작업에 의미 정보를 통합할 수 있는 일반적인 프레임워크를 제안하고, 의미 정보가 Code LLMs의 추론 능력을 향상시키는 역할을 조사했습니다. 실험 결과, 의미 정보가 SFT와 테스트 시 확장에 제한적인 유용성을 가진다는 점이 밝혀졌습니다.

## 🎯 주요 포인트

- 1. Code LLMs는 실행 시 프로그램의 실제 동작을 이해하는 데 한계가 있다.
- 2. 실행 추적과 같은 의미 정보의 일관성 없는 표현이 Code LLMs의 일반화와 추론에 장애가 된다.
- 3. Code LLMs의 추론 능력을 향상시키기 위해 체계적인 접근 방식이 필요하다.
- 4. 의미 정보를 통합하는 일반적인 프레임워크를 제안하고, 의미 정보가 Code LLMs의 추론 능력에 미치는 영향을 연구하였다.
- 5. 실험 결과, 의미 정보는 Code LLMs의 감독된 미세 조정 및 테스트 시 확장에 제한적인 유용성을 가진다.


---

*Generated on 2025-09-25 16:34:56*