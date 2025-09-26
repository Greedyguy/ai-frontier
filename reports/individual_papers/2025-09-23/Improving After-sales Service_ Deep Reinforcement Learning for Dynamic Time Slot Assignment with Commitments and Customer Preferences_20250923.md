---
keywords:
  - Deep Reinforcement Learning
  - Attention Mechanism
  - Dynamic Time Slot Assignment Problem
  - Scenario-based Planning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17870
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:58:44.170687",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Reinforcement Learning",
    "Attention Mechanism",
    "Dynamic Time Slot Assignment Problem",
    "Scenario-based Planning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Reinforcement Learning": 0.78,
    "Attention Mechanism": 0.81,
    "Dynamic Time Slot Assignment Problem": 0.79,
    "Scenario-based Planning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Reinforcement Learning",
        "canonical": "Deep Reinforcement Learning",
        "aliases": [
          "DRL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Reinforcement Learning is a key methodology in the paper, linking it to broader machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention-based Deep Reinforcement Learning",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention-based DRL"
        ],
        "category": "specific_connectable",
        "rationale": "The use of an attention mechanism within DRL is a specific technique that connects to existing research on attention models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Dynamic Time Slot Assignment Problem",
        "canonical": "Dynamic Time Slot Assignment Problem",
        "aliases": [
          "DTSAP"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique problem definition central to the paper, providing a specific context for application of the methodologies discussed.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.91,
        "link_intent_score": 0.79
      },
      {
        "surface": "Scenario-based Planning",
        "canonical": "Scenario-based Planning",
        "aliases": [
          "SBP"
        ],
        "category": "unique_technical",
        "rationale": "Scenario-based Planning is a distinct approach in the paper, offering a unique perspective on problem-solving strategies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "maintenance scheduling",
      "after-sales service"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Reinforcement Learning",
      "resolved_canonical": "Deep Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention-based Deep Reinforcement Learning",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Dynamic Time Slot Assignment Problem",
      "resolved_canonical": "Dynamic Time Slot Assignment Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.91,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Scenario-based Planning",
      "resolved_canonical": "Scenario-based Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Improving After-sales Service: Deep Reinforcement Learning for Dynamic Time Slot Assignment with Commitments and Customer Preferences

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17870.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17870](https://arxiv.org/abs/2509.17870)

## 🔗 유사한 논문
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (81.3% similar)
- [[2025-09-19/An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (81.2% similar)
- [[2025-09-22/cadrille_ Multi-modal CAD Reconstruction with Online Reinforcement Learning_20250922|cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning]] (80.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (80.3% similar)
- [[2025-09-18/SHaRe-RL_ Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks_20250918|SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Reinforcement Learning|Deep Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Dynamic Time Slot Assignment Problem|Dynamic Time Slot Assignment Problem]], [[keywords/Scenario-based Planning|Scenario-based Planning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17870v1 Announce Type: new 
Abstract: Problem definition: For original equipment manufacturers (OEMs), high-tech maintenance is a strategic component in after-sales services, involving close coordination between customers and service engineers. Each customer suggests several time slots for their maintenance task, from which the OEM must select one. This decision needs to be made promptly to support customers' planning. At the end of each day, routes for service engineers are planned to fulfill the tasks scheduled for the following day. We study this hierarchical and sequential decision-making problem-the Dynamic Time Slot Assignment Problem with Commitments and Customer Preferences (DTSAP-CCP)-in this paper. Methodology/results: Two distinct approaches are proposed: 1) an attention-based deep reinforcement learning with rollout execution (ADRL-RE) and 2) a scenario-based planning approach (SBP). The ADRL-RE combines a well-trained attention-based neural network with a rollout framework for online trajectory simulation. To support the training, we develop a neural heuristic solver that provides rapid route planning solutions, enabling efficient learning in complex combinatorial settings. The SBP approach samples several scenarios to guide the time slot assignment. Numerical experiments demonstrate the superiority of ADRL-RE and the stability of SBP compared to both rule-based and rollout-based approaches. Furthermore, the strong practicality of ADRL-RE is verified in a case study of after-sales service for large medical equipment. Implications: This study provides OEMs with practical decision-support tools for dynamic maintenance scheduling, balancing customer preferences and operational efficiency. In particular, our ADRL-RE shows strong real-world potential, supporting timely and customer-aligned maintenance scheduling.

## 📝 요약

이 논문은 원래 장비 제조업체(OEM)를 위한 동적 유지보수 일정 계획 문제(DTSAP-CCP)를 다루며, 고객의 선호 시간대와 운영 효율성을 균형 있게 고려하는 방법론을 제안합니다. 두 가지 접근법이 제시되었는데, 첫째는 주의 기반 심층 강화 학습과 롤아웃 실행을 결합한 ADRL-RE이며, 둘째는 시나리오 기반 계획 접근법(SBP)입니다. ADRL-RE는 온라인 경로 시뮬레이션을 통해 효율적인 학습을 지원하고, SBP는 여러 시나리오를 샘플링하여 시간대 할당을 안내합니다. 실험 결과, ADRL-RE는 기존 방법보다 우수한 성능을 보였으며, 특히 대형 의료 장비의 애프터서비스 사례 연구에서 그 실용성이 입증되었습니다. 이 연구는 OEM에게 고객 맞춤형 유지보수 일정 계획을 위한 실질적인 의사결정 지원 도구를 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 OEM의 애프터서비스에서 고객 선호도와 운영 효율성을 균형 있게 고려한 동적 유지보수 일정 계획을 위한 실질적인 의사결정 지원 도구를 제공합니다.
- 2. 주의 기반 심층 강화 학습과 롤아웃 실행(ADRL-RE) 및 시나리오 기반 계획 접근법(SBP)이라는 두 가지 방법론을 제안합니다.
- 3. ADRL-RE는 주의 기반 신경망과 롤아웃 프레임워크를 결합하여 온라인 경로 시뮬레이션을 수행하며, 신경 휴리스틱 솔버를 개발하여 복잡한 조합 문제에서 효율적인 학습을 지원합니다.
- 4. 수치 실험 결과, ADRL-RE는 규칙 기반 및 롤아웃 기반 접근법에 비해 우수성을 보였으며, SBP는 안정성을 입증했습니다.
- 5. ADRL-RE의 강력한 실용성은 대형 의료 장비의 애프터서비스 사례 연구에서 검증되었습니다.


---

*Generated on 2025-09-24 01:58:44*