---
keywords:
  - ASR Correction Framework
  - Large Language Model
  - Finite State Machine
  - Phonetic Variants
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.15095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:32:40.644308",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ASR Correction Framework",
    "Large Language Model",
    "Finite State Machine",
    "Phonetic Variants"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ASR Correction Framework": 0.78,
    "Large Language Model": 0.82,
    "Finite State Machine": 0.75,
    "Phonetic Variants": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ASR Correction Framework",
        "canonical": "ASR Correction Framework",
        "aliases": [
          "Automatic Speech Recognition Correction"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper's contribution and offers a unique approach to ASR error correction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are integral to the framework's operation and connect to broader NLP research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Finite State Machine",
        "canonical": "Finite State Machine",
        "aliases": [
          "FSM"
        ],
        "category": "specific_connectable",
        "rationale": "FSMs are used for heuristic optimization, linking to computational models in NLP.",
        "novelty_score": 0.58,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Phonetic Variants",
        "canonical": "Phonetic Variants",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is crucial for the iterative correction strategy proposed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "heuristic",
      "strategy",
      "process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ASR Correction Framework",
      "resolved_canonical": "ASR Correction Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Finite State Machine",
      "resolved_canonical": "Finite State Machine",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Phonetic Variants",
      "resolved_canonical": "Phonetic Variants",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Listening, Imagining & Refining: A Heuristic Optimized ASR Correction Framework with LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15095.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.15095](https://arxiv.org/abs/2509.15095)

## 🔗 유사한 논문
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (85.5% similar)
- [[2025-09-23/Retrieval Enhanced Feedback via In-context Neural Error-book_20250923|Retrieval Enhanced Feedback via In-context Neural Error-book]] (82.9% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (82.9% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (82.2% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Finite State Machine|Finite State Machine]]
**⚡ Unique Technical**: [[keywords/ASR Correction Framework|ASR Correction Framework]], [[keywords/Phonetic Variants|Phonetic Variants]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15095v2 Announce Type: replace-cross 
Abstract: Automatic Speech Recognition (ASR) systems remain prone to errors that affect downstream applications. In this paper, we propose LIR-ASR, a heuristic optimized iterative correction framework using LLMs, inspired by human auditory perception. LIR-ASR applies a "Listening-Imagining-Refining" strategy, generating phonetic variants and refining them in context. A heuristic optimization with finite state machine (FSM) is introduced to prevent the correction process from being trapped in local optima and rule-based constraints help maintain semantic fidelity. Experiments on both English and Chinese ASR outputs show that LIR-ASR achieves average reductions in CER/WER of up to 1.5 percentage points compared to baselines, demonstrating substantial accuracy gains in transcription.

## 📝 요약

이 논문에서는 자동 음성 인식(ASR) 시스템의 오류를 개선하기 위해 LIR-ASR이라는 새로운 교정 프레임워크를 제안합니다. 인간의 청각 인식을 모방한 "듣기-상상하기-정제하기" 전략을 사용하여 음성 변형을 생성하고 문맥에서 이를 정제합니다. 유한 상태 기계(FSM)를 활용한 휴리스틱 최적화를 통해 지역 최적점에 빠지지 않도록 하며, 규칙 기반 제약을 통해 의미적 일관성을 유지합니다. 실험 결과, 영어와 중국어 ASR 출력에서 LIR-ASR은 CER/WER을 평균 1.5%포인트까지 감소시켜 정확도를 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. LIR-ASR는 인간의 청각 인식을 본떠 개발된 LLM 기반의 자동 음성 인식 오류 수정 프레임워크입니다.
- 2. "듣기-상상하기-정제하기" 전략을 통해 음성 변형을 생성하고 문맥 내에서 이를 정제합니다.
- 3. 유한 상태 기계(FSM)를 활용한 휴리스틱 최적화를 통해 지역 최적점에 갇히는 것을 방지합니다.
- 4. 규칙 기반 제약 조건을 통해 의미적 충실도를 유지합니다.
- 5. 실험 결과, LIR-ASR는 영어와 중국어 ASR 출력에서 평균 CER/WER을 최대 1.5% 포인트 감소시켜 정확성을 크게 향상시켰습니다.


---

*Generated on 2025-09-24 01:32:40*