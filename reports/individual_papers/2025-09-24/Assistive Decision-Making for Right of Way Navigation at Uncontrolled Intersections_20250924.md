<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:48:25.883335",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Partially Observable Markov Decision Process",
    "Probabilistic Planning",
    "Sensor Fusion",
    "Environment Perception"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Partially Observable Markov Decision Process": 0.78,
    "Probabilistic Planning": 0.8,
    "Sensor Fusion": 0.82,
    "Environment Perception": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Partially Observable Markov Decision Process",
        "canonical": "Partially Observable Markov Decision Process",
        "aliases": [
          "POMDP"
        ],
        "category": "unique_technical",
        "rationale": "POMDP is a specialized concept in decision-making under uncertainty, crucial for linking to advanced planning strategies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "probabilistic planners",
        "canonical": "Probabilistic Planning",
        "aliases": [
          "probabilistic planners"
        ],
        "category": "specific_connectable",
        "rationale": "Probabilistic planning is a key concept in autonomous systems, facilitating connections to various decision-making frameworks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "sensor fusion",
        "canonical": "Sensor Fusion",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Sensor fusion is integral to enhancing perception in autonomous systems, linking to real-time data integration.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "environment perception",
        "canonical": "Environment Perception",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Environment perception is critical for autonomous navigation, connecting to sensor data interpretation and decision-making.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "driver-assist framework",
      "stochastic traffic agents"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Partially Observable Markov Decision Process",
      "resolved_canonical": "Partially Observable Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "probabilistic planners",
      "resolved_canonical": "Probabilistic Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "sensor fusion",
      "resolved_canonical": "Sensor Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "environment perception",
      "resolved_canonical": "Environment Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18407.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18407](https://arxiv.org/abs/2509.18407)

## 🔗 유사한 논문
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (85.4% similar)
- [[2025-09-24/MMCD_ Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation_20250924|MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation]] (84.9% similar)
- [[2025-09-23/DriveDPO_ Policy Learning via Safety DPO For End-to-End Autonomous Driving_20250923|DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving]] (84.3% similar)
- [[2025-09-23/ReasonPlan_ Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving_20250923|ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving]] (83.7% similar)
- [[2025-09-17/MAP_ End-to-End Autonomous Driving with Map-Assisted Planning_20250917|MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Probabilistic Planning|Probabilistic Planning]], [[keywords/Sensor Fusion|Sensor Fusion]], [[keywords/Environment Perception|Environment Perception]]
**⚡ Unique Technical**: [[keywords/Partially Observable Markov Decision Process|Partially Observable Markov Decision Process]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18407v1 Announce Type: cross 
Abstract: Uncontrolled intersections account for a significant fraction of roadway crashes due to ambiguous right-of-way rules, occlusions, and unpredictable driver behavior. While autonomous vehicle research has explored uncertainty-aware decision making, few systems exist to retrofit human-operated vehicles with assistive navigation support. We present a driver-assist framework for right-of-way reasoning at uncontrolled intersections, formulated as a Partially Observable Markov Decision Process (POMDP). Using a custom simulation testbed with stochastic traffic agents, pedestrians, occlusions, and adversarial scenarios, we evaluate four decision-making approaches: a deterministic finite state machine (FSM), and three probabilistic planners: QMDP, POMCP, and DESPOT. Results show that probabilistic planners outperform the rule-based baseline, achieving up to 97.5 percent collision-free navigation under partial observability, with POMCP prioritizing safety and DESPOT balancing efficiency and runtime feasibility. Our findings highlight the importance of uncertainty-aware planning for driver assistance and motivate future integration of sensor fusion and environment perception modules for real-time deployment in realistic traffic environments.

## 📝 요약

이 논문은 비신호 교차로에서의 운전 보조 시스템을 제안하며, 이는 부분 관측 마르코프 결정 프로세스(POMDP)로 구성됩니다. 연구는 맞춤형 시뮬레이션 환경에서 확률적 플래너(QMDP, POMCP, DESPOT)와 결정론적 유한 상태 기계(FSM)를 평가했습니다. 결과적으로, 확률적 플래너가 규칙 기반 시스템보다 뛰어난 성능을 보였으며, POMCP는 안전성을, DESPOT는 효율성과 실행 가능성을 중시했습니다. 이 연구는 불확실성을 고려한 계획의 중요성을 강조하며, 실시간 배치를 위한 센서 융합 및 환경 인식 모듈의 통합 필요성을 제시합니다.

## 🎯 주요 포인트

- 1. 무신호 교차로에서의 사고는 불명확한 통행 우선권 규칙, 시야 가림, 예측 불가능한 운전자 행동 때문에 발생하며, 이를 해결하기 위한 운전자 보조 프레임워크가 제안되었습니다.
- 2. 제안된 프레임워크는 부분 관측 마르코프 결정 프로세스(POMDP)로 구성되어 있으며, 이는 인간 운전 차량에 보조 내비게이션을 제공하는 데 중점을 둡니다.
- 3. 확률적 계획 수립 접근법인 QMDP, POMCP, DESPOT가 규칙 기반의 결정적 유한 상태 기계(FSM)보다 뛰어난 성능을 보였으며, POMCP는 안전성을 우선시하고 DESPOT는 효율성과 실행 가능성을 균형 있게 유지합니다.
- 4. 연구 결과는 불확실성을 고려한 계획 수립이 운전자 보조에 중요함을 강조하며, 실시간 배치를 위한 센서 융합 및 환경 인식 모듈의 통합 필요성을 제시합니다.


---

*Generated on 2025-09-24 13:48:25*