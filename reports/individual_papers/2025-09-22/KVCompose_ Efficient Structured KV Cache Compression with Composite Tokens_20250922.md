---
keywords:
  - Large Language Model
  - KV Cache Compression
  - Attention Mechanism
  - Composite Tokens
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.05165
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:11:17.227846",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "KV Cache Compression",
    "Attention Mechanism",
    "Composite Tokens"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "KV Cache Compression": 0.7,
    "Attention Mechanism": 0.8,
    "Composite Tokens": 0.65
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
        "rationale": "Large Language Models are central to the paper's focus on KV cache compression, linking to broader discussions in NLP and AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "KV Cache Compression",
        "canonical": "KV Cache Compression",
        "aliases": [
          "Key-Value Cache Compression"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical concept introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanism is a key component in the proposed method for estimating token importance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Composite Tokens",
        "canonical": "Composite Tokens",
        "aliases": [
          "Composite Token"
        ],
        "category": "unique_technical",
        "rationale": "Composite Tokens are a novel concept in the paper, essential for the proposed KV cache compression strategy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "approach"
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
      "candidate_surface": "KV Cache Compression",
      "resolved_canonical": "KV Cache Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Composite Tokens",
      "resolved_canonical": "Composite Tokens",
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

# KVCompose: Efficient Structured KV Cache Compression with Composite Tokens

**Korean Title:** KVCompose: 복합 토큰을 활용한 효율적인 구조적 KV 캐시 압축

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.05165.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.05165](https://arxiv.org/abs/2509.05165)

## 🔗 유사한 논문
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (89.9% similar)
- [[2025-09-22/UniGist_ Towards General and Hardware-aligned Sequence-level Long Context Compression_20250922|UniGist: Towards General and Hardware-aligned Sequence-level Long Context Compression]] (84.9% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (83.3% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (83.2% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/KV Cache Compression|KV Cache Compression]], [[keywords/Composite Tokens|Composite Tokens]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.05165v2 Announce Type: replace 
Abstract: Large language models (LLMs) rely on key-value (KV) caches for efficient autoregressive decoding; however, cache size grows linearly with context length and model depth, becoming a major bottleneck in long-context inference. Prior KV cache compression methods either enforce rigid heuristics, disrupt tensor layouts with per-attention-head variability, or require specialized compute kernels.
  We propose a simple, yet effective, KV cache compression framework based on attention-guided, layer-adaptive composite tokens. Our method aggregates attention scores to estimate token importance, selects head-specific tokens independently, and aligns them into composite tokens that respect the uniform cache structure required by existing inference engines. A global allocation mechanism further adapts retention budgets across layers, assigning more capacity to layers with informative tokens. This approach achieves significant memory reduction while preserving accuracy, consistently outperforming prior structured and semi-structured methods. Crucially, our approach remains fully compatible with standard inference pipelines, offering a practical and scalable solution for efficient long-context LLM deployment.

## 🔍 Abstract (한글 번역)

arXiv:2509.05165v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)은 효율적인 자기회귀 디코딩을 위해 키-값(KV) 캐시를 활용하지만, 캐시 크기는 문맥 길이와 모델 깊이에 따라 선형적으로 증가하여 긴 문맥 추론에서 주요 병목 현상이 됩니다. 이전의 KV 캐시 압축 방법들은 엄격한 휴리스틱을 강요하거나, 주의 헤드별 가변성으로 인해 텐서 레이아웃을 방해하거나, 특수한 계산 커널을 요구합니다.  
우리는 주의 기반, 계층 적응형 복합 토큰에 기반한 간단하면서도 효과적인 KV 캐시 압축 프레임워크를 제안합니다. 우리의 방법은 주의 점수를 집계하여 토큰의 중요성을 추정하고, 헤드별로 독립적으로 토큰을 선택하며, 기존 추론 엔진이 요구하는 균일한 캐시 구조를 준수하는 복합 토큰으로 정렬합니다. 전역 할당 메커니즘은 계층 간 유지 예산을 조정하여 정보가 많은 토큰을 가진 계층에 더 많은 용량을 할당합니다. 이 접근 방식은 정확성을 유지하면서도 메모리 사용량을 크게 줄이며, 이전의 구조적 및 반구조적 방법들을 일관되게 능가합니다. 무엇보다도, 우리의 접근 방식은 표준 추론 파이프라인과 완전히 호환되며, 효율적인 긴 문맥 LLM 배포를 위한 실용적이고 확장 가능한 솔루션을 제공합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 효율적인 오토리그레시브 디코딩을 위한 KV 캐시 압축 방법을 제안합니다. 기존 방법들이 고정된 규칙을 강요하거나 특수한 계산 커널을 요구하는 반면, 제안된 방법은 주의 기반의 레이어 적응형 복합 토큰을 사용하여 캐시를 압축합니다. 주의 점수를 통해 토큰 중요도를 추정하고, 각 헤드별로 독립적으로 토큰을 선택하여 기존 추론 엔진과 호환되는 구조를 유지합니다. 또한, 글로벌 할당 메커니즘을 통해 레이어별로 정보가 많은 토큰에 더 많은 용량을 할당합니다. 이 방법은 메모리 사용량을 크게 줄이면서도 정확성을 유지하며, 기존 방법들보다 우수한 성능을 보입니다. 특히, 표준 추론 파이프라인과 완벽하게 호환되어 실용적이고 확장 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 효율적인 오토리그레시브 디코딩을 위해 사용되는 KV 캐시는 문맥 길이와 모델 깊이에 따라 선형적으로 증가하여 긴 문맥 추론에서 주요 병목 현상이 된다.
- 2. 기존의 KV 캐시 압축 방법은 엄격한 휴리스틱을 적용하거나, 주의 헤드별 변동성으로 텐서 레이아웃을 방해하거나, 특수한 계산 커널을 요구한다.
- 3. 제안된 방법은 주의 기반, 계층 적응형 복합 토큰을 사용하여 간단하면서도 효과적인 KV 캐시 압축 프레임워크를 제공한다.
- 4. 이 방법은 주의 점수를 집계하여 토큰 중요도를 추정하고, 헤드별로 독립적으로 토큰을 선택하여 기존 추론 엔진이 요구하는 균일한 캐시 구조에 맞게 복합 토큰으로 정렬한다.
- 5. 제안된 접근 방식은 메모리 절감을 이루면서도 정확성을 유지하며, 기존의 구조적 및 반구조적 방법을 일관되게 능가한다.


---

*Generated on 2025-09-23 11:11:17*