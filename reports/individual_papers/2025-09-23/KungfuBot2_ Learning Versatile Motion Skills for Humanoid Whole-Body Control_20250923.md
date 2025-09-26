---
keywords:
  - Whole-Body Control
  - Humanoid Robots
  - Orthogonal Mixture-of-Experts
  - Motion Skills
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16638
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:29:46.573859",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Whole-Body Control",
    "Humanoid Robots",
    "Orthogonal Mixture-of-Experts",
    "Motion Skills"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Whole-Body Control": 0.78,
    "Humanoid Robots": 0.82,
    "Orthogonal Mixture-of-Experts": 0.85,
    "Motion Skills": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "whole-body control",
        "canonical": "Whole-Body Control",
        "aliases": [
          "full-body control",
          "entire-body control"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on humanoid robot capabilities and is not commonly found in existing vocabularies, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "humanoid robots",
        "canonical": "Humanoid Robots",
        "aliases": [
          "humanoid robotics",
          "humanoid machines"
        ],
        "category": "broad_technical",
        "rationale": "This term is crucial for linking discussions related to robotics and AI, providing a broad technical context.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Orthogonal Mixture-of-Experts",
        "canonical": "Orthogonal Mixture-of-Experts",
        "aliases": [
          "OMoE"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel architecture proposed in the paper, offering a unique approach to skill specialization and generalization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "motion skills",
        "canonical": "Motion Skills",
        "aliases": [
          "movement skills",
          "dynamic skills"
        ],
        "category": "specific_connectable",
        "rationale": "This term is essential for linking to discussions on robotics and AI focusing on movement and skill acquisition.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
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
      "candidate_surface": "whole-body control",
      "resolved_canonical": "Whole-Body Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "humanoid robots",
      "resolved_canonical": "Humanoid Robots",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Orthogonal Mixture-of-Experts",
      "resolved_canonical": "Orthogonal Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "motion skills",
      "resolved_canonical": "Motion Skills",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16638.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16638](https://arxiv.org/abs/2509.16638)

## 🔗 유사한 논문
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (86.1% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (85.7% similar)
- [[2025-09-18/Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (84.8% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (83.5% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Humanoid Robots|Humanoid Robots]]
**🔗 Specific Connectable**: [[keywords/Motion Skills|Motion Skills]]
**⚡ Unique Technical**: [[keywords/Whole-Body Control|Whole-Body Control]], [[keywords/Orthogonal Mixture-of-Experts|Orthogonal Mixture-of-Experts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16638v1 Announce Type: cross 
Abstract: Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 📝 요약

이 논문은 다양한 인간의 움직임을 추적하여 다목적 휴머노이드 로봇이 전신 기술을 학습하는 방법을 제시합니다. VMS라는 통합 전신 제어기를 개발하여 하나의 정책으로 다양한 동작 기술을 안정적으로 수행할 수 있도록 했습니다. 이 프레임워크는 지역적 움직임 충실도와 전반적 궤적 일관성을 균형 있게 유지하는 하이브리드 추적 목표와, 동작 간 일반화를 강화하면서 기술 전문화를 촉진하는 직교 전문가 혼합(OMoE) 구조를 통합합니다. 또한, 전역 변위와 일시적 부정확성을 처리할 때의 강건성을 높이기 위해 세그먼트 수준의 추적 보상을 도입했습니다. 시뮬레이션과 실제 실험을 통해 VMS의 정확한 동적 기술 모방, 분 단위 시퀀스에서의 안정적 성능, 미지의 동작에 대한 강한 일반화 능력을 입증했습니다. VMS는 다재다능한 휴머노이드 전신 제어의 확장 가능한 기반으로서의 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. VMS는 단일 정책으로 다양한 인간의 동작을 추적하여 휴머노이드 로봇이 다재다능한 전신 기술을 학습할 수 있게 하는 통합 전신 제어기입니다.
- 2. 하이브리드 추적 목표를 통해 지역적 동작 충실도와 전역 궤적 일관성을 균형 있게 유지합니다.
- 3. OMoE 아키텍처를 활용하여 기술 전문화를 장려하면서도 다양한 동작에 대한 일반화를 향상시킵니다.
- 4. 세그먼트 수준의 추적 보상을 도입하여 전역적 변위와 일시적 부정확성을 처리할 때의 강건성을 높입니다.
- 5. 시뮬레이션과 실제 실험에서 VMS의 정확한 동적 기술 모방과 분 단위의 안정적 성능, 보지 못한 동작에 대한 강력한 일반화를 입증했습니다.


---

*Generated on 2025-09-23 23:29:46*