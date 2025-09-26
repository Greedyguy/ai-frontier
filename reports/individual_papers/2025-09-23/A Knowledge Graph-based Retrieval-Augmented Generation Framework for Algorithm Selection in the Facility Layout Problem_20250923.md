---
keywords:
  - Retrieval Augmented Generation
  - Facility Layout Problem
  - Large Language Model
  - Graph-based Search
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18054
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:19:12.101937",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Facility Layout Problem",
    "Large Language Model",
    "Graph-based Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.89,
    "Facility Layout Problem": 0.78,
    "Large Language Model": 0.8,
    "Graph-based Search": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Knowledge Graph-based Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "KG RAG",
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the trending concept of RAG, which is central to the paper's framework.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.89
      },
      {
        "surface": "Facility Layout Problem",
        "canonical": "Facility Layout Problem",
        "aliases": [
          "FLP"
        ],
        "category": "unique_technical",
        "rationale": "A specific problem domain that provides context for algorithm selection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "A key component in the framework that connects to existing knowledge on LLMs.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "graph-based search",
        "canonical": "Graph-based Search",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific retrieval approach that enhances connectivity with graph-related concepts.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "algorithm selection",
      "recommendation method",
      "test cases"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Knowledge Graph-based Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Facility Layout Problem",
      "resolved_canonical": "Facility Layout Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "graph-based search",
      "resolved_canonical": "Graph-based Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# A Knowledge Graph-based Retrieval-Augmented Generation Framework for Algorithm Selection in the Facility Layout Problem

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18054.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18054](https://arxiv.org/abs/2509.18054)

## 🔗 유사한 논문
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (84.5% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (82.9% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (82.7% similar)
- [[2025-09-22/CodeRAG_ Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion_20250922|CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion]] (82.3% similar)
- [[2025-09-23/Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on Math Textbook_20250923|Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on Math Textbook]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Graph-based Search|Graph-based Search]]
**⚡ Unique Technical**: [[keywords/Facility Layout Problem|Facility Layout Problem]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18054v1 Announce Type: cross 
Abstract: Selecting a solution algorithm for the Facility Layout Problem (FLP), an NP-hard optimization problem with a multiobjective trade-off, is a complex task that requires deep expert knowledge. The performance of a given algorithm depends on specific problem characteristics such as its scale, objectives, and constraints. This creates a need for a data-driven recommendation method to guide algorithm selection in automated design systems. This paper introduces a new recommendation method to make such expertise accessible, based on a Knowledge Graph-based Retrieval-Augmented Generation (KG RAG) framework. To address this, a domain-specific knowledge graph is constructed from published literature. The method then employs a multi-faceted retrieval mechanism to gather relevant evidence from this knowledge graph using three distinct approaches, which include a precise graph-based search, flexible vector-based search, and high-level cluster-based search. The retrieved evidence is utilized by a Large Language Model (LLM) to generate algorithm recommendations with data-driven reasoning. The proposed KG-RAG method is compared against a commercial LLM chatbot with access to the knowledge base as a table, across a series of diverse, real-world FLP test cases. Based on recommendation accuracy and reasoning capability, the proposed method performed significantly better than the commercial LLM chatbot.

## 📝 요약

이 논문은 다목적 최적화 문제인 시설 배치 문제(FLP)에 적합한 알고리즘을 추천하는 새로운 방법론을 제안합니다. FLP는 문제의 규모, 목표, 제약 조건에 따라 알고리즘 성능이 달라지므로, 전문 지식이 필요합니다. 이를 해결하기 위해, 저자들은 지식 그래프 기반의 검색-증강 생성(KG RAG) 프레임워크를 사용하여 알고리즘 추천 방식을 개발했습니다. 이 방법론은 문헌에서 구축된 도메인 특화 지식 그래프를 활용하여, 정밀한 그래프 기반 검색, 유연한 벡터 기반 검색, 고수준 클러스터 기반 검색을 통해 관련 증거를 수집합니다. 수집된 증거는 대형 언어 모델(LLM)이 데이터 기반으로 알고리즘을 추천하는 데 사용됩니다. 제안된 KG-RAG 방법은 상업용 LLM 챗봇과 비교하여 다양한 실제 FLP 사례에서 추천 정확도와 추론 능력 면에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 시설 배치 문제(FLP)의 알고리즘 선택은 복잡한 작업으로, 문제의 규모, 목표 및 제약 조건에 따라 알고리즘 성능이 달라진다.
- 2. 본 논문은 지식 그래프 기반의 검색-증강 생성(KG RAG) 프레임워크를 활용한 새로운 추천 방법을 제안한다.
- 3. 도메인 특화 지식 그래프를 구축하고, 이를 통해 정밀한 그래프 기반 검색, 유연한 벡터 기반 검색, 고수준 클러스터 기반 검색을 포함한 다면적 검색 메커니즘을 사용한다.
- 4. 대형 언어 모델(LLM)이 검색된 증거를 활용하여 데이터 기반의 알고리즘 추천을 생성한다.
- 5. 제안된 KG-RAG 방법은 상업적 LLM 챗봇보다 추천 정확성과 추론 능력에서 뛰어난 성능을 보였다.


---

*Generated on 2025-09-24 00:19:12*