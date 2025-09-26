---
keywords:
  - Multi-Agent Reinforcement Learning
  - Event-Triggered Policy Gradient
  - Attention Mechanism
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20338
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:07:37.975960",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Reinforcement Learning",
    "Event-Triggered Policy Gradient",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Reinforcement Learning": 0.78,
    "Event-Triggered Policy Gradient": 0.82,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Agent Reinforcement Learning",
        "canonical": "Multi-Agent Reinforcement Learning",
        "aliases": [
          "MARL"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in the paper, linking to a broad area of research in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Event-Triggered Policy Gradient",
        "canonical": "Event-Triggered Policy Gradient",
        "aliases": [
          "ET-MAPG"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to the paper, enhancing connectivity with related technical concepts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Attention-Based Variant",
        "canonical": "Attention Mechanism",
        "aliases": [
          "AET-MAPG"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing research on attention mechanisms, which is crucial for understanding communication patterns in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "time-triggered execution",
      "state-of-the-art",
      "computational load"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Agent Reinforcement Learning",
      "resolved_canonical": "Multi-Agent Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Event-Triggered Policy Gradient",
      "resolved_canonical": "Event-Triggered Policy Gradient",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Attention-Based Variant",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Adaptive Event-Triggered Policy Gradient for Multi-Agent Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20338.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20338](https://arxiv.org/abs/2509.20338)

## 🔗 유사한 논문
- [[2025-09-23/Bayesian Ego-graph inference for Networked Multi-Agent Reinforcement Learning_20250923|Bayesian Ego-graph inference for Networked Multi-Agent Reinforcement Learning]] (88.0% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (87.1% similar)
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (85.3% similar)
- [[2025-09-23/Strategic Coordination for Evolving Multi-agent Systems_ A Hierarchical Reinforcement and Collective Learning Approach_20250923|Strategic Coordination for Evolving Multi-agent Systems: A Hierarchical Reinforcement and Collective Learning Approach]] (85.2% similar)
- [[2025-09-23/HypeMARL_ Multi-Agent Reinforcement Learning For High-Dimensional, Parametric, and Distributed Systems_20250923|HypeMARL: Multi-Agent Reinforcement Learning For High-Dimensional, Parametric, and Distributed Systems]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Agent Reinforcement Learning|Multi-Agent Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Event-Triggered Policy Gradient|Event-Triggered Policy Gradient]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20338v1 Announce Type: cross 
Abstract: Conventional multi-agent reinforcement learning (MARL) methods rely on time-triggered execution, where agents sample and communicate actions at fixed intervals. This approach is often computationally expensive and communication-intensive. To address this limitation, we propose ET-MAPG (Event-Triggered Multi-Agent Policy Gradient reinforcement learning), a framework that jointly learns an agent's control policy and its event-triggering policy. Unlike prior work that decouples these mechanisms, ET-MAPG integrates them into a unified learning process, enabling agents to learn not only what action to take but also when to execute it. For scenarios with inter-agent communication, we introduce AET-MAPG, an attention-based variant that leverages a self-attention mechanism to learn selective communication patterns. AET-MAPG empowers agents to determine not only when to trigger an action but also with whom to communicate and what information to exchange, thereby optimizing coordination. Both methods can be integrated with any policy gradient MARL algorithm. Extensive experiments across diverse MARL benchmarks demonstrate that our approaches achieve performance comparable to state-of-the-art, time-triggered baselines while significantly reducing both computational load and communication overhead.

## 📝 요약

기존의 다중 에이전트 강화 학습(MARL) 방법은 고정된 간격으로 행동을 샘플링하고 통신하는 시간 기반 실행에 의존하여 계산 비용과 통신 부담이 큽니다. 이를 해결하기 위해, 우리는 ET-MAPG(이벤트 기반 다중 에이전트 정책 경사 강화 학습)를 제안합니다. 이 프레임워크는 에이전트의 제어 정책과 이벤트 트리거 정책을 통합하여 학습하며, 에이전트가 어떤 행동을 취할지뿐만 아니라 언제 실행할지를 학습할 수 있게 합니다. 또한, 에이전트 간 통신이 필요한 시나리오를 위해 AET-MAPG라는 주의 메커니즘 기반 변형을 도입하여 선택적 통신 패턴을 학습합니다. AET-MAPG는 에이전트가 행동을 언제 실행할지뿐만 아니라 누구와 통신할지, 어떤 정보를 교환할지를 결정하여 협업을 최적화합니다. 이 두 방법은 모든 정책 경사 MARL 알고리즘과 통합될 수 있으며, 다양한 MARL 벤치마크에서 실험한 결과, 최신 시간 기반 방법들과 유사한 성능을 보이면서도 계산 및 통신 부담을 크게 줄였습니다.

## 🎯 주요 포인트

- 1. 기존의 다중 에이전트 강화 학습(MARL) 방법은 고정된 간격으로 행동을 샘플링하고 통신하는 시간 기반 실행에 의존합니다.
- 2. ET-MAPG는 에이전트의 제어 정책과 이벤트 트리거 정책을 통합하여 학습하는 프레임워크로, 에이전트가 어떤 행동을 취할지뿐만 아니라 언제 실행할지를 학습할 수 있게 합니다.
- 3. AET-MAPG는 주의 메커니즘을 활용하여 선택적 통신 패턴을 학습하는 주의 기반 변형으로, 에이전트가 행동을 언제 트리거할지뿐만 아니라 누구와 통신할지, 어떤 정보를 교환할지를 결정할 수 있게 합니다.
- 4. 제안된 방법들은 모든 정책 경사 MARL 알고리즘과 통합될 수 있으며, 다양한 MARL 벤치마크에서 실험한 결과, 최신의 시간 기반 방법들과 비교해 성능은 유사하면서도 계산 부하와 통신 오버헤드를 크게 줄였습니다.


---

*Generated on 2025-09-25 16:07:37*