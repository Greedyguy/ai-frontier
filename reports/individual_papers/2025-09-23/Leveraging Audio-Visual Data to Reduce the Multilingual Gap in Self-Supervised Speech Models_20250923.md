---
keywords:
  - Self-supervised Learning
  - Multilingual Self-supervised Learning
  - Visual Grounding
  - Zero-Shot Learning
  - Speech Representation Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17523
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:29:39.148807",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Multilingual Self-supervised Learning",
    "Visual Grounding",
    "Zero-Shot Learning",
    "Speech Representation Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.88,
    "Multilingual Self-supervised Learning": 0.75,
    "Visual Grounding": 0.8,
    "Zero-Shot Learning": 0.77,
    "Speech Representation Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "A core method in the paper, connecting with existing models like wav2vec 2.0 and HuBERT.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Multilingual SSL models",
        "canonical": "Multilingual Self-supervised Learning",
        "aliases": [
          "Multilingual SSL"
        ],
        "category": "unique_technical",
        "rationale": "Addresses the multilingual gap, a central challenge discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Visual grounding",
        "canonical": "Visual Grounding",
        "aliases": [
          "Visual Context"
        ],
        "category": "specific_connectable",
        "rationale": "Introduces a novel approach to improve multilingual model performance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Zero-shot phonetic discrimination",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot Discrimination"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the performance improvement in zero-shot scenarios, a key result.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "Speech representation learning",
        "canonical": "Speech Representation Learning",
        "aliases": [
          "Speech Embeddings"
        ],
        "category": "broad_technical",
        "rationale": "Fundamental to the paper's focus on improving speech model performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "multilingual gap",
      "performance gap"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Multilingual SSL models",
      "resolved_canonical": "Multilingual Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Visual grounding",
      "resolved_canonical": "Visual Grounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Zero-shot phonetic discrimination",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Speech representation learning",
      "resolved_canonical": "Speech Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Leveraging Audio-Visual Data to Reduce the Multilingual Gap in Self-Supervised Speech Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17523.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17523](https://arxiv.org/abs/2509.17523)

## 🔗 유사한 논문
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (84.3% similar)
- [[2025-09-22/The Curious Case of Visual Grounding_ Different Effects for Speech- and Text-based Language Encoders_20250922|The Curious Case of Visual Grounding: Different Effects for Speech- and Text-based Language Encoders]] (84.2% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (84.0% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (83.7% similar)
- [[2025-09-23/An Effective Strategy for Modeling Score Ordinality and Non-uniform Intervals in Automated Speaking Assessment_20250923|An Effective Strategy for Modeling Score Ordinality and Non-uniform Intervals in Automated Speaking Assessment]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Speech Representation Learning|Speech Representation Learning]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Visual Grounding|Visual Grounding]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Multilingual Self-supervised Learning|Multilingual Self-supervised Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17523v1 Announce Type: new 
Abstract: Self-supervised learning (SSL) has made significant advances in speech representation learning. Models like wav2vec 2.0 and HuBERT have achieved state-of-the-art results in tasks such as speech recognition, particularly in monolingual settings. However, multilingual SSL models tend to underperform their monolingual counterparts on each individual language, especially in multilingual scenarios with few languages such as the bilingual setting. In this work, we investigate a novel approach to reduce this performance gap by introducing limited visual grounding into bilingual speech SSL models. Our results show that visual grounding benefits both monolingual and bilingual models, with especially pronounced gains for the latter, reducing the multilingual performance gap on zero-shot phonetic discrimination from 31.5% for audio-only models to 8.04% with grounding.

## 📝 요약

이 논문은 음성 표현 학습에서 자가 지도 학습(SSL)의 발전을 다룹니다. 기존의 wav2vec 2.0과 HuBERT 모델은 단일 언어 환경에서 뛰어난 성과를 보였으나, 다중 언어 SSL 모델은 개별 언어에서 성능이 저하되는 문제가 있었습니다. 본 연구는 이 성능 격차를 줄이기 위해 시각적 기반을 도입하는 새로운 접근법을 제안합니다. 연구 결과, 시각적 기반은 단일 언어 및 이중 언어 모델 모두에 이점을 제공하며, 특히 이중 언어 모델에서 성능 격차를 크게 줄였습니다. 시각적 기반을 통해 오디오 전용 모델의 31.5% 성능 격차가 8.04%로 감소했습니다.

## 🎯 주요 포인트

- 1. 자가 지도 학습(SSL)은 음성 표현 학습에서 큰 발전을 이루었으며, wav2vec 2.0과 HuBERT와 같은 모델은 단일 언어 환경에서 뛰어난 성과를 보였습니다.
- 2. 다국어 SSL 모델은 각 개별 언어에서 단일 언어 모델보다 성능이 떨어지며, 특히 이중 언어와 같은 소수 언어 환경에서 그 차이가 두드러집니다.
- 3. 본 연구에서는 이 성능 격차를 줄이기 위해 이중 언어 음성 SSL 모델에 제한된 시각적 기초를 도입하는 새로운 접근 방식을 제안합니다.
- 4. 시각적 기초는 단일 언어 및 이중 언어 모델 모두에 이점을 제공하며, 특히 이중 언어 모델에서 두드러진 성능 향상을 보여줍니다.
- 5. 시각적 기초를 도입함으로써 오디오 전용 모델의 다국어 성능 격차가 31.5%에서 8.04%로 감소했습니다.


---

*Generated on 2025-09-24 03:29:39*