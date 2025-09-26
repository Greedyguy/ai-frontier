<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:59:22.888614",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sim-to-Real Transfer",
    "Domain Randomization",
    "Zero-Shot Safety",
    "Robust Safe Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sim-to-Real Transfer": 0.87,
    "Domain Randomization": 0.83,
    "Zero-Shot Safety": 0.79,
    "Robust Safe Reinforcement Learning": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sim-to-real transfer",
        "canonical": "Sim-to-Real Transfer",
        "aliases": [
          "sim2real",
          "simulation to reality transfer"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for linking discussions around transferring learned policies from simulated environments to real-world applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.87
      },
      {
        "surface": "Domain randomization",
        "canonical": "Domain Randomization",
        "aliases": [
          "randomized domain",
          "DR"
        ],
        "category": "specific_connectable",
        "rationale": "Domain randomization is a key technique in sim-to-real transfer, enhancing the connectivity with other sim-to-real strategies.",
        "novelty_score": 0.48,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.83
      },
      {
        "surface": "Zero-Shot Safety",
        "canonical": "Zero-Shot Safety",
        "aliases": [
          "zero-shot safe transfer"
        ],
        "category": "unique_technical",
        "rationale": "This novel concept addresses safety in sim-to-real transfer without prior real-world data, making it a unique point of discussion.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Robust Safe RL",
        "canonical": "Robust Safe Reinforcement Learning",
        "aliases": [
          "safe RL",
          "robust RL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a critical area of research for ensuring safety in RL applications, linking well with safety and robustness discussions.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "safety",
      "real-world applications",
      "training environments",
      "simulation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sim-to-real transfer",
      "resolved_canonical": "Sim-to-Real Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Domain randomization",
      "resolved_canonical": "Domain Randomization",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Zero-Shot Safety",
      "resolved_canonical": "Zero-Shot Safety",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Robust Safe RL",
      "resolved_canonical": "Robust Safe Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# SPiDR: A Simple Approach for Zero-Shot Safety in Sim-to-Real Transfer

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18648.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18648](https://arxiv.org/abs/2509.18648)

## 🔗 유사한 논문
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (86.0% similar)
- [[2025-09-22/Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations_20250922|Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations]] (83.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.3% similar)
- [[2025-09-24/APRIL_ Active Partial Rollouts in Reinforcement Learning to tame long-tail generation_20250924|APRIL: Active Partial Rollouts in Reinforcement Learning to tame long-tail generation]] (83.3% similar)
- [[2025-09-23/RIFT_ Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation_20250923|RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sim-to-Real Transfer|Sim-to-Real Transfer]], [[keywords/Domain Randomization|Domain Randomization]], [[keywords/Robust Safe Reinforcement Learning|Robust Safe Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Zero-Shot Safety|Zero-Shot Safety]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18648v1 Announce Type: cross 
Abstract: Safety remains a major concern for deploying reinforcement learning (RL) in real-world applications. Simulators provide safe, scalable training environments, but the inevitable sim-to-real gap introduces additional safety concerns, as policies must satisfy constraints in real-world conditions that differ from simulation. To address this challenge, robust safe RL techniques offer principled methods, but are often incompatible with standard scalable training pipelines. In contrast, domain randomization, a simple and popular sim-to-real technique, stands out as a promising alternative, although it often results in unsafe behaviors in practice. We present SPiDR, short for Sim-to-real via Pessimistic Domain Randomization -- a scalable algorithm with provable guarantees for safe sim-to-real transfer. SPiDR uses domain randomization to incorporate the uncertainty about the sim-to-real gap into the safety constraints, making it versatile and highly compatible with existing training pipelines. Through extensive experiments on sim-to-sim benchmarks and two distinct real-world robotic platforms, we demonstrate that SPiDR effectively ensures safety despite the sim-to-real gap while maintaining strong performance.

## 📝 요약

강화 학습(RL)의 실제 적용에서 안전성 문제를 해결하기 위해 SPiDR(Sim-to-real via Pessimistic Domain Randomization) 알고리즘을 제안합니다. 기존의 강건한 안전 RL 기법은 표준 훈련 파이프라인과 호환되지 않는 경우가 많지만, SPiDR은 도메인 랜덤화를 통해 시뮬레이션과 현실 간의 불확실성을 안전 제약에 반영하여 이를 해결합니다. 이 알고리즘은 확장 가능하며, 기존 훈련 파이프라인과 높은 호환성을 보입니다. 다양한 시뮬레이션 및 실제 로봇 플랫폼 실험을 통해 SPiDR이 시뮬레이션-현실 간 격차에도 불구하고 안전성을 보장하면서도 우수한 성능을 유지함을 입증했습니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)의 실제 응용에서 안전성은 여전히 주요 우려 사항입니다.
- 2. 시뮬레이터는 안전하고 확장 가능한 훈련 환경을 제공하지만, 시뮬레이션과 실제 간의 차이로 인해 추가적인 안전 문제가 발생합니다.
- 3. SPiDR는 비관적 도메인 랜덤화를 통해 안전한 시뮬레이션-현실 전이를 보장하는 확장 가능한 알고리즘입니다.
- 4. SPiDR는 기존 훈련 파이프라인과 높은 호환성을 가지며, 시뮬레이션-현실 간의 불확실성을 안전 제약에 통합합니다.
- 5. 실험 결과, SPiDR는 시뮬레이션-현실 간의 차이에도 불구하고 안전성을 보장하면서 강력한 성능을 유지합니다.


---

*Generated on 2025-09-24 13:59:22*