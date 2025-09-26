---
keywords:
  - Large Language Model
  - Wisdom of Crowds
  - World Model
  - Guesstimation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2501.17310
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:24:43.497644",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Wisdom of Crowds",
    "World Model",
    "Guesstimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Wisdom of Crowds": 0.78,
    "World Model": 0.8,
    "Guesstimation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader field of language models and their applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Wisdom of Crowds",
        "canonical": "Wisdom of Crowds",
        "aliases": [
          "WOC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a unique approach to improve LLM performance through crowd-sourced estimation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "World Model",
        "canonical": "World Model",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights the conceptual framework within which LLMs operate for reasoning tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Guesstimation",
        "canonical": "Guesstimation",
        "aliases": [
          "Estimation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on using LLMs for approximate reasoning tasks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
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
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Wisdom of Crowds",
      "resolved_canonical": "Wisdom of Crowds",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "World Model",
      "resolved_canonical": "World Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Guesstimation",
      "resolved_canonical": "Guesstimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Probing LLM World Models: Enhancing Guesstimation with Wisdom of Crowds Decoding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.17310.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2501.17310](https://arxiv.org/abs/2501.17310)

## 🔗 유사한 논문
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (84.6% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.3% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (84.0% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (83.0% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/World Model|World Model]]
**⚡ Unique Technical**: [[keywords/Wisdom of Crowds|Wisdom of Crowds]], [[keywords/Guesstimation|Guesstimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.17310v3 Announce Type: replace 
Abstract: Guesstimation--the task of making approximate quantitative estimates about objects or events-is a common real--world skill, yet remains underexplored in large language model (LLM) research. We introduce three guesstimation datasets: MARBLES, FUTURE, and ELECPRED, spanning physical estimation (e.g., how many marbles fit in a cup) to abstract predictions (e.g., the 2024 U.S. presidential election). Inspired by the social science concept of Wisdom of Crowds (WOC)- where the median of multiple estimates improves accuracy-we propose WOC decoding for LLMs. We replicate WOC effects in human participants and find that LLMs exhibit similar benefits: median aggregation across sampled responses consistently improves accuracy over greedy decoding, self-consistency decoding, and mean decoding. This suggests that LLMs encode a world model that supports approximate reasoning. Our results position guesstimation as a useful probe of LLM world knowledge and highlight WOC decoding as a strategy for enhancing LLM guesstimation performance on real-world tasks.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 연구에서 상대적으로 덜 탐구된 '추정' 과제를 다룹니다. 저자들은 물리적 추정부터 추상적 예측까지 아우르는 세 가지 데이터셋(MARBLES, FUTURE, ELECPRED)을 소개합니다. 사회과학의 '군중의 지혜(WOC)' 개념에 영감을 받아, LLM에서 WOC 디코딩을 제안합니다. 연구 결과, LLM에서도 WOC 효과가 나타나며, 샘플링된 응답의 중위수 집계가 정확성을 향상시킴을 확인했습니다. 이는 LLM이 세계 모델을 통해 근사 추론을 지원함을 시사하며, WOC 디코딩이 실제 과제에서 LLM의 추정 성능을 향상시키는 전략임을 강조합니다.

## 🎯 주요 포인트

- 1. Guesstimation은 실제 세계에서 흔히 사용되는 기술이지만, 대형 언어 모델(LLM) 연구에서는 충분히 탐구되지 않았다.
- 2. 본 연구에서는 물리적 추정부터 추상적 예측까지 아우르는 세 가지 guesstimation 데이터셋(MARBLES, FUTURE, ELECPRED)을 소개한다.
- 3. 군중의 지혜(Wisdom of Crowds, WOC) 개념에 영감을 받아, LLM의 정확성을 향상시키기 위한 WOC 디코딩 방법을 제안한다.
- 4. WOC 효과를 인간 참여자와 LLM에서 재현한 결과, 샘플링된 응답의 중위수 집계가 정확성을 향상시키는 것으로 나타났다.
- 5. 연구 결과는 guesstimation이 LLM의 세계 지식을 탐구하는 유용한 도구임을 보여주며, WOC 디코딩이 실제 과제에서 LLM의 성능을 향상시키는 전략임을 강조한다.


---

*Generated on 2025-09-24 00:24:43*