---
keywords:
  - Transformer
  - Attribute-Vector Fusion
  - Hybrid ANN
  - Filtered Retrieval Systems
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19767
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:47:59.626165",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Attribute-Vector Fusion",
    "Hybrid ANN",
    "Filtered Retrieval Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Attribute-Vector Fusion": 0.78,
    "Hybrid ANN": 0.82,
    "Filtered Retrieval Systems": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based convexification",
        "canonical": "Transformer",
        "aliases": [
          "Transformer-based methods"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the method, linking it to a broad range of NLP and ML applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attribute-Vector Fusion",
        "canonical": "Attribute-Vector Fusion",
        "aliases": [
          "Fused Attribute-Vector"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hybrid ANN",
        "canonical": "Hybrid ANN",
        "aliases": [
          "Hybrid Artificial Neural Network"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on hybrid ANN systems, which are key to its contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Filtered Retrieval Systems",
        "canonical": "Filtered Retrieval Systems",
        "aliases": [
          "Filtered Search Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Filtered retrieval is a significant aspect of the paper's contribution to search systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
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
      "candidate_surface": "Transformer-based convexification",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attribute-Vector Fusion",
      "resolved_canonical": "Attribute-Vector Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hybrid ANN",
      "resolved_canonical": "Hybrid ANN",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Filtered Retrieval Systems",
      "resolved_canonical": "Filtered Retrieval Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# FusedANN: Convexified Hybrid ANN via Attribute-Vector Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19767.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19767](https://arxiv.org/abs/2509.19767)

## 🔗 유사한 논문
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.8% similar)
- [[2025-09-24/FedFusion_ Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity_20250924|FedFusion: Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity]] (80.2% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (79.6% similar)
- [[2025-09-24/HyperNAS_ Enhancing Architecture Representation for NAS Predictor via Hypernetwork_20250924|HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork]] (79.4% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Filtered Retrieval Systems|Filtered Retrieval Systems]]
**⚡ Unique Technical**: [[keywords/Attribute-Vector Fusion|Attribute-Vector Fusion]], [[keywords/Hybrid ANN|Hybrid ANN]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19767v1 Announce Type: cross 
Abstract: Vector search powers transformers technology, but real-world use demands hybrid queries that combine vector similarity with attribute filters (e.g., "top document in category X, from 2023"). Current solutions trade off recall, speed, and flexibility, relying on fragile index hacks that don't scale. We introduce FusedANN (Fused Attribute-Vector Nearest Neighbor), a geometric framework that elevates filtering to ANN optimization constraints and introduces a convex fused space via a Lagrangian-like relaxation. Our method jointly embeds attributes and vectors through transformer-based convexification, turning hard filters into continuous, weighted penalties that preserve top-k semantics while enabling efficient approximate search. We prove that FusedANN reduces to exact filtering under high selectivity, gracefully relaxes to semantically nearest attributes when exact matches are insufficient, and preserves downstream ANN alpha-approximation guarantees. Empirically, FusedANN improves query throughput by eliminating brittle filtering stages, achieving superior recall-latency tradeoffs on standard hybrid benchmarks without specialized index hacks, delivering up to 3 times higher throughput and better recall than state-of-the-art hybrid and graph-based systems. Theoretically, we provide explicit error bounds and parameter selection rules that make FusedANN practical for production. This establishes a principled, scalable, and verifiable bridge between symbolic constraints and vector similarity, unlocking a new generation of filtered retrieval systems for large, hybrid, and dynamic NLP/ML workloads.

## 📝 요약

FusedANN은 벡터 유사성과 속성 필터를 결합한 하이브리드 쿼리를 효율적으로 처리하기 위한 기하학적 프레임워크입니다. 기존 방법들이 확장성 문제를 겪는 반면, FusedANN은 속성을 ANN 최적화 제약으로 통합하고, 라그랑주 이완을 통해 속성과 벡터를 공동 임베딩합니다. 이 방법은 필터를 연속적이고 가중된 패널티로 변환하여 효율적인 근사 검색을 가능하게 합니다. FusedANN은 높은 선택성에서는 정확한 필터링을 제공하고, 부족할 경우 의미적으로 가장 가까운 속성을 선택합니다. 실험 결과, FusedANN은 기존 방법보다 최대 3배 높은 처리량과 더 나은 재현율을 달성하며, 이론적으로 명시적인 오류 범위와 파라미터 선택 규칙을 제공하여 실용성을 높였습니다. 이를 통해 대규모 하이브리드 검색 시스템의 새로운 가능성을 열었습니다.

## 🎯 주요 포인트

- 1. FusedANN은 벡터 유사성과 속성 필터를 결합한 하이브리드 쿼리를 효율적으로 처리하기 위한 기하학적 프레임워크를 제공합니다.
- 2. 이 방법은 속성과 벡터를 트랜스포머 기반의 볼록화 과정을 통해 공동 임베딩하여, 하드 필터를 연속적이고 가중치가 부여된 패널티로 변환합니다.
- 3. FusedANN은 높은 선택성 하에서 정확한 필터링으로 축소되며, 정확한 일치가 부족할 경우 의미적으로 가장 가까운 속성으로 유연하게 전환됩니다.
- 4. 실험적으로 FusedANN은 기존의 하이브리드 및 그래프 기반 시스템보다 최대 3배 높은 처리량과 더 나은 리콜을 달성합니다.
- 5. 이론적으로 FusedANN은 명시적인 오류 범위와 파라미터 선택 규칙을 제공하여, 대규모 하이브리드 및 동적 NLP/ML 작업 부하에 적합한 새로운 필터링 검색 시스템을 구현합니다.


---

*Generated on 2025-09-25 15:47:59*