---
keywords:
  - Dominated Actions
  - Imperfect-Information Games
  - Nash Equilibrium
  - Polynomial-Time Algorithm
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2504.09716
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:53:37.293131",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dominated Actions",
    "Imperfect-Information Games",
    "Nash Equilibrium",
    "Polynomial-Time Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dominated Actions": 0.75,
    "Imperfect-Information Games": 0.8,
    "Nash Equilibrium": 0.85,
    "Polynomial-Time Algorithm": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dominated Actions",
        "canonical": "Dominated Actions",
        "aliases": [
          "Dominated Strategies"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and offers a unique angle for linking game theory concepts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Imperfect-Information Games",
        "canonical": "Imperfect-Information Games",
        "aliases": [
          "Games with Imperfect Information"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key context for the study and connects to broader discussions in game theory.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Nash Equilibrium",
        "canonical": "Nash Equilibrium",
        "aliases": [
          "Nash Equilibria"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in game theory that is relevant to the paper's focus on strategy optimization.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Polynomial-Time Algorithm",
        "canonical": "Polynomial-Time Algorithm",
        "aliases": [
          "Efficient Algorithm"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the computational efficiency aspect of the paper's contribution.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "strategic-form games",
      "extensive form",
      "game tree"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dominated Actions",
      "resolved_canonical": "Dominated Actions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Imperfect-Information Games",
      "resolved_canonical": "Imperfect-Information Games",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Nash Equilibrium",
      "resolved_canonical": "Nash Equilibrium",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Polynomial-Time Algorithm",
      "resolved_canonical": "Polynomial-Time Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Dominated Actions in Imperfect-Information Games

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2504.09716.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2504.09716](https://arxiv.org/abs/2504.09716)

## 🔗 유사한 논문
- [[2025-09-17/Nash Equilibria in Games with Playerwise Concave Coupling Constraints_ Existence and Computation_20250917|Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation]] (81.1% similar)
- [[2025-09-18/Zero-sum turn games using Q-learning_ finite computation with security guarantees_20250918|Zero-sum turn games using Q-learning: finite computation with security guarantees]] (78.2% similar)
- [[2025-09-18/Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (78.2% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (75.8% similar)
- [[2025-09-22/Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems_20250922|Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems]] (75.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nash Equilibrium|Nash Equilibrium]]
**🔗 Specific Connectable**: [[keywords/Imperfect-Information Games|Imperfect-Information Games]], [[keywords/Polynomial-Time Algorithm|Polynomial-Time Algorithm]]
**⚡ Unique Technical**: [[keywords/Dominated Actions|Dominated Actions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.09716v4 Announce Type: replace-cross 
Abstract: Dominance is a fundamental concept in game theory. In strategic-form games dominated strategies can be identified in polynomial time. As a consequence, iterative removal of dominated strategies can be performed efficiently as a preprocessing step for reducing the size of a game before computing a Nash equilibrium. For imperfect-information games in extensive form, we could convert the game to strategic form and then iteratively remove dominated strategies in the same way; however, this conversion may cause an exponential blowup in game size. In this paper we define and study the concept of dominated actions in imperfect-information games. Our main result is a polynomial-time algorithm for determining whether an action is dominated (strictly or weakly) by any mixed strategy in n-player games, which can be extended to an algorithm for iteratively removing dominated actions. This allows us to efficiently reduce the size of the game tree as a preprocessing step for Nash equilibrium computation. We explore the role of dominated actions empirically in the "All In or Fold" No-Limit Texas Hold'em poker variant.

## 📝 요약

이 논문은 불완전 정보 게임에서 지배적 행동의 개념을 정의하고 연구합니다. 주요 기여는 n-인 플레이어 게임에서 혼합 전략에 의해 행동이 지배되는지 여부를 다항 시간 내에 결정할 수 있는 알고리즘을 제안한 것입니다. 이 알고리즘은 지배적 행동을 반복적으로 제거하여 게임 트리의 크기를 효율적으로 줄일 수 있게 합니다. 이를 통해 내쉬 균형 계산 전 전처리 단계로 활용할 수 있습니다. 연구는 "All In or Fold" 노리밋 텍사스 홀덤 포커 변형에서 지배적 행동의 역할을 실증적으로 탐구합니다.

## 🎯 주요 포인트

- 1. 게임 이론에서 지배는 기본적인 개념이며, 전략형 게임에서는 지배 전략을 다항 시간 내에 식별할 수 있다.
- 2. 불완전 정보 게임에서 지배된 행동을 정의하고 연구하며, n-인 게임에서 혼합 전략에 의해 지배되는 행동을 다항 시간 내에 결정하는 알고리즘을 제안한다.
- 3. 제안된 알고리즘은 지배된 행동을 반복적으로 제거하여 게임 트리의 크기를 효율적으로 줄이고, 내쉬 균형 계산의 전처리 단계로 활용할 수 있다.
- 4. "올인 또는 폴드" 노리밋 텍사스 홀덤 포커 변형에서 지배된 행동의 역할을 실증적으로 탐구한다.


---

*Generated on 2025-09-24 00:53:37*