<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:33:25.092221",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural ODE",
    "Universal Differential Equation",
    "Bullwhip Effect",
    "Stochastic Demand",
    "Inventory Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural ODE": 0.78,
    "Universal Differential Equation": 0.82,
    "Bullwhip Effect": 0.79,
    "Stochastic Demand": 0.75,
    "Inventory Dynamics": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural ODE",
        "canonical": "Neural ODE",
        "aliases": [
          "NODE"
        ],
        "category": "unique_technical",
        "rationale": "Neural ODEs are a specific type of neural network architecture relevant to continuous-time modeling, which is central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Universal Differential Equation",
        "canonical": "Universal Differential Equation",
        "aliases": [
          "UDE"
        ],
        "category": "unique_technical",
        "rationale": "UDEs are a novel approach combining differential equations with neural networks, crucial for the paper's exploration of inventory dynamics.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bullwhip Effect",
        "canonical": "Bullwhip Effect",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The bullwhip effect is a key concept in supply chain management, directly addressed in the paper's context of forecasting under stochastic demand.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Stochastic Demand",
        "canonical": "Stochastic Demand",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Stochastic demand is a central theme in the paper, affecting the dynamics and forecasting models discussed.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Inventory Dynamics",
        "canonical": "Inventory Dynamics",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Inventory dynamics are fundamental to the paper's exploration of continuous-time modeling and forecasting.",
        "novelty_score": 0.58,
        "connectivity_score": 0.67,
        "specificity_score": 0.76,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural ODE",
      "resolved_canonical": "Neural ODE",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Universal Differential Equation",
      "resolved_canonical": "Universal Differential Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bullwhip Effect",
      "resolved_canonical": "Bullwhip Effect",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Stochastic Demand",
      "resolved_canonical": "Stochastic Demand",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Inventory Dynamics",
      "resolved_canonical": "Inventory Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.67,
        "specificity": 0.76,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# BULL-ODE: Bullwhip Learning with Neural ODEs and Universal Differential Equations under Stochastic Demand

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18105.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18105](https://arxiv.org/abs/2509.18105)

## 🔗 유사한 논문
- [[2025-09-23/Efficient Neural SDE Training using Wiener-Space Cubature_20250923|Efficient Neural SDE Training using Wiener-Space Cubature]] (78.9% similar)
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (78.3% similar)
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (77.6% similar)
- [[2025-09-23/Controlling Neural Collapse Enhances Out-of-Distribution Detection and Transfer Learning_20250923|Controlling Neural Collapse Enhances Out-of-Distribution Detection and Transfer Learning]] (77.6% similar)
- [[2025-09-23/Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems_20250923|Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems]] (77.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Bullwhip Effect|Bullwhip Effect]], [[keywords/Stochastic Demand|Stochastic Demand]], [[keywords/Inventory Dynamics|Inventory Dynamics]]
**⚡ Unique Technical**: [[keywords/Neural ODE|Neural ODE]], [[keywords/Universal Differential Equation|Universal Differential Equation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18105v1 Announce Type: cross 
Abstract: We study learning of continuous-time inventory dynamics under stochastic demand and quantify when structure helps or hurts forecasting of the bullwhip effect. BULL-ODE compares a fully learned Neural ODE (NODE) that models the entire right-hand side against a physics-informed Universal Differential Equation (UDE) that preserves conservation and order-up-to structure while learning a small residual policy term. Classical supply chain models explain the bullwhip through control/forecasting choices and information sharing, while recent physics-informed and neural differential equation methods blend domain constraints with learned components. It is unclear whether structural bias helps or hinders forecasting under different demand regimes. We address this by using a single-echelon testbed with three demand regimes - AR(1) (autocorrelated), i.i.d. Gaussian, and heavy-tailed lognormal. Training is done on varying fractions of each trajectory, followed by evaluation of multi-step forecasts for inventory I, order rate O, and demand D. Across the structured regimes, UDE consistently generalizes better: with 90% of the training horizon, inventory RMSE drops from 4.92 (NODE) to 0.26 (UDE) under AR(1) and from 5.96 to 0.95 under Gaussian demand. Under heavy-tailed lognormal shocks, the flexibility of NODE is better. These trends persist as train18 ing data shrinks, with NODE exhibiting phase drift in extrapolation while UDE remains stable but underreacts to rare spikes. Our results provide concrete guidance: enforce structure when noise is light-tailed or temporally correlated; relax structure when extreme events dominate. Beyond inventory control, the results offer guidance for hybrid modeling in scientific and engineering systems: enforce known structure when conservation laws and modest noise dominate, and relax structure to capture extremes in settings where rare events drive dynamics.

## 📝 요약

이 논문은 확률적 수요 하에서 연속 시간 재고 동태를 학습하고, 구조가 황소채찍 효과 예측에 미치는 영향을 분석합니다. 연구는 Neural ODE(NODE)와 물리 정보를 반영한 Universal Differential Equation(UDE)을 비교합니다. NODE는 전체를 학습하지만, UDE는 보존 및 주문 구조를 유지하며 작은 잔여 정책만 학습합니다. 세 가지 수요 체제(AR(1), i.i.d. Gaussian, heavy-tailed lognormal)에서 실험한 결과, UDE는 구조화된 환경에서 일반화 성능이 뛰어났습니다. 특히, AR(1)과 Gaussian 수요 하에서 UDE의 재고 RMSE는 NODE보다 크게 낮았습니다. 반면, 극단적 사건이 지배적인 heavy-tailed lognormal 수요에서는 NODE의 유연성이 더 나았습니다. 연구는 소음이 가벼운 경우 구조를 유지하고, 극단적 사건이 지배적일 때는 구조를 완화할 것을 제안합니다. 이는 과학 및 공학 시스템에서의 하이브리드 모델링에도 유용한 지침을 제공합니다.

## 🎯 주요 포인트

- 1. BULL-ODE는 완전 학습된 Neural ODE와 물리 기반 Universal Differential Equation(UDE)을 비교하여 구조가 예측에 미치는 영향을 분석합니다.
- 2. UDE는 AR(1) 및 가우시안 수요 하에서 NODE보다 일관되게 더 나은 일반화 성능을 보이며, 재고 RMSE가 크게 감소합니다.
- 3. 중증도 로그정규 분포의 충격 하에서는 NODE의 유연성이 더 우수하여, NODE는 극단적인 이벤트를 더 잘 포착합니다.
- 4. 구조적 편향은 가벼운 꼬리 또는 시간적으로 상관된 노이즈 하에서 예측에 도움이 되지만, 극단적인 이벤트가 지배적인 경우에는 구조를 완화해야 합니다.
- 5. 연구 결과는 과학 및 공학 시스템의 하이브리드 모델링에 대한 지침을 제공하며, 보존 법칙이 지배적일 때는 구조를 적용하고, 극단적인 이벤트가 동력을 제공할 때는 구조를 완화해야 함을 시사합니다.


---

*Generated on 2025-09-24 13:33:25*