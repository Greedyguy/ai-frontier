---
keywords:
  - Camera Splatting
  - View Optimization
  - Novel View Synthesis
  - Point Cameras
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15677
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:05:33.503614",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Camera Splatting",
    "View Optimization",
    "Novel View Synthesis",
    "Point Cameras"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Camera Splatting": 0.8,
    "View Optimization": 0.75,
    "Novel View Synthesis": 0.78,
    "Point Cameras": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Camera Splatting",
        "canonical": "Camera Splatting",
        "aliases": [
          "3D Gaussian Splatting",
          "View Optimization Framework"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for view synthesis, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "View Optimization",
        "canonical": "View Optimization",
        "aliases": [
          "Continuous View Optimization"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking to other works on optimization techniques in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Novel View Synthesis",
        "canonical": "Novel View Synthesis",
        "aliases": [
          "View Synthesis"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on generating new perspectives, linking to broader synthesis research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.82,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Point Cameras",
        "canonical": "Point Cameras",
        "aliases": [
          "Virtual Cameras"
        ],
        "category": "unique_technical",
        "rationale": "Unique concept in the paper for observing camera splats, enhancing understanding of the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
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
      "candidate_surface": "Camera Splatting",
      "resolved_canonical": "Camera Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "View Optimization",
      "resolved_canonical": "View Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Novel View Synthesis",
      "resolved_canonical": "Novel View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.82,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Point Cameras",
      "resolved_canonical": "Point Cameras",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Camera Splatting for Continuous View Optimization

**Korean Title:** 카메라 스플래팅을 통한 연속적 뷰 최적화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15677.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15677](https://arxiv.org/abs/2509.15677)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (83.6% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (81.9% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (80.8% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (80.1% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/View Optimization|View Optimization]], [[keywords/Novel View Synthesis|Novel View Synthesis]]
**⚡ Unique Technical**: [[keywords/Camera Splatting|Camera Splatting]], [[keywords/Point Cameras|Point Cameras]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15677v1 Announce Type: new 
Abstract: We propose Camera Splatting, a novel view optimization framework for novel view synthesis. Each camera is modeled as a 3D Gaussian, referred to as a camera splat, and virtual cameras, termed point cameras, are placed at 3D points sampled near the surface to observe the distribution of camera splats. View optimization is achieved by continuously and differentiably refining the camera splats so that desirable target distributions are observed from the point cameras, in a manner similar to the original 3D Gaussian splatting. Compared to the Farthest View Sampling (FVS) approach, our optimized views demonstrate superior performance in capturing complex view-dependent phenomena, including intense metallic reflections and intricate textures such as text.

## 🔍 Abstract (한글 번역)

arXiv:2509.15677v1 발표 유형: 신규  
초록: 우리는 새로운 시점 합성을 위한 새로운 시점 최적화 프레임워크인 Camera Splatting을 제안합니다. 각 카메라는 3D 가우시안으로 모델링되며, 이를 카메라 스플랫이라고 합니다. 가상 카메라, 즉 포인트 카메라는 카메라 스플랫의 분포를 관찰하기 위해 표면 근처에서 샘플링된 3D 지점에 배치됩니다. 시점 최적화는 원래의 3D 가우시안 스플래팅과 유사한 방식으로 포인트 카메라에서 원하는 목표 분포가 관찰되도록 카메라 스플랫을 지속적이고 미분 가능하게 정제함으로써 달성됩니다. Farthest View Sampling (FVS) 접근법과 비교할 때, 우리의 최적화된 시점은 강렬한 금속 반사 및 텍스트와 같은 복잡한 텍스처를 포함한 복잡한 시점 의존 현상을 포착하는 데 있어 우수한 성능을 보여줍니다.

## 📝 요약

이 논문에서는 새로운 시점 최적화 프레임워크인 Camera Splatting을 제안합니다. 각 카메라는 3D 가우시안으로 모델링되며, 이를 카메라 스플랫이라 부릅니다. 가상 카메라인 포인트 카메라는 표면 근처의 3D 포인트에 배치되어 카메라 스플랫의 분포를 관찰합니다. 시점 최적화는 포인트 카메라에서 원하는 목표 분포가 관찰되도록 카메라 스플랫을 지속적이고 미분 가능한 방식으로 정제하여 이루어집니다. 이는 기존의 3D 가우시안 스플래팅과 유사한 방식입니다. Farthest View Sampling(FVS) 접근법과 비교했을 때, 최적화된 시점은 복잡한 시점 의존적 현상, 특히 강렬한 금속 반사와 복잡한 텍스처(예: 텍스트)를 더 잘 포착합니다.

## 🎯 주요 포인트

- 1. Camera Splatting은 새로운 시점 최적화 프레임워크로, 3D 가우시안으로 모델링된 카메라 스플랫을 활용합니다.
- 2. 가상 카메라인 포인트 카메라는 표면 근처에서 샘플링된 3D 지점에 배치되어 카메라 스플랫의 분포를 관찰합니다.
- 3. 시점 최적화는 카메라 스플랫을 지속적이고 미분 가능하게 정제하여 포인트 카메라에서 목표 분포를 관찰할 수 있도록 합니다.
- 4. Farthest View Sampling(FVS) 접근법과 비교했을 때, 최적화된 시점은 금속 반사와 복잡한 텍스처와 같은 복잡한 시점 의존적 현상을 더 잘 포착합니다.


---

*Generated on 2025-09-23 12:05:33*