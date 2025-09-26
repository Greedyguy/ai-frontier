---
keywords:
  - Graph Neural Network
  - Schreier-Coset Graph Propagation
  - Cayley Graph
  - Expander Graph
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.10392
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:56:26.086191",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Schreier-Coset Graph Propagation",
    "Cayley Graph",
    "Expander Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.95,
    "Schreier-Coset Graph Propagation": 0.85,
    "Cayley Graph": 0.7,
    "Expander Graph": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Neural Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, linking to existing GNN research enhances connectivity.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.95
      },
      {
        "surface": "Schreier-Coset Graph Propagation",
        "canonical": "Schreier-Coset Graph Propagation",
        "aliases": [
          "SCGP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specific to the paper, offering new linkage opportunities.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cayley graphs",
        "canonical": "Cayley Graph",
        "aliases": [
          "Cayley graphs"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant to graph theory and connects to existing literature on graph structures.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "expander graphs",
        "canonical": "Expander Graph",
        "aliases": [
          "expander graphs"
        ],
        "category": "specific_connectable",
        "rationale": "Links to a well-known concept in graph theory, facilitating connections to related research.",
        "novelty_score": 0.35,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.95
      }
    },
    {
      "candidate_surface": "Schreier-Coset Graph Propagation",
      "resolved_canonical": "Schreier-Coset Graph Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cayley graphs",
      "resolved_canonical": "Cayley Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "expander graphs",
      "resolved_canonical": "Expander Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Schreier-Coset Graph Propagation

**Korean Title:** 슈라이어-코셋 그래프 전파

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.10392.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.10392](https://arxiv.org/abs/2505.10392)

## 🔗 유사한 논문
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (85.6% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (85.3% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (84.8% similar)
- [[2025-09-18/Towards Pre-trained Graph Condensation via Optimal Transport_20250918|Towards Pre-trained Graph Condensation via Optimal Transport]] (84.3% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Cayley Graph|Cayley Graph]], [[keywords/Expander Graph|Expander Graph]]
**⚡ Unique Technical**: [[keywords/Schreier-Coset Graph Propagation|Schreier-Coset Graph Propagation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10392v2 Announce Type: replace-cross 
Abstract: Graph Neural Networks (GNNs) offer a principled framework for learning over graph-structured data, yet their expressive capacity is often hindered by over-squashing, wherein information from distant nodes is compressed into fixed-size vectors. Existing solutions, including graph rewiring and bottleneck-resistant architectures such as Cayley and expander graphs, avoid this problem but introduce scalability bottlenecks. In particular, the Cayley graphs constructed over $SL(2,\mathbb{Z}_n)$ exhibit strong theoretical properties, yet suffer from cubic node growth $O(n^3)$, leading to high memory usage. To address this, this work introduces Schrier-Coset Graph Propagation (SCGP), a group-theoretic augmentation method that enriches node features through Schreier-coset embeddings without altering the input graph topology. SCGP embeds bottleneck-free connectivity patterns into a compact feature space, improving long-range message passing while maintaining computational efficiency. Empirical evaluations across standard node and graph classification benchmarks demonstrate that SCGP achieves performance comparable to, or exceeding, expander graph and rewired GNN baselines. Furthermore, SCGP exhibits particular advantages in processing hierarchical and modular graph structures, offering reduced inference latency, improved scalability, and a low memory footprint, making it suitable for real-time and resource-constrained applications.

## 🔍 Abstract (한글 번역)

arXiv:2505.10392v2 발표 유형: 교체-크로스  
초록: 그래프 신경망(GNN)은 그래프 구조 데이터를 학습하기 위한 원칙적인 프레임워크를 제공하지만, 종종 먼 노드로부터의 정보가 고정 크기의 벡터로 압축되는 오버 스쿼싱(over-squashing)으로 인해 표현력이 제한됩니다. 그래프 재배선 및 Cayley 및 확장자 그래프와 같은 병목 저항 아키텍처를 포함한 기존 솔루션은 이 문제를 피하지만 확장성 병목을 초래합니다. 특히, $SL(2,\mathbb{Z}_n)$에 대해 구성된 Cayley 그래프는 강력한 이론적 특성을 보이지만, 노드 성장 $O(n^3)$으로 인해 높은 메모리 사용량을 초래합니다. 이를 해결하기 위해, 본 연구는 입력 그래프의 토폴로지를 변경하지 않고 Schreier-coset 임베딩을 통해 노드 기능을 풍부하게 하는 군 이론적 증강 방법인 Schrier-Coset Graph Propagation (SCGP)을 소개합니다. SCGP는 병목 없는 연결 패턴을 컴팩트한 특징 공간에 임베딩하여, 계산 효율성을 유지하면서 장거리 메시지 전달을 개선합니다. 표준 노드 및 그래프 분류 벤치마크에 대한 실험적 평가 결과, SCGP는 확장자 그래프 및 재배선된 GNN 기준선과 비교하여 동등하거나 그 이상의 성능을 달성함을 보여줍니다. 또한, SCGP는 계층적이고 모듈식인 그래프 구조를 처리하는 데 있어 특히 장점을 보이며, 추론 지연 감소, 확장성 개선, 낮은 메모리 사용량을 제공하여 실시간 및 자원 제약 애플리케이션에 적합합니다.

## 📝 요약

이 논문은 그래프 신경망(GNN)의 정보 압축 문제를 해결하기 위해 Schreier-Coset Graph Propagation(SCGP) 방법을 제안합니다. 기존의 Cayley 그래프와 같은 방법은 이론적으로 우수하지만 메모리 사용량이 높다는 단점이 있습니다. SCGP는 입력 그래프의 구조를 변경하지 않고 Schreier-coset 임베딩을 통해 노드 특징을 강화하여, 장거리 메시지 전달을 개선하고 계산 효율성을 유지합니다. 실험 결과, SCGP는 기존의 확장 그래프 및 재배선 GNN과 비교하여 성능이 뛰어나며, 계층적 및 모듈형 그래프 구조 처리에서 특히 장점을 보입니다. 이 방법은 실시간 및 자원 제약이 있는 환경에서 적합한 낮은 메모리 사용량과 향상된 확장성을 제공합니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN)의 표현력을 제한하는 문제인 오버스쿼싱을 해결하기 위해 Schrier-Coset Graph Propagation(SCGP) 방법을 제안합니다.
- 2. SCGP는 입력 그래프의 토폴로지를 변경하지 않고 Schreier-coset 임베딩을 통해 노드 특징을 강화합니다.
- 3. SCGP는 확장 그래프 및 리와이어드 GNN과 비교하여 성능이 동등하거나 우수하며, 특히 계층적 및 모듈형 그래프 구조 처리에 유리합니다.
- 4. SCGP는 실시간 및 자원 제약이 있는 애플리케이션에 적합하도록 추론 지연을 줄이고 확장성을 개선하며 메모리 사용량을 낮춥니다.


---

*Generated on 2025-09-23 09:56:26*