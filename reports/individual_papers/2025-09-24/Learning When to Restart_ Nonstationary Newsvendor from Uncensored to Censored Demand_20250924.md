<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:12:21.764464",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Nonstationary Newsvendor Problem",
    "Distributional Detection and Restart Framework",
    "Nonparametric Demand Models",
    "Censored Demand Settings"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Nonstationary Newsvendor Problem": 0.78,
    "Distributional Detection and Restart Framework": 0.82,
    "Nonparametric Demand Models": 0.77,
    "Censored Demand Settings": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "nonstationary newsvendor problem",
        "canonical": "Nonstationary Newsvendor Problem",
        "aliases": [
          "dynamic newsvendor",
          "adaptive newsvendor"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper and represents a specific class of stochastic optimization problems, facilitating connections to related research in adaptive decision-making under uncertainty.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "distributional-detection-and-restart framework",
        "canonical": "Distributional Detection and Restart Framework",
        "aliases": [
          "detection-restart framework"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a novel contribution of the paper, providing a method for handling nonstationarity, which is applicable to a wide range of stochastic optimization problems.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "nonparametric demand models",
        "canonical": "Nonparametric Demand Models",
        "aliases": [
          "demand models",
          "nonparametric models"
        ],
        "category": "broad_technical",
        "rationale": "This term links to broader discussions in demand forecasting and modeling, which are relevant to various fields in operations research and economics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "censored demand settings",
        "canonical": "Censored Demand Settings",
        "aliases": [
          "demand censoring",
          "censored demand"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding and addressing demand censoring is crucial for accurate demand forecasting and inventory management, linking to broader topics in data analysis and operations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "algorithm",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "nonstationary newsvendor problem",
      "resolved_canonical": "Nonstationary Newsvendor Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "distributional-detection-and-restart framework",
      "resolved_canonical": "Distributional Detection and Restart Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "nonparametric demand models",
      "resolved_canonical": "Nonparametric Demand Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "censored demand settings",
      "resolved_canonical": "Censored Demand Settings",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Learning When to Restart: Nonstationary Newsvendor from Uncensored to Censored Demand

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18709.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18709](https://arxiv.org/abs/2509.18709)

## 🔗 유사한 논문
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (81.1% similar)
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (80.5% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (80.0% similar)
- [[2025-09-23/Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks_20250923|Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks]] (80.0% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading: An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonparametric Demand Models|Nonparametric Demand Models]]
**🔗 Specific Connectable**: [[keywords/Censored Demand Settings|Censored Demand Settings]]
**⚡ Unique Technical**: [[keywords/Nonstationary Newsvendor Problem|Nonstationary Newsvendor Problem]], [[keywords/Distributional Detection and Restart Framework|Distributional Detection and Restart Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18709v1 Announce Type: cross 
Abstract: We study nonstationary newsvendor problems under nonparametric demand models and general distributional measures of nonstationarity, addressing the practical challenges of unknown degree of nonstationarity and demand censoring. We propose a novel distributional-detection-and-restart framework for learning in nonstationary environments, and instantiate it through two efficient algorithms for the uncensored and censored demand settings. The algorithms are fully adaptive, requiring no prior knowledge of the degree and type of nonstationarity, and offer a flexible yet powerful approach to handling both abrupt and gradual changes in nonstationary environments. We establish a comprehensive optimality theory for our algorithms by deriving matching regret upper and lower bounds under both general and refined structural conditions with nontrivial proof techniques that are of independent interest. Numerical experiments using real-world datasets, including nurse staffing data for emergency departments and COVID-19 test demand data, showcase the algorithms' superior and robust empirical performance. While motivated by the newsvendor problem, the distributional-detection-and-restart framework applies broadly to a wide class of nonstationary stochastic optimization problems. Managerially, our framework provides a practical, easy-to-deploy, and theoretically grounded solution for decision-making under nonstationarity.

## 📝 요약

이 논문은 비정상적인 수요 모델과 일반적인 비정상성 분포 측정에서의 비정상 뉴스벤더 문제를 다룹니다. 비정상성의 정도와 수요 검열의 미지성을 해결하기 위해, 비정상 환경에서 학습할 수 있는 새로운 분포 탐지 및 재시작 프레임워크를 제안합니다. 이 프레임워크는 검열된 수요와 그렇지 않은 수요 설정에 대해 두 가지 효율적인 알고리즘으로 구현되며, 비정상성의 정도와 유형에 대한 사전 지식 없이도 완전히 적응할 수 있습니다. 이 알고리즘은 급격한 변화와 점진적인 변화를 모두 처리할 수 있는 강력한 접근 방식을 제공합니다. 알고리즘의 최적 이론을 확립하고, 일반 및 정제된 구조적 조건 하에서 일치하는 후회 상한 및 하한을 도출합니다. 실제 데이터셋을 사용한 실험 결과, 알고리즘의 우수하고 견고한 성능을 보여줍니다. 이 프레임워크는 뉴스벤더 문제뿐만 아니라 다양한 비정상 확률 최적화 문제에도 적용될 수 있으며, 비정상성 하에서의 의사결정에 실용적이고 이론적으로 근거 있는 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 비정상 수요 모델과 일반적인 비정상성 분포 측정 하의 비정상 뉴스벤더 문제를 연구합니다.
- 2. 비정상 환경에서 학습을 위한 새로운 분포 감지 및 재시작 프레임워크를 제안하고, 검열되지 않은 수요와 검열된 수요 설정에 대한 두 가지 효율적인 알고리즘을 구현합니다.
- 3. 알고리즘은 비정상성의 정도와 유형에 대한 사전 지식 없이 완전히 적응적이며, 급격한 변화와 점진적인 변화를 모두 처리할 수 있는 유연하고 강력한 접근 방식을 제공합니다.
- 4. 실제 데이터셋을 사용한 수치 실험에서 알고리즘의 뛰어난 성능을 입증하였으며, 이는 간호 인력 배치 데이터와 COVID-19 테스트 수요 데이터를 포함합니다.
- 5. 제안된 프레임워크는 뉴스벤더 문제뿐만 아니라 광범위한 비정상 확률 최적화 문제에 적용 가능하며, 비정상성 하에서의 의사결정을 위한 실용적이고 이론적으로 기반을 둔 솔루션을 제공합니다.


---

*Generated on 2025-09-24 15:12:21*