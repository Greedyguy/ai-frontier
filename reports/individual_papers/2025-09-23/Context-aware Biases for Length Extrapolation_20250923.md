---
keywords:
  - Transformer
  - Relative Positional Encoding
  - Context-Aware Biases for Length Extrapolation
  - Attention Mechanism
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2503.08067
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:52:27.968250",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Relative Positional Encoding",
    "Context-Aware Biases for Length Extrapolation",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Relative Positional Encoding": 0.78,
    "Context-Aware Biases for Length Extrapolation": 0.8,
    "Attention Mechanism": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformers",
        "canonical": "Transformer",
        "aliases": [
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the paper's discussion on length extrapolation and positional encoding.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Relative Positional Encoding",
        "canonical": "Relative Positional Encoding",
        "aliases": [
          "RPE"
        ],
        "category": "specific_connectable",
        "rationale": "RPE is a key concept in addressing the paper's main problem of length extrapolation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Context-Aware Biases for Length Extrapolation",
        "canonical": "Context-Aware Biases for Length Extrapolation",
        "aliases": [
          "CABLE"
        ],
        "category": "unique_technical",
        "rationale": "CABLE is the novel method proposed in the paper, offering a unique approach to positional encoding.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention Head",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Heads"
        ],
        "category": "specific_connectable",
        "rationale": "Attention heads are crucial for understanding how CABLE modifies transformer behavior.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
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
      "candidate_surface": "Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Relative Positional Encoding",
      "resolved_canonical": "Relative Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Context-Aware Biases for Length Extrapolation",
      "resolved_canonical": "Context-Aware Biases for Length Extrapolation",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention Head",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Context-aware Biases for Length Extrapolation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.08067.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2503.08067](https://arxiv.org/abs/2503.08067)

## 🔗 유사한 논문
- [[2025-09-23/Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features_20250923|Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features]] (82.2% similar)
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (80.5% similar)
- [[2025-09-22/BEFT_ Bias-Efficient Fine-Tuning of Language Models_20250922|BEFT: Bias-Efficient Fine-Tuning of Language Models]] (80.0% similar)
- [[2025-09-23/Causally-Guided Pairwise Transformer -- Towards Foundational Digital Twins in Process Industry_20250923|Causally-Guided Pairwise Transformer -- Towards Foundational Digital Twins in Process Industry]] (79.4% similar)
- [[2025-09-23/Efficient Beam Search for Large Language Models Using Trie-Based Decoding_20250923|Efficient Beam Search for Large Language Models Using Trie-Based Decoding]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Relative Positional Encoding|Relative Positional Encoding]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Context-Aware Biases for Length Extrapolation|Context-Aware Biases for Length Extrapolation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.08067v3 Announce Type: replace 
Abstract: Transformers often struggle to generalize to longer sequences than those seen during training, a limitation known as length extrapolation. Most existing Relative Positional Encoding (RPE) methods attempt to address this by introducing either fixed linear biases or globally learned biases, which lack the capacity to adapt to different input contexts. In this work, we propose an additive RPE, Context-Aware Biases for Length Extrapolation (CABLE), a method that learns token-specific, context-aware biases for each attention head in transformers. By dynamically adjusting positional biases based on the input sequence, CABLE overcomes the rigidity of fixed RPEs. When evaluated on sequences longer than originally trained with, GPT-2 Medium (334M parameters) with CABLE achieves lower perplexity than counterparts using other widely adopted positional encoding methods. Additionally, by applying CABLE to the BERT base model we improved performance in long-context retrieval tasks. Our method significantly enhances the extrapolation performance of existing RPE methods tested on the FineWeb-Edu-10B and WikiText-103 datasets. Our code is available at: https://github.com/AlgonetLabs/Cable.

## 📝 요약

이 논문은 트랜스포머 모델의 길이 외삽 문제를 해결하기 위해 새로운 상대적 위치 인코딩(RPE) 방법인 CABLE을 제안합니다. CABLE은 각 주의 헤드에 대해 토큰별로 문맥에 맞춘 바이어스를 학습하여 입력 시퀀스에 따라 위치 바이어스를 동적으로 조정합니다. 이를 통해 기존의 고정된 RPE의 한계를 극복하고, GPT-2 Medium 모델에서 다른 위치 인코딩 방법보다 낮은 퍼플렉시티를 달성했습니다. 또한, BERT 모델에 CABLE을 적용하여 긴 문맥 검색 작업에서 성능을 향상시켰으며, FineWeb-Edu-10B 및 WikiText-103 데이터셋에서 기존 RPE 방법의 외삽 성능을 크게 개선했습니다.

## 🎯 주요 포인트

- 1. Transformer 모델의 길이 외삽 문제를 해결하기 위해 문맥 인식 바이어스를 학습하는 CABLE 방법을 제안합니다.
- 2. CABLE은 입력 시퀀스에 따라 위치 바이어스를 동적으로 조정하여 고정된 상대적 위치 인코딩(RPE)의 경직성을 극복합니다.
- 3. CABLE을 적용한 GPT-2 Medium 모델은 기존의 위치 인코딩 방법보다 긴 시퀀스에서 낮은 퍼플렉시티를 달성했습니다.
- 4. BERT base 모델에 CABLE을 적용하여 긴 문맥 검색 작업에서 성능을 향상시켰습니다.
- 5. FineWeb-Edu-10B 및 WikiText-103 데이터셋에서 기존 RPE 방법의 외삽 성능을 크게 향상시켰습니다.


---

*Generated on 2025-09-24 03:52:27*