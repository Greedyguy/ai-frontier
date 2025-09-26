---
keywords:
  - Exact Positional Embeddings
  - Transformer
  - Positional Encoding
  - Causal Language Modeling
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19569
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:43:10.325348",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Exact Positional Embeddings",
    "Transformer",
    "Positional Encoding",
    "Causal Language Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Exact Positional Embeddings": 0.92,
    "Transformer": 0.85,
    "Positional Encoding": 0.8,
    "Causal Language Modeling": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Exact Positional Embeddings",
        "canonical": "Exact Positional Embeddings",
        "aliases": [
          "ExPE"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for positional encoding that enhances transformer models' extrapolation capabilities.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "Transformer Models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on enhancing transformer models with new positional embeddings.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Positional Encoding",
        "canonical": "Positional Encoding",
        "aliases": [
          "Position Embeddings"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in improving the model's ability to handle longer sequences.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Language Modeling",
        "canonical": "Causal Language Modeling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Relevant to the application of the proposed embeddings in reducing perplexity.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "embedding vectors",
      "token positions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Exact Positional Embeddings",
      "resolved_canonical": "Exact Positional Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Transformer Models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Positional Encoding",
      "resolved_canonical": "Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Language Modeling",
      "resolved_canonical": "Causal Language Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# ExPe: Exact Positional Encodings for Generative Transformer Models with Extrapolating Capabilities

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19569.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19569](https://arxiv.org/abs/2509.19569)

## 🔗 유사한 논문
- [[2025-09-23/Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features_20250923|Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features]] (85.6% similar)
- [[2025-09-23/Context-aware Biases for Length Extrapolation_20250923|Context-aware Biases for Length Extrapolation]] (81.7% similar)
- [[2025-09-22/Positional Encoding in Transformer-Based Time Series Models_ A Survey_20250922|Positional Encoding in Transformer-Based Time Series Models: A Survey]] (80.6% similar)
- [[2025-09-19/DyWPE_ Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers_20250919|DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers]] (80.5% similar)
- [[2025-09-23/Proxy-Embedding as an Adversarial Teacher_ An Embedding-Guided Bidirectional Attack for Referring Expression Segmentation Models_20250923|Proxy-Embedding as an Adversarial Teacher: An Embedding-Guided Bidirectional Attack for Referring Expression Segmentation Models]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Positional Encoding|Positional Encoding]], [[keywords/Causal Language Modeling|Causal Language Modeling]]
**⚡ Unique Technical**: [[keywords/Exact Positional Embeddings|Exact Positional Embeddings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19569v1 Announce Type: new 
Abstract: This paper introduces a novel approach to position embeddings in transformer models, named "Exact Positional Embeddings" (ExPE). An absolute positional embedding method that can extrapolate to sequences of lengths longer than the ones it was trained on. Traditional transformer models rely on absolute or relative position embeddings to incorporate positional information into token embeddings, which often struggle with extrapolation to sequences longer than those seen during training. Our proposed method utilizes a novel embedding strategy that encodes exact positional information by overriding specific dimensions of the embedding vectors, thereby enabling a more precise representation of token positions. The proposed approach not only maintains the integrity of the original embeddings but also enhances the model's ability to generalize to more extended sequences. In causal language modeling, our ExPE embeddings significantly reduce perplexity compared to rotary and sinusoidal embeddings, when tested on sequences longer than those used in training.

## 📝 요약

이 논문은 "정확한 위치 임베딩(ExPE)"이라는 새로운 위치 임베딩 방법을 소개합니다. ExPE는 훈련된 시퀀스보다 더 긴 시퀀스에 대해 외삽할 수 있는 절대 위치 임베딩 방법입니다. 기존의 트랜스포머 모델은 절대 또는 상대 위치 임베딩을 사용하여 위치 정보를 통합하지만, 긴 시퀀스에 대한 일반화에 어려움을 겪습니다. 제안된 방법은 임베딩 벡터의 특정 차원을 재정의하여 정확한 위치 정보를 인코딩함으로써 토큰 위치를 더 정밀하게 표현합니다. 이 접근법은 원래 임베딩의 무결성을 유지하면서도 더 긴 시퀀스에 대한 일반화 능력을 향상시킵니다. 인과적 언어 모델링에서 ExPE 임베딩은 훈련 시 사용된 시퀀스보다 긴 시퀀스에 대해 회전 및 사인 임베딩보다 당혹도를 크게 줄였습니다.

## 🎯 주요 포인트

- 1. "Exact Positional Embeddings" (ExPE)라는 새로운 위치 임베딩 방법을 제안합니다.
- 2. ExPE는 훈련 시 사용된 시퀀스보다 더 긴 시퀀스에 대해 외삽할 수 있는 절대 위치 임베딩 방법입니다.
- 3. 제안된 방법은 임베딩 벡터의 특정 차원을 재정의하여 정확한 위치 정보를 인코딩합니다.
- 4. ExPE는 원래 임베딩의 무결성을 유지하면서 더 긴 시퀀스에 대한 일반화 능력을 향상시킵니다.
- 5. 인과적 언어 모델링에서 ExPE 임베딩은 훈련에 사용된 시퀀스보다 긴 시퀀스에 대해 회전 및 사인파 임베딩보다 당혹도를 크게 줄입니다.


---

*Generated on 2025-09-26 08:43:10*