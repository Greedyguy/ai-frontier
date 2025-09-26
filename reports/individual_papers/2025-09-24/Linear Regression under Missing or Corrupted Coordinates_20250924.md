<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:18:38.949551",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Linear Regression",
    "Gaussian Covariates",
    "Adversarial Missingness",
    "Information-Theoretic Lower Bounds"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Linear Regression": 0.8,
    "Gaussian Covariates": 0.75,
    "Adversarial Missingness": 0.78,
    "Information-Theoretic Lower Bounds": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Linear Regression",
        "canonical": "Linear Regression",
        "aliases": [
          "Linear Model",
          "Linear Predictor"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental statistical method widely used in machine learning and data analysis, facilitating connections to various regression techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gaussian Covariates",
        "canonical": "Gaussian Covariates",
        "aliases": [
          "Gaussian Features",
          "Normal Covariates"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific type of input data distribution critical for understanding the statistical properties of the model.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Adversarial Missingness",
        "canonical": "Adversarial Missingness",
        "aliases": [
          "Adversarial Data Deletion",
          "Adversarial Erasure"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept of data missingness due to adversarial actions, relevant for robust statistical modeling.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Information-Theoretic Lower Bounds",
        "canonical": "Information-Theoretic Lower Bounds",
        "aliases": [
          "IT Lower Bounds",
          "Information Bounds"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a theoretical framework for understanding the limits of estimation error, linking to broader topics in information theory.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
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
      "candidate_surface": "Linear Regression",
      "resolved_canonical": "Linear Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gaussian Covariates",
      "resolved_canonical": "Gaussian Covariates",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Adversarial Missingness",
      "resolved_canonical": "Adversarial Missingness",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Information-Theoretic Lower Bounds",
      "resolved_canonical": "Information-Theoretic Lower Bounds",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Linear Regression under Missing or Corrupted Coordinates

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19242.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19242](https://arxiv.org/abs/2509.19242)

## 🔗 유사한 논문
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (81.7% similar)
- [[2025-09-17/On the Rate of Gaussian Approximation for Linear Regression Problems_20250917|On the Rate of Gaussian Approximation for Linear Regression Problems]] (80.9% similar)
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (80.4% similar)
- [[2025-09-19/Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models_20250919|Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models]] (80.2% similar)
- [[2025-09-24/Stability and Generalization of Adversarial Diffusion Training_20250924|Stability and Generalization of Adversarial Diffusion Training]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Linear Regression|Linear Regression]]
**🔗 Specific Connectable**: [[keywords/Information-Theoretic Lower Bounds|Information-Theoretic Lower Bounds]]
**⚡ Unique Technical**: [[keywords/Gaussian Covariates|Gaussian Covariates]], [[keywords/Adversarial Missingness|Adversarial Missingness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19242v1 Announce Type: cross 
Abstract: We study multivariate linear regression under Gaussian covariates in two settings, where data may be erased or corrupted by an adversary under a coordinate-wise budget. In the incomplete data setting, an adversary may inspect the dataset and delete entries in up to an $\eta$-fraction of samples per coordinate; a strong form of the Missing Not At Random model. In the corrupted data setting, the adversary instead replaces values arbitrarily, and the corruption locations are unknown to the learner. Despite substantial work on missing data, linear regression under such adversarial missingness remains poorly understood, even information-theoretically. Unlike the clean setting, where estimation error vanishes with more samples, here the optimal error remains a positive function of the problem parameters. Our main contribution is to characterize this error up to constant factors across essentially the entire parameter range. Specifically, we establish novel information-theoretic lower bounds on the achievable error that match the error of (computationally efficient) algorithms. A key implication is that, perhaps surprisingly, the optimal error in the missing data setting matches that in the corruption setting-so knowing the corruption locations offers no general advantage.

## 📝 요약

이 논문은 가우시안 공변량 하에서 다변량 선형 회귀를 연구하며, 데이터가 좌표별 예산에 따라 삭제되거나 손상될 수 있는 두 가지 상황을 다룹니다. 첫 번째는 데이터가 임의로 삭제될 수 있는 불완전 데이터 상황이며, 두 번째는 데이터가 임의로 변경될 수 있는 손상 데이터 상황입니다. 주요 기여는 이러한 적대적 결측 상황에서의 최적 오류를 문제 매개변수의 함수로 특성화한 것입니다. 특히, 정보 이론적 하한을 설정하여, 알고리즘의 오류와 일치하는 최적 오류를 제시합니다. 중요한 발견은 결측 데이터와 손상 데이터 상황에서의 최적 오류가 일치한다는 점으로, 손상 위치를 아는 것이 일반적인 이점을 제공하지 않는다는 것입니다.

## 🎯 주요 포인트

- 1. 가우시안 공변량 하에서 다변량 선형 회귀를 연구하며, 데이터가 삭제되거나 적대적으로 손상될 수 있는 두 가지 설정을 다룹니다.
- 2. 불완전 데이터 설정에서는 적대자가 각 좌표당 샘플의 $\eta$-비율까지 데이터를 삭제할 수 있습니다.
- 3. 손상된 데이터 설정에서는 적대자가 임의로 값을 대체하며, 손상 위치는 학습자가 알 수 없습니다.
- 4. 정보 이론적으로 달성 가능한 오류에 대한 새로운 하한을 제시하며, 이는 효율적인 알고리즘의 오류와 일치합니다.
- 5. 손실 데이터 설정에서 최적의 오류가 손상 데이터 설정과 일치하여, 손상 위치를 아는 것이 일반적으로 이점을 제공하지 않는다는 점을 보여줍니다.


---

*Generated on 2025-09-24 15:18:38*