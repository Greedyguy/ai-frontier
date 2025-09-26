<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:26:57.274162",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Transformer",
    "Token Sparsification",
    "Attention Mechanism",
    "Generative Quality",
    "Sampling Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Transformer": 0.8,
    "Token Sparsification": 0.78,
    "Attention Mechanism": 0.82,
    "Generative Quality": 0.7,
    "Sampling Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Diffusion Transformer",
        "aliases": [
          "DiT"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific architecture discussed in the paper, crucial for understanding the context of SparseDiT.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Token Sparsification",
        "canonical": "Token Sparsification",
        "aliases": [
          "Sparse Tokens"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper to improve computational efficiency in transformers.",
        "novelty_score": 0.88,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Self-Attention"
        ],
        "category": "specific_connectable",
        "rationale": "A fundamental component in transformers, relevant for understanding architectural inefficiencies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Generative Quality",
        "canonical": "Generative Quality",
        "aliases": [
          "Generative Performance"
        ],
        "category": "unique_technical",
        "rationale": "Key aspect of the paper's focus on maintaining quality while improving efficiency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Sampling Optimization",
        "canonical": "Sampling Optimization",
        "aliases": [
          "Sampling Efficiency"
        ],
        "category": "specific_connectable",
        "rationale": "Important for linking to broader discussions on improving inference speed in generative models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
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
      "resolved_canonical": "Diffusion Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Token Sparsification",
      "resolved_canonical": "Token Sparsification",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Generative Quality",
      "resolved_canonical": "Generative Quality",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Sampling Optimization",
      "resolved_canonical": "Sampling Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SparseDiT: Token Sparsification for Efficient Diffusion Transformer

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.06028.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2412.06028](https://arxiv.org/abs/2412.06028)

## 🔗 유사한 논문
- [[2025-09-23/DiCo_ Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling_20250923|DiCo: Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling]] (88.2% similar)
- [[2025-09-24/Foresight_ Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation_20250924|Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation]] (87.6% similar)
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (86.6% similar)
- [[2025-09-23/LRQ-DiT_ Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation_20250923|LRQ-DiT: Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation]] (86.6% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (86.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Sampling Optimization|Sampling Optimization]]
**⚡ Unique Technical**: [[keywords/Diffusion Transformer|Diffusion Transformer]], [[keywords/Token Sparsification|Token Sparsification]], [[keywords/Generative Quality|Generative Quality]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.06028v2 Announce Type: replace 
Abstract: Diffusion Transformers (DiT) are renowned for their impressive generative performance; however, they are significantly constrained by considerable computational costs due to the quadratic complexity in self-attention and the extensive sampling steps required. While advancements have been made in expediting the sampling process, the underlying architectural inefficiencies within DiT remain underexplored. We introduce SparseDiT, a novel framework that implements token sparsification across spatial and temporal dimensions to enhance computational efficiency while preserving generative quality. Spatially, SparseDiT employs a tri-segment architecture that allocates token density based on feature requirements at each layer: Poolingformer in the bottom layers for efficient global feature extraction, Sparse-Dense Token Modules (SDTM) in the middle layers to balance global context with local detail, and dense tokens in the top layers to refine high-frequency details. Temporally, SparseDiT dynamically modulates token density across denoising stages, progressively increasing token count as finer details emerge in later timesteps. This synergy between SparseDiT spatially adaptive architecture and its temporal pruning strategy enables a unified framework that balances efficiency and fidelity throughout the generation process. Our experiments demonstrate SparseDiT effectiveness, achieving a 55% reduction in FLOPs and a 175% improvement in inference speed on DiT-XL with similar FID score on 512x512 ImageNet, a 56% reduction in FLOPs across video generation datasets, and a 69% improvement in inference speed on PixArt-$\alpha$ on text-to-image generation task with a 0.24 FID score decrease. SparseDiT provides a scalable solution for high-quality diffusion-based generation compatible with sampling optimization techniques.

## 📝 요약

SparseDiT는 Diffusion Transformers(DiT)의 계산 효율성을 개선하기 위해 제안된 새로운 프레임워크입니다. DiT는 뛰어난 생성 성능을 보이지만, 자가 주의 메커니즘의 복잡성과 샘플링 단계로 인해 높은 계산 비용이 필요합니다. SparseDiT는 공간적 및 시간적 차원에서 토큰 희소화를 구현하여 이러한 비효율성을 해결합니다. 공간적으로는 세 가지 세그먼트 구조를 통해 각 층의 특징 요구에 따라 토큰 밀도를 조절하며, 시간적으로는 디노이징 단계에 따라 토큰 밀도를 동적으로 변화시킵니다. 실험 결과, SparseDiT는 DiT-XL에서 FLOPs를 55% 감소시키고 추론 속도를 175% 향상시키면서도 유사한 FID 점수를 유지했습니다. 또한, 비디오 생성 데이터셋에서 FLOPs를 56% 줄이고, 텍스트-이미지 생성 작업에서 추론 속도를 69% 향상시켰습니다. SparseDiT는 샘플링 최적화 기술과 호환되는 고품질 생성의 확장 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. SparseDiT는 공간적 및 시간적 차원에서 토큰 희소화를 구현하여 계산 효율성을 높이면서 생성 품질을 유지합니다.
- 2. 공간적으로 SparseDiT는 각 층의 기능 요구에 따라 토큰 밀도를 할당하는 삼분할 아키텍처를 사용합니다.
- 3. 시간적으로 SparseDiT는 디노이징 단계에 따라 토큰 밀도를 동적으로 조절하여 세부 사항이 나타날수록 토큰 수를 증가시킵니다.
- 4. SparseDiT는 DiT-XL에서 FLOPs를 55% 줄이고 추론 속도를 175% 향상시키면서 유사한 FID 점수를 유지합니다.
- 5. SparseDiT는 샘플링 최적화 기술과 호환되는 고품질 확산 기반 생성의 확장 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-24 16:26:57*