---
keywords:
  - Large Language Model
  - Optimization Models
  - Natural Language Dialogue System
  - Functional Calls
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2501.08406
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:00:15.333306",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Optimization Models",
    "Natural Language Dialogue System",
    "Functional Calls"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Optimization Models": 0.78,
    "Natural Language Dialogue System": 0.82,
    "Functional Calls": 0.75
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
        "rationale": "Large Language Models are central to the paper's approach and connect to a wide range of NLP and AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Optimization Models",
        "canonical": "Optimization Models",
        "aliases": [
          "Optimization Model",
          "Optimization"
        ],
        "category": "unique_technical",
        "rationale": "Optimization Models are the core subject of the paper, providing a unique technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Natural Language Dialogue System",
        "canonical": "Natural Language Dialogue System",
        "aliases": [
          "Dialogue System",
          "Chatbot"
        ],
        "category": "specific_connectable",
        "rationale": "The dialogue system is a key component of the paper, facilitating interaction between users and models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Functional Calls",
        "canonical": "Functional Calls",
        "aliases": [
          "Function Calls",
          "API Calls"
        ],
        "category": "unique_technical",
        "rationale": "Functional calls are crucial for integrating LLMs with optimization models, offering a unique technical angle.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
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
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Optimization Models",
      "resolved_canonical": "Optimization Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Natural Language Dialogue System",
      "resolved_canonical": "Natural Language Dialogue System",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Functional Calls",
      "resolved_canonical": "Functional Calls",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# OptiChat: Bridging Optimization Models and Practitioners with Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.08406.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2501.08406](https://arxiv.org/abs/2501.08406)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.4% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.0% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (83.7% similar)
- [[2025-09-23/"What's Up, Doc?"_ Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets_20250923|"What's Up, Doc?": Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets]] (83.1% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Natural Language Dialogue System|Natural Language Dialogue System]]
**⚡ Unique Technical**: [[keywords/Optimization Models|Optimization Models]], [[keywords/Functional Calls|Functional Calls]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.08406v2 Announce Type: replace-cross 
Abstract: Optimization models have been applied to solve a wide variety of decision-making problems. These models are usually developed by optimization experts but are used by practitioners without optimization expertise in various application domains. As a result, practitioners often struggle to interact with and draw useful conclusions from optimization models independently. To fill this gap, we introduce OptiChat, a natural language dialogue system designed to help practitioners interpret model formulation, diagnose infeasibility, analyze sensitivity, retrieve information, evaluate modifications, and provide counterfactual explanations. By augmenting large language models (LLMs) with functional calls and code generation tailored for optimization models, we enable seamless interaction and minimize the risk of hallucinations in OptiChat. We develop a new dataset to evaluate OptiChat's performance in explaining optimization models. Experiments demonstrate that OptiChat effectively bridges the gap between optimization models and practitioners, delivering autonomous, accurate, and instant responses.

## 📝 요약

이 논문은 최적화 모델을 이해하기 어려워하는 실무자들을 위해 자연어 대화 시스템인 OptiChat을 소개합니다. OptiChat은 모델의 해석, 비현실성 진단, 민감도 분석, 정보 검색, 수정 평가 및 반사실적 설명을 지원합니다. 대형 언어 모델(LLM)에 최적화 모델에 맞춘 함수 호출과 코드 생성을 결합하여, 실무자들이 모델과 원활하게 상호작용할 수 있도록 설계되었습니다. 새로운 데이터셋을 통해 OptiChat의 성능을 평가한 결과, 실무자와 최적화 모델 간의 간극을 효과적으로 메우며, 자율적이고 정확한 즉각적인 응답을 제공함을 확인했습니다.

## 🎯 주요 포인트

- 1. OptiChat은 최적화 모델을 해석하고, 불가능성을 진단하며, 민감도를 분석하는 자연어 대화 시스템입니다.
- 2. OptiChat은 최적화 모델에 맞춘 기능 호출과 코드 생성을 통해 대화의 일관성을 높이고 환각의 위험을 최소화합니다.
- 3. 새로운 데이터셋을 개발하여 OptiChat의 최적화 모델 설명 성능을 평가하였습니다.
- 4. 실험 결과, OptiChat은 최적화 모델과 실무자 간의 격차를 효과적으로 줄이며, 자율적이고 정확한 즉각적인 응답을 제공합니다.


---

*Generated on 2025-09-24 03:00:15*