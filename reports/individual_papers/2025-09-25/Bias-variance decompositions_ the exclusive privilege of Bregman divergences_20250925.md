---
keywords:
  - Bregman Divergence
  - Bias-Variance Decomposition
  - Cross-Entropy Loss
  - Mahalanobis Distance
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2501.18581
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:05:57.532251",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bregman Divergence",
    "Bias-Variance Decomposition",
    "Cross-Entropy Loss",
    "Mahalanobis Distance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bregman Divergence": 0.78,
    "Bias-Variance Decomposition": 0.8,
    "Cross-Entropy Loss": 0.82,
    "Mahalanobis Distance": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bregman divergences",
        "canonical": "Bregman Divergence",
        "aliases": [
          "Bregman divergence",
          "Bregman"
        ],
        "category": "unique_technical",
        "rationale": "Bregman divergences are central to the paper's discussion on bias-variance decomposition, offering a unique perspective in machine learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "bias-variance decomposition",
        "canonical": "Bias-Variance Decomposition",
        "aliases": [
          "bias variance decomposition"
        ],
        "category": "broad_technical",
        "rationale": "This concept is fundamental to understanding model generalization and is directly addressed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "cross-entropy loss",
        "canonical": "Cross-Entropy Loss",
        "aliases": [
          "cross entropy",
          "cross-entropy"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-entropy loss is a special case of Bregman divergences, making it relevant for linking with other loss function discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "squared Mahalanobis distance",
        "canonical": "Mahalanobis Distance",
        "aliases": [
          "squared Mahalanobis",
          "Mahalanobis"
        ],
        "category": "specific_connectable",
        "rationale": "The squared Mahalanobis distance is highlighted as the only symmetric loss function with a clean bias-variance decomposition.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "loss function",
      "generalization performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bregman divergences",
      "resolved_canonical": "Bregman Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "bias-variance decomposition",
      "resolved_canonical": "Bias-Variance Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cross-entropy loss",
      "resolved_canonical": "Cross-Entropy Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "squared Mahalanobis distance",
      "resolved_canonical": "Mahalanobis Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Bias-variance decompositions: the exclusive privilege of Bregman divergences

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.18581.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2501.18581](https://arxiv.org/abs/2501.18581)

## 🔗 유사한 논문
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (81.4% similar)
- [[2025-09-23/Loss-Complexity Landscape and Model Structure Functions_20250923|Loss-Complexity Landscape and Model Structure Functions]] (80.2% similar)
- [[2025-09-23/Convergence analysis of equilibrium methods for inverse problems_20250923|Convergence analysis of equilibrium methods for inverse problems]] (80.2% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.1% similar)
- [[2025-09-24/Global Minimizers of Sigmoid Contrastive Loss_20250924|Global Minimizers of Sigmoid Contrastive Loss]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bias-Variance Decomposition|Bias-Variance Decomposition]]
**🔗 Specific Connectable**: [[keywords/Cross-Entropy Loss|Cross-Entropy Loss]], [[keywords/Mahalanobis Distance|Mahalanobis Distance]]
**⚡ Unique Technical**: [[keywords/Bregman Divergence|Bregman Divergence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.18581v2 Announce Type: replace 
Abstract: Bias-variance decompositions are widely used to understand the generalization performance of machine learning models. While the squared error loss permits a straightforward decomposition, other loss functions - such as zero-one loss or $L_1$ loss - either fail to sum bias and variance to the expected loss or rely on definitions that lack the essential properties of meaningful bias and variance. Recent research has shown that clean decompositions can be achieved for the broader class of Bregman divergences, with the cross-entropy loss as a special case. However, the necessary and sufficient conditions for these decompositions remain an open question.
  In this paper, we address this question by studying continuous, nonnegative loss functions that satisfy the identity of indiscernibles (zero loss if and only if the two arguments are identical), under mild regularity conditions. We prove that so-called $g$-Bregman divergences are the only such loss functions that have a clean bias-variance decomposition. A $g$-Bregman divergence can be transformed into a standard Bregman divergence through an invertible change of variables. This makes the squared Mahalanobis distance, up to such a variable transformation, the only symmetric loss function with a clean bias-variance decomposition. Consequently, common metrics such as $0$-$1$ and $L_1$ losses cannot admit a clean bias-variance decomposition, explaining why previous attempts have failed. We also examine the impact of relaxing the restrictions on the loss functions and how this affects our results.

## 📝 요약

이 논문은 기계 학습 모델의 일반화 성능을 이해하기 위해 사용되는 편향-분산 분해에 관한 연구입니다. 기존의 제곱 오차 손실은 간단히 분해가 가능하지만, 다른 손실 함수들은 의미 있는 편향과 분산의 속성을 만족하지 못하거나 기대 손실로 합산되지 않습니다. 이 연구에서는 Bregman 발산의 더 넓은 범주에서 명확한 분해가 가능하다는 점을 밝히고, 교차 엔트로피 손실이 그 특별한 경우임을 설명합니다. 저자들은 연속적이고 비음수인 손실 함수가 indiscernibles의 정체성을 만족할 때, $g$-Bregman 발산만이 명확한 편향-분산 분해를 가질 수 있음을 증명했습니다. 이로 인해 $0$-$1$ 및 $L_1$ 손실과 같은 일반적인 지표는 명확한 편향-분산 분해를 가질 수 없음을 설명합니다.

## 🎯 주요 포인트

- 1. 편향-분산 분해는 기계 학습 모델의 일반화 성능을 이해하는 데 널리 사용되며, Bregman 발산의 경우 명확한 분해가 가능하다.
- 2. $g$-Bregman 발산은 편향-분산 분해가 가능한 유일한 손실 함수로, 표준 Bregman 발산으로 변환될 수 있다.
- 3. $0$-$1$ 손실이나 $L_1$ 손실은 명확한 편향-분산 분해를 허용하지 않으며, 이는 이전 시도가 실패한 이유를 설명한다.
- 4. 손실 함수에 대한 제약을 완화할 경우 결과에 미치는 영향을 분석하였다.


---

*Generated on 2025-09-25 17:05:57*