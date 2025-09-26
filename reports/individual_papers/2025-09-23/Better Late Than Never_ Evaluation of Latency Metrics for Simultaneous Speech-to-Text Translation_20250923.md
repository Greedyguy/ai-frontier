---
keywords:
  - Simultaneous Speech-to-Text Translation
  - Yet Another Average Lagging
  - SoftSegmenter
  - Natural Language Processing
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17349
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:53:15.064651",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Simultaneous Speech-to-Text Translation",
    "Yet Another Average Lagging",
    "SoftSegmenter",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Simultaneous Speech-to-Text Translation": 0.78,
    "Yet Another Average Lagging": 0.77,
    "SoftSegmenter": 0.74,
    "Natural Language Processing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Simultaneous speech-to-text translation",
        "canonical": "Simultaneous Speech-to-Text Translation",
        "aliases": [
          "SimulST"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized area within translation systems, crucial for linking research on real-time translation technologies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "YAAL",
        "canonical": "Yet Another Average Lagging",
        "aliases": [
          "YAAL"
        ],
        "category": "unique_technical",
        "rationale": "A new metric proposed in the paper, important for linking discussions on latency evaluation in translation systems.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "SoftSegmenter",
        "canonical": "SoftSegmenter",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel tool introduced in the paper, relevant for linking to work on segmentation and alignment in speech processing.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "A foundational field relevant to the paper's focus on translation and latency metrics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "latency metrics",
      "translation quality",
      "segmentation bias"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Simultaneous speech-to-text translation",
      "resolved_canonical": "Simultaneous Speech-to-Text Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "YAAL",
      "resolved_canonical": "Yet Another Average Lagging",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "SoftSegmenter",
      "resolved_canonical": "SoftSegmenter",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Better Late Than Never: Evaluation of Latency Metrics for Simultaneous Speech-to-Text Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17349.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17349](https://arxiv.org/abs/2509.17349)

## 🔗 유사한 논문
- [[2025-09-22/Direct Simultaneous Translation Activation for Large Audio-Language Models_20250922|Direct Simultaneous Translation Activation for Large Audio-Language Models]] (82.2% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (79.9% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (79.0% similar)
- [[2025-09-17/SSL-SSAW_ Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation_20250917|SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (78.8% similar)
- [[2025-09-22/VoXtream_ Full-Stream Text-to-Speech with Extremely Low Latency_20250922|VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Simultaneous Speech-to-Text Translation|Simultaneous Speech-to-Text Translation]], [[keywords/Yet Another Average Lagging|Yet Another Average Lagging]], [[keywords/SoftSegmenter|SoftSegmenter]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17349v1 Announce Type: cross 
Abstract: Simultaneous speech-to-text translation (SimulST) systems have to balance translation quality with latency--the delay between speech input and the translated output. While quality evaluation is well established, accurate latency measurement remains a challenge. Existing metrics often produce inconsistent or misleading results, especially in the widely used short-form setting, where speech is artificially presegmented. In this paper, we present the first comprehensive analysis of SimulST latency metrics across language pairs, systems, and both short- and long-form regimes. We uncover a structural bias in current metrics related to segmentation that undermines fair and meaningful comparisons. To address this, we introduce YAAL (Yet Another Average Lagging), a refined latency metric that delivers more accurate evaluations in the short-form regime. We extend YAAL to LongYAAL for unsegmented audio and propose SoftSegmenter, a novel resegmentation tool based on word-level alignment. Our experiments show that YAAL and LongYAAL outperform popular latency metrics, while SoftSegmenter enhances alignment quality in long-form evaluation, together enabling more reliable assessments of SimulST systems.

## 📝 요약

이 논문은 동시 음성-텍스트 번역(SimulST) 시스템의 번역 품질과 지연 시간 간의 균형을 맞추는 문제를 다룹니다. 기존의 지연 시간 측정 지표는 특히 짧은 형태의 설정에서 일관되지 않거나 오해를 불러일으킬 수 있습니다. 본 연구는 다양한 언어 쌍과 시스템, 그리고 짧은 및 긴 형태의 설정에서 SimulST 지연 시간 지표를 종합적으로 분석한 최초의 연구입니다. 현재 지표의 구조적 편향을 발견하고 이를 해결하기 위해 YAAL(Yet Another Average Lagging)이라는 정제된 지연 시간 지표를 제안합니다. YAAL은 짧은 형태의 설정에서 더 정확한 평가를 제공하며, LongYAAL로 확장하여 비분할 오디오에 적용할 수 있습니다. 또한, SoftSegmenter라는 새로운 재분할 도구를 제안하여 단어 수준 정렬을 기반으로 합니다. 실험 결과, YAAL과 LongYAAL은 기존의 지연 시간 지표보다 우수하며, SoftSegmenter는 긴 형태 평가에서 정렬 품질을 향상시켜 SimulST 시스템의 평가를 더욱 신뢰할 수 있게 합니다.

## 🎯 주요 포인트

- 1. SimulST 시스템은 번역 품질과 지연 시간의 균형을 맞춰야 하며, 지연 시간 측정은 여전히 어려운 과제입니다.
- 2. 기존 지연 시간 측정 지표는 특히 인위적으로 분할된 짧은 형태의 설정에서 일관되지 않거나 오해를 불러일으킬 수 있습니다.
- 3. YAAL(새로운 평균 지연)이라는 정제된 지연 시간 지표를 도입하여 짧은 형태의 설정에서 더 정확한 평가를 제공합니다.
- 4. LongYAAL은 분할되지 않은 오디오에 대한 지표로 확장되었으며, SoftSegmenter라는 새로운 재분할 도구는 단어 수준의 정렬을 기반으로 합니다.
- 5. 실험 결과, YAAL과 LongYAAL이 인기 있는 지연 시간 지표보다 우수하며, SoftSegmenter는 긴 형태 평가에서 정렬 품질을 향상시킵니다.


---

*Generated on 2025-09-23 23:53:15*