---
keywords:
  - Large Language Model
  - Psychometric Properties
  - AIPsychoBench
  - Role-Playing Prompt
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16530
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:23:55.510553",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Psychometric Properties",
    "AIPsychoBench",
    "Role-Playing Prompt"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Psychometric Properties": 0.78,
    "AIPsychoBench": 0.82,
    "Role-Playing Prompt": 0.77
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus on psychometrics and are a key concept in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "psychometric properties",
        "canonical": "Psychometric Properties",
        "aliases": [
          "psychometrics",
          "psychometric measures"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for linking discussions on cognitive assessments between humans and LLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "AIPsychoBench",
        "canonical": "AIPsychoBench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "As a new benchmark introduced in the paper, it is essential for understanding LLM psychometrics.",
        "novelty_score": 0.95,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "role-playing prompt",
        "canonical": "Role-Playing Prompt",
        "aliases": [
          "role-play prompt"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is pivotal for improving response rates in LLM assessments.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "human scales",
      "traditional jailbreak prompts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "psychometric properties",
      "resolved_canonical": "Psychometric Properties",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AIPsychoBench",
      "resolved_canonical": "AIPsychoBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "role-playing prompt",
      "resolved_canonical": "Role-Playing Prompt",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16530.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16530](https://arxiv.org/abs/2509.16530)

## 🔗 유사한 논문
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (89.4% similar)
- [[2025-09-22/Benchmark of stylistic variation in LLM-generated texts_20250922|Benchmark of stylistic variation in LLM-generated texts]] (86.7% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (86.5% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (86.4% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (86.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Role-Playing Prompt|Role-Playing Prompt]]
**⚡ Unique Technical**: [[keywords/Psychometric Properties|Psychometric Properties]], [[keywords/AIPsychoBench|AIPsychoBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16530v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) with hundreds of billions of parameters have exhibited human-like intelligence by learning from vast amounts of internet-scale data. However, the uninterpretability of large-scale neural networks raises concerns about the reliability of LLM. Studies have attempted to assess the psychometric properties of LLMs by borrowing concepts from human psychology to enhance their interpretability, but they fail to account for the fundamental differences between LLMs and humans. This results in high rejection rates when human scales are reused directly. Furthermore, these scales do not support the measurement of LLM psychological property variations in different languages. This paper introduces AIPsychoBench, a specialized benchmark tailored to assess the psychological properties of LLM. It uses a lightweight role-playing prompt to bypass LLM alignment, improving the average effective response rate from 70.12% to 90.40%. Meanwhile, the average biases are only 3.3% (positive) and 2.1% (negative), which are significantly lower than the biases of 9.8% and 6.9%, respectively, caused by traditional jailbreak prompts. Furthermore, among the total of 112 psychometric subcategories, the score deviations for seven languages compared to English ranged from 5% to 20.2% in 43 subcategories, providing the first comprehensive evidence of the linguistic impact on the psychometrics of LLM.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 심리적 속성을 평가하기 위해 AIPsychoBench라는 벤치마크를 제안합니다. 기존의 인간 심리학 개념을 차용한 연구들은 LLM과 인간의 근본적 차이를 간과하여 높은 거부율을 보였습니다. AIPsychoBench는 경량화된 역할 수행 프롬프트를 사용하여 LLM의 정렬 문제를 우회하며, 평균 유효 응답률을 70.12%에서 90.40%로 향상시켰습니다. 또한, 전통적 방법보다 편향이 크게 감소했습니다. 7개 언어의 심리측정 점수 편차를 분석하여 LLM의 심리측정에 미치는 언어적 영향을 처음으로 포괄적으로 증명했습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)의 해석 가능성을 높이기 위해 인간 심리학 개념을 차용한 연구들이 있지만, LLM과 인간의 근본적인 차이를 간과하여 높은 거부율을 초래한다.
- 2. 기존의 인간 심리 척도는 LLM의 심리적 특성 변화를 다양한 언어에서 측정하는 데 한계가 있다.
- 3. AIPsychoBench는 LLM의 심리적 특성을 평가하기 위한 특화된 벤치마크로, 경량의 롤플레잉 프롬프트를 사용하여 LLM 정렬 문제를 우회하고 평균 유효 응답률을 70.12%에서 90.40%로 향상시킨다.
- 4. AIPsychoBench는 전통적인 탈옥 프롬프트에 비해 편향이 크게 줄어들어, 긍정적 편향 3.3%와 부정적 편향 2.1%를 기록한다.
- 5. 112개의 심리 측정 하위 범주 중 43개에서 영어와 비교했을 때 7개 언어의 점수 편차가 5%에서 20.2% 범위로 나타나, LLM의 심리 측정에 대한 언어적 영향에 대한 포괄적인 증거를 제공한다.


---

*Generated on 2025-09-23 23:23:55*