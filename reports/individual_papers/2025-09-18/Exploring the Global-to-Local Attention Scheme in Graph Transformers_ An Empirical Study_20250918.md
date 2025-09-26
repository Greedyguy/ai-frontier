---
keywords:
  - Graph Neural Networks
  - Attention Mechanism
  - Transformer Architecture
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:29:10.153494",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Attention Mechanism",
    "Transformer Architecture"
  ],
  "rejected_keywords": [
    "Global-to-Local Attention Scheme"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.85,
    "Attention Mechanism": 0.82,
    "Transformer Architecture": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Exploring the Global-to-Local Attention Scheme in Graph Transformers: An Empirical Study

**Korean Title:** 그래프 변환기에서의 글로벌-로컬 주의 메커니즘 탐구: 실증적 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Transformer Architecture|Graph Transformers]]

## 🔗 유사한 논문
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (86.9% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (80.3% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (79.3% similar)
- [[Soft Graph Transformer for MIMO Detection_20250918|Soft Graph Transformer for MIMO Detection]] (79.1% similar)
- [[Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy Toward Privacy-Aware Hypergraph Structure Completion]] (77.4% similar)

## 📋 저자 정보

**Authors:** Zhengwei Wang, Gang Wu

## 📄 Abstract (원문)

Graph Transformers (GTs) show considerable potential in graph representation
learning. The architecture of GTs typically integrates Graph Neural Networks
(GNNs) with global attention mechanisms either in parallel or as a precursor to
attention mechanisms, yielding a local-and-global or local-to-global attention
scheme. However, as the global attention mechanism primarily captures
long-range dependencies between nodes, these integration schemes may suffer
from information loss, where the local neighborhood information learned by GNN
could be diluted by the attention mechanism. Therefore, we propose G2LFormer,
featuring a novel global-to-local attention scheme where the shallow network
layers use attention mechanisms to capture global information, while the deeper
layers employ GNN modules to learn local structural information, thereby
preventing nodes from ignoring their immediate neighbors. An effective
cross-layer information fusion strategy is introduced to allow local layers to
retain beneficial information from global layers and alleviate information
loss, with acceptable trade-offs in scalability. To validate the feasibility of
the global-to-local attention scheme, we compare G2LFormer with
state-of-the-art linear GTs and GNNs on node-level and graph-level tasks. The
results indicate that G2LFormer exhibits excellent performance while keeping
linear complexity.

## 🔍 Abstract (한글 번역)

그래프 변환기(Graph Transformers, GTs)는 그래프 표현 학습에서 상당한 잠재력을 보여줍니다. GT의 아키텍처는 일반적으로 그래프 신경망(Graph Neural Networks, GNNs)과 전역 주의 메커니즘을 병렬로 또는 주의 메커니즘의 전 단계로 통합하여 로컬 및 글로벌 또는 로컬에서 글로벌로의 주의 체계를 형성합니다. 그러나 전역 주의 메커니즘이 주로 노드 간의 장거리 종속성을 포착하기 때문에, 이러한 통합 체계는 GNN이 학습한 로컬 이웃 정보가 주의 메커니즘에 의해 희석될 수 있는 정보 손실을 겪을 수 있습니다. 따라서 우리는 G2LFormer를 제안합니다. 이는 얕은 네트워크 계층이 주의 메커니즘을 사용하여 글로벌 정보를 포착하고, 더 깊은 계층은 GNN 모듈을 사용하여 로컬 구조 정보를 학습하는 새로운 글로벌에서 로컬로의 주의 체계를 특징으로 하여 노드가 즉각적인 이웃을 무시하지 않도록 합니다. 효과적인 계층 간 정보 융합 전략이 도입되어 로컬 계층이 글로벌 계층에서 유익한 정보를 유지하고 정보 손실을 완화하며, 확장성에서 수용 가능한 절충을 제공합니다. 글로벌에서 로컬로의 주의 체계의 타당성을 검증하기 위해, 우리는 G2LFormer를 최첨단 선형 GT 및 GNN과 노드 수준 및 그래프 수준 작업에서 비교합니다. 결과는 G2LFormer가 선형 복잡성을 유지하면서 우수한 성능을 보임을 나타냅니다.

## 📝 요약

Graph Transformers(GTs)는 그래프 표현 학습에서 잠재력을 보이지만, 기존의 GT 구조는 정보 손실 문제를 겪을 수 있습니다. 이를 해결하기 위해, 우리는 새로운 글로벌-투-로컬 주의 메커니즘을 갖춘 G2LFormer를 제안합니다. 얕은 네트워크 층에서는 주의 메커니즘을 사용해 글로벌 정보를 포착하고, 깊은 층에서는 GNN 모듈을 사용해 지역 구조 정보를 학습하여 노드가 인접 이웃을 무시하지 않도록 합니다. 또한, 효과적인 층 간 정보 융합 전략을 도입하여 지역 층이 글로벌 층의 유익한 정보를 유지하도록 하였습니다. G2LFormer는 노드 및 그래프 수준의 작업에서 기존의 GTs 및 GNNs와 비교하여 우수한 성능을 보이며, 선형 복잡성을 유지합니다.

## 🎯 주요 포인트

- 1. Graph Transformers는 그래프 표현 학습에서 큰 잠재력을 보여주며, 주로 GNN과 글로벌 주의 메커니즘을 통합하여 지역 및 글로벌 주의 체계를 형성합니다.

- 2. 기존의 통합 방식은 글로벌 주의 메커니즘이 노드 간 장거리 의존성을 주로 포착하여 정보 손실을 초래할 수 있습니다.

- 3. G2LFormer는 얕은 네트워크 층에서 글로벌 정보를 포착하고, 깊은 층에서 GNN 모듈을 사용하여 지역 구조 정보를 학습하는 글로벌-투-로컬 주의 체계를 제안합니다.

- 4. 효과적인 층 간 정보 융합 전략을 통해 지역 층이 글로벌 층의 유익한 정보를 유지하고 정보 손실을 완화합니다.

- 5. G2LFormer는 최첨단 선형 GT 및 GNN과 비교하여 노드 및 그래프 수준 작업에서 뛰어난 성능을 보이며, 선형 복잡성을 유지합니다.

---

*Generated on 2025-09-20 02:46:26*