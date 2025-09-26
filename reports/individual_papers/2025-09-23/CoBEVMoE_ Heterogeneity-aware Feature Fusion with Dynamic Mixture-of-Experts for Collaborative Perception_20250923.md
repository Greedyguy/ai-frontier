---
keywords:
  - Collaborative Perception
  - Dynamic Mixture-of-Experts
  - Bird's Eye View
  - Dynamic Expert Metric Loss
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17107
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:46:11.224452",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Collaborative Perception",
    "Dynamic Mixture-of-Experts",
    "Bird's Eye View",
    "Dynamic Expert Metric Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Collaborative Perception": 0.78,
    "Dynamic Mixture-of-Experts": 0.8,
    "Bird's Eye View": 0.77,
    "Dynamic Expert Metric Loss": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Collaborative Perception",
        "canonical": "Collaborative Perception",
        "aliases": [
          "Multi-Agent Perception"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a growing area of research in perception systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dynamic Mixture-of-Experts",
        "canonical": "Dynamic Mixture-of-Experts",
        "aliases": [
          "DMoE"
        ],
        "category": "unique_technical",
        "rationale": "This architecture is a key innovation in the paper, enabling dynamic feature extraction.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Bird's Eye View",
        "canonical": "Bird's Eye View",
        "aliases": [
          "BEV"
        ],
        "category": "specific_connectable",
        "rationale": "BEV is a critical perspective in computer vision for autonomous systems and is well-connected in related literature.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Dynamic Expert Metric Loss",
        "canonical": "Dynamic Expert Metric Loss",
        "aliases": [
          "DEML"
        ],
        "category": "unique_technical",
        "rationale": "This loss function is specifically designed to enhance the model's performance, representing a novel contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Collaborative Perception",
      "resolved_canonical": "Collaborative Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dynamic Mixture-of-Experts",
      "resolved_canonical": "Dynamic Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Bird's Eye View",
      "resolved_canonical": "Bird's Eye View",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Dynamic Expert Metric Loss",
      "resolved_canonical": "Dynamic Expert Metric Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17107.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17107](https://arxiv.org/abs/2509.17107)

## 🔗 유사한 논문
- [[2025-09-18/FishBEV_ Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras_20250918|FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (85.2% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (84.9% similar)
- [[2025-09-18/BEVUDA++_ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection_20250918|BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (84.6% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (84.4% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Bird's Eye View|Bird's Eye View]]
**⚡ Unique Technical**: [[keywords/Collaborative Perception|Collaborative Perception]], [[keywords/Dynamic Mixture-of-Experts|Dynamic Mixture-of-Experts]], [[keywords/Dynamic Expert Metric Loss|Dynamic Expert Metric Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17107v1 Announce Type: new 
Abstract: Collaborative perception aims to extend sensing coverage and improve perception accuracy by sharing information among multiple agents. However, due to differences in viewpoints and spatial positions, agents often acquire heterogeneous observations. Existing intermediate fusion methods primarily focus on aligning similar features, often overlooking the perceptual diversity among agents. To address this limitation, we propose CoBEVMoE, a novel collaborative perception framework that operates in the Bird's Eye View (BEV) space and incorporates a Dynamic Mixture-of-Experts (DMoE) architecture. In DMoE, each expert is dynamically generated based on the input features of a specific agent, enabling it to extract distinctive and reliable cues while attending to shared semantics. This design allows the fusion process to explicitly model both feature similarity and heterogeneity across agents. Furthermore, we introduce a Dynamic Expert Metric Loss (DEML) to enhance inter-expert diversity and improve the discriminability of the fused representation. Extensive experiments on the OPV2V and DAIR-V2X-C datasets demonstrate that CoBEVMoE achieves state-of-the-art performance. Specifically, it improves the IoU for Camera-based BEV segmentation by +1.5% on OPV2V and the AP@50 for LiDAR-based 3D object detection by +3.0% on DAIR-V2X-C, verifying the effectiveness of expert-based heterogeneous feature modeling in multi-agent collaborative perception. The source code will be made publicly available at https://github.com/godk0509/CoBEVMoE.

## 📝 요약

이 논문은 다중 에이전트 간 정보 공유를 통해 인식 정확도를 높이는 협력적 인식을 다룹니다. 기존 방법들이 유사한 특징 정렬에 집중하는 반면, 제안된 CoBEVMoE 프레임워크는 Bird's Eye View 공간에서 Dynamic Mixture-of-Experts(DMoE) 구조를 활용하여 에이전트 간의 특징 다양성과 유사성을 모두 모델링합니다. DMoE는 각 에이전트의 입력 특징에 따라 동적으로 전문가를 생성하여 독특하고 신뢰할 수 있는 정보를 추출합니다. 또한, Dynamic Expert Metric Loss(DEML)를 도입하여 전문가 간 다양성을 높이고 융합 표현의 변별력을 향상시킵니다. 실험 결과, CoBEVMoE는 OPV2V와 DAIR-V2X-C 데이터셋에서 최첨단 성능을 보이며, 카메라 기반 BEV 분할과 LiDAR 기반 3D 객체 탐지에서 각각 +1.5%와 +3.0%의 성능 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. CoBEVMoE는 Bird's Eye View (BEV) 공간에서 작동하며 Dynamic Mixture-of-Experts (DMoE) 아키텍처를 통합한 새로운 협력 인식 프레임워크입니다.
- 2. DMoE는 특정 에이전트의 입력 특징에 기반하여 동적으로 전문가를 생성하여, 공유된 의미에 주의를 기울이면서 독특하고 신뢰할 수 있는 단서를 추출합니다.
- 3. Dynamic Expert Metric Loss (DEML)을 도입하여 전문가 간 다양성을 강화하고 융합된 표현의 변별력을 향상시킵니다.
- 4. CoBEVMoE는 OPV2V와 DAIR-V2X-C 데이터셋에서 최첨단 성능을 달성하며, 카메라 기반 BEV 세분화의 IoU를 +1.5% 향상시키고, LiDAR 기반 3D 객체 탐지의 AP@50을 +3.0% 향상시킵니다.
- 5. CoBEVMoE의 소스 코드는 https://github.com/godk0509/CoBEVMoE에서 공개될 예정입니다.


---

*Generated on 2025-09-24 04:46:11*