---
keywords:
  - Neural Controlled Differential Equations
  - Neural Ordinary Differential Equations
  - Negative Feedback Mechanism
  - Gaussian Process
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2408.08055
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:15:42.364617",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Controlled Differential Equations",
    "Neural Ordinary Differential Equations",
    "Negative Feedback Mechanism",
    "Gaussian Process"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Controlled Differential Equations": 0.78,
    "Neural Ordinary Differential Equations": 0.82,
    "Negative Feedback Mechanism": 0.75,
    "Gaussian Process": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural CDEs",
        "canonical": "Neural Controlled Differential Equations",
        "aliases": [
          "Neural CDE"
        ],
        "category": "unique_technical",
        "rationale": "Neural CDEs are a specific type of neural network architecture for time series, offering a unique approach to modeling temporal data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural ODE",
        "canonical": "Neural Ordinary Differential Equations",
        "aliases": [
          "Neural ODEs"
        ],
        "category": "specific_connectable",
        "rationale": "Neural ODEs are a foundational concept in continuous-time modeling, linking to a broad range of neural network research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Negative Feedback",
        "canonical": "Negative Feedback Mechanism",
        "aliases": [
          "Negative Feedback"
        ],
        "category": "unique_technical",
        "rationale": "Negative feedback is crucial for stabilizing the dynamics in neural models, providing a unique technical approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gaussian process theory",
        "canonical": "Gaussian Process",
        "aliases": [
          "Gaussian process theory"
        ],
        "category": "broad_technical",
        "rationale": "Gaussian processes are widely used in machine learning for probabilistic modeling, offering strong links to statistical methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "function evaluations",
      "integration time horizon",
      "solver error tolerance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural CDEs",
      "resolved_canonical": "Neural Controlled Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural ODE",
      "resolved_canonical": "Neural Ordinary Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Negative Feedback",
      "resolved_canonical": "Negative Feedback Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gaussian process theory",
      "resolved_canonical": "Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DeNOTS: Stable Deep Neural ODEs for Time Series

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2408.08055.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2408.08055](https://arxiv.org/abs/2408.08055)

## 🔗 유사한 논문
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (87.5% similar)
- [[2025-09-23/Efficient Neural SDE Training using Wiener-Space Cubature_20250923|Efficient Neural SDE Training using Wiener-Space Cubature]] (83.1% similar)
- [[2025-09-24/MeshODENet_ A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems_20250924|MeshODENet: A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems]] (82.7% similar)
- [[2025-09-23/Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs_20250923|Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs]] (82.6% similar)
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gaussian Process|Gaussian Process]]
**🔗 Specific Connectable**: [[keywords/Neural Ordinary Differential Equations|Neural Ordinary Differential Equations]]
**⚡ Unique Technical**: [[keywords/Neural Controlled Differential Equations|Neural Controlled Differential Equations]], [[keywords/Negative Feedback Mechanism|Negative Feedback Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.08055v4 Announce Type: replace-cross 
Abstract: Neural CDEs provide a natural way to process the temporal evolution of irregular time series. The number of function evaluations (NFE) is these systems' natural analog of depth (the number of layers in traditional neural networks). It is usually regulated via solver error tolerance: lower tolerance means higher numerical precision, requiring more integration steps. However, lowering tolerances does not adequately increase the models' expressiveness. We propose a simple yet effective alternative: scaling the integration time horizon to increase NFEs and "deepen`` the model. Increasing the integration interval causes uncontrollable growth in conventional vector fields, so we also propose a way to stabilize the dynamics via Negative Feedback (NF). It ensures provable stability without constraining flexibility. It also implies robustness: we provide theoretical bounds for Neural ODE risk using Gaussian process theory. Experiments on four open datasets demonstrate that our method, DeNOTS, outperforms existing approaches~ -- ~including recent Neural RDEs and state space models,~ -- ~achieving up to $20\%$ improvement in metrics. DeNOTS combines expressiveness, stability, and robustness, enabling reliable modelling in continuous-time domains.

## 📝 요약

이 논문은 불규칙한 시계열 데이터를 처리하는 신경 미분 방정식(CDE)의 모델 표현력을 향상시키기 위한 새로운 방법을 제안합니다. 기존 방법은 오차 허용치를 낮춰 수치적 정밀도를 높였으나, 이는 모델의 표현력을 충분히 증가시키지 못했습니다. 저자들은 통합 시간 범위를 확장하여 함수 평가 수(NFE)를 늘리고 모델의 '깊이'를 증가시키는 방법을 제안합니다. 또한, 부정적 피드백(NF)을 통해 다이나믹스를 안정화하여 안정성을 보장하면서도 유연성을 유지합니다. 이 방법은 Gaussian 프로세스 이론을 통해 신경 ODE의 위험에 대한 이론적 경계를 제공하며, 네 개의 공개 데이터셋 실험에서 기존 방법보다 최대 20% 성능 향상을 보였습니다. DeNOTS는 표현력, 안정성, 견고성을 결합하여 연속 시간 영역에서 신뢰할 수 있는 모델링을 가능하게 합니다.

## 🎯 주요 포인트

- 1. Neural CDEs는 불규칙한 시계열의 시간적 진화를 처리하는 자연스러운 방법을 제공한다.
- 2. 기존의 오차 허용치를 낮추는 방식은 모델의 표현력을 충분히 증가시키지 못한다.
- 3. 통합 시간 범위를 확장하여 NFE를 증가시키고 모델을 "심화"시키는 방법을 제안한다.
- 4. Negative Feedback(NF)을 통해 통합 간격 증가로 인한 벡터 필드의 불안정성을 안정화한다.
- 5. 제안된 방법 DeNOTS는 기존 방법들보다 최대 20% 성능 향상을 보이며, 연속 시간 도메인에서 신뢰할 수 있는 모델링을 가능하게 한다.


---

*Generated on 2025-09-25 16:15:42*