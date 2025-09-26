---
keywords:
  - Large Language Model
  - Conversational Agent
  - Knowledge-Behavior Disconnect
  - Ethical Conversational Knowledge
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20004
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:56:25.021165",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Conversational Agent",
    "Knowledge-Behavior Disconnect",
    "Ethical Conversational Knowledge"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Conversational Agent": 0.8,
    "Knowledge-Behavior Disconnect": 0.78,
    "Ethical Conversational Knowledge": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on the limitations and disconnect in chatbot behavior.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Conversational chatbot",
        "canonical": "Conversational Agent",
        "aliases": [
          "Chatbot"
        ],
        "category": "specific_connectable",
        "rationale": "Key subject of study, focusing on behavior and ethical considerations.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Knowledge-behaviour disconnect",
        "canonical": "Knowledge-Behavior Disconnect",
        "aliases": [
          "Knowledge-Behaviour Gap"
        ],
        "category": "unique_technical",
        "rationale": "Unique concept introduced in the paper to describe a fundamental limitation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Ethical conversational knowledge",
        "canonical": "Ethical Conversational Knowledge",
        "aliases": [
          "Ethical Knowledge in Chatbots"
        ],
        "category": "unique_technical",
        "rationale": "Addresses the ethical dimension of the disconnect, relevant for ethical AI discussions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Artificial conversational agents",
      "Correct answers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large language model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Conversational chatbot",
      "resolved_canonical": "Conversational Agent",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Knowledge-behaviour disconnect",
      "resolved_canonical": "Knowledge-Behavior Disconnect",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Ethical conversational knowledge",
      "resolved_canonical": "Ethical Conversational Knowledge",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# The Knowledge-Behaviour Disconnect in LLM-based Chatbots

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20004.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20004](https://arxiv.org/abs/2509.20004)

## 🔗 유사한 논문
- [[2025-09-23/"What's Up, Doc?"_ Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets_20250923|"What's Up, Doc?": Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets]] (83.2% similar)
- [[2025-09-24/Disambiguation in Conversational Question Answering in the Era of LLMs and Agents_ A Survey_20250924|Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey]] (81.8% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (81.5% similar)
- [[2025-09-22/Do Retrieval Augmented Language Models Know When They Don't Know?_20250922|Do Retrieval Augmented Language Models Know When They Don't Know?]] (81.5% similar)
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Conversational Agent|Conversational Agent]]
**⚡ Unique Technical**: [[keywords/Knowledge-Behavior Disconnect|Knowledge-Behavior Disconnect]], [[keywords/Ethical Conversational Knowledge|Ethical Conversational Knowledge]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20004v1 Announce Type: cross 
Abstract: Large language model-based artificial conversational agents (like ChatGPT) give answers to all kinds of questions, and often enough these answers are correct. Just on the basis of that capacity alone, we may attribute knowledge to them. But do these models use this knowledge as a basis for their own conversational behaviour? I argue this is not the case, and I will refer to this failure as a `disconnect'. I further argue this disconnect is fundamental in the sense that with more data and more training of the LLM on which a conversational chatbot is based, it will not disappear. The reason is, as I will claim, that the core technique used to train LLMs does not allow for the establishment of the connection we are after. The disconnect reflects a fundamental limitation on the capacities of LLMs, and explains the source of hallucinations. I will furthermore consider the ethical version of the disconnect (ethical conversational knowledge not being aligned with ethical conversational behaviour), since in this domain researchers have come up with several additional techniques to influence a chatbot's behaviour. I will discuss how these techniques do nothing to solve the disconnect and can make it worse.

## 📝 요약

이 논문은 대형 언어 모델 기반 인공지능 대화 에이전트가 지식을 보유하고 있는 것처럼 보이지만, 실제 대화에서 이를 효과적으로 활용하지 못하는 '단절' 현상을 설명합니다. 저자는 이 단절이 데이터와 훈련의 증가로 해결되지 않는 근본적인 한계라고 주장하며, 이는 LLM의 핵심 훈련 기법이 이러한 연결을 구축하지 못하기 때문이라고 설명합니다. 이러한 단절은 LLM의 환각 현상의 원인이며, 윤리적 대화 지식과 행동의 불일치 문제에서도 나타납니다. 연구자들이 개발한 추가적인 기술들이 이 문제를 해결하지 못하고 오히려 악화시킬 수 있음을 논의합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델 기반 인공지능 대화 에이전트는 다양한 질문에 대한 답변을 제공하지만, 이러한 답변이 항상 모델의 대화 행동에 반영되지는 않는다.
- 2. 이러한 '단절'은 대화형 챗봇의 기반이 되는 LLM의 데이터와 훈련이 증가해도 사라지지 않는 근본적인 문제로 제기된다.
- 3. LLM을 훈련하는 핵심 기술이 이러한 연결을 확립할 수 없기 때문에 '단절'이 발생하며, 이는 LLM의 한계를 나타내고 환각의 원인을 설명한다.
- 4. 윤리적 대화 지식과 행동 간의 단절 문제를 해결하기 위해 추가적인 기술이 개발되었으나, 이는 문제를 해결하지 못하고 오히려 악화시킬 수 있다.


---

*Generated on 2025-09-25 15:56:25*