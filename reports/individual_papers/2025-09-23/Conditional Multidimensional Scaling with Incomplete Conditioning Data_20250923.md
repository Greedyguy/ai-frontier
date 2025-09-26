---
keywords:
  - Conditional Multidimensional Scaling
  - Dimensionality Reduction
  - Data Imputation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16627
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:11:59.204375",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Conditional Multidimensional Scaling",
    "Dimensionality Reduction",
    "Data Imputation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Conditional Multidimensional Scaling": 0.8,
    "Dimensionality Reduction": 0.75,
    "Data Imputation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Conditional Multidimensional Scaling",
        "canonical": "Conditional Multidimensional Scaling",
        "aliases": [
          "Conditional MDS"
        ],
        "category": "unique_technical",
        "rationale": "This is the core method discussed in the paper, offering a unique approach to handling incomplete data in multidimensional scaling.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Low-Dimensional Configuration",
        "canonical": "Dimensionality Reduction",
        "aliases": [
          "Low-Dimensional Representation"
        ],
        "category": "broad_technical",
        "rationale": "Dimensionality reduction is a common theme in machine learning, facilitating connections with other techniques that reduce data complexity.",
        "novelty_score": 0.45,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Impute Missing Values",
        "canonical": "Data Imputation",
        "aliases": [
          "Missing Data Imputation"
        ],
        "category": "specific_connectable",
        "rationale": "Data imputation is crucial for handling incomplete datasets, linking to various data preprocessing and cleaning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.68,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "estimation quality",
      "knowledge discovery tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Conditional Multidimensional Scaling",
      "resolved_canonical": "Conditional Multidimensional Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Low-Dimensional Configuration",
      "resolved_canonical": "Dimensionality Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Impute Missing Values",
      "resolved_canonical": "Data Imputation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.68,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Conditional Multidimensional Scaling with Incomplete Conditioning Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16627.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16627](https://arxiv.org/abs/2509.16627)

## 🔗 유사한 논문
- [[2025-09-23/DISCO_ Mitigating Bias in Deep Learning with Conditional Distance Correlation_20250923|DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation]] (81.8% similar)
- [[2025-09-23/Local Mechanisms of Compositional Generalization in Conditional Diffusion_20250923|Local Mechanisms of Compositional Generalization in Conditional Diffusion]] (80.1% similar)
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (79.5% similar)
- [[2025-09-23/A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis_20250923|A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis]] (79.2% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dimensionality Reduction|Dimensionality Reduction]]
**🔗 Specific Connectable**: [[keywords/Data Imputation|Data Imputation]]
**⚡ Unique Technical**: [[keywords/Conditional Multidimensional Scaling|Conditional Multidimensional Scaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16627v1 Announce Type: cross 
Abstract: Conditional multidimensional scaling seeks for a low-dimensional configuration from pairwise dissimilarities, in the presence of other known features. By taking advantage of available data of the known features, conditional multidimensional scaling improves the estimation quality of the low-dimensional configuration and simplifies knowledge discovery tasks. However, existing conditional multidimensional scaling methods require full data of the known features, which may not be always attainable due to time, cost, and other constraints. This paper proposes a conditional multidimensional scaling method that can learn the low-dimensional configuration when there are missing values in the known features. The method can also impute the missing values, which provides additional insights of the problem. Computer codes of this method are maintained in the cml R package on CRAN.

## 📝 요약

이 논문은 기존의 조건부 다차원 척도법이 알려진 특징의 완전한 데이터가 필요하다는 한계를 극복하기 위해, 일부 특징 데이터가 누락된 상황에서도 저차원 구성을 학습할 수 있는 새로운 방법을 제안합니다. 이 방법은 누락된 값을 추정하여 문제에 대한 추가적인 통찰을 제공합니다. 제안된 방법의 컴퓨터 코드는 CRAN의 cml R 패키지에서 제공됩니다. 주요 기여는 누락된 데이터가 있는 상황에서도 저차원 구성의 추정 품질을 개선하고, 지식 발견 작업을 단순화하는 데 있습니다.

## 🎯 주요 포인트

- 1. 조건부 다차원 척도법은 알려진 특징이 있는 경우 쌍별 비유사성으로부터 저차원 구성을 찾는 방법이다.
- 2. 기존 방법들은 알려진 특징의 완전한 데이터가 필요하지만, 본 논문은 결측값이 있는 경우에도 학습할 수 있는 방법을 제안한다.
- 3. 제안된 방법은 결측값을 보완할 수 있어 문제에 대한 추가적인 통찰력을 제공한다.
- 4. 이 방법의 컴퓨터 코드는 CRAN의 cml R 패키지에서 관리된다.


---

*Generated on 2025-09-24 02:11:59*