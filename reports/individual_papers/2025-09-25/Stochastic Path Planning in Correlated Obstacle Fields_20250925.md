---
keywords:
  - Stochastic Path Planning
  - Gaussian Random Field
  - Bayesian Inference
  - Distributional Reinforcement Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19559
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:55:52.816513",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Path Planning",
    "Gaussian Random Field",
    "Bayesian Inference",
    "Distributional Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Path Planning": 0.78,
    "Gaussian Random Field": 0.77,
    "Bayesian Inference": 0.7,
    "Distributional Reinforcement Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Stochastic Path Planning",
        "canonical": "Stochastic Path Planning",
        "aliases": [
          "Probabilistic Path Planning"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific approach to path planning under uncertainty, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian Random Field",
        "canonical": "Gaussian Random Field",
        "aliases": [
          "GRF"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key statistical model used for spatial correlation in the paper, linking it to probabilistic modeling.",
        "novelty_score": 0.58,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Bayesian belief updates",
        "canonical": "Bayesian Inference",
        "aliases": [
          "Bayesian Updates"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian methods are a broad technical category that supports the paper's probabilistic framework.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Distributional Reinforcement Learning",
        "canonical": "Distributional Reinforcement Learning",
        "aliases": [
          "Distributional RL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specialized form of reinforcement learning that enhances uncertainty quantification, relevant to the paper's goals.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "navigation",
      "sensor",
      "policy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Stochastic Path Planning",
      "resolved_canonical": "Stochastic Path Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian Random Field",
      "resolved_canonical": "Gaussian Random Field",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Bayesian belief updates",
      "resolved_canonical": "Bayesian Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Distributional Reinforcement Learning",
      "resolved_canonical": "Distributional Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Stochastic Path Planning in Correlated Obstacle Fields

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19559.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19559](https://arxiv.org/abs/2509.19559)

## 🔗 유사한 논문
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (81.2% similar)
- [[2025-09-24/Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections_20250924|Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections]] (81.2% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (81.2% similar)
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (81.1% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Inference|Bayesian Inference]]
**🔗 Specific Connectable**: [[keywords/Gaussian Random Field|Gaussian Random Field]], [[keywords/Distributional Reinforcement Learning|Distributional Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Stochastic Path Planning|Stochastic Path Planning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19559v1 Announce Type: cross 
Abstract: We introduce the Stochastic Correlated Obstacle Scene (SCOS) problem, a navigation setting with spatially correlated obstacles of uncertain blockage status, realistically constrained sensors that provide noisy readings and costly disambiguation. Modeling the spatial correlation with Gaussian Random Field (GRF), we develop Bayesian belief updates that refine blockage probabilities, and use the posteriors to reduce search space for efficiency. To find the optimal traversal policy, we propose a novel two-stage learning framework. An offline phase learns a robust base policy via optimistic policy iteration augmented with information bonus to encourage exploration in informative regions, followed by an online rollout policy with periodic base updates via a Bayesian mechanism for information adaptation. This framework supports both Monte Carlo point estimation and distributional reinforcement learning (RL) to learn full cost distributions, leading to stronger uncertainty quantification. We establish theoretical benefits of correlation-aware updating and convergence property under posterior sampling. Comprehensive empirical evaluations across varying obstacle densities, sensor capabilities demonstrate consistent performance gains over baselines. This framework addresses navigation challenges in environments with adversarial interruptions or clustered natural hazards.

## 📝 요약

Stochastic Correlated Obstacle Scene (SCOS) 문제는 공간적으로 상관된 장애물과 불확실한 차단 상태를 가진 환경에서의 내비게이션 문제를 다룹니다. Gaussian Random Field(GRF)를 사용하여 공간적 상관관계를 모델링하고, 베이지안 신념 업데이트를 통해 차단 확률을 개선하여 탐색 공간을 줄입니다. 최적의 경로 탐색을 위해 두 단계의 학습 프레임워크를 제안합니다. 오프라인 단계에서는 정보 보너스를 활용한 정책 반복으로 탐색을 장려하고, 온라인 단계에서는 베이지안 메커니즘을 통한 주기적 업데이트로 정보를 적응시킵니다. 이 프레임워크는 몬테카를로 점 추정과 분포 강화 학습을 지원하여 불확실성 정량화를 강화합니다. 이론적 이점과 수렴성을 입증하며, 다양한 장애물 밀도와 센서 능력에서 일관된 성능 향상을 보여줍니다. 이 연구는 적대적 방해나 자연적 위험이 있는 환경에서의 내비게이션 문제를 해결합니다.

## 🎯 주요 포인트

- 1. Stochastic Correlated Obstacle Scene (SCOS) 문제는 공간적으로 상관된 장애물과 불확실한 차단 상태를 다루는 내비게이션 설정을 소개합니다.
- 2. Gaussian Random Field (GRF)를 사용하여 공간적 상관성을 모델링하고, 베이지안 신념 업데이트를 통해 차단 확률을 정제합니다.
- 3. 최적의 탐색 정책을 찾기 위해 두 단계의 학습 프레임워크를 제안하며, 오프라인 단계에서는 정보 보너스를 통해 탐색을 장려하는 강력한 기본 정책을 학습합니다.
- 4. 온라인 롤아웃 정책은 베이지안 메커니즘을 통해 주기적으로 기본 업데이트를 수행하여 정보 적응을 지원합니다.
- 5. 다양한 장애물 밀도와 센서 기능을 아우르는 실험 평가에서 일관된 성능 향상을 보여주며, 적대적 방해나 자연 재해가 있는 환경에서의 내비게이션 문제를 해결합니다.


---

*Generated on 2025-09-25 16:55:52*