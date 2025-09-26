---
keywords:
  - Multispectral Oriented Detection
  - Heterogeneous Feature Extraction Network
  - Multimodal Learning
  - Condition-based Multimodal Label Fusion
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16957
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:40:06.065814",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multispectral Oriented Detection",
    "Heterogeneous Feature Extraction Network",
    "Multimodal Learning",
    "Condition-based Multimodal Label Fusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multispectral Oriented Detection": 0.78,
    "Heterogeneous Feature Extraction Network": 0.77,
    "Multimodal Learning": 0.8,
    "Condition-based Multimodal Label Fusion": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multispectral Oriented Detection",
        "canonical": "Multispectral Oriented Detection",
        "aliases": [
          "MO R-CNN",
          "Multispectral Detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique method proposed in the paper, enhancing object detection in remote sensing images.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Heterogeneous Feature Extraction Network",
        "canonical": "Heterogeneous Feature Extraction Network",
        "aliases": [
          "HFEN"
        ],
        "category": "unique_technical",
        "rationale": "A novel network architecture that could connect to discussions on feature extraction methods.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of integrating multiple data modalities, which is a trending topic.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Condition-based Multimodal Label Fusion",
        "canonical": "Condition-based Multimodal Label Fusion",
        "aliases": [
          "CMLF"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific technique for label fusion in multimodal datasets, enhancing model robustness.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
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
      "candidate_surface": "Multispectral Oriented Detection",
      "resolved_canonical": "Multispectral Oriented Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Heterogeneous Feature Extraction Network",
      "resolved_canonical": "Heterogeneous Feature Extraction Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Condition-based Multimodal Label Fusion",
      "resolved_canonical": "Condition-based Multimodal Label Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16957.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16957](https://arxiv.org/abs/2509.16957)

## 🔗 유사한 논문
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (84.2% similar)
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (83.9% similar)
- [[2025-09-22/MoCA_ Multi-modal Cross-masked Autoencoder for Digital Health Measurements_20250922|MoCA: Multi-modal Cross-masked Autoencoder for Digital Health Measurements]] (83.8% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (83.6% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Multispectral Oriented Detection|Multispectral Oriented Detection]], [[keywords/Heterogeneous Feature Extraction Network|Heterogeneous Feature Extraction Network]], [[keywords/Condition-based Multimodal Label Fusion|Condition-based Multimodal Label Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16957v1 Announce Type: new 
Abstract: Oriented object detection for multi-spectral imagery faces significant challenges due to differences both within and between modalities. Although existing methods have improved detection accuracy through complex network architectures, their high computational complexity and memory consumption severely restrict their performance. Motivated by the success of large kernel convolutions in remote sensing, we propose MO R-CNN, a lightweight framework for multi-spectral oriented detection featuring heterogeneous feature extraction network (HFEN), single modality supervision (SMS), and condition-based multimodal label fusion (CMLF). HFEN leverages inter-modal differences to adaptively align, merge, and enhance multi-modal features. SMS constrains multi-scale features and enables the model to learn from multiple modalities. CMLF fuses multimodal labels based on specific rules, providing the model with a more robust and consistent supervisory signal. Experiments on the DroneVehicle, VEDAI and OGSOD datasets prove the superiority of our method. The source code is available at:https://github.com/Iwill-github/MORCNN.

## 📝 요약

이 논문은 다중 스펙트럼 이미지를 위한 경량화된 방향성 객체 탐지 프레임워크인 MO R-CNN을 제안합니다. 기존 방법들이 복잡한 네트워크 구조로 정확도를 높였으나, 높은 계산 복잡도와 메모리 소비가 성능을 제한했습니다. MO R-CNN은 이질적 특징 추출 네트워크(HFEN), 단일 모달리티 감독(SMS), 조건 기반 다중 모달 레이블 융합(CMLF)을 특징으로 합니다. HFEN은 모달 간 차이를 활용하여 특징을 정렬, 병합, 향상시키고, SMS는 다중 모달리티 학습을 가능하게 하며, CMLF는 특정 규칙에 따라 레이블을 융합하여 강력한 감독 신호를 제공합니다. DroneVehicle, VEDAI, OGSOD 데이터셋 실험 결과, 제안된 방법의 우수성이 입증되었습니다. 소스 코드는 https://github.com/Iwill-github/MORCNN에서 제공됩니다.

## 🎯 주요 포인트

- 1. MO R-CNN은 다중 스펙트럼 이미지의 방향성 객체 탐지를 위한 경량 프레임워크로, 이질적인 특징 추출 네트워크(HFEN), 단일 모달리티 감독(SMS), 조건 기반 다중 모달 레이블 융합(CMLF)을 특징으로 합니다.
- 2. HFEN은 모달 간 차이를 활용하여 다중 모달 특징을 적응적으로 정렬, 병합 및 향상시킵니다.
- 3. SMS는 다중 스케일 특징을 제한하고 모델이 여러 모달리티로부터 학습할 수 있도록 합니다.
- 4. CMLF는 특정 규칙에 기반하여 다중 모달 레이블을 융합하여 모델에 더 강력하고 일관된 감독 신호를 제공합니다.
- 5. DroneVehicle, VEDAI 및 OGSOD 데이터셋에서의 실험을 통해 제안된 방법의 우수성이 입증되었습니다.


---

*Generated on 2025-09-24 04:40:06*