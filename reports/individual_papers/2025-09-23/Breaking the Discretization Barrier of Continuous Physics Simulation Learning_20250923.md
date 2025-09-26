---
keywords:
  - Continuous Physics Simulation
  - Graph Neural Network
  - Message Passing
  - Markov-based Neural Auto-Correction
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17955
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:06:43.648955",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continuous Physics Simulation",
    "Graph Neural Network",
    "Message Passing",
    "Markov-based Neural Auto-Correction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continuous Physics Simulation": 0.88,
    "Graph Neural Network": 0.82,
    "Message Passing": 0.8,
    "Markov-based Neural Auto-Correction": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "continuous physics simulation",
        "canonical": "Continuous Physics Simulation",
        "aliases": [
          "CoPS"
        ],
        "category": "unique_technical",
        "rationale": "This term represents the core innovation of the paper, focusing on overcoming discretization in physics simulations.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "graph ODEs",
        "canonical": "Graph Neural Network",
        "aliases": [
          "graph ordinary differential equations"
        ],
        "category": "specific_connectable",
        "rationale": "Graph ODEs are a novel application of Graph Neural Networks, providing a strong link to existing research in continuous-time dynamics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "message-passing mechanism",
        "canonical": "Message Passing",
        "aliases": [
          "message passing"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism is crucial for feature mapping in the proposed method, linking to broader work on graph-based learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Markov-based neural auto-correction",
        "canonical": "Markov-based Neural Auto-Correction",
        "aliases": [
          "Markov neural correction"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique component of the proposed method, enhancing continuous extrapolation accuracy.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "continuous physics simulation",
      "resolved_canonical": "Continuous Physics Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "graph ODEs",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "message-passing mechanism",
      "resolved_canonical": "Message Passing",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Markov-based neural auto-correction",
      "resolved_canonical": "Markov-based Neural Auto-Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Breaking the Discretization Barrier of Continuous Physics Simulation Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17955.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17955](https://arxiv.org/abs/2509.17955)

## 🔗 유사한 논문
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (82.0% similar)
- [[2025-09-18/DeCoP_ Enhancing Self-Supervised Time Series Representation with Dependency Controlled Pre-training_20250918|DeCoP: Enhancing Self-Supervised Time Series Representation with Dependency Controlled Pre-training]] (81.9% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (81.8% similar)
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (81.0% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Message Passing|Message Passing]]
**⚡ Unique Technical**: [[keywords/Continuous Physics Simulation|Continuous Physics Simulation]], [[keywords/Markov-based Neural Auto-Correction|Markov-based Neural Auto-Correction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17955v1 Announce Type: new 
Abstract: The modeling of complicated time-evolving physical dynamics from partial observations is a long-standing challenge. Particularly, observations can be sparsely distributed in a seemingly random or unstructured manner, making it difficult to capture highly nonlinear features in a variety of scientific and engineering problems. However, existing data-driven approaches are often constrained by fixed spatial and temporal discretization. While some researchers attempt to achieve spatio-temporal continuity by designing novel strategies, they either overly rely on traditional numerical methods or fail to truly overcome the limitations imposed by discretization. To address these, we propose CoPS, a purely data-driven methods, to effectively model continuous physics simulation from partial observations. Specifically, we employ multiplicative filter network to fuse and encode spatial information with the corresponding observations. Then we customize geometric grids and use message-passing mechanism to map features from original spatial domain to the customized grids. Subsequently, CoPS models continuous-time dynamics by designing multi-scale graph ODEs, while introducing a Markov-based neural auto-correction module to assist and constrain the continuous extrapolations. Comprehensive experiments demonstrate that CoPS advances the state-of-the-art methods in space-time continuous modeling across various scenarios.

## 📝 요약

이 논문에서는 부분 관찰로부터 복잡한 시간 변화 물리 동역학을 모델링하는 문제를 다룹니다. 기존의 데이터 기반 접근법은 고정된 시공간 분할에 제한되지만, CoPS라는 순수 데이터 기반 방법을 제안하여 이를 극복하고자 합니다. CoPS는 곱셈 필터 네트워크를 사용해 공간 정보를 관찰값과 융합하고, 메시지 전달 메커니즘을 통해 원래의 공간 도메인에서 사용자 정의 격자로 특징을 매핑합니다. 또한, 다중 스케일 그래프 ODE를 설계하여 연속 시간 동역학을 모델링하고, 마르코프 기반 신경망 자동 수정 모듈을 도입하여 연속적 외삽을 보조하고 제약합니다. 실험 결과, CoPS는 다양한 시나리오에서 시공간 연속 모델링의 최신 방법들을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 복잡한 시간 변화 물리 역학을 부분 관측으로부터 모델링하는 것은 오랜 도전 과제입니다.
- 2. 기존 데이터 기반 접근법은 고정된 공간 및 시간 이산화에 의해 제한되는 경우가 많습니다.
- 3. CoPS는 순수 데이터 기반 방법으로, 부분 관측으로부터 연속적인 물리 시뮬레이션을 효과적으로 모델링합니다.
- 4. CoPS는 공간 정보를 관측치와 융합하기 위해 곱셈 필터 네트워크를 사용하고, 메시지 전달 메커니즘을 통해 원래 공간 도메인에서 사용자 정의 그리드로 특징을 매핑합니다.
- 5. CoPS는 다중 스케일 그래프 ODE를 설계하여 연속 시간 역학을 모델링하고, 마르코프 기반의 신경망 자동 보정 모듈을 도입하여 연속적인 외삽을 지원하고 제약합니다.


---

*Generated on 2025-09-24 05:06:43*