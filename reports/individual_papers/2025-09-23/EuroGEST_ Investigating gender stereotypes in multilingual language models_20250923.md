---
keywords:
  - Large Language Model
  - Gender Stereotypes
  - Multilingual Language Models
  - EuroGEST Dataset
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.03867
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:02:39.461251",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Gender Stereotypes",
    "Multilingual Language Models",
    "EuroGEST Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Gender Stereotypes": 0.88,
    "Multilingual Language Models": 0.82,
    "EuroGEST Dataset": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing discussions on the capabilities and biases of large-scale AI models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "gender stereotypes",
        "canonical": "Gender Stereotypes",
        "aliases": [
          "gender bias",
          "stereotypical reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on bias in language models across multiple languages.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "multilingual language models",
        "canonical": "Multilingual Language Models",
        "aliases": [
          "multilingual LLMs",
          "cross-lingual models"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the multilingual aspect of the study, relevant for cross-lingual NLP research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "EuroGEST",
        "canonical": "EuroGEST Dataset",
        "aliases": [
          "EuroGEST benchmark"
        ],
        "category": "unique_technical",
        "rationale": "A new dataset introduced by the paper, crucial for understanding gender bias in multilingual contexts.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
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
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "gender stereotypes",
      "resolved_canonical": "Gender Stereotypes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "multilingual language models",
      "resolved_canonical": "Multilingual Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "EuroGEST",
      "resolved_canonical": "EuroGEST Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# EuroGEST: Investigating gender stereotypes in multilingual language models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.03867.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.03867](https://arxiv.org/abs/2506.03867)

## 🔗 유사한 논문
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (84.7% similar)
- [[2025-09-23/AIPsychoBench_ Understanding the Psychometric Differences between LLMs and Humans_20250923|AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans]] (84.1% similar)
- [[2025-09-23/Justice in Judgment_ Unveiling (Hidden) Bias in LLM-assisted Peer Reviews_20250923|Justice in Judgment: Unveiling (Hidden) Bias in LLM-assisted Peer Reviews]] (83.7% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (83.6% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multilingual Language Models|Multilingual Language Models]]
**⚡ Unique Technical**: [[keywords/Gender Stereotypes|Gender Stereotypes]], [[keywords/EuroGEST Dataset|EuroGEST Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.03867v2 Announce Type: replace 
Abstract: Large language models increasingly support multiple languages, yet most benchmarks for gender bias remain English-centric. We introduce EuroGEST, a dataset designed to measure gender-stereotypical reasoning in LLMs across English and 29 European languages. EuroGEST builds on an existing expert-informed benchmark covering 16 gender stereotypes, expanded in this work using translation tools, quality estimation metrics, and morphological heuristics. Human evaluations confirm that our data generation method results in high accuracy of both translations and gender labels across languages. We use EuroGEST to evaluate 24 multilingual language models from six model families, demonstrating that the strongest stereotypes in all models across all languages are that women are 'beautiful', 'empathetic' and 'neat' and men are 'leaders', 'strong, tough' and 'professional'. We also show that larger models encode gendered stereotypes more strongly and that instruction finetuning does not consistently reduce gendered stereotypes. Our work highlights the need for more multilingual studies of fairness in LLMs and offers scalable methods and resources to audit gender bias across languages.

## 📝 요약

이 논문은 다국어를 지원하는 대형 언어 모델(LLM)에서의 성별 편향을 측정하기 위해 EuroGEST라는 데이터셋을 소개합니다. EuroGEST는 기존의 16가지 성별 고정관념을 포함한 벤치마크를 기반으로 하며, 번역 도구와 품질 추정 지표, 형태학적 추론을 사용하여 29개의 유럽 언어로 확장되었습니다. 인간 평가를 통해 번역과 성별 레이블의 높은 정확성을 확인했습니다. 24개의 다국어 언어 모델을 평가한 결과, 모든 모델과 언어에서 여성은 '아름답고', '공감적이며', '깔끔하다'는 고정관념이, 남성은 '리더', '강하고 터프하며', '전문적이다'는 고정관념이 강하게 나타났습니다. 또한, 더 큰 모델일수록 성별 고정관념을 더 강하게 인코딩하며, 지시 미세 조정이 항상 성별 고정관념을 줄이지는 않는다는 것을 보여줍니다. 이 연구는 LLM의 공정성을 다루는 다국어 연구의 필요성을 강조하며, 성별 편향을 감사할 수 있는 확장 가능한 방법과 자원을 제공합니다.

## 🎯 주요 포인트

- 1. EuroGEST는 영어와 29개의 유럽 언어에서 대형 언어 모델(LLM)의 성별 고정관념적 추론을 측정하기 위해 설계된 데이터셋입니다.
- 2. EuroGEST는 16개의 성별 고정관념을 다루는 기존의 전문가 정보 기반 벤치마크를 바탕으로 번역 도구, 품질 추정 지표 및 형태론적 휴리스틱을 사용하여 확장되었습니다.
- 3. 인간 평가 결과, EuroGEST의 데이터 생성 방법이 번역 및 성별 레이블의 높은 정확성을 보장함을 확인했습니다.
- 4. 연구 결과, 모든 언어 모델에서 여성은 '아름답고', '공감적이며', '깔끔하다'는 고정관념이, 남성은 '리더', '강하고 터프하며', '전문적이다'는 고정관념이 가장 강하게 나타났습니다.
- 5. 대형 모델일수록 성별 고정관념을 더 강하게 내포하며, 지시 기반 미세 조정이 일관되게 성별 고정관념을 줄이지는 못한다는 것을 보여줍니다.


---

*Generated on 2025-09-24 04:02:39*