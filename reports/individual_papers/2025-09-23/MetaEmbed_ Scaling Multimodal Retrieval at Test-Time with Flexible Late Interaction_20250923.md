---
keywords:
  - MetaEmbed
  - Multimodal Learning
  - Matryoshka Multi-Vector Retrieval
  - Vision-Language Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.18095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:42:13.359491",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MetaEmbed",
    "Multimodal Learning",
    "Matryoshka Multi-Vector Retrieval",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MetaEmbed": 0.78,
    "Multimodal Learning": 0.82,
    "Matryoshka Multi-Vector Retrieval": 0.77,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MetaEmbed",
        "canonical": "MetaEmbed",
        "aliases": [
          "MetaEmbed Framework"
        ],
        "category": "unique_technical",
        "rationale": "MetaEmbed is a novel framework introduced in the paper, crucial for understanding the proposed approach to multimodal retrieval.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "multimodal retrieval",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal retrieval"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal retrieval is a key application of multimodal learning, linking to broader discussions in the field.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Matryoshka Multi-Vector Retrieval",
        "canonical": "Matryoshka Multi-Vector Retrieval",
        "aliases": [
          "Matryoshka Retrieval"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific training method introduced in the paper, important for understanding the framework's operation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are relevant to the paper's context, linking to current trends in multimodal research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "universal multimodal embedding models",
      "semantic relevance",
      "fine-grained information"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MetaEmbed",
      "resolved_canonical": "MetaEmbed",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multimodal retrieval",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Matryoshka Multi-Vector Retrieval",
      "resolved_canonical": "Matryoshka Multi-Vector Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18095.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.18095](https://arxiv.org/abs/2509.18095)

## 🔗 유사한 논문
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (82.9% similar)
- [[2025-09-22/Causal2Vec_ Improving Decoder-only LLMs as Versatile Embedding Models_20250922|Causal2Vec: Improving Decoder-only LLMs as Versatile Embedding Models]] (82.2% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (82.1% similar)
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (82.1% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/MetaEmbed|MetaEmbed]], [[keywords/Matryoshka Multi-Vector Retrieval|Matryoshka Multi-Vector Retrieval]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18095v1 Announce Type: cross 
Abstract: Universal multimodal embedding models have achieved great success in capturing semantic relevance between queries and candidates. However, current methods either condense queries and candidates into a single vector, potentially limiting the expressiveness for fine-grained information, or produce too many vectors that are prohibitively expensive for multi-vector retrieval. In this work, we introduce MetaEmbed, a new framework for multimodal retrieval that rethinks how multimodal embeddings are constructed and interacted with at scale. During training, a fixed number of learnable Meta Tokens are appended to the input sequence. At test-time, their last-layer contextualized representations serve as compact yet expressive multi-vector embeddings. Through the proposed Matryoshka Multi-Vector Retrieval training, MetaEmbed learns to organize information by granularity across multiple vectors. As a result, we enable test-time scaling in multimodal retrieval, where users can balance retrieval quality against efficiency demands by selecting the number of tokens used for indexing and retrieval interactions. Extensive evaluations on the Massive Multimodal Embedding Benchmark (MMEB) and the Visual Document Retrieval Benchmark (ViDoRe) confirm that MetaEmbed achieves state-of-the-art retrieval performance while scaling robustly to models with 32B parameters.

## 📝 요약

MetaEmbed는 멀티모달 검색을 위한 새로운 프레임워크로, 기존의 단일 벡터 또는 과도한 다중 벡터 방식의 한계를 극복합니다. 학습 시 입력 시퀀스에 고정된 수의 학습 가능한 메타 토큰을 추가하고, 테스트 시 이들의 마지막 층 표현을 다중 벡터 임베딩으로 사용합니다. 이를 통해 정보의 세분화된 조직화를 학습하며, 검색 품질과 효율성 간의 균형을 사용자가 조절할 수 있습니다. 대규모 멀티모달 임베딩 벤치마크(MMEB)와 비주얼 문서 검색 벤치마크(ViDoRe)에서의 평가 결과, MetaEmbed는 32B 파라미터 모델에서도 최첨단 검색 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. MetaEmbed는 다중 벡터 검색을 위한 새로운 프레임워크로, 멀티모달 임베딩의 구성 및 상호작용 방식을 재고합니다.
- 2. 학습 시, 고정된 수의 학습 가능한 메타 토큰을 입력 시퀀스에 추가하여 마지막 층의 문맥화된 표현이 압축적이면서도 표현력 있는 다중 벡터 임베딩을 제공합니다.
- 3. 제안된 Matryoshka Multi-Vector Retrieval 학습을 통해, MetaEmbed는 여러 벡터에 걸쳐 정보의 세분화를 학습합니다.
- 4. 사용자는 인덱싱 및 검색 상호작용에 사용되는 토큰 수를 선택하여 검색 품질과 효율성 요구 사항 간의 균형을 맞출 수 있습니다.
- 5. 대규모 멀티모달 임베딩 벤치마크(MMEB)와 시각적 문서 검색 벤치마크(ViDoRe)에서의 광범위한 평가 결과, MetaEmbed는 32B 파라미터 모델에서도 견고하게 확장되면서 최첨단 검색 성능을 달성합니다.


---

*Generated on 2025-09-24 03:42:13*