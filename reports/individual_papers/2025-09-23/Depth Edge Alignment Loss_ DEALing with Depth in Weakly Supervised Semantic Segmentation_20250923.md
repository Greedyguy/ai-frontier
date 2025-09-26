---
keywords:
  - Weakly Supervised Learning
  - Depth Edge Alignment Loss
  - Semantic Segmentation
  - Autonomous Robotic Systems
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17702
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:00:03.405141",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Weakly Supervised Learning",
    "Depth Edge Alignment Loss",
    "Semantic Segmentation",
    "Autonomous Robotic Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Weakly Supervised Learning": 0.82,
    "Depth Edge Alignment Loss": 0.88,
    "Semantic Segmentation": 0.79,
    "Autonomous Robotic Systems": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Weakly Supervised Semantic Segmentation",
        "canonical": "Weakly Supervised Learning",
        "aliases": [
          "Weak Supervision",
          "Weakly Supervised Segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This term is crucial for linking to research on methods that reduce the need for extensive labeled data.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Depth Edge Alignment Loss",
        "canonical": "Depth Edge Alignment Loss",
        "aliases": [
          "DEAL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel loss function specific to this study, enhancing depth information utilization.",
        "novelty_score": 0.92,
        "connectivity_score": 0.67,
        "specificity_score": 0.91,
        "link_intent_score": 0.88
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental concept in computer vision, relevant for linking to a wide range of segmentation studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Robotic Systems",
        "canonical": "Autonomous Robotic Systems",
        "aliases": [
          "Robotics",
          "Autonomous Robots"
        ],
        "category": "specific_connectable",
        "rationale": "Links to research on robotics, particularly in applications involving computer vision.",
        "novelty_score": 0.53,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "model-agnostic",
      "improvements",
      "datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Weakly Supervised Semantic Segmentation",
      "resolved_canonical": "Weakly Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Depth Edge Alignment Loss",
      "resolved_canonical": "Depth Edge Alignment Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.67,
        "specificity": 0.91,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Robotic Systems",
      "resolved_canonical": "Autonomous Robotic Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.53,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17702.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17702](https://arxiv.org/abs/2509.17702)

## 🔗 유사한 논문
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (85.5% similar)
- [[2025-09-23/Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification_20250923|Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification]] (83.8% similar)
- [[2025-09-23/When Confidence Fails_ Revisiting Pseudo-Label Selection in Semi-supervised Semantic Segmentation_20250923|When Confidence Fails: Revisiting Pseudo-Label Selection in Semi-supervised Semantic Segmentation]] (83.8% similar)
- [[2025-09-18/Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (83.4% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semantic Segmentation|Semantic Segmentation]]
**🔗 Specific Connectable**: [[keywords/Weakly Supervised Learning|Weakly Supervised Learning]], [[keywords/Autonomous Robotic Systems|Autonomous Robotic Systems]]
**⚡ Unique Technical**: [[keywords/Depth Edge Alignment Loss|Depth Edge Alignment Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17702v1 Announce Type: new 
Abstract: Autonomous robotic systems applied to new domains require an abundance of expensive, pixel-level dense labels to train robust semantic segmentation models under full supervision. This study proposes a model-agnostic Depth Edge Alignment Loss to improve Weakly Supervised Semantic Segmentation models across different datasets. The methodology generates pixel-level semantic labels from image-level supervision, avoiding expensive annotation processes. While weak supervision is widely explored in traditional computer vision, our approach adds supervision with pixel-level depth information, a modality commonly available in robotic systems. We demonstrate how our approach improves segmentation performance across datasets and models, but can also be combined with other losses for even better performance, with improvements up to +5.439, +1.274 and +16.416 points in mean Intersection over Union on the PASCAL VOC / MS COCO validation, and the HOPE static onboarding split, respectively. Our code will be made publicly available.

## 📝 요약

이 연구는 새로운 분야에 적용되는 자율 로봇 시스템을 위한 약한 지도 학습 기반의 의미 분할 모델을 개선하기 위해 모델에 구애받지 않는 깊이 엣지 정렬 손실(Depth Edge Alignment Loss)을 제안합니다. 이 방법론은 이미지 수준의 감독으로부터 픽셀 수준의 의미 레이블을 생성하여 비용이 많이 드는 주석 과정을 피합니다. 특히, 로봇 시스템에서 흔히 사용되는 픽셀 수준의 깊이 정보를 추가하여 감독을 강화합니다. 이 접근법은 다양한 데이터셋과 모델에서 분할 성능을 향상시키며, 다른 손실 함수와 결합하여 성능을 더욱 개선할 수 있습니다. PASCAL VOC, MS COCO 검증 세트 및 HOPE 정적 온보딩 분할에서 평균 교차 합집합 점수가 각각 최대 +5.439, +1.274, +16.416 포인트 향상되었습니다. 연구의 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 본 연구는 Depth Edge Alignment Loss를 제안하여 약한 지도 학습 기반의 의미 분할 모델 성능을 향상시킨다.
- 2. 이미지 수준의 감독에서 픽셀 수준의 의미 레이블을 생성하여 고비용의 주석 과정을 피한다.
- 3. 로봇 시스템에서 일반적으로 사용 가능한 픽셀 수준의 깊이 정보를 추가하여 감독을 강화한다.
- 4. 제안된 방법은 다양한 데이터셋과 모델에서 분할 성능을 향상시키며, 다른 손실 함수와 결합하여 최대 +16.416 포인트의 성능 향상을 달성한다.
- 5. 연구의 코드는 공개될 예정이다.


---

*Generated on 2025-09-24 05:00:03*