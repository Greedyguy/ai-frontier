---
keywords:
  - Diffusion Large Language Models
  - Speculative Decoding
  - Directed Draft Graph
  - Key-Value Caching
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18085
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:20:27.792692",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Large Language Models",
    "Speculative Decoding",
    "Directed Draft Graph",
    "Key-Value Caching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Large Language Models": 0.78,
    "Speculative Decoding": 0.8,
    "Directed Draft Graph": 0.75,
    "Key-Value Caching": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion LLMs",
        "canonical": "Diffusion Large Language Models",
        "aliases": [
          "dLLMs"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel approach in language model architecture that is distinct from autoregressive models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Speculative Decoding",
        "canonical": "Speculative Decoding",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific decoding strategy that enhances the performance of language models, relevant for linking with decoding techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Directed Draft Graph",
        "canonical": "Directed Draft Graph",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel graph structure proposed for optimizing language model generation, useful for linking with graph-based methods.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "KV-caching",
        "canonical": "Key-Value Caching",
        "aliases": [
          "KV-caching"
        ],
        "category": "specific_connectable",
        "rationale": "A known technique for improving model efficiency, relevant for linking with memory optimization strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "autoregressive LLMs",
      "token generation rates",
      "output quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion LLMs",
      "resolved_canonical": "Diffusion Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Speculative Decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Directed Draft Graph",
      "resolved_canonical": "Directed Draft Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "KV-caching",
      "resolved_canonical": "Key-Value Caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18085.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18085](https://arxiv.org/abs/2509.18085)

## 🔗 유사한 논문
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (88.0% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (83.8% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (83.3% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (81.8% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Key-Value Caching|Key-Value Caching]]
**⚡ Unique Technical**: [[keywords/Diffusion Large Language Models|Diffusion Large Language Models]], [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/Directed Draft Graph|Directed Draft Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18085v1 Announce Type: cross 
Abstract: Diffusion LLMs (dLLMs) have recently emerged as a powerful alternative to autoregressive LLMs (AR-LLMs) with the potential to operate at significantly higher token generation rates. However, currently available open-source dLLMs often generate at much lower rates, typically decoding only a single token at every denoising timestep in order to maximize output quality. We present Spiffy, a speculative decoding algorithm that accelerates dLLM inference by $\mathbf{2.8{-}3.1\times}$ while provably preserving the model's output distribution. This work addresses the unique challenges involved in applying ideas from speculative decoding of AR-LLMs to the dLLM setting. Spiffy proposes draft states by leveraging the dLLM's distribution itself in an auto-speculative manner. This approach is efficient and effective, and eliminates the overheads of training and running an independent draft model. To structure the candidate draft states, we propose a novel directed draft graph which is uniquely designed to take advantage of the bidirectional, block-wise nature of dLLM generation and can be verified in parallel by the dLLM. To further optimize the structure of these draft graphs, we introduce an efficient, offline calibration algorithm that procedurally determines high-quality graph configurations. These optimized draft graphs, enabling increased acceptance rates, lead to a significant boost in the overall speedup achieved by the system. Crucially, Spiffy is also complementary to other recent innovations in improving dLLM generation speeds such as KV-caching and multi-token unmasking. We demonstrate that when combined with such parallel decoding algorithms, Spiffy is able to effectively multiply the benefits of these methods leading to total speedups of up to $\mathbf{7.9\times}$.

## 📝 요약

이 논문에서는 Spiffy라는 추측 디코딩 알고리즘을 제안하여 확산 기반 대형 언어 모델(dLLM)의 추론 속도를 2.8~3.1배 가속화하면서도 모델의 출력 분포를 유지합니다. Spiffy는 dLLM의 분포를 활용하여 자동 추측 방식으로 초안 상태를 생성하며, 독립적인 초안 모델의 훈련 및 실행 부담을 제거합니다. 또한, 양방향 블록 방식의 dLLM 생성 특성을 활용하기 위해 새로운 방향성 초안 그래프를 제안하고, 이를 병렬로 검증할 수 있도록 설계했습니다. 오프라인 보정 알고리즘을 통해 초안 그래프의 구조를 최적화하여 수용률을 높이고, 시스템의 전체 속도를 크게 향상시켰습니다. Spiffy는 KV-캐싱 및 다중 토큰 언마스킹과 같은 최신 기법과도 상호 보완적으로 작용하여 최대 7.9배의 속도 향상을 달성할 수 있습니다.

## 🎯 주요 포인트

- 1. Spiffy는 dLLM 추론 속도를 2.8-3.1배 가속화하면서 모델의 출력 분포를 보존하는 추론 알고리즘입니다.
- 2. Spiffy는 dLLM의 분포를 활용하여 자동 추론 방식으로 초안 상태를 제안하며, 독립적인 초안 모델의 훈련 및 실행 오버헤드를 제거합니다.
- 3. 제안된 방향성 초안 그래프는 dLLM 생성의 양방향, 블록 단위 특성을 활용하여 병렬 검증이 가능하도록 설계되었습니다.
- 4. 오프라인 보정 알고리즘을 통해 초안 그래프의 구조를 최적화하여 시스템의 전체 속도를 크게 향상시킵니다.
- 5. Spiffy는 KV-캐싱 및 다중 토큰 언마스킹과 같은 dLLM 생성 속도 개선 혁신과 상호 보완적으로 작용하여 최대 7.9배의 총 속도 향상을 달성합니다.


---

*Generated on 2025-09-24 00:20:27*