---
keywords:
  - Lifelong Knowledge Editing
  - Large Language Model
  - WikiBigEdit
  - Retrieval Augmented Generation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2503.05683
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:02:14.333031",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Lifelong Knowledge Editing",
    "Large Language Model",
    "WikiBigEdit",
    "Retrieval Augmented Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Lifelong Knowledge Editing": 0.79,
    "Large Language Model": 0.85,
    "WikiBigEdit": 0.78,
    "Retrieval Augmented Generation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Lifelong Knowledge Editing",
        "canonical": "Lifelong Knowledge Editing",
        "aliases": [
          "Continuous Knowledge Update",
          "Persistent Knowledge Editing"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to maintaining up-to-date information in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a foundational element of the study, and linking them helps integrate the paper into broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "WikiBigEdit",
        "canonical": "WikiBigEdit",
        "aliases": [
          "Wikidata Edit Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "As a newly introduced benchmark, it provides a specific context for evaluating knowledge editing techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Retrieval Augmentation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is compared against knowledge editing, providing a relevant connection to trending methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "benchmark",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Lifelong Knowledge Editing",
      "resolved_canonical": "Lifelong Knowledge Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
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
      "candidate_surface": "WikiBigEdit",
      "resolved_canonical": "WikiBigEdit",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Retrieval Augmentation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.05683.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2503.05683](https://arxiv.org/abs/2503.05683)

## 🔗 유사한 논문
- [[2025-09-22/DualEdit_ Dual Editing for Knowledge Updating in Vision-Language Models_20250922|DualEdit: Dual Editing for Knowledge Updating in Vision-Language Models]] (84.4% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (81.2% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (81.2% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (79.7% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Lifelong Knowledge Editing|Lifelong Knowledge Editing]], [[keywords/WikiBigEdit|WikiBigEdit]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.05683v2 Announce Type: replace-cross 
Abstract: Keeping large language models factually up-to-date is crucial for deployment, yet costly retraining remains a challenge. Knowledge editing offers a promising alternative, but methods are only tested on small-scale or synthetic edit benchmarks. In this work, we aim to bridge research into lifelong knowledge editing to real-world edits at a practically relevant scale. We first introduce WikiBigEdit; a large-scale benchmark of real-world Wikidata edits, built to automatically extend lifelong for future-proof benchmarking. In its first instance, it includes over 500K question-answer pairs for knowledge editing alongside a comprehensive evaluation pipeline. Finally, we use WikiBigEdit to study existing knowledge editing techniques' ability to incorporate large volumes of real-world facts and contrast their capabilities to generic modification techniques such as retrieval augmentation and continual finetuning to acquire a complete picture of the practical extent of current lifelong knowledge editing.

## 📝 요약

이 논문은 대규모 언어 모델을 최신 정보로 유지하는 데 있어 지식 편집의 중요성을 강조하며, 기존 방법들이 소규모 또는 인위적인 편집 벤치마크에만 테스트된다는 문제를 지적합니다. 이를 해결하기 위해, 실제 세계의 대규모 편집을 다룰 수 있는 WikiBigEdit라는 벤치마크를 소개합니다. 이 벤치마크는 50만 개 이상의 질문-답변 쌍을 포함하며, 지속 가능한 평가를 위한 포괄적인 파이프라인을 제공합니다. 연구는 WikiBigEdit를 활용하여 기존 지식 편집 기술이 실제 사실을 얼마나 잘 통합할 수 있는지를 평가하고, 검색 증강 및 지속적 미세 조정과 같은 일반적인 수정 기술과 비교하여 현재 지식 편집의 실용적 한계를 분석합니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델을 최신 정보로 유지하는 것은 중요하지만, 재훈련에는 높은 비용이 든다.
- 2. 지식 편집은 대안으로 제시되지만, 기존 방법들은 소규모 또는 인공적인 편집 벤치마크에서만 테스트되었다.
- 3. WikiBigEdit는 실세계의 대규모 Wikidata 편집을 위한 벤치마크로, 50만 개 이상의 질문-답변 쌍을 포함한다.
- 4. WikiBigEdit를 통해 기존 지식 편집 기법이 대량의 실세계 사실을 통합할 수 있는 능력을 연구한다.
- 5. 지식 편집 기법과 검색 증강, 지속적 미세 조정과 같은 일반적인 수정 기법을 비교하여 현재 지식 편집의 실제적 범위를 평가한다.


---

*Generated on 2025-09-24 03:02:14*