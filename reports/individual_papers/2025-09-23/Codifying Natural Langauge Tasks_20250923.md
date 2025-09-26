---
keywords:
  - Text-to-Code
  - Natural Language Processing
  - ICRAG Framework
  - External Knowledge Integration
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17455
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:56:56.174465",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Code",
    "Natural Language Processing",
    "ICRAG Framework",
    "External Knowledge Integration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Code": 0.78,
    "Natural Language Processing": 0.72,
    "ICRAG Framework": 0.8,
    "External Knowledge Integration": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text-to-code",
        "canonical": "Text-to-Code",
        "aliases": [
          "code generation",
          "program synthesis"
        ],
        "category": "unique_technical",
        "rationale": "Text-to-Code is a unique approach that bridges natural language processing and code generation, enhancing connectivity with programming and NLP domains.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "natural language tasks",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP tasks",
          "language tasks"
        ],
        "category": "broad_technical",
        "rationale": "Natural Language Processing is a foundational field that connects various tasks and methodologies in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "ICRAG",
        "canonical": "ICRAG Framework",
        "aliases": [
          "iterative code refinement",
          "ICRAG model"
        ],
        "category": "unique_technical",
        "rationale": "ICRAG is a novel framework introduced in the paper, providing a specific method for transforming natural language into executable code.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "external knowledge",
        "canonical": "External Knowledge Integration",
        "aliases": [
          "knowledge resources",
          "domain knowledge"
        ],
        "category": "specific_connectable",
        "rationale": "Integrating external knowledge is crucial for enhancing the accuracy and applicability of the generated code.",
        "novelty_score": 0.65,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "real-world problems",
      "detailed analysis",
      "limitations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text-to-code",
      "resolved_canonical": "Text-to-Code",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "natural language tasks",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "ICRAG",
      "resolved_canonical": "ICRAG Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "external knowledge",
      "resolved_canonical": "External Knowledge Integration",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Codifying Natural Langauge Tasks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17455.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17455](https://arxiv.org/abs/2509.17455)

## 🔗 유사한 논문
- [[2025-09-22/CodeRAG_ Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion_20250922|CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion]] (83.8% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (82.8% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (81.8% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (81.8% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/External Knowledge Integration|External Knowledge Integration]]
**⚡ Unique Technical**: [[keywords/Text-to-Code|Text-to-Code]], [[keywords/ICRAG Framework|ICRAG Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17455v1 Announce Type: cross 
Abstract: We explore the applicability of text-to-code to solve real-world problems that are typically solved in natural language, such as legal judgment and medical QA. Unlike previous works, our approach leverages the explicit reasoning provided by program generation. We present ICRAG, a framework that transforms natural language into executable programs through iterative refinement using external knowledge from domain resources and GitHub. Across 13 benchmarks, ICRAG achieves up to 161.1\% relative improvement. We provide a detailed analysis of the generated code and the impact of external knowledge, and we discuss the limitations of applying text-to-code approaches to real-world natural language tasks.

## 📝 요약

이 논문은 자연어로 해결되는 법적 판단 및 의료 QA와 같은 실제 문제를 코드로 해결하는 방법을 탐구합니다. 기존 연구와 달리, 프로그램 생성의 명시적 추론을 활용하는 ICRAG 프레임워크를 제안합니다. ICRAG는 외부 지식과 GitHub를 활용하여 자연어를 실행 가능한 프로그램으로 변환하며, 13개 벤치마크에서 최대 161.1%의 상대적 성능 향상을 달성했습니다. 생성된 코드와 외부 지식의 영향을 분석하고, 텍스트-코드 접근법의 한계도 논의합니다.

## 🎯 주요 포인트

- 1. ICRAG는 자연어를 실행 가능한 프로그램으로 변환하는 프레임워크로, 외부 지식과 GitHub를 활용하여 반복적으로 개선합니다.
- 2. ICRAG는 법적 판단 및 의료 QA와 같은 자연어로 해결되는 실제 문제를 해결하기 위해 텍스트-코드 접근 방식을 탐구합니다.
- 3. 13개 벤치마크에서 ICRAG는 최대 161.1%의 상대적 성능 향상을 달성했습니다.
- 4. 생성된 코드와 외부 지식의 영향을 상세히 분석하고, 텍스트-코드 접근 방식의 한계를 논의합니다.


---

*Generated on 2025-09-23 23:56:56*