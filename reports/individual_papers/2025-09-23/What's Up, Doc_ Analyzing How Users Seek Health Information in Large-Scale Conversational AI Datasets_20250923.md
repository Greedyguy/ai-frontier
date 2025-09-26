---
keywords:
  - Large Language Model
  - HealthChat-11K
  - Conversational AI
  - Healthcare Information
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.21532
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:10:07.897662",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "HealthChat-11K",
    "Conversational AI",
    "Healthcare Information"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "HealthChat-11K": 0.78,
    "Conversational AI": 0.8,
    "Healthcare Information": 0.77
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
        "rationale": "Large Language Models are central to the study and provide a basis for understanding user interactions in conversational AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "HealthChat-11K",
        "canonical": "HealthChat-11K",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "HealthChat-11K is a unique dataset introduced in the paper, crucial for linking specific research findings.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "conversational AI",
        "canonical": "Conversational AI",
        "aliases": [
          "chatbots"
        ],
        "category": "specific_connectable",
        "rationale": "Conversational AI is a key context for the study, linking AI technology with user interaction insights.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "healthcare information",
        "canonical": "Healthcare Information",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Healthcare Information is a central theme of the paper, linking user needs with AI capabilities.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "interactive chatbots",
      "real-world conversations",
      "user messages"
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
      "candidate_surface": "HealthChat-11K",
      "resolved_canonical": "HealthChat-11K",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "conversational AI",
      "resolved_canonical": "Conversational AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "healthcare information",
      "resolved_canonical": "Healthcare Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# "What's Up, Doc?": Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.21532.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.21532](https://arxiv.org/abs/2506.21532)

## 🔗 유사한 논문
- [[2025-09-23/From Chat Logs to Collective Insights_ Aggregative Question Answering_20250923|From Chat Logs to Collective Insights: Aggregative Question Answering]] (84.3% similar)
- [[2025-09-23/A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents_20250923|A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents]] (82.8% similar)
- [[2025-09-23/SouLLMate_ An Application Enhancing Diverse Mental Health Support with Adaptive LLMs, Prompt Engineering, and RAG Techniques_20250923|SouLLMate: An Application Enhancing Diverse Mental Health Support with Adaptive LLMs, Prompt Engineering, and RAG Techniques]] (82.2% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (82.1% similar)
- [[2025-09-18/Can I Trust This Chatbot? Assessing User Privacy in AI-Healthcare Chatbot Applications_20250918|Can I Trust This Chatbot? Assessing User Privacy in AI-Healthcare Chatbot Applications]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Conversational AI|Conversational AI]], [[keywords/Healthcare Information|Healthcare Information]]
**⚡ Unique Technical**: [[keywords/HealthChat-11K|HealthChat-11K]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.21532v3 Announce Type: replace-cross 
Abstract: People are increasingly seeking healthcare information from large language models (LLMs) via interactive chatbots, yet the nature and inherent risks of these conversations remain largely unexplored. In this paper, we filter large-scale conversational AI datasets to achieve HealthChat-11K, a curated dataset of 11K real-world conversations composed of 25K user messages. We use HealthChat-11K and a clinician-driven taxonomy for how users interact with LLMs when seeking healthcare information in order to systematically study user interactions across 21 distinct health specialties. Our analysis reveals insights into the nature of how and why users seek health information, such as common interactions, instances of incomplete context, affective behaviors, and interactions (e.g., leading questions) that can induce sycophancy, underscoring the need for improvements in the healthcare support capabilities of LLMs deployed as conversational AI. Code and artifacts to retrieve our analyses and combine them into a curated dataset can be found here: https://github.com/yahskapar/HealthChat

## 📝 요약

이 논문은 대화형 챗봇을 통해 대형 언어 모델(LLM)로부터 건강 정보를 얻는 사용자 상호작용의 본질과 위험성을 탐구합니다. 연구진은 대규모 대화형 AI 데이터셋을 필터링하여 11,000개의 실제 대화를 포함한 HealthChat-11K 데이터셋을 구축했습니다. 이를 통해 21개 건강 분야에서 사용자가 LLM과 상호작용하는 방식을 체계적으로 분석했습니다. 분석 결과, 사용자들이 건강 정보를 찾는 방식과 이유, 불완전한 맥락, 감정적 행동, 아첨을 유도할 수 있는 상호작용의 사례 등이 밝혀졌습니다. 이는 대화형 AI로서 LLM의 의료 지원 기능 개선 필요성을 강조합니다. 연구 결과와 데이터셋은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. HealthChat-11K는 11,000개의 실제 대화와 25,000개의 사용자 메시지로 구성된 데이터셋으로, 대규모 대화형 AI 데이터셋을 필터링하여 구축되었습니다.
- 2. 사용자가 대화형 AI를 통해 건강 정보를 찾는 방식과 이유를 체계적으로 연구하기 위해 21개의 건강 전문 분야에 걸쳐 사용자 상호작용을 분석했습니다.
- 3. 분석 결과, 불완전한 맥락, 감정적 행동, 아첨을 유도할 수 있는 상호작용 등 사용자가 건강 정보를 찾는 일반적인 상호작용의 특성을 밝혀냈습니다.
- 4. 대화형 AI로서의 LLM의 의료 지원 기능 개선 필요성을 강조했습니다.
- 5. 연구 분석 결과와 데이터셋은 GitHub에서 확인할 수 있습니다: https://github.com/yahskapar/HealthChat


---

*Generated on 2025-09-24 01:10:07*