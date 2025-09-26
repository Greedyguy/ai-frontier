---
keywords:
  - Computer Vision
  - YOLO
  - Optical Character Recognition
  - Assistive Technology
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2503.04139
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:23:24.248443",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Computer Vision",
    "YOLO",
    "Optical Character Recognition",
    "Assistive Technology"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Computer Vision": 0.85,
    "YOLO": 0.88,
    "Optical Character Recognition": 0.82,
    "Assistive Technology": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Computer Vision is a fundamental technology enabling the detection of construction sites, linking to a wide range of visual processing applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "YOLO-based model",
        "canonical": "YOLO",
        "aliases": [
          "You Only Look Once"
        ],
        "category": "specific_connectable",
        "rationale": "YOLO is a specific object detection model that is crucial for identifying construction elements, providing strong connections to object detection research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Optical Character Recognition",
        "canonical": "Optical Character Recognition",
        "aliases": [
          "OCR"
        ],
        "category": "specific_connectable",
        "rationale": "OCR is essential for interpreting construction signage, linking to text recognition technologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Assistive Technology",
        "canonical": "Assistive Technology",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Assistive Technology is a unique application area for this system, linking to innovations in accessibility.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "hazard detection",
      "navigation tools",
      "urban environments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "YOLO-based model",
      "resolved_canonical": "YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Optical Character Recognition",
      "resolved_canonical": "Optical Character Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Assistive Technology",
      "resolved_canonical": "Assistive Technology",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Robust Computer-Vision based Construction Site Detection for Assistive-Technology Applications

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.04139.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2503.04139](https://arxiv.org/abs/2503.04139)

## 🔗 유사한 논문
- [[2025-09-24/NaviSense_ A Multimodal Assistive Mobile application for Object Retrieval by Persons with Visual Impairment_20250924|NaviSense: A Multimodal Assistive Mobile application for Object Retrieval by Persons with Visual Impairment]] (85.1% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (82.1% similar)
- [[2025-09-18/BIM Informed Visual SLAM for Construction Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (81.9% similar)
- [[2025-09-23/Vision-Based Driver Drowsiness Monitoring_ Comparative Analysis of YOLOv5-v11 Models_20250923|Vision-Based Driver Drowsiness Monitoring: Comparative Analysis of YOLOv5-v11 Models]] (81.8% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/YOLO|YOLO]], [[keywords/Optical Character Recognition|Optical Character Recognition]]
**⚡ Unique Technical**: [[keywords/Assistive Technology|Assistive Technology]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04139v2 Announce Type: replace 
Abstract: Purpose: Navigating urban environments poses significant challenges for individuals who are blind or have low vision, especially in areas affected by construction. Construction zones introduce hazards such as uneven surfaces, barriers, hazardous materials, excessive noise, and altered routes that obstruct familiar paths and compromise safety. Although navigation tools assist in trip planning, they often overlook these temporary obstacles. Existing hazard detection systems also struggle with the visual variability of construction sites. Methods: We developed a computer vision--based assistive system integrating three modules: an open-vocabulary object detector to identify diverse construction-related elements, a YOLO-based model specialized in detecting scaffolding and poles, and an optical character recognition module to interpret construction signage. Results: In static testing at seven construction sites using images from multiple stationary viewpoints, the system achieved 88.56% overall accuracy. It consistently identified relevant objects within 2--10 meters and at approach angles up to 75$^{\circ}$. At 2--4 meters, detection was perfect (100%) across all angles. Even at 10 meters, six of seven sites remained detectable within a 15$^{\circ}$ approach. In dynamic testing along a 0.5-mile urban route containing eight construction sites, the system analyzed every frame of a first-person walking video. It achieved 87.26% accuracy in distinguishing construction from non-construction areas, rising to 92.0% with a 50-frame majority vote filter. Conclusion: The system can reliably detect construction sites in real time and at sufficient distances to provide advance warnings, enabling individuals with visual impairments to make safer mobility decisions such as proceeding with caution or rerouting.

## 📝 요약

이 논문은 시각 장애인들이 도시 환경에서 특히 공사 구역을 안전하게 탐색할 수 있도록 돕는 컴퓨터 비전 기반 보조 시스템을 개발했습니다. 이 시스템은 다양한 공사 관련 요소를 식별하는 개방형 어휘 객체 탐지기, 비계 및 기둥을 감지하는 YOLO 기반 모델, 공사 표지판을 해석하는 광학 문자 인식 모듈로 구성되어 있습니다. 7개의 공사 현장에서 정적 테스트 결과, 시스템은 88.56%의 정확도를 보였으며, 2~10미터 거리와 최대 75도 접근 각도에서 일관되게 관련 객체를 식별했습니다. 동적 테스트에서는 0.5마일의 도시 경로를 따라 87.26%의 정확도로 공사 구역을 식별했으며, 50프레임 다수결 필터를 적용하면 92.0%로 정확도가 향상되었습니다. 이 시스템은 실시간으로 공사 구역을 감지하여 시각 장애인들이 안전한 이동 결정을 내릴 수 있도록 돕습니다.

## 🎯 주요 포인트

- 1. 시각 장애인을 위한 도시 환경 내비게이션은 공사 구역에서 특히 어려움을 겪으며, 기존 도구들은 이러한 임시 장애물을 간과하는 경향이 있다.
- 2. 본 연구에서는 다양한 공사 관련 요소를 식별하는 개방형 어휘 객체 탐지기, 비계 및 기둥을 감지하는 YOLO 기반 모델, 공사 표지판을 해석하는 광학 문자 인식 모듈을 통합한 컴퓨터 비전 기반 보조 시스템을 개발하였다.
- 3. 정적 테스트 결과, 시스템은 88.56%의 정확도를 기록했으며, 2-4미터 거리에서는 모든 각도에서 완벽한(100%) 탐지를 이루었다.
- 4. 동적 테스트에서는 0.5마일의 도시 경로에서 87.26%의 정확도로 공사 구역과 비공사 구역을 구분했으며, 50프레임 다수결 필터를 적용했을 때 정확도는 92.0%로 상승했다.
- 5. 본 시스템은 실시간으로 공사 구역을 감지하여 시각 장애인이 안전한 이동 결정을 내릴 수 있도록 사전 경고를 제공한다.


---

*Generated on 2025-09-26 09:23:24*