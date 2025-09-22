
# Federated Hypergraph Learning with Local Differential Privacy: Toward Privacy-Aware Hypergraph Structure Completion

**Korean Title:** 로컬 차등 프라이버시를 활용한 연합 하이퍼그래프 학습: 프라이버시 인식 하이퍼그래프 구조 완성을 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Federated Hypergraph Learning

## 🔗 유사한 논문
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (80.1% similar)
- [[FedDiverse Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection]] (79.9% similar)
- [[FedSSG Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (79.9% similar)
- [[Hierarchical_Federated_Learning_for_Social_Network_with_Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (79.6% similar)
- [[Federated Learning for Deforestation Detection A Distributed Approach with Satellite Imagery]] (78.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.05160v3 Announce Type: replace 
Abstract: The rapid growth of graph-structured data necessitates partitioning and distributed storage across decentralized systems, driving the emergence of federated graph learning to collaboratively train Graph Neural Networks (GNNs) without compromising privacy. However, current methods exhibit limited performance when handling hypergraphs, which inherently represent complex high-order relationships beyond pairwise connections. Partitioning hypergraph structures across federated subsystems amplifies structural complexity, hindering high-order information mining and compromising local information integrity. To bridge the gap between hypergraph learning and federated systems, we develop FedHGL, a first-of-its-kind framework for federated hypergraph learning on disjoint and privacy-constrained hypergraph partitions. Beyond collaboratively training a comprehensive hypergraph neural network across multiple clients, FedHGL introduces a pre-propagation hyperedge completion mechanism to preserve high-order structural integrity within each client. This procedure leverages the federated central server to perform cross-client hypergraph convolution without exposing internal topological information, effectively mitigating the high-order information loss induced by subgraph partitioning. Furthermore, by incorporating two kinds of local differential privacy (LDP) mechanisms, we provide formal privacy guarantees for this process, ensuring that sensitive node features remain protected against inference attacks from potentially malicious servers or clients. Experimental results on seven real-world datasets confirm the effectiveness of our approach and demonstrate its performance advantages over traditional federated graph learning methods.

## 🔍 Abstract (한글 번역)

arXiv:2408.05160v3 발표 유형: 교체  
초록: 그래프 구조 데이터를 빠르게 처리하기 위해 분할 및 분산 저장이 필요하며, 이는 프라이버시를 침해하지 않고 협력적으로 그래프 신경망(GNN)을 훈련할 수 있는 연합 그래프 학습의 등장을 촉진합니다. 그러나 현재의 방법들은 쌍 연결을 넘어 복잡한 고차 관계를 본질적으로 나타내는 하이퍼그래프를 처리할 때 제한된 성능을 보입니다. 연합 하위 시스템 간에 하이퍼그래프 구조를 분할하면 구조적 복잡성이 증가하여 고차 정보 채굴이 어려워지고, 지역 정보의 무결성이 손상됩니다. 하이퍼그래프 학습과 연합 시스템 간의 간극을 해소하기 위해, 우리는 분리되고 프라이버시가 제한된 하이퍼그래프 분할에서 연합 하이퍼그래프 학습을 위한 최초의 프레임워크인 FedHGL을 개발했습니다. 여러 클라이언트에 걸쳐 포괄적인 하이퍼그래프 신경망을 협력적으로 훈련하는 것을 넘어, FedHGL은 각 클라이언트 내에서 고차 구조적 무결성을 유지하기 위한 사전 전파 하이퍼엣지 완성 메커니즘을 도입합니다. 이 절차는 연합 중앙 서버를 활용하여 내부 토폴로지 정보를 노출하지 않고 클라이언트 간 하이퍼그래프 합성을 수행하여, 서브그래프 분할로 인한 고차 정보 손실을 효과적으로 완화합니다. 또한, 두 가지 유형의 로컬 차등 프라이버시(LDP) 메커니즘을 통합하여, 잠재적으로 악의적인 서버나 클라이언트로부터의 추론 공격에 대해 민감한 노드 특징이 보호되도록 공식적인 프라이버시 보장을 제공합니다. 7개의 실제 데이터셋에 대한 실험 결과는 우리의 접근 방식의 효과를 확인하고, 전통적인 연합 그래프 학습 방법에 비해 성능상의 이점을 보여줍니다.

## 📝 요약

이 논문은 분산 시스템에서 그래프 구조 데이터를 처리하기 위한 연합 그래프 학습의 필요성을 강조하며, 특히 고차원 관계를 표현하는 하이퍼그래프에 대한 기존 방법의 한계를 지적합니다. 이를 해결하기 위해, 저자들은 FedHGL이라는 새로운 프레임워크를 제안합니다. FedHGL은 분리된 하이퍼그래프 파티션에서 프라이버시를 유지하면서 연합 하이퍼그래프 학습을 수행합니다. 이 프레임워크는 클라이언트 간 하이퍼그래프 컨볼루션을 통해 고차원 구조의 완전성을 유지하며, 두 가지 로컬 차등 프라이버시 메커니즘을 도입하여 민감한 노드 특징을 보호합니다. 실험 결과, 제안된 방법이 기존의 연합 그래프 학습 방법보다 우수한 성능을 보임을 확인했습니다.

## 🎯 주요 포인트

- 1. FedHGL은 분산된 하이퍼그래프 파티션에서 프라이버시를 보장하면서 협력적으로 하이퍼그래프 신경망을 학습하는 최초의 프레임워크입니다.

- 2. FedHGL은 클라이언트 간 하이퍼그래프 컨볼루션을 수행하여 하이퍼엣지 완성 메커니즘을 도입, 각 클라이언트 내에서 고차 구조적 무결성을 유지합니다.

- 3. 두 가지 종류의 로컬 차등 프라이버시(LDP) 메커니즘을 통해 민감한 노드 특징이 잠재적으로 악의적인 서버나 클라이언트의 추론 공격으로부터 보호됩니다.

- 4. 실험 결과, FedHGL은 기존의 연합 그래프 학습 방법에 비해 성능상의 이점을 보여주며, 7개의 실제 데이터셋에서 그 효과가 입증되었습니다.

- 5. 하이퍼그래프 구조의 분할은 구조적 복잡성을 증대시키고, 고차 정보 손실을 유발하지만, FedHGL은 이를 효과적으로 완화합니다.

---

*Generated on 2025-09-19 15:38:09*