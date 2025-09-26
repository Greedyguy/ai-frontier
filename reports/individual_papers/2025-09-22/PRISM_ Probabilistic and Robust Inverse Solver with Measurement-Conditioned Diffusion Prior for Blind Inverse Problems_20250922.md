---
keywords:
  - Diffusion Models
  - Blind Inverse Problems
  - Image Deblurring
  - Measurement-Conditioned Diffusion Prior
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16106
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:57:07.844749",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Blind Inverse Problems",
    "Image Deblurring",
    "Measurement-Conditioned Diffusion Prior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Blind Inverse Problems": 0.72,
    "Image Deblurring": 0.77,
    "Measurement-Conditioned Diffusion Prior": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based Models"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's methodology and connect well with computational imaging topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Blind Inverse Problems",
        "canonical": "Blind Inverse Problems",
        "aliases": [
          "Blind Inverse Problem Solving"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific problem domain addressed by the paper, offering high novelty and specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Image Deblurring",
        "canonical": "Image Deblurring",
        "aliases": [
          "Deblurring"
        ],
        "category": "specific_connectable",
        "rationale": "Image deblurring is a key application area, providing strong connectivity to related computational imaging techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Measurement-Conditioned Diffusion Prior",
        "canonical": "Measurement-Conditioned Diffusion Prior",
        "aliases": [
          "Measurement-Conditioned Prior"
        ],
        "category": "unique_technical",
        "rationale": "This concept is novel and specific to the proposed method, enhancing the understanding of the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
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
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Blind Inverse Problems",
      "resolved_canonical": "Blind Inverse Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Image Deblurring",
      "resolved_canonical": "Image Deblurring",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Measurement-Conditioned Diffusion Prior",
      "resolved_canonical": "Measurement-Conditioned Diffusion Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PRISM: Probabilistic and Robust Inverse Solver with Measurement-Conditioned Diffusion Prior for Blind Inverse Problems

**Korean Title:** PRISM: 측정 조건 확산 사전이 적용된 확률적이고 견고한 블라인드 역문제 해결기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16106.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16106](https://arxiv.org/abs/2509.16106)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (84.2% similar)
- [[2025-09-22/Analysis Plug-and-Play Methods for Imaging Inverse Problems_20250922|Analysis Plug-and-Play Methods for Imaging Inverse Problems]] (83.0% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (81.8% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (81.7% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Image Deblurring|Image Deblurring]]
**⚡ Unique Technical**: [[keywords/Blind Inverse Problems|Blind Inverse Problems]], [[keywords/Measurement-Conditioned Diffusion Prior|Measurement-Conditioned Diffusion Prior]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16106v1 Announce Type: cross 
Abstract: Diffusion models are now commonly used to solve inverse problems in computational imaging. However, most diffusion-based inverse solvers require complete knowledge of the forward operator to be used. In this work, we introduce a novel probabilistic and robust inverse solver with measurement-conditioned diffusion prior (PRISM) to effectively address blind inverse problems. PRISM offers a technical advancement over current methods by incorporating a powerful measurement-conditioned diffusion model into a theoretically principled posterior sampling scheme. Experiments on blind image deblurring validate the effectiveness of the proposed method, demonstrating the superior performance of PRISM over state-of-the-art baselines in both image and blur kernel recovery.

## 🔍 Abstract (한글 번역)

arXiv:2509.16106v1 발표 유형: 교차  
초록: 확산 모델은 이제 계산 영상에서 역문제를 해결하는 데 일반적으로 사용됩니다. 그러나 대부분의 확산 기반 역문제 해결기는 사용될 전방 연산자에 대한 완전한 지식을 필요로 합니다. 본 연구에서는 측정 조건부 확산 사전(PRISM)을 갖춘 새로운 확률적이고 강력한 역문제 해결기를 도입하여 블라인드 역문제를 효과적으로 해결합니다. PRISM은 강력한 측정 조건부 확산 모델을 이론적으로 원칙 있는 사후 샘플링 방식에 통합함으로써 현재 방법에 비해 기술적 진보를 제공합니다. 블라인드 이미지 디블러링에 대한 실험은 제안된 방법의 효과를 검증하며, 이미지 및 블러 커널 복원에서 최첨단 기준선보다 PRISM의 우수한 성능을 입증합니다.

## 📝 요약

이 논문에서는 측정 조건 확산 사전(PRISM)을 활용한 새로운 확률적이고 강력한 역문제 해결 방법을 제안합니다. 기존의 확산 기반 역문제 해결 방법은 전방 연산자에 대한 완전한 지식을 필요로 하지만, PRISM은 이 제한을 극복하여 블라인드 역문제를 효과적으로 해결합니다. 이 방법은 강력한 측정 조건 확산 모델을 이론적으로 정립된 사후 샘플링 방식에 통합하여 기술적 진보를 이룹니다. 블라인드 이미지 디블러링 실험을 통해 PRISM의 효과가 입증되었으며, 이미지 및 블러 커널 복원에서 최첨단 기준을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 확산 모델은 계산 영상에서 역문제를 해결하는 데 일반적으로 사용된다.
- 2. 대부분의 확산 기반 역문제 해결기는 전방 연산자에 대한 완전한 지식을 필요로 한다.
- 3. PRISM은 측정 조건부 확산 모델을 활용하여 맹목적 역문제를 효과적으로 해결하는 새로운 확률적이고 견고한 역문제 해결기를 제안한다.
- 4. PRISM은 이론적으로 원칙에 입각한 사후 샘플링 방식을 통해 기술적 진보를 제공한다.
- 5. 실험 결과, PRISM은 맹목적 이미지 디블러링에서 최첨단 기준을 능가하는 성능을 보여준다.


---

*Generated on 2025-09-23 10:57:07*