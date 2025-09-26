---
keywords:
  - Geometric Autoencoders for Bayesian Inversion
  - Uncertainty Quantification
  - Approximate Bayesian Computation
  - Geometry-Adapted Posterior Distribution
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19929
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:59:10.024713",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Geometric Autoencoders for Bayesian Inversion",
    "Uncertainty Quantification",
    "Approximate Bayesian Computation",
    "Geometry-Adapted Posterior Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Geometric Autoencoders for Bayesian Inversion": 0.78,
    "Uncertainty Quantification": 0.7,
    "Approximate Bayesian Computation": 0.72,
    "Geometry-Adapted Posterior Distribution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Geometric Autoencoders for Bayesian Inversion",
        "canonical": "Geometric Autoencoders for Bayesian Inversion",
        "aliases": [
          "GABI"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework specifically designed for geometry-aware Bayesian inversion, offering a unique approach to uncertainty quantification.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty Quantification",
        "canonical": "Uncertainty Quantification",
        "aliases": [
          "UQ"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in engineering and scientific inference, providing a basis for linking various methodologies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Approximate Bayesian Computation",
        "canonical": "Approximate Bayesian Computation",
        "aliases": [
          "ABC"
        ],
        "category": "specific_connectable",
        "rationale": "A critical technique for implementing the proposed framework, facilitating connections with Bayesian methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "geometry-adapted posterior distribution",
        "canonical": "Geometry-Adapted Posterior Distribution",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach, representing a novel adaptation of Bayesian inference.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Geometric Autoencoders for Bayesian Inversion",
      "resolved_canonical": "Geometric Autoencoders for Bayesian Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty Quantification",
      "resolved_canonical": "Uncertainty Quantification",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Approximate Bayesian Computation",
      "resolved_canonical": "Approximate Bayesian Computation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "geometry-adapted posterior distribution",
      "resolved_canonical": "Geometry-Adapted Posterior Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Geometric Autoencoder Priors for Bayesian Inversion: Learn First Observe Later

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19929.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19929](https://arxiv.org/abs/2509.19929)

## 🔗 유사한 논문
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (82.4% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (82.3% similar)
- [[2025-09-23/An AI-powered Bayesian generative modeling approach for causal inference in observational studies_20250923|An AI-powered Bayesian generative modeling approach for causal inference in observational studies]] (82.3% similar)
- [[2025-09-24/Diffusion Bridge Variational Inference for Deep Gaussian Processes_20250924|Diffusion Bridge Variational Inference for Deep Gaussian Processes]] (81.9% similar)
- [[2025-09-24/Probabilistic Geometric Principal Component Analysis with application to neural data_20250924|Probabilistic Geometric Principal Component Analysis with application to neural data]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**🔗 Specific Connectable**: [[keywords/Approximate Bayesian Computation|Approximate Bayesian Computation]]
**⚡ Unique Technical**: [[keywords/Geometric Autoencoders for Bayesian Inversion|Geometric Autoencoders for Bayesian Inversion]], [[keywords/Geometry-Adapted Posterior Distribution|Geometry-Adapted Posterior Distribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19929v1 Announce Type: cross 
Abstract: Uncertainty Quantification (UQ) is paramount for inference in engineering applications. A common inference task is to recover full-field information of physical systems from a small number of noisy observations, a usually highly ill-posed problem. Critically, engineering systems often have complicated and variable geometries prohibiting the use of standard Bayesian UQ. In this work, we introduce Geometric Autoencoders for Bayesian Inversion (GABI), a framework for learning geometry-aware generative models of physical responses that serve as highly informative geometry-conditioned priors for Bayesian inversion. Following a ''learn first, observe later'' paradigm, GABI distills information from large datasets of systems with varying geometries, without requiring knowledge of governing PDEs, boundary conditions, or observation processes, into a rich latent prior. At inference time, this prior is seamlessly combined with the likelihood of the specific observation process, yielding a geometry-adapted posterior distribution. Our proposed framework is architecture agnostic. A creative use of Approximate Bayesian Computation (ABC) sampling yields an efficient implementation that utilizes modern GPU hardware. We test our method on: steady-state heat over rectangular domains; Reynold-Averaged Navier-Stokes (RANS) flow around airfoils; Helmholtz resonance and source localization on 3D car bodies; RANS airflow over terrain. We find: the predictive accuracy to be comparable to deterministic supervised learning approaches in the restricted setting where supervised learning is applicable; UQ to be well calibrated and robust on challenging problems with complex geometries. The method provides a flexible geometry-aware train-once-use-anywhere foundation model which is independent of any particular observation process.

## 📝 요약

이 논문은 복잡한 기하학적 구조를 가진 공학 시스템에서 불확실성 정량화(UQ)를 위한 새로운 프레임워크인 GABI(Geometric Autoencoders for Bayesian Inversion)를 제안합니다. GABI는 다양한 기하학적 구조를 가진 시스템의 대규모 데이터셋에서 정보를 학습하여 기하학적 조건에 맞춘 사전 확률을 생성합니다. 이는 특정 관측 과정의 가능성과 결합되어 기하학에 적응된 사후 확률 분포를 제공합니다. 이 방법은 특정 아키텍처에 구애받지 않으며, 현대 GPU 하드웨어를 활용한 Approximate Bayesian Computation(ABC) 샘플링을 통해 효율적으로 구현됩니다. 다양한 테스트 결과, GABI는 복잡한 기하학적 문제에서 예측 정확도가 높고, 불확실성 정량화가 잘 조정되어 있음을 보여줍니다. 이 방법은 특정 관측 과정에 독립적인 유연한 기하학 인식 모델을 제공합니다.

## 🎯 주요 포인트

- 1. GABI는 복잡하고 다양한 기하학적 구조를 가진 물리 시스템의 정보를 효과적으로 추론하기 위한 기하학적 오토인코더 기반의 베이지안 역문제 해결 프레임워크입니다.
- 2. 이 방법은 지배 방정식, 경계 조건, 관측 과정에 대한 사전 지식 없이도 다양한 기하학적 구조를 가진 시스템의 대규모 데이터셋에서 정보를 추출하여 풍부한 잠재 사전 분포를 학습합니다.
- 3. 제안된 프레임워크는 특정 아키텍처에 구애받지 않으며, 현대 GPU 하드웨어를 활용한 Approximate Bayesian Computation (ABC) 샘플링을 통해 효율적으로 구현됩니다.
- 4. GABI는 복잡한 기하학적 구조를 가진 문제에서도 잘 보정된 불확실성 정량화(UQ)를 제공하며, 예측 정확도는 제한된 환경에서의 결정론적 지도 학습 접근법과 비교할 만합니다.
- 5. 이 방법은 특정 관측 과정에 독립적인 기하학적 인식 기반의 유연한 학습-한번-사용-어디서나 가능한 기초 모델을 제공합니다.


---

*Generated on 2025-09-25 16:59:10*