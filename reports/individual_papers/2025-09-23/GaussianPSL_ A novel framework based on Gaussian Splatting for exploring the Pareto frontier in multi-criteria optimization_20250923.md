---
keywords:
  - Gaussian Splatting
  - Pareto Set Learning
  - Multi-objective Optimization
  - Non-convex Pareto Frontiers
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17889
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:59:25.847524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Splatting",
    "Pareto Set Learning",
    "Multi-objective Optimization",
    "Non-convex Pareto Frontiers"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Splatting": 0.78,
    "Pareto Set Learning": 0.82,
    "Multi-objective Optimization": 0.8,
    "Non-convex Pareto Frontiers": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Splatting",
        "canonical": "Gaussian Splatting",
        "aliases": [
          "Gaussian Splatter"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique for handling non-convex Pareto frontiers in multi-objective optimization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pareto Set Learning",
        "canonical": "Pareto Set Learning",
        "aliases": [
          "PSL"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on improving learning of irregular Pareto fronts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-objective optimization",
        "canonical": "Multi-objective Optimization",
        "aliases": [
          "MOO"
        ],
        "category": "broad_technical",
        "rationale": "Fundamental concept in the paper, connecting to broader optimization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Non-convex Pareto frontiers",
        "canonical": "Non-convex Pareto Frontiers",
        "aliases": [
          "Irregular Pareto Fronts"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the specific challenge addressed by the proposed framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian Splatting",
      "resolved_canonical": "Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pareto Set Learning",
      "resolved_canonical": "Pareto Set Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-objective optimization",
      "resolved_canonical": "Multi-objective Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Non-convex Pareto frontiers",
      "resolved_canonical": "Non-convex Pareto Frontiers",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# GaussianPSL: A novel framework based on Gaussian Splatting for exploring the Pareto frontier in multi-criteria optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17889.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17889](https://arxiv.org/abs/2509.17889)

## 🔗 유사한 논문
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (84.1% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.1% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (81.9% similar)
- [[2025-09-23/Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs_20250923|Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs]] (81.6% similar)
- [[2025-09-17/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-objective Optimization|Multi-objective Optimization]]
**🔗 Specific Connectable**: [[keywords/Pareto Set Learning|Pareto Set Learning]]
**⚡ Unique Technical**: [[keywords/Gaussian Splatting|Gaussian Splatting]], [[keywords/Non-convex Pareto Frontiers|Non-convex Pareto Frontiers]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17889v1 Announce Type: new 
Abstract: Multi-objective optimization (MOO) is essential for solving complex real-world problems involving multiple conflicting objectives. However, many practical applications - including engineering design, autonomous systems, and machine learning - often yield non-convex, degenerate, or discontinuous Pareto frontiers, which involve traditional scalarization and Pareto Set Learning (PSL) methods that struggle to approximate accurately. Existing PSL approaches perform well on convex fronts but tend to fail in capturing the diversity and structure of irregular Pareto sets commonly observed in real-world scenarios. In this paper, we propose Gaussian-PSL, a novel framework that integrates Gaussian Splatting into PSL to address the challenges posed by non-convex Pareto frontiers. Our method dynamically partitions the preference vector space, enabling simple MLP networks to learn localized features within each region, which are then integrated by an additional MLP aggregator. This partition-aware strategy enhances both exploration and convergence, reduces sensi- tivity to initialization, and improves robustness against local optima. We first provide the mathematical formulation for controllable Pareto set learning using Gaussian Splat- ting. Then, we introduce the Gaussian-PSL architecture and evaluate its performance on synthetic and real-world multi-objective benchmarks. Experimental results demonstrate that our approach outperforms standard PSL models in learning irregular Pareto fronts while maintaining computational efficiency and model simplicity. This work offers a new direction for effective and scalable MOO under challenging frontier geometries.

## 📝 요약

이 논문은 복잡한 현실 문제에서 발생하는 비볼록, 퇴화, 불연속적인 파레토 전선을 효과적으로 학습하기 위한 새로운 프레임워크인 Gaussian-PSL을 제안합니다. 기존의 파레토 집합 학습(PSL) 방법은 비정형 파레토 집합을 잘 포착하지 못하는 한계를 보입니다. Gaussian-PSL은 Gaussian Splatting을 PSL에 통합하여 이러한 문제를 해결하며, 선호 벡터 공간을 동적으로 분할하여 각 지역의 특성을 학습하고 이를 MLP 집계기로 통합합니다. 이 방법은 탐색과 수렴을 향상시키고 초기화에 대한 민감도를 줄이며, 지역 최적점에 대한 강건성을 높입니다. 실험 결과, Gaussian-PSL은 비정형 파레토 전선을 학습하는 데 있어 기존 PSL 모델보다 우수한 성능을 보이며, 계산 효율성과 모델 단순성을 유지합니다. 이 연구는 복잡한 파레토 전선에서 효과적이고 확장 가능한 다목적 최적화의 새로운 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 다중 목표 최적화(MOO)는 여러 상충하는 목표를 포함하는 복잡한 현실 문제 해결에 필수적이다.
- 2. 기존의 Pareto Set Learning(PSL) 방법은 비정형적인 Pareto 집합의 다양성과 구조를 포착하는 데 한계가 있다.
- 3. Gaussian-PSL은 비볼록 Pareto 전선 문제를 해결하기 위해 Gaussian Splatting을 PSL에 통합한 새로운 프레임워크이다.
- 4. 제안된 방법은 선호 벡터 공간을 동적으로 분할하여 각 지역 내에서 단순한 MLP 네트워크가 지역화된 특징을 학습하도록 한다.
- 5. 실험 결과, Gaussian-PSL은 복잡한 Pareto 전선을 학습하는 데 있어 기존 PSL 모델보다 우수한 성능을 보였다.


---

*Generated on 2025-09-24 01:59:25*