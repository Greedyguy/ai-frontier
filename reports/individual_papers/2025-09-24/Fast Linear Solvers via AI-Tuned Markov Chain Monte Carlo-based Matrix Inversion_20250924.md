<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:51:35.785454",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Markov Chain Monte Carlo",
    "Graph Neural Network",
    "Bayesian Optimization",
    "Krylov Subspace Methods"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Markov Chain Monte Carlo": 0.82,
    "Graph Neural Network": 0.79,
    "Bayesian Optimization": 0.78,
    "Krylov Subspace Methods": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Markov Chain Monte Carlo",
        "canonical": "Markov Chain Monte Carlo",
        "aliases": [
          "MCMC"
        ],
        "category": "specific_connectable",
        "rationale": "MCMC is a key technique for matrix inversion and preconditioning, linking it to probabilistic methods in computational mathematics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Graph Neural Surrogate",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN surrogate"
        ],
        "category": "specific_connectable",
        "rationale": "The use of a graph neural surrogate highlights the application of GNNs in predicting preconditioning speed, connecting it to neural network advancements.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Bayesian Acquisition Function",
        "canonical": "Bayesian Optimization",
        "aliases": [
          "Bayesian acquisition"
        ],
        "category": "unique_technical",
        "rationale": "This function is crucial for selecting optimal MCMC parameters, linking to Bayesian methods in optimization.",
        "novelty_score": 0.72,
        "connectivity_score": 0.77,
        "specificity_score": 0.83,
        "link_intent_score": 0.78
      },
      {
        "surface": "Krylov Subspace Solvers",
        "canonical": "Krylov Subspace Methods",
        "aliases": [
          "Krylov solvers"
        ],
        "category": "specific_connectable",
        "rationale": "These solvers are fundamental in solving sparse linear systems, connecting to numerical linear algebra techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "AI-driven framework",
      "large-scale systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Markov Chain Monte Carlo",
      "resolved_canonical": "Markov Chain Monte Carlo",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Graph Neural Surrogate",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Bayesian Acquisition Function",
      "resolved_canonical": "Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.77,
        "specificity": 0.83,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Krylov Subspace Solvers",
      "resolved_canonical": "Krylov Subspace Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Fast Linear Solvers via AI-Tuned Markov Chain Monte Carlo-based Matrix Inversion

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18452.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18452](https://arxiv.org/abs/2509.18452)

## 🔗 유사한 논문
- [[2025-09-23/A geometric framework for momentum-based optimizers for low-rank training_20250923|A geometric framework for momentum-based optimizers for low-rank training]] (81.0% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (80.6% similar)
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (80.1% similar)
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (79.8% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Markov Chain Monte Carlo|Markov Chain Monte Carlo]], [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Krylov Subspace Methods|Krylov Subspace Methods]]
**⚡ Unique Technical**: [[keywords/Bayesian Optimization|Bayesian Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18452v1 Announce Type: new 
Abstract: Large, sparse linear systems are pervasive in modern science and engineering, and Krylov subspace solvers are an established means of solving them. Yet convergence can be slow for ill-conditioned matrices, so practical deployments usually require preconditioners. Markov chain Monte Carlo (MCMC)-based matrix inversion can generate such preconditioners and accelerate Krylov iterations, but its effectiveness depends on parameters whose optima vary across matrices; manual or grid search is costly. We present an AI-driven framework recommending MCMC parameters for a given linear system. A graph neural surrogate predicts preconditioning speed from $A$ and MCMC parameters. A Bayesian acquisition function then chooses the parameter sets most likely to minimise iterations. On a previously unseen ill-conditioned system, the framework achieves better preconditioning with 50\% of the search budget of conventional methods, yielding about a 10\% reduction in iterations to convergence. These results suggest a route for incorporating MCMC-based preconditioners into large-scale systems.

## 📝 요약

이 논문은 대규모 희소 선형 시스템을 해결하기 위한 AI 기반 프레임워크를 제안합니다. Krylov 부분 공간 해법은 이러한 시스템을 해결하는 데 널리 사용되지만, 조건이 나쁜 행렬에서는 수렴이 느려질 수 있어 전처리기가 필요합니다. 저자들은 MCMC 기반의 행렬 반전을 통해 전처리기를 생성하고 Krylov 반복을 가속화할 수 있음을 보여줍니다. 그러나 MCMC의 효과는 행렬에 따라 최적의 매개변수가 달라지므로, 이를 수동으로 찾는 것은 비용이 많이 듭니다. 제안된 프레임워크는 그래프 신경망을 통해 전처리 속도를 예측하고, 베이지안 획득 함수를 사용해 반복 횟수를 최소화할 수 있는 매개변수를 추천합니다. 이 방법은 기존 방법 대비 50% 적은 탐색 비용으로 약 10%의 반복 횟수 감소를 달성했습니다. 이는 대규모 시스템에서 MCMC 기반 전처리기를 효과적으로 통합할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 희소 선형 시스템에서 Krylov 부분 공간 해법의 수렴 속도를 개선하기 위해 MCMC 기반 행렬 역행렬이 사용될 수 있다.
- 2. MCMC 기반 전처리기의 효과는 행렬에 따라 최적의 파라미터가 달라지며, 이를 수동으로 찾거나 그리드 탐색하는 것은 비용이 많이 든다.
- 3. 제안된 AI 기반 프레임워크는 주어진 선형 시스템에 대해 MCMC 파라미터를 추천하여, 수렴을 위한 반복 횟수를 줄인다.
- 4. 그래프 신경망 대리 모델이 행렬 $A$와 MCMC 파라미터로부터 전처리 속도를 예측하고, 베이지안 획득 함수가 반복 횟수를 최소화할 가능성이 높은 파라미터 세트를 선택한다.
- 5. 새로운 악조건 시스템에서 프레임워크는 기존 방법의 탐색 예산의 50%로 더 나은 전처리를 달성하며, 약 10%의 수렴 반복 횟수 감소를 이끌어낸다.


---

*Generated on 2025-09-24 14:51:35*