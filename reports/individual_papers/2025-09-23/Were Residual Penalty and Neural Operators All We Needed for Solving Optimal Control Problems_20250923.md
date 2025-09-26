---
keywords:
  - Neural Network
  - Optimal Control
  - Neural Operator
  - DeepONet
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.04742
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:05:20.158672",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Optimal Control",
    "Neural Operator",
    "DeepONet"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Optimal Control": 0.82,
    "Neural Operator": 0.79,
    "DeepONet": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the paper's methodology and connect to a wide range of related topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Optimal Control Problems",
        "canonical": "Optimal Control",
        "aliases": [
          "Optimal Control Tasks"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on solving optimal control problems, making it a key concept for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Neural Operator",
        "canonical": "Neural Operator",
        "aliases": [
          "Neural Operators"
        ],
        "category": "unique_technical",
        "rationale": "Neural operators are a novel approach discussed in the paper, relevant for linking to advanced computational techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "DeepONet",
        "canonical": "DeepONet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DeepONet is a specific neural operator architecture used in the study, important for technical specificity.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "training process",
      "cost function",
      "optimization routine"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Optimal Control Problems",
      "resolved_canonical": "Optimal Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Neural Operator",
      "resolved_canonical": "Neural Operator",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "DeepONet",
      "resolved_canonical": "DeepONet",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.04742.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.04742](https://arxiv.org/abs/2506.04742)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (83.0% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (81.8% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (81.6% similar)
- [[2025-09-22/Geometric Integration for Neural Control Variates_20250922|Geometric Integration for Neural Control Variates]] (81.6% similar)
- [[2025-09-22/Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems_20250922|Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Optimal Control|Optimal Control]]
**⚡ Unique Technical**: [[keywords/Neural Operator|Neural Operator]], [[keywords/DeepONet|DeepONet]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.04742v2 Announce Type: replace-cross 
Abstract: Neural networks have been used to solve optimal control problems, typically by training neural networks using a combined loss function that considers data, differential equation residuals, and objective costs. We show that including cost functions in the training process is unnecessary, advocating for a simpler architecture and streamlined approach by decoupling the optimal control problem from the training process. Thus, our work shows that a simple neural operator architecture, such as DeepONet, coupled with an unconstrained optimization routine, can solve multiple optimal control problems with a single physics-informed training phase and a subsequent optimization phase. We achieve this by adding a penalty term based on the differential equation residual to the cost function and computing gradients with respect to the control using automatic differentiation through the trained neural operator within an iterative optimization routine. Our results show acceptable accuracy for practical applications and potential computational savings for more complex and higher-dimensional problems.

## 📝 요약

이 논문에서는 최적 제어 문제를 해결하기 위해 신경망을 사용하는 기존 방법에서 비용 함수를 훈련 과정에 포함할 필요가 없음을 제안합니다. 대신, 최적 제어 문제를 훈련 과정에서 분리하여 간단한 신경 연산자 구조와 비제약 최적화 절차를 통해 문제를 해결할 수 있음을 보입니다. DeepONet과 같은 신경 연산자와 물리 정보를 활용한 훈련 단계를 통해 여러 최적 제어 문제를 해결할 수 있으며, 미분 방정식 잔차를 기반으로 한 페널티 항을 비용 함수에 추가하여 자동 미분을 통해 제어에 대한 기울기를 계산합니다. 이 방법은 실용적인 정확도를 제공하며, 복잡하고 고차원 문제에서의 계산 비용 절감 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 최적 제어 문제 해결에 있어 비용 함수를 훈련 과정에 포함시키는 것은 불필요하며, 단순한 신경망 구조와 접근법을 제안합니다.
- 2. DeepONet과 같은 단순한 신경 연산자 구조와 비제약 최적화 루틴을 결합하여 여러 최적 제어 문제를 해결할 수 있습니다.
- 3. 훈련된 신경 연산자를 통한 자동 미분을 사용하여 제어에 대한 그래디언트를 계산하고, 반복 최적화 루틴을 통해 최적화를 수행합니다.
- 4. 제안된 방법은 실질적인 응용에서 수용 가능한 정확도를 보이며, 복잡하고 고차원적인 문제에서의 계산 비용 절감을 기대할 수 있습니다.


---

*Generated on 2025-09-24 01:05:20*