<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:03:18.208851",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "XMem Memory Network",
    "Tumor Segmentation",
    "Real-Time MRI-Guided Radiotherapy",
    "TrackRAD2025 Challenge"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "XMem Memory Network": 0.78,
    "Tumor Segmentation": 0.8,
    "Real-Time MRI-Guided Radiotherapy": 0.77,
    "TrackRAD2025 Challenge": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "XMem Memory Network",
        "canonical": "XMem Memory Network",
        "aliases": [
          "XMem",
          "Memory-Augmented Architecture"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific architecture used in the paper, which is crucial for understanding the segmentation framework discussed.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "tumor segmentation",
        "canonical": "Tumor Segmentation",
        "aliases": [
          "tumor tracking",
          "segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area in the paper that connects to broader topics in medical imaging and radiotherapy.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "real-time MRI-guided radiotherapy",
        "canonical": "Real-Time MRI-Guided Radiotherapy",
        "aliases": [
          "MRI-guided radiotherapy",
          "real-time radiotherapy"
        ],
        "category": "unique_technical",
        "rationale": "A specific application context that is critical for understanding the clinical relevance of the research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "TrackRAD2025 challenge",
        "canonical": "TrackRAD2025 Challenge",
        "aliases": [
          "TrackRAD",
          "TrackRAD Challenge"
        ],
        "category": "unique_technical",
        "rationale": "A specific benchmark or challenge that provides context for the research's objectives and constraints.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "XMem Memory Network",
      "resolved_canonical": "XMem Memory Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "tumor segmentation",
      "resolved_canonical": "Tumor Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "real-time MRI-guided radiotherapy",
      "resolved_canonical": "Real-Time MRI-Guided Radiotherapy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "TrackRAD2025 challenge",
      "resolved_canonical": "TrackRAD2025 Challenge",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Enhancing Video Object Segmentation in TrackRAD Using XMem Memory Network

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18591.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18591](https://arxiv.org/abs/2509.18591)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (85.1% similar)
- [[2025-09-23/VocSegMRI_ Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI_20250923|VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (83.6% similar)
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (83.3% similar)
- [[2025-09-23/SmaRT_ Style-Modulated Robust Test-Time Adaptation for Cross-Domain Brain Tumor Segmentation in MRI_20250923|SmaRT: Style-Modulated Robust Test-Time Adaptation for Cross-Domain Brain Tumor Segmentation in MRI]] (83.1% similar)
- [[2025-09-24/CPT-4DMR_ Continuous sPatial-Temporal Representation for 4D-MRI Reconstruction_20250924|CPT-4DMR: Continuous sPatial-Temporal Representation for 4D-MRI Reconstruction]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Tumor Segmentation|Tumor Segmentation]]
**⚡ Unique Technical**: [[keywords/XMem Memory Network|XMem Memory Network]], [[keywords/Real-Time MRI-Guided Radiotherapy|Real-Time MRI-Guided Radiotherapy]], [[keywords/TrackRAD2025 Challenge|TrackRAD2025 Challenge]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18591v1 Announce Type: new 
Abstract: This paper presents an advanced tumor segmentation framework for real-time MRI-guided radiotherapy, designed for the TrackRAD2025 challenge. Our method leverages the XMem model, a memory-augmented architecture, to segment tumors across long cine-MRI sequences. The proposed system efficiently integrates memory mechanisms to track tumor motion in real-time, achieving high segmentation accuracy even under challenging conditions with limited annotated data. Unfortunately, the detailed experimental records have been lost, preventing us from reporting precise quantitative results at this stage. Nevertheless, From our preliminary impressions during development, the XMem-based framework demonstrated reasonable segmentation performance and satisfied the clinical real-time requirement. Our work contributes to improving the precision of tumor tracking during MRI-guided radiotherapy, which is crucial for enhancing the accuracy and safety of cancer treatments.

## 📝 요약

이 논문은 TrackRAD2025 챌린지를 위해 실시간 MRI 유도 방사선 치료에 적합한 고급 종양 분할 프레임워크를 제안합니다. XMem 모델을 활용하여 긴 cine-MRI 시퀀스에서 종양을 분할하며, 메모리 메커니즘을 통합해 실시간으로 종양 움직임을 추적합니다. 제한된 주석 데이터에서도 높은 분할 정확도를 달성했으며, 임상 실시간 요구 사항을 만족했습니다. 실험 기록이 유실되어 정량적 결과는 제공하지 못하지만, 이 연구는 MRI 유도 방사선 치료 중 종양 추적의 정밀성을 향상시켜 암 치료의 정확성과 안전성을 높이는 데 기여합니다.

## 🎯 주요 포인트

- 1. 본 논문은 실시간 MRI 유도 방사선 치료를 위한 고급 종양 분할 프레임워크를 제안합니다.
- 2. 제안된 시스템은 XMem 모델을 활용하여 긴 cine-MRI 시퀀스에서 종양을 분할하며, 메모리 메커니즘을 통합하여 실시간으로 종양 움직임을 추적합니다.
- 3. 제한된 주석 데이터에서도 높은 분할 정확도를 달성하며, 임상 실시간 요구사항을 충족합니다.
- 4. 실험 기록이 손실되어 정량적 결과를 보고할 수 없지만, 개발 중의 초기 인상에서는 합리적인 성능을 보였습니다.
- 5. 본 연구는 MRI 유도 방사선 치료 중 종양 추적의 정밀도를 향상시켜 암 치료의 정확성과 안전성을 높이는 데 기여합니다.


---

*Generated on 2025-09-24 16:03:18*