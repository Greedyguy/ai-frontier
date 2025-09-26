---
keywords:
  - Large Language Model
  - Asynchronous Communication
  - Mafia Games
  - Adaptive Asynchronous LLM Agent
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.05309
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:05:58.673653",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Asynchronous Communication",
    "Mafia Games",
    "Adaptive Asynchronous LLM Agent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Asynchronous Communication": 0.78,
    "Mafia Games": 0.77,
    "Adaptive Asynchronous LLM Agent": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus and connect well with existing literature on AI communication.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "asynchronous communication",
        "canonical": "Asynchronous Communication",
        "aliases": [
          "async communication"
        ],
        "category": "unique_technical",
        "rationale": "The concept of asynchronous communication is crucial for understanding the novel application of LLMs in this context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mafia games",
        "canonical": "Mafia Games",
        "aliases": [
          "Mafia game",
          "social deduction games"
        ],
        "category": "unique_technical",
        "rationale": "Mafia games serve as the experimental setting, providing a unique context for the study of LLMs in social interactions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "adaptive asynchronous LLM agent",
        "canonical": "Adaptive Asynchronous LLM Agent",
        "aliases": [
          "adaptive LLM agent"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel agent architecture proposed in the paper, crucial for understanding the implementation and results.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "synchronous communication",
      "game performance metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM",
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
      "candidate_surface": "asynchronous communication",
      "resolved_canonical": "Asynchronous Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mafia games",
      "resolved_canonical": "Mafia Games",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "adaptive asynchronous LLM agent",
      "resolved_canonical": "Adaptive Asynchronous LLM Agent",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Time to Talk: LLM Agents for Asynchronous Group Communication in Mafia Games

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.05309.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.05309](https://arxiv.org/abs/2506.05309)

## 🔗 유사한 논문
- [[2025-09-18/Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem_20250918|Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem]] (85.8% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (85.2% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (85.1% similar)
- [[2025-09-19/OnlineMate_ An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning_20250919|OnlineMate: An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (84.9% similar)
- [[2025-09-23/Overhearing LLM Agents_ A Survey, Taxonomy, and Roadmap_20250923|Overhearing LLM Agents: A Survey, Taxonomy, and Roadmap]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Asynchronous Communication|Asynchronous Communication]], [[keywords/Mafia Games|Mafia Games]], [[keywords/Adaptive Asynchronous LLM Agent|Adaptive Asynchronous LLM Agent]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.05309v2 Announce Type: replace-cross 
Abstract: LLMs are used predominantly in synchronous communication, where a human user and a model communicate in alternating turns. In contrast, many real-world settings are asynchronous. For example, in group chats, online team meetings, or social games, there is no inherent notion of turns. In this work, we develop an adaptive asynchronous LLM agent consisting of two modules: a generator that decides what to say, and a scheduler that decides when to say it. To evaluate our agent, we collect a unique dataset of online Mafia games, where our agent plays with human participants. Overall, our agent performs on par with human players, both in game performance metrics and in its ability to blend in with the other human players. Our analysis shows that the agent's behavior in deciding when to speak closely mirrors human patterns, although differences emerge in message content. We make all of our code and data publicly available. This work paves the way for integration of LLMs into realistic human group settings, from assistance in team discussions to educational and professional environments where complex social dynamics must be navigated.

## 📝 요약

이 연구는 비동기적 환경에서 작동하는 적응형 LLM 에이전트를 개발했습니다. 에이전트는 발화 내용을 결정하는 생성기와 발화 시점을 결정하는 스케줄러로 구성됩니다. 온라인 마피아 게임 데이터를 통해 평가한 결과, 에이전트는 게임 성능과 인간 참가자와의 융화 능력에서 인간 플레이어와 유사한 성과를 보였습니다. 특히 발화 시점 결정에서 인간과 유사한 패턴을 보였으나, 메시지 내용에서는 차이가 있었습니다. 이 연구는 팀 회의나 교육, 전문 환경에서 LLM의 활용 가능성을 제시합니다. 모든 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 연구에서는 비동기적 환경에서 작동하는 적응형 비동기 LLM 에이전트를 개발하였다.
- 2. 에이전트는 무엇을 말할지 결정하는 생성기와 언제 말할지 결정하는 스케줄러로 구성되어 있다.
- 3. 온라인 마피아 게임 데이터셋을 통해 에이전트의 성능을 평가했으며, 인간 참가자와 유사한 성과를 보였다.
- 4. 에이전트의 발언 시점 결정은 인간의 패턴과 유사하지만, 메시지 내용에서는 차이가 나타났다.
- 5. 이 연구는 팀 토론 지원부터 복잡한 사회적 역학을 다루는 교육 및 전문 환경까지 LLM의 현실적 인간 그룹 환경 통합 가능성을 제시한다.


---

*Generated on 2025-09-24 01:05:58*