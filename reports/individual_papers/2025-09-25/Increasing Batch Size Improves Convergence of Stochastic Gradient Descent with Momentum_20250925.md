---
keywords:
  - Stochastic Gradient Descent with Momentum
  - Neural Network
  - Mini-batch Stochastic Gradient Descent with Momentum
  - Increasing Batch Size
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2501.08883
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:05:40.699219",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Gradient Descent with Momentum",
    "Neural Network",
    "Mini-batch Stochastic Gradient Descent with Momentum",
    "Increasing Batch Size"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Gradient Descent with Momentum": 0.85,
    "Neural Network": 0.8,
    "Mini-batch Stochastic Gradient Descent with Momentum": 0.8,
    "Increasing Batch Size": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Stochastic Gradient Descent with Momentum",
        "canonical": "Stochastic Gradient Descent with Momentum",
        "aliases": [
          "SGDM"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific optimization technique crucial for training neural networks, enhancing connectivity to related optimization methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Deep Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are foundational to deep learning, linking to a wide range of machine learning topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mini-batch SGDM",
        "canonical": "Mini-batch Stochastic Gradient Descent with Momentum",
        "aliases": [
          "Mini-batch SGDM"
        ],
        "category": "unique_technical",
        "rationale": "This variant of SGDM is specifically used in the context of deep learning, providing a focused link to training methodologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Increasing Batch Size",
        "canonical": "Increasing Batch Size",
        "aliases": [
          "Variable Batch Size"
        ],
        "category": "unique_technical",
        "rationale": "This technique is highlighted for its impact on convergence, linking to optimization strategies in machine learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Stochastic Gradient Descent with Momentum",
      "resolved_canonical": "Stochastic Gradient Descent with Momentum",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Deep Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mini-batch SGDM",
      "resolved_canonical": "Mini-batch Stochastic Gradient Descent with Momentum",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Increasing Batch Size",
      "resolved_canonical": "Increasing Batch Size",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Increasing Batch Size Improves Convergence of Stochastic Gradient Descent with Momentum

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.08883.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2501.08883](https://arxiv.org/abs/2501.08883)

## 🔗 유사한 논문
- [[2025-09-22/Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size_20250922|Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size]] (91.1% similar)
- [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (87.8% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (85.8% similar)
- [[2025-09-22/Generalization and Optimization of SGD with Lookahead_20250922|Generalization and Optimization of SGD with Lookahead]] (82.4% similar)
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Stochastic Gradient Descent with Momentum|Stochastic Gradient Descent with Momentum]], [[keywords/Mini-batch Stochastic Gradient Descent with Momentum|Mini-batch Stochastic Gradient Descent with Momentum]], [[keywords/Increasing Batch Size|Increasing Batch Size]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.08883v2 Announce Type: replace 
Abstract: Stochastic gradient descent with momentum (SGDM), in which a momentum term is added to SGD, has been well studied in both theory and practice. The theoretical studies show that the settings of the learning rate and momentum weight affect the convergence of SGDM. Meanwhile, the practical studies have shown that the batch-size setting strongly affects the performance of SGDM. In this paper, we focus on mini-batch SGDM with a constant learning rate and constant momentum weight, which is frequently used to train deep neural networks. We show theoretically that using a constant batch size does not always minimize the expectation of the full gradient norm of the empirical loss in training a deep neural network, whereas using an increasing batch size definitely minimizes it; that is, an increasing batch size improves the convergence of mini-batch SGDM. We also provide numerical results supporting our analyses, indicating specifically that mini-batch SGDM with an increasing batch size converges to stationary points faster than with a constant batch size, while also reducing computational cost. Python implementations of the optimizers used in the numerical experiments are available at https://github.com/iiduka-researches/NSHB_increasing_batchsize_acml25/.

## 📝 요약

이 논문은 모멘텀을 포함한 확률적 경사 하강법(SGDM)의 성능에 대한 연구로, 특히 미니배치 SGDM에서 일정한 학습률과 모멘텀 가중치를 사용할 때의 효과를 분석합니다. 이 연구는 증가하는 배치 크기가 일정한 배치 크기보다 경험적 손실의 전체 그래디언트 노름을 최소화하는 데 더 효과적임을 이론적으로 증명합니다. 즉, 증가하는 배치 크기는 미니배치 SGDM의 수렴성을 향상시킵니다. 수치 실험 결과, 증가하는 배치 크기를 사용한 경우가 일정한 배치 크기를 사용한 경우보다 더 빠르게 수렴하며 계산 비용도 절감됨을 보여줍니다. 관련 최적화 기법의 파이썬 구현은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 모멘텀을 포함한 확률적 경사 하강법(SGDM)은 학습률과 모멘텀 가중치 설정이 수렴에 영향을 미친다.
- 2. 실험적으로 배치 크기 설정이 SGDM의 성능에 강한 영향을 준다.
- 3. 일정한 배치 크기보다 증가하는 배치 크기를 사용할 때 미니배치 SGDM의 수렴이 개선된다.
- 4. 증가하는 배치 크기를 사용하는 미니배치 SGDM은 일정한 배치 크기를 사용할 때보다 계산 비용을 줄이면서 더 빠르게 수렴한다.
- 5. 연구 결과를 뒷받침하는 수치적 결과가 제공되며, 관련 최적화기의 파이썬 구현이 공개되어 있다.


---

*Generated on 2025-09-25 17:05:40*