# DiRW: Path-Aware Digraph Learning for Heterophily

**Korean Title:** 이질성을 위한 경로 인식 유향 그래프 학습: DiRW

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Path Aware Digraph Learning

## 🔗 유사한 논문
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (83.5% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (82.5% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (81.7% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation A Robustness Analysis]] (80.6% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.10320v3 Announce Type: replace-cross 
Abstract: Recently, graph neural network (GNN) has emerged as a powerful representation learning tool for graph-structured data. However, most approaches are tailored for undirected graphs, neglecting the abundant information in the edges of directed graphs (digraphs). In fact, digraphs are widely applied in the real world and confirmed to address heterophily challenges. Despite recent advancements, existing spatial- and spectral-based DiGNNs have limitations due to their complex learning mechanisms and reliance on high-quality topology, resulting in low efficiency and unstable performance. To address these issues, we propose Directed Random Walk (DiRW), a plug-and-play strategy for most spatial-based DiGNNs and also an innovative model which offers a new digraph learning paradigm. Specifically, it utilizes a direction-aware path sampler optimized from the perspectives of walk probability, length, and number in a weight-free manner by considering node profiles and topologies. Building upon this, DiRW incorporates a node-wise learnable path aggregator for generalized node representations. Extensive experiments on 9 datasets demonstrate that DiRW: (1) enhances most spatial-based methods as a plug-and-play strategy; (2) achieves SOTA performance as a new digraph learning paradigm. The source code and data are available at https://github.com/dhsiuu/DiRW.

## 🔍 Abstract (한글 번역)

arXiv:2410.10320v3 발표 유형: 교체-교차  
초록: 최근 그래프 신경망(GNN)은 그래프 구조 데이터를 위한 강력한 표현 학습 도구로 부상했습니다. 그러나 대부분의 접근법은 무방향 그래프에 맞춰져 있으며, 방향 그래프(디그래프)의 간선에 있는 풍부한 정보를 간과하고 있습니다. 사실, 디그래프는 실제 세계에서 널리 적용되며 이질성 문제를 해결하는 데 효과적임이 확인되었습니다. 최근의 발전에도 불구하고, 기존의 공간 기반 및 스펙트럼 기반 DiGNN은 복잡한 학습 메커니즘과 고품질 토폴로지에 대한 의존성으로 인해 효율성이 낮고 성능이 불안정한 한계를 가지고 있습니다. 이러한 문제를 해결하기 위해, 우리는 대부분의 공간 기반 DiGNN에 플러그 앤 플레이 전략으로 사용할 수 있는 Directed Random Walk (DiRW)와 새로운 디그래프 학습 패러다임을 제공하는 혁신적인 모델을 제안합니다. 구체적으로, DiRW는 노드 프로필과 토폴로지를 고려하여 방향 인식 경로 샘플러를 사용하며, 이는 경로 확률, 길이 및 수의 관점에서 최적화된 무가중치 방식입니다. 이를 바탕으로, DiRW는 일반화된 노드 표현을 위한 노드별 학습 가능한 경로 집계기를 통합합니다. 9개의 데이터셋에 대한 광범위한 실험 결과, DiRW는 (1) 대부분의 공간 기반 방법을 플러그 앤 플레이 전략으로 강화하며; (2) 새로운 디그래프 학습 패러다임으로서 SOTA 성능을 달성합니다. 소스 코드와 데이터는 https://github.com/dhsiuu/DiRW에서 사용할 수 있습니다.

## 📝 요약

최근 그래프 신경망(GNN)은 그래프 구조 데이터를 위한 강력한 표현 학습 도구로 부상했지만, 대부분의 접근법은 무방향 그래프에 맞춰져 있어 방향 그래프(digraph)의 풍부한 정보를 간과하고 있습니다. 이러한 문제를 해결하기 위해, 우리는 Directed Random Walk (DiRW)를 제안합니다. DiRW는 대부분의 공간 기반 DiGNN에 적용 가능한 플러그 앤 플레이 전략이자 혁신적인 모델로, 방향 인식 경로 샘플러를 활용하여 노드 프로필과 토폴로지를 고려한 무게 없는 방식으로 최적화합니다. 이를 기반으로 노드별 학습 가능한 경로 집계기를 포함하여 일반화된 노드 표현을 제공합니다. 9개의 데이터셋에 대한 실험 결과, DiRW는 대부분의 공간 기반 방법을 향상시키고, 새로운 방향 그래프 학습 패러다임으로서 SOTA 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN)은 그래프 구조 데이터의 표현 학습 도구로 부상했지만, 대부분의 접근법은 무방향 그래프에 맞춰져 있어 방향 그래프의 풍부한 정보를 간과하고 있다.

- 2. 방향 그래프는 이질성 문제를 해결하는 데 효과적이며, 실제 세계에서 널리 사용된다.

- 3. 기존의 공간 및 스펙트럼 기반 DiGNN은 복잡한 학습 메커니즘과 고품질 토폴로지에 대한 의존성으로 인해 효율성이 낮고 성능이 불안정하다.

- 4. DiRW는 대부분의 공간 기반 DiGNN에 적용 가능한 플러그 앤 플레이 전략이며, 새로운 방향 그래프 학습 패러다임을 제공하는 혁신적인 모델이다.

- 5. DiRW는 9개의 데이터셋에서 광범위한 실험을 통해 대부분의 공간 기반 방법을 향상시키고, 새로운 방향 그래프 학습 패러다임으로서 SOTA 성능을 달성했다.

---

*Generated on 2025-09-22 14:38:54*