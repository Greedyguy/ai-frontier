---
keywords:
  - Deer Detection
  - Edge Computing
  - YOLO
  - NVIDIA Jetson
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20318
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:16:20.345980",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deer Detection",
    "Edge Computing",
    "YOLO",
    "NVIDIA Jetson"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deer Detection": 0.78,
    "Edge Computing": 0.82,
    "YOLO": 0.85,
    "NVIDIA Jetson": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "YOLO-based Deer Detection",
        "canonical": "Deer Detection",
        "aliases": [
          "YOLO Deer Detection",
          "Deer Detection System"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on improving detection methods specifically for deer using YOLO models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Edge Devices",
        "canonical": "Edge Computing",
        "aliases": [
          "Edge Platforms",
          "Edge Hardware"
        ],
        "category": "broad_technical",
        "rationale": "Edge computing is crucial for deploying AI models in real-world scenarios, linking to broader discussions on computational efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "YOLO architectures",
        "canonical": "YOLO",
        "aliases": [
          "YOLO models",
          "YOLO variants"
        ],
        "category": "specific_connectable",
        "rationale": "YOLO is a well-known object detection framework, and its variants are central to the study's comparative analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "NVIDIA Jetson AGX Xavier",
        "canonical": "NVIDIA Jetson",
        "aliases": [
          "Jetson AGX",
          "Jetson Xavier"
        ],
        "category": "unique_technical",
        "rationale": "This specific hardware platform is key to the study's evaluation of model performance on edge devices.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.9,
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
      "candidate_surface": "YOLO-based Deer Detection",
      "resolved_canonical": "Deer Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Edge Devices",
      "resolved_canonical": "Edge Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "YOLO architectures",
      "resolved_canonical": "YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "NVIDIA Jetson AGX Xavier",
      "resolved_canonical": "NVIDIA Jetson",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Comprehensive Evaluation of YOLO-based Deer Detection Performance on Edge Devices

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20318.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20318](https://arxiv.org/abs/2509.20318)

## 🔗 유사한 논문
- [[2025-09-23/Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture_20250923|Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture]] (85.6% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (84.8% similar)
- [[2025-09-18/Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies_20250918|Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies]] (84.5% similar)
- [[2025-09-23/An Empirical Study on the Robustness of YOLO Models for Underwater Object Detection_20250923|An Empirical Study on the Robustness of YOLO Models for Underwater Object Detection]] (83.9% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Edge Computing|Edge Computing]]
**🔗 Specific Connectable**: [[keywords/YOLO|YOLO]]
**⚡ Unique Technical**: [[keywords/Deer Detection|Deer Detection]], [[keywords/NVIDIA Jetson|NVIDIA Jetson]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20318v1 Announce Type: new 
Abstract: The escalating economic losses in agriculture due to deer intrusion, estimated to be in the hundreds of millions of dollars annually in the U.S., highlight the inadequacy of traditional mitigation strategies since these methods are often labor-intensive, costly, and ineffective for modern farming systems. To overcome this, there is a critical need for intelligent, autonomous solutions which require accurate and efficient deer detection. But the progress in this field is impeded by a significant gap in the literature, mainly the lack of a domain-specific, practical dataset and limited study on the on-field deployability of deer detection systems. Addressing this gap, this study presents a comprehensive evaluation of state-of-the-art deep learning models for deer detection in challenging real-world scenarios. The contributions of this work are threefold. First, we introduce a curated, publicly available dataset of 3,095 annotated images with bounding-box annotations of deer, derived from the Idaho Cameratraps project. Second, we provide an extensive comparative analysis of 12 model variants across four recent YOLO architectures(v8, v9, v10, and v11). Finally, we benchmarked performance on a high-end NVIDIA RTX 5090 GPU and evaluated on two representative edge computing platforms: Raspberry Pi 5 and NVIDIA Jetson AGX Xavier. Results show that the real-time detection is not feasible in Raspberry Pi without hardware-specific model optimization, while NVIDIA Jetson provides greater than 30 FPS with GPU-accelerated inference on 's' and 'n' series models. This study also reveals that smaller, architecturally advanced models such as YOLOv11n, YOLOv8s, and YOLOv9s offer the optimal balance of high accuracy (AP@.5 > 0.85) and computational efficiency (FPS > 30). To support further research, both the source code and datasets are publicly available at https://github.com/WinnerBishal/track-the-deer.

## 📝 요약

이 연구는 미국 농업에서 사슴 침입으로 인한 경제적 손실을 줄이기 위해 지능적이고 자율적인 사슴 탐지 시스템의 필요성을 강조합니다. 기존 방법의 한계를 극복하기 위해, 연구진은 3,095개의 사슴 이미지로 구성된 새로운 데이터셋을 제공하고, 최신 YOLO 모델(v8, v9, v10, v11)을 비교 분석했습니다. NVIDIA Jetson AGX Xavier에서는 GPU 가속을 통해 30 FPS 이상의 성능을 보였지만, Raspberry Pi에서는 하드웨어 최적화 없이는 실시간 탐지가 어려웠습니다. YOLOv11n, YOLOv8s, YOLOv9s 모델은 높은 정확도(AP@.5 > 0.85)와 효율성을 보여 최적의 성능을 제공합니다. 연구 결과와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 미국 농업에서 사슴 침입으로 인한 경제적 손실이 연간 수억 달러에 달하며, 기존 완화 전략의 비효율성을 드러냅니다.
- 2. 이 연구는 사슴 탐지를 위한 최신 딥러닝 모델의 평가를 통해, 분야별 실용적인 데이터셋의 부족과 현장 배치 가능성에 대한 연구의 한계를 해결합니다.
- 3. Idaho Cameratraps 프로젝트에서 수집한 3,095개의 주석 이미지로 구성된 공개 데이터셋을 소개합니다.
- 4. YOLO 아키텍처(v8, v9, v10, v11)의 12개 모델 변형에 대한 비교 분석을 수행하고, 고급 GPU 및 엣지 컴퓨팅 플랫폼에서 성능을 평가했습니다.
- 5. YOLOv11n, YOLOv8s, YOLOv9s 모델이 높은 정확도와 계산 효율성을 제공하며, 연구 지원을 위해 소스 코드와 데이터셋이 공개되었습니다.


---

*Generated on 2025-09-26 09:16:20*