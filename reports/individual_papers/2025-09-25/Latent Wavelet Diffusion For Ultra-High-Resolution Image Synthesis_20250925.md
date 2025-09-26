---
keywords:
  - Latent Wavelet Diffusion
  - High-Resolution Image Synthesis
  - Wavelet Energy Maps
  - Scale-Consistent VAE Objective
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2506.00433
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:39:12.308607",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Wavelet Diffusion",
    "High-Resolution Image Synthesis",
    "Wavelet Energy Maps",
    "Scale-Consistent VAE Objective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Wavelet Diffusion": 0.8,
    "High-Resolution Image Synthesis": 0.78,
    "Wavelet Energy Maps": 0.72,
    "Scale-Consistent VAE Objective": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Latent Wavelet Diffusion",
        "canonical": "Latent Wavelet Diffusion",
        "aliases": [
          "LWD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for linking advancements in high-resolution image synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "high-resolution image synthesis",
        "canonical": "High-Resolution Image Synthesis",
        "aliases": [
          "ultra-high-resolution image synthesis"
        ],
        "category": "broad_technical",
        "rationale": "This is a key area of research in generative modeling, facilitating connections to related works.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "wavelet energy maps",
        "canonical": "Wavelet Energy Maps",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology, offering a unique approach to frequency-aware masking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "scale-consistent VAE objective",
        "canonical": "Scale-Consistent VAE Objective",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This objective is a specific innovation in the paper, enhancing spectral fidelity in image synthesis.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "computational efficiency",
      "fine-grained visual detail",
      "perceptual quality",
      "FID scores"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Latent Wavelet Diffusion",
      "resolved_canonical": "Latent Wavelet Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "high-resolution image synthesis",
      "resolved_canonical": "High-Resolution Image Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "wavelet energy maps",
      "resolved_canonical": "Wavelet Energy Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "scale-consistent VAE objective",
      "resolved_canonical": "Scale-Consistent VAE Objective",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Latent Wavelet Diffusion For Ultra-High-Resolution Image Synthesis

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00433.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2506.00433](https://arxiv.org/abs/2506.00433)

## 🔗 유사한 논문
- [[2025-09-23/Alias-Free Latent Diffusion Models_ Improving Fractional Shift Equivariance of Diffusion Latent Space_20250923|Alias-Free Latent Diffusion Models: Improving Fractional Shift Equivariance of Diffusion Latent Space]] (83.7% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (83.5% similar)
- [[2025-09-23/When Color-Space Decoupling Meets Diffusion for Adverse-Weather Image Restoration_20250923|When Color-Space Decoupling Meets Diffusion for Adverse-Weather Image Restoration]] (83.0% similar)
- [[2025-09-24/Prompt-Guided Dual Latent Steering for Inversion Problems_20250924|Prompt-Guided Dual Latent Steering for Inversion Problems]] (82.7% similar)
- [[2025-09-24/WaveletGaussian_ Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction_20250924|WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/High-Resolution Image Synthesis|High-Resolution Image Synthesis]]
**⚡ Unique Technical**: [[keywords/Latent Wavelet Diffusion|Latent Wavelet Diffusion]], [[keywords/Wavelet Energy Maps|Wavelet Energy Maps]], [[keywords/Scale-Consistent VAE Objective|Scale-Consistent VAE Objective]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00433v3 Announce Type: replace-cross 
Abstract: High-resolution image synthesis remains a core challenge in generative modeling, particularly in balancing computational efficiency with the preservation of fine-grained visual detail. We present Latent Wavelet Diffusion (LWD), a lightweight training framework that significantly improves detail and texture fidelity in ultra-high-resolution (2K-4K) image synthesis. LWD introduces a novel, frequency-aware masking strategy derived from wavelet energy maps, which dynamically focuses the training process on detail-rich regions of the latent space. This is complemented by a scale-consistent VAE objective to ensure high spectral fidelity. The primary advantage of our approach is its efficiency: LWD requires no architectural modifications and adds zero additional cost during inference, making it a practical solution for scaling existing models. Across multiple strong baselines, LWD consistently improves perceptual quality and FID scores, demonstrating the power of signal-driven supervision as a principled and efficient path toward high-resolution generative modeling.

## 📝 요약

Latent Wavelet Diffusion (LWD)는 초고해상도 이미지 합성에서 세부 묘사와 질감 충실도를 크게 향상시키는 경량 훈련 프레임워크입니다. LWD는 웨이블릿 에너지 맵에서 파생된 주파수 인식 마스킹 전략을 도입하여 잠재 공간의 세부가 풍부한 영역에 집중적으로 훈련합니다. 또한, 스케일 일관성을 유지하는 VAE 목표를 통해 높은 스펙트럼 충실도를 보장합니다. LWD는 아키텍처 수정 없이 추가 비용 없이 효율성을 제공하며, 여러 강력한 기준선에서 인지적 품질과 FID 점수를 지속적으로 개선합니다. 이는 고해상도 생성 모델링을 위한 신호 기반 감독의 효과적인 경로를 제시합니다.

## 🎯 주요 포인트

- 1. Latent Wavelet Diffusion(LWD)는 초고해상도 이미지 합성에서 세부 및 질감 충실도를 크게 향상시키는 경량 학습 프레임워크입니다.
- 2. LWD는 웨이블릿 에너지 맵에서 파생된 주파수 인식 마스킹 전략을 도입하여 잠재 공간의 세부 정보가 풍부한 영역에 집중합니다.
- 3. LWD는 스케일 일관성을 유지하는 VAE 목표를 통해 높은 스펙트럼 충실도를 보장합니다.
- 4. LWD는 아키텍처 수정 없이 추론 시 추가 비용이 발생하지 않아 기존 모델 확장에 실용적입니다.
- 5. 여러 강력한 기준선에서 LWD는 일관되게 지각적 품질과 FID 점수를 개선하여 고해상도 생성 모델링을 위한 효율적인 경로를 제시합니다.


---

*Generated on 2025-09-26 08:39:12*