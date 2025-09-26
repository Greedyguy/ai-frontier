<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:11:18.772457",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Age of Information",
    "Online Learning",
    "Energy Consumption",
    "Channel Statistics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Age of Information": 0.8,
    "Online Learning": 0.82,
    "Energy Consumption": 0.75,
    "Channel Statistics": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Age of Information",
        "canonical": "Age of Information",
        "aliases": [
          "AoI"
        ],
        "category": "unique_technical",
        "rationale": "Age of Information is a specific metric central to the paper's focus on optimizing information freshness.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Online Learning",
        "canonical": "Online Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Online Learning is a key method used to address the unknown channel statistics problem in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Energy Consumption",
        "canonical": "Energy Consumption",
        "aliases": [
          "Transmission Cost"
        ],
        "category": "unique_technical",
        "rationale": "Energy Consumption is a critical factor in the tradeoff being optimized in the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Channel Statistics",
        "canonical": "Channel Statistics",
        "aliases": [
          "Unknown Channel Statistics"
        ],
        "category": "unique_technical",
        "rationale": "Channel Statistics are fundamental to the problem setting and the development of the proposed algorithms.",
        "novelty_score": 0.7,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "real-time monitoring system",
      "status update transmissions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Age of Information",
      "resolved_canonical": "Age of Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Online Learning",
      "resolved_canonical": "Online Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Energy Consumption",
      "resolved_canonical": "Energy Consumption",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Channel Statistics",
      "resolved_canonical": "Channel Statistics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Online Learning for Optimizing AoI-Energy Tradeoff under Unknown Channel Statistics

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18654.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18654](https://arxiv.org/abs/2509.18654)

## 🔗 유사한 논문
- [[2025-09-23/Learn to Optimize Resource Allocation under QoS Constraint of AR_20250923|Learn to Optimize Resource Allocation under QoS Constraint of AR]] (82.4% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.0% similar)
- [[2025-09-24/Zero-Shot Transferable Solution Method for Parametric Optimal Control Problems_20250924|Zero-Shot Transferable Solution Method for Parametric Optimal Control Problems]] (79.8% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (79.7% similar)
- [[2025-09-24/A Simple and Reproducible Hybrid Solver for a Truck-Drone VRP with Recharge_20250924|A Simple and Reproducible Hybrid Solver for a Truck-Drone VRP with Recharge]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Online Learning|Online Learning]]
**⚡ Unique Technical**: [[keywords/Age of Information|Age of Information]], [[keywords/Energy Consumption|Energy Consumption]], [[keywords/Channel Statistics|Channel Statistics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18654v1 Announce Type: cross 
Abstract: We consider a real-time monitoring system where a source node (with energy limitations) aims to keep the information status at a destination node as fresh as possible by scheduling status update transmissions over a set of channels. The freshness of information at the destination node is measured in terms of the Age of Information (AoI) metric. In this setting, a natural tradeoff exists between the transmission cost (or equivalently, energy consumption) of the source and the achievable AoI performance at the destination. This tradeoff has been optimized in the existing literature under the assumption of having a complete knowledge of the channel statistics. In this work, we develop online learning-based algorithms with finite-time guarantees that optimize this tradeoff in the practical scenario where the channel statistics are unknown to the scheduler. In particular, when the channel statistics are known, the optimal scheduling policy is first proven to have a threshold-based structure with respect to the value of AoI (i.e., it is optimal to drop updates when the AoI value is below some threshold). This key insight was then utilized to develop the proposed learning algorithms that surprisingly achieve an order-optimal regret (i.e., $O(1)$) with respect to the time horizon length.

## 📝 요약

이 논문은 에너지 제약이 있는 소스 노드가 목적지 노드의 정보 신선도를 최대한 유지하기 위해 상태 업데이트 전송을 스케줄링하는 실시간 모니터링 시스템을 다룹니다. 정보 신선도는 정보의 연령(AoI)으로 측정됩니다. 기존 연구에서는 채널 통계에 대한 완전한 지식이 있는 상황에서 전송 비용과 AoI 성능 간의 균형을 최적화했습니다. 본 연구에서는 채널 통계가 알려지지 않은 실용적인 시나리오에서 이 균형을 최적화하는 온라인 학습 기반 알고리즘을 개발했습니다. 특히, 채널 통계가 알려진 경우 최적 스케줄링 정책이 AoI 값에 대한 임계값 기반 구조를 가짐을 증명했습니다. 이 통찰력을 바탕으로 제안된 학습 알고리즘은 시간 경과에 따른 후회를 $O(1)$로 줄이는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 에너지 제한이 있는 소스 노드가 목적지 노드의 정보 신선도를 최대한 유지하기 위해 상태 업데이트 전송을 스케줄링하는 실시간 모니터링 시스템을 고려합니다.
- 2. 정보 신선도는 정보의 나이(AoI) 메트릭으로 측정되며, 전송 비용과 목적지에서의 AoI 성능 간의 자연스러운 상충 관계가 존재합니다.
- 3. 채널 통계에 대한 완전한 지식이 없는 실용적인 시나리오에서 이 상충 관계를 최적화하기 위해 온라인 학습 기반 알고리즘을 개발하였습니다.
- 4. 채널 통계가 알려진 경우, 최적의 스케줄링 정책은 AoI 값에 대한 임계값 기반 구조를 가지며, 이는 업데이트를 버리는 것이 최적임을 증명하였습니다.
- 5. 제안된 학습 알고리즘은 시간 지평 길이에 대한 순서 최적의 후회를 달성합니다.


---

*Generated on 2025-09-24 15:11:18*