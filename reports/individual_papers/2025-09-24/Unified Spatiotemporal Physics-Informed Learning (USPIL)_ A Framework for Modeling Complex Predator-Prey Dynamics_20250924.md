<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:29:08.398195",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "USPIL",
    "Physics-Informed Neural Networks",
    "Lotka-Volterra System",
    "Conservation Laws"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "USPIL": 0.8,
    "Physics-Informed Neural Networks": 0.85,
    "Lotka-Volterra System": 0.78,
    "Conservation Laws": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Unified Spatiotemporal Physics-Informed Learning",
        "canonical": "USPIL",
        "aliases": [
          "Unified Spatiotemporal Physics-Informed Learning"
        ],
        "category": "unique_technical",
        "rationale": "USPIL is a novel framework integrating physics-informed neural networks for ecological modeling, offering unique insights into predator-prey dynamics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Physics-Informed Neural Networks",
        "canonical": "Physics-Informed Neural Networks",
        "aliases": [
          "PINNs"
        ],
        "category": "specific_connectable",
        "rationale": "PINNs are crucial for integrating physical laws into neural network models, enhancing the interpretability and accuracy of ecological simulations.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Lotka-Volterra system",
        "canonical": "Lotka-Volterra System",
        "aliases": [
          "Predator-Prey Model"
        ],
        "category": "specific_connectable",
        "rationale": "The Lotka-Volterra system is a foundational model in ecological dynamics, providing a basis for understanding predator-prey interactions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Conservation Laws",
        "canonical": "Conservation Laws",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Conservation laws are essential for ensuring that models adhere to fundamental physical principles, crucial for ecological accuracy.",
        "novelty_score": 0.45,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "temporal oscillations",
      "emergent patterns",
      "automatic differentiation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Unified Spatiotemporal Physics-Informed Learning",
      "resolved_canonical": "USPIL",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Physics-Informed Neural Networks",
      "resolved_canonical": "Physics-Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Lotka-Volterra system",
      "resolved_canonical": "Lotka-Volterra System",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Conservation Laws",
      "resolved_canonical": "Conservation Laws",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Unified Spatiotemporal Physics-Informed Learning (USPIL): A Framework for Modeling Complex Predator-Prey Dynamics

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13425.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.13425](https://arxiv.org/abs/2509.13425)

## 🔗 유사한 논문
- [[2025-09-24/Study Design and Demystification of Physics Informed Neural Networks for Power Flow Simulation_20250924|Study Design and Demystification of Physics Informed Neural Networks for Power Flow Simulation]] (84.8% similar)
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (83.1% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (81.8% similar)
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (81.4% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Conservation Laws|Conservation Laws]]
**🔗 Specific Connectable**: [[keywords/Physics-Informed Neural Networks|Physics-Informed Neural Networks]], [[keywords/Lotka-Volterra System|Lotka-Volterra System]]
**⚡ Unique Technical**: [[keywords/USPIL|USPIL]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13425v3 Announce Type: replace 
Abstract: Ecological systems exhibit complex multi-scale dynamics that challenge traditional modeling. New methods must capture temporal oscillations and emergent spatiotemporal patterns while adhering to conservation principles. We present the Unified Spatiotemporal Physics-Informed Learning (USPIL) framework, a deep learning architecture integrating physics-informed neural networks (PINNs) and conservation laws to model predator-prey dynamics across dimensional scales. The framework provides a unified solution for both ordinary (ODE) and partial (PDE) differential equation systems, describing temporal cycles and reaction-diffusion patterns within a single neural network architecture. Our methodology uses automatic differentiation to enforce physics constraints and adaptive loss weighting to balance data fidelity with physical consistency. Applied to the Lotka-Volterra system, USPIL achieves 98.9% correlation for 1D temporal dynamics (loss: 0.0219, MAE: 0.0184) and captures complex spiral waves in 2D systems (loss: 4.7656, pattern correlation: 0.94). Validation confirms conservation law adherence within 0.5% and shows a 10-50x computational speedup for inference compared to numerical solvers. USPIL also enables mechanistic understanding through interpretable physics constraints, facilitating parameter discovery and sensitivity analysis not possible with purely data-driven methods. Its ability to transition between dimensional formulations opens new avenues for multi-scale ecological modeling. These capabilities make USPIL a transformative tool for ecological forecasting, conservation planning, and understanding ecosystem resilience, establishing physics-informed deep learning as a powerful and scientifically rigorous paradigm.

## 📝 요약

이 논문은 복잡한 생태계의 다중 규모 동역학을 모델링하기 위해 새로운 방법론인 통합 시공간 물리 정보 학습(USPIL) 프레임워크를 제안합니다. 이 프레임워크는 물리 정보 신경망(PINNs)과 보존 법칙을 통합하여 포식자-피식자 동역학을 모델링하며, 상미분방정식(ODE)과 편미분방정식(PDE) 시스템을 하나의 신경망 구조로 설명합니다. Lotka-Volterra 시스템에 적용하여 1차원 시간 동역학에서 98.9%의 상관관계를 달성하고, 2차원 시스템에서 복잡한 나선형 파동을 포착합니다. 물리적 제약을 자동 미분으로 구현하고, 데이터 충실도와 물리적 일관성을 균형 있게 유지합니다. 이 방법론은 기존 수치 해석보다 10-50배 빠른 계산 속도를 제공하며, 해석 가능한 물리적 제약을 통해 매개변수 발견과 민감도 분석을 가능하게 합니다. USPIL은 생태계 예측, 보존 계획, 생태계 회복력 이해에 있어 혁신적인 도구로 자리매김하며, 물리 정보 딥러닝의 과학적 엄밀성을 입증합니다.

## 🎯 주요 포인트

- 1. USPIL 프레임워크는 물리 정보를 포함한 신경망과 보존 법칙을 통합하여 포식자-피식자 동역학을 다차원적으로 모델링합니다.
- 2. 이 프레임워크는 ODE와 PDE 시스템을 모두 설명하며, 자동 미분과 적응형 손실 가중치를 사용하여 물리적 제약을 강화합니다.
- 3. Lotka-Volterra 시스템에 적용된 USPIL은 1D 시간 동역학에서 98.9%의 상관관계를 달성하고, 2D 시스템에서 복잡한 나선형 파동을 포착합니다.
- 4. USPIL은 보존 법칙을 0.5% 이내로 준수하며, 수치 해석기보다 10-50배 빠른 추론 속도를 보여줍니다.
- 5. 물리적 제약을 통한 해석 가능성을 제공하여 매개변수 발견 및 민감도 분석을 가능하게 하며, 다차원 생태계 모델링에 새로운 가능성을 열어줍니다.


---

*Generated on 2025-09-24 15:29:08*