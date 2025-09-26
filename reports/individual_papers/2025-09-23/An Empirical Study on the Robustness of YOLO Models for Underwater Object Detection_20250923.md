---
keywords:
  - YOLO
  - Underwater Object Detection
  - Noise-Aware Sample Injection
  - Domain Adaptation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17561
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:01:28.841993",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "YOLO",
    "Underwater Object Detection",
    "Noise-Aware Sample Injection",
    "Domain Adaptation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "YOLO": 0.78,
    "Underwater Object Detection": 0.77,
    "Noise-Aware Sample Injection": 0.75,
    "Domain Adaptation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "YOLO models",
        "canonical": "YOLO",
        "aliases": [
          "You Only Look Once"
        ],
        "category": "unique_technical",
        "rationale": "YOLO is a specific object detection model family critical for linking discussions on real-time detection.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "underwater object detection",
        "canonical": "Underwater Object Detection",
        "aliases": [
          "UOD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized application area within computer vision, essential for linking domain-specific research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "noise-aware sample injection",
        "canonical": "Noise-Aware Sample Injection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach to improving model robustness, relevant for linking to domain adaptation strategies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "domain adaptation",
        "canonical": "Domain Adaptation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Domain adaptation is a key concept for linking strategies that enhance model performance across different environments.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "YOLO models",
      "resolved_canonical": "YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "underwater object detection",
      "resolved_canonical": "Underwater Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "noise-aware sample injection",
      "resolved_canonical": "Noise-Aware Sample Injection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "domain adaptation",
      "resolved_canonical": "Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# An Empirical Study on the Robustness of YOLO Models for Underwater Object Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17561.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17561](https://arxiv.org/abs/2509.17561)

## 🔗 유사한 논문
- [[2025-09-18/Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies_20250918|Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies]] (85.1% similar)
- [[2025-09-23/Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture_20250923|Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture]] (83.4% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (83.3% similar)
- [[2025-09-18/Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (83.1% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Domain Adaptation|Domain Adaptation]]
**⚡ Unique Technical**: [[keywords/YOLO|YOLO]], [[keywords/Underwater Object Detection|Underwater Object Detection]], [[keywords/Noise-Aware Sample Injection|Noise-Aware Sample Injection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17561v1 Announce Type: cross 
Abstract: Underwater object detection (UOD) remains a critical challenge in computer vision due to underwater distortions which degrade low-level features and compromise the reliability of even state-of-the-art detectors. While YOLO models have become the backbone of real-time object detection, little work has systematically examined their robustness under these uniquely challenging conditions. This raises a critical question: Are YOLO models genuinely robust when operating under the chaotic and unpredictable conditions of underwater environments? In this study, we present one of the first comprehensive evaluations of recent YOLO variants (YOLOv8-YOLOv12) across six simulated underwater environments. Using a unified dataset of 10,000 annotated images from DUO and Roboflow100, we not only benchmark model robustness but also analyze how distortions affect key low-level features such as texture, edges, and color. Our findings show that (1) YOLOv12 delivers the strongest overall performance but is highly vulnerable to noise, and (2) noise disrupts edge and texture features, explaining the poor detection performance in noisy images. Class imbalance is a persistent challenge in UOD. Experiments revealed that (3) image counts and instance frequency primarily drive detection performance, while object appearance exerts only a secondary influence. Finally, we evaluated lightweight training-aware strategies: noise-aware sample injection, which improves robustness in both noisy and real-world conditions, and fine-tuning with advanced enhancement, which boosts accuracy in enhanced domains but slightly lowers performance in original data, demonstrating strong potential for domain adaptation, respectively. Together, these insights provide practical guidance for building resilient and cost-efficient UOD systems.

## 📝 요약

이 연구는 YOLO 모델의 수중 객체 탐지 성능을 평가한 최초의 포괄적 연구 중 하나로, YOLOv8부터 YOLOv12까지의 변형을 여섯 가지 시뮬레이션된 수중 환경에서 테스트했습니다. 10,000개의 주석이 달린 DUO 및 Roboflow100 이미지를 사용하여 모델의 강인성을 벤치마킹하고 왜곡이 텍스처, 가장자리, 색상 등 저수준 특징에 미치는 영향을 분석했습니다. 주요 발견사항으로는 (1) YOLOv12가 가장 뛰어난 성능을 보였으나 노이즈에 취약하며, (2) 노이즈가 가장자리와 텍스처 특징을 방해하여 탐지 성능을 저하시킨다는 점이 있습니다. 또한, (3) 이미지 수와 인스턴스 빈도가 탐지 성능에 주로 영향을 미치며, 객체의 외형은 부차적 영향을 미친다는 점을 발견했습니다. 마지막으로, 노이즈 인식 샘플 주입과 고급 향상 기법을 통한 미세 조정이 각각 노이즈와 실제 환경에서의 강인성을 개선하고, 향상된 도메인에서의 정확성을 높이는 데 효과적임을 확인했습니다. 이러한 결과는 강인하고 비용 효율적인 수중 객체 탐지 시스템 구축에 실질적인 지침을 제공합니다.

## 🎯 주요 포인트

- 1. YOLOv12 모델은 전반적으로 가장 강력한 성능을 보이지만, 노이즈에 매우 취약합니다.
- 2. 노이즈는 엣지와 텍스처 특징을 방해하여 노이즈가 많은 이미지에서 탐지 성능이 저하됩니다.
- 3. 이미지 수와 인스턴스 빈도가 탐지 성능에 주로 영향을 미치며, 객체의 외형은 부차적인 영향을 미칩니다.
- 4. 노이즈 인식 샘플 주입은 노이즈가 있는 환경과 실제 환경 모두에서 강건성을 향상시킵니다.
- 5. 고급 향상을 통한 미세 조정은 향상된 도메인에서의 정확도를 높이지만, 원본 데이터에서는 성능이 약간 저하됩니다.


---

*Generated on 2025-09-24 00:01:28*