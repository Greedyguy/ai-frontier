---
keywords:
  - Speculative Decoding
  - Cache-Assisted Parallel Speculative Decoding
  - Large Language Model
  - Query-and-Correct Paradigm
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2508.04462
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:10:52.397771",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Speculative Decoding",
    "Cache-Assisted Parallel Speculative Decoding",
    "Large Language Model",
    "Query-and-Correct Paradigm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Speculative Decoding": 0.78,
    "Cache-Assisted Parallel Speculative Decoding": 0.8,
    "Large Language Model": 0.7,
    "Query-and-Correct Paradigm": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Speculative Decoding",
        "canonical": "Speculative Decoding",
        "aliases": [
          "SD"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to LLM inference that can be linked to advancements in decoding methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cache-Assisted Parallel Speculative Decoding",
        "canonical": "Cache-Assisted Parallel Speculative Decoding",
        "aliases": [
          "CARD"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific framework that enhances speculative decoding, offering a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Fundamental to the paper's context, connecting to a wide range of research in language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Query-and-Correct Paradigm",
        "canonical": "Query-and-Correct Paradigm",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes a novel paradigm that differentiates the proposed method from existing approaches.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "draft model",
      "target model",
      "vanilla autoregressive decoding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Speculative Decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cache-Assisted Parallel Speculative Decoding",
      "resolved_canonical": "Cache-Assisted Parallel Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Query-and-Correct Paradigm",
      "resolved_canonical": "Query-and-Correct Paradigm",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference

**Korean Title:** CARD: 쿼리 및 수정 패러다임을 통한 캐시 지원 병렬 추측 디코딩 프레임워크를 활용한 LLM 추론 가속화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.04462.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2508.04462](https://arxiv.org/abs/2508.04462)

## 🔗 유사한 논문
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (83.7% similar)
- [[2025-09-22/Cross-Attention Speculative Decoding_20250922|Cross-Attention Speculative Decoding]] (83.2% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (82.8% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (82.7% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/Cache-Assisted Parallel Speculative Decoding|Cache-Assisted Parallel Speculative Decoding]], [[keywords/Query-and-Correct Paradigm|Query-and-Correct Paradigm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.04462v2 Announce Type: replace 
Abstract: Speculative decoding (SD), where a draft model provides multiple candidate tokens for the target model to verify in parallel, has demonstrated significant potential for accelerating LLM inference. Yet, existing SD approaches adhere to a strict draft-then-verify paradigm, enforcing a sequential process that hampers performance and constrains the draft model's capacity. Moreover, rejecting a token in the candidate sequence invalidates all subsequent tokens, leading to wasted computation during drafting. To overcome these limitations, we propose a cache-assisted parallel speculative decoding framework called CARD, which employs a novel query-and-correct paradigm. Our approach decouples drafting from verification: the draft model populates a shared cache with candidate tokens, while the target model concurrently refines the draft's trajectory. This enables inference at near-draft-speed, effectively leveraging the draft model's efficiency without additional fine-tuning. Experimental results show that CARD significantly outperforms existing state-of-the-art methods, achieving up to a 4.83x acceleration over vanilla autoregressive decoding, with no fine-tuning required for either models.

## 🔍 Abstract (한글 번역)

arXiv:2508.04462v2 발표 유형: 교체  
초록: 추론 모델이 여러 후보 토큰을 제공하고 대상 모델이 이를 병렬로 검증하는 추측 디코딩(Speculative Decoding, SD)은 대형 언어 모델(LLM) 추론을 가속화하는 데 상당한 잠재력을 보여주었습니다. 그러나 기존의 SD 접근 방식은 엄격한 초안 작성 후 검증 패러다임을 따르며, 이는 성능을 저해하고 초안 모델의 역량을 제한합니다. 게다가, 후보 시퀀스에서 토큰을 거부하면 이후의 모든 토큰이 무효화되어 초안 작성 중에 계산이 낭비됩니다. 이러한 제한을 극복하기 위해, 우리는 새로운 쿼리 및 수정 패러다임을 사용하는 캐시 지원 병렬 추측 디코딩 프레임워크인 CARD를 제안합니다. 우리의 접근 방식은 초안 작성과 검증을 분리합니다: 초안 모델은 후보 토큰으로 공유 캐시를 채우고, 대상 모델은 동시에 초안의 경로를 수정합니다. 이는 초안 속도에 가까운 추론을 가능하게 하여, 추가적인 미세 조정 없이 초안 모델의 효율성을 효과적으로 활용합니다. 실험 결과, CARD는 기존 최첨단 방법을 크게 능가하며, 기본 자동회귀 디코딩에 비해 최대 4.83배의 가속을 달성하며, 두 모델 모두에 대해 미세 조정이 필요하지 않습니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM) 추론을 가속화하기 위한 새로운 방법론인 카드(CARD)를 제안합니다. 기존의 추론 방식은 초안 생성 후 검증하는 순차적 과정으로, 성능 저하와 자원 낭비가 발생합니다. 카드(CARD)는 초안 생성과 검증을 분리하여, 초안 모델이 후보 토큰을 캐시에 저장하고 목표 모델이 이를 동시 검증하는 구조를 채택합니다. 이를 통해 초안 속도에 가까운 추론이 가능하며, 추가적인 모델 튜닝 없이도 효율성을 극대화합니다. 실험 결과, 카드(CARD)는 기존 방법보다 최대 4.83배 빠른 속도를 달성했습니다.

## 🎯 주요 포인트

- 1. 기존의 추론 모델은 엄격한 초안-검증 절차를 따르며 성능을 저해하고 초안 모델의 역량을 제한한다.
- 2. 제안된 CARD 프레임워크는 초안과 검증을 분리하여 병렬 추론을 가능하게 한다.
- 3. CARD는 공유 캐시를 활용하여 초안 모델의 효율성을 극대화하고 검증 모델이 초안의 경로를 동시에 수정할 수 있도록 한다.
- 4. 실험 결과, CARD는 기존 최첨단 방법보다 최대 4.83배 빠른 추론 속도를 달성하며, 추가적인 모델 미세 조정이 필요 없다.


---

*Generated on 2025-09-23 11:10:52*