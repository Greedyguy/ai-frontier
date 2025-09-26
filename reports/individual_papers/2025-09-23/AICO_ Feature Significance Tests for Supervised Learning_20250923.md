---
keywords:
  - Machine Learning
  - Feature Significance Tests
  - Regression and Classification Algorithms
  - High-Dimensional Data
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.23396
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:06:16.192906",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Feature Significance Tests",
    "Regression and Classification Algorithms",
    "High-Dimensional Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.7,
    "Feature Significance Tests": 0.8,
    "Regression and Classification Algorithms": 0.75,
    "High-Dimensional Data": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Supervised Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "Supervised ML"
        ],
        "category": "broad_technical",
        "rationale": "Supervised learning is a fundamental aspect of machine learning, providing a strong link to broader technical discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Feature Significance Tests",
        "canonical": "Feature Significance Tests",
        "aliases": [
          "Feature Importance Tests"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique method introduced in the paper, offering a new perspective on evaluating feature importance.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Regression or Classification Algorithm",
        "canonical": "Regression and Classification Algorithms",
        "aliases": [
          "Regression Algorithms",
          "Classification Algorithms"
        ],
        "category": "specific_connectable",
        "rationale": "These are core components of machine learning models, relevant for linking discussions on model evaluation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "High-Dimensional Settings",
        "canonical": "High-Dimensional Data",
        "aliases": [
          "High-Dimensional Environments"
        ],
        "category": "specific_connectable",
        "rationale": "High-dimensional data is a common challenge in machine learning, relevant for discussions on computational efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "model performance",
      "test set",
      "real-world data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Supervised Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Feature Significance Tests",
      "resolved_canonical": "Feature Significance Tests",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Regression or Classification Algorithm",
      "resolved_canonical": "Regression and Classification Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "High-Dimensional Settings",
      "resolved_canonical": "High-Dimensional Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# AICO: Feature Significance Tests for Supervised Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.23396.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.23396](https://arxiv.org/abs/2506.23396)

## 🔗 유사한 논문
- [[2025-09-23/Model Guidance via Robust Feature Attribution_20250923|Model Guidance via Robust Feature Attribution]] (83.3% similar)
- [[2025-09-23/The Impact of Feature Scaling In Machine Learning_ Effects on Regression and Classification Tasks_20250923|The Impact of Feature Scaling In Machine Learning: Effects on Regression and Classification Tasks]] (82.0% similar)
- [[2025-09-22/On the (In)Significance of Feature Selection in High-Dimensional Datasets_20250922|On the (In)Significance of Feature Selection in High-Dimensional Datasets]] (81.9% similar)
- [[2025-09-22/Top-$k$ Feature Importance Ranking_20250922|Top-$k$ Feature Importance Ranking]] (80.9% similar)
- [[2025-09-23/Significativity Indices for Agreement Values_20250923|Significativity Indices for Agreement Values]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Regression and Classification Algorithms|Regression and Classification Algorithms]], [[keywords/High-Dimensional Data|High-Dimensional Data]]
**⚡ Unique Technical**: [[keywords/Feature Significance Tests|Feature Significance Tests]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.23396v2 Announce Type: replace-cross 
Abstract: The opacity of many supervised learning algorithms remains a key challenge, hindering scientific discovery and limiting broader deployment -- particularly in high-stakes domains. This paper develops model- and distribution-agnostic significance tests to assess the influence of input features in any regression or classification algorithm. Our method evaluates a feature's incremental contribution to model performance by masking its values across samples. Under the null hypothesis, the distribution of performance differences across a test set has a non-positive median. We construct a uniformly most powerful, randomized sign test for this median, yielding exact p-values for assessing feature significance and confidence intervals with exact coverage for estimating population-level feature importance. The approach requires minimal assumptions, avoids model retraining or auxiliary models, and remains computationally efficient even for large-scale, high-dimensional settings. Experiments on synthetic tasks validate its statistical and computational advantages, and applications to real-world data illustrate its practical utility.

## 📝 요약

이 논문은 회귀 또는 분류 알고리즘에서 입력 특징의 중요성을 평가하기 위한 모델 및 분포에 무관한 유의성 검정을 개발했습니다. 이 방법은 특징의 값을 샘플에서 마스킹하여 모델 성능에 대한 기여도를 평가합니다. 귀무 가설 하에서 테스트 세트의 성능 차이 분포는 비양수의 중앙값을 가집니다. 이를 위해 중앙값에 대한 무작위 부호 검정을 구성하여 특징 유의성을 평가하는 정확한 p-값과 모집단 수준의 특징 중요성을 추정하는 신뢰 구간을 제공합니다. 이 접근법은 최소한의 가정을 필요로 하며, 모델 재훈련이나 보조 모델 없이도 대규모, 고차원 환경에서 계산 효율성을 유지합니다. 실험 결과, 통계적 및 계산적 이점이 입증되었으며, 실제 데이터에 대한 적용을 통해 실용성을 보여주었습니다.

## 🎯 주요 포인트

- 1. 많은 지도 학습 알고리즘의 불투명성은 과학적 발견을 방해하고 특히 고위험 분야에서의 광범위한 배치를 제한하는 주요 문제입니다.
- 2. 본 논문은 회귀 또는 분류 알고리즘에서 입력 특징의 영향을 평가하기 위한 모델 및 분포에 무관한 유의성 검정을 개발합니다.
- 3. 제안된 방법은 특징의 값을 샘플 전반에 걸쳐 마스킹하여 모델 성능에 대한 특징의 기여도를 평가합니다.
- 4. 이 접근법은 최소한의 가정을 필요로 하며, 모델 재훈련이나 보조 모델을 피하고 대규모, 고차원 설정에서도 계산 효율성을 유지합니다.
- 5. 합성 작업에 대한 실험은 통계적 및 계산적 이점을 검증하고, 실제 데이터에 대한 응용은 실용적인 유용성을 보여줍니다.


---

*Generated on 2025-09-24 03:06:16*