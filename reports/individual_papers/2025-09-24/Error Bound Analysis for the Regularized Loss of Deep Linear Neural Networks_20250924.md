<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:31:56.901728",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Regularization",
    "Error Bound Analysis",
    "Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Regularization": 0.82,
    "Error Bound Analysis": 0.79,
    "Gradient Descent": 0.87
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "deep linear networks",
        "canonical": "Deep Learning",
        "aliases": [
          "deep linear neural networks"
        ],
        "category": "broad_technical",
        "rationale": "Deep linear networks are a specific type of neural network architecture, closely related to the broader field of deep learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "regularized loss",
        "canonical": "Regularization",
        "aliases": [
          "regularized squared loss"
        ],
        "category": "specific_connectable",
        "rationale": "Regularization is a key concept in optimizing neural networks, providing a link to discussions on improving model generalization.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "error bound",
        "canonical": "Error Bound Analysis",
        "aliases": [
          "error bounds"
        ],
        "category": "unique_technical",
        "rationale": "Error bound analysis is crucial for understanding the convergence properties of optimization algorithms in neural networks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "gradient descent",
        "canonical": "Gradient Descent",
        "aliases": [
          "GD"
        ],
        "category": "specific_connectable",
        "rationale": "Gradient descent is a fundamental optimization method used in training neural networks, linking to broader optimization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.87
      }
    ],
    "ban_list_suggestions": [
      "optimization foundations",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "deep linear networks",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "regularized loss",
      "resolved_canonical": "Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "error bound",
      "resolved_canonical": "Error Bound Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "gradient descent",
      "resolved_canonical": "Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.87
      }
    }
  ]
}
-->

# Error Bound Analysis for the Regularized Loss of Deep Linear Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11152.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2502.11152](https://arxiv.org/abs/2502.11152)

## 🔗 유사한 논문
- [[2025-09-24/Diagonal Linear Networks and the Lasso Regularization Path_20250924|Diagonal Linear Networks and the Lasso Regularization Path]] (84.8% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (84.3% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (83.3% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.4% similar)
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Regularization|Regularization]], [[keywords/Gradient Descent|Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Error Bound Analysis|Error Bound Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11152v3 Announce Type: replace-cross 
Abstract: The optimization foundations of deep linear networks have recently received significant attention. However, due to their inherent non-convexity and hierarchical structure, analyzing the loss functions of deep linear networks remains a challenging task. In this work, we study the local geometric landscape of the regularized squared loss of deep linear networks around each critical point. Specifically, we derive a closed-form characterization of the critical point set and establish an error bound for the regularized loss under mild conditions on network width and regularization parameters. Notably, this error bound quantifies the distance from a point to the critical point set in terms of the current gradient norm, which can be used to derive linear convergence of first-order methods. To support our theoretical findings, we conduct numerical experiments and demonstrate that gradient descent converges linearly to a critical point when optimizing the regularized loss of deep linear networks.

## 📝 요약

이 논문은 심층 선형 네트워크의 최적화 기초를 연구하며, 특히 비볼록성과 계층 구조로 인해 손실 함수 분석이 어려운 문제를 다룹니다. 저자들은 심층 선형 네트워크의 정규화된 제곱 손실의 국소 기하학적 구조를 분석하고, 임계점 집합의 닫힌 형태를 도출했습니다. 또한, 네트워크의 폭과 정규화 매개변수에 대한 조건 하에서 정규화된 손실에 대한 오류 경계를 설정했습니다. 이 오류 경계는 현재의 그래디언트 노름을 기준으로 임계점 집합까지의 거리를 정량화하며, 이를 통해 1차 방법의 선형 수렴을 도출할 수 있습니다. 이론적 결과를 뒷받침하기 위해 수치 실험을 수행했으며, 그래디언트 하강법이 정규화된 손실을 최적화할 때 임계점으로 선형 수렴함을 보여주었습니다.

## 🎯 주요 포인트

- 1. 딥 선형 네트워크의 최적화 기초는 비선형성과 계층 구조로 인해 분석이 어렵습니다.
- 2. 본 연구에서는 딥 선형 네트워크의 정규화된 제곱 손실의 국소 기하학적 구조를 분석합니다.
- 3. 각 임계점 주변에서 임계점 집합의 닫힌 형태를 유도하고, 네트워크 폭과 정규화 매개변수에 대한 조건 하에 오차 경계를 확립합니다.
- 4. 오차 경계는 현재의 그래디언트 노름을 통해 임계점 집합과의 거리를 정량화하며, 이를 통해 1차 방법의 선형 수렴을 도출할 수 있습니다.
- 5. 수치 실험을 통해 그래디언트 디센트가 딥 선형 네트워크의 정규화된 손실을 최적화할 때 임계점으로 선형 수렴함을 입증합니다.


---

*Generated on 2025-09-24 15:31:56*