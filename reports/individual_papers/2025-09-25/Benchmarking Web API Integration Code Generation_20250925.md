---
keywords:
  - Large Language Model
  - API Integration
  - Web API Invocation
  - Evaluation Pipeline
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20172
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:01:45.220285",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "API Integration",
    "Web API Invocation",
    "Evaluation Pipeline"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "API Integration": 0.78,
    "Web API Invocation": 0.77,
    "Evaluation Pipeline": 0.8
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
        "rationale": "LLMs are central to the paper's exploration of automating web API code generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "API Integration",
        "canonical": "API Integration",
        "aliases": [
          "API Connectivity"
        ],
        "category": "unique_technical",
        "rationale": "API integration is the core focus of the study, linking to digital infrastructure discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Web API Invocation",
        "canonical": "Web API Invocation",
        "aliases": [
          "API Call",
          "API Request"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the specific challenges addressed in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Dataset and Evaluation Pipeline",
        "canonical": "Evaluation Pipeline",
        "aliases": [
          "Benchmarking Framework"
        ],
        "category": "specific_connectable",
        "rationale": "The evaluation pipeline is essential for assessing LLMs' performance in the study.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
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
      "candidate_surface": "API Integration",
      "resolved_canonical": "API Integration",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Web API Invocation",
      "resolved_canonical": "Web API Invocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Dataset and Evaluation Pipeline",
      "resolved_canonical": "Evaluation Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Benchmarking Web API Integration Code Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20172.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20172](https://arxiv.org/abs/2509.20172)

## 🔗 유사한 논문
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (84.9% similar)
- [[2025-09-19/Automated and Context-Aware Code Documentation Leveraging Advanced LLMs_20250919|Automated and Context-Aware Code Documentation Leveraging Advanced LLMs]] (84.0% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (83.9% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.8% similar)
- [[2025-09-25/Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers_20250925|Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Evaluation Pipeline|Evaluation Pipeline]]
**⚡ Unique Technical**: [[keywords/API Integration|API Integration]], [[keywords/Web API Invocation|Web API Invocation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20172v1 Announce Type: cross 
Abstract: API integration is a cornerstone of our digital infrastructure, enabling software systems to connect and interact. However, as shown by many studies, writing or generating correct code to invoke APIs, particularly web APIs, is challenging. Although large language models~(LLMs) have become popular in software development, their effectiveness in automating the generation of web API integration code remains unexplored. In order to address this, we present a dataset and evaluation pipeline designed to assess the ability of LLMs to generate web API invocation code. Our experiments with several open-source LLMs reveal that generating API invocations poses a significant challenge, resulting in hallucinated endpoints, incorrect argument usage, and other errors. None of the evaluated open-source models were able to solve more than 40% of the tasks.

## 📝 요약

이 논문은 웹 API 통합 코드를 자동 생성하는 데 있어 대형 언어 모델(LLM)의 효과를 평가하기 위해 데이터셋과 평가 파이프라인을 제안합니다. 실험 결과, 여러 오픈소스 LLM이 API 호출을 생성하는 데 어려움을 겪으며, 잘못된 엔드포인트 생성과 인수 사용 오류 등의 문제가 발생했습니다. 평가된 오픈소스 모델 중 40% 이상의 작업을 해결한 모델은 없었습니다. 이는 LLM이 웹 API 통합 코드 생성에 있어 여전히 한계가 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. API 통합은 디지털 인프라의 핵심 요소로, 소프트웨어 시스템 간의 연결과 상호작용을 가능하게 한다.
- 2. 웹 API 호출을 위한 올바른 코드를 작성하거나 생성하는 것은 여전히 어려운 과제이다.
- 3. 대형 언어 모델(LLMs)은 소프트웨어 개발에서 인기를 끌고 있지만, 웹 API 통합 코드 생성 자동화에서의 효과는 아직 탐구되지 않았다.
- 4. 실험 결과, 여러 오픈 소스 LLM들이 API 호출 생성에서 상당한 어려움을 겪으며, 잘못된 엔드포인트 생성이나 인수 사용 오류 등의 문제를 보였다.
- 5. 평가된 오픈 소스 모델 중 어느 것도 40% 이상의 작업을 해결하지 못했다.


---

*Generated on 2025-09-25 17:01:45*