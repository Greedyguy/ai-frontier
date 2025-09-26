---
keywords:
  - Partial Differential Equations
  - Random Feature Models
  - Physics-Informed Neural Networks
  - Kernel Methods
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2501.00288
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:59:26.648939",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Partial Differential Equations",
    "Random Feature Models",
    "Physics-Informed Neural Networks",
    "Kernel Methods"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Partial Differential Equations": 0.8,
    "Random Feature Models": 0.78,
    "Physics-Informed Neural Networks": 0.79,
    "Kernel Methods": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "partial differential equations",
        "canonical": "Partial Differential Equations",
        "aliases": [
          "PDEs"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, linking to mathematical modeling and simulation topics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "random feature models",
        "canonical": "Random Feature Models",
        "aliases": [
          "random feature method"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for solving PDEs, distinct from existing methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "physics-informed neural networks",
        "canonical": "Physics-Informed Neural Networks",
        "aliases": [
          "PINNs"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for connecting to other works using neural networks for solving PDEs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "kernel method",
        "canonical": "Kernel Methods",
        "aliases": [
          "kernel machines"
        ],
        "category": "broad_technical",
        "rationale": "Provides a foundational comparison for the proposed method.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "implementation",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "partial differential equations",
      "resolved_canonical": "Partial Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "random feature models",
      "resolved_canonical": "Random Feature Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "physics-informed neural networks",
      "resolved_canonical": "Physics-Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "kernel method",
      "resolved_canonical": "Kernel Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Solving Partial Differential Equations with Random Feature Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.00288.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2501.00288](https://arxiv.org/abs/2501.00288)

## 🔗 유사한 논문
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (84.0% similar)
- [[2025-09-23/PACMANN_ Point Adaptive Collocation Method for Artificial Neural Networks_20250923|PACMANN: Point Adaptive Collocation Method for Artificial Neural Networks]] (83.8% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (83.5% similar)
- [[2025-09-23/Data-Driven Discovery of PDEs via the Adjoint Method_20250923|Data-Driven Discovery of PDEs via the Adjoint Method]] (83.3% similar)
- [[2025-09-23/Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs_20250923|Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Kernel Methods|Kernel Methods]]
**🔗 Specific Connectable**: [[keywords/Physics-Informed Neural Networks|Physics-Informed Neural Networks]]
**⚡ Unique Technical**: [[keywords/Partial Differential Equations|Partial Differential Equations]], [[keywords/Random Feature Models|Random Feature Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.00288v2 Announce Type: replace-cross 
Abstract: Machine learning based partial differential equations (PDEs) solvers have received great attention in recent years. Most progress in this area has been driven by deep neural networks such as physics-informed neural networks (PINNs) and kernel method. In this paper, we introduce a random feature based framework toward efficiently solving PDEs. Random feature method was originally proposed to approximate large-scale kernel machines and can be viewed as a shallow neural network as well. We provide an error analysis for our proposed method along with comprehensive numerical results on several PDE benchmarks. In contrast to the state-of-the-art solvers that face challenges with a large number of collocation points, our proposed method reduces the computational complexity. Moreover, the implementation of our method is simple and does not require additional computational resources. Due to the theoretical guarantee and advantages in computation, our approach is proven to be efficient for solving PDEs.

## 📝 요약

이 논문은 기계 학습 기반의 편미분 방정식(PDE) 해법에 대한 연구로, 랜덤 피처 기반의 프레임워크를 제안합니다. 기존의 물리 정보 신경망(PINNs)과 커널 방법에 비해, 이 방법은 많은 수의 배치점에서 발생하는 계산 복잡성을 줄입니다. 또한, 구현이 간단하고 추가적인 계산 자원이 필요하지 않습니다. 제안된 방법의 오류 분석과 여러 PDE 벤치마크에 대한 수치 결과를 제공하며, 이론적 보장과 계산 효율성 측면에서 효과적임을 입증합니다.

## 🎯 주요 포인트

- 1. 최근 기계 학습 기반 편미분 방정식(PDE) 해법이 큰 주목을 받고 있다.
- 2. 본 논문에서는 랜덤 피처 기반 프레임워크를 도입하여 PDE를 효율적으로 해결하는 방법을 제안한다.
- 3. 제안된 방법은 많은 수의 배치점에서 발생하는 계산 복잡성을 줄인다.
- 4. 이 방법은 구현이 간단하며 추가적인 계산 자원을 필요로 하지 않는다.
- 5. 이론적 보장과 계산상의 장점으로 인해 제안된 접근법은 PDE 해결에 효율적임이 입증되었다.


---

*Generated on 2025-09-24 02:59:26*