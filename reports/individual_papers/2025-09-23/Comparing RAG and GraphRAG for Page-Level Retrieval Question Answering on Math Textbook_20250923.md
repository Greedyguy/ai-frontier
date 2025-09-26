---
keywords:
  - Retrieval Augmented Generation
  - GraphRAG
  - Large Language Model
  - Knowledge Graph
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16780
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:33:37.926530",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "GraphRAG",
    "Large Language Model",
    "Knowledge Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "GraphRAG": 0.78,
    "Large Language Model": 0.7,
    "Knowledge Graph": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RAG",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is central to the study, offering a direct link to retrieval-augmented generation techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "GraphRAG",
        "canonical": "GraphRAG",
        "aliases": [
          "Graph-based RAG"
        ],
        "category": "unique_technical",
        "rationale": "GraphRAG represents a novel approach integrating knowledge graphs with RAG, crucial for understanding the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are foundational to the study's context, linking to broader discussions on AI in education.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Knowledge Graph",
        "canonical": "Knowledge Graph",
        "aliases": [
          "KG"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge graphs are integral to the GraphRAG method, providing a structural link to interconnected concepts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Technology-enhanced learning environments",
      "self-paced study",
      "retrieval accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RAG",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "GraphRAG",
      "resolved_canonical": "GraphRAG",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Knowledge Graph",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on Math Textbook

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16780.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16780](https://arxiv.org/abs/2509.16780)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (85.9% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (85.9% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (85.9% similar)
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (85.9% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Knowledge Graph|Knowledge Graph]]
**⚡ Unique Technical**: [[keywords/GraphRAG|GraphRAG]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16780v1 Announce Type: cross 
Abstract: Technology-enhanced learning environments often help students retrieve relevant learning content for questions arising during self-paced study. Large language models (LLMs) have emerged as novel aids for information retrieval during learning. While LLMs are effective for general-purpose question-answering, they typically lack alignment with the domain knowledge of specific course materials such as textbooks and slides. We investigate Retrieval-Augmented Generation (RAG) and GraphRAG, a knowledge graph-enhanced RAG approach, for page-level question answering in an undergraduate mathematics textbook. While RAG has been effective for retrieving discrete, contextually relevant passages, GraphRAG may excel in modeling interconnected concepts and hierarchical knowledge structures. We curate a dataset of 477 question-answer pairs, each tied to a distinct textbook page. We then compare the standard embedding-based RAG methods to GraphRAG for evaluating both retrieval accuracy-whether the correct page is retrieved-and generated answer quality via F1 scores. Our findings show that embedding-based RAG achieves higher retrieval accuracy and better F1 scores compared to GraphRAG, which tends to retrieve excessive and sometimes irrelevant content due to its entity-based structure. We also explored re-ranking the retrieved pages with LLM and observed mixed results, including performance drop and hallucinations when dealing with larger context windows. Overall, this study highlights both the promises and challenges of page-level retrieval systems in educational contexts, emphasizing the need for more refined retrieval methods to build reliable AI tutoring solutions in providing reference page numbers.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 정보 검색의 한계를 극복하기 위해 Retrieval-Augmented Generation (RAG)과 GraphRAG를 활용한 페이지 수준의 질문 응답 시스템을 연구합니다. 특히, 학부 수학 교과서의 페이지별 질문에 대한 답변을 제공하기 위해 두 방법을 비교했습니다. 477개의 질문-답변 쌍을 기반으로 한 실험에서, RAG는 더 높은 검색 정확도와 F1 점수를 기록하며, GraphRAG보다 우수한 성능을 보였습니다. GraphRAG는 개체 기반 구조로 인해 불필요한 정보를 과도하게 검색하는 경향이 있었습니다. 또한, LLM을 사용한 페이지 재정렬 실험에서는 혼합된 결과가 나타났습니다. 이 연구는 교육 환경에서 페이지 수준의 검색 시스템의 가능성과 도전을 강조하며, 보다 정교한 검색 방법의 필요성을 제기합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 일반적인 질문-응답에는 효과적이지만, 특정 교재의 도메인 지식과의 정렬이 부족하다.
- 2. Retrieval-Augmented Generation (RAG)과 GraphRAG는 학부 수학 교재의 페이지 수준 질문 응답에 사용되었으며, RAG는 개별적이고 맥락적으로 관련된 구절을 잘 검색하는 반면, GraphRAG는 상호 연결된 개념과 계층적 지식 구조를 모델링하는 데 강점을 보인다.
- 3. RAG는 GraphRAG에 비해 더 높은 검색 정확도와 F1 점수를 기록했으며, GraphRAG는 엔티티 기반 구조로 인해 과도하고 때로는 관련 없는 콘텐츠를 검색하는 경향이 있다.
- 4. LLM을 사용한 검색 페이지의 재정렬 실험에서는 혼합된 결과가 나타났으며, 특히 더 큰 컨텍스트 창을 다룰 때 성능 저하와 환각 현상이 발생했다.
- 5. 이 연구는 교육 맥락에서 페이지 수준 검색 시스템의 가능성과 도전을 강조하며, 신뢰할 수 있는 AI 튜터링 솔루션을 구축하기 위해 더 정교한 검색 방법의 필요성을 제시한다.


---

*Generated on 2025-09-23 23:33:37*