---
keywords:
  - LiDAR-based Two-Stage Transformer
  - Multi-object Tracking
  - Attention Mechanism
  - Temporal Coherence
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2505.12753
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:25:01.971479",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LiDAR-based Two-Stage Transformer",
    "Multi-object Tracking",
    "Attention Mechanism",
    "Temporal Coherence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LiDAR-based Two-Stage Transformer": 0.8,
    "Multi-object Tracking": 0.85,
    "Attention Mechanism": 0.87,
    "Temporal Coherence": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LiDAR-based Two-Stage Transformer",
        "canonical": "LiDAR-based Two-Stage Transformer",
        "aliases": [
          "LiDAR MOT-DETR"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach combining LiDAR data with a two-stage transformer architecture, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-object Tracking",
        "canonical": "Multi-object Tracking",
        "aliases": [
          "MOT"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-object tracking is a key application area for the proposed method, linking it to broader tracking research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attention Block",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Block"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for the transformer architecture and enhance connectivity with existing research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.87
      },
      {
        "surface": "Temporal Coherence",
        "canonical": "Temporal Coherence",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Temporal coherence is critical for maintaining object identities across frames, a unique challenge addressed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
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
      "candidate_surface": "LiDAR-based Two-Stage Transformer",
      "resolved_canonical": "LiDAR-based Two-Stage Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-object Tracking",
      "resolved_canonical": "Multi-object Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attention Block",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Temporal Coherence",
      "resolved_canonical": "Temporal Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# LiDAR MOT-DETR: A LiDAR-based Two-Stage Transformer for 3D Multiple Object Tracking

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.12753.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2505.12753](https://arxiv.org/abs/2505.12753)

## 🔗 유사한 논문
- [[2025-09-23/DepTR-MOT_ Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking_20250923|DepTR-MOT: Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking]] (87.6% similar)
- [[2025-09-23/TinyDef-DETR_ A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery_20250923|TinyDef-DETR: A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery]] (83.7% similar)
- [[2025-09-24/MLF-4DRCNet_ Multi-Level Fusion with 4D Radar and Camera for 3D Object Detection in Autonomous Driving_20250924|MLF-4DRCNet: Multi-Level Fusion with 4D Radar and Camera for 3D Object Detection in Autonomous Driving]] (83.2% similar)
- [[2025-09-24/Track-On2_ Enhancing Online Point Tracking with Memory_20250924|Track-On2: Enhancing Online Point Tracking with Memory]] (82.6% similar)
- [[2025-09-22/LC-SLab -- An Object-based Deep Learning Framework for Large-scale Land Cover Classification from Satellite Imagery and Sparse In-situ Labels_20250922|LC-SLab -- An Object-based Deep Learning Framework for Large-scale Land Cover Classification from Satellite Imagery and Sparse In-situ Labels]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-object Tracking|Multi-object Tracking]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/LiDAR-based Two-Stage Transformer|LiDAR-based Two-Stage Transformer]], [[keywords/Temporal Coherence|Temporal Coherence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.12753v3 Announce Type: replace 
Abstract: Multi-object tracking from LiDAR point clouds presents unique challenges due to the sparse and irregular nature of the data, compounded by the need for temporal coherence across frames. Traditional tracking systems often rely on hand-crafted features and motion models, which can struggle to maintain consistent object identities in crowded or fast-moving scenes. We present a lidar-based two-staged DETR inspired transformer; a smoother and tracker. The smoother stage refines lidar object detections, from any off-the-shelf detector, across a moving temporal window. The tracker stage uses a DETR-based attention block to maintain tracks across time by associating tracked objects with the refined detections using the point cloud as context. The model is trained on the datasets nuScenes and KITTI in both online and offline (forward peeking) modes demonstrating strong performance across metrics such as ID-switch and multiple object tracking accuracy (MOTA). The numerical results indicate that the online mode outperforms the lidar-only baseline and SOTA models on the nuScenes dataset, with an aMOTA of 0.724 and an aMOTP of 0.475, while the offline mode provides an additional 3 pp aMOTP.

## 📝 요약

이 논문은 LiDAR 점 구름 데이터를 활용한 다중 객체 추적 문제를 다룹니다. 기존의 추적 시스템은 수작업으로 설계된 특징과 운동 모델에 의존하여 복잡한 장면에서 객체의 정체성을 유지하는 데 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 DETR 기반의 트랜스포머 모델을 제안합니다. 이 모델은 두 단계로 구성되며, 첫 번째 단계에서는 LiDAR 객체 검출을 시간적 창을 통해 정제하고, 두 번째 단계에서는 DETR 기반 주의 메커니즘을 활용해 시간에 걸쳐 객체를 추적합니다. 이 모델은 nuScenes와 KITTI 데이터셋에서 온라인 및 오프라인 모드로 학습되었으며, ID 전환 및 다중 객체 추적 정확도(MOTA)에서 우수한 성능을 보였습니다. 특히, 온라인 모드는 nuScenes 데이터셋에서 기존의 LiDAR 전용 모델과 최신 모델을 능가하는 성과를 보였으며, 오프라인 모드는 추가적인 성능 향상을 제공합니다.

## 🎯 주요 포인트

- 1. LiDAR 포인트 클라우드에서 다중 객체 추적은 데이터의 희소성과 불규칙성으로 인해 독특한 도전 과제를 제시합니다.
- 2. 본 연구에서는 DETR에서 영감을 받은 LiDAR 기반의 두 단계 변환기(스무더와 트래커)를 제안합니다.
- 3. 스무더 단계는 이동하는 시간 창을 통해 LiDAR 객체 탐지를 정제합니다.
- 4. 트래커 단계는 DETR 기반 주의 블록을 사용하여 시간에 걸쳐 객체 추적을 유지합니다.
- 5. 제안된 모델은 nuScenes 및 KITTI 데이터셋에서 강력한 성능을 보이며, 온라인 모드에서 aMOTA 0.724 및 aMOTP 0.475를 기록했습니다.


---

*Generated on 2025-09-26 09:25:01*