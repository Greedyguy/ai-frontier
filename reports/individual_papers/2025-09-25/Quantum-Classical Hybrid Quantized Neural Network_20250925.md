---
keywords:
  - Neural Network
  - Quadratic Binary Optimization
  - Forward Interval Propagation
  - Quantum Conditional Gradient Descent
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2506.18240
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:28:42.534507",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Quadratic Binary Optimization",
    "Forward Interval Propagation",
    "Quantum Conditional Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Quadratic Binary Optimization": 0.78,
    "Forward Interval Propagation": 0.82,
    "Quantum Conditional Gradient Descent": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "quantized neural network",
        "canonical": "Neural Network",
        "aliases": [
          "QNN",
          "quantized NN"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing neural network literature and concepts, facilitating integration with broader AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Quadratic Binary Optimization",
        "canonical": "Quadratic Binary Optimization",
        "aliases": [
          "QBO"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a specific optimization model unique to this research, relevant for quantum computing applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Forward Interval Propagation",
        "canonical": "Forward Interval Propagation",
        "aliases": [
          "FIP"
        ],
        "category": "unique_technical",
        "rationale": "A novel method for handling non-linearity in neural networks, enhancing the paper's unique contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Quantum Conditional Gradient Descent",
        "canonical": "Quantum Conditional Gradient Descent",
        "aliases": [
          "QCGD"
        ],
        "category": "unique_technical",
        "rationale": "A specific algorithm leveraging quantum computing, crucial for linking quantum and classical optimization techniques.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "spline interpolation",
      "penalty method",
      "empirical risk minimization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "quantized neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Quadratic Binary Optimization",
      "resolved_canonical": "Quadratic Binary Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Forward Interval Propagation",
      "resolved_canonical": "Forward Interval Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Quantum Conditional Gradient Descent",
      "resolved_canonical": "Quantum Conditional Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Quantum-Classical Hybrid Quantized Neural Network

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.18240.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2506.18240](https://arxiv.org/abs/2506.18240)

## 🔗 유사한 논문
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (85.2% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (84.8% similar)
- [[2025-09-24/Re-uploading quantum data_ A universal function approximator for quantum inputs_20250924|Re-uploading quantum data: A universal function approximator for quantum inputs]] (84.4% similar)
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (84.3% similar)
- [[2025-09-22/Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits_20250922|Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Quadratic Binary Optimization|Quadratic Binary Optimization]], [[keywords/Forward Interval Propagation|Forward Interval Propagation]], [[keywords/Quantum Conditional Gradient Descent|Quantum Conditional Gradient Descent]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.18240v3 Announce Type: replace-cross 
Abstract: Here in this work, we present a novel Quadratic Binary Optimization (QBO) model for quantized neural network training, enabling the use of arbitrary activation and loss functions through spline interpolation. We introduce Forward Interval Propagation (FIP), a method designed to tackle the challenges of non-linearity and the multi-layer composite structure in neural networks by discretizing activation functions into linear subintervals. This approach preserves the universal approximation properties of neural networks while allowing complex nonlinear functions to be optimized using quantum computers, thus broadening their applicability in artificial intelligence. We provide theoretical upper bounds on the approximation error and the number of Ising spins required, by deriving the sample complexity of the empirical risk minimization problem, from an optimization perspective. A significant challenge in solving the associated Quadratic Constrained Binary Optimization (QCBO) model on a large scale is the presence of numerous constraints. When employing the penalty method to handle these constraints, tuning a large number of penalty coefficients becomes a critical hyperparameter optimization problem, increasing computational complexity and potentially affecting solution quality. To address this, we employ the Quantum Conditional Gradient Descent (QCGD) algorithm, which leverages quantum computing to directly solve the QCBO problem. We prove the convergence of QCGD under a quantum oracle with randomness and bounded variance in objective value, as well as under limited precision constraints in the coefficient matrix. Additionally, we provide an upper bound on the Time-To-Solution for the QCBO solving process. We further propose a training algorithm with single-sample bit-scale optimization.

## 📝 요약

이 논문은 양자화된 신경망 훈련을 위한 새로운 이차 이진 최적화(QBO) 모델을 제안합니다. 이 모델은 스플라인 보간법을 통해 임의의 활성화 및 손실 함수를 사용할 수 있게 하며, 비선형성과 다층 구조의 문제를 해결하기 위해 활성화 함수를 선형 구간으로 분할하는 전방 구간 전파(FIP) 방법을 도입합니다. 이를 통해 신경망의 보편적 근사 특성을 유지하면서 양자 컴퓨터를 사용해 복잡한 비선형 함수를 최적화할 수 있습니다. 또한, 경험적 위험 최소화 문제의 샘플 복잡성을 도출하여 근사 오차와 필요한 이징 스핀 수에 대한 이론적 상한을 제공합니다. QCBO 모델의 대규모 문제 해결 시 많은 제약 조건이 존재하는데, 이를 해결하기 위해 양자 조건부 경사 하강(QCGD) 알고리즘을 사용하여 직접 QCBO 문제를 해결합니다. QCGD의 수렴성을 증명하고, QCBO 해결 과정의 시간 상한을 제시합니다. 추가로 단일 샘플 비트 스케일 최적화를 통한 훈련 알고리즘을 제안합니다.

## 🎯 주요 포인트

- 1. 본 연구는 스플라인 보간법을 통해 임의의 활성화 및 손실 함수를 사용할 수 있는 새로운 이진 2차 최적화(QBO) 모델을 제안합니다.
- 2. 비선형성과 다층 구조의 문제를 해결하기 위해 활성화 함수를 선형 구간으로 이산화하는 전방 간격 전파(FIP) 방법을 도입했습니다.
- 3. 양자 컴퓨팅을 활용하여 복잡한 비선형 함수를 최적화함으로써 인공지능에서의 적용 가능성을 확장합니다.
- 4. 페널티 방법을 사용할 때 많은 페널티 계수를 조정하는 것이 중요한 하이퍼파라미터 최적화 문제가 되어 계산 복잡성을 증가시킵니다.
- 5. 양자 조건부 경사 하강(QCGD) 알고리즘을 사용하여 QCBO 문제를 직접 해결하고, 수렴성과 시간-해결 상한을 증명했습니다.


---

*Generated on 2025-09-25 16:28:42*