---
keywords:
  - Federated Learning
  - Hierarchical Federated Learning
  - Intermittent Client Participation
  - Stagewise Decision-Making
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.09303
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:38:07.870574",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Hierarchical Federated Learning",
    "Intermittent Client Participation",
    "Stagewise Decision-Making"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Hierarchical Federated Learning": 0.78,
    "Intermittent Client Participation": 0.77,
    "Stagewise Decision-Making": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a foundational concept that connects to various distributed learning paradigms.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Federated Learning",
        "canonical": "Hierarchical Federated Learning",
        "aliases": [
          "HFL"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific variant of Federated Learning that addresses hierarchical client organization, offering unique linkage opportunities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Intermittent Client Participation",
        "canonical": "Intermittent Client Participation",
        "aliases": [
          "Dynamic Client Availability"
        ],
        "category": "unique_technical",
        "rationale": "Addresses a critical real-world challenge in Federated Learning, providing a unique angle for research connections.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Stagewise Decision-Making Methodology",
        "canonical": "Stagewise Decision-Making",
        "aliases": [
          "Stagewise Approach"
        ],
        "category": "unique_technical",
        "rationale": "This methodology offers a novel approach to client selection in Federated Learning, enhancing decision-making processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "model",
      "system",
      "methodology"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hierarchical Federated Learning",
      "resolved_canonical": "Hierarchical Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Intermittent Client Participation",
      "resolved_canonical": "Intermittent Client Participation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Stagewise Decision-Making Methodology",
      "resolved_canonical": "Stagewise Decision-Making",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.09303.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.09303](https://arxiv.org/abs/2502.09303)

## 🔗 유사한 논문
- [[2025-09-23/Asynchronous Federated Learning_ A Scalable Approach for Decentralized Machine Learning_20250923|Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning]] (86.5% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (86.1% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (85.9% similar)
- [[2025-09-22/Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning_20250922|Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning]] (85.7% similar)
- [[2025-09-17/Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning_20250917|Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**⚡ Unique Technical**: [[keywords/Hierarchical Federated Learning|Hierarchical Federated Learning]], [[keywords/Intermittent Client Participation|Intermittent Client Participation]], [[keywords/Stagewise Decision-Making|Stagewise Decision-Making]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.09303v3 Announce Type: replace 
Abstract: Federated Learning (FL) offers a pioneering distributed learning paradigm that enables devices/clients to build a shared global model. This global model is obtained through frequent model transmissions between clients and a central server, which may cause high latency, energy consumption, and congestion over backhaul links. To overcome these drawbacks, Hierarchical Federated Learning (HFL) has emerged, which organizes clients into multiple clusters and utilizes edge nodes (e.g., edge servers) for intermediate model aggregations between clients and the central server. Current research on HFL mainly focus on enhancing model accuracy, latency, and energy consumption in scenarios with a stable/fixed set of clients. However, addressing the dynamic availability of clients -- a critical aspect of real-world scenarios -- remains underexplored. This study delves into optimizing client selection and client-to-edge associations in HFL under intermittent client participation so as to minimize overall system costs (i.e., delay and energy), while achieving fast model convergence. We unveil that achieving this goal involves solving a complex NP-hard problem. To tackle this, we propose a stagewise methodology that splits the solution into two stages, referred to as Plan A and Plan B. Plan A focuses on identifying long-term clients with high chance of participation in subsequent model training rounds. Plan B serves as a backup, selecting alternative clients when long-term clients are unavailable during model training rounds. This stagewise methodology offers a fresh perspective on client selection that can enhance both HFL and conventional FL via enabling low-overhead decision-making processes. Through evaluations on MNIST and CIFAR-10 datasets, we show that our methodology outperforms existing benchmarks in terms of model accuracy and system costs.

## 📝 요약

이 논문은 동적 클라이언트 참여를 고려한 계층적 연합 학습(HFL)에서 클라이언트 선택 및 엣지 노드 연결 최적화를 통해 시스템 비용(지연 및 에너지)을 최소화하고 빠른 모델 수렴을 달성하는 방법을 제안합니다. 연구는 클라이언트의 불규칙한 참여를 다루기 위해 두 단계로 나누어진 방법론(Plan A와 Plan B)을 제시합니다. Plan A는 장기적으로 참여 가능성이 높은 클라이언트를 식별하고, Plan B는 장기 클라이언트가 불가능할 때 대체 클라이언트를 선택합니다. 이 방법론은 MNIST와 CIFAR-10 데이터셋 평가에서 기존 벤치마크보다 모델 정확도와 시스템 비용 측면에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 연합 학습(Federated Learning, FL)은 장치/클라이언트가 공유 글로벌 모델을 구축할 수 있도록 하는 혁신적인 분산 학습 패러다임을 제공합니다.
- 2. 계층적 연합 학습(HFL)은 클라이언트를 여러 클러스터로 조직하고 엣지 노드를 활용하여 클라이언트와 중앙 서버 간의 중간 모델 집계를 수행합니다.
- 3. 본 연구는 간헐적인 클라이언트 참여 하에서 HFL의 클라이언트 선택 및 클라이언트-엣지 연결 최적화를 통해 시스템 비용(지연 및 에너지)을 최소화하면서 빠른 모델 수렴을 달성하는 것을 목표로 합니다.
- 4. 제안된 단계적 방법론은 Plan A와 Plan B로 해결책을 나누어, 장기적으로 참여 가능성이 높은 클라이언트를 식별하고 대체 클라이언트를 선택하는 프로세스를 제시합니다.
- 5. MNIST와 CIFAR-10 데이터셋에 대한 평가를 통해 제안된 방법론이 모델 정확도와 시스템 비용 측면에서 기존 벤치마크를 능가함을 입증했습니다.


---

*Generated on 2025-09-24 02:38:07*