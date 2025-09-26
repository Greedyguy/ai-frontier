---
keywords:
  - UAV Navigation
  - Relative Navigation
  - Search and Rescue Operations
  - Reactive High-Speed Flight
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19452
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:54:00.316111",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "UAV Navigation",
    "Relative Navigation",
    "Search and Rescue Operations",
    "Reactive High-Speed Flight"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "UAV Navigation": 0.75,
    "Relative Navigation": 0.72,
    "Search and Rescue Operations": 0.7,
    "Reactive High-Speed Flight": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "UAV Navigation",
        "canonical": "UAV Navigation",
        "aliases": [
          "Drone Navigation",
          "Unmanned Aerial Vehicle Navigation"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on high-speed navigation in unstructured environments.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Relative Navigation",
        "canonical": "Relative Navigation",
        "aliases": [
          "Relative Positioning",
          "Relative Localization"
        ],
        "category": "unique_technical",
        "rationale": "Relative navigation is a key concept for tracking and navigation without global localization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Search and Rescue Operations",
        "canonical": "Search and Rescue Operations",
        "aliases": [
          "SAR Operations",
          "Rescue Missions"
        ],
        "category": "specific_connectable",
        "rationale": "The application context of search and rescue is crucial for understanding the use case of the technology.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reactive High-Speed Flight",
        "canonical": "Reactive High-Speed Flight",
        "aliases": [
          "High-Speed Reactive Flight",
          "Fast Reactive Flight"
        ],
        "category": "unique_technical",
        "rationale": "This concept is essential for understanding the paper's contribution to UAV agility and speed.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "UAV Navigation",
      "resolved_canonical": "UAV Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Relative Navigation",
      "resolved_canonical": "Relative Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Search and Rescue Operations",
      "resolved_canonical": "Search and Rescue Operations",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reactive High-Speed Flight",
      "resolved_canonical": "Reactive High-Speed Flight",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# HUNT: High-Speed UAV Navigation and Tracking in Unstructured Environments via Instantaneous Relative Frames

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19452.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19452](https://arxiv.org/abs/2509.19452)

## 🔗 유사한 논문
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (82.4% similar)
- [[2025-09-23/SWA-PF_ Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments_20250923|SWA-PF: Semantic-Weighted Adaptive Particle Filter for Memory-Efficient 4-DoF UAV Localization in GNSS-Denied Environments]] (81.8% similar)
- [[2025-09-19/Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors_20250919|Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors]] (81.0% similar)
- [[2025-09-18/Reinforcement Learning for Autonomous Point-to-Point UAV Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (80.9% similar)
- [[2025-09-23/A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments_20250923|A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Search and Rescue Operations|Search and Rescue Operations]]
**⚡ Unique Technical**: [[keywords/UAV Navigation|UAV Navigation]], [[keywords/Relative Navigation|Relative Navigation]], [[keywords/Reactive High-Speed Flight|Reactive High-Speed Flight]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19452v1 Announce Type: cross 
Abstract: Search and rescue operations require unmanned aerial vehicles to both traverse unknown unstructured environments at high speed and track targets once detected. Achieving both capabilities under degraded sensing and without global localization remains an open challenge. Recent works on relative navigation have shown robust tracking by anchoring planning and control to a visible detected object, but cannot address navigation when no target is in the field of view. We present HUNT (High-speed UAV Navigation and Tracking), a real-time framework that unifies traversal, acquisition, and tracking within a single relative formulation. HUNT defines navigation objectives directly from onboard instantaneous observables such as attitude, altitude, and velocity, enabling reactive high-speed flight during search. Once a target is detected, the same perception-control pipeline transitions seamlessly to tracking. Outdoor experiments in dense forests, container compounds, and search-and-rescue operations with vehicles and mannequins demonstrate robust autonomy where global methods fail.

## 📝 요약

이 논문은 탐색 및 구조 작업에서 무인 항공기(UAV)가 고속으로 미지의 환경을 탐색하고 목표물을 추적하는 문제를 다룹니다. 기존의 상대 내비게이션 연구는 목표물이 시야에 있을 때는 효과적이지만, 목표물이 보이지 않을 때는 한계가 있습니다. 이를 해결하기 위해 HUNT라는 실시간 프레임워크를 제안합니다. HUNT는 기체의 자세, 고도, 속도와 같은 즉각적인 관측값을 기반으로 내비게이션 목표를 설정하여 탐색 중에도 반응적인 고속 비행을 가능하게 합니다. 목표물이 감지되면 동일한 인식-제어 파이프라인이 추적 모드로 전환됩니다. 이 방법은 밀집된 숲, 컨테이너 구역, 구조 작업 등에서의 실험을 통해 전 지구적 방법이 실패하는 상황에서도 강력한 자율성을 입증했습니다.

## 🎯 주요 포인트

- 1. HUNT는 고속 무인 항공기 탐색 및 추적을 위한 실시간 프레임워크로, 탐색, 획득, 추적을 단일 상대적 공식으로 통합합니다.
- 2. 이 프레임워크는 자세, 고도, 속도와 같은 기내 즉각적 관측치를 기반으로 탐색 목표를 정의하여 탐색 중 반응적인 고속 비행을 가능하게 합니다.
- 3. 목표물이 감지되면 동일한 인식-제어 파이프라인이 원활하게 추적으로 전환됩니다.
- 4. 밀집된 숲, 컨테이너 단지, 차량 및 마네킹을 활용한 수색 및 구조 작업에서 HUNT는 글로벌 방법이 실패하는 상황에서도 견고한 자율성을 입증했습니다.
- 5. 기존의 상대적 내비게이션 연구는 탐지된 객체에 계획 및 제어를 고정하여 견고한 추적을 보여주었으나, 시야에 목표가 없을 때의 내비게이션 문제는 해결하지 못했습니다.


---

*Generated on 2025-09-25 16:54:00*