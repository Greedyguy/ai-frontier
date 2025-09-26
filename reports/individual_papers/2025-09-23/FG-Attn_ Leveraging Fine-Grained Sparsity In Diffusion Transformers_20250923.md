---
keywords:
  - Transformer
  - FG-Attn
  - Attention Mechanism
  - Video Diffusion Models
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16518
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:25:54.580041",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "FG-Attn",
    "Attention Mechanism",
    "Video Diffusion Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.8,
    "FG-Attn": 0.7,
    "Attention Mechanism": 0.78,
    "Video Diffusion Models": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Transformer",
        "aliases": [
          "Diffusion Transformer"
        ],
        "category": "broad_technical",
        "rationale": "This connects to the broader concept of Transformers, which are central to the paper's focus on video generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "FG-Attn",
        "canonical": "FG-Attn",
        "aliases": [
          "Fine-Grained Attention"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel attention mechanism specific to the paper, enhancing understanding of fine-grained sparsity.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Sparse Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Sparse Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of Attention Mechanism, a key component in neural network architectures.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Video Diffusion Models",
        "canonical": "Video Diffusion Models",
        "aliases": [
          "Video Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "Specifically addresses the application of diffusion models in video generation, a unique aspect of the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.68
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
      "candidate_surface": "Diffusion Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "FG-Attn",
      "resolved_canonical": "FG-Attn",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Sparse Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Video Diffusion Models",
      "resolved_canonical": "Video Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16518.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16518](https://arxiv.org/abs/2509.16518)

## 🔗 유사한 논문
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (84.3% similar)
- [[2025-09-23/70% Size, 100% Accuracy_ Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float_20250923|70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float]] (83.0% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (82.4% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (82.3% similar)
- [[2025-09-23/Optimizing Inference in Transformer-Based Models_ A Multi-Method Benchmark_20250923|Optimizing Inference in Transformer-Based Models: A Multi-Method Benchmark]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/FG-Attn|FG-Attn]], [[keywords/Video Diffusion Models|Video Diffusion Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16518v1 Announce Type: new 
Abstract: Generating realistic videos with diffusion transformers demands significant computation, with attention layers the central bottleneck; even producing a short clip requires running a transformer over a very long sequence of embeddings, e.g., more than 30K embeddings for a 5-second video, incurring significant latency. Prior work aims to mitigate this bottleneck by exploiting sparsity in the attention layers to reduce computation. However, these works typically rely on block-sparse attention, which skips score computation only when all entries in a block of attention scores (corresponding to M queries and M keys, with M = 64 typically) are zero. This coarse-granular skipping of attention scores does not fully exploit sparsity in the attention map and leaves room for improvement. In this work, we propose FG-Attn, a sparse attention mechanism for long-context diffusion transformers that leverages sparsity at a fine granularity. Unlike block-sparse attention, which skips entire MxM blocks, our approach skips computations at the granularity of Mx1 slices of the attention map. Each slice is produced by query-key dot products between a block of query vectors and a single key. To implement our proposed sparse attention mechanism, we develop a new efficient bulk-load operation called asynchronous-gather load. This load operation gathers a sparse set of relevant key-value vectors from memory and arranges them into packed tiles in the GPU's shared memory. Only a sparse set of keys relevant to those queries are loaded into shared memory when computing attention for a block of queries, in contrast to loading full blocks of key tokens in block-sparse attention. Our fine-grained sparse attention, applied to video diffusion models, achieves an average 1.55X (up to 1.65X) speedup for 5 second, 480p videos, and an average 1.41X (up to 1.49X) for 5 second, 720p videos on a single H100 GPU.

## 📝 요약

이 논문은 긴 문맥을 처리하는 확산 변환기에서 주의 메커니즘의 계산량을 줄이기 위한 FG-Attn이라는 세밀한 희소 주의 메커니즘을 제안합니다. 기존의 블록 희소 주의 메커니즘은 MxM 블록 단위로 계산을 건너뛰지만, FG-Attn은 Mx1 슬라이스 단위로 계산을 건너뛰어 더 세밀하게 희소성을 활용합니다. 이를 위해 비동기 수집 로드라는 새로운 효율적 로드 작업을 개발하여, 관련 키-값 벡터만을 GPU의 공유 메모리에 불러옵니다. 이 방법은 5초 길이의 480p 비디오에서 평균 1.55배, 720p 비디오에서 평균 1.41배의 속도 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. FG-Attn은 긴 문맥을 처리하는 확산 변환기에서 세밀한 수준의 희소성을 활용하여 주의 메커니즘의 효율성을 개선합니다.
- 2. 기존의 블록 희소 주의 메커니즘과 달리, FG-Attn은 Mx1 슬라이스 단위로 계산을 건너뛰어 주의 맵의 희소성을 더 잘 활용합니다.
- 3. 비동기 수집 로드라는 새로운 효율적인 벌크 로드 작업을 개발하여, 메모리에서 관련 키-값 벡터를 수집하고 GPU의 공유 메모리에 배치합니다.
- 4. FG-Attn을 비디오 확산 모델에 적용하면, 5초 길이의 480p 비디오에서 평균 1.55배(최대 1.65배), 720p 비디오에서 평균 1.41배(최대 1.49배) 속도 향상을 달성합니다.


---

*Generated on 2025-09-24 04:25:54*