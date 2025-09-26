<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:13:40.708491",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Policy Mirror Descent",
    "Temporal Difference Learning",
    "Machine Learning",
    "Generative Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Policy Mirror Descent": 0.8,
    "Temporal Difference Learning": 0.75,
    "Machine Learning": 0.7,
    "Generative Model": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Policy Mirror Descent",
        "canonical": "Policy Mirror Descent",
        "aliases": [
          "PMD"
        ],
        "category": "unique_technical",
        "rationale": "A specific reinforcement learning framework that is central to the paper's contributions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Temporal Difference Evaluation",
        "canonical": "Temporal Difference Learning",
        "aliases": [
          "TD Learning",
          "TD Evaluation"
        ],
        "category": "specific_connectable",
        "rationale": "A key method in reinforcement learning that connects to broader temporal difference methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental area of machine learning that underpins the study.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Generative Model",
        "canonical": "Generative Model",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Important for understanding sample complexity in the context of the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "result",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Policy Mirror Descent",
      "resolved_canonical": "Policy Mirror Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Temporal Difference Evaluation",
      "resolved_canonical": "Temporal Difference Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Generative Model",
      "resolved_canonical": "Generative Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# On the Convergence of Policy Mirror Descent with Temporal Difference Evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18822.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18822](https://arxiv.org/abs/2509.18822)

## 🔗 유사한 논문
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (83.4% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.2% similar)
- [[2025-09-23/Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs_20250923|Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs]] (81.9% similar)
- [[2025-09-23/Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm_20250923|Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm]] (81.7% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Temporal Difference Learning|Temporal Difference Learning]], [[keywords/Generative Model|Generative Model]]
**⚡ Unique Technical**: [[keywords/Policy Mirror Descent|Policy Mirror Descent]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18822v1 Announce Type: cross 
Abstract: Policy mirror descent (PMD) is a general policy optimization framework in reinforcement learning, which can cover a wide range of typical policy optimization methods by specifying different mirror maps. Existing analysis of PMD requires exact or approximate evaluation (for example unbiased estimation via Monte Carlo simulation) of action values solely based on policy. In this paper, we consider policy mirror descent with temporal difference evaluation (TD-PMD). It is shown that, given the access to exact policy evaluations, the dimension-free $O(1/T)$ sublinear convergence still holds for TD-PMD with any constant step size and any initialization. In order to achieve this result, new monotonicity and shift invariance arguments have been developed. The dimension free $\gamma$-rate linear convergence of TD-PMD is also established provided the step size is selected adaptively. For the two common instances of TD-PMD (i.e., TD-PQA and TD-NPG), it is further shown that they enjoy the convergence in the policy domain. Additionally, we investigate TD-PMD in the inexact setting and give the sample complexity for it to achieve the last iterate $\varepsilon$-optimality under a generative model, which improves the last iterate sample complexity for PMD over the dependence on $1/(1-\gamma)$.

## 📝 요약

이 논문은 강화 학습에서 정책 최적화 프레임워크인 정책 미러 강하(PMD)의 변형인 TD-PMD를 제안합니다. 기존 PMD 분석은 정책에 기반한 행동 가치의 정확한 평가를 요구하지만, 이 연구에서는 시차 차이 평가를 사용하는 TD-PMD를 도입하여 이러한 제한을 완화합니다. TD-PMD는 정확한 정책 평가가 가능할 때, 차원에 상관없이 $O(1/T)$의 수렴 속도를 유지하며, 적응적인 스텝 크기를 선택하면 선형 수렴도 가능합니다. TD-PQA와 TD-NPG 같은 TD-PMD의 일반적인 사례에서도 정책 도메인 내 수렴이 확인되었습니다. 또한, 생성 모델 하에서 근사 설정에서의 샘플 복잡성을 분석하여, 기존 PMD보다 $1/(1-\gamma)$에 대한 의존성을 개선했습니다.

## 🎯 주요 포인트

- 1. 정책 미러 하강(PMD)은 강화 학습에서 다양한 정책 최적화 방법을 포괄할 수 있는 일반적인 정책 최적화 프레임워크입니다.
- 2. 본 논문에서는 시차 차이 평가(TD)를 사용하는 정책 미러 하강(TD-PMD)을 고려합니다.
- 3. TD-PMD는 정확한 정책 평가에 접근할 수 있을 때, 차원에 무관하게 $O(1/T)$의 수렴 속도를 유지합니다.
- 4. TD-PMD의 두 가지 일반적인 사례(TD-PQA 및 TD-NPG)는 정책 도메인에서의 수렴성을 보장합니다.
- 5. 생성 모델 하에서 TD-PMD의 샘플 복잡성을 분석하여, 마지막 반복에서 $\varepsilon$-최적성을 달성하는 데 필요한 샘플 복잡성을 개선합니다.


---

*Generated on 2025-09-24 15:13:40*