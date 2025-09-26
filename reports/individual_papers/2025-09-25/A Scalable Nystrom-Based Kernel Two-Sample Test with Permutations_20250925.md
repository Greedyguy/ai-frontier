---
keywords:
  - Two-Sample Hypothesis Testing
  - Maximum Mean Discrepancy
  - Nyström Approximation
  - Nonparametric Testing
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2502.13570
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:37:56.336980",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Two-Sample Hypothesis Testing",
    "Maximum Mean Discrepancy",
    "Nyström Approximation",
    "Nonparametric Testing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Two-Sample Hypothesis Testing": 0.75,
    "Maximum Mean Discrepancy": 0.8,
    "Nyström Approximation": 0.78,
    "Nonparametric Testing": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "two-sample hypothesis testing",
        "canonical": "Two-Sample Hypothesis Testing",
        "aliases": [
          "two-sample test",
          "two-sample hypothesis test"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific statistical method that is central to the paper's contribution.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "maximum mean discrepancy",
        "canonical": "Maximum Mean Discrepancy",
        "aliases": [
          "MMD"
        ],
        "category": "specific_connectable",
        "rationale": "A key statistical measure used in the paper, relevant for linking to statistical testing methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Nyström approximation",
        "canonical": "Nyström Approximation",
        "aliases": [
          "Nyström method"
        ],
        "category": "unique_technical",
        "rationale": "A specific computational technique used to enhance the efficiency of the test, relevant for algorithmic discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "nonparametric testing",
        "canonical": "Nonparametric Testing",
        "aliases": [
          "nonparametric test"
        ],
        "category": "broad_technical",
        "rationale": "A broad category of statistical tests that the paper contributes to, useful for linking to statistical methodologies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "two-sample hypothesis testing",
      "resolved_canonical": "Two-Sample Hypothesis Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "maximum mean discrepancy",
      "resolved_canonical": "Maximum Mean Discrepancy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Nyström approximation",
      "resolved_canonical": "Nyström Approximation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "nonparametric testing",
      "resolved_canonical": "Nonparametric Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# A Scalable Nystr\"om-Based Kernel Two-Sample Test with Permutations

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13570.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2502.13570](https://arxiv.org/abs/2502.13570)

## 🔗 유사한 논문
- [[2025-09-24/Recovering Wasserstein Distance Matrices from Few Measurements_20250924|Recovering Wasserstein Distance Matrices from Few Measurements]] (81.2% similar)
- [[2025-09-23/A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis_20250923|A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis]] (80.9% similar)
- [[2025-09-24/"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts_20250924|"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts]] (80.9% similar)
- [[2025-09-24/Measuring Sample Quality with Copula Discrepancies_20250924|Measuring Sample Quality with Copula Discrepancies]] (79.8% similar)
- [[2025-09-23/Kernel K-means clustering of distributional data_20250923|Kernel K-means clustering of distributional data]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonparametric Testing|Nonparametric Testing]]
**🔗 Specific Connectable**: [[keywords/Maximum Mean Discrepancy|Maximum Mean Discrepancy]]
**⚡ Unique Technical**: [[keywords/Two-Sample Hypothesis Testing|Two-Sample Hypothesis Testing]], [[keywords/Nyström Approximation|Nyström Approximation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13570v3 Announce Type: replace-cross 
Abstract: Two-sample hypothesis testing-determining whether two sets of data are drawn from the same distribution-is a fundamental problem in statistics and machine learning with broad scientific applications. In the context of nonparametric testing, maximum mean discrepancy (MMD) has gained popularity as a test statistic due to its flexibility and strong theoretical foundations. However, its use in large-scale scenarios is plagued by high computational costs. In this work, we use a Nystr\"om approximation of the MMD to design a computationally efficient and practical testing algorithm while preserving statistical guarantees. Our main result is a finite-sample bound on the power of the proposed test for distributions that are sufficiently separated with respect to the MMD. The derived separation rate matches the known minimax optimal rate in this setting. We support our findings with a series of numerical experiments, emphasizing applicability to realistic scientific data.

## 📝 요약

이 논문은 두 집단의 데이터가 동일한 분포에서 나왔는지를 검정하는 문제를 다룹니다. 비모수 검정에서 최대 평균 차이(MMD)는 유연성과 이론적 기반으로 인기를 얻고 있지만, 대규모 데이터에서는 계산 비용이 높다는 문제가 있습니다. 본 연구에서는 MMD의 Nyström 근사를 활용하여 계산 효율적이고 실용적인 검정 알고리즘을 제안하며, 통계적 보장을 유지합니다. 주요 기여는 MMD에 대해 충분히 분리된 분포에 대한 제안된 검정의 유한 표본 검정력 경계를 제시한 것입니다. 이는 기존의 최적 분리율과 일치합니다. 연구 결과는 실제 과학 데이터에의 적용 가능성을 강조하는 일련의 수치 실험을 통해 뒷받침됩니다.

## 🎯 주요 포인트

- 1. 두 표본 가설 검정은 두 데이터 집합이 동일한 분포에서 추출되었는지를 판단하는 문제로, 통계 및 머신러닝에서 중요한 문제이다.
- 2. 최대 평균 차이(MMD)는 비모수 검정에서 유연성과 강력한 이론적 기반으로 인해 인기 있는 검정 통계량이다.
- 3. 본 연구에서는 MMD의 Nystr\"om 근사를 사용하여 계산 효율적이고 실용적인 검정 알고리즘을 설계하면서 통계적 보장을 유지한다.
- 4. 제안된 검정의 파워에 대한 유한 표본 경계를 도출하였으며, 이는 MMD에 대해 충분히 분리된 분포에 적용된다.
- 5. 제안된 방법의 분리율은 기존의 미니맥스 최적율과 일치하며, 현실적인 과학 데이터에 대한 적용 가능성을 강조하는 수치 실험을 통해 이를 뒷받침한다.


---

*Generated on 2025-09-26 08:37:56*