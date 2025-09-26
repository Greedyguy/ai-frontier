---
keywords:
  - Monte-Carlo Tree Search
  - Minimax Search
  - Process Mining
  - Multi-agent Monte-Carlo Tree Search
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.23326
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:11:26.512668",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Monte-Carlo Tree Search",
    "Minimax Search",
    "Process Mining",
    "Multi-agent Monte-Carlo Tree Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Monte-Carlo Tree Search": 0.78,
    "Minimax Search": 0.75,
    "Process Mining": 0.74,
    "Multi-agent Monte-Carlo Tree Search": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Monte-Carlo Tree Search",
        "canonical": "Monte-Carlo Tree Search",
        "aliases": [
          "MCTS"
        ],
        "category": "unique_technical",
        "rationale": "Monte-Carlo Tree Search is central to the paper's exploration of decision-making in AI, providing a unique technical focus.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "minimax search",
        "canonical": "Minimax Search",
        "aliases": [
          "minimax"
        ],
        "category": "specific_connectable",
        "rationale": "Minimax Search complements MCTS in the paper, enhancing understanding of AI decision-making strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "process mining",
        "canonical": "Process Mining",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Process Mining is used to explain agent strategies, linking AI techniques with process analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.74
      },
      {
        "surface": "multi-agent MCTS",
        "canonical": "Multi-agent Monte-Carlo Tree Search",
        "aliases": [
          "multi-agent MCTS"
        ],
        "category": "unique_technical",
        "rationale": "The integration of multi-agent dynamics with MCTS is a novel approach explored in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "board game",
      "decision-making",
      "3v3 checkers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Monte-Carlo Tree Search",
      "resolved_canonical": "Monte-Carlo Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "minimax search",
      "resolved_canonical": "Minimax Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "process mining",
      "resolved_canonical": "Process Mining",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "multi-agent MCTS",
      "resolved_canonical": "Multi-agent Monte-Carlo Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Exploring Explainable Multi-agent MCTS-minimax Hybrids in Board Game Using Process Mining

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.23326.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.23326](https://arxiv.org/abs/2503.23326)

## 🔗 유사한 논문
- [[2025-09-23/MCTS-EP_ Empowering Embodied Planning with Online Preference Optimization_20250923|MCTS-EP: Empowering Embodied Planning with Online Preference Optimization]] (82.0% similar)
- [[2025-09-22/Improving Monte Carlo Tree Search for Symbolic Regression_20250922|Improving Monte Carlo Tree Search for Symbolic Regression]] (81.9% similar)
- [[2025-09-25/Adaptive Event-Triggered Policy Gradient for Multi-Agent Reinforcement Learning_20250925|Adaptive Event-Triggered Policy Gradient for Multi-Agent Reinforcement Learning]] (79.4% similar)
- [[2025-09-23/A Data-Driven Discretized CS_GO Simulation Environment to Facilitate Strategic Multi-Agent Planning Research_20250923|A Data-Driven Discretized CS:GO Simulation Environment to Facilitate Strategic Multi-Agent Planning Research]] (79.0% similar)
- [[2025-09-18/Meta-Optimization and Program Search using Language Models for Task and Motion Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Minimax Search|Minimax Search]], [[keywords/Process Mining|Process Mining]]
**⚡ Unique Technical**: [[keywords/Monte-Carlo Tree Search|Monte-Carlo Tree Search]], [[keywords/Multi-agent Monte-Carlo Tree Search|Multi-agent Monte-Carlo Tree Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.23326v3 Announce Type: replace 
Abstract: Monte-Carlo Tree Search (MCTS) is a family of sampling-based search algorithms widely used for online planning in sequential decision-making domains and at the heart of many recent advances in artificial intelligence. Understanding the behavior of MCTS agents is difficult for developers and users due to the frequently large and complex search trees that result from the simulation of many possible futures, their evaluations, and their relationships. This paper presents our ongoing investigation into potential explanations for the decision-making and behavior of MCTS. A weakness of MCTS is that it constructs a highly selective tree and, as a result, can miss crucial moves and fall into tactical traps. Full-width minimax search constitutes the solution. We integrate shallow minimax search into the rollout phase of multi-agent MCTS and use process mining technique to explain agents' strategies in 3v3 checkers.

## 📝 요약

이 논문은 몬테카를로 트리 탐색(MCTS)의 의사결정 및 행동을 설명하기 위한 연구를 다룹니다. MCTS는 복잡한 탐색 트리를 생성하여 개발자와 사용자가 그 행동을 이해하기 어렵게 만듭니다. 본 연구에서는 MCTS의 약점인 선택적 트리 구조로 인해 중요한 수를 놓치거나 전술적 함정에 빠질 수 있다는 문제를 해결하기 위해, 다중 에이전트 MCTS의 롤아웃 단계에 얕은 미니맥스 탐색을 통합했습니다. 또한, 프로세스 마이닝 기법을 사용하여 3대3 체커 게임에서 에이전트의 전략을 설명합니다. 주요 기여는 MCTS의 의사결정 과정을 더 명확하게 이해할 수 있는 방법론을 제시한 것입니다.

## 🎯 주요 포인트

- 1. 몬테카를로 트리 탐색(MCTS)은 순차적 의사 결정 분야에서 온라인 계획을 위해 널리 사용되는 샘플링 기반 탐색 알고리즘이다.
- 2. MCTS 에이전트의 행동을 이해하는 것은 시뮬레이션된 많은 가능한 미래와 그 평가, 관계로 인해 복잡한 탐색 트리로 인해 어렵다.
- 3. MCTS의 약점은 매우 선택적인 트리를 구성하여 중요한 수를 놓치거나 전술적 함정에 빠질 수 있다는 것이다.
- 4. 이 논문에서는 다중 에이전트 MCTS의 롤아웃 단계에 얕은 미니맥스 탐색을 통합하여 3대3 체커에서 에이전트의 전략을 설명하는 방법을 제안한다.


---

*Generated on 2025-09-25 16:11:26*