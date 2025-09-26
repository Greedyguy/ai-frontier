---
keywords:
  - Neural Attention Search
  - Transformer
  - Attention Mechanism
  - Key-Value Cache
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.13251
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:47:40.502354",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Attention Search",
    "Transformer",
    "Attention Mechanism",
    "Key-Value Cache"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Attention Search": 0.88,
    "Transformer": 0.8,
    "Attention Mechanism": 0.78,
    "Key-Value Cache": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Attention Search",
        "canonical": "Neural Attention Search",
        "aliases": [
          "NAtS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for token importance evaluation in sequences, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Core technology used in the framework, linking to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the framework's operation, facilitating connections with other attention-based methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "KV cache",
        "canonical": "Key-Value Cache",
        "aliases": [
          "KV cache"
        ],
        "category": "unique_technical",
        "rationale": "Key component in reducing inference costs, relevant for efficiency-focused research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "sequence",
      "token",
      "step"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Attention Search",
      "resolved_canonical": "Neural Attention Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "KV cache",
      "resolved_canonical": "Key-Value Cache",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Neural Attention Search

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13251.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.13251](https://arxiv.org/abs/2502.13251)

## 🔗 유사한 논문
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (82.4% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (81.0% similar)
- [[2025-09-22/Walk and Read Less_ Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning_20250922|Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning]] (80.8% similar)
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC): A Cognitive-Inspired Approach for Attention Management in Transformers]] (80.4% similar)
- [[2025-09-17/Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions_20250917|Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Neural Attention Search|Neural Attention Search]], [[keywords/Key-Value Cache|Key-Value Cache]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13251v3 Announce Type: replace-cross 
Abstract: We present Neural Attention Search (NAtS), a framework that automatically evaluates the importance of each token within a sequence and determines if the corresponding token can be dropped after several steps. This approach can efficiently reduce the KV cache sizes required by transformer-based models during inference and thus reduce inference costs. In this paper, we design a search space that contains three token types: (i) Global Tokens will be preserved and queried by all the following tokens. (ii) Local Tokens survive until the next global token appears. (iii) Sliding Window Tokens have an impact on the inference of a fixed size of the next following tokens. Similar to the One-Shot Neural Architecture Search approach, this token-type information can be learned jointly with the architecture weights via a learnable attention mask. Experiments on both training a new transformer from scratch and fine-tuning existing large language models show that NAtS can efficiently reduce the KV cache size required for the models while maintaining the models' performance.

## 📝 요약

Neural Attention Search (NAtS)는 시퀀스 내 각 토큰의 중요성을 자동으로 평가하고, 특정 단계 이후 해당 토큰을 삭제할 수 있는지를 결정하는 프레임워크입니다. 이를 통해 트랜스포머 기반 모델의 추론 시 필요한 KV 캐시 크기를 효율적으로 줄여 추론 비용을 절감할 수 있습니다. NAtS는 글로벌 토큰, 로컬 토큰, 슬라이딩 윈도우 토큰의 세 가지 토큰 유형을 포함하는 검색 공간을 설계하여, 학습 가능한 주의 마스크를 통해 아키텍처 가중치와 함께 토큰 유형 정보를 학습할 수 있습니다. 새로운 트랜스포머를 처음부터 학습하거나 기존 대형 언어 모델을 미세 조정하는 실험에서 NAtS는 모델 성능을 유지하면서도 필요한 KV 캐시 크기를 효과적으로 줄일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. Neural Attention Search (NAtS)는 시퀀스 내 각 토큰의 중요성을 자동으로 평가하여 불필요한 토큰을 제거하는 프레임워크입니다.
- 2. NAtS는 추론 시 필요한 KV 캐시 크기를 줄여 추론 비용을 절감할 수 있습니다.
- 3. 세 가지 토큰 유형(글로벌, 로컬, 슬라이딩 윈도우)을 포함한 검색 공간을 설계하여 효율성을 높였습니다.
- 4. 학습 가능한 주의 마스크를 통해 토큰 유형 정보를 아키텍처 가중치와 함께 학습할 수 있습니다.
- 5. 실험 결과, NAtS는 모델 성능을 유지하면서도 KV 캐시 크기를 효율적으로 줄일 수 있음을 보여주었습니다.


---

*Generated on 2025-09-24 00:47:40*