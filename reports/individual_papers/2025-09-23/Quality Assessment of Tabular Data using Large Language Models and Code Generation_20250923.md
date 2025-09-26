---
keywords:
  - Large Language Model
  - Retrieval Augmented Generation
  - Few-Shot Learning
  - Code Generation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.10572
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:28:12.619225",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Few-Shot Learning",
    "Code Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.88,
    "Retrieval Augmented Generation": 0.91,
    "Few-Shot Learning": 0.87,
    "Code Generation": 0.84
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the framework and connect to a wide range of NLP and AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.68,
        "link_intent_score": 0.88
      },
      {
        "surface": "Retrieval-augmented generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending technique that enhances LLMs with external knowledge, crucial for generating reliable quality rules.",
        "novelty_score": 0.78,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.91
      },
      {
        "surface": "Few-shot examples",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "few-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is a key method for training models with minimal data, relevant to the framework's iterative prompting.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.76,
        "link_intent_score": 0.87
      },
      {
        "surface": "Code-generating LLMs",
        "canonical": "Code Generation",
        "aliases": [
          "code synthesis"
        ],
        "category": "unique_technical",
        "rationale": "Code Generation is a unique aspect of the framework, enabling the creation of executable validators.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.84
      }
    ],
    "ban_list_suggestions": [
      "rule-based validation",
      "traditional clustering"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.68,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Retrieval-augmented generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.91
      }
    },
    {
      "candidate_surface": "Few-shot examples",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.76,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Code-generating LLMs",
      "resolved_canonical": "Code Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.84
      }
    }
  ]
}
-->

# Quality Assessment of Tabular Data using Large Language Models and Code Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10572.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.10572](https://arxiv.org/abs/2509.10572)

## 🔗 유사한 논문
- [[2025-09-23/Table2LaTeX-RL_ High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models_20250923|Table2LaTeX-RL: High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models]] (85.9% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (84.3% similar)
- [[2025-09-22/SeCodePLT_ A Unified Platform for Evaluating the Security of Code GenAI_20250922|SeCodePLT: A Unified Platform for Evaluating the Security of Code GenAI]] (84.2% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (83.8% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Code Generation|Code Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10572v2 Announce Type: replace-cross 
Abstract: Reliable data quality is crucial for downstream analysis of tabular datasets, yet rule-based validation often struggles with inefficiency, human intervention, and high computational costs. We present a three-stage framework that combines statistical inliner detection with LLM-driven rule and code generation. After filtering data samples through traditional clustering, we iteratively prompt LLMs to produce semantically valid quality rules and synthesize their executable validators through code-generating LLMs. To generate reliable quality rules, we aid LLMs with retrieval-augmented generation (RAG) by leveraging external knowledge sources and domain-specific few-shot examples. Robust guardrails ensure the accuracy and consistency of both rules and code snippets. Extensive evaluations on benchmark datasets confirm the effectiveness of our approach.

## 📝 요약

이 논문은 표 형식 데이터의 품질을 향상시키기 위한 새로운 3단계 프레임워크를 제안합니다. 기존의 규칙 기반 검증이 비효율적이고 비용이 많이 드는 문제를 해결하기 위해, 통계적 이상치 탐지와 대규모 언어 모델(LLM)을 활용한 규칙 및 코드 생성 방식을 결합했습니다. 데이터 샘플을 전통적인 클러스터링으로 필터링한 후, LLM을 통해 의미적으로 유효한 품질 규칙을 생성하고, 코드 생성 LLM을 통해 실행 가능한 검증기를 만듭니다. 외부 지식 소스와 도메인 특화 예제를 활용한 검색 증강 생성(RAG)을 통해 신뢰할 수 있는 품질 규칙을 생성하며, 견고한 가드레일을 통해 규칙과 코드의 정확성과 일관성을 보장합니다. 벤치마크 데이터셋에 대한 광범위한 평가를 통해 이 접근 방식의 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 신뢰할 수 있는 데이터 품질은 테이블 형식 데이터의 후속 분석에 필수적이며, 기존의 규칙 기반 검증은 비효율성과 높은 계산 비용 문제를 겪고 있다.
- 2. 본 연구는 통계적 이상치 탐지와 대형 언어 모델(LLM)을 활용한 규칙 및 코드 생성을 결합한 3단계 프레임워크를 제안한다.
- 3. 전통적인 클러스터링을 통해 데이터 샘플을 필터링한 후, LLM을 반복적으로 사용하여 의미적으로 유효한 품질 규칙을 생성하고 코드 생성 LLM을 통해 실행 가능한 검증기를 합성한다.
- 4. 외부 지식 소스와 도메인 특화 예제를 활용한 검색 증강 생성(RAG)을 통해 신뢰할 수 있는 품질 규칙 생성을 지원한다.
- 5. 벤치마크 데이터셋에 대한 광범위한 평가 결과, 제안된 접근 방식의 효과가 입증되었다.


---

*Generated on 2025-09-24 01:28:12*