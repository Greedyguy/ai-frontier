---
keywords:
  - Large Language Model
  - Mathematical Reasoning
  - Chain-of-Thought Prompting
  - Overfitting in Contextual Learning
  - Corrective Rationales
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.08550
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:45:58.406502",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Mathematical Reasoning",
    "Chain-of-Thought Prompting",
    "Overfitting in Contextual Learning",
    "Corrective Rationales"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Mathematical Reasoning": 0.7,
    "Chain-of-Thought Prompting": 0.78,
    "Overfitting in Contextual Learning": 0.72,
    "Corrective Rationales": 0.75
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
        "rationale": "Central to the paper's focus on learning dynamics without explicit rationales.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "math reasoning tasks",
        "canonical": "Mathematical Reasoning",
        "aliases": [
          "math reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Specific task type explored for LLM performance improvements.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "chain-of-thought prompting",
        "canonical": "Chain-of-Thought Prompting",
        "aliases": [
          "CoT prompting"
        ],
        "category": "specific_connectable",
        "rationale": "A specific prompting strategy compared against in the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "overfitting to in-context rationales",
        "canonical": "Overfitting in Contextual Learning",
        "aliases": [
          "overfitting to rationales"
        ],
        "category": "unique_technical",
        "rationale": "Describes a key limitation observed in the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "corrective rationales",
        "canonical": "Corrective Rationales",
        "aliases": [
          "rationales",
          "correction rationales"
        ],
        "category": "specific_connectable",
        "rationale": "Central concept in evaluating LLM learning without explicit feedback.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "evaluations",
      "context length"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "math reasoning tasks",
      "resolved_canonical": "Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "chain-of-thought prompting",
      "resolved_canonical": "Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "overfitting to in-context rationales",
      "resolved_canonical": "Overfitting in Contextual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "corrective rationales",
      "resolved_canonical": "Corrective Rationales",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# No Need for Explanations: LLMs can implicitly learn from mistakes in-context

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.08550.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.08550](https://arxiv.org/abs/2502.08550)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.8% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (86.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.9% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.7% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Prompting|Chain-of-Thought Prompting]], [[keywords/Corrective Rationales|Corrective Rationales]]
**⚡ Unique Technical**: [[keywords/Mathematical Reasoning|Mathematical Reasoning]], [[keywords/Overfitting in Contextual Learning|Overfitting in Contextual Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.08550v3 Announce Type: replace-cross 
Abstract: Showing incorrect answers to Large Language Models (LLMs) is a popular strategy to improve their performance in reasoning-intensive tasks. It is widely assumed that, in order to be helpful, the incorrect answers must be accompanied by comprehensive rationales, explicitly detailing where the mistakes are and how to correct them. However, in this work we present a counterintuitive finding: we observe that LLMs perform better in math reasoning tasks when these rationales are eliminated from the context and models are left to infer on their own what makes an incorrect answer flawed. This approach also substantially outperforms chain-of-thought prompting in our evaluations. These results are consistent across LLMs of different sizes and varying reasoning abilities. To gain an understanding of why LLMs learn from mistakes more effectively without explicit corrective rationales, we perform a thorough analysis, investigating changes in context length and answer diversity between different prompting strategies, and their effect on performance. We also examine evidence of overfitting to the in-context rationales when these are provided, and study the extent to which LLMs are able to autonomously infer high-quality corrective rationales given only incorrect answers as input. We find evidence that, while incorrect answers are more beneficial for LLM learning than additional diverse correct answers, explicit corrective rationales over-constrain the model, thus limiting those benefits.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 성능 향상을 위해 잘못된 답변을 제시하는 전략을 연구합니다. 일반적으로 잘못된 답변은 오류를 설명하고 수정 방법을 제시하는 논리와 함께 제공되어야 한다고 생각되지만, 이 연구는 반대로 논리 없이 잘못된 답변만 제공할 때 수학적 추론 과제에서 더 나은 성능을 보인다는 발견을 제시합니다. 이러한 접근법은 다양한 크기와 추론 능력을 가진 LLM에서 일관된 성과를 보이며, 체인 오브 쏘트 프롬팅보다 우수한 결과를 나타냈습니다. 연구는 명시적인 논리가 모델의 과적합을 초래할 수 있음을 시사하며, LLM이 잘못된 답변만으로도 스스로 높은 품질의 수정 논리를 추론할 수 있는 능력을 탐구합니다. 잘못된 답변이 다양한 올바른 답변보다 학습에 더 유익하다는 증거도 발견되었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 수학적 추론 작업에서 명시적인 설명 없이 잘못된 답변만 제공될 때 더 나은 성능을 보인다.
- 2. 잘못된 답변에 대한 명시적인 설명이 없을 때, LLM의 성능이 향상되며 이는 다양한 크기와 추론 능력을 가진 모델에서도 일관되게 나타난다.
- 3. 명시적인 설명이 제공되면 LLM이 과적합될 가능성이 있으며, 이는 모델의 학습 효과를 제한한다.
- 4. 잘못된 답변만을 입력으로 제공받은 LLM은 고품질의 수정 설명을 자율적으로 추론할 수 있는 능력을 가지고 있다.
- 5. 잘못된 답변은 다양한 올바른 답변보다 LLM 학습에 더 유익하다.


---

*Generated on 2025-09-24 00:45:58*