---
keywords:
  - Metriplectic Conditional Flow Matching
  - Dissipative Dynamics
  - Structure Preserving Sampler
  - Symplectic Update
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19526
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:37:06.911864",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Metriplectic Conditional Flow Matching",
    "Dissipative Dynamics",
    "Structure Preserving Sampler",
    "Symplectic Update"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Metriplectic Conditional Flow Matching": 0.78,
    "Dissipative Dynamics": 0.79,
    "Structure Preserving Sampler": 0.77,
    "Symplectic Update": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Metriplectic Conditional Flow Matching",
        "canonical": "Metriplectic Conditional Flow Matching",
        "aliases": [
          "MCFM"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method specifically introduced in the paper for learning dissipative dynamics, making it a unique technical term.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dissipative Dynamics",
        "canonical": "Dissipative Dynamics",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding dissipative dynamics is crucial for linking to studies on energy conservation and stability in dynamic systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Structure Preserving Sampler",
        "canonical": "Structure Preserving Sampler",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This component is essential for maintaining the conservative-dissipative split, a key innovation of the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Symplectic Update",
        "canonical": "Symplectic Update",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Symplectic updates are significant for ensuring energy conservation in numerical simulations, linking to broader computational physics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "neural surrogates",
      "short transitions",
      "trusted energy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Metriplectic Conditional Flow Matching",
      "resolved_canonical": "Metriplectic Conditional Flow Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dissipative Dynamics",
      "resolved_canonical": "Dissipative Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Structure Preserving Sampler",
      "resolved_canonical": "Structure Preserving Sampler",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Symplectic Update",
      "resolved_canonical": "Symplectic Update",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Metriplectic Conditional Flow Matching for Dissipative Dynamics

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19526.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19526](https://arxiv.org/abs/2509.19526)

## 🔗 유사한 논문
- [[2025-09-24/CAR-Flow_ Condition-Aware Reparameterization Aligns Source and Target for Better Flow Matching_20250924|CAR-Flow: Condition-Aware Reparameterization Aligns Source and Target for Better Flow Matching]] (81.9% similar)
- [[2025-09-24/Flow marching for a generative PDE foundation model_20250924|Flow marching for a generative PDE foundation model]] (81.6% similar)
- [[2025-09-23/Equilibrium flow_ From Snapshots to Dynamics_20250923|Equilibrium flow: From Snapshots to Dynamics]] (81.5% similar)
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (80.4% similar)
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive: Energy Flow Field for End-to-End Autonomous Driving]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Dissipative Dynamics|Dissipative Dynamics]], [[keywords/Symplectic Update|Symplectic Update]]
**⚡ Unique Technical**: [[keywords/Metriplectic Conditional Flow Matching|Metriplectic Conditional Flow Matching]], [[keywords/Structure Preserving Sampler|Structure Preserving Sampler]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19526v1 Announce Type: new 
Abstract: Metriplectic conditional flow matching (MCFM) learns dissipative dynamics without violating first principles. Neural surrogates often inject energy and destabilize long-horizon rollouts; MCFM instead builds the conservative-dissipative split into both the vector field and a structure preserving sampler. MCFM trains via conditional flow matching on short transitions, avoiding long rollout adjoints. In inference, a Strang-prox scheme alternates a symplectic update with a proximal metric step, ensuring discrete energy decay; an optional projection enforces strict decay when a trusted energy is available. We provide continuous and discrete time guarantees linking this parameterization and sampler to conservation, monotonic dissipation, and stable rollouts. On a controlled mechanical benchmark, MCFM yields phase portraits closer to ground truth and markedly fewer energy-increase and positive energy rate events than an equally expressive unconstrained neural flow, while matching terminal distributional fit.

## 📝 요약

Metriplectic 조건부 흐름 매칭(MCFM)은 기본 원칙을 위배하지 않고 소산적 동역학을 학습하는 방법론입니다. 일반적인 신경망 대리 모델은 에너지를 주입하여 장기 예측의 불안정을 초래할 수 있지만, MCFM은 보존-소산 분할을 벡터 필드와 구조 보존 샘플러에 통합합니다. MCFM은 짧은 전이 구간에서 조건부 흐름 매칭을 통해 학습하여 긴 예측의 역전파를 피합니다. 추론 시에는 Strang-prox 방식으로 심플렉틱 업데이트와 근접 메트릭 단계를 번갈아 수행하여 이산 에너지 감소를 보장하며, 신뢰할 수 있는 에너지가 있을 경우 엄격한 감소를 강제하는 투영을 선택적으로 적용합니다. 이 방법론은 보존, 단조 소산 및 안정적인 예측과 관련된 연속 및 이산 시간 보장을 제공합니다. 제어된 기계적 벤치마크에서 MCFM은 실제에 가까운 위상 초상화를 제공하며, 에너지 증가 및 양의 에너지 비율 사건이 덜 발생하여 비슷한 표현력을 가진 비제약 신경 흐름보다 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. Metriplectic conditional flow matching (MCFM)는 보존-소산 분할을 벡터 필드와 구조 보존 샘플러에 통합하여 제1원칙을 위반하지 않고 소산 역학을 학습합니다.
- 2. MCFM은 짧은 전이에 대한 조건부 흐름 매칭을 통해 훈련하여 긴 롤아웃의 역방향 계산을 피합니다.
- 3. 추론 시, Strang-prox 스킴은 심플렉틱 업데이트와 근접 메트릭 단계를 번갈아 수행하여 이산 에너지 감소를 보장합니다.
- 4. MCFM는 연속 및 이산 시간 보장을 제공하여 보존, 단조 소산 및 안정적인 롤아웃과의 연결을 보장합니다.
- 5. 제어된 기계적 벤치마크에서 MCFM은 실제와 더 가까운 위상 초상화를 제공하며, 에너지 증가 및 양의 에너지율 이벤트가 현저히 적습니다.


---

*Generated on 2025-09-25 16:37:06*