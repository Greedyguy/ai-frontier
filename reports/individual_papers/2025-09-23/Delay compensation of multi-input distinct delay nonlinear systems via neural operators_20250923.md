---
keywords:
  - Neural Network
  - Multi-Input Nonlinear Systems
  - Transport Partial Differential Equation
  - Mobile Robot Experiment
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17131
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:19:45.878806",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Multi-Input Nonlinear Systems",
    "Transport Partial Differential Equation",
    "Mobile Robot Experiment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.82,
    "Multi-Input Nonlinear Systems": 0.79,
    "Transport Partial Differential Equation": 0.75,
    "Mobile Robot Experiment": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "neural operators",
        "canonical": "Neural Network",
        "aliases": [
          "neural operator"
        ],
        "category": "broad_technical",
        "rationale": "Neural operators are a specific application of neural networks, which are central to the paper's methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      },
      {
        "surface": "multi-input non-linear systems",
        "canonical": "Multi-Input Nonlinear Systems",
        "aliases": [
          "multi-input nonlinear system"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the specific system type addressed in the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "transport PDE",
        "canonical": "Transport Partial Differential Equation",
        "aliases": [
          "transport PDE"
        ],
        "category": "unique_technical",
        "rationale": "The transformation of delays into transport PDEs is a key methodological step in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.59,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
      },
      {
        "surface": "mobile robot experiment",
        "canonical": "Mobile Robot Experiment",
        "aliases": [
          "robot experiment"
        ],
        "category": "unique_technical",
        "rationale": "The mobile robot experiment is a specific application example that demonstrates the paper's theoretical results.",
        "novelty_score": 0.65,
        "connectivity_score": 0.54,
        "specificity_score": 0.73,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "stability results",
      "error bound",
      "region of attraction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "neural operators",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "multi-input non-linear systems",
      "resolved_canonical": "Multi-Input Nonlinear Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "transport PDE",
      "resolved_canonical": "Transport Partial Differential Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.59,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "mobile robot experiment",
      "resolved_canonical": "Mobile Robot Experiment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.54,
        "specificity": 0.73,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Delay compensation of multi-input distinct delay nonlinear systems via neural operators

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17131.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17131](https://arxiv.org/abs/2509.17131)

## 🔗 유사한 논문
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (80.6% similar)
- [[2025-09-23/System-Level Uncertainty Quantification with Multiple Machine Learning Models_ A Theoretical Framework_20250923|System-Level Uncertainty Quantification with Multiple Machine Learning Models: A Theoretical Framework]] (79.9% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (79.8% similar)
- [[2025-09-22/Time-adaptive SympNets for separable Hamiltonian systems_20250922|Time-adaptive SympNets for separable Hamiltonian systems]] (79.5% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Multi-Input Nonlinear Systems|Multi-Input Nonlinear Systems]], [[keywords/Transport Partial Differential Equation|Transport Partial Differential Equation]], [[keywords/Mobile Robot Experiment|Mobile Robot Experiment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17131v1 Announce Type: cross 
Abstract: In this work, we present the first stability results for approximate predictors in multi-input non-linear systems with distinct actuation delays. We show that if the predictor approximation satisfies a uniform (in time) error bound, semi-global practical stability is correspondingly achieved. For such approximators, the required uniform error bound depends on the desired region of attraction and the number of control inputs in the system. The result is achieved through transforming the delay into a transport PDE and conducting analysis on the coupled ODE-PDE cascade. To highlight the viability of such error bounds, we demonstrate our results on a class of approximators - neural operators - showcasing sufficiency for satisfying such a universal bound both theoretically and in simulation on a mobile robot experiment.

## 📝 요약

이 연구는 다중 입력 비선형 시스템에서 서로 다른 작용 지연을 가진 근사 예측기의 안정성 결과를 처음으로 제시합니다. 예측기 근사가 시간에 대해 균일한 오류 범위를 만족하면 준전역적 실용 안정성이 달성됩니다. 이러한 근사기의 경우, 필요한 균일 오류 범위는 시스템의 제어 입력 수와 원하는 흡인 영역에 따라 달라집니다. 연구에서는 지연을 수송 편미분 방정식(PDE)으로 변환하고 결합된 상미분 방정식-편미분 방정식(ODE-PDE) 연쇄에 대한 분석을 통해 결과를 도출했습니다. 이러한 오류 범위의 실현 가능성을 강조하기 위해, 신경 연산자를 사용한 사례를 통해 이론적 및 모바일 로봇 실험 시뮬레이션에서 보편적인 오류 범위를 만족하는 충분성을 입증했습니다.

## 🎯 주요 포인트

- 1. 다중 입력 비선형 시스템에서 서로 다른 작용 지연을 가진 근사 예측기의 안정성 결과를 최초로 제시했습니다.
- 2. 예측기 근사가 시간에 대해 균일한 오류 경계를 만족하면 반글로벌 실용적 안정성이 달성됩니다.
- 3. 필요한 균일 오류 경계는 시스템의 제어 입력 수와 원하는 흡인 영역에 따라 달라집니다.
- 4. 지연을 수송 편미분 방정식(PDE)으로 변환하고 결합된 상미분 방정식-편미분 방정식(ODE-PDE) 연쇄에서 분석을 수행하여 결과를 도출했습니다.
- 5. 신경 연산자와 같은 근사기 클래스에서 이론적 및 시뮬레이션을 통해 이러한 보편적 경계를 만족하는 충분성을 입증했습니다.


---

*Generated on 2025-09-24 02:19:45*