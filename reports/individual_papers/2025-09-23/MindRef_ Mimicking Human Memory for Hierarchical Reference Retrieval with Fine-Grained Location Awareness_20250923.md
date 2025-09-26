---
keywords:
  - Large Language Model
  - Hierarchical Reference Retrieval
  - Constrained Decoding
  - KILT Benchmark
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2402.17010
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:38:08.709768",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Hierarchical Reference Retrieval",
    "Constrained Decoding",
    "KILT Benchmark"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Hierarchical Reference Retrieval": 0.7,
    "Constrained Decoding": 0.8,
    "KILT Benchmark": 0.78
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
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's methodology, linking to a foundational concept in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Reference Retrieval",
        "canonical": "Hierarchical Reference Retrieval",
        "aliases": [
          "reference retrieval",
          "hierarchical retrieval"
        ],
        "category": "unique_technical",
        "rationale": "Describes the novel retrieval approach proposed in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Constrained Decoding",
        "canonical": "Constrained Decoding",
        "aliases": [
          "restricted decoding",
          "controlled decoding"
        ],
        "category": "specific_connectable",
        "rationale": "A specific technique used in the retrieval process, relevant for linking to decoding strategies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "KILT knowledge-sensitive tasks",
        "canonical": "KILT Benchmark",
        "aliases": [
          "KILT tasks",
          "knowledge-intensive language tasks"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to a specific benchmark used for evaluating the method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "parameterized knowledge",
      "document set",
      "short prefix"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hierarchical Reference Retrieval",
      "resolved_canonical": "Hierarchical Reference Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Constrained Decoding",
      "resolved_canonical": "Constrained Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "KILT knowledge-sensitive tasks",
      "resolved_canonical": "KILT Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# MindRef: Mimicking Human Memory for Hierarchical Reference Retrieval with Fine-Grained Location Awareness

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2402.17010.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2402.17010](https://arxiv.org/abs/2402.17010)

## 🔗 유사한 논문
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (85.4% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (84.0% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (83.9% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (83.8% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Constrained Decoding|Constrained Decoding]], [[keywords/KILT Benchmark|KILT Benchmark]]
**⚡ Unique Technical**: [[keywords/Hierarchical Reference Retrieval|Hierarchical Reference Retrieval]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2402.17010v3 Announce Type: replace-cross 
Abstract: When completing knowledge-intensive tasks, humans sometimes need an answer and a corresponding reference passage for auxiliary reading. Previous methods required obtaining pre-segmented article chunks through additional retrieval models. This paper explores leveraging the parameterized knowledge stored during the pre-training phase of large language models (LLMs) to recall reference passage from any starting position independently. We propose a two-stage framework that simulates the scenario of humans recalling easily forgotten references. Initially, the LLM is prompted to recall document title identifiers to obtain a coarse-grained document set. Then, based on the acquired coarse-grained document set, it recalls fine-grained passage. In the two-stage recall process, we use constrained decoding to ensure that content outside of the stored documents is not generated. To increase speed, we only recall a short prefix in the second stage, and then locate its position to retrieve a complete passage. Experiments on KILT knowledge-sensitive tasks have verified that LLMs can independently recall reference passage locations in various task forms, and the obtained reference significantly assists downstream tasks.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 사전 학습 단계에서 저장된 매개변수화된 지식을 활용하여, 지식 집약적 작업에서 참조 구문을 독립적으로 회상하는 방법을 제안합니다. 기존 방법은 추가 검색 모델을 통해 미리 분할된 기사 조각을 필요로 했으나, 본 연구는 인간이 쉽게 잊어버리는 참조를 회상하는 시나리오를 시뮬레이션하는 두 단계 프레임워크를 제안합니다. 첫 단계에서는 LLM이 문서 제목 식별자를 회상하여 대략적인 문서 집합을 얻고, 두 번째 단계에서는 이를 바탕으로 세부 구문을 회상합니다. 이 과정에서 제한된 디코딩을 사용하여 저장된 문서 외의 내용이 생성되지 않도록 하며, 속도를 높이기 위해 두 번째 단계에서는 짧은 접두사만 회상하여 전체 구문을 검색합니다. KILT 지식 민감 작업에서의 실험 결과, LLM이 다양한 작업 형태에서 참조 구문 위치를 독립적으로 회상할 수 있으며, 얻어진 참조가 다운스트림 작업에 크게 기여함을 확인했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 대형 언어 모델(LLM)의 사전 학습 단계에서 저장된 매개변수화된 지식을 활용하여 참조 구문을 독립적으로 회상하는 방법을 탐구합니다.
- 2. 제안된 두 단계 프레임워크는 인간이 쉽게 잊어버리는 참조를 회상하는 시나리오를 시뮬레이션하며, 초기에는 문서 제목 식별자를 회상하여 대략적인 문서 집합을 얻습니다.
- 3. 두 단계 회상 과정에서 저장된 문서 외의 내용이 생성되지 않도록 제한된 디코딩을 사용합니다.
- 4. 실험 결과, LLM이 다양한 작업 형태에서 참조 구문 위치를 독립적으로 회상할 수 있으며, 얻어진 참조가 다운스트림 작업에 크게 도움이 됨을 확인했습니다.


---

*Generated on 2025-09-24 00:38:08*