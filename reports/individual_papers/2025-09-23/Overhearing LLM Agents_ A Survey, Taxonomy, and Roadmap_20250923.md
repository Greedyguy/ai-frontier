---
keywords:
  - Overhearing Agents
  - Human-AI Interaction
  - Large Language Model
  - Contextual Assistance
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16325
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:14:04.530883",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Overhearing Agents",
    "Human-AI Interaction",
    "Large Language Model",
    "Contextual Assistance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Overhearing Agents": 0.78,
    "Human-AI Interaction": 0.72,
    "Large Language Model": 0.8,
    "Contextual Assistance": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "overhearing agents",
        "canonical": "Overhearing Agents",
        "aliases": [
          "ambient agents",
          "contextual agents"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel interaction paradigm with LLMs that can be linked to future research in human-AI interaction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "human-AI interaction",
        "canonical": "Human-AI Interaction",
        "aliases": [
          "HCI",
          "human-computer interaction"
        ],
        "category": "broad_technical",
        "rationale": "Provides a foundational concept for linking various studies on AI systems and their interaction with humans.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study of overhearing agents and provides a basis for linking to other AI research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "contextual assistance",
        "canonical": "Contextual Assistance",
        "aliases": [
          "context-aware help",
          "ambient assistance"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking studies on AI providing assistance without direct interaction.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "task",
      "system",
      "interaction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "overhearing agents",
      "resolved_canonical": "Overhearing Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "human-AI interaction",
      "resolved_canonical": "Human-AI Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "contextual assistance",
      "resolved_canonical": "Contextual Assistance",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Overhearing LLM Agents: A Survey, Taxonomy, and Roadmap

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16325.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16325](https://arxiv.org/abs/2509.16325)

## 🔗 유사한 논문
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era: A Survey]] (83.2% similar)
- [[2025-09-19/Ask-to-Clarify_ Resolving Instruction Ambiguity through Multi-turn Dialogue_20250919|Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue]] (82.5% similar)
- [[2025-09-19/OnlineMate_ An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning_20250919|OnlineMate: An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (82.2% similar)
- [[2025-09-22/Using Natural Language for Human-Robot Collaboration in the Real World_20250922|Using Natural Language for Human-Robot Collaboration in the Real World]] (82.0% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Human-AI Interaction|Human-AI Interaction]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Contextual Assistance|Contextual Assistance]]
**⚡ Unique Technical**: [[keywords/Overhearing Agents|Overhearing Agents]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16325v1 Announce Type: cross 
Abstract: Imagine AI assistants that enhance conversations without interrupting them: quietly providing relevant information during a medical consultation, seamlessly preparing materials as teachers discuss lesson plans, or unobtrusively scheduling meetings as colleagues debate calendars. While modern conversational LLM agents directly assist human users with tasks through a chat interface, we study this alternative paradigm for interacting with LLM agents, which we call "overhearing agents." Rather than demanding the user's attention, overhearing agents continuously monitor ambient activity and intervene only when they can provide contextual assistance. In this paper, we present the first analysis of overhearing LLM agents as a distinct paradigm in human-AI interaction and establish a taxonomy of overhearing agent interactions and tasks grounded in a survey of works on prior LLM-powered agents and exploratory HCI studies. Based on this taxonomy, we create a list of best practices for researchers and developers building overhearing agent systems. Finally, we outline the remaining research gaps and reveal opportunities for future research in the overhearing paradigm.

## 📝 요약

이 논문은 대화에 방해를 주지 않으면서 정보를 제공하는 "overhearing agents"라는 새로운 AI 상호작용 패러다임을 제시합니다. 기존의 대화형 LLM 에이전트와 달리, 이 에이전트는 사용자의 주의를 끌지 않고 주변 활동을 모니터링하며 필요할 때만 개입합니다. 논문은 이러한 에이전트의 상호작용과 과제를 분류하고, 이를 기반으로 연구자와 개발자를 위한 모범 사례를 제시합니다. 또한, 이 패러다임의 연구 격차와 향후 연구 기회를 탐색합니다.

## 🎯 주요 포인트

- 1. "Overhearing agents"는 사용자의 주의를 끌지 않고 대화 중 필요한 정보를 제공하는 AI 보조 시스템을 의미합니다.
- 2. 이 논문은 인간-AI 상호작용에서 "overhearing agents"라는 새로운 패러다임을 분석한 최초의 연구입니다.
- 3. "Overhearing agents"의 상호작용 및 작업에 대한 분류 체계를 수립하고, 이를 기반으로 최적의 개발 관행을 제시합니다.
- 4. 기존 LLM 기반 에이전트와 HCI 연구를 조사하여 "overhearing agents"의 가능성과 연구 기회를 제시합니다.


---

*Generated on 2025-09-23 23:14:04*