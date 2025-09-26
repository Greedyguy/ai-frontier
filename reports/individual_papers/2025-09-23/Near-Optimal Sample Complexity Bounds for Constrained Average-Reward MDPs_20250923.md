---
keywords:
  - Constrained Average-Reward MDP
  - Sample Complexity
  - Generative Model
  - Feasibility Settings
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16586
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:40:44.704749",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Constrained Average-Reward MDP",
    "Sample Complexity",
    "Generative Model",
    "Feasibility Settings"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Constrained Average-Reward MDP": 0.9,
    "Sample Complexity": 0.7,
    "Generative Model": 0.8,
    "Feasibility Settings": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "constrained average-reward MDP",
        "canonical": "Constrained Average-Reward MDP",
        "aliases": [
          "CAMDP"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a specific type of Markov decision process with constraints, which is crucial for linking related works.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "sample complexity",
        "canonical": "Sample Complexity",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Sample complexity is a fundamental concept in learning theory, relevant for connecting with other works on learning efficiency.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "generative model",
        "canonical": "Generative Model",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Generative models are widely used in machine learning, providing a strong link to related methodologies and applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "feasibility settings",
        "canonical": "Feasibility Settings",
        "aliases": [
          "relaxed feasibility",
          "strict feasibility"
        ],
        "category": "unique_technical",
        "rationale": "These settings are specific to the paper's approach and are important for understanding the constraints applied in the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "constrained average-reward MDP",
      "resolved_canonical": "Constrained Average-Reward MDP",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "sample complexity",
      "resolved_canonical": "Sample Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "generative model",
      "resolved_canonical": "Generative Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "feasibility settings",
      "resolved_canonical": "Feasibility Settings",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16586.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16586](https://arxiv.org/abs/2509.16586)

## 🔗 유사한 논문
- [[2025-09-18/Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain_20250918|Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain]] (84.9% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (82.8% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (82.1% similar)
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty: A Sample-Based Approach]] (81.8% similar)
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Sample Complexity|Sample Complexity]], [[keywords/Generative Model|Generative Model]]
**⚡ Unique Technical**: [[keywords/Constrained Average-Reward MDP|Constrained Average-Reward MDP]], [[keywords/Feasibility Settings|Feasibility Settings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16586v1 Announce Type: new 
Abstract: Recent advances have significantly improved our understanding of the sample complexity of learning in average-reward Markov decision processes (AMDPs) under the generative model. However, much less is known about the constrained average-reward MDP (CAMDP), where policies must satisfy long-run average constraints. In this work, we address this gap by studying the sample complexity of learning an $\epsilon$-optimal policy in CAMDPs under a generative model. We propose a model-based algorithm that operates under two settings: (i) relaxed feasibility, which allows small constraint violations, and (ii) strict feasibility, where the output policy satisfies the constraint. We show that our algorithm achieves sample complexities of $\tilde{O}\left(\frac{S A (B+H)}{ \epsilon^2}\right)$ and $\tilde{O} \left(\frac{S A (B+H)}{\epsilon^2 \zeta^2} \right)$ under the relaxed and strict feasibility settings, respectively. Here, $\zeta$ is the Slater constant indicating the size of the feasible region, $H$ is the span bound of the bias function, and $B$ is the transient time bound. Moreover, a matching lower bound of $\tilde{\Omega}\left(\frac{S A (B+H)}{ \epsilon^2\zeta^2}\right)$ for the strict feasibility case is established, thus providing the first minimax-optimal bounds for CAMDPs. Our results close the theoretical gap in understanding the complexity of constrained average-reward MDPs.

## 📝 요약

이 논문은 생성 모델 하에서 제약된 평균 보상 마르코프 결정 과정(CAMDP)의 샘플 복잡성을 연구합니다. 저자들은 $\epsilon$-최적 정책을 학습하기 위한 모델 기반 알고리즘을 제안하며, (i) 작은 제약 위반을 허용하는 완화된 타당성 설정과 (ii) 제약을 만족하는 엄격한 타당성 설정 두 가지를 다룹니다. 제안된 알고리즘은 각각 $\tilde{O}\left(\frac{S A (B+H)}{ \epsilon^2}\right)$와 $\tilde{O} \left(\frac{S A (B+H)}{\epsilon^2 \zeta^2} \right)$의 샘플 복잡성을 달성하며, 여기서 $\zeta$는 슬레이터 상수, $H$는 편향 함수의 범위, $B$는 과도 시간 한계를 나타냅니다. 또한, 엄격한 타당성 경우에 대한 하한을 제시하여 CAMDP의 복잡성에 대한 이론적 격차를 해소합니다.

## 🎯 주요 포인트

- 1. 평균 보상 마르코프 결정 과정(AMDP)의 표본 복잡성에 대한 이해가 최근 크게 향상되었다.
- 2. 제한된 평균 보상 MDP(CAMDP)의 학습 표본 복잡성을 연구하여 이론적 격차를 해소하였다.
- 3. 제안된 알고리즘은 완화된 타당성과 엄격한 타당성 두 가지 설정에서 작동하며, 각각의 표본 복잡성을 달성한다.
- 4. 엄격한 타당성 설정에서의 하한을 제공하여 CAMDP에 대한 첫 번째 미니맥스 최적 경계를 제시하였다.
- 5. 연구 결과는 제한된 평균 보상 MDP의 복잡성에 대한 이론적 이해를 완성하였다.


---

*Generated on 2025-09-24 01:40:44*