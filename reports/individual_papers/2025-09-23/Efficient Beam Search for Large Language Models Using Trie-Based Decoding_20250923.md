---
keywords:
  - Large Language Model
  - Trie-Based Decoding
  - Attention Mechanism
  - Memory-Constrained Environments
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2502.00085
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:47:26.475473",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Trie-Based Decoding",
    "Attention Mechanism",
    "Memory-Constrained Environments"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Trie-Based Decoding": 0.8,
    "Attention Mechanism": 0.78,
    "Memory-Constrained Environments": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving decoding efficiency for large-scale models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Trie-Based Decoding",
        "canonical": "Trie-Based Decoding",
        "aliases": [
          "Prefix-Tree Decoding"
        ],
        "category": "unique_technical",
        "rationale": "Describes the novel method introduced in the paper, crucial for understanding the proposed efficiency improvements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-Head Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "MHA"
        ],
        "category": "specific_connectable",
        "rationale": "A key component of the architectures evaluated, linking to broader attention mechanism studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Memory-Constrained Environments",
        "canonical": "Memory-Constrained Environments",
        "aliases": [
          "Low-Memory Settings"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the practical application context of the method, relevant for deployment scenarios.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
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
      "candidate_surface": "Trie-Based Decoding",
      "resolved_canonical": "Trie-Based Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-Head Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Memory-Constrained Environments",
      "resolved_canonical": "Memory-Constrained Environments",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Efficient Beam Search for Large Language Models Using Trie-Based Decoding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.00085.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2502.00085](https://arxiv.org/abs/2502.00085)

## 🔗 유사한 논문
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (84.8% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (84.8% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (83.1% similar)
- [[2025-09-23/SEDM_ Scalable Self-Evolving Distributed Memory for Agents_20250923|SEDM: Scalable Self-Evolving Distributed Memory for Agents]] (82.3% similar)
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Trie-Based Decoding|Trie-Based Decoding]], [[keywords/Memory-Constrained Environments|Memory-Constrained Environments]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.00085v2 Announce Type: replace 
Abstract: This work presents a novel trie (prefix-tree)-based parallel decoding method that addresses the memory inefficiency of batch-based beam search. By sharing a single KV cache across beams with common prefixes, our approach dramatically reduces memory usage and enables efficient decoding. We evaluated our method across three attention architectures, Multi-Head Attention (Phi-3.5-mini-instruct), Grouped Query Attention (Llama-3.1-8B-Instruct), and Sliding Window Attention (Mistral-Small-24B-Instruct-2501), using CNN/DailyMail for abstractive summarization and HumanEval for code generation. Our experiments demonstrate substantial memory savings (4--8$\times$) and up to 2.4$\times$ faster decoding, without compromising generation quality. These results highlight our method's suitability for memory-constrained environments and large-scale deployments.

## 📝 요약

이 논문은 배치 기반 빔 서치의 메모리 비효율성을 해결하기 위해 새로운 트라이 기반 병렬 디코딩 방법을 제안합니다. 공통 접두사를 가진 빔들 간에 단일 KV 캐시를 공유함으로써 메모리 사용량을 크게 줄이고 효율적인 디코딩을 가능하게 합니다. Multi-Head Attention, Grouped Query Attention, Sliding Window Attention 등 세 가지 주의 메커니즘을 사용하여 CNN/DailyMail과 HumanEval 데이터셋에서 실험한 결과, 메모리 사용량을 4~8배 절감하고 디코딩 속도를 최대 2.4배 향상시켰으며, 생성 품질은 유지되었습니다. 이 방법은 메모리 제약이 있는 환경과 대규모 배포에 적합함을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 배치 기반 빔 서치의 메모리 비효율성을 해결하기 위한 새로운 트라이 기반 병렬 디코딩 방법을 제안합니다.
- 2. 공통 접두사를 가진 빔 간에 단일 KV 캐시를 공유함으로써 메모리 사용량을 크게 줄이고 효율적인 디코딩을 가능하게 합니다.
- 3. Multi-Head Attention, Grouped Query Attention, Sliding Window Attention 등 세 가지 주의 메커니즘을 대상으로 실험을 수행했습니다.
- 4. 실험 결과, 메모리 사용량을 4~8배 절감하고 디코딩 속도를 최대 2.4배 향상시키면서도 생성 품질을 유지했습니다.
- 5. 이 방법은 메모리 제약이 있는 환경과 대규모 배포에 적합하다는 점을 강조합니다.


---

*Generated on 2025-09-24 03:47:26*