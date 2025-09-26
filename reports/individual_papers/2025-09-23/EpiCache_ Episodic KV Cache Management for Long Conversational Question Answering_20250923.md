---
keywords:
  - EpiCache
  - Long Conversational Question Answering
  - Key-Value Caching
  - Large Language Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17396
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:24:21.716796",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "EpiCache",
    "Long Conversational Question Answering",
    "Key-Value Caching",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "EpiCache": 0.8,
    "Long Conversational Question Answering": 0.78,
    "Key-Value Caching": 0.75,
    "Large Language Model": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "EpiCache",
        "canonical": "EpiCache",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "EpiCache is a novel framework specific to the paper's context, offering unique insights into KV cache management.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Long Conversational Question Answering",
        "canonical": "Long Conversational Question Answering",
        "aliases": [
          "LongConvQA"
        ],
        "category": "unique_technical",
        "rationale": "This term describes a specific application area that the paper addresses, relevant for linking related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Key-Value Caching",
        "canonical": "Key-Value Caching",
        "aliases": [
          "KV Caching"
        ],
        "category": "specific_connectable",
        "rationale": "Key-Value Caching is central to the paper's discussion and connects to broader research on memory management in LLMs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to the paper's context, providing a broad technical basis for linking.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "EpiCache",
      "resolved_canonical": "EpiCache",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Long Conversational Question Answering",
      "resolved_canonical": "Long Conversational Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Key-Value Caching",
      "resolved_canonical": "Key-Value Caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# EpiCache: Episodic KV Cache Management for Long Conversational Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17396.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17396](https://arxiv.org/abs/2509.17396)

## 🔗 유사한 논문
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (86.7% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (85.5% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (83.5% similar)
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (83.5% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Key-Value Caching|Key-Value Caching]]
**⚡ Unique Technical**: [[keywords/EpiCache|EpiCache]], [[keywords/Long Conversational Question Answering|Long Conversational Question Answering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17396v1 Announce Type: new 
Abstract: Recent advances in large language models (LLMs) have extended context lengths, enabling assistants to sustain long histories for coherent, personalized responses. This ability, however, hinges on Key-Value (KV) caching, whose memory grows linearly with dialogue length and quickly dominates under strict resource constraints. An active line of research for reducing this overhead is KV cache compression, which seeks to limit cache size while preserving accuracy. Yet existing methods face two major limitations: (i) evicting entries after full-context prefill causes unbounded peak memory, and (ii) query-dependent eviction narrows the cache to a single query, leading to degraded accuracy in multi-turn conversations. We introduce EpiCache, a training-free KV cache management framework for long conversational question answering (LongConvQA) under fixed memory budgets. EpiCache bounds cache growth through block-wise prefill and preserves topic-relevant context via episodic KV compression, which clusters conversation history into coherent episodes and applies episode-specific KV cache eviction. We further design an adaptive layer-wise budget allocation strategy that measures each layer's sensitivity to eviction and distributes the memory budget across layers accordingly. Across three LongConvQA benchmarks, EpiCache improves accuracy by up to 40% over recent baselines, sustains near-full KV accuracy under 4-6x compression, and reduces latency and memory by up to 2.4x and 3.5x, thereby enabling efficient multi-turn interaction under strict resource constraints.

## 📝 요약

최근 대형 언어 모델(LLM)의 발전으로 긴 대화 기록을 유지하며 일관되고 개인화된 응답을 제공할 수 있게 되었습니다. 그러나 이는 대화 길이에 따라 선형적으로 증가하는 메모리 문제를 야기하는 Key-Value(KV) 캐싱에 의존합니다. 이를 해결하기 위해 KV 캐시 압축이 연구되고 있지만, 기존 방법은 메모리 사용량 문제와 정확도 저하 문제를 겪고 있습니다. 본 논문에서는 고정된 메모리 환경에서 긴 대화형 질문 응답(LongConvQA)을 위한 EpiCache라는 새로운 KV 캐시 관리 프레임워크를 제안합니다. EpiCache는 블록 단위의 프리필과 에피소드별 KV 압축을 통해 캐시 성장을 제한하고, 대화 기록을 일관된 에피소드로 클러스터링하여 주제 관련 컨텍스트를 유지합니다. 또한, 각 레이어의 민감도를 측정하여 메모리 예산을 적절히 분배하는 적응형 레이어 예산 할당 전략을 설계했습니다. 세 가지 LongConvQA 벤치마크에서 EpiCache는 기존 기준보다 최대 40% 정확도를 향상시키고, 4-6배 압축에서도 거의 완전한 KV 정확도를 유지하며, 지연 시간과 메모리를 최대 2.4배 및 3.5배 줄여 자원 제약 하에서 효율적인 다중 턴 상호작용을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 발전으로 맥락 길이가 확장되어, 개인화된 응답을 위한 긴 대화 기록을 유지할 수 있게 되었다.
- 2. KV 캐시 압축은 메모리 사용량을 줄이면서도 정확성을 유지하기 위한 연구로, 기존 방법들은 메모리 사용량의 한계를 극복하지 못하고 있다.
- 3. EpiCache는 고정된 메모리 예산 하에서 긴 대화형 질문 응답(LongConvQA)을 위한 훈련이 필요 없는 KV 캐시 관리 프레임워크를 제안한다.
- 4. EpiCache는 블록 단위의 프리필과 에피소드별 KV 압축을 통해 캐시 성장을 제한하고, 주제 관련 맥락을 유지한다.
- 5. EpiCache는 세 가지 LongConvQA 벤치마크에서 최대 40%의 정확도 향상과 4-6배의 압축 하에서도 거의 완전한 KV 정확성을 유지하며, 지연 시간과 메모리를 최대 2.4배 및 3.5배까지 줄인다.


---

*Generated on 2025-09-24 03:24:21*