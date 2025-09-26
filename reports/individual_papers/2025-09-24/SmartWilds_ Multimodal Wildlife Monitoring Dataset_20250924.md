<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:10:53.087638",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Computer Vision",
    "Conservation Ecology",
    "Bioacoustic Monitoring"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.79,
    "Computer Vision": 0.85,
    "Conservation Ecology": 0.78,
    "Bioacoustic Monitoring": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal wildlife monitoring",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal monitoring",
          "Multimodal dataset"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to research in integrating multiple data sources for comprehensive analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [
          "Vision-based analysis"
        ],
        "category": "broad_technical",
        "rationale": "Essential for linking to visual data analysis in wildlife monitoring.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Conservation ecology",
        "canonical": "Conservation Ecology",
        "aliases": [
          "Ecological conservation"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the ecological aspect of the study, enhancing domain-specific links.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bioacoustic recordings",
        "canonical": "Bioacoustic Monitoring",
        "aliases": [
          "Acoustic data",
          "Sound recordings"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the use of sound data in wildlife monitoring, linking to niche research areas.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "monitoring",
      "species"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal wildlife monitoring",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Conservation ecology",
      "resolved_canonical": "Conservation Ecology",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bioacoustic recordings",
      "resolved_canonical": "Bioacoustic Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SmartWilds: Multimodal Wildlife Monitoring Dataset

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18894.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18894](https://arxiv.org/abs/2509.18894)

## 🔗 유사한 논문
- [[2025-09-22/Overview of PlantCLEF 2024_ multi-species plant identification in vegetation plot images_20250922|Overview of PlantCLEF 2024: multi-species plant identification in vegetation plot images]] (77.5% similar)
- [[2025-09-23/Overview of PlantCLEF 2025_ Multi-Species Plant Identification in Vegetation Quadrat Images_20250923|Overview of PlantCLEF 2025: Multi-Species Plant Identification in Vegetation Quadrat Images]] (77.1% similar)
- [[2025-09-24/V-SenseDrive_ A Privacy-Preserving Road Video and In-Vehicle Sensor Fusion Framework for Road Safety & Driver Behaviour Modelling_20250924|V-SenseDrive: A Privacy-Preserving Road Video and In-Vehicle Sensor Fusion Framework for Road Safety & Driver Behaviour Modelling]] (76.8% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (76.0% similar)
- [[2025-09-23/PM25Vision_ A Large-Scale Benchmark Dataset for Visual Estimation of Air Quality_20250923|PM25Vision: A Large-Scale Benchmark Dataset for Visual Estimation of Air Quality]] (76.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Conservation Ecology|Conservation Ecology]], [[keywords/Bioacoustic Monitoring|Bioacoustic Monitoring]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18894v1 Announce Type: new 
Abstract: We present the first release of SmartWilds, a multimodal wildlife monitoring dataset. SmartWilds is a synchronized collection of drone imagery, camera trap photographs and videos, and bioacoustic recordings collected during summer 2025 at The Wilds safari park in Ohio. This dataset supports multimodal AI research for comprehensive environmental monitoring, addressing critical needs in endangered species research, conservation ecology, and habitat management. Our pilot deployment captured four days of synchronized monitoring across three modalities in a 220-acre pasture containing Pere David's deer, Sichuan takin, Przewalski's horses, as well as species native to Ohio, including bald eagles, white-tailed deer, and coyotes. We provide a comparative analysis of sensor modality performance, demonstrating complementary strengths for landuse patterns, species detection, behavioral analysis, and habitat monitoring. This work establishes reproducible protocols for multimodal wildlife monitoring while contributing open datasets to advance conservation computer vision research. Future releases will include synchronized GPS tracking data from tagged individuals, citizen science data, and expanded temporal coverage across multiple seasons.

## 📝 요약

SmartWilds는 드론 이미지, 카메라 트랩 사진 및 비디오, 생물음향 녹음을 포함한 멀티모달 야생동물 모니터링 데이터셋으로, 2025년 여름 오하이오의 The Wilds 사파리 공원에서 수집되었습니다. 이 데이터셋은 멸종 위기 종 연구, 보전 생태학, 서식지 관리에 필요한 포괄적인 환경 모니터링을 지원합니다. 연구는 220에이커의 초원에서 4일간 3가지 모달리티로 동기화된 모니터링을 수행했으며, 다양한 종의 서식지와 행동 분석을 위한 센서 모달리티 성능을 비교 분석했습니다. 이 연구는 멀티모달 야생동물 모니터링을 위한 재현 가능한 프로토콜을 확립하고, 보전 컴퓨터 비전 연구를 위한 공개 데이터셋을 제공합니다. 향후 GPS 추적 데이터와 시민 과학 데이터를 포함한 확장된 데이터셋이 추가로 공개될 예정입니다.

## 🎯 주요 포인트

- 1. SmartWilds는 드론 이미지, 카메라 트랩 사진 및 비디오, 생물음향 녹음을 포함한 멀티모달 야생동물 모니터링 데이터셋의 첫 번째 릴리스입니다.
- 2. 이 데이터셋은 멸종 위기 종 연구, 보전 생태학, 서식지 관리의 중요한 요구를 해결하기 위해 멀티모달 AI 연구를 지원합니다.
- 3. 220에이커의 목초지에서 4일간의 동기화된 모니터링을 통해 다양한 종의 서식지와 행동을 분석했습니다.
- 4. 센서 모달리티 성능의 비교 분석을 통해 토지 이용 패턴, 종 탐지, 행동 분석 및 서식지 모니터링에 대한 상호 보완적인 강점을 입증했습니다.
- 5. 향후 릴리스에는 태그가 부착된 개체의 GPS 추적 데이터, 시민 과학 데이터 및 여러 계절에 걸친 확장된 시간적 범위가 포함될 예정입니다.


---

*Generated on 2025-09-24 16:10:53*