---
keywords:
  - Zero-Shot Learning
  - Terrain-aware Adapter
  - Temporal Prompt Generator
  - Multi-scale Fusion Strategy
  - Remote Sensing Segmentation
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15795
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:11:29.383341",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Terrain-aware Adapter",
    "Temporal Prompt Generator",
    "Multi-scale Fusion Strategy",
    "Remote Sensing Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Terrain-aware Adapter": 0.72,
    "Temporal Prompt Generator": 0.7,
    "Multi-scale Fusion Strategy": 0.71,
    "Remote Sensing Segmentation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Segment Anything Model",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "SAM"
        ],
        "category": "specific_connectable",
        "rationale": "SAM's zero-shot capabilities align with the concept of Zero-Shot Learning, enhancing connectivity to similar models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Terrain-aware Adapter",
        "canonical": "Terrain-aware Adapter",
        "aliases": [
          "Elevation Priors Module"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for integrating elevation data into segmentation, which is unique to this model.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Temporal Prompt Generator",
        "canonical": "Temporal Prompt Generator",
        "aliases": [
          "Time-aware Module"
        ],
        "category": "unique_technical",
        "rationale": "Captures temporal dynamics in remote sensing, offering a novel perspective for time-based data analysis.",
        "novelty_score": 0.81,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multi-scale Fusion Strategy",
        "canonical": "Multi-scale Fusion Strategy",
        "aliases": [
          "Scale Integration Method"
        ],
        "category": "unique_technical",
        "rationale": "Enhances object delineation by integrating multiple scales, which is crucial for remote sensing applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.71
      },
      {
        "surface": "Remote Sensing Segmentation",
        "canonical": "Remote Sensing Segmentation",
        "aliases": [
          "Geospatial Segmentation"
        ],
        "category": "broad_technical",
        "rationale": "A core domain of the study, linking to broader geospatial and remote sensing research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "high-resolution",
      "performance gains",
      "computational overhead"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Segment Anything Model",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Terrain-aware Adapter",
      "resolved_canonical": "Terrain-aware Adapter",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Temporal Prompt Generator",
      "resolved_canonical": "Temporal Prompt Generator",
      "decision": "linked",
      "scores": {
        "novelty": 0.81,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multi-scale Fusion Strategy",
      "resolved_canonical": "Multi-scale Fusion Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "Remote Sensing Segmentation",
      "resolved_canonical": "Remote Sensing Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation

**Korean Title:** TASAM: 시간 규모 원격 감지 분할을 위한 지형 인식 세그먼트 모델

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15795.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15795](https://arxiv.org/abs/2509.15795)

## 🔗 유사한 논문
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (83.7% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (83.3% similar)
- [[2025-09-22/RangeSAM_ Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation_20250922|RangeSAM: Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation]] (82.5% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (82.3% similar)
- [[2025-09-22/FloorSAM_ SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion_20250922|FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Remote Sensing Segmentation|Remote Sensing Segmentation]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Terrain-aware Adapter|Terrain-aware Adapter]], [[keywords/Temporal Prompt Generator|Temporal Prompt Generator]], [[keywords/Multi-scale Fusion Strategy|Multi-scale Fusion Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15795v1 Announce Type: new 
Abstract: Segment Anything Model (SAM) has demonstrated impressive zero-shot segmentation capabilities across natural image domains, but it struggles to generalize to the unique challenges of remote sensing data, such as complex terrain, multi-scale objects, and temporal dynamics. In this paper, we introduce TASAM, a terrain and temporally-aware extension of SAM designed specifically for high-resolution remote sensing image segmentation. TASAM integrates three lightweight yet effective modules: a terrain-aware adapter that injects elevation priors, a temporal prompt generator that captures land-cover changes over time, and a multi-scale fusion strategy that enhances fine-grained object delineation. Without retraining the SAM backbone, our approach achieves substantial performance gains across three remote sensing benchmarks-LoveDA, iSAID, and WHU-CD-outperforming both zero-shot SAM and task-specific models with minimal computational overhead. Our results highlight the value of domain-adaptive augmentation for foundation models and offer a scalable path toward more robust geospatial segmentation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15795v1 발표 유형: 신규  
초록: Segment Anything Model (SAM)은 자연 이미지 도메인에서 인상적인 제로샷 분할 능력을 보여주었지만, 복잡한 지형, 다중 규모의 객체, 시간적 역학과 같은 원격 감지 데이터의 고유한 문제에 일반화하는 데 어려움을 겪고 있습니다. 본 논문에서는 고해상도 원격 감지 이미지 분할을 위해 특별히 설계된 SAM의 지형 및 시간 인식 확장판인 TASAM을 소개합니다. TASAM은 경량이면서도 효과적인 세 가지 모듈을 통합합니다: 고도 사전 정보를 주입하는 지형 인식 어댑터, 시간에 따른 토지 피복 변화를 포착하는 시간적 프롬프트 생성기, 세밀한 객체 경계를 향상시키는 다중 규모 융합 전략입니다. SAM 백본을 재훈련하지 않고도, 우리의 접근 방식은 LoveDA, iSAID, WHU-CD의 세 가지 원격 감지 벤치마크에서 상당한 성능 향상을 달성하며, 제로샷 SAM과 작업별 모델 모두를 최소한의 계산 오버헤드로 능가합니다. 우리의 결과는 기초 모델에 대한 도메인 적응 증강의 가치를 강조하며, 보다 견고한 지리공간 분할을 위한 확장 가능한 경로를 제공합니다.

## 📝 요약

Segment Anything Model (SAM)은 자연 이미지에서 뛰어난 제로샷 분할 능력을 보였으나, 원격 탐사 데이터의 복잡한 지형, 다중 규모 객체, 시간적 변화에 대한 일반화에는 한계가 있습니다. 본 논문에서는 이러한 문제를 해결하기 위해 고해상도 원격 탐사 이미지 분할에 특화된 TASAM을 제안합니다. TASAM은 지형 정보를 반영하는 어댑터, 시간에 따른 지표 변화 포착을 위한 프롬프트 생성기, 다중 규모 융합 전략을 통합하여 세밀한 객체 구분을 강화합니다. SAM 백본을 재훈련하지 않고도 LoveDA, iSAID, WHU-CD의 세 가지 원격 탐사 벤치마크에서 성능을 크게 향상시켰으며, 제로샷 SAM과 특정 작업 모델을 능가하는 결과를 보였습니다. 이는 기초 모델의 도메인 적응적 증강의 가치를 입증하며, 더 견고한 지리 공간 분할로 나아가는 확장 가능한 경로를 제시합니다.

## 🎯 주요 포인트

- 1. Segment Anything Model (SAM)은 자연 이미지 도메인에서 뛰어난 제로샷 세분화 능력을 보였으나, 원격 탐사 데이터의 복잡한 지형, 다중 규모 객체, 시간적 동적 특성에는 일반화하기 어렵다.
- 2. TASAM은 SAM을 고해상도 원격 탐사 이미지 세분화를 위해 지형 및 시간 인식 확장으로 설계된 모델로, 지형 인식 어댑터, 시간적 프롬프트 생성기, 다중 규모 융합 전략을 통합한다.
- 3. TASAM은 SAM 백본을 재훈련하지 않고도 LoveDA, iSAID, WHU-CD의 세 가지 원격 탐사 벤치마크에서 성능을 크게 향상시켰다.
- 4. TASAM은 제로샷 SAM 및 특정 작업 모델을 능가하며, 최소한의 계산 오버헤드로 성능을 발휘한다.
- 5. 본 연구는 기초 모델에 대한 도메인 적응형 증강의 가치를 강조하며, 보다 강력한 지리 공간 세분화를 위한 확장 가능한 경로를 제시한다.


---

*Generated on 2025-09-23 12:11:29*