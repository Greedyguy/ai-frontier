---
keywords:
  - Diffusion Models
  - LowDiff
  - Image Generation
  - Cascaded Generation
  - Latent Space
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15342
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:56:16.662615",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "LowDiff",
    "Image Generation",
    "Cascaded Generation",
    "Latent Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.88,
    "LowDiff": 0.8,
    "Image Generation": 0.7,
    "Cascaded Generation": 0.75,
    "Latent Space": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion Process",
          "Diffusion Framework"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's methodology and connect to broader research in generative models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "LowDiff",
        "canonical": "LowDiff",
        "aliases": [
          "Low-Resolution Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "LowDiff is a novel approach introduced by the paper, offering a unique method for efficient diffusion sampling.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Image Generation",
        "canonical": "Image Generation",
        "aliases": [
          "Image Synthesis"
        ],
        "category": "broad_technical",
        "rationale": "Image generation is a fundamental application area for diffusion models, linking to a wide array of computer vision research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Cascaded Approach",
        "canonical": "Cascaded Generation",
        "aliases": [
          "Cascaded Method"
        ],
        "category": "specific_connectable",
        "rationale": "The cascaded approach is a key technique in the paper, enabling efficient resolution refinement in diffusion models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Latent Space",
        "canonical": "Latent Space",
        "aliases": [
          "Latent Representation"
        ],
        "category": "specific_connectable",
        "rationale": "Latent space is crucial for understanding the paper's application of diffusion models in different domains.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "sampling speed",
      "efficiency gains"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "LowDiff",
      "resolved_canonical": "LowDiff",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Image Generation",
      "resolved_canonical": "Image Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Cascaded Approach",
      "resolved_canonical": "Cascaded Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Latent Space",
      "resolved_canonical": "Latent Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition

**Korean Title:** 로우디프: 저해상도 조건을 이용한 효율적인 확산 샘플링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15342.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15342](https://arxiv.org/abs/2509.15342)

## 🔗 유사한 논문
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (85.3% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (83.9% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (83.5% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (83.3% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Generation|Image Generation]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Cascaded Generation|Cascaded Generation]], [[keywords/Latent Space|Latent Space]]
**⚡ Unique Technical**: [[keywords/LowDiff|LowDiff]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15342v1 Announce Type: new 
Abstract: Diffusion models have achieved remarkable success in image generation but their practical application is often hindered by the slow sampling speed. Prior efforts of improving efficiency primarily focus on compressing models or reducing the total number of denoising steps, largely neglecting the possibility to leverage multiple input resolutions in the generation process. In this work, we propose LowDiff, a novel and efficient diffusion framework based on a cascaded approach by generating increasingly higher resolution outputs. Besides, LowDiff employs a unified model to progressively refine images from low resolution to the desired resolution. With the proposed architecture design and generation techniques, we achieve comparable or even superior performance with much fewer high-resolution sampling steps. LowDiff is applicable to diffusion models in both pixel space and latent space. Extensive experiments on both conditional and unconditional generation tasks across CIFAR-10, FFHQ and ImageNet demonstrate the effectiveness and generality of our method. Results show over 50% throughput improvement across all datasets and settings while maintaining comparable or better quality. On unconditional CIFAR-10, LowDiff achieves an FID of 2.11 and IS of 9.87, while on conditional CIFAR-10, an FID of 1.94 and IS of 10.03. On FFHQ 64x64, LowDiff achieves an FID of 2.43, and on ImageNet 256x256, LowDiff built on LightningDiT-B/1 produces high-quality samples with a FID of 4.00 and an IS of 195.06, together with substantial efficiency gains.

## 🔍 Abstract (한글 번역)

arXiv:2509.15342v1 발표 유형: 신규  
초록: 확산 모델은 이미지 생성에서 놀라운 성공을 거두었지만, 느린 샘플링 속도로 인해 실용적인 응용이 종종 방해받습니다. 효율성을 개선하려는 이전의 노력은 주로 모델을 압축하거나 디노이징 단계의 총 수를 줄이는 데 초점을 맞추었으며, 생성 과정에서 여러 입력 해상도를 활용할 가능성은 크게 간과되었습니다. 본 연구에서는 점차적으로 더 높은 해상도의 출력을 생성하는 계단식 접근 방식을 기반으로 한 새로운 효율적인 확산 프레임워크인 LowDiff를 제안합니다. 또한, LowDiff는 통합된 모델을 사용하여 저해상도에서 원하는 해상도로 이미지를 점진적으로 개선합니다. 제안된 아키텍처 설계 및 생성 기술을 통해 훨씬 적은 고해상도 샘플링 단계로도 동등하거나 더 우수한 성능을 달성합니다. LowDiff는 픽셀 공간과 잠재 공간 모두에서 확산 모델에 적용 가능합니다. CIFAR-10, FFHQ, ImageNet에서의 조건부 및 비조건부 생성 작업에 대한 광범위한 실험은 본 방법의 효과성과 일반성을 입증합니다. 결과는 모든 데이터셋과 설정에서 50% 이상의 처리량 개선을 보여주며, 동등하거나 더 나은 품질을 유지합니다. 비조건부 CIFAR-10에서 LowDiff는 FID 2.11과 IS 9.87을 달성하며, 조건부 CIFAR-10에서는 FID 1.94와 IS 10.03을 달성합니다. FFHQ 64x64에서는 FID 2.43을, ImageNet 256x256에서는 LightningDiT-B/1을 기반으로 한 LowDiff가 FID 4.00과 IS 195.06의 고품질 샘플을 생성하며, 상당한 효율성 향상을 함께 제공합니다.

## 📝 요약

이 논문에서는 이미지 생성에서의 확산 모델의 샘플링 속도를 개선하기 위해 LowDiff라는 새로운 프레임워크를 제안합니다. LowDiff는 점진적으로 높은 해상도의 출력을 생성하는 계단식 접근 방식을 사용하며, 통합된 모델을 통해 저해상도에서 원하는 해상도로 이미지를 정교하게 개선합니다. 이 방법론은 픽셀 공간과 잠재 공간 모두에서 적용 가능하며, CIFAR-10, FFHQ, ImageNet 등 다양한 데이터셋에서 실험을 통해 효과와 일반성을 입증했습니다. 결과적으로, 모든 데이터셋에서 50% 이상의 처리량 개선을 이루면서도 품질을 유지하거나 향상시켰습니다. 특히, CIFAR-10에서 무조건적 생성 시 FID 2.11, IS 9.87을, 조건적 생성 시 FID 1.94, IS 10.03을 달성했습니다. FFHQ 64x64에서는 FID 2.43, ImageNet 256x256에서는 FID 4.00, IS 195.06을 기록하며 효율성을 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. LowDiff는 점진적으로 더 높은 해상도의 출력을 생성하는 계단식 접근 방식을 기반으로 한 새로운 효율적인 확산 프레임워크입니다.
- 2. LowDiff는 낮은 해상도에서 원하는 해상도로 이미지를 점진적으로 개선하는 통합 모델을 사용합니다.
- 3. 제안된 아키텍처 설계와 생성 기술을 통해 고해상도 샘플링 단계를 크게 줄이면서도 동등하거나 더 나은 성능을 달성합니다.
- 4. LowDiff는 픽셀 공간과 잠재 공간 모두에서 확산 모델에 적용 가능하며, 모든 데이터셋과 설정에서 50% 이상의 처리량 개선을 보여줍니다.
- 5. 다양한 데이터셋에서 실험한 결과, LowDiff는 높은 품질의 샘플을 생성하면서도 상당한 효율성 향상을 이루었습니다.


---

*Generated on 2025-09-23 11:56:16*