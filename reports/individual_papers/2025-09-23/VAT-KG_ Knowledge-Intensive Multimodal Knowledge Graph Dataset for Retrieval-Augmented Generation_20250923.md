---
keywords:
  - Retrieval Augmented Generation
  - Multimodal Knowledge Graph
  - Visual-Audio-Text Knowledge Graph
  - Multimodal Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.21556
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:06:26.826666",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Multimodal Knowledge Graph",
    "Visual-Audio-Text Knowledge Graph",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "Multimodal Knowledge Graph": 0.78,
    "Visual-Audio-Text Knowledge Graph": 0.82,
    "Multimodal Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's proposed framework and is a trending topic, enhancing connectivity with related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal Knowledge Graph",
        "canonical": "Multimodal Knowledge Graph",
        "aliases": [
          "MMKG"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel type of knowledge graph, which is crucial for understanding its contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Visual-Audio-Text Knowledge Graph",
        "canonical": "Visual-Audio-Text Knowledge Graph",
        "aliases": [
          "VAT-KG"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific implementation of the proposed concept, highlighting its unique contribution to the field.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "The paper's focus on integrating multiple modalities aligns with this trending concept, facilitating broader connections.",
        "novelty_score": 0.5,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "knowledge",
      "dataset",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal Knowledge Graph",
      "resolved_canonical": "Multimodal Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Visual-Audio-Text Knowledge Graph",
      "resolved_canonical": "Visual-Audio-Text Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# VAT-KG: Knowledge-Intensive Multimodal Knowledge Graph Dataset for Retrieval-Augmented Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.21556.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.21556](https://arxiv.org/abs/2506.21556)

## 🔗 유사한 논문
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (83.2% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (82.5% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (82.1% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (82.1% similar)
- [[2025-09-22/DistillMatch_ Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching_20250922|DistillMatch: Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Multimodal Knowledge Graph|Multimodal Knowledge Graph]], [[keywords/Visual-Audio-Text Knowledge Graph|Visual-Audio-Text Knowledge Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.21556v2 Announce Type: replace 
Abstract: Multimodal Knowledge Graphs (MMKGs), which represent explicit knowledge across multiple modalities, play a pivotal role by complementing the implicit knowledge of Multimodal Large Language Models (MLLMs) and enabling more grounded reasoning via Retrieval Augmented Generation (RAG). However, existing MMKGs are generally limited in scope: they are often constructed by augmenting pre-existing knowledge graphs, which restricts their knowledge, resulting in outdated or incomplete knowledge coverage, and they often support only a narrow range of modalities, such as text and visual information. These limitations reduce their extensibility and applicability to a broad range of multimodal tasks, particularly as the field shifts toward richer modalities such as video and audio in recent MLLMs. Therefore, we propose the Visual-Audio-Text Knowledge Graph (VAT-KG), the first concept-centric and knowledge-intensive multimodal knowledge graph that covers visual, audio, and text information, where each triplet is linked to multimodal data and enriched with detailed descriptions of concepts. Specifically, our construction pipeline ensures cross-modal knowledge alignment between multimodal data and fine-grained semantics through a series of stringent filtering and alignment steps, enabling the automatic generation of MMKGs from any multimodal dataset. We further introduce a novel multimodal RAG framework that retrieves detailed concept-level knowledge in response to queries from arbitrary modalities. Experiments on question answering tasks across various modalities demonstrate the effectiveness of VAT-KG in supporting MLLMs, highlighting its practical value in unifying and leveraging multimodal knowledge.

## 📝 요약

이 논문은 시각, 오디오, 텍스트 정보를 아우르는 최초의 개념 중심 멀티모달 지식 그래프인 VAT-KG를 제안합니다. 기존 멀티모달 지식 그래프는 주로 기존 지식 그래프를 확장하여 구축되며, 텍스트와 시각 정보에 국한되어 있어 지식 범위가 제한적입니다. VAT-KG는 이러한 한계를 극복하고, 개념의 상세한 설명과 멀티모달 데이터를 연결하여 보다 풍부한 지식 표현을 제공합니다. 또한, 새로운 멀티모달 RAG 프레임워크를 통해 다양한 모달리티의 질의에 대해 개념 수준의 상세한 지식을 검색할 수 있습니다. 실험 결과, VAT-KG는 멀티모달 대형 언어 모델(MLLMs)을 효과적으로 지원하며, 멀티모달 지식을 통합하고 활용하는 데 실질적인 가치를 가짐을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 멀티모달 지식 그래프(MMKG)는 범위가 제한적이며, 주로 기존 지식 그래프를 보강하여 구축되어 지식이 제한적이고 최신 정보가 부족하다.
- 2. VAT-KG는 시각, 오디오, 텍스트 정보를 포함하는 최초의 개념 중심 멀티모달 지식 그래프로, 각 삼중항이 멀티모달 데이터와 연결되어 있다.
- 3. VAT-KG의 구축 파이프라인은 엄격한 필터링과 정렬 단계를 통해 멀티모달 데이터와 세밀한 의미 간의 교차 모달 지식 정렬을 보장한다.
- 4. 새로운 멀티모달 RAG 프레임워크는 임의의 모달리티로부터의 쿼리에 대해 상세한 개념 수준의 지식을 검색할 수 있다.
- 5. 다양한 모달리티의 질문 응답 실험에서 VAT-KG는 MLLM을 지원하는 데 효과적이며, 멀티모달 지식을 통합하고 활용하는 실질적인 가치를 입증한다.


---

*Generated on 2025-09-24 04:06:26*