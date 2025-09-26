<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:15:34.992187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Calibration",
    "Surrogate Models",
    "Model Discrepancy",
    "Glioblastoma Progression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Calibration": 0.82,
    "Surrogate Models": 0.8,
    "Model Discrepancy": 0.79,
    "Glioblastoma Progression": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian calibration",
        "canonical": "Bayesian Calibration",
        "aliases": [
          "Bayesian parameter estimation"
        ],
        "category": "specific_connectable",
        "rationale": "Bayesian calibration is crucial for parameter estimation in complex models, enhancing connectivity with statistical modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "surrogate models",
        "canonical": "Surrogate Models",
        "aliases": [
          "approximate models",
          "meta-models"
        ],
        "category": "specific_connectable",
        "rationale": "Surrogate models are pivotal in reducing computational cost, linking to efficiency improvements in model simulations.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "model discrepancy",
        "canonical": "Model Discrepancy",
        "aliases": [
          "model error",
          "model bias"
        ],
        "category": "unique_technical",
        "rationale": "Understanding model discrepancy is essential for refining models, offering unique insights into model limitations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "glioblastoma progression",
        "canonical": "Glioblastoma Progression",
        "aliases": [
          "brain tumor growth"
        ],
        "category": "unique_technical",
        "rationale": "Glioblastoma progression is a specific biological process that connects to medical and biological research on cancer.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "computational models",
      "parameter probability distributions",
      "predictive performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian calibration",
      "resolved_canonical": "Bayesian Calibration",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "surrogate models",
      "resolved_canonical": "Surrogate Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "model discrepancy",
      "resolved_canonical": "Model Discrepancy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "glioblastoma progression",
      "resolved_canonical": "Glioblastoma Progression",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Bayesian Calibration and Model Assessment of Cell Migration Dynamics with Surrogate Model Integration

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18998.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18998](https://arxiv.org/abs/2509.18998)

## 🔗 유사한 논문
- [[2025-09-23/Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation_20250923|Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation]] (81.6% similar)
- [[2025-09-24/Surrogate Modelling of Proton Dose with Monte Carlo Dropout Uncertainty Quantification_20250924|Surrogate Modelling of Proton Dose with Monte Carlo Dropout Uncertainty Quantification]] (81.5% similar)
- [[2025-09-23/An AI-powered Bayesian generative modeling approach for causal inference in observational studies_20250923|An AI-powered Bayesian generative modeling approach for causal inference in observational studies]] (81.5% similar)
- [[2025-09-24/Accounting for Uncertainty in Machine Learning Surrogates_ A Gauss-Hermite Quadrature Approach to Reliability Analysis_20250924|Accounting for Uncertainty in Machine Learning Surrogates: A Gauss-Hermite Quadrature Approach to Reliability Analysis]] (80.9% similar)
- [[2025-09-23/Enhancing Performance and Calibration in Quantile Hyperparameter Optimization_20250923|Enhancing Performance and Calibration in Quantile Hyperparameter Optimization]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Bayesian Calibration|Bayesian Calibration]], [[keywords/Surrogate Models|Surrogate Models]]
**⚡ Unique Technical**: [[keywords/Model Discrepancy|Model Discrepancy]], [[keywords/Glioblastoma Progression|Glioblastoma Progression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18998v1 Announce Type: cross 
Abstract: Computational models provide crucial insights into complex biological processes such as cancer evolution, but their mechanistic nature often makes them nonlinear and parameter-rich, complicating calibration. We systematically evaluate parameter probability distributions in cell migration models using Bayesian calibration across four complementary strategies: parametric and surrogate models, each with and without explicit model discrepancy. This approach enables joint analysis of parameter uncertainty, predictive performance, and interpretability. Applied to a real data experiment of glioblastoma progression in microfluidic devices, surrogate models achieve higher computational efficiency and predictive accuracy, whereas parametric models yield more reliable parameter estimates due to their mechanistic grounding. Incorporating model discrepancy exposes structural limitations, clarifying where model refinement is necessary. Together, these comparisons offer practical guidance for calibrating and improving computational models of complex biological systems.

## 📝 요약

이 논문은 암 진화와 같은 복잡한 생물학적 과정을 이해하는 데 중요한 계산 모델의 매개변수 불확실성을 평가하는 방법을 제시합니다. 저자들은 세포 이동 모델의 매개변수 확률 분포를 베이지안 보정을 통해 네 가지 전략으로 평가했습니다. 실험에서는 미세유체 장치에서의 교모세포종 진행 데이터를 사용했으며, 대리 모델은 계산 효율성과 예측 정확도가 높았고, 매개변수 모델은 신뢰할 수 있는 매개변수 추정치를 제공했습니다. 모델 불일치를 포함하면 구조적 한계를 드러내어 모델 개선이 필요한 부분을 명확히 할 수 있었습니다. 이러한 비교는 복잡한 생물학적 시스템의 계산 모델 보정 및 개선에 실질적인 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 컴퓨터 모델은 암 진화와 같은 복잡한 생물학적 과정을 이해하는 데 중요한 통찰력을 제공하지만, 비선형성과 많은 매개변수로 인해 보정이 복잡하다.
- 2. 베이지안 보정을 통해 세포 이동 모델의 매개변수 확률 분포를 평가하며, 명시적 모델 불일치 여부에 따라 네 가지 전략을 사용한다.
- 3. 대리 모델은 계산 효율성과 예측 정확도에서 우수한 성능을 보이며, 매개변수 모델은 기계적 기반으로 인해 더 신뢰할 수 있는 매개변수 추정치를 제공한다.
- 4. 모델 불일치를 포함하면 구조적 한계를 드러내어 모델 개선이 필요한 부분을 명확히 한다.
- 5. 이러한 비교는 복잡한 생물학적 시스템의 컴퓨터 모델 보정 및 개선을 위한 실질적인 지침을 제공한다.


---

*Generated on 2025-09-24 15:15:34*