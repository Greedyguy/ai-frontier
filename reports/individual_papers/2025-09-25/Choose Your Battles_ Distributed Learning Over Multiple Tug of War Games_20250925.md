---
keywords:
  - Meta Tug-of-War
  - Meta Tug-of-Peace Algorithm
  - Distributed Learning
  - Stochastic Approximation Algorithm
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20147
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:01:25.415581",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Meta Tug-of-War",
    "Meta Tug-of-Peace Algorithm",
    "Distributed Learning",
    "Stochastic Approximation Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Meta Tug-of-War": 0.8,
    "Meta Tug-of-Peace Algorithm": 0.78,
    "Distributed Learning": 0.75,
    "Stochastic Approximation Algorithm": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Meta Tug-of-War",
        "canonical": "Meta Tug-of-War",
        "aliases": [
          "Meta-ToW"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel game-theoretic framework.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Meta Tug-of-Peace algorithm",
        "canonical": "Meta Tug-of-Peace Algorithm",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific algorithm introduced in the paper, crucial for understanding the proposed solution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "distributed learning",
        "canonical": "Distributed Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Distributed learning is a key aspect of the paper, linking it to broader machine learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "stochastic approximation algorithm",
        "canonical": "Stochastic Approximation Algorithm",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This algorithm type is crucial for the implementation of the proposed solution, linking to stochastic methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "games",
      "players",
      "reward"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Meta Tug-of-War",
      "resolved_canonical": "Meta Tug-of-War",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Meta Tug-of-Peace algorithm",
      "resolved_canonical": "Meta Tug-of-Peace Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "distributed learning",
      "resolved_canonical": "Distributed Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "stochastic approximation algorithm",
      "resolved_canonical": "Stochastic Approximation Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Choose Your Battles: Distributed Learning Over Multiple Tug of War Games

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20147.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20147](https://arxiv.org/abs/2509.20147)

## 🔗 유사한 논문
- [[2025-09-25/Pure Exploration via Frank-Wolfe Self-Play_20250925|Pure Exploration via Frank-Wolfe Self-Play]] (79.8% similar)
- [[2025-09-19/Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships_20250919|Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships]] (79.7% similar)
- [[2025-09-18/Zero-sum turn games using Q-learning_ finite computation with security guarantees_20250918|Zero-sum turn games using Q-learning: finite computation with security guarantees]] (79.3% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (79.1% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Distributed Learning|Distributed Learning]]
**🔗 Specific Connectable**: [[keywords/Stochastic Approximation Algorithm|Stochastic Approximation Algorithm]]
**⚡ Unique Technical**: [[keywords/Meta Tug-of-War|Meta Tug-of-War]], [[keywords/Meta Tug-of-Peace Algorithm|Meta Tug-of-Peace Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20147v1 Announce Type: cross 
Abstract: Consider N players and K games taking place simultaneously. Each of these games is modeled as a Tug-of-War (ToW) game where increasing the action of one player decreases the reward for all other players. Each player participates in only one game at any given time. At each time step, a player decides the game in which they wish to participate in and the action they take in that game. Their reward depends on the actions of all players that are in the same game. This system of K games is termed `Meta Tug-of-War' (Meta-ToW) game. These games can model scenarios such as power control, distributed task allocation, and activation in sensor networks. We propose the Meta Tug-of-Peace algorithm, a distributed algorithm where the action updates are done using a simple stochastic approximation algorithm, and the decision to switch games is made using an infrequent 1-bit communication between the players. We prove that in Meta-ToW games, our algorithm converges to an equilibrium that satisfies a target Quality of Service reward vector for the players. We then demonstrate the efficacy of our algorithm through simulations for the scenarios mentioned above.

## 📝 요약

이 논문은 여러 게임이 동시에 진행되는 환경에서 각 게임이 Tug-of-War 게임으로 모델링된 '메타 Tug-of-War' 게임 시스템을 제안합니다. 각 플레이어는 한 번에 하나의 게임에만 참여하며, 자신의 행동이 다른 플레이어의 보상에 영향을 미칩니다. 저자들은 '메타 Tug-of-Peace'라는 분산 알고리즘을 제안하여, 간단한 확률적 근사 알고리즘을 사용해 행동을 업데이트하고, 플레이어 간 1비트 통신으로 게임 전환을 결정합니다. 이 알고리즘은 목표 서비스 품질 보상 벡터를 만족하는 균형점에 수렴함을 증명하고, 시뮬레이션을 통해 알고리즘의 효율성을 입증합니다.

## 🎯 주요 포인트

- 1. N명의 플레이어와 K개의 게임이 동시에 진행되는 '메타 줄다리기(Meta-ToW)' 게임 시스템을 제안합니다.
- 2. 각 게임은 한 플레이어의 행동이 다른 모든 플레이어의 보상을 감소시키는 줄다리기 게임으로 모델링됩니다.
- 3. 제안된 '메타 평화의 줄다리기' 알고리즘은 간단한 확률적 근사 알고리즘을 사용하여 행동을 업데이트하고, 플레이어 간의 드문 1비트 통신을 통해 게임 전환을 결정합니다.
- 4. 이 알고리즘은 플레이어의 목표 서비스 품질 보상 벡터를 만족하는 균형점으로 수렴함을 증명합니다.
- 5. 제안된 알고리즘의 효능은 전력 제어, 분산 작업 할당, 센서 네트워크 활성화 시나리오를 통해 시뮬레이션으로 입증됩니다.


---

*Generated on 2025-09-25 17:01:25*