---
keywords:
  - Bayesian Optimization
  - Gaussian Process
  - Pareto Set Identification
  - Adaptive Discretization
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2006.14061
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:04:15.069832",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Optimization",
    "Gaussian Process",
    "Pareto Set Identification",
    "Adaptive Discretization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Optimization": 0.85,
    "Gaussian Process": 0.78,
    "Pareto Set Identification": 0.72,
    "Adaptive Discretization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian Optimization",
        "canonical": "Bayesian Optimization",
        "aliases": [
          "BO"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian Optimization is a key concept in machine learning and optimization, providing strong connectivity with related topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.85
      },
      {
        "surface": "Gaussian Process",
        "canonical": "Gaussian Process",
        "aliases": [
          "GP"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian Processes are fundamental in probabilistic modeling, linking to a wide range of machine learning applications.",
        "novelty_score": 0.52,
        "connectivity_score": 0.82,
        "specificity_score": 0.71,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pareto Set Identification",
        "canonical": "Pareto Set Identification",
        "aliases": [
          "Pareto Optimization"
        ],
        "category": "unique_technical",
        "rationale": "This concept is specific to multi-objective optimization, offering unique insights and connections within optimization research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.69,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Adaptive Discretization",
        "canonical": "Adaptive Discretization",
        "aliases": [
          "Adaptive Sampling"
        ],
        "category": "unique_technical",
        "rationale": "Adaptive Discretization is a novel technique in optimization, enhancing the specificity and novelty of the research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.64,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "objective function",
      "noisy observation",
      "sample complexity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian Optimization",
      "resolved_canonical": "Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Gaussian Process",
      "resolved_canonical": "Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.82,
        "specificity": 0.71,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pareto Set Identification",
      "resolved_canonical": "Pareto Set Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.69,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Adaptive Discretization",
      "resolved_canonical": "Adaptive Discretization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.64,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Beyond Grids: Multi-objective Bayesian Optimization With Adaptive Discretization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2006.14061.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2006.14061](https://arxiv.org/abs/2006.14061)

## 🔗 유사한 논문
- [[2025-09-23/GaussianPSL_ A novel framework based on Gaussian Splatting for exploring the Pareto frontier in multi-criteria optimization_20250923|GaussianPSL: A novel framework based on Gaussian Splatting for exploring the Pareto frontier in multi-criteria optimization]] (85.9% similar)
- [[2025-09-23/Enhancing Performance and Calibration in Quantile Hyperparameter Optimization_20250923|Enhancing Performance and Calibration in Quantile Hyperparameter Optimization]] (85.4% similar)
- [[2025-09-23/Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm_20250923|Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm]] (83.7% similar)
- [[2025-09-23/Robust, Online, and Adaptive Decentralized Gaussian Processes_20250923|Robust, Online, and Adaptive Decentralized Gaussian Processes]] (83.5% similar)
- [[2025-09-22/Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems_20250922|Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Optimization|Bayesian Optimization]]
**🔗 Specific Connectable**: [[keywords/Gaussian Process|Gaussian Process]]
**⚡ Unique Technical**: [[keywords/Pareto Set Identification|Pareto Set Identification]], [[keywords/Adaptive Discretization|Adaptive Discretization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2006.14061v4 Announce Type: replace 
Abstract: We consider the problem of optimizing a vector-valued objective function $\boldsymbol{f}$ sampled from a Gaussian Process (GP) whose index set is a well-behaved, compact metric space $({\cal X},d)$ of designs. We assume that $\boldsymbol{f}$ is not known beforehand and that evaluating $\boldsymbol{f}$ at design $x$ results in a noisy observation of $\boldsymbol{f}(x)$. Since identifying the Pareto optimal designs via exhaustive search is infeasible when the cardinality of ${\cal X}$ is large, we propose an algorithm, called Adaptive $\boldsymbol{\epsilon}$-PAL, that exploits the smoothness of the GP-sampled function and the structure of $({\cal X},d)$ to learn fast. In essence, Adaptive $\boldsymbol{\epsilon}$-PAL employs a tree-based adaptive discretization technique to identify an $\boldsymbol{\epsilon}$-accurate Pareto set of designs in as few evaluations as possible. We provide both information-type and metric dimension-type bounds on the sample complexity of $\boldsymbol{\epsilon}$-accurate Pareto set identification. We also experimentally show that our algorithm outperforms other Pareto set identification methods.

## 📝 요약

이 논문은 가우시안 프로세스(GP)에서 샘플링된 벡터 값 목표 함수를 최적화하는 문제를 다룹니다. 목표 함수는 잘 정의된 컴팩트한 메트릭 공간에서 정의되며, 함수 평가 시 노이즈가 포함된 관측값을 얻습니다. 대규모 디자인 집합에서 파레토 최적 디자인을 식별하는 것은 비현실적이므로, 저자들은 'Adaptive $\boldsymbol{\epsilon}$-PAL'이라는 알고리즘을 제안합니다. 이 알고리즘은 GP 함수의 매끄러움과 메트릭 공간의 구조를 활용하여 빠르게 학습하며, 트리 기반의 적응적 이산화 기법을 통해 최소한의 평가로 $\boldsymbol{\epsilon}$-정확한 파레토 집합을 식별합니다. 또한, 정보형 및 메트릭 차원형 샘플 복잡도 경계를 제공하고, 실험적으로 다른 방법들보다 우수한 성능을 보임을 입증합니다.

## 🎯 주요 포인트

- 1. 본 논문은 Gaussian Process에서 샘플링된 벡터 값 목표 함수의 최적화를 다루고 있습니다.
- 2. 제안된 알고리즘인 Adaptive $\boldsymbol{\epsilon}$-PAL은 GP 샘플 함수의 매끄러움과 설계 공간의 구조를 활용하여 빠르게 학습합니다.
- 3. Adaptive $\boldsymbol{\epsilon}$-PAL은 트리 기반의 적응적 이산화 기법을 사용하여 $\boldsymbol{\epsilon}$-정확한 파레토 집합을 식별합니다.
- 4. 제안된 알고리즘의 샘플 복잡도에 대한 정보형 및 메트릭 차원형 경계를 제공합니다.
- 5. 실험 결과, 제안된 알고리즘이 다른 파레토 집합 식별 방법보다 우수한 성능을 보였습니다.


---

*Generated on 2025-09-25 17:04:15*