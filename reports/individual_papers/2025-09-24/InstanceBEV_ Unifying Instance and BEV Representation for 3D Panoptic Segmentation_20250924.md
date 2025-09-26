<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:29:07.165358",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "BEV-based 3D Perception",
    "InstanceBEV",
    "Attention Mechanism",
    "Multi-task Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "BEV-based 3D Perception": 0.78,
    "InstanceBEV": 0.8,
    "Attention Mechanism": 0.85,
    "Multi-task Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "BEV-based 3D perception",
        "canonical": "BEV-based 3D Perception",
        "aliases": [
          "Bird's Eye View 3D Perception"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific approach in 3D perception crucial for autonomous driving, linking to spatial representation techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "InstanceBEV",
        "canonical": "InstanceBEV",
        "aliases": [
          "Instance BEV"
        ],
        "category": "unique_technical",
        "rationale": "InstanceBEV is a novel method introduced in the paper, providing a unique perspective on combining instance and BEV representation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "global attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Global Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for integrating global context, linking to broader AI techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "multi-task learning",
        "canonical": "Multi-task Learning",
        "aliases": [
          "MTL"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-task learning is a key concept in machine learning, enhancing model efficiency by sharing representations.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "autonomous driving",
      "efficiency challenges"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "BEV-based 3D perception",
      "resolved_canonical": "BEV-based 3D Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "InstanceBEV",
      "resolved_canonical": "InstanceBEV",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "global attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multi-task learning",
      "resolved_canonical": "Multi-task Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# InstanceBEV: Unifying Instance and BEV Representation for 3D Panoptic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.13817.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2505.13817](https://arxiv.org/abs/2505.13817)

## 🔗 유사한 논문
- [[2025-09-23/CoBEVMoE_ Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception_20250923|CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception]] (86.8% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (86.2% similar)
- [[2025-09-18/BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (85.8% similar)
- [[2025-09-24/TinyBEV_ Cross Modal Knowledge Distillation for Efficient Multi Task Bird's Eye View Perception and Planning_20250924|TinyBEV: Cross Modal Knowledge Distillation for Efficient Multi Task Bird's Eye View Perception and Planning]] (85.6% similar)
- [[2025-09-18/FishBEV_ Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras_20250918|FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Multi-task Learning|Multi-task Learning]]
**⚡ Unique Technical**: [[keywords/BEV-based 3D Perception|BEV-based 3D Perception]], [[keywords/InstanceBEV|InstanceBEV]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13817v2 Announce Type: replace 
Abstract: BEV-based 3D perception has emerged as a focal point of research in end-to-end autonomous driving. However, existing BEV approaches encounter significant challenges due to the large feature space, complicating efficient modeling and hindering effective integration of global attention mechanisms. We propose a novel modeling strategy, called InstanceBEV, that synergistically combines the strengths of both map-centric approaches and object-centric approaches. Our method effectively extracts instance-level features within the BEV features, facilitating the implementation of global attention modeling in a highly compressed feature space, thereby addressing the efficiency challenges inherent in map-centric global modeling. Furthermore, our approach enables effective multi-task learning without introducing additional module. We validate the efficiency and accuracy of the proposed model through predicting occupancy, achieving 3D occupancy panoptic segmentation by combining instance information. Experimental results on the OCC3D-nuScenes dataset demonstrate that InstanceBEV, utilizing only 8 frames, achieves a RayPQ of 15.3 and a RayIoU of 38.2. This surpasses SparseOcc's RayPQ by 9.3% and RayIoU by 10.7%, showcasing the effectiveness of multi-task synergy.

## 📝 요약

InstanceBEV는 자율주행을 위한 BEV 기반 3D 인식의 효율성을 개선하기 위해 제안된 새로운 모델링 전략입니다. 이 방법은 지도 중심 접근법과 객체 중심 접근법의 장점을 결합하여 BEV 특징 내에서 인스턴스 수준의 특징을 효과적으로 추출합니다. 이를 통해 전역 주의 메커니즘을 압축된 특징 공간에서 구현할 수 있어 지도 중심 전역 모델링의 효율성 문제를 해결합니다. 또한, 추가 모듈 없이도 효과적인 다중 작업 학습이 가능합니다. OCC3D-nuScenes 데이터셋 실험 결과, InstanceBEV는 8프레임만으로 RayPQ 15.3과 RayIoU 38.2를 달성하여, SparseOcc보다 각각 9.3%와 10.7% 향상된 성능을 보였습니다.

## 🎯 주요 포인트

- 1. BEV 기반 3D 인식은 자율주행 연구의 핵심 주제로 부상했으나, 기존 방법은 큰 특징 공간으로 인해 효율적인 모델링에 어려움을 겪고 있습니다.
- 2. InstanceBEV는 지도 중심 접근법과 객체 중심 접근법의 장점을 결합하여 인스턴스 수준의 특징을 효과적으로 추출합니다.
- 3. 제안된 방법은 지도 중심의 전역 모델링에서 발생하는 효율성 문제를 해결하며, 추가 모듈 없이 효과적인 다중 작업 학습을 가능하게 합니다.
- 4. OCC3D-nuScenes 데이터셋 실험 결과, InstanceBEV는 8 프레임만으로 RayPQ 15.3과 RayIoU 38.2를 달성하며, SparseOcc보다 각각 9.3%와 10.7% 향상된 성능을 보였습니다.


---

*Generated on 2025-09-24 16:29:07*