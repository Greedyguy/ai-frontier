<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:35:47.441292",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Computer Vision",
    "YOLO Model",
    "Mask R-CNN",
    "Robotic Waste Management"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Computer Vision": 0.78,
    "YOLO Model": 0.81,
    "Mask R-CNN": 0.79,
    "Robotic Waste Management": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Image Segmentation",
        "canonical": "Computer Vision",
        "aliases": [
          "Image Analysis",
          "Image Processing"
        ],
        "category": "broad_technical",
        "rationale": "Image segmentation is a fundamental task in computer vision, linking to broader applications in robotics and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "YOLOv11",
        "canonical": "YOLO Model",
        "aliases": [
          "You Only Look Once"
        ],
        "category": "unique_technical",
        "rationale": "YOLO is a widely recognized model in object detection, crucial for linking advancements in real-time image processing.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.88,
        "link_intent_score": 0.81
      },
      {
        "surface": "Mask-RCNN",
        "canonical": "Mask R-CNN",
        "aliases": [
          "Mask Region-based Convolutional Neural Network"
        ],
        "category": "unique_technical",
        "rationale": "Mask R-CNN is a significant model for instance segmentation, enhancing connections in computer vision research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Waste Segregation",
        "canonical": "Robotic Waste Management",
        "aliases": [
          "Automated Waste Sorting",
          "E-waste Segregation"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept links robotics and environmental sustainability, a growing area of interest in AI applications.",
        "novelty_score": 0.65,
        "connectivity_score": 0.73,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "pick-and-place robots",
      "custom dataset",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Image Segmentation",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "YOLOv11",
      "resolved_canonical": "YOLO Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.88,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Mask-RCNN",
      "resolved_canonical": "Mask R-CNN",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Waste Segregation",
      "resolved_canonical": "Robotic Waste Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.73,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Image Segmentation and Classification of E-waste for Training Robots for Waste Segregation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.07122.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2506.07122](https://arxiv.org/abs/2506.07122)

## 🔗 유사한 논문
- [[2025-09-19/Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary_20250919|Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary]] (79.8% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (79.5% similar)
- [[2025-09-18/RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (79.4% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (79.0% similar)
- [[2025-09-19/Object Recognition and Force Estimation with the GelSight Baby Fin Ray_20250919|Object Recognition and Force Estimation with the GelSight Baby Fin Ray]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/YOLO Model|YOLO Model]], [[keywords/Mask R-CNN|Mask R-CNN]]
**🚀 Evolved Concepts**: [[keywords/Robotic Waste Management|Robotic Waste Management]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.07122v2 Announce Type: replace-cross 
Abstract: Industry partners provided a problem statement that involves classifying electronic waste using machine learning models that will be used by pick-and-place robots for waste segregation. This was achieved by taking common electronic waste items, such as a mouse and charger, unsoldering them, and taking pictures to create a custom dataset. Then state-of-the art YOLOv11 model was trained and run to achieve 70 mAP in real-time. Mask-RCNN model was also trained and achieved 41 mAP. The model can be integrated with pick-and-place robots to perform segregation of e-waste.

## 📝 요약

이 논문은 전자 폐기물을 분류하기 위해 기계 학습 모델을 활용하는 방법을 제안합니다. 연구진은 마우스와 충전기 같은 일반적인 전자 폐기물을 분해하고 사진을 촬영하여 맞춤형 데이터셋을 생성했습니다. 그런 다음 최첨단 YOLOv11 모델을 훈련시켜 실시간으로 70 mAP를 달성했으며, Mask-RCNN 모델도 훈련하여 41 mAP를 기록했습니다. 이 모델은 전자 폐기물 분류를 위해 픽 앤 플레이스 로봇과 통합될 수 있습니다.

## 🎯 주요 포인트

- 1. 전자 폐기물을 분류하기 위해 머신러닝 모델을 활용하여 분류 문제를 해결하고자 하였다.
- 2. 마우스와 충전기와 같은 일반적인 전자 폐기물 아이템을 분해하고 사진을 촬영하여 커스텀 데이터셋을 생성하였다.
- 3. 최신 YOLOv11 모델을 훈련시켜 실시간으로 70 mAP를 달성하였다.
- 4. Mask-RCNN 모델도 훈련시켜 41 mAP를 달성하였다.
- 5. 이 모델은 픽앤플레이스 로봇과 통합되어 전자 폐기물의 분류 작업을 수행할 수 있다.


---

*Generated on 2025-09-24 14:35:47*