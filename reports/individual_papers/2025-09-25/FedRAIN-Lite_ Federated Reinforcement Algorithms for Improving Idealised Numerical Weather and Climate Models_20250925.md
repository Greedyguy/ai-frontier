---
keywords:
  - Federated Reinforcement Learning
  - Deep Deterministic Policy Gradient
  - General Circulation Models
  - Energy-Balance Climate Models
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2508.14315
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:09:37.321646",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Reinforcement Learning",
    "Deep Deterministic Policy Gradient",
    "General Circulation Models",
    "Energy-Balance Climate Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Reinforcement Learning": 0.78,
    "Deep Deterministic Policy Gradient": 0.82,
    "General Circulation Models": 0.8,
    "Energy-Balance Climate Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Reinforcement Learning",
        "canonical": "Federated Reinforcement Learning",
        "aliases": [
          "FedRL"
        ],
        "category": "unique_technical",
        "rationale": "Federated Reinforcement Learning is a novel approach that combines federated learning with reinforcement learning, enhancing adaptability in climate models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Deterministic Policy Gradient",
        "canonical": "Deep Deterministic Policy Gradient",
        "aliases": [
          "DDPG"
        ],
        "category": "specific_connectable",
        "rationale": "DDPG is a well-known reinforcement learning algorithm that can be linked to other works on policy gradient methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.79,
        "link_intent_score": 0.82
      },
      {
        "surface": "General Circulation Models",
        "canonical": "General Circulation Models",
        "aliases": [
          "GCMs"
        ],
        "category": "broad_technical",
        "rationale": "General Circulation Models are fundamental in climate modeling and provide a basis for connecting various climate studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Energy-Balance Climate Models",
        "canonical": "Energy-Balance Climate Models",
        "aliases": [
          "EBCMs"
        ],
        "category": "unique_technical",
        "rationale": "Energy-Balance Climate Models are specific to climate studies and offer a unique perspective on model simplification.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "parameter learning",
      "offline tuning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Reinforcement Learning",
      "resolved_canonical": "Federated Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Deterministic Policy Gradient",
      "resolved_canonical": "Deep Deterministic Policy Gradient",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.79,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "General Circulation Models",
      "resolved_canonical": "General Circulation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Energy-Balance Climate Models",
      "resolved_canonical": "Energy-Balance Climate Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FedRAIN-Lite: Federated Reinforcement Algorithms for Improving Idealised Numerical Weather and Climate Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.14315.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2508.14315](https://arxiv.org/abs/2508.14315)

## 🔗 유사한 논문
- [[2025-09-25/BoreaRL_ A Multi-Objective Reinforcement Learning Environment for Climate-Adaptive Boreal Forest Management_20250925|BoreaRL: A Multi-Objective Reinforcement Learning Environment for Climate-Adaptive Boreal Forest Management]] (83.9% similar)
- [[2025-09-25/Surrogate Modeling of 3D Rayleigh-Benard Convection with Equivariant Autoencoders_20250925|Surrogate Modeling of 3D Rayleigh-Benard Convection with Equivariant Autoencoders]] (81.8% similar)
- [[2025-09-23/Are Deep Learning Methods Suitable for Downscaling Global Climate Projections? An Intercomparison for Temperature and Precipitation over Spain_20250923|Are Deep Learning Methods Suitable for Downscaling Global Climate Projections? An Intercomparison for Temperature and Precipitation over Spain]] (81.3% similar)
- [[2025-09-23/Synergies between Federated Foundation Models and Smart Power Grids_20250923|Synergies between Federated Foundation Models and Smart Power Grids]] (81.2% similar)
- [[2025-09-24/A Generative Framework for Probabilistic, Spatiotemporally Coherent Downscaling of Climate Simulation_20250924|A Generative Framework for Probabilistic, Spatiotemporally Coherent Downscaling of Climate Simulation]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/General Circulation Models|General Circulation Models]]
**🔗 Specific Connectable**: [[keywords/Deep Deterministic Policy Gradient|Deep Deterministic Policy Gradient]]
**⚡ Unique Technical**: [[keywords/Federated Reinforcement Learning|Federated Reinforcement Learning]], [[keywords/Energy-Balance Climate Models|Energy-Balance Climate Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.14315v2 Announce Type: replace 
Abstract: Sub-grid parameterisations in climate models are traditionally static and tuned offline, limiting adaptability to evolving states. This work introduces FedRAIN-Lite, a federated reinforcement learning (FedRL) framework that mirrors the spatial decomposition used in general circulation models (GCMs) by assigning agents to latitude bands, enabling local parameter learning with periodic global aggregation. Using a hierarchy of simplified energy-balance climate models, from a single-agent baseline (ebm-v1) to multi-agent ensemble (ebm-v2) and GCM-like (ebm-v3) setups, we benchmark three RL algorithms under different FedRL configurations. Results show that Deep Deterministic Policy Gradient (DDPG) consistently outperforms both static and single-agent baselines, with faster convergence and lower area-weighted RMSE in tropical and mid-latitude zones across both ebm-v2 and ebm-v3 setups. DDPG's ability to transfer across hyperparameters and low computational cost make it well-suited for geographically adaptive parameter learning. This capability offers a scalable pathway towards high-complexity GCMs and provides a prototype for physically aligned, online-learning climate models that can evolve with a changing climate. Code accessible at https://github.com/p3jitnath/climate-rl-fedrl.

## 📝 요약

이 연구는 기후 모델의 하위 격자 매개변수화를 개선하기 위해 FedRAIN-Lite라는 연합 강화 학습(FedRL) 프레임워크를 제안합니다. 이 프레임워크는 일반 순환 모델(GCM)의 공간 분해 방식을 모방하여 위도대에 에이전트를 할당하고, 지역 매개변수를 학습하며 주기적으로 전역 집계를 수행합니다. 연구에서는 단일 에이전트 기반 모델(ebm-v1)부터 다중 에이전트 앙상블(ebm-v2), GCM 유사 모델(ebm-v3)까지 다양한 설정에서 세 가지 강화 학습 알고리즘을 평가했습니다. 그 결과, Deep Deterministic Policy Gradient(DDPG) 알고리즘이 정적 및 단일 에이전트 기준 모델보다 빠른 수렴 속도와 낮은 면적 가중 RMSE를 보이며 우수한 성능을 나타냈습니다. DDPG는 지리적 적응 매개변수 학습에 적합하며, 복잡한 GCM으로의 확장 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. FedRAIN-Lite는 위도대에 에이전트를 할당하여 지역적 매개변수 학습을 가능하게 하고 주기적인 글로벌 집계를 통해 기후 모델의 적응성을 향상시킵니다.
- 2. Deep Deterministic Policy Gradient (DDPG) 알고리즘은 다양한 FedRL 설정에서 정적 및 단일 에이전트 기준을 능가하며, 열대 및 중위도 지역에서 빠른 수렴과 낮은 면적 가중 RMSE를 보여줍니다.
- 3. DDPG는 하이퍼파라미터 전이 능력과 낮은 계산 비용으로 지리적으로 적응적인 매개변수 학습에 적합합니다.
- 4. 이 연구는 고복잡도 일반 순환 모델(GCM)로의 확장 가능한 경로를 제공하며, 변화하는 기후에 적응할 수 있는 물리적으로 정렬된 온라인 학습 기후 모델의 프로토타입을 제시합니다.


---

*Generated on 2025-09-25 17:09:37*