---
keywords:
  - Large Language Model
  - Disfluency Removal Evaluation Suite
  - Switchboard Transcripts
  - Speech-Driven Systems
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20321
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:06:35.392482",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Disfluency Removal Evaluation Suite",
    "Switchboard Transcripts",
    "Speech-Driven Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Disfluency Removal Evaluation Suite": 0.8,
    "Switchboard Transcripts": 0.77,
    "Speech-Driven Systems": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and provide a basis for connecting various disfluency removal strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Disfluency Removal Evaluation Suite",
        "canonical": "Disfluency Removal Evaluation Suite",
        "aliases": [
          "DRES"
        ],
        "category": "unique_technical",
        "rationale": "DRES is a novel benchmark specifically designed for evaluating disfluency removal, making it a unique technical contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Switchboard transcripts",
        "canonical": "Switchboard Transcripts",
        "aliases": [
          "Switchboard"
        ],
        "category": "specific_connectable",
        "rationale": "Switchboard transcripts are a well-known dataset in speech processing, providing a foundation for linking related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "speech-driven systems",
        "canonical": "Speech-Driven Systems",
        "aliases": [
          "Speech Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Speech-driven systems are a key application area for disfluency removal, facilitating connections to related technologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "disfluency",
      "removal",
      "evaluation",
      "suite",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Disfluency Removal Evaluation Suite",
      "resolved_canonical": "Disfluency Removal Evaluation Suite",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Switchboard transcripts",
      "resolved_canonical": "Switchboard Transcripts",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "speech-driven systems",
      "resolved_canonical": "Speech-Driven Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# DRES: Benchmarking LLMs for Disfluency Removal

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20321.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20321](https://arxiv.org/abs/2509.20321)

## 🔗 유사한 논문
- [[2025-09-25/Z-Scores_ A Metric for Linguistically Assessing Disfluency Removal_20250925|Z-Scores: A Metric for Linguistically Assessing Disfluency Removal]] (86.5% similar)
- [[2025-09-23/DCR_ Quantifying Data Contamination in LLMs Evaluation_20250923|DCR: Quantifying Data Contamination in LLMs Evaluation]] (84.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.1% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (84.1% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Switchboard Transcripts|Switchboard Transcripts]], [[keywords/Speech-Driven Systems|Speech-Driven Systems]]
**⚡ Unique Technical**: [[keywords/Disfluency Removal Evaluation Suite|Disfluency Removal Evaluation Suite]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20321v1 Announce Type: cross 
Abstract: Disfluencies -- such as "um," "uh," interjections, parentheticals, and edited statements -- remain a persistent challenge for speech-driven systems, degrading accuracy in command interpretation, summarization, and conversational agents. We introduce DRES (Disfluency Removal Evaluation Suite), a controlled text-level benchmark that establishes a reproducible semantic upper bound for this task. DRES builds on human-annotated Switchboard transcripts, isolating disfluency removal from ASR errors and acoustic variability. We systematically evaluate proprietary and open-source LLMs across scales, prompting strategies, and architectures. Our results reveal that (i) simple segmentation consistently improves performance, even for long-context models; (ii) reasoning-oriented models tend to over-delete fluent tokens; and (iii) fine-tuning achieves near state-of-the-art precision and recall but harms generalization abilities. We further present a set of LLM-specific error modes and offer nine practical recommendations (R1-R9) for deploying disfluency removal in speech-driven pipelines. DRES provides a reproducible, model-agnostic foundation for advancing robust spoken-language systems.

## 📝 요약

이 논문은 음성 기반 시스템에서 발생하는 비유창성 문제를 해결하기 위해 DRES(Disfluency Removal Evaluation Suite)를 소개합니다. DRES는 인간이 주석을 단 Switchboard 전사본을 기반으로 하여 비유창성 제거를 평가하는 통제된 텍스트 수준의 벤치마크입니다. 연구에서는 다양한 대규모 언어 모델(LLM)을 평가하여 간단한 세분화가 성능을 향상시키고, 추론 중심 모델은 유창한 토큰을 과도하게 삭제하는 경향이 있으며, 미세 조정이 정밀도와 재현율을 높이지만 일반화 능력을 저해한다는 것을 발견했습니다. 또한, LLM에 특화된 오류 모드를 제시하고, 비유창성 제거를 위한 9가지 실용적인 권장 사항을 제공합니다. DRES는 견고한 음성 언어 시스템 개발을 위한 재현 가능한 모델 독립적 기반을 제공합니다.

## 🎯 주요 포인트

- 1. DRES는 비유창성 제거를 위한 통제된 텍스트 수준 벤치마크로, 이 작업의 재현 가능한 의미적 상한선을 설정합니다.
- 2. DRES는 인간이 주석을 단 Switchboard 전사에 기반하여 비유창성 제거를 ASR 오류 및 음향 변동성과 분리합니다.
- 3. 간단한 세분화는 긴 문맥 모델에서도 일관되게 성능을 향상시킵니다.
- 4. 추론 지향 모델은 유창한 토큰을 과도하게 삭제하는 경향이 있습니다.
- 5. 미세 조정은 최첨단 정밀도와 재현율에 근접하지만 일반화 능력을 해칩니다.


---

*Generated on 2025-09-25 16:06:35*