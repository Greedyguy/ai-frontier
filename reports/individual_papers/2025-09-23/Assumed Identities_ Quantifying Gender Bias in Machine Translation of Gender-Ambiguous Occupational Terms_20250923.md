---
keywords:
  - Machine Translation
  - Gender Bias
  - GRAPE Metric
  - GAMBIT Dataset
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2503.04372
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:52:02.239908",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Translation",
    "Gender Bias",
    "GRAPE Metric",
    "GAMBIT Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Translation": 0.78,
    "Gender Bias": 0.79,
    "GRAPE Metric": 0.73,
    "GAMBIT Dataset": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "broad_technical",
        "rationale": "Machine Translation is a core area within Natural Language Processing, relevant for linking discussions on language models and translation systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gender Bias",
        "canonical": "Gender Bias",
        "aliases": [
          "Bias in Translation"
        ],
        "category": "unique_technical",
        "rationale": "Gender Bias is a critical issue in AI ethics and fairness, linking to broader discussions on bias mitigation in AI systems.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "GRAPE",
        "canonical": "GRAPE Metric",
        "aliases": [
          "GRAPE"
        ],
        "category": "unique_technical",
        "rationale": "GRAPE is a novel metric introduced in the paper, providing a unique method for evaluating gender bias in translation systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.73
      },
      {
        "surface": "GAMBIT",
        "canonical": "GAMBIT Dataset",
        "aliases": [
          "GAMBIT"
        ],
        "category": "unique_technical",
        "rationale": "GAMBIT is a new dataset specifically designed for benchmarking gender bias, offering unique data for research in bias evaluation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "gender-ambiguous occupational terms",
      "systematic patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gender Bias",
      "resolved_canonical": "Gender Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "GRAPE",
      "resolved_canonical": "GRAPE Metric",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "GAMBIT",
      "resolved_canonical": "GAMBIT Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.04372.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2503.04372](https://arxiv.org/abs/2503.04372)

## 🔗 유사한 논문
- [[2025-09-23/Auto-Search and Refinement_ An Automated Framework for Gender Bias Mitigation in Large Language Models_20250923|Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in Large Language Models]] (80.4% similar)
- [[2025-09-23/Specification-Aware Machine Translation and Evaluation for Purpose Alignment_20250923|Specification-Aware Machine Translation and Evaluation for Purpose Alignment]] (80.4% similar)
- [[2025-09-18/Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (79.3% similar)
- [[2025-09-22/Translationese-index_ Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese_20250922|Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese]] (78.8% similar)
- [[2025-09-23/Investigating Bias_ A Multilingual Pipeline for Generating, Solving, and Evaluating Math Problems with LLMs_20250923|Investigating Bias: A Multilingual Pipeline for Generating, Solving, and Evaluating Math Problems with LLMs]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Translation|Machine Translation]]
**⚡ Unique Technical**: [[keywords/Gender Bias|Gender Bias]], [[keywords/GRAPE Metric|GRAPE Metric]], [[keywords/GAMBIT Dataset|GAMBIT Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04372v3 Announce Type: replace 
Abstract: Machine Translation (MT) systems frequently encounter gender-ambiguous occupational terms, where they must assign gender without explicit contextual cues. While individual translations in such cases may not be inherently biased, systematic patterns-such as consistently translating certain professions with specific genders-can emerge, reflecting and perpetuating societal stereotypes. This ambiguity challenges traditional instance-level single-answer evaluation approaches, as no single gold standard translation exists. To address this, we introduce GRAPE, a probability-based metric designed to evaluate gender bias by analyzing aggregated model responses. Alongside this, we present GAMBIT, a benchmarking dataset in English with gender-ambiguous occupational terms. Using GRAPE, we evaluate several MT systems and examine whether their gendered translations in Greek and French align with or diverge from societal stereotypes, real-world occupational gender distributions, and normative standards

## 📝 요약

이 논문은 기계 번역 시스템이 성별이 모호한 직업 용어를 번역할 때 발생하는 성 편향 문제를 다룹니다. 전통적인 평가 방법으로는 이러한 편향을 제대로 평가하기 어려운 점을 지적하며, 이를 해결하기 위해 GRAPE라는 확률 기반의 성 편향 평가 지표를 제안합니다. 또한, 영어의 성별 모호한 직업 용어를 포함한 벤치마크 데이터셋인 GAMBIT를 소개합니다. 연구는 GRAPE를 사용하여 여러 기계 번역 시스템을 평가하고, 그리스어와 프랑스어 번역이 사회적 고정관념, 실제 직업 성별 분포, 규범적 기준과 어떻게 일치하거나 다른지를 분석합니다. 주요 기여는 성 편향을 체계적으로 평가할 수 있는 새로운 방법론을 제공한 점입니다.

## 🎯 주요 포인트

- 1. 기계 번역 시스템은 성별이 모호한 직업 용어를 번역할 때 명시적인 맥락 단서 없이 성별을 할당해야 하는 문제에 직면한다.
- 2. 특정 직업을 특정 성별로 일관되게 번역하는 체계적인 패턴은 사회적 고정관념을 반영하고 지속시킬 수 있다.
- 3. GRAPE는 모델의 집계된 응답을 분석하여 성별 편향을 평가하는 확률 기반 지표로 소개되었다.
- 4. GAMBIT는 성별이 모호한 직업 용어를 포함한 영어 벤치마킹 데이터셋으로 제시되었다.
- 5. GRAPE를 사용하여 여러 기계 번역 시스템을 평가하고, 그리스어와 프랑스어 번역이 사회적 고정관념 및 실제 직업 성별 분포와 어떻게 일치하거나 다른지를 조사하였다.


---

*Generated on 2025-09-24 03:52:02*