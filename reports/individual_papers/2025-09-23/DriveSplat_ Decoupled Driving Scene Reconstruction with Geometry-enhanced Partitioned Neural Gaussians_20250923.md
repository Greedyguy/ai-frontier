---
keywords:
  - 3D Scene Reconstruction
  - Neural Gaussian Representations
  - Dynamic-Static Decoupling
  - Waymo and KITTI Datasets
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2508.15376
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:29:58.738881",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Scene Reconstruction",
    "Neural Gaussian Representations",
    "Dynamic-Static Decoupling",
    "Waymo and KITTI Datasets"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Scene Reconstruction": 0.78,
    "Neural Gaussian Representations": 0.75,
    "Dynamic-Static Decoupling": 0.72,
    "Waymo and KITTI Datasets": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D scene reconstruction",
        "canonical": "3D Scene Reconstruction",
        "aliases": [
          "3D reconstruction",
          "scene reconstruction"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in computer vision, linking to various reconstruction techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Gaussian representations",
        "canonical": "Neural Gaussian Representations",
        "aliases": [
          "Gaussian representations",
          "neural Gaussians"
        ],
        "category": "unique_technical",
        "rationale": "A unique approach in the paper, offering a new method for scene reconstruction.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "dynamic-static decoupling",
        "canonical": "Dynamic-Static Decoupling",
        "aliases": [
          "decoupling dynamic and static",
          "dynamic-static separation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's methodology, enhancing understanding of motion handling.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Waymo and KITTI datasets",
        "canonical": "Waymo and KITTI Datasets",
        "aliases": [
          "Waymo dataset",
          "KITTI dataset"
        ],
        "category": "specific_connectable",
        "rationale": "These datasets are widely used benchmarks in autonomous driving research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "novel views"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D scene reconstruction",
      "resolved_canonical": "3D Scene Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Gaussian representations",
      "resolved_canonical": "Neural Gaussian Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "dynamic-static decoupling",
      "resolved_canonical": "Dynamic-Static Decoupling",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Waymo and KITTI datasets",
      "resolved_canonical": "Waymo and KITTI Datasets",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.68,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15376.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2508.15376](https://arxiv.org/abs/2508.15376)

## 🔗 유사한 논문
- [[2025-09-23/From Restoration to Reconstruction_ Rethinking 3D Gaussian Splatting for Underwater Scenes_20250923|From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes]] (86.7% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (85.9% similar)
- [[2025-09-23/SPFSplatV2_ Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views_20250923|SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views]] (85.5% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (85.1% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Scene Reconstruction|3D Scene Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Waymo and KITTI Datasets|Waymo and KITTI Datasets]]
**⚡ Unique Technical**: [[keywords/Neural Gaussian Representations|Neural Gaussian Representations]], [[keywords/Dynamic-Static Decoupling|Dynamic-Static Decoupling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15376v3 Announce Type: replace 
Abstract: In the realm of driving scenarios, the presence of rapidly moving vehicles, pedestrians in motion, and large-scale static backgrounds poses significant challenges for 3D scene reconstruction. Recent methods based on 3D Gaussian Splatting address the motion blur problem by decoupling dynamic and static components within the scene. However, these decoupling strategies overlook background optimization with adequate geometry relationships and rely solely on fitting each training view by adding Gaussians. Therefore, these models exhibit limited robustness in rendering novel views and lack an accurate geometric representation. To address the above issues, we introduce DriveSplat, a high-quality reconstruction method for driving scenarios based on neural Gaussian representations with dynamic-static decoupling. To better accommodate the predominantly linear motion patterns of driving viewpoints, a region-wise voxel initialization scheme is employed, which partitions the scene into near, middle, and far regions to enhance close-range detail representation. Deformable neural Gaussians are introduced to model non-rigid dynamic actors, whose parameters are temporally adjusted by a learnable deformation network. The entire framework is further supervised by depth and normal priors from pre-trained models, improving the accuracy of geometric structures. Our method has been rigorously evaluated on the Waymo and KITTI datasets, demonstrating state-of-the-art performance in novel-view synthesis for driving scenarios.

## 📝 요약

논문은 운전 시나리오에서 3D 장면 재구성의 어려움을 해결하기 위해 DriveSplat이라는 새로운 방법을 제안합니다. 기존의 3D Gaussian Splatting 기반 방법들이 동적 및 정적 요소를 분리하지만, 배경 최적화와 정확한 기하학적 표현에 한계가 있었습니다. DriveSplat은 동적-정적 분리를 통해 고품질 재구성을 제공하며, 장면을 근거리, 중거리, 원거리로 나누어 세부 표현을 강화합니다. 비강체 동적 객체를 모델링하기 위해 변형 가능한 신경 가우시안을 도입하고, 학습 가능한 변형 네트워크로 매개변수를 조정합니다. 또한, 사전 학습된 모델의 깊이 및 법선 정보를 사용하여 기하학적 구조의 정확성을 높입니다. Waymo와 KITTI 데이터셋에서 평가한 결과, 새로운 시점 합성에서 최첨단 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. 3D 장면 재구성에서 동적 및 정적 요소를 분리하여 모션 블러 문제를 해결하는 3D Gaussian Splatting 기반의 최신 방법들이 존재합니다.
- 2. 기존 방법들은 배경 최적화와 정확한 기하학적 표현이 부족하여 새로운 시점에서의 렌더링에 한계가 있습니다.
- 3. DriveSplat은 동적-정적 분리를 기반으로 한 신경망 Gaussian 표현을 사용하여 운전 시나리오의 고품질 재구성을 제공합니다.
- 4. 장면을 근거리, 중간 거리, 원거리로 나누는 지역별 복셀 초기화 방식을 통해 근거리 세부 표현을 향상시킵니다.
- 5. Waymo와 KITTI 데이터셋에서 DriveSplat의 성능을 평가한 결과, 운전 시나리오의 새로운 시점 합성에서 최첨단 성능을 입증했습니다.


---

*Generated on 2025-09-24 05:29:58*