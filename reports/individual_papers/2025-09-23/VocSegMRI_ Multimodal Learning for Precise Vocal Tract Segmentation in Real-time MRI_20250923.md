---
keywords:
  - Multimodal Learning
  - Attention Mechanism
  - Self-supervised Learning
  - Vocal Tract Segmentation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.13767
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:32:00.193901",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Attention Mechanism",
    "Self-supervised Learning",
    "Vocal Tract Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Attention Mechanism": 0.82,
    "Self-supervised Learning": 0.79,
    "Vocal Tract Segmentation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal framework",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal integration"
        ],
        "category": "specific_connectable",
        "rationale": "Links to recent advancements in integrating multiple data types for enhanced learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-attention fusion",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Cross-attention"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to attention-based models which are central to modern neural network architectures.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Contrastive learning objective",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive learning"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a key technique in self-supervised learning that enhances model robustness.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Vocal tract segmentation",
        "canonical": "Vocal Tract Segmentation",
        "aliases": [
          "Articulatory structure segmentation"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the domain of speech and MRI analysis, offering unique insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
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
      "candidate_surface": "Multimodal framework",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cross-attention fusion",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Contrastive learning objective",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Vocal tract segmentation",
      "resolved_canonical": "Vocal Tract Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13767.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.13767](https://arxiv.org/abs/2509.13767)

## 🔗 유사한 논문
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (86.2% similar)
- [[2025-09-23/Multimodal Medical Image Classification via Synergistic Learning Pre-training_20250923|Multimodal Medical Image Classification via Synergistic Learning Pre-training]] (84.8% similar)
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (82.8% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (82.7% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Vocal Tract Segmentation|Vocal Tract Segmentation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13767v2 Announce Type: replace 
Abstract: Accurately segmenting articulatory structures in real-time magnetic resonance imaging (rtMRI) remains challenging, as most existing methods rely almost entirely on visual cues. Yet synchronized acoustic and phonological signals provide complementary context that can enrich visual information and improve precision. In this paper, we introduce VocSegMRI, a multimodal framework that integrates video, audio, and phonological inputs through cross-attention fusion for dynamic feature alignment. To further enhance cross-modal representation, we incorporate a contrastive learning objective that improves segmentation performance even when the audio modality is unavailable at inference. Evaluated on a sub-set of USC-75 rtMRI dataset, our approach achieves state-of-the-art performance, with a Dice score of 0.95 and a 95th percentile Hausdorff Distance (HD_95) of 4.20 mm, outperforming both unimodal and multimodal baselines. Ablation studies confirm the contributions of cross-attention and contrastive learning to segmentation precision and robustness. These results highlight the value of integrative multimodal modeling for accurate vocal tract analysis.

## 📝 요약

이 논문에서는 실시간 자기공명영상(rtMRI)에서 조음 구조를 정확히 분할하기 위한 새로운 다중 모달 프레임워크인 VocSegMRI를 제안합니다. 이 방법은 비디오, 오디오, 음운 입력을 교차 주의 융합을 통해 통합하여 동적 특징 정렬을 수행합니다. 또한, 대조 학습 목표를 도입하여 오디오 모달리티가 없는 경우에도 분할 성능을 향상시킵니다. USC-75 rtMRI 데이터셋의 일부를 사용한 평가에서 Dice 점수 0.95와 95번째 백분위수 하우스도르프 거리(HD_95) 4.20 mm를 기록하며 기존 방법들을 능가했습니다. 연구 결과는 교차 주의와 대조 학습이 분할의 정밀성과 견고성에 기여함을 확인하며, 정확한 성대 분석을 위한 통합적 다중 모달 모델링의 가치를 강조합니다.

## 🎯 주요 포인트

- 1. VocSegMRI는 비디오, 오디오, 음운 입력을 통합하여 교차 주의 융합을 통해 동적 특징 정렬을 수행하는 다중 모달 프레임워크입니다.
- 2. 대조 학습 목표를 도입하여 오디오 모달리티가 불가능한 경우에도 분할 성능을 향상시킵니다.
- 3. USC-75 rtMRI 데이터셋의 하위 집합에서 평가한 결과, Dice 점수 0.95와 HD_95 4.20 mm로 최첨단 성능을 달성했습니다.
- 4. 교차 주의와 대조 학습이 분할 정밀도와 강건성에 기여함을 입증하는 소거 연구가 수행되었습니다.
- 5. 통합적 다중 모달 모델링이 정확한 발성 기관 분석에 가치가 있음을 강조합니다.


---

*Generated on 2025-09-24 05:32:00*