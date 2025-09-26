---
keywords:
  - Sparse Fusion Transformer
  - Multimodal Learning
  - Attention Mechanism
  - Range-Adaptive Radar Aggregation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2411.19860
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:37:16.192759",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Fusion Transformer",
    "Multimodal Learning",
    "Attention Mechanism",
    "Range-Adaptive Radar Aggregation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Fusion Transformer": 0.8,
    "Multimodal Learning": 0.85,
    "Attention Mechanism": 0.82,
    "Range-Adaptive Radar Aggregation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse fusion transformer",
        "canonical": "Sparse Fusion Transformer",
        "aliases": [
          "SpaRC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to 3D perception by integrating radar and camera data, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Radar-Camera fusion",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Radar-Camera Integration"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader concept of integrating multiple data modalities for enhanced perception.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Local self-attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "LSA"
        ],
        "category": "specific_connectable",
        "rationale": "Relates to the use of attention mechanisms in improving focused query aggregation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Range-adaptive radar aggregation",
        "canonical": "Range-Adaptive Radar Aggregation",
        "aliases": [
          "RAR"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique for improving object localization precision, specific to the paper's methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "depth estimation",
      "object-centric methodology"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse fusion transformer",
      "resolved_canonical": "Sparse Fusion Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Radar-Camera fusion",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Local self-attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Range-adaptive radar aggregation",
      "resolved_canonical": "Range-Adaptive Radar Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SpaRC: Sparse Radar-Camera Fusion for 3D Object Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.19860.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2411.19860](https://arxiv.org/abs/2411.19860)

## 🔗 유사한 논문
- [[2025-09-24/MLF-4DRCNet_ Multi-Level Fusion with 4D Radar and Camera for 3D Object Detection in Autonomous Driving_20250924|MLF-4DRCNet: Multi-Level Fusion with 4D Radar and Camera for 3D Object Detection in Autonomous Driving]] (86.8% similar)
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (86.3% similar)
- [[2025-09-23/RCTDistill_ Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion_20250923|RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion]] (85.1% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (84.5% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Sparse Fusion Transformer|Sparse Fusion Transformer]], [[keywords/Range-Adaptive Radar Aggregation|Range-Adaptive Radar Aggregation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.19860v2 Announce Type: replace-cross 
Abstract: In this work, we present SpaRC, a novel Sparse fusion transformer for 3D perception that integrates multi-view image semantics with Radar and Camera point features. The fusion of radar and camera modalities has emerged as an efficient perception paradigm for autonomous driving systems. While conventional approaches utilize dense Bird's Eye View (BEV)-based architectures for depth estimation, contemporary query-based transformers excel in camera-only detection through object-centric methodology. However, these query-based approaches exhibit limitations in false positive detections and localization precision due to implicit depth modeling. We address these challenges through three key contributions: (1) sparse frustum fusion (SFF) for cross-modal feature alignment, (2) range-adaptive radar aggregation (RAR) for precise object localization, and (3) local self-attention (LSA) for focused query aggregation. In contrast to existing methods requiring computationally intensive BEV-grid rendering, SpaRC operates directly on encoded point features, yielding substantial improvements in efficiency and accuracy. Empirical evaluations on the nuScenes and TruckScenes benchmarks demonstrate that SpaRC significantly outperforms existing dense BEV-based and sparse query-based detectors. Our method achieves state-of-the-art performance metrics of 67.1 NDS and 63.1 AMOTA. The code and pretrained models are available at https://github.com/phi-wol/sparc.

## 📝 요약

이 연구는 3D 인식을 위한 새로운 희소 융합 변환기인 SpaRC를 제안하며, 이는 다중 시점 이미지 의미론을 레이더 및 카메라 포인트 기능과 통합합니다. 기존 방법들이 조밀한 조감도(BEV) 기반 아키텍처를 사용한 반면, SpaRC는 쿼리 기반 변환기의 한계를 극복하기 위해 세 가지 주요 기여를 합니다: (1) 교차 모달 특징 정렬을 위한 희소 프러스텀 융합(SFF), (2) 정확한 객체 위치 지정을 위한 범위 적응형 레이더 집계(RAR), (3) 집중된 쿼리 집계를 위한 지역적 자기 주의(LSA). SpaRC는 인코딩된 포인트 기능에서 직접 작동하여 효율성과 정확성을 크게 향상시킵니다. nuScenes 및 TruckScenes 벤치마크에서 SpaRC는 기존의 조밀한 BEV 기반 및 희소 쿼리 기반 탐지기를 능가하며, 67.1 NDS 및 63.1 AMOTA의 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. SpaRC는 3D 인식을 위해 다중 뷰 이미지 의미론을 레이더 및 카메라 포인트 특징과 통합하는 새로운 희소 융합 트랜스포머입니다.
- 2. 기존의 BEV 기반 깊이 추정 방식의 한계를 극복하기 위해 희소 프러스텀 융합(SFF), 범위 적응형 레이더 집계(RAR), 국소 자기 주의(LSA)를 도입했습니다.
- 3. SpaRC는 인코딩된 포인트 특징에서 직접 작동하여 효율성과 정확성을 크게 향상시킵니다.
- 4. nuScenes 및 TruckScenes 벤치마크에서 SpaRC는 기존의 밀집 BEV 기반 및 희소 쿼리 기반 탐지기를 능가하는 성능을 보였습니다.
- 5. SpaRC는 최첨단 성능 지표인 67.1 NDS와 63.1 AMOTA를 달성했습니다.


---

*Generated on 2025-09-26 08:37:16*