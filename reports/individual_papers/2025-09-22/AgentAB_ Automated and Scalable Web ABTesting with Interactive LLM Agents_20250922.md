---
keywords:
  - A/B Testing
  - Large Language Model Agents
  - User Interaction Simulation
  - Between-Subject A/B Testing
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2504.09723
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:52:29.441258",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "A/B Testing",
    "Large Language Model Agents",
    "User Interaction Simulation",
    "Between-Subject A/B Testing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "A/B Testing": 0.82,
    "Large Language Model Agents": 0.88,
    "User Interaction Simulation": 0.79,
    "Between-Subject A/B Testing": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "A/B testing",
        "canonical": "A/B Testing",
        "aliases": [
          "AB Testing",
          "Split Testing"
        ],
        "category": "unique_technical",
        "rationale": "A/B Testing is central to the paper's focus on evaluating UI/UX design decisions and is a key concept in web experimentation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "LLM Agents",
        "canonical": "Large Language Model Agents",
        "aliases": [
          "LLM Agents"
        ],
        "category": "specific_connectable",
        "rationale": "LLM Agents are a novel application of Large Language Models for simulating user interactions, which is a core innovation of the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "user interaction behaviors",
        "canonical": "User Interaction Simulation",
        "aliases": [
          "User Behavior Simulation"
        ],
        "category": "unique_technical",
        "rationale": "Simulating user interactions is a unique technical approach that differentiates the proposed method from traditional A/B testing.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.83,
        "link_intent_score": 0.79
      },
      {
        "surface": "between-subject A/B testing",
        "canonical": "Between-Subject A/B Testing",
        "aliases": [
          "Between-Subject Testing"
        ],
        "category": "unique_technical",
        "rationale": "This specific type of A/B testing is crucial for understanding the experimental setup used in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "experiment",
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "A/B testing",
      "resolved_canonical": "A/B Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "LLM Agents",
      "resolved_canonical": "Large Language Model Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "user interaction behaviors",
      "resolved_canonical": "User Interaction Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.83,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "between-subject A/B testing",
      "resolved_canonical": "Between-Subject A/B Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AgentA/B: Automated and Scalable Web A/BTesting with Interactive LLM Agents

**Korean Title:** 에이전트A/B: 상호작용형 LLM 에이전트를 활용한 자동화 및 확장 가능한 웹 A/B 테스트

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.09723.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2504.09723](https://arxiv.org/abs/2504.09723)

## 🔗 유사한 논문
- [[2025-09-22/UXAgent_ A System for Simulating Usability Testing of Web Design with LLM Agents_20250922|UXAgent: A System for Simulating Usability Testing of Web Design with LLM Agents]] (89.7% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (85.4% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities: A Psychometric Approach]] (83.9% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (83.3% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Model Agents|Large Language Model Agents]]
**⚡ Unique Technical**: [[keywords/A/B Testing|A/B Testing]], [[keywords/User Interaction Simulation|User Interaction Simulation]], [[keywords/Between-Subject A/B Testing|Between-Subject A/B Testing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.09723v3 Announce Type: replace-cross 
Abstract: A/B testing experiment is a widely adopted method for evaluating UI/UX design decisions in modern web applications. Yet, traditional A/B testing remains constrained by its dependence on the large-scale and live traffic of human participants, and the long time of waiting for the testing result. Through formative interviews with six experienced industry practitioners, we identified critical bottlenecks in current A/B testing workflows. In response, we present AgentA/B, a novel system that leverages Large Language Model-based autonomous agents (LLM Agents) to automatically simulate user interaction behaviors with real webpages. AgentA/B enables scalable deployment of LLM agents with diverse personas, each capable of navigating the dynamic webpage and interactively executing multi-step interactions like search, clicking, filtering, and purchasing. In a demonstrative controlled experiment, we employ AgentA/B to simulate a between-subject A/B testing with 1,000 LLM agents Amazon.com, and compare agent behaviors with real human shopping behaviors at a scale. Our findings suggest AgentA/B can emulate human-like behavior patterns.

## 🔍 Abstract (한글 번역)

arXiv:2504.09723v3 발표 유형: 교차 교체  
초록: A/B 테스트 실험은 현대 웹 애플리케이션에서 UI/UX 디자인 결정을 평가하기 위해 널리 채택된 방법입니다. 그러나 전통적인 A/B 테스트는 대규모의 실시간 인간 참여자 트래픽에 의존하고, 테스트 결과를 기다리는 긴 시간에 의해 제약을 받습니다. 여섯 명의 경험 많은 업계 실무자들과의 형성적 인터뷰를 통해 현재 A/B 테스트 워크플로우에서의 주요 병목 현상을 확인했습니다. 이에 대응하여, 우리는 실시간 웹페이지와의 사용자 상호작용 행동을 자동으로 시뮬레이션하는 대규모 언어 모델 기반의 자율 에이전트(LLM 에이전트)를 활용한 새로운 시스템인 AgentA/B를 제시합니다. AgentA/B는 다양한 페르소나를 가진 LLM 에이전트를 확장 가능하게 배포할 수 있으며, 각 에이전트는 동적 웹페이지를 탐색하고 검색, 클릭, 필터링, 구매와 같은 다단계 상호작용을 상호작용적으로 실행할 수 있습니다. 시연적인 통제 실험에서, 우리는 AgentA/B를 사용하여 1,000개의 LLM 에이전트를 통한 피험자 간 A/B 테스트를 Amazon.com에서 시뮬레이션하고, 에이전트 행동을 대규모로 실제 인간의 쇼핑 행동과 비교합니다. 우리의 연구 결과는 AgentA/B가 인간과 유사한 행동 패턴을 모방할 수 있음을 시사합니다.

## 📝 요약

이 논문은 전통적인 A/B 테스트의 한계를 극복하기 위해 AgentA/B라는 새로운 시스템을 제안합니다. AgentA/B는 대규모 언어 모델 기반의 자율 에이전트를 활용하여 실제 웹 페이지에서 사용자 상호작용을 자동으로 시뮬레이션합니다. 이를 통해 다양한 페르소나를 가진 에이전트들이 동적 웹 페이지를 탐색하고 검색, 클릭, 필터링, 구매와 같은 다단계 상호작용을 수행할 수 있습니다. 실험에서는 1,000개의 에이전트를 사용하여 Amazon.com에서의 A/B 테스트를 수행하고, 에이전트의 행동이 실제 인간의 쇼핑 행동과 유사함을 확인했습니다. 이 연구는 AgentA/B가 인간과 유사한 행동 패턴을 모방할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 전통적인 A/B 테스트는 대규모의 실시간 사용자 트래픽과 긴 테스트 결과 대기 시간에 의존하는 한계가 있다.
- 2. AgentA/B는 대형 언어 모델 기반의 자율 에이전트를 활용하여 실제 웹페이지에서 사용자 상호작용을 자동으로 시뮬레이션하는 시스템이다.
- 3. AgentA/B는 다양한 페르소나를 가진 LLM 에이전트를 대규모로 배치하여 검색, 클릭, 필터링, 구매 등의 다단계 상호작용을 수행할 수 있다.
- 4. AgentA/B를 사용한 실험에서 1,000명의 LLM 에이전트를 통해 Amazon.com에서의 A/B 테스트를 시뮬레이션하고, 실제 인간의 쇼핑 행동과 비교하였다.
- 5. 연구 결과, AgentA/B는 인간과 유사한 행동 패턴을 모방할 수 있음을 시사한다.


---

*Generated on 2025-09-23 11:52:29*