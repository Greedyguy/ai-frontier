---
keywords:
  - Panoptic Symbol Spotting
  - 3D Point Cloud Model
  - Sliding Window Aggregation
  - Non-Maximum Suppression
  - LS-CAD Dataset
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2412.07377
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:29:33.909850",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Panoptic Symbol Spotting",
    "3D Point Cloud Model",
    "Sliding Window Aggregation",
    "Non-Maximum Suppression",
    "LS-CAD Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Panoptic Symbol Spotting": 0.78,
    "3D Point Cloud Model": 0.82,
    "Sliding Window Aggregation": 0.75,
    "Non-Maximum Suppression": 0.8,
    "LS-CAD Dataset": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "panoptic symbol spotting",
        "canonical": "Panoptic Symbol Spotting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach specific to the paper's focus on identifying symbols in CAD drawings.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D point cloud model",
        "canonical": "3D Point Cloud Model",
        "aliases": [
          "Point Cloud Representation"
        ],
        "category": "broad_technical",
        "rationale": "The use of 3D point clouds is a key technical aspect that connects to broader topics in computer vision and CAD analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Sliding Window Aggregation",
        "canonical": "Sliding Window Aggregation",
        "aliases": [
          "SWA"
        ],
        "category": "unique_technical",
        "rationale": "This technique is introduced as a novel method for improving segmentation accuracy in large-scale CAD drawings.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Non-Maximum Suppression",
        "canonical": "Non-Maximum Suppression",
        "aliases": [
          "NMS"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known technique in object detection that enhances the connectivity with existing computer vision methodologies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "LS-CAD",
        "canonical": "LS-CAD Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A new dataset introduced in the paper, crucial for future research and benchmarking in CAD analysis.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.95,
        "link_intent_score": 0.85
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
      "candidate_surface": "panoptic symbol spotting",
      "resolved_canonical": "Panoptic Symbol Spotting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D point cloud model",
      "resolved_canonical": "3D Point Cloud Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Sliding Window Aggregation",
      "resolved_canonical": "Sliding Window Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Non-Maximum Suppression",
      "resolved_canonical": "Non-Maximum Suppression",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LS-CAD",
      "resolved_canonical": "LS-CAD Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.95,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# CADSpotting: Robust Panoptic Symbol Spotting on Large-Scale CAD Drawings

**Korean Title:** CADSpotting: 대규모 CAD 도면에서의 강력한 범용 심볼 탐지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.07377.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2412.07377](https://arxiv.org/abs/2412.07377)

## 🔗 유사한 논문
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (82.9% similar)
- [[2025-09-22/cadrille_ Multi-modal CAD Reconstruction with Online Reinforcement Learning_20250922|cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning]] (82.9% similar)
- [[2025-09-22/Img2CAD_ Reverse Engineering 3D CAD Models from Images through VLM-Assisted Conditional Factorization_20250922|Img2CAD: Reverse Engineering 3D CAD Models from Images through VLM-Assisted Conditional Factorization]] (82.1% similar)
- [[2025-09-22/FloorSAM_ SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion_20250922|FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion]] (81.9% similar)
- [[2025-09-22/CAGE_ Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction_20250922|CAGE: Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Point Cloud Model|3D Point Cloud Model]]
**🔗 Specific Connectable**: [[keywords/Non-Maximum Suppression|Non-Maximum Suppression]]
**⚡ Unique Technical**: [[keywords/Panoptic Symbol Spotting|Panoptic Symbol Spotting]], [[keywords/Sliding Window Aggregation|Sliding Window Aggregation]], [[keywords/LS-CAD Dataset|LS-CAD Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.07377v4 Announce Type: replace 
Abstract: We introduce CADSpotting, an effective method for panoptic symbol spotting in large-scale architectural CAD drawings. Existing approaches often struggle with symbol diversity, scale variations, and overlapping elements in CAD designs, and typically rely on additional features (e.g., primitive types or graphical layers) to improve performance. CADSpotting overcomes these challenges by representing primitives through densely sampled points with only coordinate attributes, using a unified 3D point cloud model for robust feature learning. To enable accurate segmentation in large drawings, we further propose a novel Sliding Window Aggregation (SWA) technique that combines weighted voting and Non-Maximum Suppression (NMS). Moreover, we introduce LS-CAD, a new large-scale dataset comprising 45 finely annotated floorplans, each covering approximately 1,000 $m^2$, significantly larger than prior benchmarks. LS-CAD will be publicly released to support future research. Experiments on FloorPlanCAD and LS-CAD demonstrate that CADSpotting significantly outperforms existing methods. We also showcase its practical value by enabling automated parametric 3D interior reconstruction directly from raw CAD inputs.

## 🔍 Abstract (한글 번역)

arXiv:2412.07377v4 발표 유형: 교체  
초록: 우리는 대규모 건축 CAD 도면에서 전반적인 심볼 탐지를 위한 효과적인 방법인 CADSpotting을 소개합니다. 기존 접근 방식은 CAD 설계에서 심볼의 다양성, 규모의 변동, 겹치는 요소들에 종종 어려움을 겪으며, 성능 향상을 위해 추가적인 특징(예: 기본 유형 또는 그래픽 레이어)에 의존하는 경우가 많습니다. CADSpotting은 좌표 속성만을 가진 조밀하게 샘플링된 점을 통해 기본 요소를 표현하고, 강력한 특징 학습을 위한 통합 3D 포인트 클라우드 모델을 사용하여 이러한 문제를 극복합니다. 대규모 도면에서 정확한 세분화를 가능하게 하기 위해, 우리는 가중치 투표와 비최대 억제(NMS)를 결합한 새로운 슬라이딩 윈도우 집계(SWA) 기법을 제안합니다. 또한, 우리는 45개의 정밀하게 주석이 달린 도면을 포함하는 새로운 대규모 데이터셋인 LS-CAD를 소개하며, 각각 약 1,000 $m^2$를 커버하여 이전 벤치마크보다 훨씬 큽니다. LS-CAD는 향후 연구를 지원하기 위해 공개될 예정입니다. FloorPlanCAD와 LS-CAD에 대한 실험은 CADSpotting이 기존 방법을 크게 능가함을 보여줍니다. 우리는 또한 원시 CAD 입력에서 직접 자동화된 매개변수 3D 내부 재구성을 가능하게 함으로써 그 실용적 가치를 입증합니다.

## 📝 요약

CADSpotting은 대규모 건축 CAD 도면에서 파노라마 심볼 탐지를 위한 효과적인 방법입니다. 기존 방법들이 심볼 다양성, 규모 변동, 겹치는 요소들로 인해 어려움을 겪는 반면, CADSpotting은 좌표 속성만을 가진 조밀한 샘플링 포인트로 원시 데이터를 표현하여 강력한 특징 학습을 위한 통합 3D 포인트 클라우드 모델을 사용합니다. 정확한 분할을 위해 가중치 투표와 비최대 억제를 결합한 새로운 슬라이딩 윈도우 집계(SWA) 기법을 제안합니다. 또한, 45개의 정교하게 주석된 대규모 데이터셋 LS-CAD를 소개하며, 이는 기존 벤치마크보다 훨씬 큽니다. 실험 결과 CADSpotting은 기존 방법들보다 뛰어난 성능을 보였으며, 원시 CAD 입력으로부터 자동화된 매개변수 3D 내부 재구성을 가능하게 합니다.

## 🎯 주요 포인트

- 1. CADSpotting은 대규모 건축 CAD 도면에서 파노라마 심볼 탐지를 위한 효과적인 방법을 제안합니다.
- 2. CADSpotting은 좌표 속성만을 사용하여 조밀하게 샘플링된 점을 통해 원시 요소를 표현하고, 통합된 3D 포인트 클라우드 모델을 사용하여 강력한 특징 학습을 수행합니다.
- 3. 대형 도면에서의 정확한 분할을 위해 가중치 투표와 비최대 억제를 결합한 새로운 슬라이딩 윈도우 집계(SWA) 기법을 제안합니다.
- 4. LS-CAD는 약 1,000㎡를 커버하는 45개의 정밀하게 주석이 달린 평면도를 포함하는 새로운 대규모 데이터셋으로, 향후 연구를 지원하기 위해 공개될 예정입니다.
- 5. FloorPlanCAD와 LS-CAD 실험에서 CADSpotting은 기존 방법들보다 성능이 뛰어남을 입증하였으며, 원시 CAD 입력으로부터 자동화된 매개변수 3D 내부 재구성을 가능하게 하는 실용적 가치를 보여줍니다.


---

*Generated on 2025-09-23 12:29:33*