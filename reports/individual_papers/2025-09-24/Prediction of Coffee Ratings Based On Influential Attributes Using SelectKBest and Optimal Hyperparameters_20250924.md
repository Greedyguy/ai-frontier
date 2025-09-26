<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:46:09.604201",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "XGBoost",
    "Feature Selection",
    "Hyperparameter Tuning",
    "Ensemble Methods"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "XGBoost": 0.75,
    "Feature Selection": 0.8,
    "Hyperparameter Tuning": 0.82,
    "Ensemble Methods": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Machine Learning is a central theme of the paper, connecting it to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "XGBoost",
        "canonical": "XGBoost",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "XGBoost is highlighted as a key model in the study, offering a specific connection to ensemble learning techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Feature Selection",
        "canonical": "Feature Selection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Feature Selection is crucial for the study's methodology, linking to broader discussions on data preprocessing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hyperparameter Tuning",
        "canonical": "Hyperparameter Tuning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Hyperparameter Tuning is essential for model optimization, providing a link to advanced model training techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Ensemble Methods",
        "canonical": "Ensemble Methods",
        "aliases": [
          "Ensemble Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Ensemble Methods are emphasized for their superior performance, connecting to studies on model improvement strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Decision Tree",
      "K-Nearest Neighbors",
      "F1-score"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "XGBoost",
      "resolved_canonical": "XGBoost",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Feature Selection",
      "resolved_canonical": "Feature Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hyperparameter Tuning",
      "resolved_canonical": "Hyperparameter Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Ensemble Methods",
      "resolved_canonical": "Ensemble Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Prediction of Coffee Ratings Based On Influential Attributes Using SelectKBest and Optimal Hyperparameters

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18124.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18124](https://arxiv.org/abs/2509.18124)

## 🔗 유사한 논문
- [[2025-09-17/Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (79.0% similar)
- [[2025-09-24/Hierarchical Evaluation Function_ A Multi-Metric Approach for Optimizing Demand Forecasting Models_20250924|Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models]] (78.9% similar)
- [[2025-09-24/From "What to Eat?" to Perfect Recipe_ ChefMind's Chain-of-Exploration for Ambiguous User Intent in Recipe Recommendation_20250924|From "What to Eat?" to Perfect Recipe: ChefMind's Chain-of-Exploration for Ambiguous User Intent in Recipe Recommendation]] (78.8% similar)
- [[2025-09-23/The Impact of Feature Scaling In Machine Learning_ Effects on Regression and Classification Tasks_20250923|The Impact of Feature Scaling In Machine Learning: Effects on Regression and Classification Tasks]] (78.3% similar)
- [[2025-09-23/AICO_ Feature Significance Tests for Supervised Learning_20250923|AICO: Feature Significance Tests for Supervised Learning]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Feature Selection|Feature Selection]], [[keywords/Hyperparameter Tuning|Hyperparameter Tuning]], [[keywords/Ensemble Methods|Ensemble Methods]]
**⚡ Unique Technical**: [[keywords/XGBoost|XGBoost]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18124v1 Announce Type: new 
Abstract: This study explores the application of supervised machine learning algorithms to predict coffee ratings based on a combination of influential textual and numerical attributes extracted from user reviews. Through careful data preprocessing including text cleaning, feature extraction using TF-IDF, and selection with SelectKBest, the study identifies key factors contributing to coffee quality assessments. Six models (Decision Tree, KNearest Neighbors, Multi-layer Perceptron, Random Forest, Extra Trees, and XGBoost) were trained and evaluated using optimized hyperparameters. Model performance was assessed primarily using F1-score, Gmean, and AUC metrics. Results demonstrate that ensemble methods (Extra Trees, Random Forest, and XGBoost), as well as Multi-layer Perceptron, consistently outperform simpler classifiers (Decision Trees and K-Nearest Neighbors) in terms of evaluation metrics such as F1 scores, G-mean and AUC. The findings highlight the essence of rigorous feature selection and hyperparameter tuning in building robust predictive systems for sensory product evaluation, offering a data driven approach to complement traditional coffee cupping by expertise of trained professionals.

## 📝 요약

이 연구는 사용자 리뷰에서 추출한 텍스트 및 수치 속성을 기반으로 커피 평점을 예측하기 위해 지도 학습 알고리즘을 적용했습니다. 데이터 전처리 과정에서 텍스트 정리, TF-IDF를 통한 특징 추출, SelectKBest를 통한 특징 선택을 수행하여 커피 품질 평가에 기여하는 주요 요소를 식별했습니다. 의사결정나무, K-최근접 이웃, 다층 퍼셉트론, 랜덤 포레스트, 엑스트라 트리, XGBoost 등 6개의 모델을 최적화된 하이퍼파라미터로 학습 및 평가했으며, F1-score, Gmean, AUC를 주요 성능 지표로 사용했습니다. 결과적으로, 앙상블 방법(엑스트라 트리, 랜덤 포레스트, XGBoost)과 다층 퍼셉트론이 단순한 분류기(의사결정나무, K-최근접 이웃)보다 우수한 성능을 보였습니다. 이 연구는 특징 선택과 하이퍼파라미터 튜닝의 중요성을 강조하며, 전통적인 커피 감별을 보완하는 데이터 기반 접근법을 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 사용자 리뷰에서 추출한 텍스트 및 수치 속성을 기반으로 커피 평점을 예측하기 위해 지도 학습 알고리즘을 적용했습니다.
- 2. 텍스트 정리, TF-IDF를 활용한 특징 추출, SelectKBest를 통한 선택 등 신중한 데이터 전처리를 통해 커피 품질 평가에 기여하는 주요 요소를 식별했습니다.
- 3. Decision Tree, K-Nearest Neighbors, Multi-layer Perceptron, Random Forest, Extra Trees, XGBoost 등 여섯 가지 모델을 최적화된 하이퍼파라미터로 학습 및 평가했습니다.
- 4. 결과에 따르면, Extra Trees, Random Forest, XGBoost와 같은 앙상블 방법과 Multi-layer Perceptron이 F1-score, G-mean, AUC 등의 평가 지표에서 단순 분류기보다 우수한 성능을 보였습니다.
- 5. 연구 결과는 감각 제품 평가를 위한 강력한 예측 시스템 구축에 있어 철저한 특징 선택과 하이퍼파라미터 튜닝의 중요성을 강조하며, 전통적인 커피 감별을 보완하는 데이터 기반 접근 방식을 제안합니다.


---

*Generated on 2025-09-24 14:46:09*