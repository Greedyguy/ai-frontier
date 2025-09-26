---
keywords:
  - Attention Mechanism
  - SDE-DET
  - Attention Mechanism
  - STP-AgriData
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19990
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:55:40.529334",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "SDE-DET",
    "Attention Mechanism",
    "STP-AgriData"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.78,
    "SDE-DET": 0.7,
    "STP-AgriData": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deformable Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Deformable Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Deformable Attention is a specialized form of Attention Mechanism, enhancing connectivity with existing models in computer vision.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "SDE-DET",
        "canonical": "SDE-DET",
        "aliases": [
          "SDE-DET model"
        ],
        "category": "unique_technical",
        "rationale": "SDE-DET is a unique model specifically designed for Shatian pomelo detection, offering novel insights into agricultural applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Efficient Multi-Scale Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Multi-Scale Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Efficient Multi-Scale Attention is a variant that enhances the existing Attention Mechanism, particularly useful in complex environments.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "STP-AgriData",
        "canonical": "STP-AgriData",
        "aliases": [
          "STP-AgriData dataset"
        ],
        "category": "unique_technical",
        "rationale": "STP-AgriData is a specialized dataset for Shatian pomelo detection, crucial for benchmarking and model training.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "complex orchard environments",
      "small object detection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deformable Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SDE-DET",
      "resolved_canonical": "SDE-DET",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Efficient Multi-Scale Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "STP-AgriData",
      "resolved_canonical": "STP-AgriData",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# SDE-DET: A Precision Network for Shatian Pomelo Detection in Complex Orchard Environments

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19990.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19990](https://arxiv.org/abs/2509.19990)

## 🔗 유사한 논문
- [[2025-09-23/TinyDef-DETR_ A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery_20250923|TinyDef-DETR: A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery]] (81.8% similar)
- [[2025-09-24/TinyEcoWeedNet_ Edge Efficient Real-Time Aerial Agricultural Weed Detection_20250924|TinyEcoWeedNet: Edge Efficient Real-Time Aerial Agricultural Weed Detection]] (81.4% similar)
- [[2025-09-23/Depth Edge Alignment Loss_ DEALing with Depth in Weakly Supervised Semantic Segmentation_20250923|Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation]] (79.4% similar)
- [[2025-09-24/SPADE_ A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture_20250924|SPADE: A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture]] (79.1% similar)
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/SDE-DET|SDE-DET]], [[keywords/STP-AgriData|STP-AgriData]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19990v1 Announce Type: cross 
Abstract: Pomelo detection is an essential process for their localization, automated robotic harvesting, and maturity analysis. However, detecting Shatian pomelo in complex orchard environments poses significant challenges, including multi-scale issues, obstructions from trunks and leaves, small object detection, etc. To address these issues, this study constructs a custom dataset STP-AgriData and proposes the SDE-DET model for Shatian pomelo detection. SDE-DET first utilizes the Star Block to effectively acquire high-dimensional information without increasing the computational overhead. Furthermore, the presented model adopts Deformable Attention in its backbone, to enhance its ability to detect pomelos under occluded conditions. Finally, multiple Efficient Multi-Scale Attention mechanisms are integrated into our model to reduce the computational overhead and extract deep visual representations, thereby improving the capacity for small object detection. In the experiment, we compared SDE-DET with the Yolo series and other mainstream detection models in Shatian pomelo detection. The presented SDE-DET model achieved scores of 0.883, 0.771, 0.838, 0.497, and 0.823 in Precision, Recall, mAP@0.5, mAP@0.5:0.95 and F1-score, respectively. SDE-DET has achieved state-of-the-art performance on the STP-AgriData dataset. Experiments indicate that the SDE-DET provides a reliable method for Shatian pomelo detection, laying the foundation for the further development of automatic harvest robots.

## 📝 요약

이 연구는 복잡한 과수원 환경에서의 사천 자몽 감지를 위한 SDE-DET 모델을 제안합니다. 주요 기여는 Star Block을 활용하여 높은 차원의 정보를 효과적으로 획득하고, Deformable Attention을 통해 가려진 조건에서도 자몽을 감지할 수 있는 능력을 강화한 것입니다. 또한, 효율적인 다중 스케일 주의 메커니즘을 통합하여 계산 부담을 줄이고 작은 객체 감지 능력을 향상시켰습니다. 실험 결과, SDE-DET 모델은 STP-AgriData 데이터셋에서 최첨단 성능을 달성했으며, 자동 수확 로봇 개발의 기초를 마련했습니다.

## 🎯 주요 포인트

- 1. Shatian 자몽의 탐지를 위해 STP-AgriData라는 맞춤형 데이터셋과 SDE-DET 모델을 제안했습니다.
- 2. SDE-DET 모델은 Star Block을 활용하여 계산 비용을 증가시키지 않고 고차원 정보를 효과적으로 획득합니다.
- 3. 모델의 백본에 변형 가능한 주의를 적용하여 가려진 조건에서도 자몽을 탐지하는 능력을 향상시켰습니다.
- 4. 효율적인 다중 스케일 주의 메커니즘을 통합하여 작은 객체 탐지 능력을 개선하고 계산 비용을 줄였습니다.
- 5. 실험 결과, SDE-DET 모델은 STP-AgriData 데이터셋에서 최첨단 성능을 달성했으며, 자동 수확 로봇 개발의 기초를 마련했습니다.


---

*Generated on 2025-09-25 15:55:40*