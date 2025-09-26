---
keywords:
  - Neural Control Variates
  - Monte Carlo Integration
  - Neural Network
  - Computational Geometry
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15538
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:49:44.899063",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Control Variates",
    "Monte Carlo Integration",
    "Neural Network",
    "Computational Geometry"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Control Variates": 0.78,
    "Monte Carlo Integration": 0.8,
    "Neural Network": 0.75,
    "Computational Geometry": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Control Variates",
        "canonical": "Neural Control Variates",
        "aliases": [
          "Neural Variance Reduction"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel application of neural networks for variance reduction in Monte Carlo integration, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Monte Carlo Integration",
        "canonical": "Monte Carlo Integration",
        "aliases": [
          "MC Integration"
        ],
        "category": "specific_connectable",
        "rationale": "Monte Carlo Integration is a key technique discussed in the paper, providing a strong link to computational methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multilayered Perceptron",
        "canonical": "Neural Network",
        "aliases": [
          "MLP"
        ],
        "category": "broad_technical",
        "rationale": "The multilayered perceptron is a fundamental neural network model explored in the paper, linking to broader neural network discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Computational Geometry",
        "canonical": "Computational Geometry",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Computational Geometry is used to solve integration problems in the paper, offering a specific link to geometric methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "function",
      "application"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Control Variates",
      "resolved_canonical": "Neural Control Variates",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Monte Carlo Integration",
      "resolved_canonical": "Monte Carlo Integration",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multilayered Perceptron",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Computational Geometry",
      "resolved_canonical": "Computational Geometry",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Geometric Integration for Neural Control Variates

**Korean Title:** 신경 제어 변수를 위한 기하학적 적분

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15538.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15538](https://arxiv.org/abs/2509.15538)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.1% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (80.3% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (80.1% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (79.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Monte Carlo Integration|Monte Carlo Integration]], [[keywords/Computational Geometry|Computational Geometry]]
**⚡ Unique Technical**: [[keywords/Neural Control Variates|Neural Control Variates]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15538v1 Announce Type: cross 
Abstract: Control variates are a variance-reduction technique for Monte Carlo integration. The principle involves approximating the integrand by a function that can be analytically integrated, and integrating using the Monte Carlo method only the residual difference between the integrand and the approximation, to obtain an unbiased estimate. Neural networks are universal approximators that could potentially be used as a control variate. However, the challenge lies in the analytic integration, which is not possible in general. In this manuscript, we study one of the simplest neural network models, the multilayered perceptron (MLP) with continuous piecewise linear activation functions, and its possible analytic integration. We propose an integration method based on integration domain subdivision, employing techniques from computational geometry to solve this problem in 2D. We demonstrate that an MLP can be used as a control variate in combination with our integration method, showing applications in the light transport simulation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15538v1 발표 유형: 교차  
초록: 제어 변수는 몬테카를로 적분의 분산 감소 기법입니다. 이 원리는 적분할 함수를 분석적으로 적분할 수 있는 함수로 근사하고, 몬테카를로 방법을 사용하여 적분과 근사 사이의 잔차 차이만을 적분하여 편향되지 않은 추정치를 얻는 것입니다. 신경망은 제어 변수로 사용될 수 있는 보편적인 근사 도구입니다. 그러나 일반적으로 분석적 적분이 불가능하다는 점이 문제입니다. 이 논문에서는 가장 간단한 신경망 모델 중 하나인 다층 퍼셉트론(MLP)을 연속적인 조각별 선형 활성화 함수와 함께 연구하고, 그 가능한 분석적 적분을 탐구합니다. 우리는 2D에서 이 문제를 해결하기 위해 계산 기하학 기법을 활용하여 적분 영역을 세분화하는 적분 방법을 제안합니다. 우리는 MLP가 우리의 적분 방법과 결합하여 제어 변수로 사용될 수 있음을 입증하며, 빛 전송 시뮬레이션에서의 응용을 보여줍니다.

## 📝 요약

이 논문은 몬테카를로 적분의 분산 감소 기법인 컨트롤 베리에이트에 대한 연구로, 신경망을 활용한 새로운 접근법을 제안합니다. 특히, 다층 퍼셉트론(MLP) 모델을 사용하여 연속적인 조각별 선형 활성화 함수의 가능한 해석적 적분을 탐구합니다. 저자들은 계산 기하학 기법을 활용하여 2D에서 적분 영역을 세분화하는 방법을 제안하고, 이를 통해 MLP가 컨트롤 베리에이트로 사용될 수 있음을 보였습니다. 이 방법은 특히 광 전송 시뮬레이션에 응용될 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 제어 변수는 몬테카를로 적분의 분산 감소 기법으로 사용된다.
- 2. 신경망은 보편적 근사기로서 제어 변수로 활용될 가능성이 있다.
- 3. 본 연구에서는 다층 퍼셉트론(MLP) 모델과 그 분석적 적분 가능성을 탐구한다.
- 4. 적분 영역 세분화와 계산 기하학 기법을 사용하여 2D 문제를 해결하는 적분 방법을 제안한다.
- 5. 제안된 적분 방법과 MLP를 결합하여 빛 전송 시뮬레이션에 응용 가능함을 입증한다.


---

*Generated on 2025-09-23 10:49:44*