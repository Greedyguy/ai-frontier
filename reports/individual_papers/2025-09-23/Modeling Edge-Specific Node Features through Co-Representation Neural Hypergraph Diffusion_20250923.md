---
keywords:
  - Graph Neural Network
  - Edge-Dependent Node Classification
  - Hypergraph Diffusion
  - Equivariant Networks
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2405.14286
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:38:44.011197",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Edge-Dependent Node Classification",
    "Hypergraph Diffusion",
    "Equivariant Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Edge-Dependent Node Classification": 0.8,
    "Hypergraph Diffusion": 0.75,
    "Equivariant Networks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hypergraph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "HGNN"
        ],
        "category": "specific_connectable",
        "rationale": "The paper discusses a novel architecture for hypergraph neural networks, which are a specific type of graph neural network.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Edge-Dependent Node Classification",
        "canonical": "Edge-Dependent Node Classification",
        "aliases": [
          "ENC"
        ],
        "category": "unique_technical",
        "rationale": "ENC is a specific task within hypergraph learning that requires unique modeling approaches, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hypergraph Diffusion",
        "canonical": "Hypergraph Diffusion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Hypergraph diffusion is a novel process described in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Equivariant Networks",
        "canonical": "Equivariant Networks",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Equivariant networks are used as diffusion operators in the proposed method, highlighting their technical importance.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "oversmoothing issue",
      "non-adaptive representation sizes"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hypergraph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Edge-Dependent Node Classification",
      "resolved_canonical": "Edge-Dependent Node Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hypergraph Diffusion",
      "resolved_canonical": "Hypergraph Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Equivariant Networks",
      "resolved_canonical": "Equivariant Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Modeling Edge-Specific Node Features through Co-Representation Neural Hypergraph Diffusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2405.14286.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2405.14286](https://arxiv.org/abs/2405.14286)

## 🔗 유사한 논문
- [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy: Toward Privacy-Aware Hypergraph Structure Completion]] (82.9% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (82.3% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (81.9% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (80.9% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Edge-Dependent Node Classification|Edge-Dependent Node Classification]], [[keywords/Hypergraph Diffusion|Hypergraph Diffusion]], [[keywords/Equivariant Networks|Equivariant Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.14286v3 Announce Type: replace-cross 
Abstract: Hypergraphs are widely being employed to represent complex higher-order relations in real-world applications. Most existing research on hypergraph learning focuses on node-level or edge-level tasks. A practically relevant and more challenging task, edge-dependent node classification (ENC), is still under-explored. In ENC, a node can have different labels across different hyperedges, which requires the modeling of node features unique to each hyperedge. The state-of-the-art ENC solution, WHATsNet, only outputs single node and edge representations, leading to the limitations of \textbf{entangled edge-specific features} and \textbf{non-adaptive representation sizes} when applied to ENC. Additionally, WHATsNet suffers from the common \textbf{oversmoothing issue} in most HGNNs. To address these limitations, we propose \textbf{CoNHD}, a novel HGNN architecture specifically designed to model edge-specific features for ENC. Instead of learning separate representations for nodes and edges, CoNHD reformulates within-edge and within-node interactions as a hypergraph diffusion process over node-edge co-representations. We develop a neural implementation of the proposed diffusion process, leveraging equivariant networks as diffusion operators to effectively learn the diffusion dynamics from data. Extensive experiments demonstrate that CoNHD achieves the best performance across all benchmark ENC datasets and several downstream tasks without sacrificing efficiency. Our implementation is available at https://github.com/zhengyijia/CoNHD.

## 📝 요약

이 논문은 복잡한 고차원 관계를 표현하는 데 사용되는 하이퍼그래프에서의 엣지 의존 노드 분류(ENC) 문제를 다룹니다. 기존의 ENC 솔루션인 WHATsNet은 엣지별 특징을 효과적으로 모델링하지 못하고, 과도한 스무딩 문제를 겪습니다. 이를 해결하기 위해, 저자들은 CoNHD라는 새로운 하이퍼그래프 신경망(HGNN) 아키텍처를 제안합니다. CoNHD는 노드와 엣지의 상호작용을 노드-엣지 공동 표현으로 재구성하여 하이퍼그래프 확산 과정을 모델링합니다. 이 과정은 등변 네트워크를 확산 연산자로 활용하여 구현됩니다. 실험 결과, CoNHD는 모든 ENC 벤치마크 데이터셋과 여러 다운스트림 작업에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 하이퍼그래프는 복잡한 고차원 관계를 표현하기 위해 널리 사용되며, 기존 연구는 주로 노드 또는 엣지 수준의 작업에 초점을 맞추고 있습니다.
- 2. 엣지 의존 노드 분류(ENC)는 실질적으로 중요한 과제이며, 각 하이퍼엣지에 고유한 노드 특징을 모델링해야 하는 도전적인 작업입니다.
- 3. 기존의 ENC 솔루션인 WHATsNet은 엣지-특정 특징이 얽히고, 비적응적인 표현 크기 문제를 가지고 있으며, 과도한 스무딩 문제를 겪고 있습니다.
- 4. CoNHD는 ENC를 위해 엣지-특정 특징을 모델링하도록 설계된 새로운 HGNN 아키텍처로, 노드와 엣지의 공동 표현을 통한 하이퍼그래프 확산 과정을 재구성합니다.
- 5. CoNHD는 모든 ENC 벤치마크 데이터셋과 여러 다운스트림 작업에서 최고의 성능을 달성하며, 효율성을 희생하지 않습니다.


---

*Generated on 2025-09-24 00:38:44*