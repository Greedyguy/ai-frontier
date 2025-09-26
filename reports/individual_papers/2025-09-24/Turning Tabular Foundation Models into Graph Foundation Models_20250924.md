<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:28:20.523064",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Foundation Models",
    "Tabular Foundation Models",
    "Graph Neural Network",
    "Neighborhood Feature Aggregation",
    "Structural Embeddings"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Foundation Models": 0.8,
    "Tabular Foundation Models": 0.78,
    "Graph Neural Network": 0.85,
    "Neighborhood Feature Aggregation": 0.72,
    "Structural Embeddings": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Foundation Models",
        "canonical": "Graph Foundation Models",
        "aliases": [
          "GFMs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept in graph machine learning, linking tabular and graph models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Tabular Foundation Models",
        "canonical": "Tabular Foundation Models",
        "aliases": [
          "TFMs"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a new application of foundation models in the context of graph learning.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNNs"
        ],
        "category": "specific_connectable",
        "rationale": "A well-established concept in graph learning, providing strong connectivity.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neighborhood Feature Aggregation",
        "canonical": "Neighborhood Feature Aggregation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific technique used in the proposed framework, relevant for graph data processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Structural Embeddings",
        "canonical": "Structural Embeddings",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for enhancing node representations in graph models, facilitating deeper insights.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
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
      "candidate_surface": "Graph Foundation Models",
      "resolved_canonical": "Graph Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Tabular Foundation Models",
      "resolved_canonical": "Tabular Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neighborhood Feature Aggregation",
      "resolved_canonical": "Neighborhood Feature Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Structural Embeddings",
      "resolved_canonical": "Structural Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Turning Tabular Foundation Models into Graph Foundation Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.20906.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2508.20906](https://arxiv.org/abs/2508.20906)

## 🔗 유사한 논문
- [[2025-09-22/Two Facets of the Same Optimization Coin_ Model Degradation and Representation Collapse in Graph Foundation Models_20250922|Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models]] (82.5% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (82.4% similar)
- [[2025-09-18/Exploring the Global-to-Local Attention Scheme in Graph Transformers_ An Empirical Study_20250918|Exploring the Global-to-Local Attention Scheme in Graph Transformers: An Empirical Study]] (82.0% similar)
- [[2025-09-24/Topological Feature Compression for Molecular Graph Neural Networks_20250924|Topological Feature Compression for Molecular Graph Neural Networks]] (81.9% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Graph Foundation Models|Graph Foundation Models]], [[keywords/Tabular Foundation Models|Tabular Foundation Models]], [[keywords/Neighborhood Feature Aggregation|Neighborhood Feature Aggregation]], [[keywords/Structural Embeddings|Structural Embeddings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.20906v2 Announce Type: replace 
Abstract: While foundation models have revolutionized such fields as natural language processing and computer vision, their potential in graph machine learning remains largely unexplored. One of the key challenges in designing graph foundation models (GFMs) is handling diverse node features that can vary across different graph datasets. While many works on GFMs have focused exclusively on text-attributed graphs, the problem of handling arbitrary features of other types in GFMs has not been fully addressed. However, this problem is not unique to the graph domain, as it also arises in the field of machine learning for tabular data. In this work, motivated by the recent success of tabular foundation models (TFMs) like TabPFNv2 or LimiX, we propose G2T-FM, a simple framework for turning tabular foundation models into graph foundation models. Specifically, G2T-FM augments the original node features with neighborhood feature aggregation, adds structural embeddings, and then applies a TFM to the constructed node representations. Even in a fully in-context regime, our model achieves strong results, significantly outperforming publicly available GFMs and performing competitively with, and often better than, well-tuned GNNs trained from scratch. Moreover, after finetuning, G2T-FM surpasses well-tuned GNN baselines. In particular, when combined with LimiX, G2T-FM often outperforms the best GNN by a significant margin. In summary, our paper reveals the potential of a previously overlooked direction of utilizing tabular foundation models for graph machine learning tasks.

## 📝 요약

이 논문은 그래프 머신러닝 분야에서 기존의 표 기반 모델(TFM)을 활용하여 새로운 그래프 기반 모델(GFM)을 제안합니다. G2T-FM이라는 프레임워크는 노드 특징에 이웃 특징 집계와 구조적 임베딩을 추가하고, 이를 표 기반 모델에 적용합니다. 이 방법은 기존의 GFM과 잘 조정된 GNN보다 뛰어난 성능을 보이며, 특히 LimiX와 결합 시 최고의 GNN을 능가합니다. 이 연구는 표 기반 모델을 그래프 머신러닝에 활용하는 새로운 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 그래프 기초 모델(GFM)의 설계에서 다양한 노드 특징을 처리하는 것이 주요 과제입니다.
- 2. G2T-FM은 테이블 기초 모델(TFM)을 그래프 기초 모델로 변환하는 간단한 프레임워크를 제안합니다.
- 3. G2T-FM은 원래 노드 특징에 이웃 특징 집계를 추가하고 구조적 임베딩을 더하여 TFM을 적용합니다.
- 4. G2T-FM은 잘 조정된 GNN과 비교하여 경쟁력 있는 성능을 보이며, 종종 더 나은 결과를 제공합니다.
- 5. G2T-FM은 테이블 기초 모델을 그래프 머신 러닝에 활용하는 새로운 가능성을 제시합니다.


---

*Generated on 2025-09-24 15:28:20*