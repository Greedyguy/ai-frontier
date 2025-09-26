---
keywords:
  - Near-Field Lighting Bundle Adjustment
  - Simultaneous Localization and Mapping
  - Neural Rendering
  - Endoscopy Procedure
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2412.13176
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:29:53.314246",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Near-Field Lighting Bundle Adjustment",
    "Simultaneous Localization and Mapping",
    "Neural Rendering",
    "Endoscopy Procedure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Near-Field Lighting Bundle Adjustment": 0.8,
    "Simultaneous Localization and Mapping": 0.85,
    "Neural Rendering": 0.78,
    "Endoscopy Procedure": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Near-Field Lighting Bundle Adjustment",
        "canonical": "Near-Field Lighting Bundle Adjustment",
        "aliases": [
          "NFL-BA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique specific to SLAM systems under dynamic lighting conditions, enhancing connectivity with other SLAM-related research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Simultaneous Localization and Mapping",
        "canonical": "Simultaneous Localization and Mapping",
        "aliases": [
          "SLAM"
        ],
        "category": "broad_technical",
        "rationale": "SLAM is a foundational concept in robotics and computer vision, linking to a wide range of related research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neural Rendering",
        "canonical": "Neural Rendering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Neural rendering is a cutting-edge technique in computer vision, relevant to the integration of NFL-BA in SLAM systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Endoscopy Procedure",
        "canonical": "Endoscopy Procedure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This application domain is crucial for understanding the practical impact of the proposed method in medical settings.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "dynamic lighting",
      "camera tracking",
      "indoor scenes"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Near-Field Lighting Bundle Adjustment",
      "resolved_canonical": "Near-Field Lighting Bundle Adjustment",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Simultaneous Localization and Mapping",
      "resolved_canonical": "Simultaneous Localization and Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neural Rendering",
      "resolved_canonical": "Neural Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Endoscopy Procedure",
      "resolved_canonical": "Endoscopy Procedure",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting

**Korean Title:** NFL-BA: 동적 조명에서 SLAM을 위한 근거리 광선 조정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.13176.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2412.13176](https://arxiv.org/abs/2412.13176)

## 🔗 유사한 논문
- [[2025-09-18/BIM Informed Visual SLAM for Construction Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (83.3% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (81.8% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (79.6% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (78.8% similar)
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Simultaneous Localization and Mapping|Simultaneous Localization and Mapping]]
**🔗 Specific Connectable**: [[keywords/Neural Rendering|Neural Rendering]]
**⚡ Unique Technical**: [[keywords/Near-Field Lighting Bundle Adjustment|Near-Field Lighting Bundle Adjustment]], [[keywords/Endoscopy Procedure|Endoscopy Procedure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.13176v3 Announce Type: replace 
Abstract: Simultaneous Localization and Mapping (SLAM) systems typically assume static, distant illumination; however, many real-world scenarios, such as endoscopy, subterranean robotics, and search & rescue in collapsed environments, require agents to operate with a co-located light and camera in the absence of external lighting. In such cases, dynamic near-field lighting introduces strong, view-dependent shading that significantly degrades SLAM performance. We introduce Near-Field Lighting Bundle Adjustment Loss (NFL-BA) which explicitly models near-field lighting as a part of Bundle Adjustment loss and enables better performance for scenes captured with dynamic lighting. NFL-BA can be integrated into neural rendering-based SLAM systems with implicit or explicit scene representations. Our evaluations mainly focus on endoscopy procedure where SLAM can enable autonomous navigation, guidance to unsurveyed regions, blindspot detections, and 3D visualizations, which can significantly improve patient outcomes and endoscopy experience for both physicians and patients. Replacing Photometric Bundle Adjustment loss of SLAM systems with NFL-BA leads to significant improvement in camera tracking, 37% for MonoGS and 14% for EndoGS, and leads to state-of-the-art camera tracking and mapping performance on the C3VD colonoscopy dataset. Further evaluation on indoor scenes captured with phone camera with flashlight turned on, also demonstrate significant improvement in SLAM performance due to NFL-BA. See results at https://asdunnbe.github.io/NFL-BA/

## 🔍 Abstract (한글 번역)

arXiv:2412.13176v3 발표 유형: 교체  
초록: 동시 위치 추정 및 지도 작성(SLAM) 시스템은 일반적으로 정적이고 먼 조명을 가정하지만, 내시경, 지하 로봇 공학, 붕괴된 환경에서의 수색 및 구조와 같은 많은 실제 시나리오에서는 외부 조명이 없는 상태에서 카메라와 조명이 함께 위치하여 작동해야 합니다. 이러한 경우, 동적 근거리 조명은 강한 시점 의존적 음영을 도입하여 SLAM 성능을 크게 저하시킵니다. 우리는 근거리 조명을 번들 조정 손실의 일부로 명시적으로 모델링하여 동적 조명으로 캡처된 장면에서 더 나은 성능을 가능하게 하는 근거리 조명 번들 조정 손실(NFL-BA)을 소개합니다. NFL-BA는 암묵적 또는 명시적 장면 표현을 가진 신경 렌더링 기반 SLAM 시스템에 통합될 수 있습니다. 우리의 평가에서는 주로 내시경 절차에 중점을 두며, 여기서 SLAM은 자율 내비게이션, 조사되지 않은 지역으로의 안내, 사각지대 탐지 및 3D 시각화를 가능하게 하여 환자 결과와 의사 및 환자의 내시경 경험을 크게 향상시킬 수 있습니다. SLAM 시스템의 광도 번들 조정 손실을 NFL-BA로 대체하면 MonoGS의 경우 37%, EndoGS의 경우 14%의 카메라 추적 성능이 크게 향상되며, C3VD 대장내시경 데이터셋에서 최첨단 카메라 추적 및 매핑 성능을 달성합니다. 플래시가 켜진 상태로 휴대폰 카메라로 촬영한 실내 장면에 대한 추가 평가에서도 NFL-BA로 인해 SLAM 성능이 크게 향상됨을 보여줍니다. 결과는 https://asdunnbe.github.io/NFL-BA/에서 확인할 수 있습니다.

## 📝 요약

이 논문은 동시 위치추정 및 지도작성(SLAM) 시스템에서 동적 근거리 조명이 성능에 미치는 영향을 해결하기 위해 Near-Field Lighting Bundle Adjustment Loss (NFL-BA)를 제안합니다. NFL-BA는 번들 조정 손실에 근거리 조명을 명시적으로 모델링하여 동적 조명 하에서의 성능을 향상시킵니다. 이 방법은 신경 렌더링 기반 SLAM 시스템에 통합될 수 있으며, 특히 내시경 절차에서 자율 내비게이션, 미탐사 지역 안내, 사각지대 탐지 및 3D 시각화를 가능하게 하여 환자 결과와 의료진의 경험을 개선할 수 있습니다. NFL-BA를 기존의 광도 기반 번들 조정 손실 대신 적용하면 카메라 추적 성능이 MonoGS에서 37%, EndoGS에서 14% 향상되며, C3VD 대장내시경 데이터셋에서 최첨단 성능을 달성합니다. 또한, 플래시가 켜진 휴대폰 카메라로 촬영한 실내 장면에서도 SLAM 성능이 크게 개선됨을 보여줍니다.

## 🎯 주요 포인트

- 1. SLAM 시스템은 일반적으로 정적이고 먼 조명을 가정하지만, 실제 시나리오에서는 카메라와 조명이 함께 이동하는 경우가 많아 성능 저하가 발생한다.
- 2. Near-Field Lighting Bundle Adjustment Loss (NFL-BA)는 동적 근거리 조명을 모델링하여 SLAM 성능을 향상시킨다.
- 3. NFL-BA는 신경 렌더링 기반 SLAM 시스템에 통합될 수 있으며, 특히 내시경 절차에서 자율 내비게이션 및 3D 시각화를 통해 환자 결과를 개선할 수 있다.
- 4. NFL-BA를 사용하면 MonoGS와 EndoGS에서 각각 37%와 14%의 카메라 추적 성능 향상이 이루어지며, C3VD 대장내시경 데이터셋에서 최첨단 성능을 달성한다.
- 5. 플래시가 켜진 휴대폰 카메라로 촬영한 실내 장면에서도 NFL-BA가 SLAM 성능을 크게 향상시킨다.


---

*Generated on 2025-09-23 12:29:53*