---
keywords:
  - Internet Yellow Pages
  - ChatIYP
  - Retrieval Augmented Generation
  - Natural Language Processing
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19411
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:53:21.387327",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Internet Yellow Pages",
    "ChatIYP",
    "Retrieval Augmented Generation",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Internet Yellow Pages": 0.78,
    "ChatIYP": 0.82,
    "Retrieval Augmented Generation": 0.8,
    "Natural Language Processing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Internet Yellow Pages",
        "canonical": "Internet Yellow Pages",
        "aliases": [
          "IYP"
        ],
        "category": "unique_technical",
        "rationale": "The Internet Yellow Pages is central to the paper's focus and offers a unique technical context for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "ChatIYP",
        "canonical": "ChatIYP",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ChatIYP is the proposed system in the paper, providing a unique technical contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that connects well with the paper's natural language processing focus.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Natural Language Questions",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "Natural language processing is a broad technical area relevant to the paper's focus on querying with natural language.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Cypher language",
      "evaluation metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Internet Yellow Pages",
      "resolved_canonical": "Internet Yellow Pages",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ChatIYP",
      "resolved_canonical": "ChatIYP",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Natural Language Questions",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Poster: ChatIYP: Enabling Natural Language Access to the Internet Yellow Pages Database

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19411.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19411](https://arxiv.org/abs/2509.19411)

## 🔗 유사한 논문
- [[2025-09-24/YAC_ Bridging Natural Language and Interactive Visual Exploration with Generative AI for Biomedical Data Discovery_20250924|YAC: Bridging Natural Language and Interactive Visual Exploration with Generative AI for Biomedical Data Discovery]] (82.9% similar)
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (80.0% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (79.3% similar)
- [[2025-09-23/From Chat Logs to Collective Insights_ Aggregative Question Answering_20250923|From Chat Logs to Collective Insights: Aggregative Question Answering]] (79.1% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Internet Yellow Pages|Internet Yellow Pages]], [[keywords/ChatIYP|ChatIYP]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19411v1 Announce Type: cross 
Abstract: The Internet Yellow Pages (IYP) aggregates information from multiple sources about Internet routing into a unified, graph-based knowledge base. However, querying it requires knowledge of the Cypher language and the exact IYP schema, thus limiting usability for non-experts. In this paper, we propose ChatIYP, a domain-specific Retrieval-Augmented Generation (RAG) system that enables users to query IYP through natural language questions. Our evaluation demonstrates solid performance on simple queries, as well as directions for improvement, and provides insights for selecting evaluation metrics that are better fit for IYP querying AI agents.

## 📝 요약

이 논문은 인터넷 라우팅 정보를 통합한 그래프 기반 지식 베이스인 Internet Yellow Pages(IYP)의 접근성을 개선하기 위해 ChatIYP라는 시스템을 제안합니다. ChatIYP는 사용자가 자연어로 IYP에 질의할 수 있도록 돕는 도메인 특화 검색-생성(RAG) 시스템입니다. 연구 결과, ChatIYP는 간단한 질의에 대해 우수한 성능을 보이며, 향후 개선 방향과 적절한 평가 지표 선택에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 인터넷 옐로 페이지(IYP)는 인터넷 라우팅 정보를 통합하여 그래프 기반의 지식 베이스로 제공한다.
- 2. IYP의 질의는 Cypher 언어와 정확한 IYP 스키마에 대한 지식이 필요하여 비전문가의 사용이 제한된다.
- 3. ChatIYP는 자연어 질문을 통해 IYP를 질의할 수 있는 도메인 특화 RAG 시스템을 제안한다.
- 4. 평가 결과, ChatIYP는 간단한 질의에서 우수한 성능을 보였으며, 개선 방향을 제시한다.
- 5. IYP 질의 AI 에이전트에 적합한 평가 지표 선택에 대한 통찰을 제공한다.


---

*Generated on 2025-09-25 16:53:21*