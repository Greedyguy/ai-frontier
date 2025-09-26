<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:04:38.918055",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Latent Space",
    "Prompt-Guided Dual Latent Steering",
    "Rectified Flow Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Latent Space": 0.78,
    "Prompt-Guided Dual Latent Steering": 0.88,
    "Rectified Flow Models": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion model"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's approach and connect well with other generative model discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "latent space",
        "canonical": "Latent Space",
        "aliases": [
          "latent vector space"
        ],
        "category": "specific_connectable",
        "rationale": "Latent space is a key concept in understanding the inversion process and links to broader discussions on generative models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Prompt-Guided Dual Latent Steering",
        "canonical": "Prompt-Guided Dual Latent Steering",
        "aliases": [
          "PDLS"
        ],
        "category": "unique_technical",
        "rationale": "PDLS is a unique framework introduced by the authors, crucial for understanding the paper's contribution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Rectified Flow models",
        "canonical": "Rectified Flow Models",
        "aliases": [
          "Rectified Flow"
        ],
        "category": "unique_technical",
        "rationale": "Rectified Flow models are integral to the paper's method, offering a stable inversion path.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "inversion",
      "reconstruction",
      "image"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "latent space",
      "resolved_canonical": "Latent Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Prompt-Guided Dual Latent Steering",
      "resolved_canonical": "Prompt-Guided Dual Latent Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Rectified Flow models",
      "resolved_canonical": "Rectified Flow Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Prompt-Guided Dual Latent Steering for Inversion Problems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18619.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18619](https://arxiv.org/abs/2509.18619)

## 🔗 유사한 논문
- [[2025-09-23/Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding_20250923|Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding]] (84.0% similar)
- [[2025-09-23/When Color-Space Decoupling Meets Diffusion for Adverse-Weather Image Restoration_20250923|When Color-Space Decoupling Meets Diffusion for Adverse-Weather Image Restoration]] (83.9% similar)
- [[2025-09-22/Analysis Plug-and-Play Methods for Imaging Inverse Problems_20250922|Analysis Plug-and-Play Methods for Imaging Inverse Problems]] (83.4% similar)
- [[2025-09-24/Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning_20250924|Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning]] (83.4% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Latent Space|Latent Space]]
**⚡ Unique Technical**: [[keywords/Prompt-Guided Dual Latent Steering|Prompt-Guided Dual Latent Steering]], [[keywords/Rectified Flow Models|Rectified Flow Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18619v1 Announce Type: new 
Abstract: Inverting corrupted images into the latent space of diffusion models is challenging. Current methods, which encode an image into a single latent vector, struggle to balance structural fidelity with semantic accuracy, leading to reconstructions with semantic drift, such as blurred details or incorrect attributes. To overcome this, we introduce Prompt-Guided Dual Latent Steering (PDLS), a novel, training-free framework built upon Rectified Flow models for their stable inversion paths. PDLS decomposes the inversion process into two complementary streams: a structural path to preserve source integrity and a semantic path guided by a prompt. We formulate this dual guidance as an optimal control problem and derive a closed-form solution via a Linear Quadratic Regulator (LQR). This controller dynamically steers the generative trajectory at each step, preventing semantic drift while ensuring the preservation of fine detail without costly, per-image optimization. Extensive experiments on FFHQ-1K and ImageNet-1K under various inversion tasks, including Gaussian deblurring, motion deblurring, super-resolution and freeform inpainting, demonstrate that PDLS produces reconstructions that are both more faithful to the original image and better aligned with the semantic information than single-latent baselines.

## 📝 요약

이 논문은 손상된 이미지를 확산 모델의 잠재 공간으로 변환하는 문제를 다룹니다. 기존 방법들은 이미지의 구조적 충실성과 의미적 정확성 사이의 균형을 맞추는 데 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 Prompt-Guided Dual Latent Steering (PDLS)라는 새로운 프레임워크를 제안합니다. PDLS는 구조적 경로와 의미적 경로로 나누어 이미지를 변환하며, 이는 최적 제어 문제로 공식화되어 Linear Quadratic Regulator (LQR)를 통해 해결됩니다. 이 방법은 이미지의 세부 사항을 보존하면서도 의미적 드리프트를 방지합니다. FFHQ-1K와 ImageNet-1K 데이터셋에서의 다양한 실험을 통해 PDLS가 기존 방법보다 원본 이미지에 더 충실하고 의미적으로 잘 정렬된 재구성을 생성함을 입증했습니다.

## 🎯 주요 포인트

- 1. 기존 방법들은 단일 잠재 벡터로 이미지를 인코딩하여 구조적 충실성과 의미적 정확성의 균형을 맞추기 어려워합니다.
- 2. PDLS(Prompt-Guided Dual Latent Steering)는 구조적 경로와 의미적 경로로 나누어 이미지를 복원하며, 의미적 드리프트를 방지합니다.
- 3. PDLS는 최적 제어 문제로서의 이중 가이던스를 공식화하고, 선형 이차 조절기(LQR)를 통해 폐쇄형 해를 도출합니다.
- 4. FFHQ-1K 및 ImageNet-1K 데이터셋에서의 다양한 복원 작업 실험에서 PDLS는 원본 이미지에 더 충실하고 의미적 정보에 더 잘 맞는 복원을 제공합니다.
- 5. PDLS는 비용이 많이 드는 이미지별 최적화 없이도 세부 사항을 보존하면서 생성 궤적을 동적으로 조정합니다.


---

*Generated on 2025-09-24 16:04:38*