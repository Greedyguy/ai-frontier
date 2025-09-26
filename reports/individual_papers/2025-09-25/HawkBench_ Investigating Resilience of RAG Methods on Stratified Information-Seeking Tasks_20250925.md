---
keywords:
  - Retrieval Augmented Generation
  - HawkBench
  - Information-Seeking Tasks
  - Multi-Domain Corpora
  - Dynamic Task Strategies
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2502.13465
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:19:37.964656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "HawkBench",
    "Information-Seeking Tasks",
    "Multi-Domain Corpora",
    "Dynamic Task Strategies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.9,
    "HawkBench": 0.85,
    "Information-Seeking Tasks": 0.8,
    "Multi-Domain Corpora": 0.77,
    "Dynamic Task Strategies": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RAG",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG methods"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is central to the paper's focus on evaluating information-seeking tasks, making it a key concept for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.88,
        "link_intent_score": 0.9
      },
      {
        "surface": "HawkBench",
        "canonical": "HawkBench",
        "aliases": [
          "HawkBench benchmark"
        ],
        "category": "unique_technical",
        "rationale": "HawkBench is a unique benchmark introduced in the paper, essential for understanding the evaluation of RAG methods.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.92,
        "link_intent_score": 0.85
      },
      {
        "surface": "information-seeking tasks",
        "canonical": "Information-Seeking Tasks",
        "aliases": [
          "information-seeking scenarios"
        ],
        "category": "broad_technical",
        "rationale": "These tasks are a fundamental aspect of the study, providing context for the evaluation of RAG methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-domain corpora",
        "canonical": "Multi-Domain Corpora",
        "aliases": [
          "multi-domain datasets"
        ],
        "category": "specific_connectable",
        "rationale": "The integration of multi-domain corpora is crucial for understanding the paper's approach to mitigating corpus bias.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "dynamic task strategies",
        "canonical": "Dynamic Task Strategies",
        "aliases": [
          "adaptive task strategies"
        ],
        "category": "unique_technical",
        "rationale": "Dynamic task strategies are highlighted as necessary for improving RAG generalizability, making them a key concept.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RAG",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.88,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "HawkBench",
      "resolved_canonical": "HawkBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.92,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "information-seeking tasks",
      "resolved_canonical": "Information-Seeking Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-domain corpora",
      "resolved_canonical": "Multi-Domain Corpora",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "dynamic task strategies",
      "resolved_canonical": "Dynamic Task Strategies",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# HawkBench: Investigating Resilience of RAG Methods on Stratified Information-Seeking Tasks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13465.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2502.13465](https://arxiv.org/abs/2502.13465)

## 🔗 유사한 논문
- [[2025-09-23/Measuring Risk of Bias in Biomedical Reports_ The RoBBR Benchmark_20250923|Measuring Risk of Bias in Biomedical Reports: The RoBBR Benchmark]] (83.8% similar)
- [[2025-09-25/FHIR-AgentBench_ Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering_20250925|FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering]] (82.8% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (82.5% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (82.1% similar)
- [[2025-09-24/SIRAG_ Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework_20250924|SIRAG: Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Information-Seeking Tasks|Information-Seeking Tasks]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Multi-Domain Corpora|Multi-Domain Corpora]]
**⚡ Unique Technical**: [[keywords/HawkBench|HawkBench]], [[keywords/Dynamic Task Strategies|Dynamic Task Strategies]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13465v2 Announce Type: replace-cross 
Abstract: In real-world information-seeking scenarios, users have dynamic and diverse needs, requiring RAG systems to demonstrate adaptable resilience. To comprehensively evaluate the resilience of current RAG methods, we introduce HawkBench, a human-labeled, multi-domain benchmark designed to rigorously assess RAG performance across categorized task types. By stratifying tasks based on information-seeking behaviors, HawkBench provides a systematic evaluation of how well RAG systems adapt to diverse user needs.
  Unlike existing benchmarks, which focus primarily on specific task types (mostly factoid queries) and rely on varying knowledge bases, HawkBench offers: (1) systematic task stratification to cover a broad range of query types, including both factoid and rationale queries, (2) integration of multi-domain corpora across all task types to mitigate corpus bias, and (3) rigorous annotation for high-quality evaluation.
  HawkBench includes 1,600 high-quality test samples, evenly distributed across domains and task types. Using this benchmark, we evaluate representative RAG methods, analyzing their performance in terms of answer quality and response latency. Our findings highlight the need for dynamic task strategies that integrate decision-making, query interpretation, and global knowledge understanding to improve RAG generalizability. We believe HawkBench serves as a pivotal benchmark for advancing the resilience of RAG methods and their ability to achieve general-purpose information seeking.

## 📝 요약

이 논문은 정보탐색 시나리오에서 사용자의 다양한 요구에 적응할 수 있는 RAG(정보 검색 및 생성) 시스템의 회복력을 평가하기 위해 HawkBench라는 벤치마크를 소개합니다. HawkBench는 인간이 라벨링한 다중 도메인 벤치마크로, 다양한 정보탐색 행동에 기반한 체계적인 과제 분류를 통해 RAG 시스템의 적응력을 평가합니다. 기존 벤치마크와 달리, HawkBench는 사실 질의와 근거 질의를 포함한 다양한 질의 유형을 다루고, 다중 도메인 코퍼스를 통합하여 편향을 줄이며, 엄격한 주석을 통해 평가의 질을 높입니다. 1,600개의 고품질 테스트 샘플을 포함하며, RAG 방법의 응답 품질과 지연 시간을 분석합니다. 연구 결과, RAG 시스템의 일반화 가능성을 높이기 위해 의사결정, 질의 해석, 전반적인 지식 이해를 통합한 동적 과제 전략의 필요성을 강조합니다. HawkBench는 RAG 방법의 회복력 향상에 중요한 기여를 할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. HawkBench는 다양한 사용자 요구에 적응하는 RAG 시스템의 회복력을 평가하기 위해 설계된 인간 라벨링 기반의 다중 도메인 벤치마크입니다.
- 2. HawkBench는 정보 탐색 행동에 따라 작업을 계층화하여 RAG 시스템이 다양한 쿼리 유형에 얼마나 잘 적응하는지를 체계적으로 평가합니다.
- 3. 이 벤치마크는 사실적 쿼리와 논리적 쿼리를 포함한 광범위한 쿼리 유형을 포괄하도록 작업을 체계적으로 분류합니다.
- 4. HawkBench는 모든 작업 유형에 걸쳐 다중 도메인 코퍼스를 통합하여 코퍼스 편향을 완화하고, 엄격한 주석을 통해 고품질 평가를 제공합니다.
- 5. 연구 결과는 RAG 시스템의 일반화 가능성을 향상시키기 위해 의사 결정, 쿼리 해석 및 글로벌 지식 이해를 통합하는 동적 작업 전략의 필요성을 강조합니다.


---

*Generated on 2025-09-25 16:19:37*