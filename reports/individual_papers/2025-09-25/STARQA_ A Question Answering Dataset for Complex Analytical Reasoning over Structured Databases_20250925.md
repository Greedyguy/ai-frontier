---
keywords:
  - Large Language Model
  - Semantic Parsing
  - Complex Analytical Reasoning
  - Text2SQLCode
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19508
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:49:40.516884",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Semantic Parsing",
    "Complex Analytical Reasoning",
    "Text2SQLCode"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Semantic Parsing": 0.82,
    "Complex Analytical Reasoning": 0.78,
    "Text2SQLCode": 0.77
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
        "rationale": "Large Language Models are central to the paper's methodology and are a key technology in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Semantic Parsing",
        "canonical": "Semantic Parsing",
        "aliases": [
          "Text to SQL",
          "SQL Parsing"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic Parsing is crucial for converting natural language to SQL, a core task in the paper.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Complex Analytical Reasoning",
        "canonical": "Complex Analytical Reasoning",
        "aliases": [
          "Analytical Reasoning",
          "Complex Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique focus of the dataset introduced in the paper, emphasizing its novelty.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Text2SQLCode",
        "canonical": "Text2SQLCode",
        "aliases": [
          "Text to SQL Code",
          "SQL and Python Decomposition"
        ],
        "category": "unique_technical",
        "rationale": "Text2SQLCode is a novel approach proposed in the paper, highlighting its innovative aspect.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "benchmark"
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
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Semantic Parsing",
      "resolved_canonical": "Semantic Parsing",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Complex Analytical Reasoning",
      "resolved_canonical": "Complex Analytical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Text2SQLCode",
      "resolved_canonical": "Text2SQLCode",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# STARQA: A Question Answering Dataset for Complex Analytical Reasoning over Structured Databases

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19508.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19508](https://arxiv.org/abs/2509.19508)

## 🔗 유사한 논문
- [[2025-09-25/SteinerSQL_ Graph-Guided Mathematical Reasoning for Text-to-SQL Generation_20250925|SteinerSQL: Graph-Guided Mathematical Reasoning for Text-to-SQL Generation]] (83.8% similar)
- [[2025-09-25/Weaver_ Interweaving SQL and LLM for Table Reasoning_20250925|Weaver: Interweaving SQL and LLM for Table Reasoning]] (82.8% similar)
- [[2025-09-19/DeKeyNLU_ Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction_20250919|DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction]] (82.3% similar)
- [[2025-09-23/AirQA_ A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation_20250923|AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation]] (81.9% similar)
- [[2025-09-23/TableEval_ A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering_20250923|TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Parsing|Semantic Parsing]]
**⚡ Unique Technical**: [[keywords/Complex Analytical Reasoning|Complex Analytical Reasoning]], [[keywords/Text2SQLCode|Text2SQLCode]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19508v1 Announce Type: cross 
Abstract: Semantic parsing methods for converting text to SQL queries enable question answering over structured data and can greatly benefit analysts who routinely perform complex analytics on vast data stored in specialized relational databases. Although several benchmarks measure the abilities of text to SQL, the complexity of their questions is inherently limited by the level of expressiveness in query languages and none focus explicitly on questions involving complex analytical reasoning which require operations such as calculations over aggregate analytics, time series analysis or scenario understanding. In this paper, we introduce STARQA, the first public human-created dataset of complex analytical reasoning questions and answers on three specialized-domain databases. In addition to generating SQL directly using LLMs, we evaluate a novel approach (Text2SQLCode) that decomposes the task into a combination of SQL and Python: SQL is responsible for data fetching, and Python more naturally performs reasoning. Our results demonstrate that identifying and combining the abilities of SQL and Python is beneficial compared to using SQL alone, yet the dataset still remains quite challenging for the existing state-of-the-art LLMs.

## 📝 요약

이 논문에서는 복잡한 분석적 추론이 필요한 질문에 답하기 위한 새로운 데이터셋인 STARQA를 소개합니다. STARQA는 세 개의 전문 분야 데이터베이스를 대상으로 하며, 인간이 만든 최초의 복잡한 분석적 질문과 답변을 포함합니다. 기존의 텍스트-SQL 변환 방법의 한계를 극복하기 위해, SQL과 Python을 결합한 새로운 접근 방식(Text2SQLCode)을 제안합니다. SQL은 데이터 검색을 담당하고, Python은 보다 자연스럽게 추론을 수행합니다. 연구 결과, SQL과 Python의 결합이 SQL 단독 사용보다 효과적임을 보여주지만, 현재의 최첨단 대규모 언어 모델(LLM)에게 여전히 도전적인 과제로 남아있습니다.

## 🎯 주요 포인트

- 1. STARQA는 복잡한 분석적 추론 질문과 답변으로 구성된 최초의 공개 데이터셋으로, 세 가지 전문 분야 데이터베이스를 대상으로 한다.
- 2. Text2SQLCode 접근법은 SQL과 Python을 결합하여 SQL은 데이터 검색을, Python은 추론을 수행하도록 한다.
- 3. SQL과 Python의 능력을 결합하는 것이 SQL 단독 사용보다 효과적임을 실험 결과가 보여준다.
- 4. 현재 최첨단 대규모 언어 모델(LLM)에게도 STARQA 데이터셋은 여전히 도전적인 과제로 남아 있다.


---

*Generated on 2025-09-26 08:49:40*