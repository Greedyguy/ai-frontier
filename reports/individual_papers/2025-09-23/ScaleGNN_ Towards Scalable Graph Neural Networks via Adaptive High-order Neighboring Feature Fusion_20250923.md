---
keywords:
  - Graph Neural Network
  - Over-smoothing in GNNs
  - Local Contribution Score
  - Feature Fusion in GNNs
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2504.15920
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:41:16.866915",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Over-smoothing in GNNs",
    "Local Contribution Score",
    "Feature Fusion in GNNs"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Over-smoothing in GNNs": 0.78,
    "Local Contribution Score": 0.8,
    "Feature Fusion in GNNs": 0.77
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
        "rationale": "Graph Neural Networks are central to the paper's methodology and connect well with existing literature on graph-based learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "over-smoothing",
        "canonical": "Over-smoothing in GNNs",
        "aliases": [
          "over-smoothing problem",
          "node representation smoothing"
        ],
        "category": "unique_technical",
        "rationale": "Over-smoothing is a specific challenge in GNNs that the paper addresses, making it a unique technical concept.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Local Contribution Score",
        "canonical": "Local Contribution Score",
        "aliases": [
          "LCS",
          "local score"
        ],
        "category": "unique_technical",
        "rationale": "The Local Contribution Score is a novel mechanism introduced in the paper, offering a unique approach to feature selection in GNNs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "feature fusion strategy",
        "canonical": "Feature Fusion in GNNs",
        "aliases": [
          "fusion strategy",
          "feature fusion"
        ],
        "category": "specific_connectable",
        "rationale": "Feature fusion is a key technique in the paper, enhancing the connectivity with other works on feature integration in GNNs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "scalability",
      "efficiency",
      "computational overhead"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "over-smoothing",
      "resolved_canonical": "Over-smoothing in GNNs",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Local Contribution Score",
      "resolved_canonical": "Local Contribution Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "feature fusion strategy",
      "resolved_canonical": "Feature Fusion in GNNs",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.15920.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2504.15920](https://arxiv.org/abs/2504.15920)

## 🔗 유사한 논문
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (87.5% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (85.1% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (84.3% similar)
- [[2025-09-23/A Scalable Multi-Robot Framework for Decentralized and Asynchronous Perception-Action-Communication Loops_20250923|A Scalable Multi-Robot Framework for Decentralized and Asynchronous Perception-Action-Communication Loops]] (84.2% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Feature Fusion in GNNs|Feature Fusion in GNNs]]
**⚡ Unique Technical**: [[keywords/Over-smoothing in GNNs|Over-smoothing in GNNs]], [[keywords/Local Contribution Score|Local Contribution Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.15920v5 Announce Type: replace 
Abstract: Graph Neural Networks (GNNs) have demonstrated impressive performance across diverse graph-based tasks by leveraging message passing to capture complex node relationships. However, when applied to large-scale real-world graphs, GNNs face two major challenges: First, it becomes increasingly difficult to ensure both scalability and efficiency, as the repeated aggregation of large neighborhoods leads to significant computational overhead; Second, the over-smoothing problem arises, where excessive or deep propagation makes node representations indistinguishable, severely hindering model expressiveness. To tackle these issues, we propose ScaleGNN, a novel framework that adaptively fuses multi-hop node features for both scalable and effective graph learning. First, we construct per-hop pure neighbor matrices that capture only the exclusive structural information at each hop, avoiding the redundancy of conventional aggregation. Then, an enhanced feature fusion strategy significantly balances low-order and high-order information, preserving both local detail and global correlations without incurring excessive complexity. To further reduce redundancy and over-smoothing, we introduce a Local Contribution Score (LCS)-based masking mechanism to filter out less relevant high-order neighbors, ensuring that only the most meaningful information is aggregated. In addition, learnable sparse constraints selectively integrate multi-hop valuable features, emphasizing the most informative high-order neighbors. Extensive experiments on real-world datasets demonstrate that ScaleGNN consistently outperforms state-of-the-art GNNs in both predictive accuracy and computational efficiency, highlighting its practical value for large-scale graph learning.

## 📝 요약

이 논문에서는 대규모 그래프 학습의 효율성과 확장성을 개선하기 위해 ScaleGNN이라는 새로운 프레임워크를 제안합니다. 기존 그래프 신경망(GNN)이 대규모 그래프에서 확장성과 과도한 스무딩 문제를 겪는다는 점을 해결하고자, ScaleGNN은 멀티 홉 노드 특징을 적응적으로 융합합니다. 각 홉의 구조적 정보를 포착하는 순수 이웃 행렬을 구성하여 중복을 피하고, 향상된 특징 융합 전략을 통해 저차 및 고차 정보를 균형 있게 결합합니다. 또한, 로컬 기여 점수(LCS) 기반의 마스킹 메커니즘과 학습 가능한 희소 제약을 도입하여, 중요하지 않은 고차 이웃을 필터링하고 유용한 정보를 강조합니다. 실험 결과, ScaleGNN은 예측 정확도와 계산 효율성에서 기존 GNN을 능가하며, 대규모 그래프 학습에 실질적인 가치를 제공합니다.

## 🎯 주요 포인트

- 1. GNN은 대규모 그래프에서 확장성과 효율성을 동시에 확보하기 어려운 문제에 직면합니다.
- 2. 과도한 전파로 인해 노드 표현이 구별되지 않는 과도한 평활화 문제가 발생합니다.
- 3. ScaleGNN은 멀티 홉 노드 특징을 적응적으로 융합하여 확장 가능하고 효과적인 그래프 학습을 제공합니다.
- 4. LCS 기반 마스킹 메커니즘을 도입하여 덜 관련 있는 고차 이웃을 필터링하고 가장 의미 있는 정보를 집계합니다.
- 5. ScaleGNN은 예측 정확도와 계산 효율성 면에서 최첨단 GNN보다 우수한 성능을 보입니다.


---

*Generated on 2025-09-24 02:41:16*