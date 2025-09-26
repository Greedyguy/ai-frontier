<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:27:16.867997",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Large Language Model",
    "Personalized PageRank",
    "Token-Efficient Graph Construction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "Large Language Model": 0.8,
    "Personalized PageRank": 0.78,
    "Token-Efficient Graph Construction": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph-Based Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a key concept in the paper, linking it to existing retrieval-augmented generation discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's discussion on improving reasoning and accuracy.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Personalized PageRank",
        "canonical": "Personalized PageRank",
        "aliases": [
          "PPR"
        ],
        "category": "unique_technical",
        "rationale": "Personalized PageRank is a novel technique used in the retrieval phase, enhancing graph construction.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Token-Efficient Graph Construction",
        "canonical": "Token-Efficient Graph Construction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept addresses the cost issue in graph-based RAG systems, offering a new perspective.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "system",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph-Based Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Personalized PageRank",
      "resolved_canonical": "Personalized PageRank",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Token-Efficient Graph Construction",
      "resolved_canonical": "Token-Efficient Graph Construction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# TERAG: Token-Efficient Graph-Based Retrieval-Augmented Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18667.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18667](https://arxiv.org/abs/2509.18667)

## 🔗 유사한 논문
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (88.6% similar)
- [[2025-09-23/Rationale-Guided Retrieval Augmented Generation for Medical Question Answering_20250923|Rationale-Guided Retrieval Augmented Generation for Medical Question Answering]] (86.1% similar)
- [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA: Graph-based Reranking against Adversarial Documents Attack]] (86.1% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (85.9% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Personalized PageRank|Personalized PageRank]], [[keywords/Token-Efficient Graph Construction|Token-Efficient Graph Construction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18667v1 Announce Type: new 
Abstract: Graph-based Retrieval-augmented generation (RAG) has become a widely studied approach for improving the reasoning, accuracy, and factuality of Large Language Models. However, many existing graph-based RAG systems overlook the high cost associated with LLM token usage during graph construction, hindering large-scale adoption. To address this, we propose TERAG, a simple yet effective framework designed to build informative graphs at a significantly lower cost. Inspired by HippoRAG, we incorporate Personalized PageRank (PPR) during the retrieval phase, and we achieve at least 80% of the accuracy of widely used graph-based RAG methods while consuming only 3%-11% of the output tokens.

## 📝 요약

이 논문은 대규모 언어 모델의 추론, 정확성 및 사실성을 향상시키기 위한 그래프 기반의 검색 증강 생성(RAG) 접근법을 다룹니다. 기존의 많은 그래프 기반 RAG 시스템은 그래프 구축 시 발생하는 높은 비용 문제를 간과하고 있습니다. 이를 해결하기 위해, 저자들은 TERAG라는 프레임워크를 제안합니다. TERAG는 HippoRAG에서 영감을 받아 검색 단계에서 개인화된 페이지랭크(PPR)를 활용하여, 기존 방법의 80% 이상의 정확성을 유지하면서도 출력 토큰 사용량을 3%-11%로 줄이는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 그래프 기반 검색 증강 생성(RAG)은 대형 언어 모델의 추론, 정확성, 사실성을 향상시키기 위한 널리 연구된 접근법이다.
- 2. 기존의 그래프 기반 RAG 시스템은 그래프 구축 시 LLM 토큰 사용의 높은 비용을 간과하여 대규모 채택을 저해한다.
- 3. TERAG는 정보성 높은 그래프를 낮은 비용으로 구축하기 위한 간단하면서도 효과적인 프레임워크를 제안한다.
- 4. TERAG는 HippoRAG에서 영감을 받아 검색 단계에서 개인화된 페이지랭크(PPR)를 통합한다.
- 5. TERAG는 널리 사용되는 그래프 기반 RAG 방법의 정확성의 최소 80%를 달성하면서 출력 토큰의 3%-11%만 소비한다.


---

*Generated on 2025-09-24 13:27:16*