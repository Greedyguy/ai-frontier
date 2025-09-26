<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:28:53.388358",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Probabilistic Finite Automata",
    "Symbolic Neural Networks",
    "Matrix-Vector Multiplication",
    "Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Probabilistic Finite Automata": 0.78,
    "Symbolic Neural Networks": 0.79,
    "Matrix-Vector Multiplication": 0.65,
    "Gradient Descent": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "probabilistic finite automata",
        "canonical": "Probabilistic Finite Automata",
        "aliases": [
          "PFA",
          "probabilistic automata"
        ],
        "category": "unique_technical",
        "rationale": "Probabilistic finite automata are central to the paper's contributions and provide a unique link between symbolic computation and neural networks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "symbolic feedforward neural networks",
        "canonical": "Symbolic Neural Networks",
        "aliases": [
          "symbolic feedforward networks"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach to simulating PFAs, bridging symbolic computation and neural networks.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "matrix-vector products",
        "canonical": "Matrix-Vector Multiplication",
        "aliases": [
          "matrix-vector products"
        ],
        "category": "broad_technical",
        "rationale": "Matrix-vector multiplication is a fundamental operation in the proposed neural network architecture for simulating PFAs.",
        "novelty_score": 0.45,
        "connectivity_score": 0.6,
        "specificity_score": 0.5,
        "link_intent_score": 0.65
      },
      {
        "surface": "gradient descent-based optimization",
        "canonical": "Gradient Descent",
        "aliases": [
          "gradient descent optimization"
        ],
        "category": "broad_technical",
        "rationale": "Gradient descent is a key method for training the symbolic neural networks to simulate PFAs.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.55,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "state distributions",
      "stochastic matrices",
      "soft updates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "probabilistic finite automata",
      "resolved_canonical": "Probabilistic Finite Automata",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "symbolic feedforward neural networks",
      "resolved_canonical": "Symbolic Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "matrix-vector products",
      "resolved_canonical": "Matrix-Vector Multiplication",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.6,
        "specificity": 0.5,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "gradient descent-based optimization",
      "resolved_canonical": "Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.55,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Symbolic Feedforward Networks for Probabilistic Finite Automata: Exact Simulation and Learnability

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10034.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.10034](https://arxiv.org/abs/2509.10034)

## 🔗 유사한 논문
- [[2025-09-24/Learning From Simulators_ A Theory of Simulation-Grounded Learning_20250924|Learning From Simulators: A Theory of Simulation-Grounded Learning]] (81.4% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (79.8% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (79.5% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (79.5% similar)
- [[2025-09-24/Fully Learnable Neural Reward Machines_20250924|Fully Learnable Neural Reward Machines]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Matrix-Vector Multiplication|Matrix-Vector Multiplication]], [[keywords/Gradient Descent|Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Probabilistic Finite Automata|Probabilistic Finite Automata]], [[keywords/Symbolic Neural Networks|Symbolic Neural Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10034v2 Announce Type: replace 
Abstract: We present a formal and constructive theory showing that probabilistic finite automata (PFAs) can be exactly simulated using symbolic feedforward neural networks. Our architecture represents state distributions as vectors and transitions as stochastic matrices, enabling probabilistic state propagation via matrix-vector products. This yields a parallel, interpretable, and differentiable simulation of PFA dynamics using soft updates-without recurrence. We formally characterize probabilistic subset construction, $\varepsilon$-closure, and exact simulation via layered symbolic computation, and prove equivalence between PFAs and specific classes of neural networks. We further show that these symbolic simulators are not only expressive but learnable: trained with standard gradient descent-based optimization on labeled sequence data, they recover the exact behavior of ground-truth PFAs. This learnability, formalized in Proposition 5.1, is the crux of this work. Our results unify probabilistic automata theory with neural architectures under a rigorous algebraic framework, bridging the gap between symbolic computation and deep learning.

## 📝 요약

이 논문은 확률적 유한 오토마타(PFA)를 상징적 피드포워드 신경망을 통해 정확히 모사할 수 있는 이론을 제시합니다. 상태 분포를 벡터로, 전이를 확률 행렬로 표현하여 행렬-벡터 곱을 통해 확률적 상태 전이를 구현합니다. 이 방법은 순환 없이 PFA의 동작을 병렬적이고 해석 가능하며 미분 가능한 방식으로 시뮬레이션합니다. 논문은 확률적 부분집합 구성, $\varepsilon$-폐포, 정확한 시뮬레이션을 계층적 상징 계산으로 특징짓고, PFA와 특정 신경망 클래스 간의 동등성을 증명합니다. 또한, 이러한 상징적 시뮬레이터가 학습 가능하며, 표준 경사 하강법을 통해 라벨이 있는 시퀀스 데이터를 학습하여 실제 PFA의 동작을 정확히 복원할 수 있음을 보여줍니다. 이 학습 가능성은 본 연구의 핵심 기여로, 확률적 오토마타 이론과 신경망 구조를 엄격한 대수적 틀 안에서 통합하여 상징 계산과 딥러닝 간의 격차를 해소합니다.

## 🎯 주요 포인트

- 1. 확률적 유한 오토마타(PFAs)를 기호적 피드포워드 신경망을 통해 정확히 시뮬레이션할 수 있는 이론을 제시합니다.
- 2. 상태 분포를 벡터로, 전이를 확률적 행렬로 표현하여 행렬-벡터 곱을 통해 확률적 상태 전파를 가능하게 합니다.
- 3. PFAs와 특정 신경망 클래스 간의 동등성을 증명하며, 이 기호적 시뮬레이터가 학습 가능함을 보여줍니다.
- 4. 표준 경사하강법 기반 최적화를 통해 레이블된 시퀀스 데이터를 학습하여, 실제 PFAs의 정확한 동작을 복원할 수 있습니다.
- 5. 본 연구는 확률적 오토마타 이론과 신경망 구조를 엄격한 대수적 프레임워크 하에 통합합니다.


---

*Generated on 2025-09-24 15:28:53*