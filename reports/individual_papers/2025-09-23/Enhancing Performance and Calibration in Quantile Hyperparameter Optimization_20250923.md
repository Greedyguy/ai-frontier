---
keywords:
  - Bayesian Hyperparameter Optimization
  - Gaussian Process
  - Conformalized Quantile Regression
  - Feedback Covariate Shift
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17051
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:46:19.073476",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Hyperparameter Optimization",
    "Gaussian Process",
    "Conformalized Quantile Regression",
    "Feedback Covariate Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Hyperparameter Optimization": 0.78,
    "Gaussian Process": 0.77,
    "Conformalized Quantile Regression": 0.75,
    "Feedback Covariate Shift": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian hyperparameter optimization",
        "canonical": "Bayesian Hyperparameter Optimization",
        "aliases": [
          "BHO"
        ],
        "category": "specific_connectable",
        "rationale": "Bayesian hyperparameter optimization is a key method in machine learning, offering strong connectivity to optimization and machine learning techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian Process",
        "canonical": "Gaussian Process",
        "aliases": [
          "GP"
        ],
        "category": "broad_technical",
        "rationale": "Gaussian Processes are widely used in machine learning for modeling and optimization, providing a strong link to statistical methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Conformalized quantile regression",
        "canonical": "Conformalized Quantile Regression",
        "aliases": [
          "CQR"
        ],
        "category": "unique_technical",
        "rationale": "This technique addresses estimation weaknesses in hyperparameter optimization, offering novel insights into robust calibration.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "feedback covariate shift",
        "canonical": "Feedback Covariate Shift",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Addressing feedback covariate shift is crucial for improving sequential acquisition in optimization, linking to adaptive learning methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "calibration",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian hyperparameter optimization",
      "resolved_canonical": "Bayesian Hyperparameter Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian Process",
      "resolved_canonical": "Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Conformalized quantile regression",
      "resolved_canonical": "Conformalized Quantile Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "feedback covariate shift",
      "resolved_canonical": "Feedback Covariate Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Enhancing Performance and Calibration in Quantile Hyperparameter Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17051.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17051](https://arxiv.org/abs/2509.17051)

## 🔗 유사한 논문
- [[2025-09-23/Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs_20250923|Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs]] (84.1% similar)
- [[2025-09-22/Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems_20250922|Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems]] (82.5% similar)
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (82.4% similar)
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (82.2% similar)
- [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gaussian Process|Gaussian Process]]
**🔗 Specific Connectable**: [[keywords/Bayesian Hyperparameter Optimization|Bayesian Hyperparameter Optimization]]
**⚡ Unique Technical**: [[keywords/Conformalized Quantile Regression|Conformalized Quantile Regression]], [[keywords/Feedback Covariate Shift|Feedback Covariate Shift]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17051v1 Announce Type: new 
Abstract: Bayesian hyperparameter optimization relies heavily on Gaussian Process (GP) surrogates, due to robust distributional posteriors and strong performance on limited training samples. GPs however underperform in categorical hyperparameter environments or when assumptions of normality, heteroskedasticity and symmetry are excessively challenged. Conformalized quantile regression can address these estimation weaknesses, while still providing robust calibration guarantees. This study builds upon early work in this area by addressing feedback covariate shift in sequential acquisition and integrating a wider range of surrogate architectures and acquisition functions. Proposed algorithms are rigorously benchmarked against a range of state of the art hyperparameter optimization methods (GP, TPE and SMAC). Findings identify quantile surrogate architectures and acquisition functions yielding superior performance to the current quantile literature, while validating the beneficial impact of conformalization on calibration and search performance.

## 📝 요약

이 논문은 베이지안 하이퍼파라미터 최적화에서 Gaussian Process(GP) 대리 모델의 한계를 극복하기 위해 연구되었습니다. GP는 범주형 하이퍼파라미터 환경에서 성능이 떨어지며, 정규성, 이분산성 및 대칭성 가정이 과도하게 도전받을 때 문제가 발생합니다. 본 연구는 이러한 문제를 해결하기 위해 적합화된 분위수 회귀를 사용하여 견고한 보정을 보장합니다. 또한, 순차적 획득에서 피드백 공변량 이동을 다루고 다양한 대리 구조 및 획득 함수를 통합합니다. 제안된 알고리즘은 최신 하이퍼파라미터 최적화 방법들과 비교 평가되었으며, 그 결과 분위수 대리 구조와 획득 함수가 기존 문헌보다 우수한 성능을 보임을 확인했습니다. 또한 적합화가 보정 및 탐색 성능에 긍정적인 영향을 미침을 검증했습니다.

## 🎯 주요 포인트

- 1. 베이지안 하이퍼파라미터 최적화는 주로 가우시안 프로세스(GP) 대리모델에 의존하지만, 범주형 하이퍼파라미터 환경에서는 성능이 저하될 수 있다.
- 2. 정규성, 이분산성, 대칭성 가정이 과도하게 도전받을 때 GP의 성능이 떨어질 수 있다.
- 3. 적합화된 분위수 회귀는 이러한 추정의 약점을 보완하면서도 강력한 보정 보증을 제공할 수 있다.
- 4. 본 연구는 피드백 공변량 이동을 해결하고 다양한 대리모델 아키텍처와 획득 함수를 통합하여 기존 연구를 확장한다.
- 5. 제안된 알고리즘은 최신 하이퍼파라미터 최적화 방법들과 비교하여 우수한 성능을 보이며, 적합화의 보정 및 검색 성능에 대한 긍정적인 영향을 검증한다.


---

*Generated on 2025-09-24 01:46:19*