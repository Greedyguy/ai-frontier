---
keywords:
  - Version Age-of-Information
  - Gossip Networks
  - Stochastic Hybrid System
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15184
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:18:19.457585",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Version Age-of-Information",
    "Gossip Networks",
    "Stochastic Hybrid System"
  ],
  "rejected_keywords": [
    "Contact Mobility",
    "Optimization"
  ],
  "similarity_scores": {
    "Version Age-of-Information": 0.78,
    "Gossip Networks": 0.72,
    "Stochastic Hybrid System": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Version Age of Information with Contact Mobility in Gossip Networks

**Korean Title:** 정보 버전 연령과 가십 네트워크에서의 접촉 이동성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Stochastic Hybrid System|Stochastic Hybrid System]]
**⚡ Unique Technical**: [[keywords/Version Age-of-Information|Version Age-of-Information]], [[keywords/Gossip Networks|Gossip Networks]]

## 🔗 유사한 논문
- [[Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks_20250917|Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks]] (78.8% similar)
- [[Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (78.1% similar)
- [[Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (76.0% similar)
- [[GraphTorque Torque-Driven Rewiring Graph Neural Network]] (75.3% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (75.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15184v1 Announce Type: cross 
Abstract: A gossip network is considered in which a source node updates its status while other nodes in the network aim at keeping track of it as it varies over time. Information gets disseminated by the source sending status updates to the nodes, and the nodes gossiping with each other. In addition, the nodes in the network are mobile, and can move to other nodes to get information, which we term contact mobility. The goal for the nodes is to remain as fresh as possible, i.e., to have the same information as the source's. To evaluate the freshness of information, we use the Version Age-of-Information (VAoI) metric, defined as the difference between the version of information available at a given node and that at the source. We analyze the effect of contact mobility on information dissemination in the gossip network using a Stochastic Hybrid System (SHS) framework for different topologies and mobility scalings with increasing number of nodes. It is shown that with the presence of contact mobility the freshness of the network improves in both ends of the network connectivity spectrum: disconnected and fully connected gossip networks. We mathematically analyze the average version age scalings and validate our theoretical results via simulations. Finally, we incorporate the cost of mobility for the network by formulating and solving an optimization problem that minimizes a weighted sum of version age and mobility cost. Our results show that contact mobility, with optimized mobility cost, improves the average version age in the network.

## 🔍 Abstract (한글 번역)

arXiv:2509.15184v1 발표 유형: 교차  
초록: 소스 노드가 상태를 업데이트하고 네트워크의 다른 노드들이 시간이 지남에 따라 이를 추적하려고 하는 가십 네트워크를 고려한다. 정보는 소스가 노드들에게 상태 업데이트를 보내고, 노드들이 서로 가십을 통해 정보를 전달함으로써 전파된다. 또한, 네트워크의 노드들은 이동성이 있으며, 정보를 얻기 위해 다른 노드로 이동할 수 있는데, 이를 접촉 이동성(contact mobility)이라고 한다. 노드들의 목표는 가능한 한 최신 상태를 유지하는 것으로, 즉 소스와 동일한 정보를 갖는 것이다. 정보의 신선도를 평가하기 위해, 주어진 노드에서 이용 가능한 정보의 버전과 소스에서의 버전 간의 차이로 정의되는 버전 정보 연령(Version Age-of-Information, VAoI) 지표를 사용한다. 우리는 서로 다른 토폴로지와 노드 수 증가에 따른 이동성 확장을 통해 가십 네트워크에서 접촉 이동성이 정보 전파에 미치는 영향을 확률적 하이브리드 시스템(Stochastic Hybrid System, SHS) 프레임워크를 사용하여 분석한다. 접촉 이동성이 존재할 때 네트워크의 신선도가 네트워크 연결성 스펙트럼의 양 끝단, 즉 단절된 가십 네트워크와 완전히 연결된 가십 네트워크 모두에서 향상됨을 보인다. 우리는 평균 버전 연령 확장을 수학적으로 분석하고, 시뮬레이션을 통해 우리의 이론적 결과를 검증한다. 마지막으로, 버전 연령과 이동성 비용의 가중 합을 최소화하는 최적화 문제를 수립하고 해결함으로써 네트워크의 이동성 비용을 통합한다. 우리의 결과는 최적화된 이동성 비용과 함께 접촉 이동성이 네트워크의 평균 버전 연령을 개선함을 보여준다.

## 📝 요약

이 논문은 소스 노드가 상태 업데이트를 수행하고, 다른 노드들이 이를 추적하는 가십 네트워크를 다룹니다. 노드들은 서로 정보를 교환하며, 이동성을 활용해 다른 노드로 이동하여 정보를 얻습니다. 정보의 신선도를 평가하기 위해 Version Age-of-Information (VAoI) 지표를 사용하며, 이는 특정 노드의 정보 버전과 소스의 정보 버전 간의 차이를 나타냅니다. Stochastic Hybrid System (SHS) 프레임워크를 통해 다양한 네트워크 토폴로지와 이동성 스케일링에서 접촉 이동성이 정보 전파에 미치는 영향을 분석했습니다. 연구 결과, 접촉 이동성이 있는 경우 네트워크의 신선도가 향상되며, 이는 연결되지 않은 네트워크와 완전히 연결된 네트워크 모두에서 나타났습니다. 또한, 이동성 비용을 고려한 최적화 문제를 해결하여, 이동성 비용이 최적화된 상태에서 네트워크의 평균 버전 연령이 개선됨을 확인했습니다.

## 🎯 주요 포인트

- 1. 소스 노드가 상태 업데이트를 수행하고 다른 노드들이 이를 추적하는 가십 네트워크를 연구합니다.

- 2. 네트워크 내 노드들은 이동성을 통해 다른 노드로 이동하여 정보를 얻을 수 있으며, 이를 '접촉 이동성'이라 정의합니다.

- 3. 정보의 신선도를 평가하기 위해 정보의 버전 차이를 나타내는 VAoI(Version Age-of-Information) 지표를 사용합니다.

- 4. 접촉 이동성이 네트워크의 정보 신선도를 향상시키며, 이는 네트워크 연결성 스펙트럼의 양 끝단에서 특히 두드러집니다.

- 5. 이동성 비용을 최적화하여 네트워크의 평균 버전 연령을 개선하는 최적화 문제를 해결합니다.

---

*Generated on 2025-09-19 16:28:02*