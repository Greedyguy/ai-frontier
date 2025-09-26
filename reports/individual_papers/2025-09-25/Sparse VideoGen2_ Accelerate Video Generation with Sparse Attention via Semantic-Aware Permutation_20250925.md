---
keywords:
  - Transformer
  - Attention Mechanism
  - Semantic Clustering
  - Resource Management
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2505.18875
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:25:19.065187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Attention Mechanism",
    "Semantic Clustering",
    "Resource Management"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Attention Mechanism": 0.88,
    "Semantic Clustering": 0.8,
    "Resource Management": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Transformer",
        "aliases": [
          "DiTs"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in machine learning, and linking to them provides context for understanding the architecture used in video generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Sparse Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Sparse Attention Mechanism"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are critical in optimizing computational efficiency, and sparse attention is a specific variant that enhances understanding of the method's efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Semantic-Aware Permutation",
        "canonical": "Semantic Clustering",
        "aliases": [
          "Semantic Reordering"
        ],
        "category": "unique_technical",
        "rationale": "This technique is unique to the paper and provides insights into how semantic similarity is leveraged for efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dynamic Budget Control",
        "canonical": "Resource Management",
        "aliases": [
          "Budget Control"
        ],
        "category": "unique_technical",
        "rationale": "Understanding resource management techniques is crucial for optimizing computational processes in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "framework",
      "efficiency",
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
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Sparse Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Semantic-Aware Permutation",
      "resolved_canonical": "Semantic Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dynamic Budget Control",
      "resolved_canonical": "Resource Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Sparse VideoGen2: Accelerate Video Generation with Sparse Attention via Semantic-Aware Permutation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18875.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2505.18875](https://arxiv.org/abs/2505.18875)

## 🔗 유사한 논문
- [[2025-09-24/SparseDiT_ Token Sparsification for Efficient Diffusion Transformer_20250924|SparseDiT: Token Sparsification for Efficient Diffusion Transformer]] (87.7% similar)
- [[2025-09-23/FG-Attn_ Leveraging Fine-Grained Sparsity In Diffusion Transformers_20250923|FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers]] (87.4% similar)
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (86.3% similar)
- [[2025-09-25/From Slow Bidirectional to Fast Autoregressive Video Diffusion Models_20250925|From Slow Bidirectional to Fast Autoregressive Video Diffusion Models]] (86.1% similar)
- [[2025-09-23/QVGen_ Pushing the Limit of Quantized Video Generative Models_20250923|QVGen: Pushing the Limit of Quantized Video Generative Models]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Semantic Clustering|Semantic Clustering]], [[keywords/Resource Management|Resource Management]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18875v2 Announce Type: replace 
Abstract: Diffusion Transformers (DiTs) are essential for video generation but suffer from significant latency due to the quadratic complexity of attention. By computing only critical tokens, sparse attention reduces computational costs and offers a promising acceleration approach. However, we identify that existing methods fail to approach optimal generation quality under the same computation budget for two reasons: (1) Inaccurate critical token identification: current methods cluster tokens based on position rather than semantics, leading to imprecise aggregated representations. (2) Excessive computation waste: critical tokens are scattered among non-critical ones, leading to wasted computation on GPUs, which are optimized for processing contiguous tokens. In this paper, we propose SVG2, a training-free framework that maximizes identification accuracy and minimizes computation waste, achieving a Pareto frontier trade-off between generation quality and efficiency. The core of SVG2 is semantic-aware permutation, which clusters and reorders tokens based on semantic similarity using k-means. This approach ensures both a precise cluster representation, improving identification accuracy, and a densified layout of critical tokens, enabling efficient computation without padding. Additionally, SVG2 integrates top-p dynamic budget control and customized kernel implementations, achieving up to 2.30x and 1.89x speedup while maintaining a PSNR of up to 30 and 26 on HunyuanVideo and Wan 2.1, respectively.

## 📝 요약

이 논문은 비디오 생성에 필수적인 Diffusion Transformers(DiTs)의 주의력 계산 복잡성을 해결하기 위해 SVG2라는 새로운 프레임워크를 제안합니다. 기존 방법들은 위치 기반으로 토큰을 클러스터링하여 정확한 토큰 식별에 실패하고, GPU 최적화에 비효율적인 계산 낭비를 초래합니다. SVG2는 의미 기반의 토큰 재배치를 통해 이러한 문제를 해결하며, k-평균을 사용하여 토큰을 의미적으로 클러스터링하고 재배열합니다. 이를 통해 정확한 클러스터 표현과 효율적인 계산을 가능하게 합니다. 또한, SVG2는 동적 예산 제어와 맞춤형 커널 구현을 통합하여 HunyuanVideo와 Wan 2.1에서 각각 최대 2.30배, 1.89배의 속도 향상을 이루면서 PSNR을 30과 26까지 유지합니다.

## 🎯 주요 포인트

- 1. DiTs는 비디오 생성에 필수적이지만, 주의력의 이차적 복잡성으로 인해 지연이 발생합니다.
- 2. 기존 방법은 위치 기반 토큰 클러스터링으로 인해 정확한 토큰 식별에 실패합니다.
- 3. SVG2는 의미 기반 클러스터링을 통해 토큰 식별 정확성을 극대화하고 계산 낭비를 최소화합니다.
- 4. SVG2는 top-p 동적 예산 제어와 맞춤형 커널 구현을 통합하여 최대 2.30배의 속도 향상을 달성합니다.
- 5. HunyuanVideo와 Wan 2.1에서 각각 최대 PSNR 30과 26을 유지하며 효율성을 높입니다.


---

*Generated on 2025-09-26 09:25:19*