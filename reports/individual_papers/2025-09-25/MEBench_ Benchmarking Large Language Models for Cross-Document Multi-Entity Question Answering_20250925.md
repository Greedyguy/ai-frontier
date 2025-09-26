---
keywords:
  - Large Language Model
  - Retrieval Augmented Generation
  - Multi-Entity Question Answering
  - Entity-Attributed F1
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2502.18993
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:51:59.050172",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Multi-Entity Question Answering",
    "Entity-Attributed F1"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.82,
    "Multi-Entity Question Answering": 0.78,
    "Entity-Attributed F1": 0.77
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
        "rationale": "Large Language Models are central to the paper's focus on MEQA and are a key technology in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG",
          "Retrieval-Augmented Generation"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that enhances LLMs by integrating retrieval mechanisms, relevant for MEQA.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Entity Question Answering",
        "canonical": "Multi-Entity Question Answering",
        "aliases": [
          "MEQA"
        ],
        "category": "unique_technical",
        "rationale": "MEQA is a unique challenge addressed by the paper, focusing on cross-document entity reasoning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Entity-Attributed F1",
        "canonical": "Entity-Attributed F1",
        "aliases": [
          "EA-F1"
        ],
        "category": "unique_technical",
        "rationale": "EA-F1 is a specific metric introduced for evaluating entity-level correctness in MEQA tasks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.54,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "information extraction"
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
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Entity Question Answering",
      "resolved_canonical": "Multi-Entity Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Entity-Attributed F1",
      "resolved_canonical": "Entity-Attributed F1",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.54,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.18993.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2502.18993](https://arxiv.org/abs/2502.18993)

## 🔗 유사한 논문
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (86.8% similar)
- [[2025-09-24/AECBench_ A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field_20250924|AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field]] (86.8% similar)
- [[2025-09-23/ESGenius_ Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge_20250923|ESGenius: Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge]] (86.7% similar)
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (86.2% similar)
- [[2025-09-23/Beyond Prompting_ An Efficient Embedding Framework for Open-Domain Question Answering_20250923|Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Multi-Entity Question Answering|Multi-Entity Question Answering]], [[keywords/Entity-Attributed F1|Entity-Attributed F1]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18993v3 Announce Type: replace 
Abstract: Multi-entity question answering (MEQA) represents significant challenges for large language models (LLM) and retrieval-augmented generation (RAG) systems, which frequently struggle to consolidate scattered information across diverse documents. While existing methods excel at single-document comprehension, they often struggle with cross-document aggregation, particularly when resolving entity-dense questions like "What is the distribution of ACM Fellows among various fields of study?", which require integrating entity-centric insights from heterogeneous sources (e.g., Wikipedia pages). To address this gap, we introduce MEBench, a novel multi-document, multi-entity benchmark designed to systematically evaluate LLMs' capacity to retrieve, consolidate, and reason over fragmented information. Our benchmark comprises 4,780 questions which are systematically categorized into three primary categories, further divided into eight distinct types, ensuring broad coverage of real-world multi-entity reasoning scenarios. Our experiments on state-of-the-art LLMs (e.g., GPT-4, Llama-3) and RAG pipelines reveal critical limitations: even advanced models achieve only 59% accuracy on MEBench. Our benchmark emphasizes the importance of completeness and factual precision of information extraction in MEQA tasks, using Entity-Attributed F1 (EA-F1) metric for granular evaluation of entity-level correctness and attribution validity. MEBench not only highlights systemic weaknesses in current LLM frameworks but also provides a foundation for advancing robust, entity-aware QA architectures.

## 📝 요약

다중 엔티티 질문 응답(MEQA)은 대형 언어 모델(LLM)과 검색 보강 생성(RAG) 시스템에 상당한 도전 과제를 제시합니다. 기존 방법은 단일 문서 이해에는 뛰어나지만, 다양한 문서에서 정보를 통합하는 데 어려움을 겪습니다. 이를 해결하기 위해 MEBench라는 새로운 벤치마크를 도입했습니다. MEBench는 LLM이 분산된 정보를 검색, 통합, 추론하는 능력을 평가하기 위해 설계된 다중 문서, 다중 엔티티 벤치마크입니다. 4,780개의 질문으로 구성되어 있으며, 실제 다중 엔티티 추론 시나리오를 포괄합니다. 최신 LLM과 RAG 파이프라인 실험 결과, MEBench에서 59%의 정확도에 그쳤으며, 정보 추출의 완전성과 사실적 정확성의 중요성을 강조합니다. MEBench는 현재 LLM의 한계를 드러내고, 엔티티 인식 QA 아키텍처 발전의 기초를 제공합니다.

## 🎯 주요 포인트

- 1. MEQA는 대규모 언어 모델과 검색 기반 생성 시스템에 있어 여러 문서에 흩어진 정보를 통합하는 데 어려움을 겪고 있다.
- 2. MEBench는 LLM의 정보 검색, 통합 및 추론 능력을 평가하기 위한 새로운 다중 문서, 다중 엔티티 벤치마크이다.
- 3. MEBench는 4,780개의 질문을 세 가지 주요 범주와 여덟 가지 유형으로 체계적으로 분류하여 실제 다중 엔티티 추론 시나리오를 포괄한다.
- 4. 최신 LLM과 RAG 파이프라인 실험 결과, MEBench에서 59%의 정확도만을 달성하여 한계를 드러냈다.
- 5. MEBench는 현재 LLM 프레임워크의 체계적 약점을 강조하며, 엔티티 중심의 QA 아키텍처 발전을 위한 기초를 제공한다.


---

*Generated on 2025-09-26 08:51:59*