---
keywords:
  - Neural Network
  - Network Compression
  - Object Location Information
  - Detection Models
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17968
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:07:01.336073",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Network Compression",
    "Object Location Information",
    "Detection Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.8,
    "Network Compression": 0.7,
    "Object Location Information": 0.6,
    "Detection Models": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "DNN",
          "Deep Networks"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are foundational to the discussed compression techniques and connect with broader machine learning topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Network Compression",
        "canonical": "Network Compression",
        "aliases": [
          "Model Compression",
          "Compression Techniques"
        ],
        "category": "unique_technical",
        "rationale": "Network Compression is a key focus of the paper, offering unique insights into reducing model complexity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Object Location Information",
        "canonical": "Object Location Information",
        "aliases": [
          "Localization Data",
          "Detection Localization"
        ],
        "category": "unique_technical",
        "rationale": "Object Location Information is crucial for the proposed method, linking it to spatial data processing.",
        "novelty_score": 0.65,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.6
      },
      {
        "surface": "Detection Models",
        "canonical": "Detection Models",
        "aliases": [
          "Object Detection Models",
          "Detection Algorithms"
        ],
        "category": "specific_connectable",
        "rationale": "Detection Models are central to the paper's experiments, providing a link to applied computer vision.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Pruning",
      "Pre-trained Models",
      "Features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Network Compression",
      "resolved_canonical": "Network Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Object Location Information",
      "resolved_canonical": "Object Location Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.6
      }
    },
    {
      "candidate_surface": "Detection Models",
      "resolved_canonical": "Detection Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Visual Detector Compression via Location-Aware Discriminant Analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17968.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17968](https://arxiv.org/abs/2509.17968)

## 🔗 유사한 논문
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (85.1% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (84.7% similar)
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (84.3% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (83.9% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Detection Models|Detection Models]]
**⚡ Unique Technical**: [[keywords/Network Compression|Network Compression]], [[keywords/Object Location Information|Object Location Information]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17968v1 Announce Type: new 
Abstract: Deep neural networks are powerful, yet their high complexity greatly limits their potential to be deployed on billions of resource-constrained edge devices. Pruning is a crucial network compression technique, yet most existing methods focus on classification models, with limited attention to detection. Even among those addressing detection, there is a lack of utilization of essential localization information. Also, many pruning methods passively rely on pre-trained models, in which useful and useless components are intertwined, making it difficult to remove the latter without harming the former at the neuron/filter level. To address the above issues, in this paper, we propose a proactive detection-discriminants-based network compression approach for deep visual detectors, which alternates between two steps: (1) maximizing and compressing detection-related discriminants and aligning them with a subset of neurons/filters immediately before the detection head, and (2) tracing the detection-related discriminating power across the layers and discarding features of lower importance. Object location information is exploited in both steps. Extensive experiments, employing four advanced detection models and four state-of-the-art competing methods on the KITTI and COCO datasets, highlight the superiority of our approach. Remarkably, our compressed models can even beat the original base models with a substantial reduction in complexity.

## 📝 요약

이 논문은 자원 제약이 있는 엣지 디바이스에서 딥 뉴럴 네트워크를 효과적으로 활용하기 위한 네트워크 압축 기법을 제안합니다. 기존의 가지치기(pruning) 방법은 주로 분류 모델에 집중되어 있으며, 탐지 모델에서는 중요한 위치 정보 활용이 부족합니다. 이를 해결하기 위해, 본 연구는 탐지 관련 판별력을 극대화하고 이를 뉴런/필터에 정렬하는 방식으로 탐지 모델을 압축하는 방법론을 제안합니다. 또한, 계층 간 탐지 관련 판별력을 추적하여 중요도가 낮은 특징을 제거합니다. KITTI와 COCO 데이터셋을 사용한 실험 결과, 제안된 방법은 기존 모델보다 복잡성을 크게 줄이면서도 성능이 우수함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 가지치기 방법은 주로 분류 모델에 집중되어 있으며, 탐지 모델에 대한 연구는 부족하다.
- 2. 탐지 모델의 가지치기에서 중요한 위치 정보의 활용이 부족하다.
- 3. 사전 학습된 모델에 의존하는 기존 방법은 유용한 요소와 불필요한 요소가 얽혀 있어 효과적인 가지치기가 어렵다.
- 4. 본 논문은 탐지 관련 판별력을 최대화하고 이를 뉴런/필터와 정렬하는 능동적인 네트워크 압축 방법을 제안한다.
- 5. 제안된 방법은 KITTI 및 COCO 데이터셋에서 기존 모델보다 복잡성을 크게 줄이면서도 성능을 능가한다.


---

*Generated on 2025-09-24 05:07:01*