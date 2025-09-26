---
keywords:
  - Large Language Model
  - Prompt Tuning
  - Entropy
  - Outlier Tokens
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.12244
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:55:00.169253",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Prompt Tuning",
    "Entropy",
    "Outlier Tokens"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Prompt Tuning": 0.78,
    "Entropy": 0.72,
    "Outlier Tokens": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Autoregressive neural language models",
        "canonical": "Large Language Model",
        "aliases": [
          "Autoregressive LMs",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Links to a fundamental concept in NLP and connects with other works on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "prompt tuning",
        "canonical": "Prompt Tuning",
        "aliases": [
          "Prompt Engineering"
        ],
        "category": "specific_connectable",
        "rationale": "A specific technique relevant to optimizing language model outputs, facilitating connections with related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "entropy",
        "canonical": "Entropy",
        "aliases": [
          "Information Entropy"
        ],
        "category": "unique_technical",
        "rationale": "A unique measure used to understand distribution complexity, aiding in linking to statistical analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "outlier tokens",
        "canonical": "Outlier Tokens",
        "aliases": [
          "Anomalous Tokens"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific phenomenon in token distribution, useful for niche research connections.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "probability distribution",
      "target distribution",
      "next-token distribution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Autoregressive neural language models",
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
      "candidate_surface": "prompt tuning",
      "resolved_canonical": "Prompt Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "entropy",
      "resolved_canonical": "Entropy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "outlier tokens",
      "resolved_canonical": "Outlier Tokens",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Distribution Prompting: Understanding the Expressivity of Language Models Through the Next-Token Distributions They Can Produce

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.12244.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.12244](https://arxiv.org/abs/2505.12244)

## 🔗 유사한 논문
- [[2025-09-23/Learning to vary_ Teaching LMs to reproduce human linguistic variability in next-word prediction_20250923|Learning to vary: Teaching LMs to reproduce human linguistic variability in next-word prediction]] (83.8% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (83.1% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.0% similar)
- [[2025-09-23/CIE_ Controlling Language Model Text Generations Using Continuous Signals_20250923|CIE: Controlling Language Model Text Generations Using Continuous Signals]] (82.8% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Prompt Tuning|Prompt Tuning]]
**⚡ Unique Technical**: [[keywords/Entropy|Entropy]], [[keywords/Outlier Tokens|Outlier Tokens]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.12244v2 Announce Type: replace 
Abstract: Autoregressive neural language models (LMs) generate a probability distribution over tokens at each time step given a prompt. In this work, we attempt to systematically understand the probability distributions that LMs can produce, showing that some distributions are significantly harder to elicit than others. Specifically, for any target next-token distribution over the vocabulary, we attempt to find a prompt that induces the LM to output a distribution as close as possible to the target, using either soft or hard gradient-based prompt tuning. We find that (1) in general, distributions with very low or very high entropy are easier to approximate than those with moderate entropy; (2) among distributions with the same entropy, those containing ''outlier tokens'' are easier to approximate; (3) target distributions generated by LMs -- even LMs with different tokenizers -- are easier to approximate than randomly chosen targets. These results offer insights into the expressiveness of LMs and the challenges of using them as probability distribution proposers.

## 📝 요약

이 논문은 자기회귀 신경망 언어 모델(LM)이 생성할 수 있는 확률 분포를 체계적으로 이해하려는 시도를 다룹니다. 연구에서는 주어진 목표 다음 토큰 분포에 최대한 근접한 분포를 생성하도록 하는 프롬프트를 찾기 위해 소프트 또는 하드 그라디언트 기반 프롬프트 튜닝을 사용합니다. 주요 발견 사항으로는 (1) 매우 낮거나 높은 엔트로피를 가진 분포가 중간 엔트로피를 가진 분포보다 근사하기 쉽다는 점, (2) 동일한 엔트로피를 가진 분포 중 '이상치 토큰'을 포함한 분포가 더 근사하기 쉽다는 점, (3) LM이 생성한 목표 분포가 무작위로 선택된 목표보다 근사하기 쉽다는 점이 있습니다. 이러한 결과는 LM의 표현력과 확률 분포 제안자로서의 사용에 대한 도전 과제를 이해하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 자회귀 신경망 언어 모델은 주어진 프롬프트에 따라 각 시간 단계에서 토큰에 대한 확률 분포를 생성한다.
- 2. 매우 낮거나 높은 엔트로피를 가진 분포는 중간 엔트로피를 가진 분포보다 근사하기 쉽다.
- 3. 같은 엔트로피를 가진 분포 중 '이상치 토큰'을 포함한 분포는 근사하기 쉽다.
- 4. LMs가 생성한 목표 분포는 무작위로 선택된 목표보다 근사하기 쉽다.
- 5. 연구 결과는 LMs의 표현력과 확률 분포 제안자로서의 사용에 대한 도전 과제를 이해하는 데 도움을 준다.


---

*Generated on 2025-09-24 03:55:00*