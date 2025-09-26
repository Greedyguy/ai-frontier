---
keywords:
  - Large Language Model
  - Offline Evaluation
  - Personalization in AI
  - Field Evaluation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19364
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:30:28.249805",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Offline Evaluation",
    "Personalization in AI",
    "Field Evaluation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Offline Evaluation": 0.75,
    "Personalization in AI": 0.8,
    "Field Evaluation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on model behavior and personalization.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "offline evaluations",
        "canonical": "Offline Evaluation",
        "aliases": [
          "offline assessment",
          "static evaluation"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific evaluation method critiqued in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "personalization",
        "canonical": "Personalization in AI",
        "aliases": [
          "user-specific adaptation",
          "customization"
        ],
        "category": "evolved_concepts",
        "rationale": "Key concept affecting model behavior as discussed in the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "field evaluations",
        "canonical": "Field Evaluation",
        "aliases": [
          "real-world testing",
          "practical evaluation"
        ],
        "category": "unique_technical",
        "rationale": "Contrasts with offline evaluations to show real-world model performance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "state-less",
      "benchmark questions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "language models",
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
      "candidate_surface": "offline evaluations",
      "resolved_canonical": "Offline Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "personalization",
      "resolved_canonical": "Personalization in AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "field evaluations",
      "resolved_canonical": "Field Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# The Inadequacy of Offline LLM Evaluations: A Need to Account for Personalization in Model Behavior

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19364.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19364](https://arxiv.org/abs/2509.19364)

## 🔗 유사한 논문
- [[2025-09-25/Benchmarking and Improving LLM Robustness for Personalized Generation_20250925|Benchmarking and Improving LLM Robustness for Personalized Generation]] (84.8% similar)
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (83.9% similar)
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (83.9% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (83.0% similar)
- [[2025-09-23/Latent Inter-User Difference Modeling for LLM Personalization_20250923|Latent Inter-User Difference Modeling for LLM Personalization]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Offline Evaluation|Offline Evaluation]], [[keywords/Field Evaluation|Field Evaluation]]
**🚀 Evolved Concepts**: [[keywords/Personalization in AI|Personalization in AI]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19364v1 Announce Type: cross 
Abstract: Standard offline evaluations for language models -- a series of independent, state-less inferences made by models -- fail to capture how language models actually behave in practice, where personalization fundamentally alters model behavior. For instance, identical benchmark questions to the same language model can produce markedly different responses when prompted to a state-less system, in one user's chat session, or in a different user's chat session. In this work, we provide empirical evidence showcasing this phenomenon by comparing offline evaluations to field evaluations conducted by having 800 real users of ChatGPT and Gemini pose benchmark and other provided questions to their chat interfaces.

## 📝 요약

이 논문은 언어 모델의 표준 오프라인 평가가 실제 사용 환경에서의 모델 행동을 제대로 반영하지 못한다는 점을 지적합니다. 개인화된 사용 환경에서는 동일한 질문이라도 사용자에 따라 다른 응답을 생성할 수 있습니다. 연구진은 ChatGPT와 Gemini를 사용하는 800명의 실제 사용자로부터 수집한 데이터를 통해 오프라인 평가와 현장 평가를 비교하여 이러한 현상을 실증적으로 보여줍니다. 주요 기여는 언어 모델의 실제 사용 환경에서의 행동을 더 잘 이해하기 위한 평가 방법론의 필요성을 강조한 것입니다.

## 🎯 주요 포인트

- 1. 전통적인 오프라인 평가 방식은 언어 모델의 실제 동작 방식을 제대로 반영하지 못합니다.
- 2. 개인화가 언어 모델의 행동을 근본적으로 변화시킵니다.
- 3. 동일한 질문이라도 사용자에 따라 언어 모델의 응답이 크게 달라질 수 있습니다.
- 4. 800명의 실제 사용자와 함께한 현장 평가를 통해 이러한 현상을 실증적으로 입증했습니다.


---

*Generated on 2025-09-25 15:30:28*