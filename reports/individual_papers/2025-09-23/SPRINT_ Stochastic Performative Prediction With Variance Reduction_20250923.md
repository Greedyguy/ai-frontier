---
keywords:
  - Performative Prediction
  - Stochastic Gradient Descent
  - Variance Reduction
  - Non-convex Models
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17304
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:52:03.716061",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Performative Prediction",
    "Stochastic Gradient Descent",
    "Variance Reduction",
    "Non-convex Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Performative Prediction": 0.8,
    "Stochastic Gradient Descent": 0.85,
    "Variance Reduction": 0.78,
    "Non-convex Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Performative Prediction",
        "canonical": "Performative Prediction",
        "aliases": [
          "PP"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a unique framework in machine learning where model deployment affects data distribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Stochastic Gradient Descent",
        "canonical": "Stochastic Gradient Descent",
        "aliases": [
          "SGD"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental optimization technique in machine learning, relevant for linking with other optimization methods discussed.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Variance Reduction",
        "canonical": "Variance Reduction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key technique in the proposed algorithm SPRINT, enhancing its performance over traditional methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Non-convex Models",
        "canonical": "Non-convex Models",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper focuses on improving convergence in non-convex settings, which is crucial for understanding the algorithm's applicability.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
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
      "candidate_surface": "Performative Prediction",
      "resolved_canonical": "Performative Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Stochastic Gradient Descent",
      "resolved_canonical": "Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Variance Reduction",
      "resolved_canonical": "Variance Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Non-convex Models",
      "resolved_canonical": "Non-convex Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SPRINT: Stochastic Performative Prediction With Variance Reduction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17304.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17304](https://arxiv.org/abs/2509.17304)

## 🔗 유사한 논문
- [[2025-09-23/On the Simplification of Neural Network Architectures for Predictive Process Monitoring_20250923|On the Simplification of Neural Network Architectures for Predictive Process Monitoring]] (81.4% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (81.2% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (80.7% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.7% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Stochastic Gradient Descent|Stochastic Gradient Descent]]
**🔗 Specific Connectable**: [[keywords/Variance Reduction|Variance Reduction]], [[keywords/Non-convex Models|Non-convex Models]]
**⚡ Unique Technical**: [[keywords/Performative Prediction|Performative Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17304v1 Announce Type: new 
Abstract: Performative prediction (PP) is an algorithmic framework for optimizing machine learning (ML) models where the model's deployment affects the distribution of the data it is trained on. Compared to traditional ML with fixed data, designing algorithms in PP converging to a stable point -- known as a stationary performative stable (SPS) solution -- is more challenging than the counterpart in conventional ML tasks due to the model-induced distribution shifts. While considerable efforts have been made to find SPS solutions using methods such as repeated gradient descent (RGD) and greedy stochastic gradient descent (SGD-GD), most prior studies assumed a strongly convex loss until a recent work established $\mathcal{O}(1/\sqrt{T})$ convergence of SGD-GD to SPS solutions under smooth, non-convex losses. However, this latest progress is still based on the restricted bounded variance assumption in stochastic gradient estimates and yields convergence bounds with a non-vanishing error neighborhood that scales with the variance. This limitation motivates us to improve convergence rates and reduce error in stochastic optimization for PP, particularly in non-convex settings. Thus, we propose a new algorithm called stochastic performative prediction with variance reduction (SPRINT) and establish its convergence to an SPS solution at a rate of $\mathcal{O}(1/T)$. Notably, the resulting error neighborhood is **independent** of the variance of the stochastic gradients. Experiments on multiple real datasets with non-convex models demonstrate that SPRINT outperforms SGD-GD in both convergence rate and stability.

## 📝 요약

이 논문은 수행적 예측(Performative Prediction, PP)에서 모델 배포가 데이터 분포에 영향을 미치는 상황을 다룹니다. 기존의 기법들은 강한 볼록 손실을 가정했으나, 최근 연구는 매끄럽고 비볼록한 손실에서도 수렴성을 보였습니다. 그러나 이는 확률적 경사 추정의 제한된 분산 가정에 기반하여, 수렴 속도가 느리고 오류가 남아있습니다. 이를 개선하기 위해, 본 연구는 분산 감소를 통한 새로운 알고리즘 SPRINT를 제안하며, 이는 $\mathcal{O}(1/T)$의 수렴 속도를 보장하고, 오류 범위가 분산에 독립적입니다. 실험 결과, SPRINT는 비볼록 모델에서 SGD-GD보다 더 빠르고 안정적으로 수렴함을 보여줍니다.

## 🎯 주요 포인트

- 1. 수행 예측(PP)은 모델 배포가 데이터 분포에 영향을 미치는 상황에서 머신러닝 모델을 최적화하는 알고리즘적 프레임워크입니다.
- 2. PP에서의 안정적 해(SPS) 솔루션으로의 수렴은 전통적인 ML 과제보다 더 복잡하며, 이는 모델로 인한 분포 변화 때문입니다.
- 3. 최근 연구에서는 매끄럽고 비볼록 손실 하에서 SGD-GD의 SPS 솔루션 수렴을 $\mathcal{O}(1/\sqrt{T})$로 확립했으나, 이는 확률적 경사 추정의 제한된 분산 가정에 기반합니다.
- 4. 새로운 알고리즘인 SPRINT는 확률적 경사도의 분산에 독립적인 오류 이웃을 가지며, $\mathcal{O}(1/T)$의 수렴 속도를 달성합니다.
- 5. 여러 실제 데이터셋 실험에서 SPRINT는 비볼록 모델에서 SGD-GD보다 수렴 속도와 안정성 면에서 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 01:52:03*