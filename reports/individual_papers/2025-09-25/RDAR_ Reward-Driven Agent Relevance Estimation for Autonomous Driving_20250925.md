---
keywords:
  - Attention Mechanism
  - Markov Decision Process
  - Autonomous Driving
  - Agent Relevance Estimation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19789
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:49:36.795107",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Markov Decision Process",
    "Autonomous Driving",
    "Agent Relevance Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Markov Decision Process": 0.8,
    "Autonomous Driving": 0.78,
    "Agent Relevance Estimation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Mechanisms"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanisms are crucial for understanding agent interactions in autonomous driving, providing a strong link to existing research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Markov Decision Process",
        "canonical": "Markov Decision Process",
        "aliases": [
          "MDP"
        ],
        "category": "specific_connectable",
        "rationale": "Markov Decision Processes are fundamental in modeling decision-making problems, linking to a wide range of applications in AI.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Autonomous Driving",
        "canonical": "Autonomous Driving",
        "aliases": [
          "Self-Driving Cars"
        ],
        "category": "unique_technical",
        "rationale": "Autonomous Driving is a distinct application area that benefits from linking to research in AI and robotics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Agent Relevance Estimation",
        "canonical": "Agent Relevance Estimation",
        "aliases": [
          "Agent Relevance"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper's approach in filtering important agents, offering a novel perspective in autonomous systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Markov Decision Process",
      "resolved_canonical": "Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Autonomous Driving",
      "resolved_canonical": "Autonomous Driving",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Agent Relevance Estimation",
      "resolved_canonical": "Agent Relevance Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# RDAR: Reward-Driven Agent Relevance Estimation for Autonomous Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19789.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19789](https://arxiv.org/abs/2509.19789)

## 🔗 유사한 논문
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (84.6% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (83.0% similar)
- [[2025-09-22/CoReVLA_ A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine_20250922|CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine]] (82.5% similar)
- [[2025-09-23/ReasonPlan_ Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving_20250923|ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving]] (81.9% similar)
- [[2025-09-23/RIFT_ Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation_20250923|RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Markov Decision Process|Markov Decision Process]]
**⚡ Unique Technical**: [[keywords/Autonomous Driving|Autonomous Driving]], [[keywords/Agent Relevance Estimation|Agent Relevance Estimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19789v1 Announce Type: cross 
Abstract: Human drivers focus only on a handful of agents at any one time. On the other hand, autonomous driving systems process complex scenes with numerous agents, regardless of whether they are pedestrians on a crosswalk or vehicles parked on the side of the road. While attention mechanisms offer an implicit way to reduce the input to the elements that affect decisions, existing attention mechanisms for capturing agent interactions are quadratic, and generally computationally expensive. We propose RDAR, a strategy to learn per-agent relevance -- how much each agent influences the behavior of the controlled vehicle -- by identifying which agents can be excluded from the input to a pre-trained behavior model. We formulate the masking procedure as a Markov Decision Process where the action consists of a binary mask indicating agent selection. We evaluate RDAR on a large-scale driving dataset, and demonstrate its ability to learn an accurate numerical measure of relevance by achieving comparable driving performance, in terms of overall progress, safety and performance, while processing significantly fewer agents compared to a state of the art behavior model.

## 📝 요약

이 논문은 자율 주행 시스템에서 주행 차량에 영향을 미치는 주변 에이전트를 효율적으로 식별하는 RDAR 전략을 제안합니다. RDAR은 사전 학습된 행동 모델에 입력될 에이전트를 선택하는 과정을 마코프 결정 과정으로 정의하여 각 에이전트의 중요도를 학습합니다. 대규모 주행 데이터셋을 통해 RDAR의 성능을 평가한 결과, 기존 모델과 유사한 주행 성능과 안전성을 유지하면서도 처리해야 할 에이전트 수를 크게 줄일 수 있음을 입증했습니다. 주요 기여는 주행 성능을 유지하면서 계산 비용을 줄이는 데 있습니다.

## 🎯 주요 포인트

- 1. 인간 운전자는 한 번에 소수의 에이전트에만 집중하지만, 자율 주행 시스템은 복잡한 장면의 수많은 에이전트를 처리한다.
- 2. 기존의 주의 메커니즘은 에이전트 상호작용을 포착하는 데 있어 계산 비용이 많이 드는 문제를 가진다.
- 3. RDAR은 사전 학습된 행동 모델에 입력되는 에이전트를 선택적으로 제외하여 각 에이전트의 관련성을 학습하는 전략을 제안한다.
- 4. RDAR은 마르코프 결정 프로세스로 마스킹 절차를 공식화하여 에이전트 선택을 이진 마스크로 나타낸다.
- 5. RDAR은 대규모 주행 데이터셋에서 평가되었으며, 적은 수의 에이전트를 처리하면서도 기존 모델과 유사한 주행 성능을 달성한다.


---

*Generated on 2025-09-25 15:49:36*