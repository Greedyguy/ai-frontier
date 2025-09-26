---
keywords:
  - PAGE Algorithm
  - Weakly Convex Functions
  - Finite-Sum Optimization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.00737
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:08:28.799764",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "PAGE Algorithm",
    "Weakly Convex Functions",
    "Finite-Sum Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "PAGE Algorithm": 0.78,
    "Weakly Convex Functions": 0.72,
    "Finite-Sum Optimization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "PAGE Stochastic Algorithm",
        "canonical": "PAGE Algorithm",
        "aliases": [
          "PAGE",
          "PAGE Stochastic"
        ],
        "category": "unique_technical",
        "rationale": "The PAGE algorithm is central to the paper and offers a unique approach to optimization problems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Weakly Convex Functions",
        "canonical": "Weakly Convex Functions",
        "aliases": [
          "τ-weakly convex",
          "weak convexity"
        ],
        "category": "unique_technical",
        "rationale": "Weakly convex functions provide a critical framework for understanding the convergence analysis discussed.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Finite-Sum Optimization",
        "canonical": "Finite-Sum Optimization",
        "aliases": [
          "finite sum",
          "sum optimization"
        ],
        "category": "unique_technical",
        "rationale": "Finite-sum optimization is a key mathematical concept in the paper, crucial for understanding the algorithm's application.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "nonconvex functions",
      "smooth case",
      "convergence rates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "PAGE Stochastic Algorithm",
      "resolved_canonical": "PAGE Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Weakly Convex Functions",
      "resolved_canonical": "Weakly Convex Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Finite-Sum Optimization",
      "resolved_canonical": "Finite-Sum Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Convergence Analysis of the PAGE Stochastic Algorithm for Weakly Convex Finite-Sum Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.00737.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.00737](https://arxiv.org/abs/2509.00737)

## 🔗 유사한 논문
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (79.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (78.9% similar)
- [[2025-09-23/Absorb and Converge_ Provable Convergence Guarantee for Absorbing Discrete Diffusion Models_20250923|Absorb and Converge: Provable Convergence Guarantee for Absorbing Discrete Diffusion Models]] (77.6% similar)
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (77.1% similar)
- [[2025-09-23/Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs_20250923|Near-Optimal Sample Complexity Bounds for Constrained Average-Reward MDPs]] (77.0% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/PAGE Algorithm|PAGE Algorithm]], [[keywords/Weakly Convex Functions|Weakly Convex Functions]], [[keywords/Finite-Sum Optimization|Finite-Sum Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.00737v2 Announce Type: replace-cross 
Abstract: PAGE, a stochastic algorithm introduced by Li et al. [2021], was designed to find stationary points of averages of smooth nonconvex functions. In this work, we study PAGE in the broad framework of $\tau$-weakly convex functions, which provides a continuous interpolation between the general nonconvex $L$-smooth case ($\tau = L$) and the convex case ($\tau = 0$). We establish new convergence rates for PAGE, showing that its complexity improves as $\tau$ decreases.

## 📝 요약

이 논문은 Li et al. [2021]이 제안한 PAGE 알고리즘을 $\tau$-약볼록 함수의 맥락에서 연구합니다. $\tau$-약볼록 함수는 일반적인 비볼록 $L$-매끄러운 함수와 볼록 함수 사이를 연속적으로 연결합니다. 연구 결과, PAGE 알고리즘의 수렴 속도가 $\tau$ 값이 감소할수록 개선된다는 새로운 복잡도를 제시합니다. 주요 기여는 PAGE 알고리즘의 적용 범위를 확장하고, $\tau$-약볼록 함수에 대한 수렴성을 입증한 것입니다.

## 🎯 주요 포인트

- 1. PAGE 알고리즘은 Li et al. [2021]에 의해 도입된 확률적 알고리즘으로, 매끄러운 비볼록 함수의 평균의 정류점을 찾기 위해 설계되었습니다.
- 2. 이 연구에서는 PAGE 알고리즘을 $\tau$-약볼록 함수의 넓은 틀에서 연구하였습니다.
- 3. $\tau$-약볼록 함수는 일반 비볼록 $L$-매끄러운 경우($\tau = L$)와 볼록 경우($\tau = 0$) 사이의 연속적인 보간을 제공합니다.
- 4. PAGE 알고리즘의 새로운 수렴 속도를 확립하였으며, $\tau$가 감소함에 따라 알고리즘의 복잡도가 개선됨을 보여주었습니다.


---

*Generated on 2025-09-24 03:08:28*