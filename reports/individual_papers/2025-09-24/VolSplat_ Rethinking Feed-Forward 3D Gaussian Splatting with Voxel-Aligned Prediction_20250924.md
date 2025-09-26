<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:21:23.536819",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Voxel-Aligned Prediction",
    "Novel View Synthesis",
    "Multi-view Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Voxel-Aligned Prediction": 0.78,
    "Novel View Synthesis": 0.82,
    "Multi-view Consistency": 0.77
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
        "rationale": "This is a unique technique central to the paper's contribution, offering a new approach to 3D reconstruction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Voxel-Aligned Prediction",
        "canonical": "Voxel-Aligned Prediction",
        "aliases": [
          "Voxel Alignment"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach introduced in the paper, differentiating it from existing methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Novel View Synthesis",
        "canonical": "Novel View Synthesis",
        "aliases": [
          "View Synthesis"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area for the discussed techniques, linking to broader research in computer graphics and vision.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-view Consistency",
        "canonical": "Multi-view Consistency",
        "aliases": [
          "Multi-view Consistency"
        ],
        "category": "specific_connectable",
        "rationale": "Ensures robust 3D reconstruction, a critical aspect of the paper's proposed method.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Voxel-Aligned Prediction",
      "resolved_canonical": "Voxel-Aligned Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Novel View Synthesis",
      "resolved_canonical": "Novel View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-view Consistency",
      "resolved_canonical": "Multi-view Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# VolSplat: Rethinking Feed-Forward 3D Gaussian Splatting with Voxel-Aligned Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19297.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19297](https://arxiv.org/abs/2509.19297)

## 🔗 유사한 논문
- [[2025-09-23/SPFSplatV2_ Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views_20250923|SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views]] (89.1% similar)
- [[2025-09-23/DriveSplat_ Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians_20250923|DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians]] (89.0% similar)
- [[2025-09-24/Variational Bayes Gaussian Splatting_20250924|Variational Bayes Gaussian Splatting]] (88.4% similar)
- [[2025-09-23/GeoSplat_ A Deep Dive into Geometry-Constrained Gaussian Splatting_20250923|GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting]] (88.3% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (87.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Novel View Synthesis|Novel View Synthesis]], [[keywords/Multi-view Consistency|Multi-view Consistency]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Voxel-Aligned Prediction|Voxel-Aligned Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19297v1 Announce Type: new 
Abstract: Feed-forward 3D Gaussian Splatting (3DGS) has emerged as a highly effective solution for novel view synthesis. Existing methods predominantly rely on a pixel-aligned Gaussian prediction paradigm, where each 2D pixel is mapped to a 3D Gaussian. We rethink this widely adopted formulation and identify several inherent limitations: it renders the reconstructed 3D models heavily dependent on the number of input views, leads to view-biased density distributions, and introduces alignment errors, particularly when source views contain occlusions or low texture. To address these challenges, we introduce VolSplat, a new multi-view feed-forward paradigm that replaces pixel alignment with voxel-aligned Gaussians. By directly predicting Gaussians from a predicted 3D voxel grid, it overcomes pixel alignment's reliance on error-prone 2D feature matching, ensuring robust multi-view consistency. Furthermore, it enables adaptive control over Gaussian density based on 3D scene complexity, yielding more faithful Gaussian point clouds, improved geometric consistency, and enhanced novel-view rendering quality. Experiments on widely used benchmarks including RealEstate10K and ScanNet demonstrate that VolSplat achieves state-of-the-art performance while producing more plausible and view-consistent Gaussian reconstructions. In addition to superior results, our approach establishes a more scalable framework for feed-forward 3D reconstruction with denser and more robust representations, paving the way for further research in wider communities. The video results, code and trained models are available on our project page: https://lhmd.top/volsplat.

## 📝 요약

3D Gaussian Splatting(3DGS)은 새로운 시점 합성에 효과적이지만, 기존의 픽셀 정렬 방식은 입력 시점 수에 의존적이며, 시점 편향 밀도 분포와 정렬 오류를 초래합니다. 이를 해결하기 위해, 우리는 VolSplat을 제안합니다. VolSplat은 픽셀 대신 보컬 정렬된 가우시안을 사용하여 3D 보컬 그리드에서 직접 가우시안을 예측합니다. 이는 2D 특징 매칭의 오류를 줄이고, 3D 장면 복잡성에 따라 가우시안 밀도를 조절하여 더 정확한 포인트 클라우드와 향상된 시점 렌더링 품질을 제공합니다. RealEstate10K와 ScanNet 벤치마크 실험에서 VolSplat은 최첨단 성능을 보이며, 더 신뢰성 있는 가우시안 재구성을 달성했습니다. 이 접근법은 더 밀도 있고 견고한 표현을 통해 3D 재구성의 확장 가능한 프레임워크를 확립하며, 추가 연구의 길을 열어줍니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting의 기존 방식은 입력 뷰 수에 의존적이며, 시점 편향 밀도 분포와 정렬 오류를 초래할 수 있습니다.
- 2. VolSplat은 픽셀 정렬 대신 보컬 정렬 가우시안을 사용하여 다중 뷰 일관성을 보장합니다.
- 3. VolSplat은 3D 장면 복잡성에 따라 가우시안 밀도를 조절할 수 있어, 보다 정확한 가우시안 포인트 클라우드와 향상된 기하학적 일관성을 제공합니다.
- 4. RealEstate10K 및 ScanNet 벤치마크 실험에서 VolSplat은 최첨단 성능을 달성하며, 보다 그럴듯하고 시점 일관적인 가우시안 재구성을 보여줍니다.
- 5. VolSplat은 밀도 높고 견고한 표현을 통해 피드포워드 3D 재구성의 확장 가능한 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 16:21:23*