<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:23:47.399562",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Neural Architecture Search",
    "Adaptive Genetic Optimization Strategy",
    "Bayesian-Guided Tuning Module",
    "Graph Representation Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Neural Architecture Search": 0.8,
    "Adaptive Genetic Optimization Strategy": 0.7,
    "Bayesian-Guided Tuning Module": 0.72,
    "Graph Representation Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on improving graph representation learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Neural Architecture Search",
        "canonical": "Neural Architecture Search",
        "aliases": [
          "NAS"
        ],
        "category": "broad_technical",
        "rationale": "Key methodology for optimizing GNN architectures in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Genetic Optimization Strategy",
        "canonical": "Adaptive Genetic Optimization Strategy",
        "aliases": [
          "AGOS"
        ],
        "category": "unique_technical",
        "rationale": "A novel component introduced in the paper for efficient search.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Bayesian-Guided Tuning Module",
        "canonical": "Bayesian-Guided Tuning Module",
        "aliases": [
          "BGTM"
        ],
        "category": "unique_technical",
        "rationale": "Innovative tuning approach that enhances scalability and robustness.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Graph Representation Learning",
        "canonical": "Graph Representation Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The primary application area of the proposed framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Neural Architecture Search",
      "resolved_canonical": "Neural Architecture Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Genetic Optimization Strategy",
      "resolved_canonical": "Adaptive Genetic Optimization Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Bayesian-Guided Tuning Module",
      "resolved_canonical": "Bayesian-Guided Tuning Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Graph Representation Learning",
      "resolved_canonical": "Graph Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# ABG-NAS: Adaptive Bayesian Genetic Neural Architecture Search for Graph Representation Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.21254.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2504.21254](https://arxiv.org/abs/2504.21254)

## 🔗 유사한 논문
- [[2025-09-24/HyperNAS_ Enhancing Architecture Representation for NAS Predictor via Hypernetwork_20250924|HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork]] (85.6% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (84.7% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (84.5% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (83.9% similar)
- [[2025-09-24/Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying_20250924|Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Architecture Search|Neural Architecture Search]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Graph Representation Learning|Graph Representation Learning]]
**⚡ Unique Technical**: [[keywords/Adaptive Genetic Optimization Strategy|Adaptive Genetic Optimization Strategy]], [[keywords/Bayesian-Guided Tuning Module|Bayesian-Guided Tuning Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.21254v3 Announce Type: replace 
Abstract: Effective and efficient graph representation learning is essential for enabling critical downstream tasks, such as node classification, link prediction, and subgraph search. However, existing graph neural network (GNN) architectures often struggle to adapt to diverse and complex graph structures, limiting their ability to produce structure-aware and task-discriminative representations. To address this challenge, we propose ABG-NAS, a novel framework for automated graph neural network architecture search tailored for efficient graph representation learning. ABG-NAS encompasses three key components: a Comprehensive Architecture Search Space (CASS), an Adaptive Genetic Optimization Strategy (AGOS), and a Bayesian-Guided Tuning Module (BGTM). CASS systematically explores diverse propagation (P) and transformation (T) operations, enabling the discovery of GNN architectures capable of capturing intricate graph characteristics. AGOS dynamically balances exploration and exploitation, ensuring search efficiency and preserving solution diversity. BGTM further optimizes hyperparameters periodically, enhancing the scalability and robustness of the resulting architectures. Empirical evaluations on benchmark datasets (Cora, PubMed, Citeseer, and CoraFull) demonstrate that ABG-NAS consistently outperforms both manually designed GNNs and state-of-the-art neural architecture search (NAS) methods. These results highlight the potential of ABG-NAS to advance graph representation learning by providing scalable and adaptive solutions for diverse graph structures. Our code is publicly available at https://github.com/sserranw/ABG-NAS.

## 📝 요약

ABG-NAS는 그래프 표현 학습을 위한 자동화된 그래프 신경망 아키텍처 검색 프레임워크로, 다양한 그래프 구조에 적응하는 데 어려움을 겪는 기존 GNN 아키텍처의 한계를 극복하고자 합니다. 이 프레임워크는 포괄적인 아키텍처 검색 공간(CASS), 적응형 유전 최적화 전략(AGOS), 베이지안 기반 튜닝 모듈(BGTM)로 구성되어 있습니다. CASS는 다양한 전파 및 변환 작업을 탐색하여 복잡한 그래프 특성을 포착할 수 있는 GNN 아키텍처를 발견하고, AGOS는 탐색 효율성을 유지하며 솔루션 다양성을 보장합니다. BGTM은 하이퍼파라미터를 주기적으로 최적화하여 확장성과 견고성을 향상시킵니다. 벤치마크 데이터셋(Cora, PubMed, Citeseer, CoraFull)에서의 실험 결과, ABG-NAS는 수작업으로 설계된 GNN 및 최신 NAS 방법을 능가하여 다양한 그래프 구조에 대한 확장 가능하고 적응적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. ABG-NAS는 효율적인 그래프 표현 학습을 위한 자동화된 그래프 신경망 아키텍처 검색 프레임워크입니다.
- 2. CASS, AGOS, BGTM의 세 가지 주요 구성 요소를 통해 복잡한 그래프 특성을 포착할 수 있는 GNN 아키텍처를 발견합니다.
- 3. ABG-NAS는 벤치마크 데이터셋에서 수작업으로 설계된 GNN 및 최신 NAS 방법보다 일관되게 우수한 성능을 보입니다.
- 4. AGOS는 탐색 효율성을 보장하고 솔루션 다양성을 유지하며, BGTM은 하이퍼파라미터를 최적화하여 아키텍처의 확장성과 견고성을 향상시킵니다.
- 5. ABG-NAS는 다양한 그래프 구조에 대한 확장 가능하고 적응적인 솔루션을 제공하여 그래프 표현 학습을 발전시킬 잠재력을 가지고 있습니다.


---

*Generated on 2025-09-24 15:23:47*