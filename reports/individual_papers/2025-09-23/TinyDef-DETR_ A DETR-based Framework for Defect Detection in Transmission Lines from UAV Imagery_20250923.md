---
keywords:
  - DETR Framework
  - ResNet Backbone
  - Attention Mechanism
  - Focaler-Wise-SIoU Loss
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.06035
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:26:30.163531",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DETR Framework",
    "ResNet Backbone",
    "Attention Mechanism",
    "Focaler-Wise-SIoU Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DETR Framework": 0.78,
    "ResNet Backbone": 0.75,
    "Attention Mechanism": 0.82,
    "Focaler-Wise-SIoU Loss": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DETR-based framework",
        "canonical": "DETR Framework",
        "aliases": [
          "DETR",
          "Detection Transformer"
        ],
        "category": "specific_connectable",
        "rationale": "DETR is a specific model architecture relevant to computer vision tasks, facilitating connections to other works using transformers for detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "edge-enhanced ResNet backbone",
        "canonical": "ResNet Backbone",
        "aliases": [
          "ResNet",
          "Residual Network"
        ],
        "category": "broad_technical",
        "rationale": "ResNet is a foundational architecture in deep learning, widely used and connected to numerous advancements in computer vision.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "cross-stage dual-domain multi-scale attention mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Multi-scale Attention",
          "Dual-domain Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are critical in modern neural networks, enabling connections to various models utilizing similar techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Focaler-Wise-SIoU regression loss",
        "canonical": "Focaler-Wise-SIoU Loss",
        "aliases": [
          "SIoU Loss",
          "Focaler Loss"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel loss function specific to the paper, offering unique insights into improving detection accuracy.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
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
      "candidate_surface": "DETR-based framework",
      "resolved_canonical": "DETR Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "edge-enhanced ResNet backbone",
      "resolved_canonical": "ResNet Backbone",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "cross-stage dual-domain multi-scale attention mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Focaler-Wise-SIoU regression loss",
      "resolved_canonical": "Focaler-Wise-SIoU Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# TinyDef-DETR: A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06035.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.06035](https://arxiv.org/abs/2509.06035)

## 🔗 유사한 논문
- [[2025-09-18/BERTector_ An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (80.8% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (80.5% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (80.3% similar)
- [[2025-09-23/Investigating Long-term Training for Remote Sensing Object Detection_20250923|Investigating Long-term Training for Remote Sensing Object Detection]] (80.3% similar)
- [[2025-09-17/Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection_20250917|Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/ResNet Backbone|ResNet Backbone]]
**🔗 Specific Connectable**: [[keywords/DETR Framework|DETR Framework]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Focaler-Wise-SIoU Loss|Focaler-Wise-SIoU Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06035v4 Announce Type: replace-cross 
Abstract: Automated defect detection from UAV imagery of transmission lines is a challenging task due to the small size, ambiguity, and complex backgrounds of defects. This paper proposes TinyDef-DETR, a DETR-based framework designed to achieve accurate and efficient detection of transmission line defects from UAV-acquired images. The model integrates four major components: an edge-enhanced ResNet backbone to strengthen boundary-sensitive representations, a stride-free space-to-depth module to enable detail-preserving downsampling, a cross-stage dual-domain multi-scale attention mechanism to jointly model global context and local cues, and a Focaler-Wise-SIoU regression loss to improve the localization of small and difficult targets. Together, these designs effectively mitigate the limitations of conventional detectors. Extensive experiments on both public and real-world datasets demonstrate that TinyDef-DETR achieves superior detection performance and strong generalization capability, while maintaining modest computational overhead. The accuracy and efficiency of TinyDef-DETR make it a suitable method for UAV-based transmission line defect detection, particularly in scenarios involving small and ambiguous targets.

## 📝 요약

이 논문은 UAV 이미지에서 송전선 결함을 자동으로 탐지하는 TinyDef-DETR 프레임워크를 제안합니다. 이 모델은 경계 감지 강화를 위한 엣지 강화 ResNet 백본, 세부 보존 다운샘플링을 위한 스트라이드 프리 공간-깊이 모듈, 글로벌 컨텍스트와 로컬 단서를 함께 모델링하는 다중 스케일 주의 메커니즘, 작은 목표물의 위치를 개선하는 Focaler-Wise-SIoU 회귀 손실을 통합합니다. 이러한 설계는 기존 탐지기의 한계를 효과적으로 극복하며, 공공 및 실제 데이터셋 실험에서 뛰어난 탐지 성능과 일반화 능력을 보여줍니다. TinyDef-DETR는 적은 계산 비용으로 높은 정확성과 효율성을 제공하여, 특히 작은 목표물 탐지에 적합한 방법입니다.

## 🎯 주요 포인트

- 1. TinyDef-DETR는 UAV 이미지에서 전송선 결함을 정확하고 효율적으로 탐지하기 위한 DETR 기반 프레임워크입니다.
- 2. 모델은 경계 민감 표현을 강화하는 엣지 강화 ResNet 백본을 통합합니다.
- 3. 세부 보존 다운샘플링을 가능하게 하는 스트라이드 프리 공간-깊이 모듈을 포함합니다.
- 4. 글로벌 컨텍스트와 로컬 큐를 공동으로 모델링하는 교차 단계 이중 도메인 다중 스케일 주의 메커니즘을 사용합니다.
- 5. Focaler-Wise-SIoU 회귀 손실을 통해 작은 목표물의 위치를 개선합니다.


---

*Generated on 2025-09-24 01:26:30*