<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:23:34.982785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Data Distribution Shifts",
    "Interpretable Machine Learning",
    "Case Study Analysis",
    "Data Modalities"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Data Distribution Shifts": 0.78,
    "Interpretable Machine Learning": 0.72,
    "Case Study Analysis": 0.68,
    "Data Modalities": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "distribution shifts",
        "canonical": "Data Distribution Shifts",
        "aliases": [
          "distribution changes",
          "dataset shifts"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding distribution shifts is crucial for improving model robustness and is a common challenge in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "interpretable methods",
        "canonical": "Interpretable Machine Learning",
        "aliases": [
          "explainable methods",
          "transparent models"
        ],
        "category": "broad_technical",
        "rationale": "Interpretable methods are essential for understanding model decisions and improving trust in machine learning applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "case studies",
        "canonical": "Case Study Analysis",
        "aliases": [
          "case analysis",
          "study examples"
        ],
        "category": "unique_technical",
        "rationale": "Case studies provide practical insights into the application of theoretical concepts, enhancing understanding and implementation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      },
      {
        "surface": "data modalities",
        "canonical": "Data Modalities",
        "aliases": [
          "data types",
          "data forms"
        ],
        "category": "specific_connectable",
        "rationale": "Different data modalities require tailored approaches, impacting model design and performance.",
        "novelty_score": 0.58,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "techniques",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "distribution shifts",
      "resolved_canonical": "Data Distribution Shifts",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "interpretable methods",
      "resolved_canonical": "Interpretable Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "case studies",
      "resolved_canonical": "Case Study Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "data modalities",
      "resolved_canonical": "Data Modalities",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# "What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2403.05652.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2403.05652](https://arxiv.org/abs/2403.05652)

## 🔗 유사한 논문
- [[2025-09-22/Estimating Model Performance Under Covariate Shift Without Labels_20250922|Estimating Model Performance Under Covariate Shift Without Labels]] (83.3% similar)
- [[2025-09-23/DISCO_ Mitigating Bias in Deep Learning with Conditional Distance Correlation_20250923|DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation]] (82.6% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (82.5% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (82.3% similar)
- [[2025-09-23/KNN-MMD_ Cross Domain Wireless Sensing via Local Distribution Alignment_20250923|KNN-MMD: Cross Domain Wireless Sensing via Local Distribution Alignment]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Interpretable Machine Learning|Interpretable Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Data Distribution Shifts|Data Distribution Shifts]], [[keywords/Data Modalities|Data Modalities]]
**⚡ Unique Technical**: [[keywords/Case Study Analysis|Case Study Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2403.05652v3 Announce Type: replace-cross 
Abstract: The performance of machine learning models relies heavily on the quality of input data, yet real-world applications often face significant data-related challenges. A common issue arises when curating training data or deploying models: two datasets from the same domain may exhibit differing distributions. While many techniques exist for detecting such distribution shifts, there is a lack of comprehensive methods to explain these differences in a human-understandable way beyond opaque quantitative metrics. To bridge this gap, we propose a versatile framework of interpretable methods for comparing datasets. Using a variety of case studies, we demonstrate the effectiveness of our approach across diverse data modalities-including tabular data, text data, images, time-series signals -- in both low and high-dimensional settings. These methods complement existing techniques by providing actionable and interpretable insights to better understand and address distribution shifts.

## 📝 요약

이 논문은 머신러닝 모델의 성능이 입력 데이터의 품질에 크게 의존하지만, 실제 응용에서는 데이터 관련 문제에 직면하는 경우가 많다는 점을 다룹니다. 특히, 같은 도메인의 두 데이터셋이 서로 다른 분포를 보일 때 발생하는 문제를 해결하기 위해, 기존의 정량적 지표를 넘어 사람에게 이해 가능한 방식으로 분포 차이를 설명하는 포괄적인 방법이 부족하다는 점을 지적합니다. 이를 해결하기 위해, 저자들은 데이터셋을 비교할 수 있는 해석 가능한 방법론의 프레임워크를 제안합니다. 다양한 사례 연구를 통해 이 접근법이 표 형식 데이터, 텍스트 데이터, 이미지, 시계열 신호 등 다양한 데이터 형태에서 효과적임을 입증하였으며, 기존 기법을 보완하여 분포 변화를 이해하고 해결하는 데 유용한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 머신러닝 모델의 성능은 입력 데이터의 품질에 크게 의존하지만, 실제 응용에서는 데이터 관련 문제에 직면하는 경우가 많다.
- 2. 동일한 도메인의 두 데이터셋이 서로 다른 분포를 보이는 경우가 흔히 발생하며, 이를 탐지하는 기술은 많지만, 인간이 이해할 수 있는 방식으로 설명하는 방법은 부족하다.
- 3. 본 연구는 데이터셋을 비교할 수 있는 해석 가능한 방법의 프레임워크를 제안하며, 다양한 데이터 모달리티에서 효과성을 입증하였다.
- 4. 제안된 방법은 기존 기술을 보완하여 분포 변화에 대한 이해와 해결을 위한 실행 가능하고 해석 가능한 통찰을 제공한다.


---

*Generated on 2025-09-24 14:23:34*