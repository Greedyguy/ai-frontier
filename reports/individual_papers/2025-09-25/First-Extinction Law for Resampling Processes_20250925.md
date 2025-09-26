---
keywords:
  - Resampling Processes
  - First-Extinction Time
  - Wright-Fisher Model
  - Model Collapse
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20101
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:00:45.542540",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Resampling Processes",
    "First-Extinction Time",
    "Wright-Fisher Model",
    "Model Collapse"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Resampling Processes": 0.78,
    "First-Extinction Time": 0.77,
    "Wright-Fisher Model": 0.8,
    "Model Collapse": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "resampling processes",
        "canonical": "Resampling Processes",
        "aliases": [
          "resampling",
          "sampling processes"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on extinction dynamics, offering unique insights into probabilistic modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "first-extinction time",
        "canonical": "First-Extinction Time",
        "aliases": [
          "extinction time"
        ],
        "category": "unique_technical",
        "rationale": "Key concept introduced by the paper, crucial for understanding the dynamics of model collapse.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Wright-Fisher result",
        "canonical": "Wright-Fisher Model",
        "aliases": [
          "Wright-Fisher"
        ],
        "category": "specific_connectable",
        "rationale": "Links to established genetic drift models, enhancing cross-disciplinary connections.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "model collapse",
        "canonical": "Model Collapse",
        "aliases": [
          "collapse",
          "model failure"
        ],
        "category": "evolved_concepts",
        "rationale": "Emerging concept in machine learning related to stability and robustness of models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "multinomial updates",
      "zero drift",
      "extensive simulations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "resampling processes",
      "resolved_canonical": "Resampling Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "first-extinction time",
      "resolved_canonical": "First-Extinction Time",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Wright-Fisher result",
      "resolved_canonical": "Wright-Fisher Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "model collapse",
      "resolved_canonical": "Model Collapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# First-Extinction Law for Resampling Processes

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20101.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20101](https://arxiv.org/abs/2509.20101)

## 🔗 유사한 논문
- [[2025-09-23/Absorb and Converge_ Provable Convergence Guarantee for Absorbing Discrete Diffusion Models_20250923|Absorb and Converge: Provable Convergence Guarantee for Absorbing Discrete Diffusion Models]] (79.4% similar)
- [[2025-09-23/Discrete Diffusion Models_ Novel Analysis and New Sampler Guarantees_20250923|Discrete Diffusion Models: Novel Analysis and New Sampler Guarantees]] (78.3% similar)
- [[2025-09-19/Gap-Dependent Bounds for Federated $Q$-learning_20250919|Gap-Dependent Bounds for Federated $Q$-learning]] (77.6% similar)
- [[2025-09-24/Accounting for Uncertainty in Machine Learning Surrogates_ A Gauss-Hermite Quadrature Approach to Reliability Analysis_20250924|Accounting for Uncertainty in Machine Learning Surrogates: A Gauss-Hermite Quadrature Approach to Reliability Analysis]] (77.5% similar)
- [[2025-09-25/From Samples to Scenarios_ A New Paradigm for Probabilistic Forecasting_20250925|From Samples to Scenarios: A New Paradigm for Probabilistic Forecasting]] (77.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Wright-Fisher Model|Wright-Fisher Model]]
**⚡ Unique Technical**: [[keywords/Resampling Processes|Resampling Processes]], [[keywords/First-Extinction Time|First-Extinction Time]]
**🚀 Evolved Concepts**: [[keywords/Model Collapse|Model Collapse]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20101v1 Announce Type: cross 
Abstract: Extinction times in resampling processes are fundamental yet often intractable, as previous formulas scale as $2^M$ with the number of states $M$ present in the initial probability distribution. We solve this by treating multinomial updates as independent square-root diffusions of zero drift, yielding a closed-form law for the first-extinction time. We prove that the mean coincides exactly with the Wright-Fisher result of Baxter et al., thereby replacing exponential-cost evaluations with a linear-cost expression, and we validate this result through extensive simulations. Finally, we demonstrate predictive power for model collapse in a simple self-training setup: the onset of collapse coincides with the resampling-driven first-extinction time computed from the model's initial stationary distribution. These results hint to a unified view of resampling extinction dynamics.

## 📝 요약

이 논문은 재표본화 과정에서 멸종 시간을 분석하는 새로운 방법을 제시합니다. 기존의 방법은 상태 수 $M$에 따라 $2^M$의 복잡도를 가지지만, 저자들은 다항식 업데이트를 독립적인 제곱근 확산으로 처리하여 멸종 시간을 계산하는 폐쇄형 법칙을 도출했습니다. 이 방법은 평균적으로 Baxter 등의 Wright-Fisher 결과와 일치하며, 지수적 비용을 선형 비용으로 대체합니다. 또한, 간단한 자기 학습 모델에서 예측력을 입증하며, 모델 붕괴의 시작이 초기 정적 분포에서 계산된 멸종 시간과 일치함을 보여줍니다. 이는 재표본화 멸종 동역학에 대한 통합된 관점을 제공합니다.

## 🎯 주요 포인트

- 1. 기존의 멸종 시간 공식은 상태 수 $M$에 따라 $2^M$로 확장되어 계산이 어려웠으나, 제안된 방법은 독립적인 제곱근 확산으로 멸종 시간을 계산하여 이를 해결합니다.
- 2. 제안된 방법은 Baxter 등의 Wright-Fisher 결과와 정확히 일치하는 평균값을 제공하며, 지수적 비용 평가를 선형적 비용 표현으로 대체합니다.
- 3. 광범위한 시뮬레이션을 통해 제안된 방법의 유효성을 검증하였습니다.
- 4. 간단한 자기 학습 환경에서 모델 붕괴 예측에 대한 새로운 통찰을 제공하며, 붕괴의 시작은 초기 확률 분포에서 계산된 첫 멸종 시간과 일치합니다.
- 5. 이 연구는 재샘플링 멸종 역학에 대한 통합된 관점을 제시합니다.


---

*Generated on 2025-09-25 17:00:45*