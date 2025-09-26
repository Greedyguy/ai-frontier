---
keywords:
  - Conversational Responsivity
  - Large Language Model
  - Semantic Similarity
  - Human-Annotated Conversations
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16464
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:12:33.700995",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Conversational Responsivity",
    "Large Language Model",
    "Semantic Similarity",
    "Human-Annotated Conversations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Conversational Responsivity": 0.8,
    "Large Language Model": 0.85,
    "Semantic Similarity": 0.7,
    "Human-Annotated Conversations": 0.6
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "responsivity",
        "canonical": "Conversational Responsivity",
        "aliases": [
          "response quality",
          "dialogue responsivity"
        ],
        "category": "unique_technical",
        "rationale": "Responsivity is a unique concept central to the paper's analysis of dialogue quality.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a key technology used in the paper's methodology for analyzing dialogue.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "semantic similarity",
        "canonical": "Semantic Similarity",
        "aliases": [
          "meaning similarity",
          "semantic relatedness"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic similarity is a critical measure used to quantify responsivity in dialogues.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "human-annotated conversations",
        "canonical": "Human-Annotated Conversations",
        "aliases": [
          "annotated dialogues",
          "human-labeled conversations"
        ],
        "category": "unique_technical",
        "rationale": "These serve as the ground truth for evaluating the methods proposed in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.6
      }
    ],
    "ban_list_suggestions": [
      "method",
      "evaluate",
      "ground truth"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "responsivity",
      "resolved_canonical": "Conversational Responsivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
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
      "candidate_surface": "semantic similarity",
      "resolved_canonical": "Semantic Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "human-annotated conversations",
      "resolved_canonical": "Human-Annotated Conversations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.6
      }
    }
  ]
}
-->

# Computational Analysis of Conversation Dynamics through Participant Responsivity

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16464.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16464](https://arxiv.org/abs/2509.16464)

## 🔗 유사한 논문
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era: A Survey]] (82.9% similar)
- [[2025-09-23/Evaluating Behavioral Alignment in Conflict Dialogue_ A Multi-Dimensional Comparison of LLM Agents and Humans_20250923|Evaluating Behavioral Alignment in Conflict Dialogue: A Multi-Dimensional Comparison of LLM Agents and Humans]] (81.4% similar)
- [[2025-09-23/SENSE-7_ Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations_20250923|SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations]] (81.2% similar)
- [[2025-09-19/Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (81.1% similar)
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Similarity|Semantic Similarity]]
**⚡ Unique Technical**: [[keywords/Conversational Responsivity|Conversational Responsivity]], [[keywords/Human-Annotated Conversations|Human-Annotated Conversations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16464v1 Announce Type: new 
Abstract: Growing literature explores toxicity and polarization in discourse, with comparatively less work on characterizing what makes dialogue prosocial and constructive. We explore conversational discourse and investigate a method for characterizing its quality built upon the notion of ``responsivity'' -- whether one person's conversational turn is responding to a preceding turn. We develop and evaluate methods for quantifying responsivity -- first through semantic similarity of speaker turns, and second by leveraging state-of-the-art large language models (LLMs) to identify the relation between two speaker turns. We evaluate both methods against a ground truth set of human-annotated conversations. Furthermore, selecting the better performing LLM-based approach, we characterize the nature of the response -- whether it responded to that preceding turn in a substantive way or not.
  We view these responsivity links as a fundamental aspect of dialogue but note that conversations can exhibit significantly different responsivity structures. Accordingly, we then develop conversation-level derived metrics to address various aspects of conversational discourse. We use these derived metrics to explore other conversations and show that they support meaningful characterizations and differentiations across a diverse collection of conversations.

## 📝 요약

이 논문은 대화의 질을 평가하는 방법으로 "응답성" 개념을 탐구합니다. 응답성은 한 사람의 대화가 이전 발언에 얼마나 잘 반응하는지를 나타냅니다. 연구진은 먼저 화자의 발언 간 의미적 유사성을 통해, 그리고 최신 대형 언어 모델(LLM)을 활용하여 두 발언 간 관계를 파악하는 방법으로 응답성을 정량화했습니다. 이 방법들은 인간이 주석한 대화 데이터와 비교하여 평가되었습니다. LLM 기반 방법이 더 우수하다고 판단되어, 발언이 이전 발언에 실질적으로 반응했는지를 분석했습니다. 연구는 대화의 응답성 구조가 다양할 수 있음을 지적하며, 이를 기반으로 대화 수준의 파생 지표를 개발하여 다양한 대화를 의미 있게 구분할 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. 대화의 질을 평가하기 위해 "responsivity" 개념을 기반으로 한 방법을 탐구합니다.
- 2. 발화의 의미적 유사성과 최신 대형 언어 모델(LLMs)을 활용하여 responsivity를 정량화하는 방법을 개발하고 평가합니다.
- 3. 인간이 주석을 단 대화의 실제 데이터와 비교하여 두 가지 방법을 평가합니다.
- 4. 더 나은 성능을 보인 LLM 기반 접근법을 통해 응답의 본질을 분석합니다.
- 5. 대화 수준의 파생 메트릭을 개발하여 다양한 대화의 특성을 의미 있게 구별합니다.


---

*Generated on 2025-09-24 03:12:33*