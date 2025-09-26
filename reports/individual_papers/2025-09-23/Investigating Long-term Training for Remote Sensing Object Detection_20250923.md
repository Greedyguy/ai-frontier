---
keywords:
  - Remote Sensing Object Detection
  - Dynamic Backbone Freezing
  - Transformer
  - Feature Backbone
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2407.15143
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:39:00.427657",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Remote Sensing Object Detection",
    "Dynamic Backbone Freezing",
    "Transformer",
    "Feature Backbone"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Remote Sensing Object Detection": 0.78,
    "Dynamic Backbone Freezing": 0.8,
    "Transformer": 0.85,
    "Feature Backbone": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "remote sensing object detection",
        "canonical": "Remote Sensing Object Detection",
        "aliases": [
          "RSOD"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a specific application area within computer vision, enhancing connectivity to domain-specific research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dynamic Backbone Freezing",
        "canonical": "Dynamic Backbone Freezing",
        "aliases": [
          "DBF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for improving model training efficiency, relevant for linking advancements in training techniques.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "transformer architectures",
        "canonical": "Transformer",
        "aliases": [
          "transformer models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to a widely used model architecture in deep learning, facilitating links to related technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "feature backbone",
        "canonical": "Feature Backbone",
        "aliases": [
          "backbone network"
        ],
        "category": "specific_connectable",
        "rationale": "Key component in neural networks for feature extraction, relevant for discussions on model architecture.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
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
      "candidate_surface": "remote sensing object detection",
      "resolved_canonical": "Remote Sensing Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dynamic Backbone Freezing",
      "resolved_canonical": "Dynamic Backbone Freezing",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "transformer architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "feature backbone",
      "resolved_canonical": "Feature Backbone",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Investigating Long-term Training for Remote Sensing Object Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2407.15143.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2407.15143](https://arxiv.org/abs/2407.15143)

## 🔗 유사한 논문
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (82.2% similar)
- [[2025-09-18/Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (82.1% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (81.1% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (81.1% similar)
- [[2025-09-22/The Missing Piece_ A Case for Pre-Training in 3D Medical Object Detection_20250922|The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Feature Backbone|Feature Backbone]]
**⚡ Unique Technical**: [[keywords/Remote Sensing Object Detection|Remote Sensing Object Detection]], [[keywords/Dynamic Backbone Freezing|Dynamic Backbone Freezing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.15143v3 Announce Type: replace-cross 
Abstract: Recently, numerous methods have achieved impressive performance in remote sensing object detection, relying on convolution or transformer architectures. Such detectors typically have a feature backbone to extract useful features from raw input images. A common practice in current detectors is initializing the backbone with pre-trained weights available online. Fine-tuning the backbone is typically required to generate features suitable for remote-sensing images. While the prolonged training could lead to over-fitting, hindering the extraction of basic visual features, it can enable models to gradually extract deeper insights and richer representations from remote sensing data. Striking a balance between these competing factors is critical for achieving optimal performance. In this study, we aim to investigate the performance and characteristics of remote sensing object detection models under very long training schedules, and propose a novel method named Dynamic Backbone Freezing (DBF) for feature backbone fine-tuning on remote sensing object detection under long-term training. Our method addresses the dilemma of whether the backbone should extract low-level generic features or possess specific knowledge of the remote sensing domain, by introducing a module called 'Freezing Scheduler' to manage the update of backbone features during long-term training dynamically. Extensive experiments on DOTA and DIOR-R show that our approach enables more accurate model learning while substantially reducing computational costs in long-term training. Besides, it can be seamlessly adopted without additional effort due to its straightforward design. The code is available at https://github.com/unique-chan/dbf.

## 📝 요약

이 연구는 원격 감지 객체 탐지 모델의 성능을 향상시키기 위해 'Dynamic Backbone Freezing (DBF)'이라는 새로운 방법을 제안합니다. 기존의 탐지기들은 사전 학습된 가중치를 사용하여 백본을 초기화하고, 이를 미세 조정하여 원격 감지 이미지에 적합한 특징을 추출합니다. 그러나 장기 훈련은 과적합을 초래할 수 있어 기본 시각적 특징의 추출을 방해할 수 있습니다. 이를 해결하기 위해 DBF는 'Freezing Scheduler' 모듈을 도입하여 장기 훈련 동안 백본 특징의 업데이트를 동적으로 관리합니다. DOTA와 DIOR-R 데이터셋에서의 실험 결과, 이 방법은 정확도를 높이고 계산 비용을 크게 줄이는 데 효과적임을 보여주었습니다. DBF는 간단한 설계로 추가적인 노력 없이도 쉽게 적용 가능합니다.

## 🎯 주요 포인트

- 1. 원격 감지 객체 탐지에서 백본을 사전 학습된 가중치로 초기화하고 미세 조정하는 것이 일반적이다.
- 2. 장기 훈련은 과적합을 초래할 수 있지만, 더 깊은 통찰력과 풍부한 표현을 추출할 수 있다.
- 3. Dynamic Backbone Freezing (DBF) 방법은 장기 훈련에서 백본의 기능을 동적으로 관리하여 최적의 성능을 달성한다.
- 4. DOTA와 DIOR-R 데이터셋에서의 실험은 DBF가 더 정확한 모델 학습과 계산 비용 절감을 가능하게 함을 보여준다.
- 5. DBF는 추가적인 노력 없이 쉽게 적용할 수 있는 간단한 설계를 가지고 있다.


---

*Generated on 2025-09-24 00:39:00*