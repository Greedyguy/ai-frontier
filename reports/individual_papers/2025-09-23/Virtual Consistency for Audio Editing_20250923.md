---
keywords:
  - Audio Editing
  - Diffusion Models
  - Neural Editing
  - Virtual Consistency
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17219
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:20:46.468594",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio Editing",
    "Diffusion Models",
    "Neural Editing",
    "Virtual Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Audio Editing": 0.75,
    "Diffusion Models": 0.8,
    "Neural Editing": 0.7,
    "Virtual Consistency": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "audio editing",
        "canonical": "Audio Editing",
        "aliases": [
          "sound editing",
          "audio manipulation"
        ],
        "category": "unique_technical",
        "rationale": "Audio Editing is central to the paper's contribution and offers unique insights into the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion processes"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion Models are a key component of the proposed system, linking to broader machine learning concepts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "neural editing",
        "canonical": "Neural Editing",
        "aliases": [
          "neural-based editing"
        ],
        "category": "unique_technical",
        "rationale": "Neural Editing is a distinct approach discussed in the paper, relevant for linking to neural network applications.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "virtual consistency",
        "canonical": "Virtual Consistency",
        "aliases": [
          "virtual coherence"
        ],
        "category": "unique_technical",
        "rationale": "Virtual Consistency is a novel concept introduced by the authors, crucial for understanding their method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "inversion procedures",
      "sampling process",
      "user study"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "audio editing",
      "resolved_canonical": "Audio Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "neural editing",
      "resolved_canonical": "Neural Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "virtual consistency",
      "resolved_canonical": "Virtual Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Virtual Consistency for Audio Editing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17219.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17219](https://arxiv.org/abs/2509.17219)

## 🔗 유사한 논문
- [[2025-09-17/RFM-Editing_ Rectified Flow Matching for Text-guided Audio Editing_20250917|RFM-Editing: Rectified Flow Matching for Text-guided Audio Editing]] (87.4% similar)
- [[2025-09-19/Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (81.1% similar)
- [[2025-09-23/Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation_20250923|Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation]] (80.8% similar)
- [[2025-09-23/Audio Contrastive-based Fine-tuning_ Decoupling Representation Learning and Classification_20250923|Audio Contrastive-based Fine-tuning: Decoupling Representation Learning and Classification]] (80.5% similar)
- [[2025-09-23/Prompt-Driven Agentic Video Editing System_ Autonomous Comprehension of Long-Form, Story-Driven Media_20250923|Prompt-Driven Agentic Video Editing System: Autonomous Comprehension of Long-Form, Story-Driven Media]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]]
**⚡ Unique Technical**: [[keywords/Audio Editing|Audio Editing]], [[keywords/Neural Editing|Neural Editing]], [[keywords/Virtual Consistency|Virtual Consistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17219v1 Announce Type: cross 
Abstract: Free-form, text-based audio editing remains a persistent challenge, despite progress in inversion-based neural methods. Current approaches rely on slow inversion procedures, limiting their practicality. We present a virtual-consistency based audio editing system that bypasses inversion by adapting the sampling process of diffusion models. Our pipeline is model-agnostic, requiring no fine-tuning or architectural changes, and achieves substantial speed-ups over recent neural editing baselines. Crucially, it achieves this efficiency without compromising quality, as demonstrated by quantitative benchmarks and a user study involving 16 participants.

## 📝 요약

이 논문은 자유형 텍스트 기반 오디오 편집의 효율성을 개선한 연구를 다룹니다. 기존 방법들은 느린 역변환 절차에 의존하여 실용성이 떨어졌습니다. 본 연구에서는 역변환을 우회하고 확산 모델의 샘플링 과정을 조정하는 가상 일관성 기반 오디오 편집 시스템을 제안합니다. 이 시스템은 모델에 구애받지 않으며, 미세 조정이나 구조적 변경 없이도 최근의 신경망 편집 기준보다 속도가 크게 향상됩니다. 중요한 점은, 이러한 효율성을 품질 저하 없이 달성했다는 것이며, 이는 정량적 벤치마크와 16명의 참가자를 대상으로 한 사용자 연구를 통해 입증되었습니다.

## 🎯 주요 포인트

- 1. 본 연구는 자유형 텍스트 기반 오디오 편집의 어려움을 해결하기 위해 가상 일관성 기반 오디오 편집 시스템을 제안합니다.
- 2. 제안된 시스템은 확산 모델의 샘플링 과정을 조정하여 역변환을 우회하며, 이는 기존의 느린 역변환 절차를 대체합니다.
- 3. 이 파이프라인은 모델에 구애받지 않으며, 미세 조정이나 구조적 변경 없이도 최근 신경망 편집 기준보다 상당히 빠른 속도를 달성합니다.
- 4. 제안된 방법은 효율성을 높이면서도 품질을 저하시키지 않으며, 이는 정량적 벤치마크와 16명의 참가자를 대상으로 한 사용자 연구를 통해 입증되었습니다.


---

*Generated on 2025-09-24 02:20:46*