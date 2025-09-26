---
keywords:
  - Large Language Model
  - Self-consistency Estimation
  - Compute Budget Allocation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19489
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:14:25.599644",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Self-consistency Estimation",
    "Compute Budget Allocation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Self-consistency Estimation": 0.7,
    "Compute Budget Allocation": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLMs",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's analysis, linking to foundational concepts in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "self-consistency",
        "canonical": "Self-consistency Estimation",
        "aliases": [
          "consistency estimation",
          "self-consistency analysis"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's focus on LLM reliability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "compute budget",
        "canonical": "Compute Budget Allocation",
        "aliases": [
          "budget allocation",
          "compute resources"
        ],
        "category": "unique_technical",
        "rationale": "Key to understanding the trade-offs discussed in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "task distribution",
      "repeated calls"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLMs",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "self-consistency",
      "resolved_canonical": "Self-consistency Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "compute budget",
      "resolved_canonical": "Compute Budget Allocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Estimating the Self-Consistency of LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19489.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19489](https://arxiv.org/abs/2509.19489)

## 🔗 유사한 논문
- [[2025-09-23/Measuring Scalar Constructs in Social Science with LLMs_20250923|Measuring Scalar Constructs in Social Science with LLMs]] (86.5% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.9% similar)
- [[2025-09-24/Prompting for Performance_ Exploring LLMs for Configuring Software_20250924|Prompting for Performance: Exploring LLMs for Configuring Software]] (84.8% similar)
- [[2025-09-24/Large Language Models Do Multi-Label Classification Differently_20250924|Large Language Models Do Multi-Label Classification Differently]] (84.2% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Self-consistency Estimation|Self-consistency Estimation]], [[keywords/Compute Budget Allocation|Compute Budget Allocation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19489v1 Announce Type: new 
Abstract: Systems often repeat the same prompt to large language models (LLMs) and aggregate responses to improve reliability. This short note analyzes an estimator of the self-consistency of LLMs and the tradeoffs it induces under a fixed compute budget $B=mn$, where $m$ is the number of prompts sampled from the task distribution and $n$ is the number of repeated LLM calls per prompt; the resulting analysis favors a rough split $m,n\propto\sqrt{B}$.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 신뢰성을 높이기 위해 동일한 프롬프트를 반복하여 응답을 집계하는 시스템을 분석합니다. 고정된 계산 예산 $B=mn$ 하에서 LLM의 자기 일관성 추정치를 분석하며, 여기서 $m$은 작업 분포에서 샘플링된 프롬프트 수, $n$은 각 프롬프트에 대한 반복 호출 수입니다. 분석 결과, $m$과 $n$의 비율은 대략적으로 $\sqrt{B}$에 비례하는 것이 유리하다는 결론을 도출합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 신뢰성을 높이기 위해 동일한 프롬프트를 반복하여 응답을 집계하는 시스템이 자주 사용된다.
- 2. LLM의 자기 일관성 추정치를 분석하고, 고정된 계산 예산 하에서의 절충점을 탐구한다.
- 3. 계산 예산 $B=mn$에서, 작업 분포로부터 샘플링된 프롬프트의 수 $m$와 각 프롬프트에 대한 반복 호출 수 $n$의 최적 분할은 $m,n\propto\sqrt{B}$로 나타난다.


---

*Generated on 2025-09-25 15:14:25*