---
keywords:
  - Generalized Momentum Methods
  - Risk-Sensitive Index
  - Large-Deviation Principle
  - Smooth Strongly Convex Functions
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.13628
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:25:10.267053",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generalized Momentum Methods",
    "Risk-Sensitive Index",
    "Large-Deviation Principle",
    "Smooth Strongly Convex Functions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generalized Momentum Methods": 0.78,
    "Risk-Sensitive Index": 0.77,
    "Large-Deviation Principle": 0.79,
    "Smooth Strongly Convex Functions": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generalized Momentum Methods",
        "canonical": "Generalized Momentum Methods",
        "aliases": [
          "GMMs"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's analysis and offers a unique perspective on momentum methods, which are crucial for linking with optimization literature.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Risk-Sensitive Index",
        "canonical": "Risk-Sensitive Index",
        "aliases": [
          "RSI"
        ],
        "category": "unique_technical",
        "rationale": "RSI is a novel metric introduced in the paper, providing a new dimension to robustness analysis in optimization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Large-Deviation Principle",
        "canonical": "Large-Deviation Principle",
        "aliases": [
          "LDP"
        ],
        "category": "specific_connectable",
        "rationale": "The large-deviation principle is a significant concept in probability theory, relevant for linking with statistical analysis in optimization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Smooth Strongly Convex Functions",
        "canonical": "Smooth Strongly Convex Functions",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in optimization theory, critical for understanding the context of the paper's results.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "gradient errors",
      "quadratic objectives",
      "Gaussian noise"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Generalized Momentum Methods",
      "resolved_canonical": "Generalized Momentum Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Risk-Sensitive Index",
      "resolved_canonical": "Risk-Sensitive Index",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Large-Deviation Principle",
      "resolved_canonical": "Large-Deviation Principle",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Smooth Strongly Convex Functions",
      "resolved_canonical": "Smooth Strongly Convex Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds

**Korean Title:** 편향된 그래디언트 추정치를 사용하는 가속 그래디언트 방법: 위험 민감성, 높은 확률 보장, 및 큰 편차 경계

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13628.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.13628](https://arxiv.org/abs/2509.13628)

## 🔗 유사한 논문
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (83.3% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (83.0% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (81.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (81.5% similar)
- [[2025-09-18/Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain_20250918|Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Smooth Strongly Convex Functions|Smooth Strongly Convex Functions]]
**🔗 Specific Connectable**: [[keywords/Large-Deviation Principle|Large-Deviation Principle]]
**⚡ Unique Technical**: [[keywords/Generalized Momentum Methods|Generalized Momentum Methods]], [[keywords/Risk-Sensitive Index|Risk-Sensitive Index]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13628v2 Announce Type: replace-cross 
Abstract: We study trade-offs between convergence rate and robustness to gradient errors in the context of first-order methods. Our focus is on generalized momentum methods (GMMs)--a broad class that includes Nesterov's accelerated gradient, heavy-ball, and gradient descent methods--for minimizing smooth strongly convex objectives. We allow stochastic gradient errors that may be adversarial and biased, and quantify robustness of these methods to gradient errors via the risk-sensitive index (RSI) from robust control theory. For quadratic objectives with i.i.d. Gaussian noise, we give closed form expressions for RSI in terms of solutions to 2x2 matrix Riccati equations, revealing a Pareto frontier between RSI and convergence rate over the choice of step-size and momentum parameters. We then prove a large-deviation principle for time-averaged suboptimality in the large iteration limit and show that the rate function is, up to a scaling, the convex conjugate of the RSI function. We further show that the rate function and RSI are linked to the $H_\infty$-norm--a measure of robustness to the worst-case deterministic gradient errors--so that stronger worst-case robustness (smaller $H_\infty$-norm) leads to sharper decay of the tail probabilities for the average suboptimality. Beyond quadratics, under potentially biased sub-Gaussian gradient errors, we derive non-asymptotic bounds on a finite-time analogue of the RSI, yielding finite-time high-probability guarantees and non-asymptotic large-deviation bounds for the averaged iterates. In the case of smooth strongly convex functions, we also observe an analogous trade-off between RSI and convergence-rate bounds. To our knowledge, these are the first non-asymptotic guarantees for GMMs with biased gradients and the first risk-sensitive analysis of GMMs. Finally, we provide numerical experiments on a robust regression problem to illustrate our results.

## 🔍 Abstract (한글 번역)

arXiv:2509.13628v2 발표 유형: 교차 교체  
초록: 우리는 1차 방법의 맥락에서 수렴 속도와 그래디언트 오류에 대한 강건성 간의 상충 관계를 연구합니다. 우리의 초점은 매끄럽고 강하게 볼록한 목적을 최소화하기 위한 일반화된 모멘텀 방법(GMMs)입니다. 이 클래스에는 Nesterov의 가속 그래디언트, 무거운 공, 그래디언트 하강 방법이 포함됩니다. 우리는 적대적이고 편향된 확률적 그래디언트 오류를 허용하며, 강건 제어 이론의 위험 민감 지수(RSI)를 통해 이러한 방법의 그래디언트 오류에 대한 강건성을 정량화합니다. 독립 동일 분포의 가우시안 잡음을 가진 이차 목적에 대해, 우리는 2x2 행렬 리카티 방정식의 해를 통해 RSI에 대한 닫힌 형식 표현을 제공하여, 스텝 크기 및 모멘텀 매개변수 선택에 따른 RSI와 수렴 속도 간의 파레토 전선을 드러냅니다. 그런 다음 우리는 큰 반복 한계에서 시간 평균 하위 최적성에 대한 대편차 원리를 증명하고, 그 비율 함수가 스케일링에 따라 RSI 함수의 볼록 켤레임을 보여줍니다. 우리는 또한 비율 함수와 RSI가 최악의 결정론적 그래디언트 오류에 대한 강건성의 척도인 $H_\infty$-노름과 연결되어 있음을 보여, 더 강한 최악의 강건성(더 작은 $H_\infty$-노름)이 평균 하위 최적성에 대한 꼬리 확률의 더 날카로운 감소를 초래함을 보여줍니다. 이차 함수 외에도, 잠재적으로 편향된 서브 가우시안 그래디언트 오류 하에서, 우리는 RSI의 유한 시간 유사체에 대한 비대칭 경계를 도출하여 유한 시간 고확률 보장과 평균 반복에 대한 비대칭 대편차 경계를 제공합니다. 매끄럽고 강하게 볼록한 함수의 경우, 우리는 또한 RSI와 수렴 속도 경계 간의 유사한 상충 관계를 관찰합니다. 우리가 아는 한, 이것들은 편향된 그래디언트를 가진 GMMs에 대한 최초의 비대칭 보장이며, GMMs에 대한 최초의 위험 민감 분석입니다. 마지막으로, 우리는 우리의 결과를 설명하기 위해 강건한 회귀 문제에 대한 수치 실험을 제공합니다.

## 📝 요약

이 논문은 1차 방법론에서 수렴 속도와 그래디언트 오류에 대한 강건성 간의 상충 관계를 연구합니다. 일반화된 모멘텀 방법(GMMs)을 사용하여 매끄럽고 강하게 볼록한 목적을 최소화하는 과정에서, 편향된 확률적 그래디언트 오류가 존재할 때의 강건성을 위험 민감 지수(RSI)를 통해 정량화합니다. 특히, i.i.d. 가우시안 노이즈가 있는 이차 목적 함수에 대해 RSI와 수렴 속도 간의 파레토 경계를 제시하며, 이는 스텝 크기와 모멘텀 매개변수 선택에 따라 달라집니다. 또한, 시간 평균 하위 최적성에 대한 대편차 원리를 증명하고, RSI 함수의 볼록 켤레와 관련이 있음을 보입니다. 더 나아가, $H_\infty$-노름과의 관계를 통해 최악의 경우 강건성이 강화될수록 평균 하위 최적성의 꼬리 확률이 더 급격히 감소함을 확인합니다. 비이차적 경우에는 편향된 서브 가우시안 그래디언트 오류 하에서 유한 시간 내 RSI의 비대칭적 경계를 도출하여 GMMs의 비대칭적 보장을 제공합니다. 마지막으로, 강건 회귀 문제에 대한 수치 실험을 통해 결과를 입증합니다.

## 🎯 주요 포인트

- 1. 일반화된 모멘텀 방법(GMMs)은 매끄럽고 강하게 볼록한 목표를 최소화하는 데 사용되며, Nesterov의 가속 경사, 무거운 공, 경사 하강 방법을 포함합니다.
- 2. 확률적 경사 오류가 적대적이고 편향적일 수 있는 상황에서 GMMs의 경사 오류에 대한 강건성을 위험 민감 지수(RSI)를 통해 정량화합니다.
- 3. 이차 목표와 독립 동일 분포 가우시안 잡음의 경우, RSI와 수렴 속도 간의 파레토 전선을 드러내는 2x2 행렬 리카티 방정식의 해를 통해 RSI의 닫힌 형태 표현식을 제공합니다.
- 4. 평균 하위 최적성의 큰 편차 원리를 증명하고, 비율 함수가 RSI 함수의 볼록 켤레임을 보여줍니다.
- 5. GMMs에 대한 편향된 경사와 관련된 비대칭적 보증과 위험 민감 분석을 최초로 제공합니다.


---

*Generated on 2025-09-23 11:25:10*