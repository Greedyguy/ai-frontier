---
keywords:
  - MirrorSAM2
  - RGB-D Video Mirror Segmentation
  - Depth Warping Module
  - Attention Mechanism
  - Mirror Mask Decoder
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17220
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:47:12.802017",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MirrorSAM2",
    "RGB-D Video Mirror Segmentation",
    "Depth Warping Module",
    "Attention Mechanism",
    "Mirror Mask Decoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MirrorSAM2": 0.8,
    "RGB-D Video Mirror Segmentation": 0.75,
    "Depth Warping Module": 0.7,
    "Attention Mechanism": 0.78,
    "Mirror Mask Decoder": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MirrorSAM2",
        "canonical": "MirrorSAM2",
        "aliases": [
          "Mirror SAM2"
        ],
        "category": "unique_technical",
        "rationale": "MirrorSAM2 is a novel framework specifically designed for RGB-D video mirror segmentation, making it a unique technical contribution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "RGB-D Video Mirror Segmentation",
        "canonical": "RGB-D Video Mirror Segmentation",
        "aliases": [
          "Video Mirror Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task that MirrorSAM2 addresses, linking it to the broader field of video processing and segmentation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Depth Warping Module",
        "canonical": "Depth Warping Module",
        "aliases": [
          "Depth Alignment Module"
        ],
        "category": "unique_technical",
        "rationale": "This module is a key innovation in MirrorSAM2, addressing the challenge of aligning RGB and depth data.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Frequency Detail Attention Fusion Module",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Frequency Detail Fusion"
        ],
        "category": "specific_connectable",
        "rationale": "This module enhances structural boundaries using attention mechanisms, linking it to the broader concept of attention in neural networks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mirror Mask Decoder",
        "canonical": "Mirror Mask Decoder",
        "aliases": [
          "Mask Decoder"
        ],
        "category": "unique_technical",
        "rationale": "The Mirror Mask Decoder is a specialized component for refined segmentation, crucial for the task addressed by MirrorSAM2.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "SAM2",
      "VMD",
      "DVMD"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MirrorSAM2",
      "resolved_canonical": "MirrorSAM2",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "RGB-D Video Mirror Segmentation",
      "resolved_canonical": "RGB-D Video Mirror Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Depth Warping Module",
      "resolved_canonical": "Depth Warping Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Frequency Detail Attention Fusion Module",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mirror Mask Decoder",
      "resolved_canonical": "Mirror Mask Decoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MirrorSAM2: Segment Mirror in Videos with Depth Perception

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17220.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17220](https://arxiv.org/abs/2509.17220)

## 🔗 유사한 논문
- [[2025-09-23/SAM-DCE_ Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation_20250923|SAM-DCE: Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation]] (84.5% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (83.3% similar)
- [[2025-09-23/BiPrompt-SAM_ Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts_20250923|BiPrompt-SAM: Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts]] (82.3% similar)
- [[2025-09-22/RangeSAM_ Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation_20250922|RangeSAM: Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation]] (81.6% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/MirrorSAM2|MirrorSAM2]], [[keywords/RGB-D Video Mirror Segmentation|RGB-D Video Mirror Segmentation]], [[keywords/Depth Warping Module|Depth Warping Module]], [[keywords/Mirror Mask Decoder|Mirror Mask Decoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17220v1 Announce Type: new 
Abstract: This paper presents MirrorSAM2, the first framework that adapts Segment Anything Model 2 (SAM2) to the task of RGB-D video mirror segmentation. MirrorSAM2 addresses key challenges in mirror detection, such as reflection ambiguity and texture confusion, by introducing four tailored modules: a Depth Warping Module for RGB and depth alignment, a Depth-guided Multi-Scale Point Prompt Generator for automatic prompt generation, a Frequency Detail Attention Fusion Module to enhance structural boundaries, and a Mirror Mask Decoder with a learnable mirror token for refined segmentation. By fully leveraging the complementarity between RGB and depth, MirrorSAM2 extends SAM2's capabilities to the prompt-free setting. To our knowledge, this is the first work to enable SAM2 for automatic video mirror segmentation. Experiments on the VMD and DVMD benchmark demonstrate that MirrorSAM2 achieves SOTA performance, even under challenging conditions such as small mirrors, weak boundaries, and strong reflections.

## 📝 요약

MirrorSAM2는 RGB-D 비디오에서 거울을 자동으로 분할하는 최초의 프레임워크로, Segment Anything Model 2 (SAM2)를 이 작업에 맞게 적응시켰습니다. 이 연구는 반사 모호성과 텍스처 혼동과 같은 거울 감지의 주요 문제를 해결하기 위해 네 가지 모듈을 도입했습니다: RGB와 깊이 정렬을 위한 깊이 왜곡 모듈, 자동 프롬프트 생성을 위한 깊이 기반 다중 스케일 포인트 프롬프트 생성기, 구조적 경계를 강화하는 주파수 세부 주의 융합 모듈, 그리고 세분화된 거울 마스크 디코더입니다. RGB와 깊이의 상호 보완성을 최대한 활용하여, MirrorSAM2는 SAM2의 기능을 프롬프트 없는 환경으로 확장합니다. 실험 결과, MirrorSAM2는 VMD와 DVMD 벤치마크에서 작은 거울, 약한 경계, 강한 반사와 같은 어려운 조건에서도 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. MirrorSAM2는 RGB-D 비디오에서의 거울 세분화를 위해 Segment Anything Model 2 (SAM2)를 최초로 적용한 프레임워크입니다.
- 2. 이 모델은 반사 모호성과 텍스처 혼란과 같은 거울 탐지의 주요 문제를 해결하기 위해 네 가지 맞춤형 모듈을 도입합니다.
- 3. RGB와 깊이 정렬을 위한 Depth Warping Module, 자동 프롬프트 생성을 위한 Depth-guided Multi-Scale Point Prompt Generator 등이 포함됩니다.
- 4. MirrorSAM2는 RGB와 깊이의 상보성을 최대한 활용하여 프롬프트 없는 설정에서도 SAM2의 기능을 확장합니다.
- 5. VMD 및 DVMD 벤치마크 실험에서 MirrorSAM2는 작은 거울, 약한 경계, 강한 반사와 같은 도전적인 조건에서도 SOTA 성능을 달성합니다.


---

*Generated on 2025-09-24 04:47:12*