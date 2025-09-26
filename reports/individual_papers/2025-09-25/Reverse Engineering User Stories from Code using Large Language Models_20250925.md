---
keywords:
  - Large Language Model
  - User Stories
  - Prompt Design
  - Chain-of-Thought Reasoning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19587
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:39:06.800435",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "User Stories",
    "Prompt Design",
    "Chain-of-Thought Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "User Stories": 0.78,
    "Prompt Design": 0.77,
    "Chain-of-Thought Reasoning": 0.79
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
        "rationale": "A key technology used in the study, linking to broader discussions on AI and NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "User Stories",
        "canonical": "User Stories",
        "aliases": [
          "User Requirements"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's investigation, connecting to software engineering practices.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Prompt Design",
        "canonical": "Prompt Design",
        "aliases": [
          "Prompt Engineering"
        ],
        "category": "unique_technical",
        "rationale": "Critical for understanding how LLMs are applied in the study, linking to AI model optimization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT"
        ],
        "category": "specific_connectable",
        "rationale": "A specific reasoning strategy evaluated in the study, connecting to cognitive approaches in AI.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "legacy systems",
      "annotated snippets"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "User Stories",
      "resolved_canonical": "User Stories",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Prompt Design",
      "resolved_canonical": "Prompt Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Reverse Engineering User Stories from Code using Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19587.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19587](https://arxiv.org/abs/2509.19587)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (87.8% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (87.0% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (86.2% similar)
- [[2025-09-24/Actions Speak Louder than Prompts_ A Large-Scale Study of LLMs for Graph Inference_20250924|Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference]] (86.0% similar)
- [[2025-09-24/Evaluating Large Language Models for Detecting Antisemitism_20250924|Evaluating Large Language Models for Detecting Antisemitism]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]]
**⚡ Unique Technical**: [[keywords/User Stories|User Stories]], [[keywords/Prompt Design|Prompt Design]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19587v1 Announce Type: cross 
Abstract: User stories are essential in agile development, yet often missing or outdated in legacy and poorly documented systems. We investigate whether large language models (LLMs) can automatically recover user stories directly from source code and how prompt design impacts output quality. Using 1,750 annotated C++ snippets of varying complexity, we evaluate five state-of-the-art LLMs across six prompting strategies. Results show that all models achieve, on average, an F1 score of 0.8 for code up to 200 NLOC. Our findings show that a single illustrative example enables the smallest model (8B) to match the performance of a much larger 70B model. In contrast, structured reasoning via Chain-of-Thought offers only marginal gains, primarily for larger models.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)이 소스 코드에서 사용자 스토리를 자동으로 복구할 수 있는지를 조사합니다. 1,750개의 C++ 코드 스니펫을 사용하여 다섯 가지 최첨단 LLM과 여섯 가지 프롬프트 전략을 평가한 결과, 모든 모델이 평균 F1 점수 0.8을 기록했습니다. 특히, 단일 예시만으로도 작은 모델(8B)이 큰 모델(70B)과 유사한 성능을 보였으며, Chain-of-Thought와 같은 구조적 추론은 주로 큰 모델에서만 약간의 성능 향상을 제공했습니다. 이 연구는 LLM을 활용한 사용자 스토리 복구의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 소스 코드에서 사용자 스토리를 자동으로 복구할 수 있으며, 프롬프트 설계가 출력 품질에 영향을 미친다.
- 2. 1,750개의 다양한 복잡도의 C++ 코드 스니펫을 사용하여 5개의 최신 LLM을 6가지 프롬프트 전략으로 평가하였다.
- 3. 모든 모델은 평균적으로 200 NLOC 이하의 코드에서 F1 점수 0.8을 달성하였다.
- 4. 단일 예시를 통해 가장 작은 모델(8B)이 훨씬 큰 모델(70B)의 성능을 맞출 수 있음을 발견하였다.
- 5. Chain-of-Thought를 통한 구조적 추론은 주로 큰 모델에서만 약간의 성능 향상을 제공하였다.


---

*Generated on 2025-09-25 15:39:06*