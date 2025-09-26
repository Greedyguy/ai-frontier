---
keywords:
  - Large Language Model
  - Table-based Question Answering
  - Semantic Processing
  - Modular Pipeline
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.18961
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:12:11.352607",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Table-based Question Answering",
    "Semantic Processing",
    "Modular Pipeline"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Table-based Question Answering": 0.7,
    "Semantic Processing": 0.8,
    "Modular Pipeline": 0.65
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
        "rationale": "Large Language Models are central to the paper's approach and connect to many related works in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Table-based Question Answering",
        "canonical": "Table-based Question Answering",
        "aliases": [
          "TableQA",
          "Table Question Answering"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application domain of the paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Semantic Processing",
        "canonical": "Semantic Processing",
        "aliases": [
          "Semantic Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic processing is a key component of the paper's methodology, linking it to broader NLP tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Modular Pipeline",
        "canonical": "Modular Pipeline",
        "aliases": [
          "Dynamic Pipeline"
        ],
        "category": "unique_technical",
        "rationale": "The modular pipeline is a novel aspect of the paper's approach, highlighting its flexibility and adaptability.",
        "novelty_score": 0.65,
        "connectivity_score": 0.5,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Table-based Question Answering",
      "resolved_canonical": "Table-based Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Semantic Processing",
      "resolved_canonical": "Semantic Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Modular Pipeline",
      "resolved_canonical": "Modular Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.5,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Weaver: Interweaving SQL and LLM for Table Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18961.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.18961](https://arxiv.org/abs/2505.18961)

## 🔗 유사한 논문
- [[2025-09-23/TableEval_ A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering_20250923|TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering]] (83.7% similar)
- [[2025-09-25/SteinerSQL_ Graph-Guided Mathematical Reasoning for Text-to-SQL Generation_20250925|SteinerSQL: Graph-Guided Mathematical Reasoning for Text-to-SQL Generation]] (83.6% similar)
- [[2025-09-25/Play by the Type Rules_ Inferring Constraints for LLM Functions in Declarative Programs_20250925|Play by the Type Rules: Inferring Constraints for LLM Functions in Declarative Programs]] (82.4% similar)
- [[2025-09-23/TranSQL+_ Serving Large Language Models with SQL on Low-Resource Hardware_20250923|TranSQL+: Serving Large Language Models with SQL on Low-Resource Hardware]] (82.1% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Processing|Semantic Processing]]
**⚡ Unique Technical**: [[keywords/Table-based Question Answering|Table-based Question Answering]], [[keywords/Modular Pipeline|Modular Pipeline]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18961v2 Announce Type: replace 
Abstract: Querying tables with unstructured data is challenging due to the presence of text (or image), either embedded in the table or in external paragraphs, which traditional SQL struggles to process, especially for tasks requiring semantic reasoning. While Large Language Models (LLMs) excel at understanding context, they face limitations with long input sequences. Existing approaches that combine SQL and LLMs typically rely on rigid, predefined work-flows, limiting their adaptability to complex queries. To address these issues, we introduce Weaver , a modular pipeline that dynamically integrates SQL and LLMs for table-based question answering (TableQA). Weaver generates a flexible, step-by-step plan that combines SQL for structured data retrieval with LLMs for semantic processing. By decomposing complex queries into manageable subtasks, Weaver improves accuracy and generalization. Our experiments show that Weaver consistently outperforms state-of-the-art methods across four TableQA datasets, reducing both API calls and error rates. The code, along with other associated scripts, are available at https://coral-lab-asu.github.io/weaver.

## 📝 요약

Weaver는 비정형 데이터가 포함된 테이블에 대한 질의 문제를 해결하기 위해 제안된 모듈형 파이프라인입니다. 기존 SQL과 대형 언어 모델(LLM)의 결합 방식이 복잡한 질의에 적응하기 어려운 점을 개선하고자, Weaver는 SQL과 LLM을 동적으로 통합하여 테이블 기반 질문 응답(TableQA)을 수행합니다. Weaver는 복잡한 질의를 관리 가능한 하위 작업으로 분해하여 정확성과 일반화를 향상시킵니다. 실험 결과, Weaver는 네 가지 TableQA 데이터셋에서 최신 방법들을 능가하며, API 호출과 오류율을 줄이는 데 성공했습니다. Weaver의 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. Weaver는 SQL과 대형 언어 모델(LLM)을 동적으로 통합하여 테이블 기반 질문 응답(TableQA)을 수행하는 모듈형 파이프라인입니다.
- 2. Weaver는 복잡한 쿼리를 관리 가능한 하위 작업으로 분해하여 정확성과 일반화를 향상시킵니다.
- 3. Weaver는 네 가지 TableQA 데이터셋에서 최신 방법들을 능가하며, API 호출과 오류율을 줄입니다.
- 4. Weaver는 구조화된 데이터 검색을 위한 SQL과 의미적 처리를 위한 LLM을 결합한 유연한 단계별 계획을 생성합니다.
- 5. Weaver의 코드와 관련 스크립트는 https://coral-lab-asu.github.io/weaver에서 제공됩니다.


---

*Generated on 2025-09-25 16:12:11*