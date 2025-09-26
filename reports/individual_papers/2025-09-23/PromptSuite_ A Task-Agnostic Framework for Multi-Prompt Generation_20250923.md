---
keywords:
  - Large Language Model
  - PromptSuite
  - Multi-Prompt Evaluation
  - Modular Prompt Design
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2507.14913
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:08:08.647430",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "PromptSuite",
    "Multi-Prompt Evaluation",
    "Modular Prompt Design"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "PromptSuite": 0.8,
    "Multi-Prompt Evaluation": 0.78,
    "Modular Prompt Design": 0.77
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
        "rationale": "Central to the paper's focus on evaluating language models with multiple prompts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "PromptSuite",
        "canonical": "PromptSuite",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique framework introduced in the paper, essential for understanding its contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-Prompt Evaluation",
        "canonical": "Multi-Prompt Evaluation",
        "aliases": [
          "Multi-Prompt Testing"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for evaluating the robustness of language models, connecting to evaluation methodologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Modular Prompt Design",
        "canonical": "Modular Prompt Design",
        "aliases": [
          "Prompt Modularity"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific design approach in the framework, highlighting its flexibility.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "framework",
      "tasks",
      "benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "PromptSuite",
      "resolved_canonical": "PromptSuite",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-Prompt Evaluation",
      "resolved_canonical": "Multi-Prompt Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Modular Prompt Design",
      "resolved_canonical": "Modular Prompt Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PromptSuite: A Task-Agnostic Framework for Multi-Prompt Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.14913.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2507.14913](https://arxiv.org/abs/2507.14913)

## 🔗 유사한 논문
- [[2025-09-23/Prompt-with-Me_ in-IDE Structured Prompt Management for LLM-Driven Software Engineering_20250923|Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven Software Engineering]] (89.3% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (84.6% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (83.1% similar)
- [[2025-09-23/QA-prompting_ Improving Summarization with Large Language Models using Question-Answering_20250923|QA-prompting: Improving Summarization with Large Language Models using Question-Answering]] (83.0% similar)
- [[2025-09-17/A Taxonomy of Prompt Defects in LLM Systems_20250917|A Taxonomy of Prompt Defects in LLM Systems]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Prompt Evaluation|Multi-Prompt Evaluation]]
**⚡ Unique Technical**: [[keywords/PromptSuite|PromptSuite]], [[keywords/Modular Prompt Design|Modular Prompt Design]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.14913v4 Announce Type: replace 
Abstract: Evaluating LLMs with a single prompt has proven unreliable, with small changes leading to significant performance differences. However, generating the prompt variations needed for a more robust multi-prompt evaluation is challenging, limiting its adoption in practice. To address this, we introduce PromptSuite, a framework that enables the automatic generation of various prompts. PromptSuite is flexible - working out of the box on a wide range of tasks and benchmarks. It follows a modular prompt design, allowing controlled perturbations to each component, and is extensible, supporting the addition of new components and perturbation types. Through a series of case studies, we show that PromptSuite provides meaningful variations to support strong evaluation practices. All resources, including the Python API, source code, user-friendly web interface, and demonstration video, are available at: https://eliyahabba.github.io/PromptSuite/.

## 📝 요약

이 논문은 단일 프롬프트로 대형 언어 모델(LLM)을 평가하는 것이 신뢰성이 떨어진다는 문제를 해결하기 위해 PromptSuite라는 프레임워크를 제안합니다. PromptSuite는 다양한 프롬프트를 자동으로 생성하여 보다 견고한 다중 프롬프트 평가를 가능하게 합니다. 이 프레임워크는 다양한 작업과 벤치마크에 적용 가능하며, 모듈식 설계를 통해 각 구성 요소를 제어된 방식으로 변형할 수 있습니다. 또한 새로운 구성 요소와 변형 유형을 추가할 수 있도록 확장 가능합니다. 사례 연구를 통해 PromptSuite가 강력한 평가를 지원하는 유의미한 변화를 제공함을 보여줍니다. 모든 리소스는 웹사이트에서 제공됩니다.

## 🎯 주요 포인트

- 1. 단일 프롬프트로 LLM을 평가하는 것은 신뢰성이 낮으며, 작은 변화에도 성능 차이가 크게 발생한다.
- 2. PromptSuite는 다양한 프롬프트를 자동으로 생성할 수 있는 프레임워크로, 여러 작업과 벤치마크에 즉시 적용 가능하다.
- 3. 모듈식 프롬프트 설계를 통해 각 구성 요소에 대한 제어된 변화를 허용하며, 새로운 구성 요소와 변화 유형의 추가를 지원한다.
- 4. 사례 연구를 통해 PromptSuite가 강력한 평가를 지원하는 의미 있는 변화를 제공함을 입증하였다.
- 5. PromptSuite의 모든 리소스는 웹 인터페이스와 데모 비디오를 포함하여 공개적으로 제공된다.


---

*Generated on 2025-09-24 04:08:08*