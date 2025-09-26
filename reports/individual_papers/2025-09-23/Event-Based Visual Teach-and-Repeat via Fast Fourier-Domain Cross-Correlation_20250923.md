---
keywords:
  - Event-Based Visual Navigation
  - Frequency-Domain Cross-Correlation
  - Prophesee Event Camera
  - AgileX Scout Mini
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17287
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:12:08.612830",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Event-Based Visual Navigation",
    "Frequency-Domain Cross-Correlation",
    "Prophesee Event Camera",
    "AgileX Scout Mini"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Event-Based Visual Navigation": 0.79,
    "Frequency-Domain Cross-Correlation": 0.75,
    "Prophesee Event Camera": 0.72,
    "AgileX Scout Mini": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "event-camera-based visual teach-and-repeat system",
        "canonical": "Event-Based Visual Navigation",
        "aliases": [
          "event-camera navigation",
          "event-based teach-and-repeat"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach to robotic navigation that leverages event cameras, which is a significant advancement over traditional methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "frequency-domain cross-correlation framework",
        "canonical": "Frequency-Domain Cross-Correlation",
        "aliases": [
          "Fourier-domain cross-correlation"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a core technical innovation that enhances processing speed, crucial for linking with computational efficiency topics.",
        "novelty_score": 0.78,
        "connectivity_score": 0.69,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Prophesee EVK4 HD event camera",
        "canonical": "Prophesee Event Camera",
        "aliases": [
          "EVK4 HD camera"
        ],
        "category": "specific_connectable",
        "rationale": "The use of this specific camera model is central to the system's performance, linking it to hardware-specific discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "AgileX Scout Mini robot",
        "canonical": "AgileX Scout Mini",
        "aliases": [
          "Scout Mini robot"
        ],
        "category": "specific_connectable",
        "rationale": "This robot model is integral to the experimental setup, providing a link to discussions on mobile robotics platforms.",
        "novelty_score": 0.6,
        "connectivity_score": 0.74,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "system",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "event-camera-based visual teach-and-repeat system",
      "resolved_canonical": "Event-Based Visual Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "frequency-domain cross-correlation framework",
      "resolved_canonical": "Frequency-Domain Cross-Correlation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.69,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Prophesee EVK4 HD event camera",
      "resolved_canonical": "Prophesee Event Camera",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "AgileX Scout Mini robot",
      "resolved_canonical": "AgileX Scout Mini",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.74,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Event-Based Visual Teach-and-Repeat via Fast Fourier-Domain Cross-Correlation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17287.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17287](https://arxiv.org/abs/2509.17287)

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (81.7% similar)
- [[2025-09-23/Leveraging RGB Images for Pre-Training of Event-Based Hand Pose Estimation_20250923|Leveraging RGB Images for Pre-Training of Event-Based Hand Pose Estimation]] (81.1% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (81.1% similar)
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (79.9% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Prophesee Event Camera|Prophesee Event Camera]], [[keywords/AgileX Scout Mini|AgileX Scout Mini]]
**⚡ Unique Technical**: [[keywords/Event-Based Visual Navigation|Event-Based Visual Navigation]], [[keywords/Frequency-Domain Cross-Correlation|Frequency-Domain Cross-Correlation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17287v1 Announce Type: cross 
Abstract: Visual teach-and-repeat navigation enables robots to autonomously traverse previously demonstrated paths by comparing current sensory input with recorded trajectories. However, conventional frame-based cameras fundamentally limit system responsiveness: their fixed frame rates (typically 30-60 Hz) create inherent latency between environmental changes and control responses. Here we present the first event-camera-based visual teach-and-repeat system. To achieve this, we develop a frequency-domain cross-correlation framework that transforms the event stream matching problem into computationally efficient Fourier space multiplications, capable of exceeding 300Hz processing rates, an order of magnitude faster than frame-based approaches. By exploiting the binary nature of event frames and applying image compression techniques, we further enhance the computational speed of the cross-correlation process without sacrificing localization accuracy. Extensive experiments using a Prophesee EVK4 HD event camera mounted on an AgileX Scout Mini robot demonstrate successful autonomous navigation across 4000+ meters of indoor and outdoor trajectories. Our system achieves ATEs below 24 cm while maintaining consistent high-frequency control updates. Our evaluations show that our approach achieves substantially higher update rates compared to conventional frame-based systems, underscoring the practical viability of event-based perception for real-time robotic navigation.

## 📝 요약

이 논문은 이벤트 카메라를 활용한 최초의 비주얼 티치-앤-리피트(teach-and-repeat) 내비게이션 시스템을 제안합니다. 기존의 프레임 기반 카메라는 고정된 프레임 속도(30-60Hz)로 인해 환경 변화에 대한 반응 속도가 제한되지만, 본 연구에서는 이벤트 카메라를 사용하여 300Hz 이상의 처리 속도를 달성했습니다. 이를 위해 주파수 도메인 상호 상관 프레임워크를 개발하여 이벤트 스트림 매칭 문제를 효율적으로 해결하였고, 이미지 압축 기법을 적용하여 계산 속도를 더욱 향상시켰습니다. Prophesee EVK4 HD 이벤트 카메라와 AgileX Scout Mini 로봇을 사용한 실험에서, 실내외 4000m 이상의 경로를 성공적으로 자율 주행하며 평균 위치 오차(ATE)를 24cm 이하로 유지했습니다. 이 연구는 이벤트 기반 인식이 실시간 로봇 내비게이션에 실용적임을 입증합니다.

## 🎯 주요 포인트

- 1. 이벤트 카메라 기반의 비주얼 티치-앤-리피트 시스템을 최초로 개발하여 기존 프레임 기반 카메라의 한계를 극복했습니다.
- 2. 주파수 도메인 교차 상관 프레임워크를 통해 300Hz 이상의 처리 속도를 달성하여 프레임 기반 접근 방식보다 10배 빠른 성능을 구현했습니다.
- 3. 이진 이벤트 프레임과 이미지 압축 기술을 활용하여 위치 정확도를 유지하면서도 계산 속도를 향상시켰습니다.
- 4. Prophesee EVK4 HD 이벤트 카메라와 AgileX Scout Mini 로봇을 사용한 실험에서 4000m 이상의 경로를 성공적으로 자율 주행했습니다.
- 5. 제안된 시스템은 기존 프레임 기반 시스템보다 높은 업데이트 속도를 달성하여 실시간 로봇 내비게이션에서 이벤트 기반 인식의 실용성을 입증했습니다.


---

*Generated on 2025-09-24 05:12:08*