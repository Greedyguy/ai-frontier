<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:21:39.656947",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Nonnegative Matrix Factorization",
    "Sum-of-norm Regularization",
    "Rank Estimation",
    "Hyperspectral Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Nonnegative Matrix Factorization": 0.78,
    "Sum-of-norm Regularization": 0.82,
    "Rank Estimation": 0.77,
    "Hyperspectral Imaging": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Nonnegative Matrix Factorization",
        "canonical": "Nonnegative Matrix Factorization",
        "aliases": [
          "NMF"
        ],
        "category": "unique_technical",
        "rationale": "NMF is a core technique discussed in the paper, essential for understanding the proposed method.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sum-of-norm",
        "canonical": "Sum-of-norm Regularization",
        "aliases": [
          "SON"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces SON as a novel regularization approach, central to the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.68,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Rank Estimation",
        "canonical": "Rank Estimation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Rank estimation is a critical problem addressed by the proposed method, linking to broader matrix factorization challenges.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hyperspectral Imaging",
        "canonical": "Hyperspectral Imaging",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The application of the proposed method in hyperspectral imaging highlights its practical relevance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "technique",
      "algorithm",
      "data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Nonnegative Matrix Factorization",
      "resolved_canonical": "Nonnegative Matrix Factorization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sum-of-norm",
      "resolved_canonical": "Sum-of-norm Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.68,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Rank Estimation",
      "resolved_canonical": "Rank Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hyperspectral Imaging",
      "resolved_canonical": "Hyperspectral Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Sum-of-norms regularized Nonnegative Matrix Factorization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2407.00706.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2407.00706](https://arxiv.org/abs/2407.00706)

## 🔗 유사한 논문
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (78.2% similar)
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (78.1% similar)
- [[2025-09-23/Bias-variance Tradeoff in Tensor Estimation_20250923|Bias-variance Tradeoff in Tensor Estimation]] (77.9% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Rank Estimation|Rank Estimation]], [[keywords/Hyperspectral Imaging|Hyperspectral Imaging]]
**⚡ Unique Technical**: [[keywords/Nonnegative Matrix Factorization|Nonnegative Matrix Factorization]], [[keywords/Sum-of-norm Regularization|Sum-of-norm Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.00706v2 Announce Type: replace 
Abstract: When applying nonnegative matrix factorization (NMF), the rank parameter is generally unknown. This rank, called the nonnegative rank, is usually estimated heuristically since computing its exact value is NP-hard. In this work, we propose an approximation method to estimate the rank on-the-fly while solving NMF. We use the sum-of-norm (SON), a group-lasso structure that encourages pairwise sim- ilarity, to reduce the rank of a factor matrix when the initial rank is overestimated. On various datasets, SON-NMF can reveal the correct nonnegative rank of the data without prior knowledge or parameter tuning. SON-NMF is a nonconvex, nonsmooth, non-separable, and non-proximable problem, making it nontrivial to solve. First, since rank estimation in NMF is NP-hard, the proposed approach does not benefit from lower computational com- plexity. Using a graph-theoretic argument, we prove that the complexity of SON- NMF is essentially irreducible. Second, the per-iteration cost of algorithms for SON-NMF can be high. This motivates us to propose a first-order BCD algorithm that approximately solves SON-NMF with low per-iteration cost via the proximal average operator. SON-NMF exhibits favorable features for applications. Besides the ability to automatically estimate the rank from data, SON-NMF can handle rank-deficient data matrices and detect weak components with small energy. Furthermore, in hyperspectral imaging, SON-NMF naturally addresses the issue of spectral variability.

## 📝 요약

이 논문에서는 비음수 행렬 분해(NMF)에서 랭크 파라미터를 추정하는 새로운 방법을 제안합니다. 일반적으로 NMF의 랭크는 NP-난해 문제로 정확한 계산이 어렵고, 주로 휴리스틱하게 추정됩니다. 제안된 방법은 SON(합-노름) 구조를 사용하여 랭크를 실시간으로 추정하며, 초기 랭크가 과대평가된 경우 이를 줄여줍니다. 다양한 데이터셋에서 SON-NMF는 사전 지식이나 파라미터 튜닝 없이 정확한 비음수 랭크를 찾아낼 수 있습니다. SON-NMF는 비볼록, 비매끄러움, 비분리 가능, 비근접 가능 문제로 해결이 까다롭지만, 제안된 1차 BCD 알고리즘은 낮은 반복 비용으로 이를 근사적으로 해결합니다. 이 방법은 데이터로부터 자동으로 랭크를 추정할 수 있으며, 랭크 결핍 데이터 행렬을 처리하고 약한 성분을 감지할 수 있습니다. 또한, 초분광 이미징에서 스펙트럼 변동 문제를 자연스럽게 해결합니다.

## 🎯 주요 포인트

- 1. 비음수 행렬 분해(NMF)에서 랭크 파라미터는 일반적으로 알려져 있지 않으며, 이를 정확히 계산하는 것은 NP-난해 문제입니다.
- 2. 본 연구에서는 NMF를 해결하는 동안 랭크를 실시간으로 추정할 수 있는 근사 방법을 제안합니다.
- 3. 제안된 SON-NMF 방법은 초기 랭크가 과대평가된 경우, 그룹 라쏘 구조를 사용하여 요인 행렬의 랭크를 줄입니다.
- 4. SON-NMF는 데이터의 비음수 랭크를 사전 지식이나 파라미터 튜닝 없이 정확하게 추정할 수 있습니다.
- 5. SON-NMF는 비볼록, 비매끄러움, 비분리 가능, 비근접 가능 문제로, 해결이 쉽지 않으며, 이를 위해 저비용의 1차 BCD 알고리즘을 제안합니다.


---

*Generated on 2025-09-24 15:21:39*