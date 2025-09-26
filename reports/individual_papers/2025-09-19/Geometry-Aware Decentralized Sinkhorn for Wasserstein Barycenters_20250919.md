---
keywords:
  - Optimal Transport
  - Decentralized Sinkhorn Algorithm
  - Wasserstein Barycenters
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14521
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:41:40.306749",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Optimal Transport",
    "Decentralized Sinkhorn Algorithm",
    "Wasserstein Barycenters"
  ],
  "rejected_keywords": [
    "Event-Triggered Transmissions"
  ],
  "similarity_scores": {
    "Optimal Transport": 0.8,
    "Decentralized Sinkhorn Algorithm": 0.82,
    "Wasserstein Barycenters": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters

**Korean Title:** 기하학 인식 분산 싱크혼을 이용한 바서슈타인 중심점 계산

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimal Transport|Optimal Transport]]
**⚡ Unique Technical**: [[keywords/Decentralized Sinkhorn Algorithm|Decentralized Sinkhorn Algorithm]], [[keywords/Wasserstein Barycenters|Wasserstein Barycenters]]

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (84.3% similar)
- [[Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (78.9% similar)
- [[Who to Trust_ Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (78.7% similar)
- [[Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (78.5% similar)
- [[FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14521v1 Announce Type: new 
Abstract: Distributed systems require fusing heterogeneous local probability distributions into a global summary over sparse and unreliable communication networks. Traditional consensus algorithms, which average distributions in Euclidean space, ignore their inherent geometric structure, leading to misleading results. Wasserstein barycenters offer a geometry-aware alternative by minimizing optimal transport costs, but their entropic approximations via the Sinkhorn algorithm typically require centralized coordination. This paper proposes a fully decentralized Sinkhorn algorithm that reformulates the centralized geometric mean as an arithmetic average in the log-domain, enabling approximation through local gossip protocols. Agents exchange log-messages with neighbors, interleaving consensus phases with local updates to mimic centralized iterations without a coordinator. To optimize bandwidth, we integrate event-triggered transmissions and b-bit quantization, providing tunable trade-offs between accuracy and communication while accommodating asynchrony and packet loss. Under mild assumptions, we prove convergence to a neighborhood of the centralized entropic barycenter, with bias linearly dependent on consensus tolerance, trigger threshold, and quantization error. Complexity scales near-linearly with network size. Simulations confirm near-centralized accuracy with significantly fewer messages, across various topologies and conditions.

## 🔍 Abstract (한글 번역)

arXiv:2509.14521v1 발표 유형: 신규  
초록: 분산 시스템은 희소하고 신뢰할 수 없는 통신 네트워크를 통해 이질적인 지역 확률 분포를 전역 요약으로 융합해야 합니다. 전통적인 합의 알고리즘은 유클리드 공간에서 분포를 평균화하지만, 그 고유한 기하학적 구조를 무시하여 오해를 불러일으킬 수 있습니다. Wasserstein 중심은 최적 수송 비용을 최소화하여 기하학적으로 인식된 대안을 제공하지만, Sinkhorn 알고리즘을 통한 엔트로피 근사는 일반적으로 중앙 집중식 조정을 필요로 합니다. 본 논문은 중앙 집중식 기하 평균을 로그 도메인에서 산술 평균으로 재구성하여 지역적인 소문 프로토콜을 통해 근사할 수 있는 완전 분산 Sinkhorn 알고리즘을 제안합니다. 에이전트는 이웃과 로그 메시지를 교환하며, 중앙 집중식 반복을 모방하기 위해 합의 단계와 지역 업데이트를 번갈아 수행합니다. 대역폭 최적화를 위해 이벤트 트리거 전송과 b-비트 양자화를 통합하여 정확도와 통신 간의 조정 가능한 균형을 제공하며 비동기성과 패킷 손실을 수용합니다. 약간의 가정 하에, 우리는 합의 허용 오차, 트리거 임계값 및 양자화 오류에 선형적으로 의존하는 편향을 가진 중앙 집중식 엔트로피 중심의 근방으로의 수렴을 증명합니다. 복잡성은 네트워크 크기에 따라 거의 선형적으로 확장됩니다. 시뮬레이션은 다양한 토폴로지와 조건에서 훨씬 적은 메시지로 거의 중앙 집중식 정확도를 확인합니다.

## 📝 요약

이 논문은 분산 시스템에서 이질적인 지역 확률 분포를 결합하여 신뢰할 수 없는 통신 네트워크에서 전역 요약을 생성하는 문제를 다룹니다. 전통적인 합의 알고리즘은 유클리드 공간에서 분포를 평균화하여 기하학적 구조를 무시하는 반면, Wasserstein 중심은 최적 수송 비용을 최소화하여 기하학적으로 인식된 대안을 제공합니다. 그러나 기존의 Sinkhorn 알고리즘은 중앙 집중식 조정을 필요로 합니다. 본 연구는 중앙 집중식 기하 평균을 로그 도메인에서 산술 평균으로 재구성하여 지역 가십 프로토콜을 통해 근사할 수 있는 완전 분산형 Sinkhorn 알고리즘을 제안합니다. 에이전트는 이웃과 로그 메시지를 교환하고, 합의 단계와 지역 업데이트를 교차하여 중앙 집중식 반복을 모방합니다. 대역폭 최적화를 위해 이벤트 트리거 전송 및 b-비트 양자화를 통합하여 정확성과 통신 간의 조정 가능한 균형을 제공합니다. 경미한 가정 하에, 중앙 집중식 엔트로피 중심 근처로의 수렴을 증명하며, 편향은 합의 허용 오차, 트리거 임계값 및 양자화 오류에 선형적으로 의존합니다. 복잡성은 네트워크 크기에 거의 선형적으로 확장됩니다. 시뮬레이션 결과, 다양한 토폴로지와 조건에서 중앙 집중식 정확도에 근접하면서도 메시지 수가 크게 감소함을 확인했습니다.

## 🎯 주요 포인트

- 1. 분산 시스템에서 이질적인 지역 확률 분포를 전역적으로 요약하기 위해 전통적인 합의 알고리즘의 한계를 극복하는 방법을 제안합니다.

- 2. 제안된 알고리즘은 중심화된 기하 평균을 로그 도메인에서 산술 평균으로 재구성하여 지역 가십 프로토콜을 통해 근사합니다.

- 3. 대역폭 최적화를 위해 이벤트 트리거 전송과 b-비트 양자화를 통합하여 정확도와 통신 간의 조절 가능한 균형을 제공합니다.

- 4. 제안된 알고리즘은 비동기성과 패킷 손실을 수용하면서 중앙 집중식 엔트로피 중심에 근접하게 수렴함을 증명합니다.

- 5. 시뮬레이션 결과, 다양한 토폴로지와 조건에서 중앙 집중식 정확도에 근접하면서도 메시지 수를 크게 줄일 수 있음을 확인했습니다.

---

*Generated on 2025-09-19 16:43:41*