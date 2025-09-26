---
keywords:
  - Variational Autoencoder
  - Bayesian Inverse Problem
  - Uncertainty Quantification
  - Laplace Equation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2502.13105
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:06:10.946432",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Autoencoder",
    "Bayesian Inverse Problem",
    "Uncertainty Quantification",
    "Laplace Equation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Autoencoder": 0.85,
    "Bayesian Inverse Problem": 0.78,
    "Uncertainty Quantification": 0.77,
    "Laplace Equation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "variational autoencoders",
        "canonical": "Variational Autoencoder",
        "aliases": [
          "VAE"
        ],
        "category": "specific_connectable",
        "rationale": "Variational autoencoders are central to the paper's methodology and connect well with existing neural network concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Bayesian inverse problems",
        "canonical": "Bayesian Inverse Problem",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific application area for variational autoencoders, providing unique insights into Bayesian methods.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "uncertainty quantification",
        "canonical": "Uncertainty Quantification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Uncertainty quantification is a key aspect of Bayesian methods and enhances the connectivity with probabilistic modeling.",
        "novelty_score": 0.48,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Laplace equation",
        "canonical": "Laplace Equation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Laplace equation is used as a test case, providing a specific example of the method's application.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "real-time",
      "numerical tests"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "variational autoencoders",
      "resolved_canonical": "Variational Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Bayesian inverse problems",
      "resolved_canonical": "Bayesian Inverse Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "uncertainty quantification",
      "resolved_canonical": "Uncertainty Quantification",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Laplace equation",
      "resolved_canonical": "Laplace Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Enhanced uncertainty quantification variational autoencoders for the solution of Bayesian inverse problems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13105.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2502.13105](https://arxiv.org/abs/2502.13105)

## 🔗 유사한 논문
- [[2025-09-23/Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation_20250923|Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation]] (85.3% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (82.9% similar)
- [[2025-09-23/Convergence analysis of equilibrium methods for inverse problems_20250923|Convergence analysis of equilibrium methods for inverse problems]] (82.2% similar)
- [[2025-09-23/Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits_20250923|Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits]] (81.9% similar)
- [[2025-09-23/An AI-powered Bayesian generative modeling approach for causal inference in observational studies_20250923|An AI-powered Bayesian generative modeling approach for causal inference in observational studies]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Variational Autoencoder|Variational Autoencoder]], [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Bayesian Inverse Problem|Bayesian Inverse Problem]], [[keywords/Laplace Equation|Laplace Equation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13105v2 Announce Type: replace 
Abstract: Among other uses, neural networks are a powerful tool for solving deterministic and Bayesian inverse problems in real-time, where variational autoencoders, a specialized type of neural network, enable the Bayesian estimation of model parameters and their distribution from observational data allowing real-time inverse uncertainty quantification. In this work, we build upon existing research [Goh, H. et al., Proceedings of Machine Learning Research, 2022] by proposing a novel loss function to train variational autoencoders for Bayesian inverse problems. When the forward map is affine, we provide a theoretical proof of the convergence of the latent states of variational autoencoders to the posterior distribution of the model parameters. We validate this theoretical result through numerical tests and we compare the proposed variational autoencoder with the existing one in the literature both in terms of accuracy and generalization properties. Finally, we test the proposed variational autoencoder on a Laplace equation, with comparison to the original one and Markov Chains Monte Carlo.

## 📝 요약

이 논문에서는 실시간으로 결정론적 및 베이지안 역문제를 해결하기 위해 변분 오토인코더(VAE)를 활용하는 방법을 제안합니다. 기존 연구를 바탕으로 새로운 손실 함수를 제안하여 베이지안 역문제에 대한 VAE의 성능을 향상시켰습니다. 특히, 순방향 맵이 아핀일 때 VAE의 잠재 상태가 모델 매개변수의 사후 분포로 수렴함을 이론적으로 증명하고, 이를 수치 실험으로 검증했습니다. 제안된 VAE는 기존 모델과 비교하여 정확성과 일반화 측면에서 우수함을 보였으며, 라플라스 방정식에 적용하여 기존 모델 및 마코프 체인 몬테카를로(MCMC)와 비교했습니다.

## 🎯 주요 포인트

- 1. 본 연구에서는 변분 오토인코더를 위한 새로운 손실 함수를 제안하여 베이지안 역문제를 해결하고자 합니다.
- 2. 선형 사상일 경우, 변분 오토인코더의 잠재 상태가 모델 매개변수의 사후 분포로 수렴함을 이론적으로 증명하였습니다.
- 3. 제안된 변분 오토인코더의 정확성과 일반화 특성을 기존 문헌의 모델과 비교하여 검증하였습니다.
- 4. 라플라스 방정식에 대해 제안된 변분 오토인코더를 테스트하고, 기존 모델 및 마코프 체인 몬테카를로와 비교하였습니다.


---

*Generated on 2025-09-25 17:06:10*