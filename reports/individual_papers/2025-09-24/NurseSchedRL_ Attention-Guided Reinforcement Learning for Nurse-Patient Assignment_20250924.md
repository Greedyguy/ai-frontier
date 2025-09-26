<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:34:54.383282",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Attention Mechanism",
    "Proximal Policy Optimization",
    "Nurse-Patient Assignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Attention Mechanism": 0.82,
    "Proximal Policy Optimization": 0.78,
    "Nurse-Patient Assignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a core technique in the proposed framework, linking to a broad range of machine learning applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention-based Representations",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanism is crucial for skill and context representation, enhancing connectivity with related neural network concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "unique_technical",
        "rationale": "PPO is a specific reinforcement learning algorithm used in the framework, offering unique insights into optimization strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Nurse-Patient Assignment",
        "canonical": "Nurse-Patient Assignment",
        "aliases": [
          "Nurse Scheduling"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary application domain of the study, providing a unique context for healthcare-related scheduling problems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention-based Representations",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Nurse-Patient Assignment",
      "resolved_canonical": "Nurse-Patient Assignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# NurseSchedRL: Attention-Guided Reinforcement Learning for Nurse-Patient Assignment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18125.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18125](https://arxiv.org/abs/2509.18125)

## 🔗 유사한 논문
- [[2025-09-23/Improving After-sales Service_ Deep Reinforcement Learning for Dynamic Time Slot Assignment with Commitments and Customer Preferences_20250923|Improving After-sales Service: Deep Reinforcement Learning for Dynamic Time Slot Assignment with Commitments and Customer Preferences]] (85.2% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.4% similar)
- [[2025-09-23/Test-Time Learning and Inference-Time Deliberation for Efficiency-First Offline Reinforcement Learning in Care Coordination and Population Health Management_20250923|Test-Time Learning and Inference-Time Deliberation for Efficiency-First Offline Reinforcement Learning in Care Coordination and Population Health Management]] (82.3% similar)
- [[2025-09-22/Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios_20250922|Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios]] (82.2% similar)
- [[2025-09-19/An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]], [[keywords/Nurse-Patient Assignment|Nurse-Patient Assignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18125v1 Announce Type: cross 
Abstract: Healthcare systems face increasing pressure to allocate limited nursing resources efficiently while accounting for skill heterogeneity, patient acuity, staff fatigue, and continuity of care. Traditional optimization and heuristic scheduling methods struggle to capture these dynamic, multi-constraint environments. I propose NurseSchedRL, a reinforcement learning framework for nurse-patient assignment that integrates structured state encoding, constrained action masking, and attention-based representations of skills, fatigue, and geographical context. NurseSchedRL uses Proximal Policy Optimization (PPO) with feasibility masks to ensure assignments respect real-world constraints, while dynamically adapting to patient arrivals and varying nurse availability. In simulation with realistic nurse and patient data, NurseSchedRL achieves improved scheduling efficiency, better alignment of skills to patient needs, and reduced fatigue compared to baseline heuristic and unconstrained RL approaches. These results highlight the potential of reinforcement learning for decision support in complex, high-stakes healthcare workforce management.

## 📝 요약

이 논문은 제한된 간호 인력을 효율적으로 배치하기 위한 강화 학습 프레임워크인 NurseSchedRL을 제안합니다. 이 시스템은 간호사의 기술, 피로도, 지리적 맥락을 고려하여 상태를 인코딩하고, 제약 조건을 준수하는 행동을 선택합니다. Proximal Policy Optimization(PPO)을 활용하여 현실적인 제약을 반영하며, 환자 도착과 간호사 가용성 변화에 동적으로 대응합니다. 시뮬레이션 결과, NurseSchedRL은 기존의 휴리스틱 및 비제약 강화 학습 방법보다 스케줄링 효율성을 높이고, 기술과 환자 요구의 일치를 개선하며, 피로도를 줄이는 데 효과적임을 보여줍니다. 이는 복잡한 의료 인력 관리에서 강화 학습의 잠재력을 시사합니다.

## 🎯 주요 포인트

- 1. NurseSchedRL은 강화 학습 프레임워크로, 간호사-환자 배정을 위해 구조화된 상태 인코딩과 제약된 행동 마스킹을 통합합니다.
- 2. Proximal Policy Optimization(PPO)와 실행 가능성 마스크를 사용하여 실제 제약 조건을 준수하면서 동적으로 환자 도착과 간호사 가용성 변화에 적응합니다.
- 3. 시뮬레이션 결과, NurseSchedRL은 기존의 휴리스틱 및 비제약 강화 학습 방법에 비해 일정 효율성을 개선하고, 기술과 환자 요구의 더 나은 정렬, 피로 감소를 달성했습니다.
- 4. 이 연구는 복잡하고 중요한 의료 인력 관리에서 의사 결정을 지원하기 위한 강화 학습의 잠재력을 강조합니다.


---

*Generated on 2025-09-24 13:34:54*