---
keywords:
  - Frank-Wolfe Self-Play
  - Multi-Armed Bandits
  - Linear Bandits
  - Differential Inclusion
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19901
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:41:47.036036",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Frank-Wolfe Self-Play",
    "Multi-Armed Bandits",
    "Linear Bandits",
    "Differential Inclusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Frank-Wolfe Self-Play": 0.8,
    "Multi-Armed Bandits": 0.9,
    "Linear Bandits": 0.7,
    "Differential Inclusion": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Frank-Wolfe Self-Play",
        "canonical": "Frank-Wolfe Self-Play",
        "aliases": [
          "FWSP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for linking to specific algorithmic discussions.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-armed bandits",
        "canonical": "Multi-Armed Bandits",
        "aliases": [
          "MAB"
        ],
        "category": "specific_connectable",
        "rationale": "A foundational concept in the paper, connecting to a wide range of exploration-exploitation literature.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "linear bandits",
        "canonical": "Linear Bandits",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific case study in the paper, relevant for linking to linear optimization problems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "differential inclusion",
        "canonical": "Differential Inclusion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A mathematical concept used in the analysis, important for linking to mathematical optimization techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "hypothesis",
      "experimenter",
      "skeptic",
      "algorithm design"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Frank-Wolfe Self-Play",
      "resolved_canonical": "Frank-Wolfe Self-Play",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-armed bandits",
      "resolved_canonical": "Multi-Armed Bandits",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "linear bandits",
      "resolved_canonical": "Linear Bandits",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "differential inclusion",
      "resolved_canonical": "Differential Inclusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Pure Exploration via Frank-Wolfe Self-Play

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19901.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19901](https://arxiv.org/abs/2509.19901)

## 🔗 유사한 논문
- [[2025-09-19/Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (84.0% similar)
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (83.6% similar)
- [[2025-09-18/Zero-sum turn games using Q-learning_ finite computation with security guarantees_20250918|Zero-sum turn games using Q-learning: finite computation with security guarantees]] (82.1% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (82.1% similar)
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Armed Bandits|Multi-Armed Bandits]], [[keywords/Linear Bandits|Linear Bandits]]
**⚡ Unique Technical**: [[keywords/Frank-Wolfe Self-Play|Frank-Wolfe Self-Play]], [[keywords/Differential Inclusion|Differential Inclusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19901v1 Announce Type: new 
Abstract: We study pure exploration in structured stochastic multi-armed bandits, aiming to efficiently identify the correct hypothesis from a finite set of alternatives. For a broad class of tasks, asymptotic analyses reduce to a maximin optimization that admits a two-player zero-sum game interpretation between an experimenter and a skeptic: the experimenter allocates measurements to rule out alternatives while the skeptic proposes alternatives. We reformulate the game by allowing the skeptic to adopt a mixed strategy, yielding a concave-convex saddle-point problem. This viewpoint leads to Frank-Wolfe Self-Play (FWSP): a projection-free, regularization-free, tuning-free method whose one-hot updates on both sides match the bandit sampling paradigm. However, structural constraints introduce sharp pathologies that complicate algorithm design and analysis: our linear-bandit case study exhibits nonunique optima, optimal designs with zero mass on the best arm, bilinear objectives, and nonsmoothness at the boundary. We address these challenges via a differential-inclusion argument, proving convergence of the game value for best-arm identification in linear bandits. Our analysis proceeds through a continuous-time limit: a differential inclusion with a Lyapunov function that decays exponentially, implying a vanishing duality gap and convergence to the optimal value. Although Lyapunov analysis requires differentiability of the objective, which is not guaranteed on the boundary, we show that along continuous trajectories the algorithm steers away from pathological nonsmooth points and achieves uniform global convergence to the optimal game value. We then embed the discrete-time updates into a perturbed flow and show that the discrete game value also converges. Building on FWSP, we further propose a learning algorithm based on posterior sampling. Numerical experiments demonstrate a vanishing duality gap.

## 📝 요약

이 논문은 구조화된 확률적 다중 슬롯머신 문제에서 올바른 가설을 효율적으로 식별하는 방법을 연구합니다. 실험자와 회의론자 간의 이중 플레이어 제로섬 게임으로 해석되는 maximin 최적화 문제를 다루며, 회의론자가 혼합 전략을 채택할 수 있도록 게임을 재구성하여 오목-볼록 안장점 문제를 제시합니다. 이를 통해 프랭크-울프 셀프 플레이(FWSP) 방법론을 개발하였으며, 이는 투영, 정규화, 튜닝이 필요 없는 방법입니다. 그러나 구조적 제약으로 인해 알고리즘 설계와 분석에 어려움이 따릅니다. 이러한 문제를 미분 포함 논증을 통해 해결하며, 선형 슬롯머신에서 최적 팔 식별을 위한 게임 값의 수렴을 입증합니다. 연속 시간 한계를 통해 Lyapunov 함수를 사용하여 지수적으로 감소하는 이중성 간격과 최적 값으로의 수렴을 보장합니다. 또한, 이산 시간 업데이트를 통해 이산 게임 값의 수렴을 보여주며, FWSP를 기반으로 후행 표본 추출에 기반한 학습 알고리즘을 제안합니다. 실험 결과는 이중성 간격의 감소를 입증합니다.

## 🎯 주요 포인트

- 1. 구조적 확률적 멀티 암드 밴딧에서 올바른 가설을 효율적으로 식별하기 위한 순수 탐색을 연구합니다.
- 2. 실험자와 회의론자 간의 이중 플레이어 제로섬 게임 해석을 통해 최대최소 최적화 문제로 귀결됩니다.
- 3. Frank-Wolfe Self-Play(FWSP)는 투영, 정규화, 튜닝이 필요 없는 방법으로 밴딧 샘플링 패러다임에 맞는 업데이트를 제공합니다.
- 4. 구조적 제약으로 인해 비선형 경계에서의 비차별성과 같은 문제들이 발생하며, 이를 미분 포함 논증을 통해 해결합니다.
- 5. FWSP를 기반으로 후행 샘플링에 기반한 학습 알고리즘을 제안하며, 수치 실험을 통해 이중성 간극이 사라짐을 보여줍니다.


---

*Generated on 2025-09-25 16:41:47*