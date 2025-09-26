---
keywords:
  - AutoEval Framework
  - Mobile Agents
  - UI State Change Representation
  - Judge System
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.02403
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:10:39.859017",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AutoEval Framework",
    "Mobile Agents",
    "UI State Change Representation",
    "Judge System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AutoEval Framework": 0.8,
    "Mobile Agents": 0.7,
    "UI State Change Representation": 0.78,
    "Judge System": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AutoEval",
        "canonical": "AutoEval Framework",
        "aliases": [
          "AutoEval"
        ],
        "category": "unique_technical",
        "rationale": "AutoEval is a novel framework specifically designed for autonomous evaluation of mobile agents, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "mobile agents",
        "canonical": "Mobile Agents",
        "aliases": [
          "mobile agents"
        ],
        "category": "broad_technical",
        "rationale": "Mobile agents are a central focus of the paper and connect to broader discussions in autonomous systems.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "UI state change representation",
        "canonical": "UI State Change Representation",
        "aliases": [
          "UI state change"
        ],
        "category": "unique_technical",
        "rationale": "This representation is a specific innovation within the framework that enables automatic generation of task reward signals.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Judge System",
        "canonical": "Judge System",
        "aliases": [
          "Judge System"
        ],
        "category": "unique_technical",
        "rationale": "The Judge System is a key component of the AutoEval framework, crucial for autonomous evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "task reward signals",
      "human evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AutoEval",
      "resolved_canonical": "AutoEval Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "mobile agents",
      "resolved_canonical": "Mobile Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "UI state change representation",
      "resolved_canonical": "UI State Change Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Judge System",
      "resolved_canonical": "Judge System",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AutoEval: A Practical Framework for Autonomous Evaluation of Mobile Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.02403.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.02403](https://arxiv.org/abs/2503.02403)

## 🔗 유사한 논문
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production]] (83.5% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (83.0% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (83.0% similar)
- [[2025-09-24/MobileRL_ Online Agentic Reinforcement Learning for Mobile GUI Agents_20250924|MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents]] (82.7% similar)
- [[2025-09-19/An Evaluation-Centric Paradigm for Scientific Visualization Agents_20250919|An Evaluation-Centric Paradigm for Scientific Visualization Agents]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Mobile Agents|Mobile Agents]]
**⚡ Unique Technical**: [[keywords/AutoEval Framework|AutoEval Framework]], [[keywords/UI State Change Representation|UI State Change Representation]], [[keywords/Judge System|Judge System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.02403v2 Announce Type: replace 
Abstract: Comprehensive evaluation of mobile agents can significantly advance their development and real-world applicability. However, existing benchmarks lack practicality and scalability due to the extensive manual effort in defining task reward signals and implementing evaluation codes. We propose AutoEval, an evaluation framework which tests mobile agents without any manual effort. Our approach designs a UI state change representation which can be used to automatically generate task reward signals, and employs a Judge System for autonomous evaluation. Evaluation shows AutoEval can automatically generate reward signals with high correlation to human-annotated signals, and achieve high accuracy (up to 94%) in autonomous evaluation comparable to human evaluation. Finally, we evaluate state-of-the-art mobile agents using our framework, providing insights into their performance and limitations.

## 📝 요약

이 논문은 모바일 에이전트의 평가를 자동화하여 개발과 실제 적용을 촉진하는 AutoEval이라는 평가 프레임워크를 제안합니다. 기존 벤치마크의 비실용성과 확장성 문제를 해결하기 위해, UI 상태 변화 표현을 통해 자동으로 작업 보상 신호를 생성하고, Judge System을 활용하여 자율 평가를 수행합니다. AutoEval은 인간이 주석한 신호와 높은 상관관계를 가지는 보상 신호를 자동으로 생성하며, 최대 94%의 높은 정확도로 인간 평가와 유사한 자율 평가를 달성합니다. 또한, 최신 모바일 에이전트를 평가하여 성능과 한계에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. AutoEval은 모바일 에이전트를 수동 작업 없이 평가할 수 있는 프레임워크를 제안합니다.
- 2. UI 상태 변화 표현을 통해 자동으로 작업 보상 신호를 생성할 수 있습니다.
- 3. AutoEval의 평가 시스템은 인간 평가와 유사한 높은 정확도(최대 94%)를 달성합니다.
- 4. 제안된 프레임워크를 사용하여 최신 모바일 에이전트의 성능과 한계를 평가합니다.


---

*Generated on 2025-09-25 16:10:39*