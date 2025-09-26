---
keywords:
  - Kernel-based Conditional Independence
  - Conditional Independence Testing
  - Kernel Ridge Regression
  - Data Splitting
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2402.13196
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:31:54.940921",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kernel-based Conditional Independence",
    "Conditional Independence Testing",
    "Kernel Ridge Regression",
    "Data Splitting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kernel-based Conditional Independence": 0.78,
    "Conditional Independence Testing": 0.8,
    "Kernel Ridge Regression": 0.77,
    "Data Splitting": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kernel-based Conditional Independence",
        "canonical": "Kernel-based Conditional Independence",
        "aliases": [
          "KCI"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method discussed in the paper, which is central to the research and not widely covered in existing vocabularies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "conditional independence testing",
        "canonical": "Conditional Independence Testing",
        "aliases": [
          "CI Testing"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key concept in statistical testing that can connect to other research on statistical methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "kernel ridge regression",
        "canonical": "Kernel Ridge Regression",
        "aliases": [
          "KRR"
        ],
        "category": "broad_technical",
        "rationale": "This is a well-known machine learning technique that provides a basis for the statistical methods discussed.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      },
      {
        "surface": "data splitting",
        "canonical": "Data Splitting",
        "aliases": [
          "Split Data"
        ],
        "category": "specific_connectable",
        "rationale": "Data splitting is a crucial step in the proposed method, enhancing the reliability of statistical tests.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "test level",
      "false positives"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kernel-based Conditional Independence",
      "resolved_canonical": "Kernel-based Conditional Independence",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "conditional independence testing",
      "resolved_canonical": "Conditional Independence Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "kernel ridge regression",
      "resolved_canonical": "Kernel Ridge Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "data splitting",
      "resolved_canonical": "Data Splitting",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Practical Kernel Tests of Conditional Independence

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2402.13196.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2402.13196](https://arxiv.org/abs/2402.13196)

## 🔗 유사한 논문
- [[2025-09-23/DISCO_ Mitigating Bias in Deep Learning with Conditional Distance Correlation_20250923|DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation]] (80.0% similar)
- [[2025-09-23/A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis_20250923|A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis]] (79.7% similar)
- [[2025-09-23/Conditional Multidimensional Scaling with Incomplete Conditioning Data_20250923|Conditional Multidimensional Scaling with Incomplete Conditioning Data]] (79.2% similar)
- [[2025-09-23/Kernel K-means clustering of distributional data_20250923|Kernel K-means clustering of distributional data]] (78.5% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (77.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Kernel Ridge Regression|Kernel Ridge Regression]]
**🔗 Specific Connectable**: [[keywords/Conditional Independence Testing|Conditional Independence Testing]], [[keywords/Data Splitting|Data Splitting]]
**⚡ Unique Technical**: [[keywords/Kernel-based Conditional Independence|Kernel-based Conditional Independence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2402.13196v2 Announce Type: replace 
Abstract: We describe a data-efficient, kernel-based approach to statistical testing of conditional independence. A major challenge of conditional independence testing is to obtain the correct test level (the specified upper bound on the rate of false positives), while still attaining competitive test power. Excess false positives arise due to bias in the test statistic, which is in our case obtained using nonparametric kernel ridge regression. We propose SplitKCI, an automated method for bias control for the Kernel-based Conditional Independence (KCI) test based on data splitting. We show that our approach significantly improves test level control for KCI without sacrificing test power, both theoretically and for synthetic and real-world data.

## 📝 요약

이 논문은 조건부 독립성의 통계적 검정을 위한 데이터 효율적인 커널 기반 접근법을 제안합니다. 조건부 독립성 검정에서 주요 과제는 잘못된 양성률을 억제하면서 검정의 파워를 유지하는 것입니다. 이를 위해 비편향적 커널 릿지 회귀를 사용한 통계량의 편향 문제를 해결하고자 합니다. 제안된 방법인 SplitKCI는 데이터 분할을 통해 커널 기반 조건부 독립성(KCI) 검정의 편향을 자동으로 제어합니다. 이 방법은 이론적으로나 실제 데이터에서 KCI의 검정 수준을 크게 개선하면서도 검정의 파워를 유지하는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 조건부 독립성 검정을 위한 데이터 효율적 커널 기반 접근법을 제안합니다.
- 2. SplitKCI는 데이터 분할을 통해 커널 기반 조건부 독립성 검정(KCI)의 편향을 자동으로 조절합니다.
- 3. 제안된 방법은 KCI의 검정 수준을 크게 개선하면서도 검정력을 유지합니다.
- 4. 이론적 분석과 실험 결과 모두 제안된 방법의 효과를 입증합니다.


---

*Generated on 2025-09-24 02:31:54*