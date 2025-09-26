---
keywords:
  - Agentic AI Workflows
  - RTL Code Generation
  - Formal Verification
  - Multi-Agent Systems
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20182
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:00:53.719223",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Agentic AI Workflows",
    "RTL Code Generation",
    "Formal Verification",
    "Multi-Agent Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Agentic AI Workflows": 0.78,
    "RTL Code Generation": 0.8,
    "Formal Verification": 0.77,
    "Multi-Agent Systems": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "agentic AI workflows",
        "canonical": "Agentic AI Workflows",
        "aliases": [
          "AI Workflows",
          "Agentic Workflows"
        ],
        "category": "unique_technical",
        "rationale": "This term captures the novel integration of AI in workflow automation, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "RTL code generation",
        "canonical": "RTL Code Generation",
        "aliases": [
          "Register Transfer Level Code Generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area within the paper, linking to specialized design and synthesis processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "formal verification feedback",
        "canonical": "Formal Verification",
        "aliases": [
          "Verification Feedback"
        ],
        "category": "specific_connectable",
        "rationale": "Formal verification is a critical component in ensuring the correctness of generated designs, connecting to broader verification methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "multi-agent framework",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "Multi-Agent Framework"
        ],
        "category": "broad_technical",
        "rationale": "Multi-agent systems are a foundational concept in AI, relevant to the coordination of agentic workflows discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "HDL",
      "EDA resources",
      "synthesis performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "agentic AI workflows",
      "resolved_canonical": "Agentic AI Workflows",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "RTL code generation",
      "resolved_canonical": "RTL Code Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "formal verification feedback",
      "resolved_canonical": "Formal Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "multi-agent framework",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Automated Multi-Agent Workflows for RTL Design

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20182.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20182](https://arxiv.org/abs/2509.20182)

## 🔗 유사한 논문
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (84.6% similar)
- [[2025-09-24/Difficulty-Aware Agent Orchestration in LLM-Powered Workflows_20250924|Difficulty-Aware Agent Orchestration in LLM-Powered Workflows]] (83.5% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (83.1% similar)
- [[2025-09-24/EvoAgentX_ An Automated Framework for Evolving Agentic Workflows_20250924|EvoAgentX: An Automated Framework for Evolving Agentic Workflows]] (83.1% similar)
- [[2025-09-23/SymRTLO_ Enhancing RTL Code Optimization with LLMs and Neuron-Inspired Symbolic Reasoning_20250923|SymRTLO: Enhancing RTL Code Optimization with LLMs and Neuron-Inspired Symbolic Reasoning]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**🔗 Specific Connectable**: [[keywords/Formal Verification|Formal Verification]]
**⚡ Unique Technical**: [[keywords/Agentic AI Workflows|Agentic AI Workflows]], [[keywords/RTL Code Generation|RTL Code Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20182v1 Announce Type: cross 
Abstract: The rise of agentic AI workflows unlocks novel opportunities for computer systems design and optimization. However, for specialized domains such as program synthesis, the relative scarcity of HDL and proprietary EDA resources online compared to more common programming tasks introduces challenges, often necessitating task-specific fine-tuning, high inference costs, and manually-crafted agent orchestration. In this work, we present VeriMaAS, a multi-agent framework designed to automatically compose agentic workflows for RTL code generation. Our key insight is to integrate formal verification feedback from HDL tools directly into workflow generation, reducing the cost of gradient-based updates or prolonged reasoning traces. Our method improves synthesis performance by 5-7% for pass@k over fine-tuned baselines, while requiring only a few hundred training examples, representing an order-of-magnitude reduction in supervision cost.

## 📝 요약

이 논문에서는 RTL 코드 생성을 위한 다중 에이전트 프레임워크인 VeriMaAS를 제안합니다. 이 연구는 HDL 도구의 형식 검증 피드백을 워크플로우 생성에 통합하여, 프로그램 합성에서의 고비용 문제를 해결하고자 합니다. 제안된 방법은 기존의 미세 조정된 기준보다 합성 성능을 5-7% 향상시키며, 몇 백 개의 훈련 예제만으로도 가능하여 감독 비용을 크게 줄입니다.

## 🎯 주요 포인트

- 1. 에이전트 기반 AI 워크플로우의 부상은 컴퓨터 시스템 설계 및 최적화에 새로운 기회를 제공합니다.
- 2. 프로그램 합성 같은 전문 분야에서는 HDL 및 EDA 리소스의 상대적 부족으로 인해 작업별 미세 조정과 높은 추론 비용이 필요합니다.
- 3. VeriMaAS는 RTL 코드 생성을 위한 에이전트 워크플로우를 자동으로 구성하는 다중 에이전트 프레임워크입니다.
- 4. HDL 도구의 형식 검증 피드백을 워크플로우 생성에 통합하여 비용을 절감하고 성능을 향상시킵니다.
- 5. 제안된 방법은 몇 백 개의 훈련 예제로 감독 비용을 크게 줄이면서 합성 성능을 5-7% 향상시킵니다.


---

*Generated on 2025-09-25 16:00:53*