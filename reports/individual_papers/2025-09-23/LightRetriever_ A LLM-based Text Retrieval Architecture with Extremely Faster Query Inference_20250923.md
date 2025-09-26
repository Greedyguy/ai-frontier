---
keywords:
  - Large Language Model
  - Text Retrieval
  - Query Encoder
  - LightRetriever
  - Retrieval Throughput
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.12260
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:58:36.712537",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Text Retrieval",
    "Query Encoder",
    "LightRetriever",
    "Retrieval Throughput"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Text Retrieval": 0.78,
    "Query Encoder": 0.8,
    "LightRetriever": 0.88,
    "Retrieval Throughput": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's architecture and are widely used in related research, facilitating numerous connections.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Text Retrieval",
        "canonical": "Text Retrieval",
        "aliases": [
          "Document Retrieval"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel approach to text retrieval, which is a specific focus of the research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Query Encoder",
        "canonical": "Query Encoder",
        "aliases": [
          "Query Encoding"
        ],
        "category": "unique_technical",
        "rationale": "The efficiency of query encoding is a key innovation in the paper, offering potential for specific technical links.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "LightRetriever",
        "canonical": "LightRetriever",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "LightRetriever is the novel architecture proposed by the paper, representing a unique technical contribution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Retrieval Throughput",
        "canonical": "Retrieval Throughput",
        "aliases": [
          "End-to-End Retrieval"
        ],
        "category": "unique_technical",
        "rationale": "Improving retrieval throughput is a significant outcome of the research, relevant for performance-focused discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
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
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Text Retrieval",
      "resolved_canonical": "Text Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Query Encoder",
      "resolved_canonical": "Query Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LightRetriever",
      "resolved_canonical": "LightRetriever",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Retrieval Throughput",
      "resolved_canonical": "Retrieval Throughput",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.12260.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.12260](https://arxiv.org/abs/2505.12260)

## 🔗 유사한 논문
- [[2025-09-18/Large Language Models for Information Retrieval_ A Survey_20250918|Large Language Models for Information Retrieval: A Survey]] (85.7% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (84.9% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (84.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.3% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Text Retrieval|Text Retrieval]], [[keywords/Query Encoder|Query Encoder]], [[keywords/LightRetriever|LightRetriever]], [[keywords/Retrieval Throughput|Retrieval Throughput]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.12260v4 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs)-based text retrieval retrieves documents relevant to search queries based on vector similarities. Documents are pre-encoded offline, while queries arrive in real-time, necessitating an efficient online query encoder. Although LLMs significantly enhance retrieval capabilities, serving deeply parameterized LLMs slows down query inference throughput and increases demands for online deployment resources. In this paper, we propose LightRetriever, a novel LLM-based retriever with extremely lightweight query encoders. Our method retains a full-sized LLM for document encoding, but reduces the workload of query encoding to no more than an embedding lookup. Compared to serving a full LLM on an A800 GPU, our method achieves over 1000x speedup in query encoding and over 10x increase in end-to-end retrieval throughput. Extensive experiments on large-scale retrieval benchmarks show that LightRetriever generalizes well across diverse tasks, maintaining an average of 95% retrieval performance.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)을 기반으로 한 텍스트 검색 시스템의 효율성을 높이기 위해 LightRetriever라는 새로운 검색기를 제안합니다. 기존의 LLM은 문서를 사전 인코딩하고, 실시간으로 도착하는 쿼리를 처리해야 하는데, 이는 온라인 쿼리 인코더에 많은 자원을 요구합니다. LightRetriever는 문서 인코딩에는 전체 크기의 LLM을 사용하지만, 쿼리 인코딩 작업을 임베딩 조회 수준으로 경량화하여 처리 속도를 크게 향상시킵니다. A800 GPU에서 전체 LLM을 사용할 때와 비교하여 쿼리 인코딩 속도가 1000배 이상 빨라지고, 전체 검색 처리량이 10배 이상 증가합니다. 대규모 검색 벤치마크 실험 결과, 다양한 작업에서 평균 95%의 검색 성능을 유지하며 높은 일반화 능력을 보였습니다.

## 🎯 주요 포인트

- 1. LightRetriever는 매우 경량화된 쿼리 인코더를 사용하여 LLM 기반 검색의 효율성을 극대화합니다.
- 2. 문서 인코딩에는 전체 크기의 LLM을 유지하면서 쿼리 인코딩 작업을 임베딩 조회 수준으로 줄입니다.
- 3. A800 GPU에서 전체 LLM을 사용할 때보다 쿼리 인코딩 속도가 1000배 이상 빨라지고, 검색 처리량이 10배 이상 증가합니다.
- 4. 대규모 검색 벤치마크 실험에서 LightRetriever는 다양한 작업에서 평균 95%의 검색 성능을 유지하며 잘 일반화됩니다.


---

*Generated on 2025-09-24 00:58:36*