---
keywords:
  - Attention Mechanism
  - Large Language Model
  - KV-caching
  - query-key normalization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.00919
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:44:09.305461",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Large Language Model",
    "KV-caching",
    "query-key normalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.8,
    "Large Language Model": 0.85,
    "KV-caching": 0.7,
    "query-key normalization": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "attention sinks",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention sink"
        ],
        "category": "specific_connectable",
        "rationale": "Attention sinks are a specific aspect of the attention mechanism, crucial for understanding model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large language model"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and connect to various advanced topics in NLP.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "KV-caching",
        "canonical": "KV-caching",
        "aliases": [
          "key-value caching"
        ],
        "category": "unique_technical",
        "rationale": "KV-caching is a unique technical concept essential for understanding memory efficiency in models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "query-key normalization",
        "canonical": "query-key normalization",
        "aliases": [
          "QK normalization"
        ],
        "category": "unique_technical",
        "rationale": "Query-key normalization is a novel concept that affects attention distribution in models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "tokens",
      "sequence",
      "model performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "attention sinks",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "KV-caching",
      "resolved_canonical": "KV-caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "query-key normalization",
      "resolved_canonical": "query-key normalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Attention Sinks: A 'Catch, Tag, Release' Mechanism for Embeddings

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.00919.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.00919](https://arxiv.org/abs/2502.00919)

## 🔗 유사한 논문
- [[2025-09-23/Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models_20250923|Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models]] (82.5% similar)
- [[2025-09-22/Tag&Tab_ Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack_20250922|Tag&Tab: Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack]] (81.3% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (81.1% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (80.1% similar)
- [[2025-09-22/Causal2Vec_ Improving Decoder-only LLMs as Versatile Embedding Models_20250922|Causal2Vec: Improving Decoder-only LLMs as Versatile Embedding Models]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/KV-caching|KV-caching]], [[keywords/query-key normalization|query-key normalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.00919v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) often concentrate their attention on a few specific tokens referred to as attention sinks. Common examples include the first token, a prompt-independent sink, and punctuation tokens, which are prompt-dependent. While the tokens causing the sinks often lack direct semantic meaning, the presence of the sinks is critical for model performance, particularly under model compression and KV-caching. Despite their ubiquity, the function, semantic role, and origin of attention sinks -- especially those beyond the first token -- remain poorly understood. In this work, we conduct a comprehensive investigation demonstrating that attention sinks: catch a sequence of tokens, tag them using a common direction in embedding space, and release them back into the residual stream, where tokens are later retrieved based on the tags they have acquired. Probing experiments reveal these tags carry semantically meaningful information, such as the truth of a statement. These findings extend to reasoning models, where the mechanism spans more heads and explains greater variance in embeddings, or recent models with query-key normalization, where sinks remain just as prevalent. To encourage future theoretical analysis, we introduce a minimal problem which can be solved through the 'catch, tag, release' mechanism, and where it emerges through training.

## 📝 요약

이 논문은 대형 언어 모델(LLMs)에서 주의가 집중되는 특정 토큰인 '주의 싱크'에 대한 연구를 다룹니다. 주의 싱크는 모델 성능, 특히 모델 압축과 KV-캐싱에서 중요한 역할을 하지만, 그 기능과 기원은 잘 알려져 있지 않습니다. 연구는 주의 싱크가 토큰을 잡아 공통 방향으로 태그를 붙이고, 나중에 태그를 기반으로 토큰을 회수하는 과정을 통해 의미 있는 정보를 전달한다는 것을 보여줍니다. 이러한 메커니즘은 추론 모델에서도 확장되며, 최근의 쿼리-키 정규화 모델에서도 여전히 중요합니다. 연구는 '잡기, 태그, 방출' 메커니즘을 통해 해결할 수 있는 최소 문제를 제시하여 이론적 분석을 장려합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 주로 특정 토큰에 집중하는 경향이 있으며, 이를 주의 싱크라고 부릅니다.
- 2. 주의 싱크는 모델 성능에 중요한 역할을 하며, 특히 모델 압축과 KV-캐싱에서 중요합니다.
- 3. 주의 싱크는 토큰을 잡아내고, 공통의 방향으로 태그를 부여한 후, 잔여 스트림으로 다시 방출합니다.
- 4. 실험 결과, 이러한 태그는 명제의 진실성과 같은 의미 있는 정보를 포함하고 있음이 밝혀졌습니다.
- 5. 우리는 '잡기, 태그하기, 방출하기' 메커니즘을 통해 해결할 수 있는 최소 문제를 제안하여 이론적 분석을 장려합니다.


---

*Generated on 2025-09-24 00:44:09*