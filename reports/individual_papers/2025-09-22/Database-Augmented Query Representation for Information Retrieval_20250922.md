---
keywords:
  - Database-Augmented Query Representation
  - Information Retrieval
  - Graph-based Set-Encoding Strategy
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2406.16013
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:43:50.673615",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Database-Augmented Query Representation",
    "Information Retrieval",
    "Graph-based Set-Encoding Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Database-Augmented Query Representation": 0.8,
    "Information Retrieval": 0.7,
    "Graph-based Set-Encoding Strategy": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Database-Augmented Query representation",
        "canonical": "Database-Augmented Query Representation",
        "aliases": [
          "DAQu"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for enhancing query retrieval using database metadata.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Information Retrieval",
        "canonical": "Information Retrieval",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Core concept of the paper, relevant to connecting with other retrieval-based research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Graph-based set-encoding strategy",
        "canonical": "Graph-based Set-Encoding Strategy",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes a specific encoding method used in the framework, relevant for linking to graph encoding techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "retrieval framework",
      "metadata",
      "features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Database-Augmented Query representation",
      "resolved_canonical": "Database-Augmented Query Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Information Retrieval",
      "resolved_canonical": "Information Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Graph-based set-encoding strategy",
      "resolved_canonical": "Graph-based Set-Encoding Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Database-Augmented Query Representation for Information Retrieval

**Korean Title:** 데이터베이스 보강 쿼리 표현을 통한 정보 검색

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2406.16013.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2406.16013](https://arxiv.org/abs/2406.16013)

## 🔗 유사한 논문
- [[2025-09-22/Chunk Knowledge Generation Model for Enhanced Information Retrieval_ A Multi-task Learning Approach_20250922|Chunk Knowledge Generation Model for Enhanced Information Retrieval: A Multi-task Learning Approach]] (83.2% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (81.2% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (80.9% similar)
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA: A multi-agent framework for annotation]] (80.4% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Information Retrieval|Information Retrieval]]
**⚡ Unique Technical**: [[keywords/Database-Augmented Query Representation|Database-Augmented Query Representation]], [[keywords/Graph-based Set-Encoding Strategy|Graph-based Set-Encoding Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.16013v3 Announce Type: replace-cross 
Abstract: Information retrieval models that aim to search for documents relevant to a query have shown multiple successes, which have been applied to diverse tasks. Yet, the query from the user is oftentimes short, which challenges the retrievers to correctly fetch relevant documents. To tackle this, previous studies have proposed expanding the query with a couple of additional (user-related) features related to it. However, they may be suboptimal to effectively augment the query, and there is plenty of other information available to augment it in a relational database. Motivated by this fact, we present a novel retrieval framework called Database-Augmented Query representation (DAQu), which augments the original query with various (query-related) metadata across multiple tables. In addition, as the number of features in the metadata can be very large and there is no order among them, we encode them with the graph-based set-encoding strategy, which considers hierarchies of features in the database without order. We validate our DAQu in diverse retrieval scenarios, demonstrating that it significantly enhances overall retrieval performance over relevant baselines.

## 🔍 Abstract (한글 번역)

arXiv:2406.16013v3 발표 유형: 교차 교체  
초록: 쿼리에 관련된 문서를 검색하기 위한 정보 검색 모델은 다양한 작업에 적용되어 여러 성공을 거두었습니다. 그러나 사용자의 쿼리는 종종 짧아서 검색기가 관련 문서를 올바르게 가져오는 데 어려움을 겪습니다. 이를 해결하기 위해 이전 연구에서는 쿼리와 관련된 몇 가지 추가적인 (사용자 관련) 기능으로 쿼리를 확장하는 방법을 제안했습니다. 하지만 이러한 방법은 쿼리를 효과적으로 보강하는 데 최적이 아닐 수 있으며, 관계형 데이터베이스에서 쿼리를 보강할 수 있는 다른 많은 정보가 존재합니다. 이러한 사실에 영감을 받아, 우리는 Database-Augmented Query 표현(DAQu)이라는 새로운 검색 프레임워크를 제안합니다. 이 프레임워크는 여러 테이블에 걸쳐 다양한 (쿼리 관련) 메타데이터로 원래 쿼리를 보강합니다. 또한 메타데이터의 기능 수가 매우 많고 그들 간에 순서가 없기 때문에, 우리는 데이터베이스의 기능 계층을 순서 없이 고려하는 그래프 기반의 집합 인코딩 전략으로 이를 인코딩합니다. 우리는 다양한 검색 시나리오에서 DAQu를 검증하여 관련 기준선 대비 전반적인 검색 성능을 크게 향상시킴을 입증합니다.

## 📝 요약

이 논문은 정보 검색 모델의 성능을 향상시키기 위한 새로운 프레임워크인 DAQu(Database-Augmented Query representation)를 제안합니다. 기존의 짧은 사용자 쿼리를 보완하기 위해 몇 가지 추가 기능을 사용하던 방법이 최적이 아닐 수 있다는 점을 지적하며, 관계형 데이터베이스의 다양한 메타데이터를 활용해 쿼리를 확장합니다. DAQu는 여러 테이블의 메타데이터를 사용하여 쿼리를 보강하며, 그래프 기반의 집합 인코딩 전략을 통해 메타데이터의 계층 구조를 고려합니다. 다양한 검색 시나리오에서 DAQu의 유효성을 검증한 결과, 관련 기준선 대비 검색 성능이 크게 향상됨을 확인했습니다.

## 🎯 주요 포인트

- 1. 정보 검색 모델은 사용자의 짧은 쿼리로 인해 관련 문서를 정확히 검색하는 데 어려움을 겪습니다.
- 2. 기존 연구에서는 사용자 관련 기능을 추가하여 쿼리를 확장하는 방법을 제안했지만, 이는 최적의 방법이 아닐 수 있습니다.
- 3. DAQu는 관계형 데이터베이스의 다양한 메타데이터를 활용하여 쿼리를 확장하는 새로운 검색 프레임워크입니다.
- 4. DAQu는 메타데이터의 다양한 기능을 그래프 기반의 집합 인코딩 전략으로 인코딩하여 기능의 계층 구조를 고려합니다.
- 5. DAQu는 다양한 검색 시나리오에서 기존 기준선보다 검색 성능을 크게 향상시킵니다.


---

*Generated on 2025-09-23 09:43:50*