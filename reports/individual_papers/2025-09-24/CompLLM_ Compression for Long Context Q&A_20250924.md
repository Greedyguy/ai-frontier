<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:45:49.025378",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Attention Mechanism",
    "Context Compression",
    "CompLLM",
    "Time To First Token"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Attention Mechanism": 0.88,
    "Context Compression": 0.8,
    "CompLLM": 0.78,
    "Time To First Token": 0.72
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
        "rationale": "Large Language Models are central to the paper's focus on context compression, linking to broader discussions in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "self-attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "self-attention"
        ],
        "category": "specific_connectable",
        "rationale": "Self-attention is a key component of Transformers, relevant for understanding the computational challenges addressed.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "context compression",
        "canonical": "Context Compression",
        "aliases": [
          "soft context compression"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel approach to context compression, which is central to its contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "CompLLM",
        "canonical": "CompLLM",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "CompLLM is the specific technique introduced in the paper, representing a unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Time To First Token",
        "canonical": "Time To First Token",
        "aliases": [
          "TTFT"
        ],
        "category": "unique_technical",
        "rationale": "Time To First Token is a performance metric used to evaluate the efficiency of the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "self-attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "context compression",
      "resolved_canonical": "Context Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "CompLLM",
      "resolved_canonical": "CompLLM",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Time To First Token",
      "resolved_canonical": "Time To First Token",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CompLLM: Compression for Long Context Q&A

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19228.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19228](https://arxiv.org/abs/2509.19228)

## 🔗 유사한 논문
- [[2025-09-23/AttnComp_ Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation_20250923|AttnComp: Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation]] (89.0% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (86.6% similar)
- [[2025-09-24/When Long Helps Short_ How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models_20250924|When Long Helps Short: How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models]] (86.2% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (85.3% similar)
- [[2025-09-24/LightThinker_ Thinking Step-by-Step Compression_20250924|LightThinker: Thinking Step-by-Step Compression]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Context Compression|Context Compression]], [[keywords/CompLLM|CompLLM]], [[keywords/Time To First Token|Time To First Token]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19228v1 Announce Type: new 
Abstract: Large Language Models (LLMs) face significant computational challenges when processing long contexts due to the quadratic complexity of self-attention. While soft context compression methods, which map input text to smaller latent representations, have shown promise, their real-world adoption is limited. Existing techniques typically compress the context as a single unit, which leads to quadratic compression complexity and an inability to reuse computations across queries with overlapping contexts. In this work, we introduce CompLLM, a soft compression technique designed for practical deployment. Instead of processing the context holistically, CompLLM divides it into segments and compresses each one independently. This simple design choice yields three critical properties: efficiency, as the compression step scales linearly with the context length; scalability, enabling models trained on short sequences (e.g., 1k tokens) to generalize to contexts of 100k tokens; and reusability, allowing compressed segments to be cached and reused across different queries. Our experiments show that with a 2x compression rate, at high context lengths CompLLM speeds up Time To First Token (TTFT) by up to 4x and reduces the KV cache size by 50%. Furthermore, CompLLM achieves performance comparable to that obtained with the uncompressed context, and even surpasses it on very long sequences, demonstrating its effectiveness and practical utility.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)이 긴 문맥을 처리할 때의 계산적 문제를 해결하기 위해 CompLLM이라는 소프트 압축 기법을 제안합니다. 기존 방법들은 문맥을 하나의 단위로 압축하여 계산 재사용이 어려웠으나, CompLLM은 문맥을 여러 세그먼트로 나누어 독립적으로 압축합니다. 이로 인해 압축 단계가 문맥 길이에 선형적으로 확장되고, 짧은 시퀀스에 훈련된 모델이 긴 문맥에 일반화할 수 있으며, 압축된 세그먼트를 캐싱하여 재사용할 수 있습니다. 실험 결과, CompLLM은 2배 압축률에서 긴 문맥 처리 시 초기 토큰 생성 시간을 최대 4배 단축하고, KV 캐시 크기를 50% 줄이며, 비압축 문맥과 유사한 성능을 보이고, 매우 긴 시퀀스에서는 이를 능가하는 성과를 보여줍니다.

## 🎯 주요 포인트

- 1. CompLLM은 문맥을 독립적인 세그먼트로 나누어 압축하여 효율성을 높이고, 압축 단계가 문맥 길이에 선형적으로 확장됩니다.
- 2. 이 기술은 짧은 시퀀스에 훈련된 모델이 100k 토큰의 긴 문맥으로 일반화할 수 있도록 확장성을 제공합니다.
- 3. 압축된 세그먼트를 캐시하여 다른 쿼리에서 재사용할 수 있는 재사용성을 제공합니다.
- 4. CompLLM은 2배 압축률로 긴 문맥에서 첫 번째 토큰 생성 시간을 최대 4배까지 단축하고 KV 캐시 크기를 50% 줄입니다.
- 5. 압축되지 않은 문맥과 비교하여 성능이 유사하거나 매우 긴 시퀀스에서는 더 뛰어난 성능을 보여줍니다.


---

*Generated on 2025-09-24 15:45:49*