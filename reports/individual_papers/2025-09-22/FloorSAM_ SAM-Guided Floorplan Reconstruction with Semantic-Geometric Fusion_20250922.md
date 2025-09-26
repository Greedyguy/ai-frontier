---
keywords:
  - FloorSAM
  - Zero-Shot Learning
  - Point Cloud
  - LiDAR Data
  - Room Segmentation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15750
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:12:08.483811",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FloorSAM",
    "Zero-Shot Learning",
    "Point Cloud",
    "LiDAR Data",
    "Room Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FloorSAM": 0.78,
    "Zero-Shot Learning": 0.8,
    "Point Cloud": 0.75,
    "LiDAR Data": 0.77,
    "Room Segmentation": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FloorSAM",
        "canonical": "FloorSAM",
        "aliases": [
          "SAM-Guided Floorplan Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel framework specifically designed for floor plan reconstruction, crucial for linking to related research in indoor mapping.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSL"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of a trending learning paradigm that enhances the model's ability to generalize across diverse layouts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Point Cloud",
        "canonical": "Point Cloud",
        "aliases": [
          "3D Point Cloud"
        ],
        "category": "broad_technical",
        "rationale": "Essential for understanding the data type used in the reconstruction process, linking to broader topics in 3D data processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "LiDAR Data",
        "canonical": "LiDAR Data",
        "aliases": [
          "LiDAR Point Cloud"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for linking to discussions on data acquisition methods in indoor mapping and reconstruction.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Room Segmentation",
        "canonical": "Room Segmentation",
        "aliases": [
          "Room Masking"
        ],
        "category": "specific_connectable",
        "rationale": "Key process in the framework that connects to broader themes in image processing and segmentation tasks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "geometric algorithms",
      "traditional methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "FloorSAM",
      "resolved_canonical": "FloorSAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Point Cloud",
      "resolved_canonical": "Point Cloud",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "LiDAR Data",
      "resolved_canonical": "LiDAR Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Room Segmentation",
      "resolved_canonical": "Room Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion

**Korean Title:** FloorSAM: 의미-기하 융합을 통한 SAM 기반 평면도 복원

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15750.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15750](https://arxiv.org/abs/2509.15750)

## 🔗 유사한 논문
- [[2025-09-22/CAGE_ Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction_20250922|CAGE: Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction]] (82.5% similar)
- [[2025-09-22/RangeSAM_ Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation_20250922|RangeSAM: Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation]] (82.2% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (82.1% similar)
- [[2025-09-22/CADSpotting_ Robust Panoptic Symbol Spotting on Large-Scale CAD Drawings_20250922|CADSpotting: Robust Panoptic Symbol Spotting on Large-Scale CAD Drawings]] (81.9% similar)
- [[2025-09-18/BIM Informed Visual SLAM for Construction Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Point Cloud|Point Cloud]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/LiDAR Data|LiDAR Data]], [[keywords/Room Segmentation|Room Segmentation]]
**⚡ Unique Technical**: [[keywords/FloorSAM|FloorSAM]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15750v1 Announce Type: cross 
Abstract: Reconstructing building floor plans from point cloud data is key for indoor navigation, BIM, and precise measurements. Traditional methods like geometric algorithms and Mask R-CNN-based deep learning often face issues with noise, limited generalization, and loss of geometric details. We propose FloorSAM, a framework that integrates point cloud density maps with the Segment Anything Model (SAM) for accurate floor plan reconstruction from LiDAR data. Using grid-based filtering, adaptive resolution projection, and image enhancement, we create robust top-down density maps. FloorSAM uses SAM's zero-shot learning for precise room segmentation, improving reconstruction across diverse layouts. Room masks are generated via adaptive prompt points and multistage filtering, followed by joint mask and point cloud analysis for contour extraction and regularization. This produces accurate floor plans and recovers room topological relationships. Tests on Giblayout and ISPRS datasets show better accuracy, recall, and robustness than traditional methods, especially in noisy and complex settings. Code and materials: github.com/Silentbarber/FloorSAM.

## 🔍 Abstract (한글 번역)

arXiv:2509.15750v1 발표 유형: 교차  
초록: 점군 데이터로부터 건물 평면도를 재구성하는 것은 실내 내비게이션, BIM, 정밀 측정에 있어 핵심적입니다. 기하학적 알고리즘이나 Mask R-CNN 기반의 딥러닝과 같은 전통적인 방법은 종종 노이즈, 제한된 일반화, 기하학적 세부사항의 손실과 같은 문제에 직면합니다. 우리는 LiDAR 데이터를 통해 정확한 평면도 재구성을 위해 점군 밀도 지도와 Segment Anything Model (SAM)을 통합한 프레임워크인 FloorSAM을 제안합니다. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 사용하여 견고한 탑다운 밀도 지도를 생성합니다. FloorSAM은 SAM의 제로샷 학습을 사용하여 다양한 레이아웃에서의 재구성을 개선하는 정밀한 방 분할을 수행합니다. 방 마스크는 적응형 프롬프트 포인트와 다단계 필터링을 통해 생성되며, 이후 마스크와 점군의 공동 분석을 통해 윤곽 추출 및 정규화를 수행합니다. 이는 정확한 평면도를 생성하고 방의 위상 관계를 복원합니다. Giblayout 및 ISPRS 데이터셋에 대한 테스트 결과, 특히 노이즈가 많고 복잡한 환경에서 전통적인 방법보다 더 나은 정확도, 재현율 및 견고성을 보여줍니다. 코드 및 자료: github.com/Silentbarber/FloorSAM.

## 📝 요약

FloorSAM은 LiDAR 데이터로부터 정확한 건물 평면도를 재구성하기 위해 개발된 프레임워크로, 실내 내비게이션 및 BIM에 유용합니다. 기존의 기하학적 알고리즘과 Mask R-CNN 기반 방법론이 가진 노이즈와 일반화 문제를 해결하기 위해, FloorSAM은 포인트 클라우드 밀도 지도와 Segment Anything Model (SAM)을 통합합니다. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 통해 강력한 밀도 지도를 생성하고, SAM의 제로샷 학습을 활용해 다양한 레이아웃에서 정확한 방 분할을 수행합니다. 적응형 프롬프트 포인트와 다단계 필터링을 통해 생성된 방 마스크는 포인트 클라우드와의 공동 분석을 통해 윤곽 추출 및 정규화를 거쳐 정확한 평면도와 방의 위상 관계를 복원합니다. Giblayout 및 ISPRS 데이터셋 테스트 결과, 기존 방법보다 정확도, 재현율, 강건성에서 우수한 성능을 보였습니다. 코드와 자료는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. FloorSAM은 LiDAR 데이터를 활용하여 포인트 클라우드 밀도 지도와 Segment Anything Model (SAM)을 통합하여 정확한 건물 평면도를 재구성하는 프레임워크입니다.
- 2. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 통해 강력한 상단 밀도 지도를 생성합니다.
- 3. SAM의 제로샷 학습을 활용하여 다양한 레이아웃에서 정확한 방 세분화를 수행하며, 적응형 프롬프트 포인트와 다단계 필터링을 통해 방 마스크를 생성합니다.
- 4. Giblayout 및 ISPRS 데이터셋에서 테스트한 결과, 전통적인 방법보다 노이즈가 많고 복잡한 환경에서도 더 나은 정확도, 재현율 및 강건성을 보여줍니다.
- 5. 코드와 자료는 GitHub에서 제공됩니다: github.com/Silentbarber/FloorSAM.


---

*Generated on 2025-09-23 09:12:08*