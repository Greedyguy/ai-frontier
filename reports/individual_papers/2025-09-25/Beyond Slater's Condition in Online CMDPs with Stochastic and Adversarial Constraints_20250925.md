---
keywords:
  - Constrained Markov Decision Processes
  - Stochastic Constraints
  - Adversarial Constraints
  - Positive Constraint Violation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20114
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:45:09.440419",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Constrained Markov Decision Processes",
    "Stochastic Constraints",
    "Adversarial Constraints",
    "Positive Constraint Violation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Constrained Markov Decision Processes": 0.8,
    "Stochastic Constraints": 0.7,
    "Adversarial Constraints": 0.78,
    "Positive Constraint Violation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Constrained Markov Decision Processes",
        "canonical": "Constrained Markov Decision Processes",
        "aliases": [
          "CMDPs"
        ],
        "category": "unique_technical",
        "rationale": "CMDPs are central to the paper's focus and are specific enough to warrant unique technical categorization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "stochastic constraints",
        "canonical": "Stochastic Constraints",
        "aliases": [
          "random constraints"
        ],
        "category": "specific_connectable",
        "rationale": "Stochastic constraints are a key aspect of the CMDP framework discussed, enabling connections to probabilistic modeling.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "adversarial constraints",
        "canonical": "Adversarial Constraints",
        "aliases": [
          "dynamic constraints"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial constraints highlight the adaptation to changing environments, relevant for linking to robust optimization.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "positive constraint violation",
        "canonical": "Positive Constraint Violation",
        "aliases": [
          "strict constraint violation"
        ],
        "category": "unique_technical",
        "rationale": "This concept is novel and specific to the paper's approach, offering a new perspective on constraint handling.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Constrained Markov Decision Processes",
      "resolved_canonical": "Constrained Markov Decision Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "stochastic constraints",
      "resolved_canonical": "Stochastic Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "adversarial constraints",
      "resolved_canonical": "Adversarial Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "positive constraint violation",
      "resolved_canonical": "Positive Constraint Violation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Beyond Slater's Condition in Online CMDPs with Stochastic and Adversarial Constraints

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20114.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20114](https://arxiv.org/abs/2509.20114)

## 🔗 유사한 논문
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty: A Sample-Based Approach]] (82.8% similar)
- [[2025-09-23/Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs_20250923|Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs]] (82.2% similar)
- [[2025-09-25/Analysis of approximate linear programming solution to Markov decision problem with log barrier function_20250925|Analysis of approximate linear programming solution to Markov decision problem with log barrier function]] (82.1% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (81.9% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Stochastic Constraints|Stochastic Constraints]], [[keywords/Adversarial Constraints|Adversarial Constraints]]
**⚡ Unique Technical**: [[keywords/Constrained Markov Decision Processes|Constrained Markov Decision Processes]], [[keywords/Positive Constraint Violation|Positive Constraint Violation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20114v1 Announce Type: new 
Abstract: We study \emph{online episodic Constrained Markov Decision Processes} (CMDPs) under both stochastic and adversarial constraints. We provide a novel algorithm whose guarantees greatly improve those of the state-of-the-art best-of-both-worlds algorithm introduced by Stradi et al. (2025). In the stochastic regime, \emph{i.e.}, when the constraints are sampled from fixed but unknown distributions, our method achieves $\widetilde{\mathcal{O}}(\sqrt{T})$ regret and constraint violation without relying on Slater's condition, thereby handling settings where no strictly feasible solution exists. Moreover, we provide guarantees on the stronger notion of \emph{positive} constraint violation, which does not allow to recover from large violation in the early episodes by playing strictly safe policies. In the adversarial regime, \emph{i.e.}, when the constraints may change arbitrarily between episodes, our algorithm ensures sublinear constraint violation without Slater's condition, and achieves sublinear $\alpha$-regret with respect to the \emph{unconstrained} optimum, where $\alpha$ is a suitably defined multiplicative approximation factor. We further validate our results through synthetic experiments, showing the practical effectiveness of our algorithm.

## 📝 요약

이 논문은 확률적 및 적대적 제약 조건 하에서 온라인 에피소드 제약 마르코프 결정 프로세스(CMDP)를 연구합니다. 저자들은 Stradi 등(2025)이 제안한 기존 알고리즘을 개선한 새로운 알고리즘을 제시합니다. 확률적 환경에서는 제약 조건이 고정된 분포에서 샘플링될 때, Slater 조건 없이도 $\widetilde{\mathcal{O}}(\sqrt{T})$의 후회와 제약 위반을 달성합니다. 이는 엄격히 실행 가능한 해가 없는 상황에서도 적용 가능합니다. 또한, 초기 에피소드에서의 큰 위반을 회복할 수 없는 '긍정적' 제약 위반에 대한 보장을 제공합니다. 적대적 환경에서는 에피소드 간 제약 조건이 임의로 변할 수 있을 때, Slater 조건 없이도 서브리니어 제약 위반을 보장하고, 비제약 최적값에 대한 서브리니어 $\alpha$-후회를 달성합니다. 실험을 통해 알고리즘의 실용성을 검증하였습니다.

## 🎯 주요 포인트

- 1. 본 연구는 온라인 에피소드 제약 마르코프 결정 프로세스(CMDP)를 확률적 및 적대적 제약 조건 하에서 다룹니다.
- 2. 제안된 알고리즘은 기존의 최첨단 알고리즘보다 개선된 성능을 보이며, Slater 조건 없이도 $\widetilde{\mathcal{O}}(\sqrt{T})$의 후회와 제약 위반을 달성합니다.
- 3. 확률적 제약 조건 하에서, 초기 에피소드에서의 큰 위반을 회복할 수 없는 강한 제약 위반 개념에 대한 보장을 제공합니다.
- 4. 적대적 제약 조건 하에서는 Slater 조건 없이도 서브리니어 제약 위반과 $\alpha$-후회를 달성합니다.
- 5. 합성 실험을 통해 제안된 알고리즘의 실용적 효과를 검증했습니다.


---

*Generated on 2025-09-25 16:45:09*