---
keywords:
  - Automatic Speech Recognition
  - Video-Guided Post-ASR Correction
  - Video-Large Multimodal Model
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.07323
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:06:14.120591",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automatic Speech Recognition",
    "Video-Guided Post-ASR Correction",
    "Video-Large Multimodal Model",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automatic Speech Recognition": 0.78,
    "Video-Guided Post-ASR Correction": 0.8,
    "Video-Large Multimodal Model": 0.77,
    "Multimodal Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Automatic Speech Recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is a foundational technology in the paper, connecting to broader fields like Natural Language Processing and Machine Learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Video-Guided Post-ASR Correction",
        "canonical": "Video-Guided Post-ASR Correction",
        "aliases": [
          "VPC"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for linking specific advancements in ASR technology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Video-Large Multimodal Model",
        "canonical": "Video-Large Multimodal Model",
        "aliases": [
          "VLMM"
        ],
        "category": "unique_technical",
        "rationale": "The VLMM is a key component of the proposed framework, linking video context with ASR outputs.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is essential for understanding the integration of video and audio data in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "complex environments",
      "transcription accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Automatic Speech Recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Video-Guided Post-ASR Correction",
      "resolved_canonical": "Video-Guided Post-ASR Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Video-Large Multimodal Model",
      "resolved_canonical": "Video-Large Multimodal Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Speech Recognition on TV Series with Video-guided Post-ASR Correction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.07323.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.07323](https://arxiv.org/abs/2506.07323)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (82.0% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech]] (82.0% similar)
- [[2025-09-23/KRAST_ Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models_20250923|KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models]] (82.0% similar)
- [[2025-09-18/Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (81.7% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Video-Guided Post-ASR Correction|Video-Guided Post-ASR Correction]], [[keywords/Video-Large Multimodal Model|Video-Large Multimodal Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.07323v2 Announce Type: replace-cross 
Abstract: Automatic Speech Recognition (ASR) has achieved remarkable success with deep learning, driving advancements in conversational artificial intelligence, media transcription, and assistive technologies. However, ASR systems still struggle in complex environments such as TV series, where multiple speakers, overlapping speech, domain-specific terminology, and long-range contextual dependencies pose significant challenges to transcription accuracy. Existing approaches fail to explicitly leverage the rich temporal and contextual information available in the video. To address this limitation, we propose a Video-Guided Post-ASR Correction (VPC) framework that uses a Video-Large Multimodal Model (VLMM) to capture video context and refine ASR outputs. Evaluations on a TV-series benchmark show that our method consistently improves transcription accuracy in complex multimedia environments.

## 📝 요약

이 논문은 복잡한 환경에서의 자동 음성 인식(ASR) 문제를 해결하기 위해 비디오 가이드 후처리 보정(VPC) 프레임워크를 제안합니다. 기존 ASR 시스템은 TV 시리즈와 같은 복잡한 환경에서 여러 화자, 중첩된 음성, 특정 용어, 장기 문맥 의존성으로 인해 정확도가 떨어집니다. 제안된 VPC는 비디오-대형 멀티모달 모델(VLMM)을 활용하여 비디오 문맥을 포착하고 ASR 출력을 개선합니다. TV 시리즈 벤치마크 평가 결과, 이 방법이 복잡한 멀티미디어 환경에서 일관되게 전사 정확도를 향상시킴을 보여줍니다.

## 🎯 주요 포인트

- 1. 자동 음성 인식(ASR)은 심층 학습을 통해 대화형 인공지능, 미디어 전사, 보조 기술 분야에서 큰 성공을 거두었다.
- 2. ASR 시스템은 TV 시리즈와 같은 복잡한 환경에서 여러 화자, 중첩된 음성, 도메인 특화 용어, 장기 문맥 의존성으로 인해 전사 정확도에 어려움을 겪고 있다.
- 3. 기존 접근법은 비디오에서 얻을 수 있는 풍부한 시간적, 문맥적 정보를 명시적으로 활용하지 못한다.
- 4. 제안된 Video-Guided Post-ASR Correction (VPC) 프레임워크는 Video-Large Multimodal Model (VLMM)을 사용하여 비디오 문맥을 포착하고 ASR 출력을 개선한다.
- 5. TV 시리즈 벤치마크 평가에서 제안된 방법은 복잡한 멀티미디어 환경에서 전사 정확도를 지속적으로 향상시킨다.


---

*Generated on 2025-09-24 01:06:14*