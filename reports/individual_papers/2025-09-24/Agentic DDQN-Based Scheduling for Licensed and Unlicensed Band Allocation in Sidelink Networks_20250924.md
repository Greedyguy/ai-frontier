<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:36:25.420498",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Q-Network",
    "Sidelink Networks",
    "Spectrum Allocation",
    "Quality of Service"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Q-Network": 0.82,
    "Sidelink Networks": 0.78,
    "Spectrum Allocation": 0.75,
    "Quality of Service": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "double deep Q-network",
        "canonical": "Deep Q-Network",
        "aliases": [
          "DDQN",
          "Double DQN"
        ],
        "category": "specific_connectable",
        "rationale": "Deep Q-Networks are a foundational concept in reinforcement learning, facilitating connections to broader RL topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "sidelink networks",
        "canonical": "Sidelink Networks",
        "aliases": [
          "SL Networks",
          "NR Sidelink"
        ],
        "category": "unique_technical",
        "rationale": "Sidelink networks are a specialized topic within wireless communications, relevant for discussions on network architecture.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "licensed/unlicensed band allocation",
        "canonical": "Spectrum Allocation",
        "aliases": [
          "Band Allocation",
          "Licensed and Unlicensed Spectrum"
        ],
        "category": "broad_technical",
        "rationale": "Spectrum allocation is a critical aspect of network design, linking to regulatory and technical discussions.",
        "novelty_score": 0.48,
        "connectivity_score": 0.79,
        "specificity_score": 0.67,
        "link_intent_score": 0.75
      },
      {
        "surface": "quality of service",
        "canonical": "Quality of Service",
        "aliases": [
          "QoS"
        ],
        "category": "broad_technical",
        "rationale": "Quality of Service is a key concept in network performance, connecting to discussions on service reliability and efficiency.",
        "novelty_score": 0.5,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "agent",
      "scheduler",
      "network edge"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "double deep Q-network",
      "resolved_canonical": "Deep Q-Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "sidelink networks",
      "resolved_canonical": "Sidelink Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "licensed/unlicensed band allocation",
      "resolved_canonical": "Spectrum Allocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.79,
        "specificity": 0.67,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "quality of service",
      "resolved_canonical": "Quality of Service",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Agentic DDQN-Based Scheduling for Licensed and Unlicensed Band Allocation in Sidelink Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06775.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.06775](https://arxiv.org/abs/2509.06775)

## 🔗 유사한 논문
- [[2025-09-19/An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (84.8% similar)
- [[2025-09-23/Learn to Optimize Resource Allocation under QoS Constraint of AR_20250923|Learn to Optimize Resource Allocation under QoS Constraint of AR]] (83.4% similar)
- [[2025-09-19/AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (81.0% similar)
- [[2025-09-24/A Simple and Reproducible Hybrid Solver for a Truck-Drone VRP with Recharge_20250924|A Simple and Reproducible Hybrid Solver for a Truck-Drone VRP with Recharge]] (80.9% similar)
- [[2025-09-24/NurseSchedRL_ Attention-Guided Reinforcement Learning for Nurse-Patient Assignment_20250924|NurseSchedRL: Attention-Guided Reinforcement Learning for Nurse-Patient Assignment]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Spectrum Allocation|Spectrum Allocation]], [[keywords/Quality of Service|Quality of Service]]
**🔗 Specific Connectable**: [[keywords/Deep Q-Network|Deep Q-Network]]
**⚡ Unique Technical**: [[keywords/Sidelink Networks|Sidelink Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06775v3 Announce Type: replace-cross 
Abstract: In this paper, we present an agentic double deep Q-network (DDQN) scheduler for licensed/unlicensed band allocation in New Radio (NR) sidelink (SL) networks. Beyond conventional reward-seeking reinforcement learning (RL), the agent perceives and reasons over a multi-dimensional context that jointly captures queueing delay, link quality, coexistence intensity, and switching stability. A capacity-aware, quality of service (QoS)-constrained reward aligns the agent with goal-oriented scheduling rather than static thresholding. Under constrained bandwidth, the proposed design reduces blocking by up to 87.5% versus threshold policies while preserving throughput, highlighting the value of context-driven decisions in coexistence-limited NR SL networks. The proposed scheduler is an embodied agent (E-agent) tailored for task-specific, resource-efficient operation at the network edge.

## 📝 요약

이 논문에서는 새로운 무선(New Radio, NR) 사이드링크(SL) 네트워크에서 면허/비면허 대역 할당을 위한 에이전트 기반의 이중 심층 Q-네트워크(DDQN) 스케줄러를 제안합니다. 제안된 에이전트는 큐잉 지연, 링크 품질, 공존 강도, 전환 안정성을 포함한 다차원적 맥락을 인식하고 분석하여 기존의 보상 중심 강화 학습을 넘어섭니다. 용량 인식 및 QoS 제약 보상 체계를 통해 에이전트가 목표 지향적 스케줄링을 수행하도록 하였으며, 제한된 대역폭 상황에서 차단율을 최대 87.5%까지 감소시키면서도 처리량을 유지합니다. 이는 공존 제한이 있는 NR SL 네트워크에서 맥락 기반 의사결정의 가치를 강조합니다. 제안된 스케줄러는 네트워크 엣지에서 자원 효율적인 작업을 수행하도록 설계된 구체화된 에이전트(E-agent)입니다.

## 🎯 주요 포인트

- 1. 본 논문에서는 NR SL 네트워크에서 라이선스/비라이선스 대역 할당을 위한 에이전트 기반의 DDQN 스케줄러를 제안합니다.
- 2. 에이전트는 대기 지연, 링크 품질, 공존 강도, 전환 안정성을 포함한 다차원 컨텍스트를 인식하고 추론합니다.
- 3. 제안된 설계는 제한된 대역폭 하에서 차단을 최대 87.5%까지 감소시키면서도 처리량을 유지합니다.
- 4. 제안된 스케줄러는 네트워크 엣지에서 작업 특화 및 자원 효율적인 운영을 위한 E-에이전트로 설계되었습니다.
- 5. QoS 제약 보상을 통해 에이전트는 정적 임계값 설정 대신 목표 지향적인 스케줄링을 수행합니다.


---

*Generated on 2025-09-24 15:36:25*