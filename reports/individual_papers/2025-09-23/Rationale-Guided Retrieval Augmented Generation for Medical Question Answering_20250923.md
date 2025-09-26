---
keywords:
  - Large Language Model
  - Retrieval Augmented Generation
  - Rationale-Guided Retrieval Augmented Generation
  - Biomedical Corpus
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2411.00300
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:44:26.903187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Rationale-Guided Retrieval Augmented Generation",
    "Biomedical Corpus"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.88,
    "Rationale-Guided Retrieval Augmented Generation": 0.8,
    "Biomedical Corpus": 0.77
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
        "rationale": "Large Language Models are central to the study and link well with other NLP concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a key technique discussed in the paper and connects with retrieval and generation methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Rationale-Guided RAG",
        "canonical": "Rationale-Guided Retrieval Augmented Generation",
        "aliases": [
          "RAG^2"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, enhancing the reliability of RAG in biomedical contexts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Biomedical Corpora",
        "canonical": "Biomedical Corpus",
        "aliases": [
          "Biomedical Corpora"
        ],
        "category": "specific_connectable",
        "rationale": "Biomedical corpora are crucial for the retrieval process in the paper, linking to domain-specific datasets.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
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
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Rationale-Guided RAG",
      "resolved_canonical": "Rationale-Guided Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Biomedical Corpora",
      "resolved_canonical": "Biomedical Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Rationale-Guided Retrieval Augmented Generation for Medical Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2411.00300.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2411.00300](https://arxiv.org/abs/2411.00300)

## 🔗 유사한 논문
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (88.4% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (88.3% similar)
- [[2025-09-23/UR$^2$_ Unify RAG and Reasoning through Reinforcement Learning_20250923|UR$^2$: Unify RAG and Reasoning through Reinforcement Learning]] (87.7% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (87.7% similar)
- [[2025-09-23/Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on Math Textbook_20250923|Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on Math Textbook]] (87.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Biomedical Corpus|Biomedical Corpus]]
**⚡ Unique Technical**: [[keywords/Rationale-Guided Retrieval Augmented Generation|Rationale-Guided Retrieval Augmented Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.00300v2 Announce Type: replace 
Abstract: Large language models (LLM) hold significant potential for applications in biomedicine, but they struggle with hallucinations and outdated knowledge. While retrieval-augmented generation (RAG) is generally employed to address these issues, it also has its own set of challenges: (1) LLMs are vulnerable to irrelevant or incorrect context, (2) medical queries are often not well-targeted for helpful information, and (3) retrievers are prone to bias toward the specific source corpus they were trained on. In this study, we present RAG$^2$ (RAtionale-Guided RAG), a new framework for enhancing the reliability of RAG in biomedical contexts. RAG$^2$ incorporates three key innovations: a small filtering model trained on perplexity-based labels of rationales, which selectively augments informative snippets of documents while filtering out distractors; LLM-generated rationales as queries to improve the utility of retrieved snippets; a structure designed to retrieve snippets evenly from a comprehensive set of four biomedical corpora, effectively mitigating retriever bias. Our experiments demonstrate that RAG$^2$ improves the state-of-the-art LLMs of varying sizes, with improvements of up to 6.1\%, and it outperforms the previous best medical RAG model by up to 5.6\% across three medical question-answering benchmarks. Our code is available at https://github.com/dmis-lab/RAG2.

## 📝 요약

이 논문은 생의학 분야에서 대형 언어 모델(LLM)의 신뢰성을 높이기 위한 새로운 프레임워크인 RAG$^2$를 제안합니다. 기존의 검색 보강 생성(RAG) 방식이 가진 문제점을 해결하기 위해, RAG$^2$는 세 가지 혁신을 도입했습니다. 첫째, 합리성 기반의 라벨로 훈련된 필터링 모델을 통해 유용한 정보만 선택적으로 보강합니다. 둘째, LLM이 생성한 합리성을 쿼리로 사용하여 검색된 정보의 유용성을 높입니다. 셋째, 네 가지 생의학 코퍼스에서 고르게 정보를 검색하여 편향을 줄입니다. 실험 결과, RAG$^2$는 기존 최고 수준의 LLM 성능을 최대 6.1% 향상시켰으며, 이전의 최고 의료 RAG 모델을 최대 5.6% 능가했습니다. 코드와 관련 자료는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 생의학 분야에서 잠재력이 크지만 환각 및 오래된 지식 문제를 겪고 있습니다.
- 2. RAG$^2$는 생의학적 문맥에서 RAG의 신뢰성을 향상시키기 위한 새로운 프레임워크로, 세 가지 주요 혁신을 포함합니다.
- 3. RAG$^2$는 혼란 요소를 걸러내고 유용한 정보 조각을 선택적으로 보강하는 소형 필터링 모델을 도입합니다.
- 4. LLM이 생성한 근거를 쿼리로 사용하여 검색된 정보 조각의 유용성을 개선합니다.
- 5. RAG$^2$는 네 가지 생의학 코퍼스에서 정보를 고르게 검색하여 검색 편향을 완화합니다.


---

*Generated on 2025-09-24 03:44:26*