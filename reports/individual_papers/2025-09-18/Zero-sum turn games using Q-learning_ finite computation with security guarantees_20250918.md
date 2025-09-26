---
keywords:
  - Reinforcement Learning
  - Zero-Sum Turn Games
  - Saddle-Point Policies
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13585
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:01:15.194634",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Zero-Sum Turn Games",
    "Saddle-Point Policies"
  ],
  "rejected_keywords": [
    "Opponent-Informed Exploration"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Zero-Sum Turn Games": 0.7,
    "Saddle-Point Policies": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Zero-sum turn games using Q-learning: finite computation with security guarantees

**Korean Title:** Q-러닝을 사용한 제로섬 턴 기반 게임: 보안 보장을 갖춘 유한한 계산

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Q-learning]]
**⚡ Unique Technical**: [[keywords/Zero-Sum Turn Games|zero-sum turn games]], [[keywords/Saddle-Point Policies|saddle-point state-feedback policies]]

## 🔗 유사한 논문
- [[Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation]] (80.7% similar)
- [[Distributionally_Robust_Equilibria_over_the_Wasserstein_Distance_for_Generalized_Nash_Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (78.0% similar)
- [[Efficient Last-Iterate Convergence in Regret Minimization via Adaptive Reward Transformation]] (77.6% similar)
- [[Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (77.4% similar)
- [[Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13585v1 Announce Type: new 
Abstract: This paper addresses zero-sum ``turn'' games, in which only one player can make decisions at each state. We show that pure saddle-point state-feedback policies for turn games can be constructed from dynamic programming fixed-point equations for a single value function or Q-function. These fixed-points can be constructed using a suitable form of Q-learning. For discounted costs, convergence of this form of Q-learning can be established using classical techniques. For undiscounted costs, we provide a convergence result that applies to finite-time deterministic games, which we use to illustrate our results. For complex games, the Q-learning iteration must be terminated before exploring the full-state, which can lead to policies that cannot guarantee the security levels implied by the final Q-function. To mitigate this, we propose an ``opponent-informed'' exploration policy for selecting the Q-learning samples. This form of exploration can guarantee that the final Q-function provides security levels that hold, at least, against a given set of policies. A numerical demonstration for a multi-agent game, Atlatl, indicates the effectiveness of these methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.13585v1 발표 유형: 새로운
요약: 본 논문은 단 한 명의 플레이어만이 각 상태에서 결정을 내릴 수 있는 제로섬 "턴" 게임에 대해 다룹니다. 우리는 턴 게임을 위한 순수한 새들 포인트 상태 피드백 정책이 단일 가치 함수 또는 Q-함수에 대한 동적 프로그래밍 고정점 방정식으로부터 구성될 수 있다는 것을 보여줍니다. 이러한 고정점은 적절한 형태의 Q-러닝을 사용하여 구성할 수 있습니다. 할인 비용의 경우, 이러한 형태의 Q-러닝의 수렴은 고전적인 기법을 사용하여 입증할 수 있습니다. 할인되지 않은 비용의 경우, 우리는 유한 시간 결정론적 게임에 적용되는 수렴 결과를 제시하며 이를 통해 결과를 설명합니다. 복잡한 게임의 경우, Q-러닝 반복은 전체 상태를 탐색하기 전에 종료되어야 하며, 이는 최종 Q-함수에서 시큐리티 수준을 보장할 수 없는 정책을 유발할 수 있습니다. 이를 완화하기 위해, 우리는 Q-러닝 샘플을 선택하기 위한 "상대방 정보를 고려한" 탐색 정책을 제안합니다. 이러한 형태의 탐색은 최종 Q-함수가 적어도 주어진 정책 집합에 대해 보장되는 시큐리티 수준을 제공함을 보장할 수 있습니다. 다중 에이전트 게임 Atlatl에 대한 수치적 시연은 이러한 방법의 효과를 보여줍니다.

## 📝 요약

이 연구는 한 플레이어만이 각 상태에서 결정을 내리는 제로섬 "턴" 게임에 대해 다룬다. 우리는 턴 게임을 위한 순수한 산마점 상태 피드백 정책이 단일 가치 함수나 Q-함수에 대한 동적 프로그래밍 고정점 방정식에서 구성될 수 있음을 보여준다. 이러한 고정점은 적절한 형태의 Q-러닝을 사용하여 구성될 수 있다. 할인된 비용에 대해, 이러한 형태의 Q-러닝의 수렴성은 고전적인 기법을 사용하여 입증될 수 있다. 할인되지 않은 비용에 대해, 우리는 유한 시간 결정론적 게임에 적용되는 수렴 결과를 제시하며 결과를 설명한다. 복잡한 게임의 경우, Q-러닝 반복은 전체 상태를 탐색하기 전에 종료되어야 하며, 이는 최종 Q-함수에서 함축된 보안 수준을 보장할 수 없는 정책으로 이어질 수 있다. 이를 완화하기 위해, 우리는 Q-러닝 샘플을 선택하기 위한 "상대방 정보를 고려한" 탐색 정책을 제안한다. 이러한 탐사 형태는 최종 Q-함수가 적어도 주어진 정책 집합에 대해 보안 수준을 제공함을 보장할 수 있다. 다중 에이전트 게임 Atlatl에 대한 수치적 시연은 이러한 방법의 효과를 보여준다.

## 🎯 주요 포인트

- 1. 순환 게임에서 순수한 안장점 상태 피드백 정책은 동적 프로그래밍 고정점 방정식을 통해 구성될 수 있다.

- 2. 할인된 비용에 대해 Q-러닝의 수렴은 고전적인 기법을 사용하여 입증할 수 있다.

- 3. 상대방에게 정보를 제공하는 탐사 정책을 통해 안전 수준을 보장할 수 있는 최종 Q-함수를 선택할 수 있다.

---

*Generated on 2025-09-18 17:24:28*