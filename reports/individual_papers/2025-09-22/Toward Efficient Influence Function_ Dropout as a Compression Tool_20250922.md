---
keywords:
  - Influence Function
  - Dropout
  - Gradient Compression
  - Machine Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15651
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:08:12.567616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Influence Function",
    "Dropout",
    "Gradient Compression",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Influence Function": 0.8,
    "Dropout": 0.75,
    "Gradient Compression": 0.7,
    "Machine Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Influence Function",
        "canonical": "Influence Function",
        "aliases": [
          "Influence Functions"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, offering a novel approach to compute it efficiently.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dropout",
        "canonical": "Dropout",
        "aliases": [
          "Dropout Technique"
        ],
        "category": "specific_connectable",
        "rationale": "Used as a compression tool in the paper, linking it to its broader applications in neural networks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gradient Compression",
        "canonical": "Gradient Compression",
        "aliases": [
          "Compressed Gradients"
        ],
        "category": "unique_technical",
        "rationale": "A novel application in the paper, crucial for reducing computational overhead.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "The foundational field for the paper's context, connecting various technical aspects.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "training data",
      "model's performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Influence Function",
      "resolved_canonical": "Influence Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dropout",
      "resolved_canonical": "Dropout",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gradient Compression",
      "resolved_canonical": "Gradient Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Toward Efficient Influence Function: Dropout as a Compression Tool

**Korean Title:** 효율적인 영향 함수로: 압축 도구로서의 드롭아웃

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15651.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15651](https://arxiv.org/abs/2509.15651)

## 🔗 유사한 논문
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (83.8% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (81.9% similar)
- [[2025-09-22/Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions_20250922|Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions]] (80.8% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (79.7% similar)
- [[2025-09-22/Estimating Model Performance Under Covariate Shift Without Labels_20250922|Estimating Model Performance Under Covariate Shift Without Labels]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Dropout|Dropout]]
**⚡ Unique Technical**: [[keywords/Influence Function|Influence Function]], [[keywords/Gradient Compression|Gradient Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15651v1 Announce Type: cross 
Abstract: Assessing the impact the training data on machine learning models is crucial for understanding the behavior of the model, enhancing the transparency, and selecting training data. Influence function provides a theoretical framework for quantifying the effect of training data points on model's performance given a specific test data. However, the computational and memory costs of influence function presents significant challenges, especially for large-scale models, even when using approximation methods, since the gradients involved in computation are as large as the model itself. In this work, we introduce a novel approach that leverages dropout as a gradient compression mechanism to compute the influence function more efficiently. Our method significantly reduces computational and memory overhead, not only during the influence function computation but also in gradient compression process. Through theoretical analysis and empirical validation, we demonstrate that our method could preserves critical components of the data influence and enables its application to modern large-scale models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15651v1 발표 유형: 교차  
초록: 머신 러닝 모델에 대한 훈련 데이터의 영향을 평가하는 것은 모델의 행동을 이해하고, 투명성을 향상시키며, 훈련 데이터를 선택하는 데 있어 중요합니다. 영향 함수는 특정 테스트 데이터가 주어졌을 때 훈련 데이터 포인트가 모델 성능에 미치는 영향을 정량화하기 위한 이론적 틀을 제공합니다. 그러나 영향 함수의 계산 및 메모리 비용은 특히 대규모 모델의 경우 상당한 도전 과제를 제시합니다. 근사 방법을 사용하더라도 계산에 관련된 기울기가 모델 자체만큼 크기 때문입니다. 이 연구에서는 드롭아웃을 기울기 압축 메커니즘으로 활용하여 영향 함수를 보다 효율적으로 계산하는 새로운 접근 방식을 소개합니다. 우리의 방법은 영향 함수 계산뿐만 아니라 기울기 압축 과정에서도 계산 및 메모리 오버헤드를 크게 줄입니다. 이론적 분석과 실증적 검증을 통해, 우리의 방법이 데이터 영향의 중요한 요소를 보존하고 현대의 대규모 모델에 적용 가능함을 입증합니다.

## 📝 요약

이 논문은 머신러닝 모델의 학습 데이터가 모델 성능에 미치는 영향을 평가하는 방법을 제안합니다. 기존의 영향 함수는 계산 및 메모리 비용이 높아 대규모 모델에 적용하기 어려웠습니다. 이를 해결하기 위해, 저자들은 드롭아웃을 활용한 새로운 접근법을 제안하여 영향 함수 계산의 효율성을 높였습니다. 이 방법은 계산 및 메모리 부담을 줄이고, 대규모 모델에서도 데이터 영향의 핵심 요소를 보존할 수 있음을 이론적 분석과 실험을 통해 입증했습니다.

## 🎯 주요 포인트

- 1. 머신러닝 모델의 훈련 데이터가 모델 성능에 미치는 영향을 평가하는 것은 모델의 행동 이해, 투명성 향상, 훈련 데이터 선택에 중요하다.
- 2. 영향 함수는 특정 테스트 데이터에 대해 훈련 데이터가 모델 성능에 미치는 영향을 정량화하는 이론적 틀을 제공한다.
- 3. 대규모 모델에서 영향 함수의 계산 및 메모리 비용은 상당한 도전 과제가 되며, 이는 근사 방법을 사용하더라도 마찬가지이다.
- 4. 본 연구에서는 드롭아웃을 활용한 새로운 접근법을 제안하여 영향 함수를 더 효율적으로 계산하고, 계산 및 메모리 오버헤드를 크게 줄였다.
- 5. 이 방법은 데이터 영향의 중요한 요소를 보존하면서 현대 대규모 모델에 적용 가능함을 이론적 분석과 실증적 검증을 통해 입증하였다.


---

*Generated on 2025-09-23 09:08:12*