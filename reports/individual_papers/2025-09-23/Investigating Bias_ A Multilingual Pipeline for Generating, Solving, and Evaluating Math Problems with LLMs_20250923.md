---
keywords:
  - Large Language Model
  - Multilingual Pipeline
  - Linguistic Bias
  - Educational Support Systems
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17701
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:07:13.384637",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multilingual Pipeline",
    "Linguistic Bias",
    "Educational Support Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multilingual Pipeline": 0.81,
    "Linguistic Bias": 0.79,
    "Educational Support Systems": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and connect to existing research in AI and education.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "multilingual pipeline",
        "canonical": "Multilingual Pipeline",
        "aliases": [
          "multilingual system"
        ],
        "category": "unique_technical",
        "rationale": "The multilingual pipeline is a unique aspect of the study, facilitating cross-linguistic analysis and linking to multilingual AI research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "linguistic bias",
        "canonical": "Linguistic Bias",
        "aliases": [
          "language bias"
        ],
        "category": "specific_connectable",
        "rationale": "Linguistic bias is a key finding in the paper, relevant to discussions on fairness and equity in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "educational support",
        "canonical": "Educational Support Systems",
        "aliases": [
          "education technology"
        ],
        "category": "evolved_concepts",
        "rationale": "Educational support systems are a growing area of interest, linking AI applications to real-world educational contexts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multilingual pipeline",
      "resolved_canonical": "Multilingual Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "linguistic bias",
      "resolved_canonical": "Linguistic Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "educational support",
      "resolved_canonical": "Educational Support Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Investigating Bias: A Multilingual Pipeline for Generating, Solving, and Evaluating Math Problems with LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17701.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17701](https://arxiv.org/abs/2509.17701)

## 🔗 유사한 논문
- [[2025-09-22/Best-of-L_ Cross-Lingual Reward Modeling for Mathematical Reasoning_20250922|Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning]] (85.3% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (85.1% similar)
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (84.7% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.7% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Linguistic Bias|Linguistic Bias]]
**⚡ Unique Technical**: [[keywords/Multilingual Pipeline|Multilingual Pipeline]]
**🚀 Evolved Concepts**: [[keywords/Educational Support Systems|Educational Support Systems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17701v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) are increasingly used for educational support, yet their response quality varies depending on the language of interaction. This paper presents an automated multilingual pipeline for generating, solving, and evaluating math problems aligned with the German K-10 curriculum. We generated 628 math exercises and translated them into English, German, and Arabic. Three commercial LLMs (GPT-4o-mini, Gemini 2.5 Flash, and Qwen-plus) were prompted to produce step-by-step solutions in each language. A held-out panel of LLM judges, including Claude 3.5 Haiku, evaluated solution quality using a comparative framework. Results show a consistent gap, with English solutions consistently rated highest, and Arabic often ranked lower. These findings highlight persistent linguistic bias and the need for more equitable multilingual AI systems in education.

## 📝 요약

이 논문은 독일 K-10 교육과정에 맞춘 수학 문제를 자동으로 생성, 해결, 평가하는 다국어 파이프라인을 제시합니다. 628개의 수학 문제를 영어, 독일어, 아랍어로 번역하고, 세 가지 상용 대형 언어 모델(LLM)을 사용해 각 언어로 단계별 해답을 생성했습니다. 평가 결과, 영어 해답의 품질이 가장 높았고 아랍어는 낮게 평가되었습니다. 이는 언어적 편향이 존재함을 보여주며, 교육 분야에서 공정한 다국어 AI 시스템의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 교육 지원에 점점 더 많이 사용되지만, 상호작용 언어에 따라 응답 품질이 달라집니다.
- 2. 본 논문은 독일 K-10 교육과정에 맞춘 수학 문제를 생성, 해결, 평가하는 자동 다국어 파이프라인을 제시합니다.
- 3. 628개의 수학 문제를 생성하여 영어, 독일어, 아랍어로 번역하였고, 세 가지 상업용 LLM을 통해 각 언어로 단계별 해답을 생성했습니다.
- 4. 평가 결과, 영어 해답이 가장 높은 평가를 받았고 아랍어 해답은 낮은 평가를 받는 경향이 있었습니다.
- 5. 이러한 결과는 언어적 편향의 지속성을 강조하며, 교육에서 보다 공평한 다국어 AI 시스템의 필요성을 시사합니다.


---

*Generated on 2025-09-24 00:07:13*