---
keywords:
  - Query Reformulation
  - Rank Fusion
  - Reciprocal Rank Fusion
  - Interactive Knowledge Assistance
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15588
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:07:10.586218",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Query Reformulation",
    "Rank Fusion",
    "Reciprocal Rank Fusion",
    "Interactive Knowledge Assistance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Query Reformulation": 0.75,
    "Rank Fusion": 0.72,
    "Reciprocal Rank Fusion": 0.78,
    "Interactive Knowledge Assistance": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "query rewriting",
        "canonical": "Query Reformulation",
        "aliases": [
          "query rewriting",
          "query modification"
        ],
        "category": "unique_technical",
        "rationale": "Query reformulation is a unique technical approach central to enhancing personalized search, offering strong linkage to retrieval strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "retrieval fusion",
        "canonical": "Rank Fusion",
        "aliases": [
          "retrieval fusion",
          "result fusion"
        ],
        "category": "unique_technical",
        "rationale": "Rank fusion is a specific technique that improves search robustness by combining results from multiple retrieval methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Reciprocal Rank Fusion",
        "canonical": "Reciprocal Rank Fusion",
        "aliases": [
          "RRF"
        ],
        "category": "specific_connectable",
        "rationale": "Reciprocal Rank Fusion is a well-known method in information retrieval, facilitating connections to similar ranking strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "interactive knowledge assistance",
        "canonical": "Interactive Knowledge Assistance",
        "aliases": [
          "iKAT"
        ],
        "category": "unique_technical",
        "rationale": "Interactive Knowledge Assistance is a novel concept in the context of TREC, focusing on real-time conversational search systems.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "TREC",
      "system",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "query rewriting",
      "resolved_canonical": "Query Reformulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "retrieval fusion",
      "resolved_canonical": "Rank Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Reciprocal Rank Fusion",
      "resolved_canonical": "Reciprocal Rank Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "interactive knowledge assistance",
      "resolved_canonical": "Interactive Knowledge Assistance",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# CFDA & CLIP at TREC iKAT 2025: Enhancing Personalized Conversational Search via Query Reformulation and Rank Fusion

**Korean Title:** CFDA & CLIP at TREC iKAT 2025: 질의 재구성과 순위 융합을 통한 개인화된 대화형 검색 강화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15588.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15588](https://arxiv.org/abs/2509.15588)

## 🔗 유사한 논문
- [[2025-09-19/Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (81.3% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (80.4% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (80.0% similar)
- [[2025-09-22/Chunk Knowledge Generation Model for Enhanced Information Retrieval_ A Multi-task Learning Approach_20250922|Chunk Knowledge Generation Model for Enhanced Information Retrieval: A Multi-task Learning Approach]] (79.5% similar)
- [[2025-09-22/Database-Augmented Query Representation for Information Retrieval_20250922|Database-Augmented Query Representation for Information Retrieval]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reciprocal Rank Fusion|Reciprocal Rank Fusion]]
**⚡ Unique Technical**: [[keywords/Query Reformulation|Query Reformulation]], [[keywords/Rank Fusion|Rank Fusion]], [[keywords/Interactive Knowledge Assistance|Interactive Knowledge Assistance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15588v1 Announce Type: cross 
Abstract: The 2025 TREC Interactive Knowledge Assistance Track (iKAT) featured both interactive and offline submission tasks. The former requires systems to operate under real-time constraints, making robustness and efficiency as important as accuracy, while the latter enables controlled evaluation of passage ranking and response generation with pre-defined datasets. To address this, we explored query rewriting and retrieval fusion as core strategies. We built our pipelines around Best-of-$N$ selection and Reciprocal Rank Fusion (RRF) strategies to handle different submission tasks. Results show that reranking and fusion improve robustness while revealing trade-offs between effectiveness and efficiency across both tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15588v1 발표 유형: 교차  
초록: 2025 TREC 인터랙티브 지식 지원 트랙(iKAT)은 인터랙티브 제출 과제와 오프라인 제출 과제를 모두 포함했습니다. 전자는 시스템이 실시간 제약 조건 하에서 작동해야 하므로 정확성만큼이나 견고성과 효율성이 중요하며, 후자는 사전 정의된 데이터셋을 사용하여 구문 순위 매기기와 응답 생성의 통제된 평가를 가능하게 합니다. 이를 해결하기 위해, 우리는 쿼리 재작성 및 검색 융합을 핵심 전략으로 탐구했습니다. 우리는 다양한 제출 과제를 처리하기 위해 Best-of-$N$ 선택 및 상호 순위 융합(RRF) 전략을 중심으로 파이프라인을 구축했습니다. 결과는 재순위 매기기와 융합이 견고성을 향상시키는 동시에 두 과제 전반에 걸쳐 효과성과 효율성 간의 상충 관계를 드러낸다는 것을 보여줍니다.

## 📝 요약

2025 TREC Interactive Knowledge Assistance Track (iKAT)에서는 실시간 상호작용과 오프라인 제출 과제를 다루었습니다. 연구팀은 쿼리 재작성과 검색 융합을 핵심 전략으로 활용하여, Best-of-$N$ 선택 및 Reciprocal Rank Fusion (RRF) 기법을 적용한 파이프라인을 구축했습니다. 결과적으로, 재랭킹과 융합이 시스템의 견고성을 향상시키며, 효율성과 효과성 간의 균형을 드러냈습니다.

## 🎯 주요 포인트

- 1. 2025 TREC Interactive Knowledge Assistance Track (iKAT)는 실시간 상호작용 및 오프라인 제출 과제를 포함합니다.
- 2. 실시간 과제에서는 시스템의 견고성과 효율성이 정확성만큼 중요합니다.
- 3. 오프라인 과제는 미리 정의된 데이터셋을 사용하여 구문 순위 및 응답 생성의 평가를 가능하게 합니다.
- 4. 쿼리 재작성 및 검색 융합 전략을 핵심으로 하여 Best-of-$N$ 선택 및 Reciprocal Rank Fusion (RRF) 전략을 사용했습니다.
- 5. 재랭킹 및 융합은 견고성을 향상시키며, 두 과제 모두에서 효과성과 효율성 간의 균형을 드러냅니다.


---

*Generated on 2025-09-23 09:07:10*