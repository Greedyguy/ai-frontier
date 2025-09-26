---
keywords:
  - Retrieval Augmented Generation
  - Attention Mechanism
  - Context Compression
  - Large Language Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17486
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:29:00.997869",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Attention Mechanism",
    "Context Compression",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.82,
    "Attention Mechanism": 0.8,
    "Context Compression": 0.78,
    "Large Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's focus and links to recent trends in enhancing LLMs with external data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The attention mechanism is a key component in the proposed method, facilitating context relevance assessment.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Context Compression",
        "canonical": "Context Compression",
        "aliases": [
          "Adaptive Context Compression"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper to improve LLM efficiency by filtering irrelevant information.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are the foundational technology being enhanced by the proposed method, linking to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
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
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Context Compression",
      "resolved_canonical": "Context Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
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
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AttnComp: Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17486.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17486](https://arxiv.org/abs/2509.17486)

## 🔗 유사한 논문
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (88.6% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (84.7% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (83.6% similar)
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (83.4% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Context Compression|Context Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17486v1 Announce Type: new 
Abstract: Retrieval-augmented generation improves the factual accuracy of Large Language Models (LLMs) by incorporating external context, but often suffers from irrelevant retrieved content that hinders effectiveness. Context compression addresses this issue by filtering out irrelevant information from context before LLM generation. However, existing methods struggle to adaptively adjust compression rates for different context, maintain low latency and integrate information across multiple documents. To overcome these limitations, We introduce AttnComp, an adaptive, efficient and context-aware compression framework. By leveraging the attention mechanism of LLMs to identify relevant information, AttnComp employs a Top-P compression algorithm to retain the minimal set of documents whose cumulative attention weights exceeds a predefined threshold. In addition to compression, AttnComp estimates response confidence by assessing the overall relevance of the retrieved content, enabling users to gauge response reliability. Experiments demonstrate that AttnComp outperforms existing compression methods and uncompressed baselines, achieving higher accuracy with substantial compression rates and lower latency.

## 📝 요약

이 논문은 외부 문맥을 활용하여 대형 언어 모델(LLM)의 사실 정확성을 개선하는 검색 기반 생성 방법의 문제점을 해결하고자 합니다. 기존 방법들은 문맥의 압축 비율을 적절히 조정하거나 여러 문서의 정보를 통합하는 데 한계가 있습니다. 이를 극복하기 위해, 저자들은 AttnComp라는 적응적이고 효율적인 문맥 압축 프레임워크를 제안합니다. 이 프레임워크는 LLM의 주의 메커니즘을 활용하여 관련 정보를 식별하고, Top-P 압축 알고리즘을 사용하여 누적 주의 가중치가 일정 임계값을 초과하는 최소 문서 집합을 유지합니다. 또한, AttnComp는 검색된 콘텐츠의 전반적인 관련성을 평가하여 응답의 신뢰도를 추정합니다. 실험 결과, AttnComp는 기존 압축 방법과 비압축 기준보다 높은 정확성과 낮은 지연 시간을 달성하며 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Retrieval-augmented generation은 외부 문맥을 통합하여 대형 언어 모델의 사실 정확성을 개선하지만, 비관련된 검색 콘텐츠로 인해 효과가 저하될 수 있습니다.
- 2. 문맥 압축은 LLM 생성 전에 비관련 정보를 필터링하여 이러한 문제를 해결합니다.
- 3. AttnComp는 적응적이고 효율적인 문맥 인식 압축 프레임워크로, LLM의 어텐션 메커니즘을 활용하여 관련 정보를 식별하고 Top-P 압축 알고리즘을 사용하여 누적 어텐션 가중치가 특정 임계값을 초과하는 최소한의 문서를 유지합니다.
- 4. AttnComp는 검색된 콘텐츠의 전반적인 관련성을 평가하여 응답 신뢰도를 추정하고, 사용자가 응답의 신뢰성을 평가할 수 있도록 합니다.
- 5. 실험 결과, AttnComp는 기존 압축 방법과 비압축 기준선보다 우수한 성능을 보이며, 높은 압축률과 낮은 지연 시간으로 더 높은 정확성을 달성합니다.


---

*Generated on 2025-09-24 03:29:00*