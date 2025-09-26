---
keywords:
  - Multi-Agent Simulation
  - Strategic Planning in Multi-Agent Systems
  - Neural Network
  - Waypoint Navigation System
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.06355
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:33:01.265994",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Simulation",
    "Strategic Planning in Multi-Agent Systems",
    "Neural Network",
    "Waypoint Navigation System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Simulation": 0.82,
    "Strategic Planning in Multi-Agent Systems": 0.84,
    "Neural Network": 0.78,
    "Waypoint Navigation System": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-agent simulator",
        "canonical": "Multi-Agent Simulation",
        "aliases": [
          "multi-agent simulator",
          "multi-agent environment"
        ],
        "category": "specific_connectable",
        "rationale": "Facilitates connections with research in multi-agent systems and simulation environments.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "strategic multi-agent planning",
        "canonical": "Strategic Planning in Multi-Agent Systems",
        "aliases": [
          "strategic planning",
          "multi-agent planning"
        ],
        "category": "specific_connectable",
        "rationale": "Links to research on strategic decision-making in multi-agent contexts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.81,
        "link_intent_score": 0.84
      },
      {
        "surface": "neural predictive and generative models",
        "canonical": "Neural Network",
        "aliases": [
          "predictive models",
          "generative models"
        ],
        "category": "broad_technical",
        "rationale": "Connects with the broader field of neural networks used for prediction and generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "waypoint system",
        "canonical": "Waypoint Navigation System",
        "aliases": [
          "waypoint system",
          "navigation system"
        ],
        "category": "unique_technical",
        "rationale": "Unique approach to discretizing continuous states in simulation environments.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.83,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "CS:GO",
      "gameplay"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-agent simulator",
      "resolved_canonical": "Multi-Agent Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "strategic multi-agent planning",
      "resolved_canonical": "Strategic Planning in Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.81,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "neural predictive and generative models",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "waypoint system",
      "resolved_canonical": "Waypoint Navigation System",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.83,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# A Data-Driven Discretized CS:GO Simulation Environment to Facilitate Strategic Multi-Agent Planning Research

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06355.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.06355](https://arxiv.org/abs/2509.06355)

## 🔗 유사한 논문
- [[2025-09-19/STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP: Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (80.5% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (80.1% similar)
- [[2025-09-23/Dynamic Speculative Agent Planning_20250923|Dynamic Speculative Agent Planning]] (79.5% similar)
- [[2025-09-22/AdaSports-Traj_ Role- and Domain-Aware Adaptation for Multi-Agent Trajectory Modeling in Sports_20250922|AdaSports-Traj: Role- and Domain-Aware Adaptation for Multi-Agent Trajectory Modeling in Sports]] (79.4% similar)
- [[2025-09-23/The STAR-XAI Protocol_ An Interactive Framework for Inducing Second-Order Agency in AI Agents_20250923|The STAR-XAI Protocol: An Interactive Framework for Inducing Second-Order Agency in AI Agents]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent Simulation|Multi-Agent Simulation]], [[keywords/Strategic Planning in Multi-Agent Systems|Strategic Planning in Multi-Agent Systems]]
**⚡ Unique Technical**: [[keywords/Waypoint Navigation System|Waypoint Navigation System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06355v2 Announce Type: replace 
Abstract: Modern simulation environments for complex multi-agent interactions must balance high-fidelity detail with computational efficiency. We present DECOY, a novel multi-agent simulator that abstracts strategic, long-horizon planning in 3D terrains into high-level discretized simulation while preserving low-level environmental fidelity. Using Counter-Strike: Global Offensive (CS:GO) as a testbed, our framework accurately simulates gameplay using only movement decisions as tactical positioning -- without explicitly modeling low-level mechanics such as aiming and shooting. Central to our approach is a waypoint system that simplifies and discretizes continuous states and actions, paired with neural predictive and generative models trained on real CS:GO tournament data to reconstruct event outcomes. Extensive evaluations show that replays generated from human data in DECOY closely match those observed in the original game. Our publicly available simulation environment provides a valuable tool for advancing research in strategic multi-agent planning and behavior generation.

## 📝 요약

DECOY는 복잡한 다중 에이전트 상호작용을 위한 시뮬레이터로, 3D 지형에서의 전략적 장기 계획을 고수준의 이산화된 시뮬레이션으로 추상화하면서도 환경의 세부 사항을 유지합니다. Counter-Strike: Global Offensive(CS:GO)를 테스트베드로 사용하여, 저수준의 조준 및 사격 메커니즘을 명시적으로 모델링하지 않고도 이동 결정만으로 게임플레이를 정확히 시뮬레이션합니다. 우리의 접근법의 핵심은 연속적인 상태와 행동을 단순화하고 이산화하는 웨이포인트 시스템이며, 실제 CS:GO 토너먼트 데이터를 기반으로 훈련된 신경 예측 및 생성 모델을 사용하여 이벤트 결과를 재구성합니다. DECOY에서 생성된 리플레이는 원래 게임에서 관찰된 것과 유사하며, 이는 전략적 다중 에이전트 계획 및 행동 생성 연구를 발전시키는 데 유용한 도구를 제공합니다.

## 🎯 주요 포인트

- 1. DECOY는 3D 지형에서의 전략적 장기 계획을 고수준의 이산 시뮬레이션으로 추상화하여 복잡한 다중 에이전트 상호작용을 효과적으로 시뮬레이션합니다.
- 2. 이 프레임워크는 CS:GO를 테스트베드로 사용하여 움직임 결정만으로 게임플레이를 정확하게 시뮬레이션하며, 조준 및 사격과 같은 저수준 메커니즘을 명시적으로 모델링하지 않습니다.
- 3. 웨이포인트 시스템을 통해 연속적인 상태와 행동을 단순화 및 이산화하며, 실제 CS:GO 대회 데이터를 기반으로 훈련된 신경 예측 및 생성 모델을 사용하여 이벤트 결과를 재구성합니다.
- 4. DECOY에서 생성된 리플레이는 원래 게임에서 관찰된 것과 밀접하게 일치하며, 이는 전략적 다중 에이전트 계획 및 행동 생성 연구를 발전시키는 데 유용한 도구를 제공합니다.


---

*Generated on 2025-09-24 00:33:01*