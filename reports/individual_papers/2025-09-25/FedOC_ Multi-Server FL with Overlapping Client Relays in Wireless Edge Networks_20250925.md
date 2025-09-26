---
keywords:
  - Federated Learning
  - Overlapping Clients
  - Edge Servers
  - Relay Overlapping Clients
  - Latency-Sensitive Edge Environments
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19398
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:34:21.641478",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Overlapping Clients",
    "Edge Servers",
    "Relay Overlapping Clients",
    "Latency-Sensitive Edge Environments"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Overlapping Clients": 0.72,
    "Edge Servers": 0.8,
    "Relay Overlapping Clients": 0.78,
    "Latency-Sensitive Edge Environments": 0.7
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
        "rationale": "Federated Learning is a central concept in the paper, linking it to broader machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Overlapping Clients",
        "canonical": "Overlapping Clients",
        "aliases": [
          "OC"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the proposed FedOC framework, facilitating specific discussions on client roles.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Edge Servers",
        "canonical": "Edge Servers",
        "aliases": [
          "ES"
        ],
        "category": "specific_connectable",
        "rationale": "Edge Servers are crucial to the architecture discussed, linking to topics in edge computing.",
        "novelty_score": 0.52,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Relay Overlapping Clients",
        "canonical": "Relay Overlapping Clients",
        "aliases": [
          "ROC"
        ],
        "category": "unique_technical",
        "rationale": "ROCs are a novel role within the FedOC framework, enhancing discussions on client relay functionalities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.62,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Latency-Sensitive Edge Environments",
        "canonical": "Latency-Sensitive Edge Environments",
        "aliases": [
          "Latency-Sensitive Edge"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is important for understanding the applicability of FedOC in real-world scenarios.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "multi-server",
      "model aggregation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Overlapping Clients",
      "resolved_canonical": "Overlapping Clients",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Edge Servers",
      "resolved_canonical": "Edge Servers",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Relay Overlapping Clients",
      "resolved_canonical": "Relay Overlapping Clients",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.62,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Latency-Sensitive Edge Environments",
      "resolved_canonical": "Latency-Sensitive Edge Environments",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# FedOC: Multi-Server FL with Overlapping Client Relays in Wireless Edge Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19398.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19398](https://arxiv.org/abs/2509.19398)

## 🔗 유사한 논문
- [[2025-09-23/Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation_ A Stagewise Decision-Making Methodology_20250923|Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology]] (83.8% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (83.5% similar)
- [[2025-09-23/FedEL_ Federated Elastic Learning for Heterogeneous Devices_20250923|FedEL: Federated Elastic Learning for Heterogeneous Devices]] (83.1% similar)
- [[2025-09-25/OmniFed_ A Modular Framework for Configurable Federated Learning from Edge to HPC_20250925|OmniFed: A Modular Framework for Configurable Federated Learning from Edge to HPC]] (82.9% similar)
- [[2025-09-23/Asynchronous Federated Learning_ A Scalable Approach for Decentralized Machine Learning_20250923|Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Edge Servers|Edge Servers]], [[keywords/Latency-Sensitive Edge Environments|Latency-Sensitive Edge Environments]]
**⚡ Unique Technical**: [[keywords/Overlapping Clients|Overlapping Clients]], [[keywords/Relay Overlapping Clients|Relay Overlapping Clients]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19398v1 Announce Type: cross 
Abstract: Multi-server Federated Learning (FL) has emerged as a promising solution to mitigate communication bottlenecks of single-server FL. We focus on a typical multi-server FL architecture, where the regions covered by different edge servers (ESs) may overlap. A key observation of this architecture is that clients located in the overlapping areas can access edge models from multiple ESs. Building on this insight, we propose FedOC (Federated learning with Overlapping Clients), a novel framework designed to fully exploit the potential of these overlapping clients. In FedOC, overlapping clients could serve dual roles: (1) as Relay Overlapping Clients (ROCs), they forward edge models between neighboring ESs in real time to facilitate model sharing among different ESs; and (2) as Normal Overlapping Clients (NOCs), they dynamically select their initial model for local training based on the edge model delivery time, which enables indirect data fusion among different regions of ESs. The overall FedOC workflow proceeds as follows: in every round, each client trains local model based on the earliest received edge model and transmits to the respective ESs for model aggregation. Then each ES transmits the aggregated edge model to neighboring ESs through ROC relaying. Upon receiving the relayed models, each ES performs a second aggregation and subsequently broadcasts the updated model to covered clients. The existence of ROCs enables the model of each ES to be disseminated to the other ESs in a decentralized manner, which indirectly achieves intercell model and speeding up the training process, making it well-suited for latency-sensitive edge environments. Extensive experimental results show remarkable performance gains of our scheme compared to existing methods.

## 📝 요약

다중 서버 연합 학습(FL)은 단일 서버 FL의 통신 병목 문제를 해결하기 위한 유망한 솔루션으로 부상하고 있습니다. 이 논문에서는 여러 엣지 서버(ES)가 서로 겹치는 영역을 커버하는 다중 서버 FL 아키텍처를 다룹니다. 이 구조에서 중첩된 영역에 위치한 클라이언트는 여러 ES의 엣지 모델에 접근할 수 있습니다. 이를 기반으로, 우리는 중첩 클라이언트를 최대한 활용하는 FedOC(Federated learning with Overlapping Clients)이라는 새로운 프레임워크를 제안합니다. FedOC에서 중첩 클라이언트는 두 가지 역할을 수행할 수 있습니다: (1) 릴레이 중첩 클라이언트(ROC)로서 인접한 ES 간의 모델 공유를 실시간으로 중계하고, (2) 일반 중첩 클라이언트(NOC)로서 엣지 모델 전달 시간을 기반으로 초기 모델을 선택하여 지역 간 간접적인 데이터 융합을 가능하게 합니다. FedOC의 전체 워크플로는 각 라운드에서 클라이언트가 가장 먼저 받은 엣지 모델로 로컬 모델을 훈련하고 이를 ES에 전송하여 모델을 집계하는 방식으로 진행됩니다. 이후 각 ES는 ROC 중계를 통해 인접 ES에 집계된 모델을 전송하고, 수신된 모델을 다시 집계하여 업데이트된 모델을 클라이언트에게 방송합니다. ROC의 존재는 각 ES의 모델을 탈중앙화 방식으로 다른 ES에 전파하여, 셀 간 모델 공유를 간접적으로 달성하고 훈련 과정을 가속화하여 지연에 민감한 엣지 환경에 적합합니다. 광범위한 실험 결과, 제안된 방법이 기존 방법에 비해 뛰어난 성능 향상을 보여줍니다.

## 🎯 주요 포인트

- 1. 다중 서버 연합 학습(FL)은 단일 서버 FL의 통신 병목 문제를 완화하는 유망한 솔루션으로 부상하고 있습니다.
- 2. FedOC는 중첩된 클라이언트를 최대한 활용하기 위해 설계된 새로운 프레임워크로, 클라이언트가 중첩 영역에서 여러 엣지 서버(ES)의 모델에 접근할 수 있는 점을 활용합니다.
- 3. FedOC에서 중첩 클라이언트는 릴레이 중첩 클라이언트(ROC)와 일반 중첩 클라이언트(NOC)로서의 이중 역할을 수행할 수 있습니다.
- 4. ROC는 인접한 ES 간의 모델 공유를 촉진하기 위해 엣지 모델을 실시간으로 전달하며, NOC는 엣지 모델 전달 시간을 기반으로 초기 모델을 선택하여 지역 간 간접 데이터 융합을 가능하게 합니다.
- 5. 실험 결과, FedOC는 기존 방법에 비해 뛰어난 성능 향상을 보여주며, 지연에 민감한 엣지 환경에 적합합니다.


---

*Generated on 2025-09-25 15:34:21*