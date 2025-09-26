---
keywords:
  - Belief-Desire-Intention Framework
  - Alternating-Time Temporal Logic
  - Plan Generation
  - Agent Collaboration
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15238
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:47:53.152622",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Belief-Desire-Intention Framework",
    "Alternating-Time Temporal Logic",
    "Plan Generation",
    "Agent Collaboration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Belief-Desire-Intention Framework": 0.78,
    "Alternating-Time Temporal Logic": 0.8,
    "Plan Generation": 0.7,
    "Agent Collaboration": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Belief-Desire-Intention",
        "canonical": "Belief-Desire-Intention Framework",
        "aliases": [
          "BDI",
          "BDI Agents"
        ],
        "category": "unique_technical",
        "rationale": "The BDI framework is central to the paper's methodology and is a unique approach to modeling agents.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Alternating-Time Temporal Logic",
        "canonical": "Alternating-Time Temporal Logic",
        "aliases": [
          "ATL"
        ],
        "category": "unique_technical",
        "rationale": "ATL is a specific logic used for plan generation in multi-agent systems, crucial for understanding the paper's contribution.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Plan Generation",
        "canonical": "Plan Generation",
        "aliases": [
          "Planning"
        ],
        "category": "broad_technical",
        "rationale": "Plan generation is a core concept in the paper, linking it to broader discussions in AI planning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Agent Collaboration",
        "canonical": "Agent Collaboration",
        "aliases": [
          "Collaborative Agents"
        ],
        "category": "specific_connectable",
        "rationale": "Collaboration among agents is a key aspect of the paper's approach, relevant to multi-agent systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
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
      "candidate_surface": "Belief-Desire-Intention",
      "resolved_canonical": "Belief-Desire-Intention Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Alternating-Time Temporal Logic",
      "resolved_canonical": "Alternating-Time Temporal Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Plan Generation",
      "resolved_canonical": "Plan Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Agent Collaboration",
      "resolved_canonical": "Agent Collaboration",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Generating Plans for Belief-Desire-Intention (BDI) Agents Using Alternating-Time Temporal Logic (ATL)

**Korean Title:** 신념-욕구-의도(BDI) 에이전트를 위한 계획 생성: 교대 시간 선형 논리(ATL) 사용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15238.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15238](https://arxiv.org/abs/2509.15238)

## 🔗 유사한 논문
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (80.2% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent]] (79.6% similar)
- [[2025-09-19/ATLANTIS_ AI-driven Threat Localization, Analysis, and Triage Intelligence System_20250919|ATLANTIS: AI-driven Threat Localization, Analysis, and Triage Intelligence System]] (78.4% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities: A Psychometric Approach]] (78.0% similar)
- [[2025-09-18/Meta-Optimization and Program Search using Language Models for Task and Motion Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Plan Generation|Plan Generation]]
**🔗 Specific Connectable**: [[keywords/Agent Collaboration|Agent Collaboration]]
**⚡ Unique Technical**: [[keywords/Belief-Desire-Intention Framework|Belief-Desire-Intention Framework]], [[keywords/Alternating-Time Temporal Logic|Alternating-Time Temporal Logic]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15238v1 Announce Type: cross 
Abstract: Belief-Desire-Intention (BDI) is a framework for modelling agents based on their beliefs, desires, and intentions. Plans are a central component of BDI agents, and define sequences of actions that an agent must undertake to achieve a certain goal. Existing approaches to plan generation often require significant manual effort, and are mainly focused on single-agent systems. As a result, in this work, we have developed a tool that automatically generates BDI plans using Alternating-Time Temporal Logic (ATL). By using ATL, the plans generated accommodate for possible competition or cooperation between the agents in the system. We demonstrate the effectiveness of the tool by generating plans for an illustrative game that requires agent collaboration to achieve a shared goal. We show that the generated plans allow the agents to successfully attain this goal.

## 🔍 Abstract (한글 번역)

arXiv:2509.15238v1 발표 유형: 교차  
초록: 믿음-욕구-의도(Belief-Desire-Intention, BDI)는 에이전트를 그들의 믿음, 욕구, 의도를 기반으로 모델링하는 프레임워크입니다. 계획은 BDI 에이전트의 중심 구성 요소로, 특정 목표를 달성하기 위해 에이전트가 수행해야 하는 일련의 행동을 정의합니다. 기존의 계획 생성 접근 방식은 종종 상당한 수작업을 요구하며, 주로 단일 에이전트 시스템에 초점을 맞추고 있습니다. 이에 따라 본 연구에서는 교대 시간 논리(Alternating-Time Temporal Logic, ATL)를 사용하여 BDI 계획을 자동으로 생성하는 도구를 개발하였습니다. ATL을 사용함으로써 생성된 계획은 시스템 내 에이전트 간의 경쟁 또는 협력을 고려할 수 있습니다. 우리는 에이전트 협력이 필요한 공유 목표를 달성하기 위한 예시 게임의 계획을 생성함으로써 도구의 효과성을 입증합니다. 생성된 계획이 에이전트가 이 목표를 성공적으로 달성할 수 있도록 함을 보여줍니다.

## 📝 요약

이 논문은 BDI(신념-욕구-의도) 프레임워크를 기반으로 에이전트의 계획을 자동 생성하는 도구를 개발했습니다. 기존의 계획 생성은 주로 단일 에이전트 시스템에 초점을 맞추고 수작업이 많이 필요했으나, 이 연구에서는 ATL(교대 시간 논리)을 활용하여 다중 에이전트 간의 경쟁 및 협력을 고려한 계획을 자동으로 생성합니다. 이를 통해 에이전트가 협력하여 공동 목표를 달성하는 게임에서 효과적으로 계획을 생성할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. BDI는 에이전트의 믿음, 욕구, 의도를 기반으로 모델링하는 프레임워크이다.
- 2. 기존의 계획 생성 방법은 주로 단일 에이전트 시스템에 집중되어 있으며, 많은 수작업이 필요하다.
- 3. 본 연구에서는 ATL을 사용하여 자동으로 BDI 계획을 생성하는 도구를 개발하였다.
- 4. ATL을 활용함으로써 에이전트 간의 경쟁 또는 협력을 고려한 계획 생성을 가능하게 한다.
- 5. 개발된 도구는 에이전트 협력이 필요한 게임에서 공동 목표를 성공적으로 달성할 수 있는 계획을 생성함을 보여준다.


---

*Generated on 2025-09-23 08:47:53*