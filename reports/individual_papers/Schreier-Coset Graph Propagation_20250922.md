# Schreier-Coset Graph Propagation

**Korean Title:** 슈라이어-코셋 그래프 전파

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Bottleneck-Free Connectivity

## 🔗 유사한 논문
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (85.6% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (85.3% similar)
- [[2025-09-18/Towards Pre-trained Graph Condensation via Optimal Transport_20250918|Towards Pre-trained Graph Condensation via Optimal Transport]] (84.3% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (82.9% similar)
- [[2025-09-22/DiRW_ Path-Aware Digraph Learning for Heterophily_20250922|DiRW Path-Aware Digraph Learning for Heterophily]] (82.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10392v2 Announce Type: replace-cross 
Abstract: Graph Neural Networks (GNNs) offer a principled framework for learning over graph-structured data, yet their expressive capacity is often hindered by over-squashing, wherein information from distant nodes is compressed into fixed-size vectors. Existing solutions, including graph rewiring and bottleneck-resistant architectures such as Cayley and expander graphs, avoid this problem but introduce scalability bottlenecks. In particular, the Cayley graphs constructed over $SL(2,\mathbb{Z}_n)$ exhibit strong theoretical properties, yet suffer from cubic node growth $O(n^3)$, leading to high memory usage. To address this, this work introduces Schrier-Coset Graph Propagation (SCGP), a group-theoretic augmentation method that enriches node features through Schreier-coset embeddings without altering the input graph topology. SCGP embeds bottleneck-free connectivity patterns into a compact feature space, improving long-range message passing while maintaining computational efficiency. Empirical evaluations across standard node and graph classification benchmarks demonstrate that SCGP achieves performance comparable to, or exceeding, expander graph and rewired GNN baselines. Furthermore, SCGP exhibits particular advantages in processing hierarchical and modular graph structures, offering reduced inference latency, improved scalability, and a low memory footprint, making it suitable for real-time and resource-constrained applications.

## 🔍 Abstract (한글 번역)

arXiv:2505.10392v2 발표 유형: 교체-교차  
초록: 그래프 신경망(GNNs)은 그래프 구조 데이터를 학습하기 위한 체계적인 프레임워크를 제공하지만, 종종 먼 노드로부터의 정보가 고정 크기 벡터로 압축되는 과도한 압축(over-squashing)으로 인해 표현력이 제한됩니다. 그래프 재배선 및 Cayley 그래프와 확장자 그래프와 같은 병목 저항 아키텍처를 포함한 기존 솔루션은 이 문제를 피하지만 확장성 병목을 초래합니다. 특히, $SL(2,\mathbb{Z}_n)$ 위에 구성된 Cayley 그래프는 강력한 이론적 특성을 보이지만, 노드의 세제곱 성장 $O(n^3)$으로 인해 높은 메모리 사용량을 초래합니다. 이를 해결하기 위해, 본 연구는 입력 그래프의 토폴로지를 변경하지 않고 Schreier-코셋 임베딩을 통해 노드 특성을 풍부하게 하는 군 이론적 증강 방법인 Schrier-Coset Graph Propagation (SCGP)을 소개합니다. SCGP는 병목 없는 연결 패턴을 압축된 특성 공간에 임베딩하여 장거리 메시지 전달을 개선하면서도 계산 효율성을 유지합니다. 표준 노드 및 그래프 분류 벤치마크에 대한 실증적 평가 결과, SCGP는 확장자 그래프 및 재배선된 GNN 기준선과 동등하거나 그 이상의 성능을 달성함을 보여줍니다. 또한, SCGP는 계층적 및 모듈형 그래프 구조를 처리하는 데 있어 특히 이점을 제공하며, 추론 지연 감소, 확장성 개선, 낮은 메모리 사용량을 제공하여 실시간 및 자원 제약이 있는 응용 프로그램에 적합합니다.

## 📝 요약

이 논문은 그래프 신경망(GNN)의 표현력을 제한하는 정보 압축 문제를 해결하기 위해 Schrier-Coset Graph Propagation(SCGP) 방법을 제안합니다. 기존의 Cayley 그래프와 확장 그래프는 이 문제를 피하지만 확장성에 제약이 있습니다. SCGP는 Schreier-coset 임베딩을 통해 입력 그래프의 구조를 변경하지 않고 노드 특징을 강화하여 장거리 메시지 전달을 개선합니다. 실험 결과, SCGP는 기존의 확장 그래프와 리와이어링된 GNN과 비교해 성능이 동등하거나 우수하며, 계층적 및 모듈형 그래프 구조 처리에서 특히 장점을 보입니다. 이는 실시간 및 자원 제약 환경에 적합한 낮은 메모리 사용량과 향상된 확장성을 제공합니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN)의 표현력은 종종 먼 노드의 정보가 고정 크기 벡터로 압축되는 오버 스쿼싱 문제로 제한됩니다.

- 2. Cayley 그래프는 이론적으로 강력한 특성을 가지지만, 노드의 기하급수적 증가로 인해 높은 메모리 사용량을 초래합니다.

- 3. Schrier-Coset Graph Propagation(SCGP)는 입력 그래프의 토폴로지를 변경하지 않고 Schreier-coset 임베딩을 통해 노드 기능을 풍부하게 하는 방법을 제안합니다.

- 4. SCGP는 긴 거리 메시지 전달을 개선하면서도 계산 효율성을 유지하여, 확장 그래프 및 리와이어드 GNN 기반과 비교해 성능이 뛰어납니다.

- 5. SCGP는 계층적 및 모듈형 그래프 구조 처리에 특히 유리하며, 실시간 및 자원 제약 애플리케이션에 적합한 낮은 메모리 사용량과 향상된 확장성을 제공합니다.

---

*Generated on 2025-09-22 14:47:54*