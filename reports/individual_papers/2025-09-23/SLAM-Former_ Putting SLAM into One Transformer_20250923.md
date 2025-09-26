---
keywords:
  - SLAM-Former
  - Transformer
  - Dense SLAM
  - Incremental Mapping
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16909
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:38:02.006407",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SLAM-Former",
    "Transformer",
    "Dense SLAM",
    "Incremental Mapping"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SLAM-Former": 0.8,
    "Transformer": 0.85,
    "Dense SLAM": 0.78,
    "Incremental Mapping": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SLAM-Former",
        "canonical": "SLAM-Former",
        "aliases": [
          "SLAM Transformer"
        ],
        "category": "unique_technical",
        "rationale": "SLAM-Former represents a novel integration of SLAM capabilities into a transformer, offering a unique approach in the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in modern neural networks, facilitating connections across various domains.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dense SLAM",
        "canonical": "Dense SLAM",
        "aliases": [
          "Dense Simultaneous Localization and Mapping"
        ],
        "category": "specific_connectable",
        "rationale": "Dense SLAM is a key area of comparison and improvement for SLAM-Former, relevant for linking advancements in SLAM technology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Incremental Mapping",
        "canonical": "Incremental Mapping",
        "aliases": [
          "Real-time Mapping"
        ],
        "category": "specific_connectable",
        "rationale": "Incremental Mapping is crucial for real-time processing in SLAM systems, providing a link to real-time computational techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SLAM-Former",
      "resolved_canonical": "SLAM-Former",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dense SLAM",
      "resolved_canonical": "Dense SLAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Incremental Mapping",
      "resolved_canonical": "Incremental Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SLAM-Former: Putting SLAM into One Transformer

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16909.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16909](https://arxiv.org/abs/2509.16909)

## 🔗 유사한 논문
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (81.7% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (81.2% similar)
- [[2025-09-22/NFL-BA_ Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting_20250922|NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting]] (80.1% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (80.0% similar)
- [[2025-09-18/BIM Informed Visual SLAM for Construction Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Dense SLAM|Dense SLAM]], [[keywords/Incremental Mapping|Incremental Mapping]]
**⚡ Unique Technical**: [[keywords/SLAM-Former|SLAM-Former]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16909v1 Announce Type: new 
Abstract: We present SLAM-Former, a novel neural approach that integrates full SLAM capabilities into a single transformer. Similar to traditional SLAM systems, SLAM-Former comprises both a frontend and a backend that operate in tandem. The frontend processes sequential monocular images in real-time for incremental mapping and tracking, while the backend performs global refinement to ensure a geometrically consistent result. This alternating execution allows the frontend and backend to mutually promote one another, enhancing overall system performance. Comprehensive experimental results demonstrate that SLAM-Former achieves superior or highly competitive performance compared to state-of-the-art dense SLAM methods.

## 📝 요약

SLAM-Former는 전통적인 SLAM 시스템의 기능을 하나의 트랜스포머로 통합한 새로운 신경망 접근법입니다. 이 시스템은 전면부와 후면부로 구성되어 있으며, 전면부는 실시간으로 연속적인 단안 이미지를 처리하여 점진적인 매핑과 추적을 수행하고, 후면부는 전역적인 정제를 통해 기하학적으로 일관된 결과를 보장합니다. 이러한 교차 실행은 전면부와 후면부가 서로의 성능을 향상시키도록 합니다. 실험 결과, SLAM-Former는 최신의 밀집 SLAM 방법들과 비교하여 우수하거나 매우 경쟁력 있는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. SLAM-Former는 전체 SLAM 기능을 단일 트랜스포머에 통합한 새로운 신경망 접근법입니다.
- 2. SLAM-Former는 전통적인 SLAM 시스템처럼 프론트엔드와 백엔드로 구성되어 있으며, 두 부분이 협력하여 작동합니다.
- 3. 프론트엔드는 실시간으로 순차적인 단안 이미지를 처리하여 점진적인 매핑과 추적을 수행합니다.
- 4. 백엔드는 전역적인 정제를 수행하여 기하학적으로 일관된 결과를 보장합니다.
- 5. 실험 결과, SLAM-Former는 최첨단 밀집 SLAM 방법들과 비교하여 우수하거나 매우 경쟁력 있는 성능을 달성했습니다.


---

*Generated on 2025-09-24 04:38:02*