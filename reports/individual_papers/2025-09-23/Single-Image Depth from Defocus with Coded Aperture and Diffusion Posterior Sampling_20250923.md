---
keywords:
  - Depth from Defocus
  - Coded Aperture Imaging
  - Diffusion Prior
  - Differentiable Forward Model
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17427
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:50:28.296382",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Depth from Defocus",
    "Coded Aperture Imaging",
    "Diffusion Prior",
    "Differentiable Forward Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Depth from Defocus": 0.78,
    "Coded Aperture Imaging": 0.77,
    "Diffusion Prior": 0.8,
    "Differentiable Forward Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "depth-from-defocus",
        "canonical": "Depth from Defocus",
        "aliases": [
          "DFD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's contribution, offering unique insights into depth estimation methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "coded-aperture imaging",
        "canonical": "Coded Aperture Imaging",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A key technique in the paper, providing a unique approach to imaging that can link to other optical methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "diffusion prior",
        "canonical": "Diffusion Prior",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the paper's novel approach to regularization in imaging.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "differentiable forward model",
        "canonical": "Differentiable Forward Model",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A technical concept that enhances understanding of the optimization framework used in the study.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
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
      "candidate_surface": "depth-from-defocus",
      "resolved_canonical": "Depth from Defocus",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "coded-aperture imaging",
      "resolved_canonical": "Coded Aperture Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "diffusion prior",
      "resolved_canonical": "Diffusion Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "differentiable forward model",
      "resolved_canonical": "Differentiable Forward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17427.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17427](https://arxiv.org/abs/2509.17427)

## 🔗 유사한 논문
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (83.6% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (83.1% similar)
- [[2025-09-19/Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration_20250919|Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration]] (82.6% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (82.5% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Prior|Diffusion Prior]]
**⚡ Unique Technical**: [[keywords/Depth from Defocus|Depth from Defocus]], [[keywords/Coded Aperture Imaging|Coded Aperture Imaging]], [[keywords/Differentiable Forward Model|Differentiable Forward Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17427v1 Announce Type: new 
Abstract: We propose a single-snapshot depth-from-defocus (DFD) reconstruction method for coded-aperture imaging that replaces hand-crafted priors with a learned diffusion prior used purely as regularization. Our optimization framework enforces measurement consistency via a differentiable forward model while guiding solutions with the diffusion prior in the denoised image domain, yielding higher accuracy and stability than clas- sical optimization. Unlike U-Net-style regressors, our approach requires no paired defocus-RGBD training data and does not tie training to a specific camera configuration. Experiments on comprehensive simulations and a prototype camera demonstrate consistently strong RGBD reconstructions across noise levels, outperforming both U-Net baselines and a classical coded- aperture DFD method.

## 📝 요약

이 논문은 코드화된 조리개 이미징을 위한 단일 스냅샷 초점 흐림(DfD) 복원 방법을 제안합니다. 이 방법은 수작업으로 설계된 사전 정보를 학습된 확산 사전으로 대체하여 정규화에 사용합니다. 최적화 프레임워크는 측정 일관성을 보장하면서, 노이즈 제거된 이미지 영역에서 확산 사전으로 솔루션을 안내하여 기존 최적화보다 높은 정확성과 안정성을 제공합니다. U-Net 스타일의 회귀 모델과 달리, 이 접근법은 특정 카메라 구성에 종속되지 않으며, 초점 흐림-RGBD 훈련 데이터가 필요하지 않습니다. 종합적인 시뮬레이션과 프로토타입 카메라 실험에서, 다양한 노이즈 수준에서도 일관되게 우수한 RGBD 복원을 보여주며, U-Net 기반 및 기존 코드화 조리개 DfD 방법을 능가합니다.

## 🎯 주요 포인트

- 1. 본 연구는 코드화된 조리개 이미징을 위한 단일 스냅샷 DFD 복원 방법을 제안하며, 이는 수작업으로 설계된 사전 대신 학습된 확산 사전을 정규화로 사용합니다.
- 2. 제안된 최적화 프레임워크는 측정 일관성을 보장하며, 확산 사전을 사용하여 더 높은 정확도와 안정성을 제공합니다.
- 3. U-Net 스타일의 회귀 모델과 달리, 본 접근법은 특정 카메라 구성에 대한 훈련 데이터가 필요하지 않습니다.
- 4. 다양한 시뮬레이션과 프로토타입 카메라 실험에서 제안된 방법은 일관되게 높은 성능의 RGBD 복원을 보여주었습니다.
- 5. 제안된 방법은 다양한 노이즈 수준에서 U-Net 기반 및 전통적인 코드화 조리개 DFD 방법을 능가합니다.


---

*Generated on 2025-09-24 04:50:28*