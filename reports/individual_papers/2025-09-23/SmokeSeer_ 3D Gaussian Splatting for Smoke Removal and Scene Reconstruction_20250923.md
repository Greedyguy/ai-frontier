---
keywords:
  - 3D Gaussian Splatting
  - Smoke Removal
  - Scene Reconstruction
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17329
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:49:19.138032",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Smoke Removal",
    "Scene Reconstruction",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Smoke Removal": 0.8,
    "Scene Reconstruction": 0.75,
    "Multimodal Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel technique used for fusing information from different image modalities, crucial for the paper's methodology.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Smoke Removal",
        "canonical": "Smoke Removal",
        "aliases": [
          "Dehazing",
          "Smoke Elimination"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's contribution, connecting to broader themes in image restoration.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Scene Reconstruction",
        "canonical": "Scene Reconstruction",
        "aliases": [
          "3D Scene Reconstruction"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in computer vision, linking to various reconstruction techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "Thermal and RGB Images",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Thermal Imaging",
          "RGB Imaging"
        ],
        "category": "specific_connectable",
        "rationale": "The use of multiple image modalities is key to the paper's approach, connecting to multimodal learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "data"
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
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Smoke Removal",
      "resolved_canonical": "Smoke Removal",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Scene Reconstruction",
      "resolved_canonical": "Scene Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Thermal and RGB Images",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# SmokeSeer: 3D Gaussian Splatting for Smoke Removal and Scene Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17329.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17329](https://arxiv.org/abs/2509.17329)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (81.3% similar)
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (80.7% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (79.9% similar)
- [[2025-09-23/ST-GS_ Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting_20250923|ST-GS: Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting]] (79.5% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Scene Reconstruction|Scene Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Smoke Removal|Smoke Removal]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17329v1 Announce Type: new 
Abstract: Smoke in real-world scenes can severely degrade the quality of images and hamper visibility. Recent methods for image restoration either rely on data-driven priors that are susceptible to hallucinations, or are limited to static low-density smoke. We introduce SmokeSeer, a method for simultaneous 3D scene reconstruction and smoke removal from a video capturing multiple views of a scene. Our method uses thermal and RGB images, leveraging the fact that the reduced scattering in thermal images enables us to see through the smoke. We build upon 3D Gaussian splatting to fuse information from the two image modalities, and decompose the scene explicitly into smoke and non-smoke components. Unlike prior approaches, SmokeSeer handles a broad range of smoke densities and can adapt to temporally varying smoke. We validate our approach on synthetic data and introduce a real-world multi-view smoke dataset with RGB and thermal images. We provide open-source code and data at the project website.

## 📝 요약

SmokeSeer는 다중 시점의 비디오를 통해 3D 장면을 재구성하고 연기를 제거하는 방법을 제안합니다. 이 방법은 열화상과 RGB 이미지를 활용하여 연기를 투과할 수 있는 열화상의 특성을 이용합니다. 3D Gaussian splatting을 기반으로 두 이미지 모달리티의 정보를 융합하고, 장면을 연기와 비연기 구성 요소로 명확히 분해합니다. 기존 방법과 달리, SmokeSeer는 다양한 밀도의 연기를 처리할 수 있으며 시간에 따라 변하는 연기에도 적응할 수 있습니다. 우리는 합성 데이터와 실제 다중 시점 연기 데이터셋을 통해 방법의 유효성을 검증하였으며, 프로젝트 웹사이트에 오픈 소스 코드와 데이터를 제공합니다.

## 🎯 주요 포인트

- 1. SmokeSeer는 비디오에서 다중 뷰를 활용하여 3D 장면 재구성과 연기 제거를 동시에 수행하는 방법을 제안합니다.
- 2. 이 방법은 열화상과 RGB 이미지를 사용하여 연기를 투과할 수 있는 열화상의 특성을 활용합니다.
- 3. 3D Gaussian splatting을 기반으로 두 이미지 모달리티의 정보를 융합하고, 장면을 연기와 비연기 구성 요소로 명확히 분해합니다.
- 4. SmokeSeer는 다양한 연기 밀도를 처리할 수 있으며, 시간에 따라 변하는 연기에도 적응할 수 있습니다.
- 5. 합성 데이터로 접근 방식을 검증하고, RGB 및 열화상 이미지를 포함한 실제 다중 뷰 연기 데이터셋을 소개합니다.


---

*Generated on 2025-09-24 04:49:19*