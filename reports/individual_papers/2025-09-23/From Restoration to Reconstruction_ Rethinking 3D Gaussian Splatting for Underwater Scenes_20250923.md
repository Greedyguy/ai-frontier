---
keywords:
  - 3D Gaussian Splatting
  - Underwater Image Restoration
  - Uncertainty-Aware Opacity Optimization
  - Contrastive Loss
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17789
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:03:16.724148",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Underwater Image Restoration",
    "Uncertainty-Aware Opacity Optimization",
    "Contrastive Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Underwater Image Restoration": 0.77,
    "Uncertainty-Aware Opacity Optimization": 0.75,
    "Contrastive Loss": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's contribution, linking it to advancements in 3D reconstruction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Underwater Image Restoration",
        "canonical": "Underwater Image Restoration",
        "aliases": [
          "UIR"
        ],
        "category": "unique_technical",
        "rationale": "The paper proposes a novel integration of this process with 3D reconstruction, making it a unique technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Uncertainty-Aware Opacity Optimization",
        "canonical": "Uncertainty-Aware Opacity Optimization",
        "aliases": [
          "UAOO"
        ],
        "category": "unique_technical",
        "rationale": "This new optimization technique is a key innovation in the paper, addressing specific challenges in 3D rendering.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "Contrastive Loss",
        "canonical": "Contrastive Loss",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a well-known technique in machine learning, relevant for ensuring stable representations in the paper's context.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "R-Splatting",
      "BlueCoral3D",
      "Seathru-NeRF"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Underwater Image Restoration",
      "resolved_canonical": "Underwater Image Restoration",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Uncertainty-Aware Opacity Optimization",
      "resolved_canonical": "Uncertainty-Aware Opacity Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Contrastive Loss",
      "resolved_canonical": "Contrastive Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17789.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17789](https://arxiv.org/abs/2509.17789)

## 🔗 유사한 논문
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (86.5% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (85.4% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.9% similar)
- [[2025-09-23/SPFSplatV2_ Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views_20250923|SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views]] (84.6% similar)
- [[2025-09-23/HyRF_ Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis_20250923|HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Contrastive Loss|Contrastive Loss]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Underwater Image Restoration|Underwater Image Restoration]], [[keywords/Uncertainty-Aware Opacity Optimization|Uncertainty-Aware Opacity Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17789v1 Announce Type: new 
Abstract: Underwater image degradation poses significant challenges for 3D reconstruction, where simplified physical models often fail in complex scenes. We propose \textbf{R-Splatting}, a unified framework that bridges underwater image restoration (UIR) with 3D Gaussian Splatting (3DGS) to improve both rendering quality and geometric fidelity. Our method integrates multiple enhanced views produced by diverse UIR models into a single reconstruction pipeline. During inference, a lightweight illumination generator samples latent codes to support diverse yet coherent renderings, while a contrastive loss ensures disentangled and stable illumination representations. Furthermore, we propose \textit{Uncertainty-Aware Opacity Optimization (UAOO)}, which models opacity as a stochastic function to regularize training. This suppresses abrupt gradient responses triggered by illumination variation and mitigates overfitting to noisy or view-specific artifacts. Experiments on Seathru-NeRF and our new BlueCoral3D dataset demonstrate that R-Splatting outperforms strong baselines in both rendering quality and geometric accuracy.

## 📝 요약

이 논문에서는 복잡한 수중 환경에서 3D 재구성을 개선하기 위한 R-Splatting이라는 통합 프레임워크를 제안합니다. 이 방법은 수중 이미지 복원(UIR)과 3D Gaussian Splatting(3DGS)을 결합하여 렌더링 품질과 기하학적 정확성을 향상시킵니다. 다양한 UIR 모델로 생성된 여러 향상된 뷰를 단일 재구성 파이프라인에 통합하며, 경량 조명 생성기가 잠재 코드를 샘플링하여 다양한 렌더링을 지원합니다. 대조 손실을 통해 조명 표현의 분리를 보장하고, 불확실성 인식 불투명도 최적화(UAOO)를 제안하여 불투명도를 확률적 함수로 모델링하여 훈련을 정규화합니다. 실험 결과, R-Splatting은 Seathru-NeRF와 새로운 BlueCoral3D 데이터셋에서 렌더링 품질과 기하학적 정확성 면에서 기존 강력한 기준을 능가합니다.

## 🎯 주요 포인트

- 1. R-Splatting은 수중 이미지 복원과 3D 가우시안 스플래팅을 결합하여 렌더링 품질과 기하학적 정확성을 개선하는 통합 프레임워크입니다.
- 2. 다양한 수중 이미지 복원 모델에서 생성된 여러 향상된 뷰를 단일 재구성 파이프라인에 통합합니다.
- 3. 경량화된 조명 생성기가 잠재 코드를 샘플링하여 다양한 렌더링을 지원하며, 대조 손실을 통해 조명 표현의 분리를 보장합니다.
- 4. 불확실성 인식 불투명도 최적화(UAOO)를 제안하여 불투명도를 확률적 함수로 모델링하여 훈련을 정규화합니다.
- 5. Seathru-NeRF와 새로운 BlueCoral3D 데이터셋 실험에서 R-Splatting이 렌더링 품질과 기하학적 정확성에서 강력한 기준선을 능가함을 입증했습니다.


---

*Generated on 2025-09-24 05:03:16*