<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:57:56.663679",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "UAV Localization",
    "Orthographic Geodata",
    "AdHoP",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "UAV Localization": 0.8,
    "Orthographic Geodata": 0.78,
    "AdHoP": 0.72,
    "Multimodal Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "UAV 6-DoF Localization",
        "canonical": "UAV Localization",
        "aliases": [
          "6-DoF UAV Localization"
        ],
        "category": "unique_technical",
        "rationale": "This term captures the specific focus on UAV localization, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Orthographic Geodata",
        "canonical": "Orthographic Geodata",
        "aliases": [
          "Orthographic Data"
        ],
        "category": "unique_technical",
        "rationale": "The use of orthographic geodata is a novel approach in the context of UAV localization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "AdHoP",
        "canonical": "AdHoP",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "AdHoP is a unique refinement technique introduced in the paper, enhancing feature matching.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.72
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "The dataset includes multiple modalities, aligning with the concept of multimodal learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "mapping",
      "large-area inspection",
      "search-and-rescue operations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "UAV 6-DoF Localization",
      "resolved_canonical": "UAV Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Orthographic Geodata",
      "resolved_canonical": "Orthographic Geodata",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AdHoP",
      "resolved_canonical": "AdHoP",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# OrthoLoC: UAV 6-DoF Localization and Calibration Using Orthographic Geodata

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18350.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18350](https://arxiv.org/abs/2509.18350)

## 🔗 유사한 논문
- [[2025-09-23/SWA-PF_ Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments_20250923|SWA-PF: Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments]] (84.1% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (81.7% similar)
- [[2025-09-18/InterKey_ Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap_20250918|InterKey: Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap]] (80.3% similar)
- [[2025-09-23/DragOSM_ Extract Building Roofs and Footprints from Aerial Images by Aligning Historical Labels_20250923|DragOSM: Extract Building Roofs and Footprints from Aerial Images by Aligning Historical Labels]] (80.0% similar)
- [[2025-09-23/StereoAdapter_ Adapting Stereo Depth Estimation to Underwater Scenes_20250923|StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/UAV Localization|UAV Localization]], [[keywords/Orthographic Geodata|Orthographic Geodata]], [[keywords/AdHoP|AdHoP]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18350v1 Announce Type: new 
Abstract: Accurate visual localization from aerial views is a fundamental problem with applications in mapping, large-area inspection, and search-and-rescue operations. In many scenarios, these systems require high-precision localization while operating with limited resources (e.g., no internet connection or GNSS/GPS support), making large image databases or heavy 3D models impractical. Surprisingly, little attention has been given to leveraging orthographic geodata as an alternative paradigm, which is lightweight and increasingly available through free releases by governmental authorities (e.g., the European Union). To fill this gap, we propose OrthoLoC, the first large-scale dataset comprising 16,425 UAV images from Germany and the United States with multiple modalities. The dataset addresses domain shifts between UAV imagery and geospatial data. Its paired structure enables fair benchmarking of existing solutions by decoupling image retrieval from feature matching, allowing isolated evaluation of localization and calibration performance. Through comprehensive evaluation, we examine the impact of domain shifts, data resolutions, and covisibility on localization accuracy. Finally, we introduce a refinement technique called AdHoP, which can be integrated with any feature matcher, improving matching by up to 95% and reducing translation error by up to 63%. The dataset and code are available at: https://deepscenario.github.io/OrthoLoC.

## 📝 요약

이 논문은 항공 이미지에서 정확한 시각적 위치 추정을 위한 새로운 접근법을 제안합니다. 기존의 대규모 이미지 데이터베이스나 3D 모델이 아닌, 경량의 정사각형 지리 데이터를 활용하는 OrthoLoC라는 대규모 데이터셋을 소개합니다. 이 데이터셋은 독일과 미국의 UAV 이미지 16,425장을 포함하며, 이미지 검색과 특징 매칭을 분리하여 공정한 벤치마킹을 가능하게 합니다. 또한, 도메인 이동, 데이터 해상도, 공가시성이 위치 추정 정확도에 미치는 영향을 평가합니다. 마지막으로, AdHoP라는 정교화 기법을 도입하여 특징 매처와 결합 시 매칭 성능을 최대 95% 개선하고, 번역 오류를 최대 63% 줄일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. OrthoLoC는 독일과 미국의 16,425개의 UAV 이미지를 포함한 대규모 데이터셋으로, 다양한 모달리티를 제공합니다.
- 2. 이 데이터셋은 UAV 이미지와 지리 공간 데이터 간의 도메인 이동 문제를 해결하며, 이미지 검색과 특징 매칭을 분리하여 공정한 벤치마킹을 가능하게 합니다.
- 3. AdHoP라는 정제 기법을 도입하여 최대 95%의 매칭 개선과 최대 63%의 번역 오류 감소를 달성할 수 있습니다.
- 4. OrthoLoC 데이터셋은 대규모 이미지 데이터베이스나 무거운 3D 모델 없이도 높은 정밀도의 시각적 위치 추정을 가능하게 합니다.
- 5. 데이터셋과 코드는 https://deepscenario.github.io/OrthoLoC에서 제공됩니다.


---

*Generated on 2025-09-24 15:57:56*