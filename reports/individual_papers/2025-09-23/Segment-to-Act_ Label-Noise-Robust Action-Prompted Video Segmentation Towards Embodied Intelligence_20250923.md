---
keywords:
  - Action-Based Video Object Segmentation
  - Label Noise
  - Parallel Mask Head Mechanism
  - Multimodal Noise
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16677
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:12:47.539549",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Action-Based Video Object Segmentation",
    "Label Noise",
    "Parallel Mask Head Mechanism",
    "Multimodal Noise"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Action-Based Video Object Segmentation": 0.8,
    "Label Noise": 0.72,
    "Parallel Mask Head Mechanism": 0.77,
    "Multimodal Noise": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "action-based video object segmentation",
        "canonical": "Action-Based Video Object Segmentation",
        "aliases": [
          "action-prompted video segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper, linking video segmentation with action semantics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "label noise",
        "canonical": "Label Noise",
        "aliases": [
          "annotation noise"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding label noise is crucial for improving machine learning models, especially in noisy environments.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Parallel Mask Head Mechanism",
        "canonical": "Parallel Mask Head Mechanism",
        "aliases": [
          "PMHM"
        ],
        "category": "unique_technical",
        "rationale": "This mechanism is a novel contribution of the paper, addressing mask annotation noise.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "multimodal noise",
        "canonical": "Multimodal Noise",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Multimodal noise is a growing concern in video analysis, impacting the accuracy of segmentation tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "failure modes"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "action-based video object segmentation",
      "resolved_canonical": "Action-Based Video Object Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "label noise",
      "resolved_canonical": "Label Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Parallel Mask Head Mechanism",
      "resolved_canonical": "Parallel Mask Head Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "multimodal noise",
      "resolved_canonical": "Multimodal Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Segment-to-Act: Label-Noise-Robust Action-Prompted Video Segmentation Towards Embodied Intelligence

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16677.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16677](https://arxiv.org/abs/2509.16677)

## 🔗 유사한 논문
- [[2025-09-23/MaskedManipulator_ Versatile Whole-Body Manipulation_20250923|MaskedManipulator: Versatile Whole-Body Manipulation]] (81.6% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (81.5% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (81.1% similar)
- [[2025-09-23/VideoArtGS_ Building Digital Twins of Articulated Objects from Monocular Video_20250923|VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video]] (80.6% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Label Noise|Label Noise]]
**⚡ Unique Technical**: [[keywords/Action-Based Video Object Segmentation|Action-Based Video Object Segmentation]], [[keywords/Parallel Mask Head Mechanism|Parallel Mask Head Mechanism]]
**🚀 Evolved Concepts**: [[keywords/Multimodal Noise|Multimodal Noise]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16677v1 Announce Type: cross 
Abstract: Embodied intelligence relies on accurately segmenting objects actively involved in interactions. Action-based video object segmentation addresses this by linking segmentation with action semantics, but it depends on large-scale annotations and prompts that are costly, inconsistent, and prone to multimodal noise such as imprecise masks and referential ambiguity. To date, this challenge remains unexplored. In this work, we take the first step by studying action-based video object segmentation under label noise, focusing on two sources: textual prompt noise (category flips and within-category noun substitutions) and mask annotation noise (perturbed object boundaries to mimic imprecise supervision). Our contributions are threefold. First, we introduce two types of label noises for the action-based video object segmentation task. Second, we build up the first action-based video object segmentation under a label noise benchmark ActiSeg-NL and adapt six label-noise learning strategies to this setting, and establish protocols for evaluating them under textual, boundary, and mixed noise. Third, we provide a comprehensive analysis linking noise types to failure modes and robustness gains, and we introduce a Parallel Mask Head Mechanism (PMHM) to address mask annotation noise. Qualitative evaluations further reveal characteristic failure modes, including boundary leakage and mislocalization under boundary perturbations, as well as occasional identity substitutions under textual flips. Our comparative analysis reveals that different learning strategies exhibit distinct robustness profiles, governed by a foreground-background trade-off where some achieve balanced performance while others prioritize foreground accuracy at the cost of background precision. The established benchmark and source code will be made publicly available at https://github.com/mylwx/ActiSeg-NL.

## 📝 요약

이 논문은 상호작용에 관여하는 객체를 정확히 분할하는 것이 중요한 체화된 지능에서, 행동 기반 비디오 객체 분할의 레이블 노이즈 문제를 처음으로 탐구합니다. 주요 기여는 세 가지입니다. 첫째, 행동 기반 비디오 객체 분할 작업에서 두 가지 유형의 레이블 노이즈를 도입했습니다. 둘째, 레이블 노이즈 벤치마크 ActiSeg-NL을 구축하고 여섯 가지 학습 전략을 적용하여 텍스트, 경계, 혼합 노이즈 하에서 평가 프로토콜을 확립했습니다. 셋째, 노이즈 유형과 실패 모드 및 강건성 향상을 연결하는 포괄적인 분석을 제공하고, 마스크 주석 노이즈를 해결하기 위한 병렬 마스크 헤드 메커니즘(PMHM)을 제안했습니다. 이 연구는 다양한 학습 전략이 서로 다른 강건성 프로파일을 보이며, 전경-배경 균형에 따라 성능이 달라짐을 보여줍니다. 연구 결과와 소스 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 행동 기반 비디오 객체 분할에서 레이블 노이즈를 다루기 위해 두 가지 유형의 레이블 노이즈를 도입했습니다.
- 2. 레이블 노이즈가 있는 행동 기반 비디오 객체 분할 벤치마크 ActiSeg-NL을 구축하고, 여섯 가지 레이블 노이즈 학습 전략을 적용하여 평가 프로토콜을 설정했습니다.
- 3. 노이즈 유형과 실패 모드 및 강건성 향상을 연결하는 포괄적인 분석을 제공하고, 마스크 주석 노이즈를 해결하기 위한 병렬 마스크 헤드 메커니즘(PMHM)을 소개했습니다.
- 4. 경계 누출 및 경계 교란 하에서의 위치 오차와 같은 특성적 실패 모드를 정성적으로 평가했습니다.
- 5. 다양한 학습 전략이 서로 다른 강건성 프로파일을 보여주며, 일부는 전경 정확도를 우선시하는 반면 다른 일부는 균형 잡힌 성능을 달성합니다.


---

*Generated on 2025-09-24 02:12:47*