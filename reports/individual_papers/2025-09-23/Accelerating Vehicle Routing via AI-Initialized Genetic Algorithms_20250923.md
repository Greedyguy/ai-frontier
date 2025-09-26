---
keywords:
  - Vehicle Routing Problem
  - Machine Learning
  - Genetic Algorithm
  - EARLI
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2504.06126
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:40:38.416875",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vehicle Routing Problem",
    "Machine Learning",
    "Genetic Algorithm",
    "EARLI"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vehicle Routing Problem": 0.8,
    "Machine Learning": 0.85,
    "Genetic Algorithm": 0.78,
    "EARLI": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vehicle Routing Problems",
        "canonical": "Vehicle Routing Problem",
        "aliases": [
          "VRP"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, VRP is a key problem in combinatorial optimization with specific applications in logistics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a subfield of Machine Learning, crucial for initializing solutions in the proposed framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Genetic Algorithm",
        "canonical": "Genetic Algorithm",
        "aliases": [
          "GA"
        ],
        "category": "specific_connectable",
        "rationale": "Genetic Algorithms are a core component of the proposed optimization framework, enhancing solution quality.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Evolutionary Algorithm with Reinforcement Learning Initialization",
        "canonical": "EARLI",
        "aliases": [
          "Evolutionary Algorithm with RL Initialization"
        ],
        "category": "unique_technical",
        "rationale": "EARLI is the novel framework introduced in the paper, combining AI and optimization techniques.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "real-time",
      "interactive",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vehicle Routing Problems",
      "resolved_canonical": "Vehicle Routing Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Genetic Algorithm",
      "resolved_canonical": "Genetic Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Evolutionary Algorithm with Reinforcement Learning Initialization",
      "resolved_canonical": "EARLI",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Accelerating Vehicle Routing via AI-Initialized Genetic Algorithms

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.06126.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2504.06126](https://arxiv.org/abs/2504.06126)

## 🔗 유사한 논문
- [[2025-09-18/VEGA_ Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization_20250918|VEGA: Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization]] (82.3% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (82.0% similar)
- [[2025-09-19/AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (82.0% similar)
- [[2025-09-19/Multi-CAP_ A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments_20250919|Multi-CAP: A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (81.7% similar)
- [[2025-09-23/Improving After-sales Service_ Deep Reinforcement Learning for Dynamic Time Slot Assignment with Commitments and Customer Preferences_20250923|Improving After-sales Service: Deep Reinforcement Learning for Dynamic Time Slot Assignment with Commitments and Customer Preferences]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Genetic Algorithm|Genetic Algorithm]]
**⚡ Unique Technical**: [[keywords/Vehicle Routing Problem|Vehicle Routing Problem]], [[keywords/EARLI|EARLI]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.06126v2 Announce Type: replace 
Abstract: Vehicle Routing Problems (VRP) are an extension of the Traveling Salesperson Problem and are a fundamental NP-hard challenge in combinatorial optimization. Solving VRP in real-time at large scale has become critical in numerous applications, from growing markets like last-mile delivery to emerging use-cases like interactive logistics planning. In many applications, one has to repeatedly solve VRP instances drawn from the same distribution, yet current state-of-the-art solvers treat each instance on its own without leveraging previous examples. We introduce an optimization framework where a reinforcement learning agent is trained on prior instances and quickly generates initial solutions, which are then further optimized by a genetic algorithm. This framework, Evolutionary Algorithm with Reinforcement Learning Initialization (EARLI), consistently outperforms current state-of-the-art solvers across various time budgets. For example, EARLI handles vehicle routing with 500 locations within one second, 10x faster than current solvers for the same solution quality, enabling real-time and interactive routing at scale. EARLI can generalize to new data, as we demonstrate on real e-commerce delivery data of a previously unseen city. By combining reinforcement learning and genetic algorithms, our hybrid framework takes a step forward to closer interdisciplinary collaboration between AI and optimization communities towards real-time optimization in diverse domains.

## 📝 요약

이 논문은 차량 경로 문제(VRP)를 실시간으로 대규모로 해결하기 위한 새로운 최적화 프레임워크인 EARLI를 소개합니다. VRP는 NP-난해한 문제로, 기존 솔버들은 각 인스턴스를 개별적으로 처리하지만, EARLI는 강화 학습 에이전트를 통해 이전 인스턴스에서 학습하여 초기 솔루션을 생성하고 이를 유전 알고리즘으로 최적화합니다. EARLI는 다양한 시간 제약 하에서 기존 솔버보다 우수한 성능을 보이며, 특히 500개 위치의 경로 문제를 1초 내에 해결하여 실시간 상호작용이 가능합니다. 또한, 새로운 데이터에 일반화할 수 있어, 미지의 도시에서의 전자상거래 배송 데이터로도 효과를 입증했습니다. 이 프레임워크는 AI와 최적화 커뮤니티 간의 협력을 통해 다양한 분야에서 실시간 최적화를 향상시킵니다.

## 🎯 주요 포인트

- 1. 차량 경로 문제(VRP)는 NP-난해한 조합 최적화 문제로, 실시간 대규모 해결이 중요해지고 있다.
- 2. 기존 솔버들은 각 인스턴스를 개별적으로 처리하지만, EARLI는 이전 인스턴스를 학습하여 초기 솔루션을 빠르게 생성한다.
- 3. EARLI는 강화 학습과 유전 알고리즘을 결합하여 다양한 시간 제약 내에서 최첨단 솔버보다 우수한 성능을 보인다.
- 4. EARLI는 새로운 데이터에 일반화할 수 있으며, 실시간 대규모 경로 최적화를 가능하게 한다.
- 5. 이 프레임워크는 AI와 최적화 커뮤니티 간의 협력을 통해 다양한 분야에서 실시간 최적화를 향상시킨다.


---

*Generated on 2025-09-24 02:40:38*