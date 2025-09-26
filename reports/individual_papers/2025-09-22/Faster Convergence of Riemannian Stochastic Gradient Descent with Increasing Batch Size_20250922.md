---
keywords:
  - Riemannian Stochastic Gradient Descent
  - Batch Size Optimization
  - Stochastic Oracle Complexity
  - Learning Rate Scheduling
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2501.18164
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:03:43.434432",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Riemannian Stochastic Gradient Descent",
    "Batch Size Optimization",
    "Stochastic Oracle Complexity",
    "Learning Rate Scheduling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Riemannian Stochastic Gradient Descent": 0.78,
    "Batch Size Optimization": 0.79,
    "Stochastic Oracle Complexity": 0.77,
    "Learning Rate Scheduling": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Riemannian Stochastic Gradient Descent",
        "canonical": "Riemannian Stochastic Gradient Descent",
        "aliases": [
          "RSGD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific optimization technique relevant to the paper's focus on convergence behavior.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "increasing batch size",
        "canonical": "Batch Size Optimization",
        "aliases": [
          "dynamic batch size",
          "variable batch size"
        ],
        "category": "specific_connectable",
        "rationale": "Optimizing batch size is crucial for improving convergence rates, linking to broader optimization strategies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "stochastic first-order oracle complexity",
        "canonical": "Stochastic Oracle Complexity",
        "aliases": [
          "SFO complexity"
        ],
        "category": "unique_technical",
        "rationale": "This term is specific to the computational analysis of the optimization method discussed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "cosine annealing decay",
        "canonical": "Learning Rate Scheduling",
        "aliases": [
          "cosine decay",
          "annealing schedule"
        ],
        "category": "specific_connectable",
        "rationale": "Learning rate scheduling is a key concept in training optimization, linking to various decay strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "convergence rate",
      "computational time"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Riemannian Stochastic Gradient Descent",
      "resolved_canonical": "Riemannian Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "increasing batch size",
      "resolved_canonical": "Batch Size Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "stochastic first-order oracle complexity",
      "resolved_canonical": "Stochastic Oracle Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "cosine annealing decay",
      "resolved_canonical": "Learning Rate Scheduling",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size

**Korean Title:** 리만 기하학적 확률적 경사 하강법의 수렴 속도 향상: 배치 크기 증가의 효과

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.18164.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2501.18164](https://arxiv.org/abs/2501.18164)

## 🔗 유사한 논문
- [[2025-09-22/Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size_20250922|Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size]] (84.1% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (83.4% similar)
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (82.3% similar)
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (81.1% similar)
- [[2025-09-22/Generalization and Optimization of SGD with Lookahead_20250922|Generalization and Optimization of SGD with Lookahead]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Batch Size Optimization|Batch Size Optimization]], [[keywords/Learning Rate Scheduling|Learning Rate Scheduling]]
**⚡ Unique Technical**: [[keywords/Riemannian Stochastic Gradient Descent|Riemannian Stochastic Gradient Descent]], [[keywords/Stochastic Oracle Complexity|Stochastic Oracle Complexity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.18164v4 Announce Type: replace 
Abstract: We theoretically analyzed the convergence behavior of Riemannian stochastic gradient descent (RSGD) and found that using an increasing batch size leads to faster convergence than using a constant batch size, not only with a constant learning rate but also with a decaying learning rate, such as cosine annealing decay and polynomial decay. The convergence rate improves from $O(T^{-1}+C)$ with a constant batch size to $O(T^{-1})$ with an increasing batch size, where $T$ denotes the total number of iterations and $C$ is a constant. Using principal component analysis and low-rank matrix completion, we investigated, both theoretically and numerically, how an increasing batch size affects computational time as quantified by stochastic first-order oracle (SFO) complexity. An increasing batch size was found to reduce the SFO complexity of RSGD. Furthermore, an increasing batch size was found to offer the advantages of both small and large constant batch sizes.

## 🔍 Abstract (한글 번역)

arXiv:2501.18164v4 발표 유형: 교체  
초록: 우리는 리만 기하학적 확률적 경사 하강법(RSGD)의 수렴 행동을 이론적으로 분석하였으며, 증가하는 배치 크기를 사용하는 것이 일정한 배치 크기를 사용하는 것보다 더 빠른 수렴을 가져온다는 것을 발견했습니다. 이는 일정한 학습률뿐만 아니라 코사인 감소 및 다항식 감소와 같은 감소하는 학습률에서도 마찬가지입니다. 수렴 속도는 일정한 배치 크기의 경우 $O(T^{-1}+C)$에서 증가하는 배치 크기의 경우 $O(T^{-1})$로 개선되며, 여기서 $T$는 총 반복 횟수이고 $C$는 상수입니다. 주성분 분석과 저순위 행렬 완성을 사용하여, 증가하는 배치 크기가 확률적 일차 오라클(SFO) 복잡성으로 정량화된 계산 시간에 어떻게 영향을 미치는지를 이론적 및 수치적으로 조사했습니다. 증가하는 배치 크기는 RSGD의 SFO 복잡성을 줄이는 것으로 나타났습니다. 또한, 증가하는 배치 크기는 작은 및 큰 일정한 배치 크기의 장점을 모두 제공하는 것으로 나타났습니다.

## 📝 요약

이 논문은 리만 기하학적 확률적 경사 하강법(RSGD)의 수렴 행동을 이론적으로 분석하여, 증가하는 배치 크기를 사용할 경우 고정 배치 크기를 사용할 때보다 더 빠르게 수렴한다는 것을 발견했습니다. 이는 고정 학습률뿐만 아니라 코사인 감소 및 다항식 감소와 같은 감소 학습률에서도 마찬가지입니다. 수렴 속도는 고정 배치 크기에서 $O(T^{-1}+C)$에서 증가하는 배치 크기에서 $O(T^{-1})$로 개선됩니다. 또한 주성분 분석과 저랭크 행렬 완성을 통해 증가하는 배치 크기가 확률적 일차 오라클(SFO) 복잡성으로 측정된 계산 시간을 어떻게 줄이는지를 이론적 및 수치적으로 조사했습니다. 증가하는 배치 크기는 RSGD의 SFO 복잡성을 줄이며, 작은 고정 배치 크기와 큰 고정 배치 크기의 장점을 모두 제공하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 리만 기하학적 확률적 경사 하강법(RSGD)의 수렴 속도는 증가하는 배치 크기를 사용할 때 더 빠르다.
- 2. 증가하는 배치 크기는 일정한 학습률뿐만 아니라 코사인 감쇠 및 다항식 감쇠와 같은 감쇠 학습률에서도 수렴 속도를 향상시킨다.
- 3. 증가하는 배치 크기는 RSGD의 확률적 일차 오라클(SFO) 복잡성을 감소시킨다.
- 4. 증가하는 배치 크기는 작은 배치 크기와 큰 배치 크기의 장점을 모두 제공한다.


---

*Generated on 2025-09-23 11:03:43*