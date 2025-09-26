---
keywords:
  - Neural Network
  - Partial Differential Equations
  - Point Adaptive Collocation Method for Artificial Neural Networks
  - Collocation Points
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2411.19632
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:58:01.932877",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Partial Differential Equations",
    "Point Adaptive Collocation Method for Artificial Neural Networks",
    "Collocation Points"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Partial Differential Equations": 0.78,
    "Point Adaptive Collocation Method for Artificial Neural Networks": 0.72,
    "Collocation Points": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Physics-Informed Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "PINNs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader category of neural networks, facilitating links to related machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Partial Differential Equations",
        "canonical": "Partial Differential Equations",
        "aliases": [
          "PDEs"
        ],
        "category": "specific_connectable",
        "rationale": "Key mathematical concept that connects to various computational and applied mathematics topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "PACMANN",
        "canonical": "Point Adaptive Collocation Method for Artificial Neural Networks",
        "aliases": [
          "PACMANN"
        ],
        "category": "unique_technical",
        "rationale": "A novel method introduced in the paper, relevant for linking to adaptive methods in neural networks.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.72
      },
      {
        "surface": "collocation points",
        "canonical": "Collocation Points",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's methodology, linking to numerical methods for solving differential equations.",
        "novelty_score": 0.48,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
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
      "candidate_surface": "Physics-Informed Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Partial Differential Equations",
      "resolved_canonical": "Partial Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "PACMANN",
      "resolved_canonical": "Point Adaptive Collocation Method for Artificial Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "collocation points",
      "resolved_canonical": "Collocation Points",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PACMANN: Point Adaptive Collocation Method for Artificial Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.19632.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2411.19632](https://arxiv.org/abs/2411.19632)

## 🔗 유사한 논문
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (85.7% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (85.6% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (84.3% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (83.5% similar)
- [[2025-09-19/Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Partial Differential Equations|Partial Differential Equations]], [[keywords/Collocation Points|Collocation Points]]
**⚡ Unique Technical**: [[keywords/Point Adaptive Collocation Method for Artificial Neural Networks|Point Adaptive Collocation Method for Artificial Neural Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.19632v2 Announce Type: replace-cross 
Abstract: Physics-Informed Neural Networks (PINNs) have emerged as a tool for approximating the solution of Partial Differential Equations (PDEs) in both forward and inverse problems. PINNs minimize a loss function which includes the PDE residual determined for a set of collocation points. Previous work has shown that the number and distribution of these collocation points have a significant influence on the accuracy of the PINN solution. Therefore, the effective placement of these collocation points is an active area of research. Specifically, available adaptive collocation point sampling methods have been reported to scale poorly in terms of computational cost when applied to high-dimensional problems. In this work, we address this issue and present the Point Adaptive Collocation Method for Artificial Neural Networks (PACMANN). PACMANN incrementally moves collocation points toward regions of higher residuals using gradient-based optimization algorithms guided by the gradient of the PINN loss function, that is, the squared PDE residual. We apply PACMANN for forward and inverse problems, and demonstrate that this method matches the performance of state-of-the-art methods in terms of the accuracy/efficiency tradeoff for the low-dimensional problems, while outperforming available approaches for high-dimensional problems. Key features of the method include its low computational cost and simplicity of integration into existing physics-informed neural network pipelines. The code is available at https://github.com/CoenVisser/PACMANN.

## 📝 요약

이 논문은 부분 미분 방정식(PDE)의 해를 근사하는 데 사용되는 물리 정보 신경망(PINN)의 효율성을 높이기 위한 새로운 방법인 PACMANN(Point Adaptive Collocation Method for Artificial Neural Networks)을 제안합니다. 기존의 적응형 배치점 샘플링 방법은 고차원 문제에서 계산 비용이 높다는 단점이 있었으나, PACMANN은 PINN 손실 함수의 그래디언트를 활용하여 배치점을 잔차가 큰 영역으로 점진적으로 이동시킴으로써 이 문제를 해결합니다. 이 방법은 저차원 문제에서 기존 최첨단 방법과 비슷한 성능을 보이며, 고차원 문제에서는 더 나은 성능을 발휘합니다. PACMANN은 낮은 계산 비용과 기존 PINN 파이프라인에 쉽게 통합할 수 있는 장점을 가지고 있습니다. 코드는 [GitHub 링크](https://github.com/CoenVisser/PACMANN)에서 제공됩니다.

## 🎯 주요 포인트

- 1. 물리 정보 신경망(PINNs)은 편미분 방정식(PDEs)의 해를 근사하는 도구로 사용됩니다.
- 2. PINNs의 정확도는 collocation 포인트의 수와 분포에 크게 영향을 받습니다.
- 3. PACMANN은 collocation 포인트를 잔차가 큰 영역으로 이동시키는 방법으로, 고차원 문제에서 기존 방법보다 우수한 성능을 보입니다.
- 4. PACMANN은 낮은 계산 비용과 기존 물리 정보 신경망 파이프라인에 쉽게 통합될 수 있는 장점을 가지고 있습니다.
- 5. PACMANN의 코드는 GitHub에서 제공됩니다.


---

*Generated on 2025-09-24 02:58:01*