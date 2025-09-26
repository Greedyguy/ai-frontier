---
keywords:
  - Belief Propagation
  - Normalizing Flows
  - Bernstein Polynomials
  - Nonlinear Dynamics
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15533
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:29:08.371883",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Belief Propagation",
    "Normalizing Flows",
    "Bernstein Polynomials",
    "Nonlinear Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Belief Propagation": 0.82,
    "Normalizing Flows": 0.79,
    "Bernstein Polynomials": 0.77,
    "Nonlinear Dynamics": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Belief Propagation",
        "canonical": "Belief Propagation",
        "aliases": [
          "BP"
        ],
        "category": "specific_connectable",
        "rationale": "Belief Propagation is a key concept in reasoning under uncertainty and connects well with stochastic systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Normalizing Flows",
        "canonical": "Normalizing Flows",
        "aliases": [
          "NF"
        ],
        "category": "unique_technical",
        "rationale": "Normalizing Flows are crucial for density estimation in the proposed model, offering a unique approach to stochastic dynamics.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Bernstein Polynomials",
        "canonical": "Bernstein Polynomials",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Bernstein Polynomials provide analytical tractability, essential for the model's theoretical foundation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Nonlinear Dynamics",
        "canonical": "Nonlinear Dynamics",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Nonlinear Dynamics are central to the challenges addressed in the paper, linking to broader stochastic system studies.",
        "novelty_score": 0.48,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "stochastic system",
      "future states",
      "approximate methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Belief Propagation",
      "resolved_canonical": "Belief Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Normalizing Flows",
      "resolved_canonical": "Normalizing Flows",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Bernstein Polynomials",
      "resolved_canonical": "Bernstein Polynomials",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Nonlinear Dynamics",
      "resolved_canonical": "Nonlinear Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows

**Korean Title:** 확률적 동역학의 보편적 학습을 위한 베르누이 정규화 흐름을 사용한 정확한 신념 전파

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15533.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15533](https://arxiv.org/abs/2509.15533)

## 🔗 유사한 논문
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (80.5% similar)
- [[2025-09-22/A Unified Theory of Exact Inference and Learning in Exponential Family Latent Variable Models_20250922|A Unified Theory of Exact Inference and Learning in Exponential Family Latent Variable Models]] (80.1% similar)
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (79.6% similar)
- [[2025-09-22/A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations_20250922|A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations]] (79.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonlinear Dynamics|Nonlinear Dynamics]]
**🔗 Specific Connectable**: [[keywords/Belief Propagation|Belief Propagation]]
**⚡ Unique Technical**: [[keywords/Normalizing Flows|Normalizing Flows]], [[keywords/Bernstein Polynomials|Bernstein Polynomials]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15533v1 Announce Type: new 
Abstract: Predicting the distribution of future states in a stochastic system, known as belief propagation, is fundamental to reasoning under uncertainty. However, nonlinear dynamics often make analytical belief propagation intractable, requiring approximate methods. When the system model is unknown and must be learned from data, a key question arises: can we learn a model that (i) universally approximates general nonlinear stochastic dynamics, and (ii) supports analytical belief propagation? This paper establishes the theoretical foundations for a class of models that satisfy both properties. The proposed approach combines the expressiveness of normalizing flows for density estimation with the analytical tractability of Bernstein polynomials. Empirical results show the efficacy of our learned model over state-of-the-art data-driven methods for belief propagation, especially for highly non-linear systems with non-additive, non-Gaussian noise.

## 🔍 Abstract (한글 번역)

arXiv:2509.15533v1 발표 유형: 신규  
초록: 확률적 시스템에서 미래 상태의 분포를 예측하는 것, 즉 신념 전파는 불확실성 하에서의 추론에 있어 기본적입니다. 그러나 비선형 동역학은 종종 분석적 신념 전파를 불가능하게 만들어, 근사 방법을 필요로 합니다. 시스템 모델이 알려지지 않았고 데이터로부터 학습되어야 할 때, 중요한 질문이 제기됩니다: (i) 일반적인 비선형 확률 동역학을 보편적으로 근사할 수 있고, (ii) 분석적 신념 전파를 지원할 수 있는 모델을 학습할 수 있는가? 본 논문은 두 가지 속성을 만족하는 모델 클래스의 이론적 기초를 확립합니다. 제안된 접근법은 밀도 추정을 위한 정규화 흐름의 표현력과 베른스타인 다항식의 분석적 취급 가능성을 결합합니다. 실험 결과는 비선형성이 매우 높고 비가우시안 잡음이 있는 시스템에 대해, 데이터 기반의 최신 방법들보다 우리의 학습된 모델이 신념 전파에 있어 효과적임을 보여줍니다.

## 📝 요약

이 논문은 비선형 확률 시스템에서 미래 상태의 분포를 예측하는 신념 전파 문제를 다룹니다. 저자들은 일반적인 비선형 확률 동역학을 보편적으로 근사하고, 신념 전파를 분석적으로 지원할 수 있는 모델을 학습할 수 있는지를 탐구합니다. 이를 위해 밀도 추정을 위한 정규화 흐름과 분석적 용이성을 제공하는 Bernstein 다항식을 결합한 새로운 모델을 제안합니다. 실험 결과, 제안된 모델은 비선형 시스템에서 기존 데이터 기반 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 비선형 동적 시스템에서의 신념 전파는 불확실성 하에서의 추론에 필수적이다.
- 2. 본 논문은 일반적인 비선형 확률 동역학을 보편적으로 근사하고 분석적 신념 전파를 지원하는 모델의 이론적 기초를 확립한다.
- 3. 제안된 접근법은 밀도 추정을 위한 정규화 흐름과 Bernstein 다항식의 분석적 처리 용이성을 결합한다.
- 4. 실험 결과, 제안된 모델은 비선형 시스템에서의 신념 전파에 있어 최신 데이터 기반 방법들보다 우수한 성능을 보였다.
- 5. 특히 비가우시안 잡음이 있는 비선형 시스템에서 제안된 모델의 효과가 두드러진다.


---

*Generated on 2025-09-23 10:29:08*