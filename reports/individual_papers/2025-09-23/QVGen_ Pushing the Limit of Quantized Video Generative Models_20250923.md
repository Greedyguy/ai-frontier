---
keywords:
  - Video Diffusion Models
  - Quantization-Aware Training
  - Singular Value Decomposition
  - Rank-Based Regularization
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2505.11497
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:22:34.503606",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Video Diffusion Models",
    "Quantization-Aware Training",
    "Singular Value Decomposition",
    "Rank-Based Regularization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Video Diffusion Models": 0.78,
    "Quantization-Aware Training": 0.77,
    "Singular Value Decomposition": 0.72,
    "Rank-Based Regularization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Video Diffusion Models",
        "canonical": "Video Diffusion Models",
        "aliases": [
          "Video DMs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on improving video synthesis efficiency, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Quantization-Aware Training",
        "canonical": "Quantization-Aware Training",
        "aliases": [
          "QAT"
        ],
        "category": "unique_technical",
        "rationale": "QAT is a key technique discussed in the paper for improving video model efficiency under low-bit quantization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Singular Value Decomposition",
        "canonical": "Singular Value Decomposition",
        "aliases": [
          "SVD"
        ],
        "category": "broad_technical",
        "rationale": "SVD is a mathematical technique used in the paper's proposed strategy to optimize model performance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Rank-Based Regularization",
        "canonical": "Rank-Based Regularization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper to enhance model efficiency by managing component contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
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
      "candidate_surface": "Video Diffusion Models",
      "resolved_canonical": "Video Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Quantization-Aware Training",
      "resolved_canonical": "Quantization-Aware Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Singular Value Decomposition",
      "resolved_canonical": "Singular Value Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Rank-Based Regularization",
      "resolved_canonical": "Rank-Based Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# QVGen: Pushing the Limit of Quantized Video Generative Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11497.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2505.11497](https://arxiv.org/abs/2505.11497)

## 🔗 유사한 논문
- [[2025-09-22/MEC-Quant_ Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training_20250922|MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training]] (84.9% similar)
- [[2025-09-23/4DGCPro_ Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming_20250923|4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming]] (84.8% similar)
- [[2025-09-23/VQToken_ Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models_20250923|VQToken: Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models]] (84.3% similar)
- [[2025-09-23/FG-Attn_ Leveraging Fine-Grained Sparsity In Diffusion Transformers_20250923|FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers]] (82.6% similar)
- [[2025-09-23/PTQTP_ Post-Training Quantization to Trit-Planes for Large Language Models_20250923|PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Singular Value Decomposition|Singular Value Decomposition]]
**⚡ Unique Technical**: [[keywords/Video Diffusion Models|Video Diffusion Models]], [[keywords/Quantization-Aware Training|Quantization-Aware Training]], [[keywords/Rank-Based Regularization|Rank-Based Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11497v3 Announce Type: replace 
Abstract: Video diffusion models (DMs) have enabled high-quality video synthesis. Yet, their substantial computational and memory demands pose serious challenges to real-world deployment, even on high-end GPUs. As a commonly adopted solution, quantization has proven notable success in reducing cost for image DMs, while its direct application to video DMs remains ineffective. In this paper, we present QVGen, a novel quantization-aware training (QAT) framework tailored for high-performance and inference-efficient video DMs under extremely low-bit quantization (e.g., 4-bit or below). We begin with a theoretical analysis demonstrating that reducing the gradient norm is essential to facilitate convergence for QAT. To this end, we introduce auxiliary modules ($\Phi$) to mitigate large quantization errors, leading to significantly enhanced convergence. To eliminate the inference overhead of $\Phi$, we propose a rank-decay strategy that progressively eliminates $\Phi$. Specifically, we repeatedly employ singular value decomposition (SVD) and a proposed rank-based regularization $\mathbf{\gamma}$ to identify and decay low-contributing components. This strategy retains performance while zeroing out inference overhead. Extensive experiments across $4$ state-of-the-art (SOTA) video DMs, with parameter sizes ranging from $1.3$B $\sim14$B, show that QVGen is the first to reach full-precision comparable quality under 4-bit settings. Moreover, it significantly outperforms existing methods. For instance, our 3-bit CogVideoX-2B achieves improvements of $+25.28$ in Dynamic Degree and $+8.43$ in Scene Consistency on VBench.

## 📝 요약

QVGen은 고성능 비디오 확산 모델(VDM)을 위한 새로운 양자화 인식 학습(QAT) 프레임워크로, 매우 낮은 비트 양자화(예: 4비트 이하)에서도 효율적인 추론을 가능하게 합니다. 이 연구는 QAT의 수렴을 위해 그래디언트 노름 감소가 필요함을 이론적으로 분석하고, 이를 위해 보조 모듈(Φ)을 도입하여 양자화 오류를 줄여 수렴성을 크게 향상시켰습니다. 또한, SVD와 랭크 기반 정규화를 활용한 랭크 감쇠 전략을 통해 성능을 유지하면서도 추론 오버헤드를 제거합니다. 실험 결과, QVGen은 4비트 설정에서 풀 프리시전과 유사한 품질을 달성하며, 기존 방법을 능가하는 성능을 보였습니다. 예를 들어, 3비트 CogVideoX-2B는 VBench에서 Dynamic Degree와 Scene Consistency에서 각각 +25.28, +8.43의 개선을 보였습니다.

## 🎯 주요 포인트

- 1. QVGen은 비디오 확산 모델의 고성능과 추론 효율성을 위한 저비트 양자화 인식 훈련(QAT) 프레임워크를 제안합니다.
- 2. 이론적 분석을 통해 QAT의 수렴을 촉진하기 위해서는 그래디언트 노름을 줄이는 것이 필수적임을 보였습니다.
- 3. 보조 모듈($\Phi$)을 도입하여 큰 양자화 오류를 완화하고 수렴을 크게 향상시켰습니다.
- 4. 랭크 감소 전략을 통해 $\Phi$의 추론 오버헤드를 제거하면서 성능을 유지합니다.
- 5. QVGen은 4비트 설정에서 풀 프리시전과 비교 가능한 품질을 달성하며, 기존 방법들을 능가하는 성능을 보입니다.


---

*Generated on 2025-09-24 05:22:34*