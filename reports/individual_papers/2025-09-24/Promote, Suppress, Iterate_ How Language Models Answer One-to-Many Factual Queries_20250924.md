<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:30:14.269514",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Attention Mechanism",
    "Token Lens",
    "Causal Tracing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Attention Mechanism": 0.9,
    "Token Lens": 0.8,
    "Causal Tracing": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LM"
        ],
        "category": "broad_technical",
        "rationale": "Links to a broad category of models used in NLP and connects with other concepts like attention mechanisms.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's mechanism of promoting and suppressing tokens, linking to many related concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Token Lens",
        "canonical": "Token Lens",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel method introduced in the paper, providing insights into token interactions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Tracing",
        "canonical": "Causal Tracing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific technique used in the paper to analyze model behavior, offering unique insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
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
      "candidate_surface": "Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Token Lens",
      "resolved_canonical": "Token Lens",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Tracing",
      "resolved_canonical": "Causal Tracing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.20475.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2502.20475](https://arxiv.org/abs/2502.20475)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (83.9% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (83.8% similar)
- [[2025-09-22/Efficient Real-time Refinement of Language Model Text Generation_20250922|Efficient Real-time Refinement of Language Model Text Generation]] (83.7% similar)
- [[2025-09-23/Adaptive Distraction_ Probing LLM Contextual Robustness with Automated Tree Search_20250923|Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search]] (83.3% similar)
- [[2025-09-23/EAMET_ Robust Massive Model Editing via Embedding Alignment Optimization_20250923|EAMET: Robust Massive Model Editing via Embedding Alignment Optimization]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Token Lens|Token Lens]], [[keywords/Causal Tracing|Causal Tracing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.20475v3 Announce Type: replace-cross 
Abstract: To answer one-to-many factual queries (e.g., listing cities of a country), a language model (LM) must simultaneously recall knowledge and avoid repeating previous answers. How are these two subtasks implemented and integrated internally? Across multiple datasets, models, and prompt templates, we identify a promote-then-suppress mechanism: the model first recalls all answers, and then suppresses previously generated ones. Specifically, LMs use both the subject and previous answer tokens to perform knowledge recall, with attention propagating subject information and MLPs promoting the answers. Then, attention attends to and suppresses previous answer tokens, while MLPs amplify the suppression signal. Our mechanism is corroborated by extensive experimental evidence: in addition to using early decoding and causal tracing, we analyze how components use different tokens by introducing both Token Lens, which decodes aggregated attention updates from specified tokens, and a knockout method that analyzes changes in MLP outputs after removing attention to specified tokens. Overall, we provide new insights into how LMs' internal components interact with different input tokens to support complex factual recall. Code is available at https://github.com/Lorenayannnnn/how-lms-answer-one-to-many-factual-queries.

## 📝 요약

이 논문은 언어 모델이 하나의 질문에 여러 개의 사실적 답변을 제공할 때, 지식을 회상하고 이전 답변을 반복하지 않는 방법을 탐구합니다. 연구는 '촉진 후 억제' 메커니즘을 제안하며, 모델이 먼저 모든 답변을 회상한 후 이전에 생성된 답변을 억제한다고 설명합니다. 주제와 이전 답변 토큰을 사용해 지식을 회상하고, 주의 메커니즘과 MLPs가 각각 주제 정보를 전파하고 답변을 촉진합니다. 이후 주의 메커니즘은 이전 답변 토큰을 억제하고, MLPs는 억제 신호를 강화합니다. 이 메커니즘은 다양한 실험을 통해 입증되었으며, Token Lens와 노크아웃 방법을 통해 모델의 내부 구성 요소가 입력 토큰과 상호작용하는 방식을 분석합니다. 이 연구는 복잡한 사실 회상을 지원하는 언어 모델의 내부 작동 방식에 대한 새로운 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 언어 모델은 하나의 질문에 여러 답을 제공할 때, 지식을 회상하고 이전 답변을 반복하지 않도록 억제하는 메커니즘을 사용합니다.
- 2. 모델은 주제와 이전 답변 토큰을 활용하여 지식을 회상하며, 주의 메커니즘과 MLPs가 각각 주제 정보를 전파하고 답변을 촉진합니다.
- 3. 주의 메커니즘은 이전 답변 토큰을 억제하고, MLPs는 억제 신호를 증폭하여 답변 중복을 방지합니다.
- 4. Token Lens와 노크아웃 방법을 통해 모델의 내부 구성 요소가 입력 토큰과 상호작용하는 방식을 분석하여 복잡한 사실 회상을 지원하는 방법을 제공합니다.
- 5. 본 연구는 다양한 데이터셋, 모델, 프롬프트 템플릿을 통해 언어 모델의 내부 메커니즘을 실험적으로 입증하였습니다.


---

*Generated on 2025-09-24 14:30:14*