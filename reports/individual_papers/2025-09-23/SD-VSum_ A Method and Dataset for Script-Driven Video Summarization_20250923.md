---
keywords:
  - Script-Driven Video Summarization
  - Attention Mechanism
  - Multimodal Learning
  - VideoXum Dataset
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.03319
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:57:09.825899",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Script-Driven Video Summarization",
    "Attention Mechanism",
    "Multimodal Learning",
    "VideoXum Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Script-Driven Video Summarization": 0.92,
    "Attention Mechanism": 0.85,
    "Multimodal Learning": 0.88,
    "VideoXum Dataset": 0.91
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "script-driven video summarization",
        "canonical": "Script-Driven Video Summarization",
        "aliases": [
          "SD-VSum"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to video summarization that aligns with user-provided scripts, enhancing personalization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "cross-modal attention mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "cross-modal attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing concepts of attention mechanisms, highlighting its application in multimodal contexts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "multimodal summarization",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal video summarization"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of multimodal learning, emphasizing integration of visual and textual data.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "VideoXum",
        "canonical": "VideoXum Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific dataset extended for script-driven video summarization, crucial for dataset linking.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.91
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
      "candidate_surface": "script-driven video summarization",
      "resolved_canonical": "Script-Driven Video Summarization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "cross-modal attention mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multimodal summarization",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "VideoXum",
      "resolved_canonical": "VideoXum Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.91
      }
    }
  ]
}
-->

# SD-VSum: A Method and Dataset for Script-Driven Video Summarization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.03319.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.03319](https://arxiv.org/abs/2505.03319)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (82.6% similar)
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions]] (81.5% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (81.4% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (81.4% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Script-Driven Video Summarization|Script-Driven Video Summarization]], [[keywords/VideoXum Dataset|VideoXum Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.03319v2 Announce Type: replace-cross 
Abstract: In this work, we introduce the task of script-driven video summarization, which aims to produce a summary of the full-length video by selecting the parts that are most relevant to a user-provided script outlining the visual content of the desired summary. Following, we extend a recently-introduced large-scale dataset for generic video summarization (VideoXum) by producing natural language descriptions of the different human-annotated summaries that are available per video. In this way we make it compatible with the introduced task, since the available triplets of ``video, summary and summary description'' can be used for training a method that is able to produce different summaries for a given video, driven by the provided script about the content of each summary. Finally, we develop a new network architecture for script-driven video summarization (SD-VSum), that employs a cross-modal attention mechanism for aligning and fusing information from the visual and text modalities. Our experimental evaluations demonstrate the advanced performance of SD-VSum against SOTA approaches for query-driven and generic (unimodal and multimodal) summarization from the literature, and document its capacity to produce video summaries that are adapted to each user's needs about their content.

## 📝 요약

이 연구는 사용자 제공 스크립트를 기반으로 전체 비디오에서 관련 부분을 선택하여 요약하는 스크립트 기반 비디오 요약 작업을 소개합니다. 이를 위해, 기존의 대규모 비디오 요약 데이터셋(VideoXum)을 확장하여 각 비디오에 대한 인간 주석 요약의 자연어 설명을 추가했습니다. 이를 통해 비디오, 요약 및 요약 설명의 삼중항을 활용하여 주어진 스크립트에 따라 다양한 요약을 생성할 수 있는 방법을 훈련할 수 있습니다. 또한, 시각 및 텍스트 모달리티 정보를 정렬하고 융합하는 교차 모달 주의 메커니즘을 사용하는 새로운 네트워크 아키텍처(SD-VSum)를 개발했습니다. 실험 결과, SD-VSum은 기존의 쿼리 기반 및 일반 비디오 요약 방법들보다 우수한 성능을 보이며, 사용자 요구에 맞춘 비디오 요약을 생성할 수 있는 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 사용자 제공 스크립트를 기반으로 전체 비디오에서 가장 관련 있는 부분을 선택하여 요약을 생성하는 스크립트 기반 비디오 요약 작업을 소개합니다.
- 2. VideoXum이라는 대규모 데이터셋을 확장하여 각 비디오에 대해 사람에 의해 주석된 요약의 자연어 설명을 추가함으로써 새로운 작업과 호환되도록 합니다.
- 3. 스크립트 기반 비디오 요약을 위한 새로운 네트워크 아키텍처(SD-VSum)를 개발하였으며, 시각 및 텍스트 모달리티의 정보를 정렬하고 융합하기 위해 교차 모달 주의 메커니즘을 사용합니다.
- 4. 실험 결과, SD-VSum은 기존의 질의 기반 및 일반적인 요약 방법들에 비해 우수한 성능을 보이며, 사용자 요구에 맞춘 비디오 요약을 생성할 수 있는 능력을 입증합니다.


---

*Generated on 2025-09-24 00:57:09*