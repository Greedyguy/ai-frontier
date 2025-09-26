---
keywords:
  - Depth Imaging
  - Autonomous Driving Systems
  - Cityscapes Dataset
  - Multi-layered Training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17686
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:06:07.844807",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Depth Imaging",
    "Autonomous Driving Systems",
    "Cityscapes Dataset",
    "Multi-layered Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Depth Imaging": 0.78,
    "Autonomous Driving Systems": 0.82,
    "Cityscapes Dataset": 0.8,
    "Multi-layered Training": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Depth imaging",
        "canonical": "Depth Imaging",
        "aliases": [
          "Depth Maps",
          "Depth Estimation"
        ],
        "category": "unique_technical",
        "rationale": "Depth imaging is a critical component in autonomous systems, providing essential data for object detection and measurement.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Autonomous Driving Systems",
        "canonical": "Autonomous Driving Systems",
        "aliases": [
          "ADS",
          "Self-Driving Cars"
        ],
        "category": "evolved_concepts",
        "rationale": "Autonomous driving systems are a rapidly evolving field with significant research interest, making it a strong link candidate.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "Cityscapes dataset",
        "canonical": "Cityscapes Dataset",
        "aliases": [
          "Cityscapes"
        ],
        "category": "specific_connectable",
        "rationale": "The Cityscapes dataset is widely used for benchmarking in computer vision, providing a common ground for linking related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.79,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-layered training approach",
        "canonical": "Multi-layered Training",
        "aliases": [
          "Layered Training",
          "Multi-layer Training"
        ],
        "category": "broad_technical",
        "rationale": "Multi-layered training is a fundamental technique in machine learning, relevant to various applications and models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "vehicle",
      "environment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Depth imaging",
      "resolved_canonical": "Depth Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Autonomous Driving Systems",
      "resolved_canonical": "Autonomous Driving Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Cityscapes dataset",
      "resolved_canonical": "Cityscapes Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.79,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-layered training approach",
      "resolved_canonical": "Multi-layered Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Predicting Depth Maps from Single RGB Images and Addressing Missing Information in Depth Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17686.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17686](https://arxiv.org/abs/2509.17686)

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (81.9% similar)
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (81.7% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (81.5% similar)
- [[2025-09-22/Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles_20250922|Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles]] (80.9% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-layered Training|Multi-layered Training]]
**🔗 Specific Connectable**: [[keywords/Cityscapes Dataset|Cityscapes Dataset]]
**⚡ Unique Technical**: [[keywords/Depth Imaging|Depth Imaging]]
**🚀 Evolved Concepts**: [[keywords/Autonomous Driving Systems|Autonomous Driving Systems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17686v1 Announce Type: cross 
Abstract: Depth imaging is a crucial area in Autonomous Driving Systems (ADS), as it plays a key role in detecting and measuring objects in the vehicle's surroundings. However, a significant challenge in this domain arises from missing information in Depth images, where certain points are not measurable due to gaps or inconsistencies in pixel data. Our research addresses two key tasks to overcome this challenge. First, we developed an algorithm using a multi-layered training approach to generate Depth images from a single RGB image. Second, we addressed the issue of missing information in Depth images by applying our algorithm to rectify these gaps, resulting in Depth images with complete and accurate data. We further tested our algorithm on the Cityscapes dataset and successfully resolved the missing information in its Depth images, demonstrating the effectiveness of our approach in real-world urban environments.

## 📝 요약

이 논문은 자율주행 시스템에서 중요한 역할을 하는 깊이 영상의 결측 정보를 해결하기 위한 연구를 다룹니다. 연구의 주요 기여는 두 가지 과제 해결에 있습니다. 첫째, 단일 RGB 이미지로부터 깊이 이미지를 생성하는 다층 학습 알고리즘을 개발했습니다. 둘째, 이 알고리즘을 활용하여 깊이 이미지의 결측 정보를 보완하고, 완전하고 정확한 데이터를 갖춘 깊이 이미지를 생성했습니다. 이 방법은 Cityscapes 데이터셋을 통해 테스트되었으며, 실제 도시 환경에서의 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. 자율 주행 시스템에서 깊이 이미지는 주변 객체를 감지하고 측정하는 데 중요한 역할을 한다.
- 2. 깊이 이미지에서 정보 누락 문제는 픽셀 데이터의 간격이나 불일치로 인해 발생한다.
- 3. 단일 RGB 이미지로부터 깊이 이미지를 생성하는 알고리즘을 개발하였다.
- 4. 알고리즘을 적용하여 깊이 이미지의 정보 누락 문제를 해결하고 완전하고 정확한 데이터를 제공하였다.
- 5. Cityscapes 데이터셋을 통해 알고리즘의 실효성을 검증하였다.


---

*Generated on 2025-09-24 00:06:07*