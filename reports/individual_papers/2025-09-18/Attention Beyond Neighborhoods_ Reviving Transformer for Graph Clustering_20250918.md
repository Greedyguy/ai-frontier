# Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering

**Korean Title:** 이웃을 넘어선 주의: 그래프 클러스터링을 위한 트랜스포머의 부활

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Xuanting Xie|Xuanting Xie]] [[authors/Bingheng Li|Bingheng Li]] [[authors/Erlin Pan|Erlin Pan]] [[authors/Rui Hou|Rui Hou]] [[authors/Wenyu Chen|Wenyu Chen]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Attention Mechanism, Graph Neural Network

## 🔗 유사한 논문
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (84.3% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (83.4% similar)
- [[Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community Guiding the Fairness of Graphs via New Links]] (80.7% similar)
- [[Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (80.1% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (79.8% similar)

## 📋 저자 정보

**Authors:** Xuanting Xie, Bingheng Li, Erlin Pan, Rui Hou, Wenyu Chen, Zhao Kang

## 📄 Abstract (원문)

Attention mechanisms have become a cornerstone in modern neural networks,
driving breakthroughs across diverse domains. However, their application to
graph structured data, where capturing topological connections is essential,
remains underexplored and underperforming compared to Graph Neural Networks
(GNNs), particularly in the graph clustering task. GNN tends to overemphasize
neighborhood aggregation, leading to a homogenization of node representations.
Conversely, Transformer tends to over globalize, highlighting distant nodes at
the expense of meaningful local patterns. This dichotomy raises a key question:
Is attention inherently redundant for unsupervised graph learning? To address
this, we conduct a comprehensive empirical analysis, uncovering the
complementary weaknesses of GNN and Transformer in graph clustering. Motivated
by these insights, we propose the Attentive Graph Clustering Network (AGCN) a
novel architecture that reinterprets the notion that graph is attention. AGCN
directly embeds the attention mechanism into the graph structure, enabling
effective global information extraction while maintaining sensitivity to local
topological cues. Our framework incorporates theoretical analysis to contrast
AGCN behavior with GNN and Transformer and introduces two innovations: (1) a KV
cache mechanism to improve computational efficiency, and (2) a pairwise margin
contrastive loss to boost the discriminative capacity of the attention space.
Extensive experimental results demonstrate that AGCN outperforms
state-of-the-art methods.

## 🔍 Abstract (한글 번역)

주의 메커니즘은 현대 신경망의 초석이 되어 다양한 분야에서 획기적인 발전을 이끌어왔습니다. 그러나, 그래프 구조 데이터를 다루는 데 있어, 특히 그래프 클러스터링 작업에서, 그래프 신경망(GNN)과 비교하여 그 적용이 충분히 탐구되지 않았고 성능이 부족한 상황입니다. GNN은 이웃 집합의 집계를 과도하게 강조하는 경향이 있어 노드 표현의 동질화를 초래합니다. 반면, Transformer는 전역화를 과도하게 진행하여 의미 있는 지역 패턴을 희생하면서 먼 노드를 강조합니다. 이러한 이분법은 주의를 기울이는 것이 비지도 그래프 학습에 본질적으로 불필요한가라는 중요한 질문을 제기합니다. 이를 해결하기 위해, 우리는 GNN과 Transformer의 그래프 클러스터링에서의 상호 보완적인 약점을 밝혀내는 포괄적인 실증 분석을 수행합니다. 이러한 통찰에 영감을 받아, 우리는 그래프가 주의라는 개념을 재해석한 새로운 아키텍처인 주의 그래프 클러스터링 네트워크(AGCN)를 제안합니다. AGCN은 주의 메커니즘을 그래프 구조에 직접 내장하여, 지역적 위상 신호에 대한 민감성을 유지하면서도 효과적인 전역 정보 추출을 가능하게 합니다. 우리의 프레임워크는 AGCN의 행동을 GNN 및 Transformer와 비교하는 이론적 분석을 포함하며, 두 가지 혁신을 도입합니다: (1) 계산 효율성을 개선하기 위한 KV 캐시 메커니즘, (2) 주의 공간의 판별력을 향상시키기 위한 쌍별 마진 대조 손실. 광범위한 실험 결과는 AGCN이 최신 방법들을 능가함을 보여줍니다.

## 📝 요약

본 논문은 그래프 구조 데이터에 대한 주의 메커니즘의 활용을 탐구하며, 그래프 클러스터링 작업에서의 한계를 지적합니다. 기존의 그래프 신경망(GNN)은 이웃 집합에 과도하게 집중하여 노드 표현의 균질화를 초래하고, 트랜스포머는 전역 정보를 강조하여 지역적 패턴을 놓치는 문제를 가지고 있습니다. 이러한 문제를 해결하기 위해, 저자들은 GNN과 트랜스포머의 상호 보완적 약점을 분석하고, 주의 메커니즘을 그래프 구조에 직접 통합한 새로운 아키텍처인 Attentive Graph Clustering Network (AGCN)을 제안합니다. AGCN은 전역 정보 추출과 지역적 토폴로지 감도를 동시에 유지하며, KV 캐시 메커니즘과 쌍별 마진 대조 손실을 도입하여 계산 효율성과 주의 공간의 변별력을 향상시킵니다. 실험 결과, AGCN은 최신 기법들을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 주의 메커니즘은 그래프 구조 데이터에 대한 적용이 미흡하며, 특히 그래프 클러스터링 작업에서 GNN에 비해 성능이 떨어진다.

- 2. GNN은 이웃 집합의 과도한 집계로 노드 표현의 동질화를 초래하며, Transformer는 전역화로 인해 지역 패턴을 간과한다.

- 3. AGCN은 그래프 구조에 주의 메커니즘을 직접 내장하여 전역 정보 추출과 지역 위상 신호에 대한 민감성을 유지한다.

- 4. AGCN은 계산 효율성을 높이는 KV 캐시 메커니즘과 주의 공간의 변별력을 강화하는 쌍별 마진 대조 손실을 도입한다.

- 5. 실험 결과, AGCN은 최신 기법들을 능가하는 성능을 보여준다.

---

*Generated on 2025-09-20 01:11:16*