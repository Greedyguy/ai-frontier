---
keywords:
  - Sparse Gradient Descent
  - Max-Affine Regression
  - Sparse Principal Component Analysis
  - Real Maslov Dequantization
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2411.02225
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:37:01.148509",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Gradient Descent",
    "Max-Affine Regression",
    "Sparse Principal Component Analysis",
    "Real Maslov Dequantization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Gradient Descent": 0.8,
    "Max-Affine Regression": 0.78,
    "Sparse Principal Component Analysis": 0.72,
    "Real Maslov Dequantization": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Gradient Descent",
        "canonical": "Sparse Gradient Descent",
        "aliases": [
          "Sp-GD"
        ],
        "category": "unique_technical",
        "rationale": "Sparse Gradient Descent is a novel method proposed in the paper, crucial for variable selection in max-affine regression.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Max-Affine Regression",
        "canonical": "Max-Affine Regression",
        "aliases": [
          "max-affine model"
        ],
        "category": "unique_technical",
        "rationale": "Max-Affine Regression is the central focus of the paper, offering a specific regression approach that can be linked to other affine transformation studies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse Principal Component Analysis",
        "canonical": "Sparse Principal Component Analysis",
        "aliases": [
          "Sparse PCA"
        ],
        "category": "broad_technical",
        "rationale": "Sparse PCA is a well-known technique used in the initialization scheme of the proposed method, linking it to dimensionality reduction topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Real Maslov Dequantization",
        "canonical": "Real Maslov Dequantization",
        "aliases": [
          "RMD"
        ],
        "category": "unique_technical",
        "rationale": "Real Maslov Dequantization is a new transformation introduced in the paper, providing a novel approach to transform polynomials into max-affine models.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.92,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "convex piecewise linear regression",
      "non-asymptotic analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Gradient Descent",
      "resolved_canonical": "Sparse Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Max-Affine Regression",
      "resolved_canonical": "Max-Affine Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse Principal Component Analysis",
      "resolved_canonical": "Sparse Principal Component Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Real Maslov Dequantization",
      "resolved_canonical": "Real Maslov Dequantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.92,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Sparse Max-Affine Regression

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.02225.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2411.02225](https://arxiv.org/abs/2411.02225)

## 🔗 유사한 논문
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (81.7% similar)
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (80.6% similar)
- [[2025-09-24/DWTGS_ Rethinking Frequency Regularization for Sparse-view 3D Gaussian Splatting_20250924|DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian Splatting]] (80.4% similar)
- [[2025-09-23/Risk Comparisons in Linear Regression_ Implicit Regularization Dominates Explicit Regularization_20250923|Risk Comparisons in Linear Regression: Implicit Regularization Dominates Explicit Regularization]] (80.3% similar)
- [[2025-09-24/Diffusion Bridge Variational Inference for Deep Gaussian Processes_20250924|Diffusion Bridge Variational Inference for Deep Gaussian Processes]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Sparse Principal Component Analysis|Sparse Principal Component Analysis]]
**⚡ Unique Technical**: [[keywords/Sparse Gradient Descent|Sparse Gradient Descent]], [[keywords/Max-Affine Regression|Max-Affine Regression]], [[keywords/Real Maslov Dequantization|Real Maslov Dequantization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.02225v2 Announce Type: replace-cross 
Abstract: This paper presents Sparse Gradient Descent as a solution for variable selection in convex piecewise linear regression, where the model is given as the maximum of $k$-affine functions $ x \mapsto \max_{j \in [k]} \langle a_j^\star, x \rangle + b_j^\star$ for $j = 1,\dots,k$. Here, $\{ a_j^\star\}_{j=1}^k$ and $\{b_j^\star\}_{j=1}^k$ denote the ground-truth weight vectors and intercepts. A non-asymptotic local convergence analysis is provided for Sp-GD under sub-Gaussian noise when the covariate distribution satisfies the sub-Gaussianity and anti-concentration properties. When the model order and parameters are fixed, Sp-GD provides an $\epsilon$-accurate estimate given $\mathcal{O}(\max(\epsilon^{-2}\sigma_z^2,1)s\log(d/s))$ observations where $\sigma_z^2$ denotes the noise variance. This also implies the exact parameter recovery by Sp-GD from $\mathcal{O}(s\log(d/s))$ noise-free observations. The proposed initialization scheme uses sparse principal component analysis to estimate the subspace spanned by $\{ a_j^\star\}_{j=1}^k$, then applies an $r$-covering search to estimate the model parameters. A non-asymptotic analysis is presented for this initialization scheme when the covariates and noise samples follow Gaussian distributions. When the model order and parameters are fixed, this initialization scheme provides an $\epsilon$-accurate estimate given $\mathcal{O}(\epsilon^{-2}\max(\sigma_z^4,\sigma_z^2,1)s^2\log^4(d))$ observations. A new transformation named Real Maslov Dequantization (RMD) is proposed to transform sparse generalized polynomials into sparse max-affine models. The error decay rate of RMD is shown to be exponentially small in its temperature parameter. Furthermore, theoretical guarantees for Sp-GD are extended to the bounded noise model induced by RMD. Numerical Monte Carlo results corroborate theoretical findings for Sp-GD and the initialization scheme.

## 📝 요약

이 논문은 볼록 조각별 선형 회귀에서 변수 선택을 위한 Sparse Gradient Descent(Sp-GD)을 제안합니다. Sp-GD는 서브 가우시안 잡음 하에서 비대칭적 지역 수렴 분석을 제공하며, 모델 순서와 매개변수가 고정된 경우 $\mathcal{O}(\max(\epsilon^{-2}\sigma_z^2,1)s\log(d/s))$ 관측치로 $\epsilon$ 정확도를 달성합니다. 초기화는 희소 주성분 분석을 사용하여 모델 매개변수를 추정하며, 이는 $\mathcal{O}(\epsilon^{-2}\max(\sigma_z^4,\sigma_z^2,1)s^2\log^4(d))$ 관측치로 $\epsilon$ 정확도를 제공합니다. 또한, 희소 일반화 다항식을 희소 최대-아핀 모델로 변환하는 Real Maslov Dequantization(RMD)을 제안하며, RMD의 오류 감소율은 온도 매개변수에 대해 지수적으로 작습니다. Sp-GD의 이론적 보장은 RMD에 의해 유도된 잡음 모델로 확장되며, 수치적 몬테카를로 결과는 이론적 발견을 뒷받침합니다.

## 🎯 주요 포인트

- 1. Sparse Gradient Descent(SGD)는 볼록 조각별 선형 회귀에서 변수 선택을 위한 솔루션을 제시합니다.
- 2. Sp-GD는 서브 가우시안 잡음 하에서 비대칭적 지역 수렴 분석을 제공합니다.
- 3. 제안된 초기화 방식은 희소 주성분 분석을 사용하여 모델 매개변수를 추정합니다.
- 4. 새로운 변환인 Real Maslov Dequantization(RMD)는 희소 일반화 다항식을 희소 최대-아핀 모델로 변환합니다.
- 5. Sp-GD와 초기화 방식에 대한 이론적 보장은 수치적 몬테카를로 결과로 확인되었습니다.


---

*Generated on 2025-09-26 08:37:01*