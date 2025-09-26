<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:41:31.889999",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Token Merge with Attention",
    "Transformer",
    "Attention Mechanism",
    "GPU Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.85,
    "Token Merge with Attention": 0.88,
    "Transformer": 0.7,
    "Attention Mechanism": 0.82,
    "GPU Efficiency": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion Processes"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's focus on improving image generation efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Token Merge with Attention",
        "canonical": "Token Merge with Attention",
        "aliases": [
          "ToMA"
        ],
        "category": "unique_technical",
        "rationale": "This is the core method proposed in the paper, offering a novel approach to token reduction.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology discussed in the context of attention complexity.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for understanding the efficiency improvements discussed.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "GPU Efficiency",
        "canonical": "GPU Efficiency",
        "aliases": [
          "GPU Optimization"
        ],
        "category": "unique_technical",
        "rationale": "The paper emphasizes GPU-aligned efficiency as a key advantage of the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "sorting",
      "scattered writes",
      "overheads"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Token Merge with Attention",
      "resolved_canonical": "Token Merge with Attention",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
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
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "GPU Efficiency",
      "resolved_canonical": "GPU Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# ToMA: Token Merge with Attention for Diffusion Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10918.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.10918](https://arxiv.org/abs/2509.10918)

## 🔗 유사한 논문
- [[2025-09-23/Optimizing Inference in Transformer-Based Models_ A Multi-Method Benchmark_20250923|Optimizing Inference in Transformer-Based Models: A Multi-Method Benchmark]] (84.4% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (84.2% similar)
- [[2025-09-23/FG-Attn_ Leveraging Fine-Grained Sparsity In Diffusion Transformers_20250923|FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers]] (84.2% similar)
- [[2025-09-19/Fast Multipole Attention_ A Scalable Multilevel Attention Mechanism for Text and Images_20250919|Fast Multipole Attention: A Scalable Multilevel Attention Mechanism for Text and Images]] (82.8% similar)
- [[2025-09-23/Seg4Diff_ Unveiling Open-Vocabulary Segmentation in Text-to-Image Diffusion Transformers_20250923|Seg4Diff: Unveiling Open-Vocabulary Segmentation in Text-to-Image Diffusion Transformers]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Token Merge with Attention|Token Merge with Attention]], [[keywords/GPU Efficiency|GPU Efficiency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10918v2 Announce Type: replace-cross 
Abstract: Diffusion models excel in high-fidelity image generation but face scalability limits due to transformers' quadratic attention complexity. Plug-and-play token reduction methods like ToMeSD and ToFu reduce FLOPs by merging redundant tokens in generated images but rely on GPU-inefficient operations (e.g., sorting, scattered writes), introducing overheads that negate theoretical speedups when paired with optimized attention implementations (e.g., FlashAttention). To bridge this gap, we propose Token Merge with Attention (ToMA), an off-the-shelf method that redesigns token reduction for GPU-aligned efficiency, with three key contributions: 1) a reformulation of token merge as a submodular optimization problem to select diverse tokens; 2) merge/unmerge as an attention-like linear transformation via GPU-friendly matrix operations; and 3) exploiting latent locality and sequential redundancy (pattern reuse) to minimize overhead. ToMA reduces SDXL/Flux generation latency by 24%/23%, respectively (with DINO $\Delta < 0.07$), outperforming prior methods. This work bridges the gap between theoretical and practical efficiency for transformers in diffusion.

## 📝 요약

이 논문은 고화질 이미지 생성에 뛰어난 확산 모델의 확장성 문제를 해결하기 위해 제안된 방법론인 ToMA(Token Merge with Attention)를 소개합니다. ToMA는 GPU 효율성을 고려하여 토큰 병합을 재설계한 방법으로, 세 가지 주요 기여를 합니다. 첫째, 다양한 토큰을 선택하기 위해 토큰 병합을 부분 모듈 최적화 문제로 재구성합니다. 둘째, GPU 친화적인 행렬 연산을 통해 병합/해제를 주의 메커니즘과 유사한 선형 변환으로 처리합니다. 셋째, 잠재적 지역성과 순차적 중복성을 활용하여 오버헤드를 최소화합니다. ToMA는 SDXL 및 Flux 생성 지연 시간을 각각 24% 및 23% 줄이며, 이론적 효율성과 실제 효율성 간의 격차를 줄입니다.

## 🎯 주요 포인트

- 1. 확산 모델의 고충실도 이미지 생성은 트랜스포머의 이차적 주의 복잡성 때문에 확장성에 한계가 있다.
- 2. ToMeSD와 ToFu 같은 토큰 감소 방법은 생성된 이미지에서 중복 토큰을 병합하여 FLOPs를 줄이지만, GPU 비효율적 작업으로 인해 이론적 속도 향상을 상쇄시킨다.
- 3. ToMA는 GPU에 맞춘 효율성을 위해 토큰 감소를 재설계한 방법으로, 다양한 토큰 선택을 위한 부분 모듈 최적화 문제로의 재구성, GPU 친화적 행렬 연산을 통한 주의 유사 선형 변환으로의 병합/분리, 잠재적 지역성과 순차적 중복성을 활용하여 오버헤드를 최소화한다.
- 4. ToMA는 SDXL/Flux 생성 지연을 각각 24%/23% 줄이며, 이전 방법보다 우수한 성능을 보인다.
- 5. 이 연구는 확산 모델에서 트랜스포머의 이론적 효율성과 실제 효율성 간의 격차를 줄인다.


---

*Generated on 2025-09-24 14:41:31*