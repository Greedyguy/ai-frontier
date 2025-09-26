---
keywords:
  - 3D Gaussian Splatting
  - Driving Scene Completion
  - Structural Matching
  - Substitution-and-Fusion Optimization
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19937
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:09:58.010624",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Driving Scene Completion",
    "Structural Matching",
    "Substitution-and-Fusion Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Driving Scene Completion": 0.72,
    "Structural Matching": 0.68,
    "Substitution-and-Fusion Optimization": 0.7
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
        "rationale": "This term is central to the paper's method and represents a novel approach to scene inpainting.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Driving Scene Completion",
        "canonical": "Driving Scene Completion",
        "aliases": [
          "Driving Scene Inpainting"
        ],
        "category": "unique_technical",
        "rationale": "The term is specific to the application domain of the method, providing a clear context for linking related works.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Structural Matching",
        "canonical": "Structural Matching",
        "aliases": [
          "Pattern Matching"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the method's approach to finding similar patterns in 3D space.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.68
      },
      {
        "surface": "Substitution-and-Fusion Optimization",
        "canonical": "Substitution-and-Fusion Optimization",
        "aliases": [
          "Fusion Optimization"
        ],
        "category": "unique_technical",
        "rationale": "This optimization technique is a key part of the method, enhancing visual harmony in the inpainting process.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Driving Scene Completion",
      "resolved_canonical": "Driving Scene Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Structural Matching",
      "resolved_canonical": "Structural Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Substitution-and-Fusion Optimization",
      "resolved_canonical": "Substitution-and-Fusion Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for Driving Scenes

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19937.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19937](https://arxiv.org/abs/2509.19937)

## 🔗 유사한 논문
- [[2025-09-24/Gaussian Herding across Pens_ An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS_20250924|Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS]] (87.1% similar)
- [[2025-09-24/FixingGS_ Enhancing 3D Gaussian Splatting via Training-Free Score Distillation_20250924|FixingGS: Enhancing 3D Gaussian Splatting via Training-Free Score Distillation]] (86.8% similar)
- [[2025-09-23/DriveSplat_ Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians_20250923|DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians]] (86.1% similar)
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (84.8% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Structural Matching|Structural Matching]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Driving Scene Completion|Driving Scene Completion]], [[keywords/Substitution-and-Fusion Optimization|Substitution-and-Fusion Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19937v1 Announce Type: new 
Abstract: This paper presents GS-RoadPatching, an inpainting method for driving scene completion by referring to completely reconstructed regions, which are represented by 3D Gaussian Splatting (3DGS). Unlike existing 3DGS inpainting methods that perform generative completion relying on 2D perspective-view-based diffusion or GAN models to predict limited appearance or depth cues for missing regions, our approach enables substitutional scene inpainting and editing directly through the 3DGS modality, extricating it from requiring spatial-temporal consistency of 2D cross-modals and eliminating the need for time-intensive retraining of Gaussians. Our key insight is that the highly repetitive patterns in driving scenes often share multi-modal similarities within the implicit 3DGS feature space and are particularly suitable for structural matching to enable effective 3DGS-based substitutional inpainting. Practically, we construct feature-embedded 3DGS scenes to incorporate a patch measurement method for abstracting local context at different scales and, subsequently, propose a structural search method to find candidate patches in 3D space effectively. Finally, we propose a simple yet effective substitution-and-fusion optimization for better visual harmony. We conduct extensive experiments on multiple publicly available datasets to demonstrate the effectiveness and efficiency of our proposed method in driving scenes, and the results validate that our method achieves state-of-the-art performance compared to the baseline methods in terms of both quality and interoperability. Additional experiments in general scenes also demonstrate the applicability of the proposed 3D inpainting strategy. The project page and code are available at: https://shanzhaguoo.github.io/GS-RoadPatching/

## 📝 요약

이 논문은 3D Gaussian Splatting(3DGS)을 활용한 주행 장면 보완 기법인 GS-RoadPatching을 제안합니다. 기존의 2D 기반 기법과 달리, 3DGS를 통해 직접적인 장면 보완과 편집이 가능하며, 이는 2D 모달 간의 일관성을 요구하지 않고 시간 소모적인 재훈련을 피할 수 있습니다. 주행 장면의 반복적인 패턴을 활용하여 3DGS 기반의 구조적 매칭을 통해 효과적인 보완을 수행합니다. 제안된 방법은 다양한 데이터셋에서 실험을 통해 기존 방법들보다 뛰어난 성능을 입증했으며, 일반 장면에서도 적용 가능성을 보였습니다.

## 🎯 주요 포인트

- 1. GS-RoadPatching은 3D Gaussian Splatting을 활용하여 운전 장면의 결손 부분을 보완하는 인페인팅 방법을 제안합니다.
- 2. 기존의 2D 기반 생성 모델과 달리, 3DGS 모달리티를 통해 공간-시간적 일관성을 요구하지 않고 직접적인 장면 보완 및 편집이 가능합니다.
- 3. 운전 장면의 반복적인 패턴을 활용하여 3DGS 기반의 구조적 매칭을 통해 효과적인 대체 인페인팅을 구현합니다.
- 4. 다양한 스케일에서 지역적 맥락을 추상화하는 패치 측정 방법과 3D 공간에서 후보 패치를 찾는 구조적 검색 방법을 제안합니다.
- 5. 제안된 방법은 여러 공개 데이터셋에서 실험을 통해 기존 방법들보다 우수한 성능을 보이며, 일반 장면에서도 적용 가능성을 입증합니다.


---

*Generated on 2025-09-26 09:09:58*