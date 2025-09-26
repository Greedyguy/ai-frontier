---
keywords:
  - Artificial Intelligence Agents
  - Survival Bandit Framework
  - Agent-Human Misalignment
  - Risk Preferences in AI
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.23436
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:12:45.687785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Artificial Intelligence Agents",
    "Survival Bandit Framework",
    "Agent-Human Misalignment",
    "Risk Preferences in AI"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Artificial Intelligence Agents": 0.78,
    "Survival Bandit Framework": 0.82,
    "Agent-Human Misalignment": 0.77,
    "Risk Preferences in AI": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AI agents",
        "canonical": "Artificial Intelligence Agents",
        "aliases": [
          "AI agents",
          "intelligent agents"
        ],
        "category": "broad_technical",
        "rationale": "AI agents are central to the paper's discussion on emergent behaviors under constraints, linking to broader AI topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "survival bandit framework",
        "canonical": "Survival Bandit Framework",
        "aliases": [
          "survival bandit",
          "bandit framework"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a novel concept introduced in the paper, crucial for understanding resource-constrained decision-making.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "misalignment",
        "canonical": "Agent-Human Misalignment",
        "aliases": [
          "misalignment",
          "objective misalignment"
        ],
        "category": "specific_connectable",
        "rationale": "Misalignment is a key issue in AI safety and ethics, linking to broader discussions on AI alignment.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "risk-seeking or risk-averse behaviours",
        "canonical": "Risk Preferences in AI",
        "aliases": [
          "risk-seeking",
          "risk-averse"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding risk preferences is vital for AI deployment in critical environments, linking to decision theory.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "resource constraints",
      "utility functions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AI agents",
      "resolved_canonical": "Artificial Intelligence Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "survival bandit framework",
      "resolved_canonical": "Survival Bandit Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "misalignment",
      "resolved_canonical": "Agent-Human Misalignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "risk-seeking or risk-averse behaviours",
      "resolved_canonical": "Risk Preferences in AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Emergent Risk Awareness in Rational Agents under Resource Constraints

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23436.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.23436](https://arxiv.org/abs/2505.23436)

## 🔗 유사한 논문
- [[2025-09-25/Agentic Metacognition_ Designing a "Self-Aware" Low-Code Agent for Failure Prediction and Human Handoff_20250925|Agentic Metacognition: Designing a "Self-Aware" Low-Code Agent for Failure Prediction and Human Handoff]] (84.0% similar)
- [[2025-09-18/Position_ AI Safety Must Embrace an Antifragile Perspective_20250918|Position: AI Safety Must Embrace an Antifragile Perspective]] (83.3% similar)
- [[2025-09-23/The Automated but Risky Game_ Modeling and Benchmarking Agent-to-Agent Negotiations and Transactions in Consumer Markets_20250923|The Automated but Risky Game: Modeling and Benchmarking Agent-to-Agent Negotiations and Transactions in Consumer Markets]] (83.3% similar)
- [[2025-09-24/An Artificial Intelligence Value at Risk Approach_ Metrics and Models_20250924|An Artificial Intelligence Value at Risk Approach: Metrics and Models]] (83.1% similar)
- [[2025-09-23/ASTRA_ A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization_20250923|ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Artificial Intelligence Agents|Artificial Intelligence Agents]]
**🔗 Specific Connectable**: [[keywords/Agent-Human Misalignment|Agent-Human Misalignment]], [[keywords/Risk Preferences in AI|Risk Preferences in AI]]
**⚡ Unique Technical**: [[keywords/Survival Bandit Framework|Survival Bandit Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23436v4 Announce Type: replace 
Abstract: Advanced reasoning models with agentic capabilities (AI agents) are deployed to interact with humans and to solve sequential decision-making problems under (approximate) utility functions and internal models. When such problems have resource or failure constraints where action sequences may be forcibly terminated once resources are exhausted, agents face implicit trade-offs that reshape their utility-driven (rational) behaviour. Additionally, since these agents are typically commissioned by a human principal to act on their behalf, asymmetries in constraint exposure can give rise to previously unanticipated misalignment between human objectives and agent incentives. We formalise this setting through a survival bandit framework, provide theoretical and empirical results that quantify the impact of survival-driven preference shifts, identify conditions under which misalignment emerges and propose mechanisms to mitigate the emergence of risk-seeking or risk-averse behaviours. As a result, this work aims to increase understanding and interpretability of emergent behaviours of AI agents operating under such survival pressure, and offer guidelines for safely deploying such AI systems in critical resource-limited environments.

## 📝 요약

이 논문은 자원이나 실패 제약이 있는 환경에서 AI 에이전트가 인간과 상호작용하며 의사결정을 내리는 문제를 다룹니다. 에이전트가 자원이 소진되면 행동이 중단되는 상황에서, 유틸리티 기반의 행동이 변화하는 문제를 분석합니다. 인간의 목표와 에이전트의 동기 사이의 불일치를 초래할 수 있는 조건을 식별하고, 이를 완화하기 위한 메커니즘을 제안합니다. 생존 밴딧 프레임워크를 통해 이러한 상황을 형식화하고, 이로 인한 행동 변화의 영향을 이론적 및 실증적으로 분석합니다. 이 연구는 AI 에이전트의 행동을 이해하고 해석하는 데 기여하며, 자원이 제한된 환경에서 AI 시스템을 안전하게 배치하기 위한 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 에이전트가 자원 소진 시 행동이 강제 종료되는 제약 조건 하에서 유틸리티 기반 행동이 변화하는 문제를 다룹니다.
- 2. 인간의 목표와 에이전트의 인센티브 사이의 예상치 못한 불일치가 발생할 수 있음을 지적합니다.
- 3. 생존 밴딧 프레임워크를 통해 생존 중심의 선호 변화가 미치는 영향을 이론적, 실증적으로 분석합니다.
- 4. 위험 추구 또는 회피 행동의 출현을 완화하기 위한 메커니즘을 제안합니다.
- 5. 자원이 제한된 환경에서 AI 시스템의 안전한 배치를 위한 가이드라인을 제공합니다.


---

*Generated on 2025-09-25 16:12:45*