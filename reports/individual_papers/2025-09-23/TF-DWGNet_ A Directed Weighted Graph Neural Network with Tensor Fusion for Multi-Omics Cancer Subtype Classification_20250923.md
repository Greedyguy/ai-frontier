---
keywords:
  - Graph Neural Network
  - Multi-Omics Integration
  - Tensor Fusion
  - Directed Weighted Graph
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16301
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:06:19.490361",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Multi-Omics Integration",
    "Tensor Fusion",
    "Directed Weighted Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Multi-Omics Integration": 0.78,
    "Tensor Fusion": 0.8,
    "Directed Weighted Graph": 0.77
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
        "rationale": "Graph Neural Networks are central to the paper's methodology and align with existing canonical vocabulary.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Omics Integration",
        "canonical": "Multi-Omics Integration",
        "aliases": [
          "Multi-Omics Data Integration"
        ],
        "category": "unique_technical",
        "rationale": "The integration of multi-omics data is a unique aspect of the study, crucial for cancer subtype classification.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Tensor Fusion",
        "canonical": "Tensor Fusion",
        "aliases": [
          "Tensor Fusion Mechanism"
        ],
        "category": "unique_technical",
        "rationale": "Tensor Fusion is a novel technique introduced in the paper for handling multi-modal interactions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Directed Weighted Graph",
        "canonical": "Directed Weighted Graph",
        "aliases": [
          "Directed Graph",
          "Weighted Graph"
        ],
        "category": "unique_technical",
        "rationale": "The directed weighted graph is a key innovation for capturing biological interaction dynamics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Omics Integration",
      "resolved_canonical": "Multi-Omics Integration",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Tensor Fusion",
      "resolved_canonical": "Tensor Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Directed Weighted Graph",
      "resolved_canonical": "Directed Weighted Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TF-DWGNet: A Directed Weighted Graph Neural Network with Tensor Fusion for Multi-Omics Cancer Subtype Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16301.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16301](https://arxiv.org/abs/2509.16301)

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (81.8% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (81.8% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (81.6% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (81.6% similar)
- [[2025-09-23/ME-Mamba_ Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis_20250923|ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Multi-Omics Integration|Multi-Omics Integration]], [[keywords/Tensor Fusion|Tensor Fusion]], [[keywords/Directed Weighted Graph|Directed Weighted Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16301v1 Announce Type: cross 
Abstract: Integration and analysis of multi-omics data provide valuable insights for cancer subtype classification. However, such data are inherently heterogeneous, high-dimensional, and exhibit complex intra- and inter-modality dependencies. Recent advances in graph neural networks (GNNs) offer powerful tools for modeling such structure. Yet, most existing methods rely on prior knowledge or predefined similarity networks to construct graphs, which are often undirected or unweighted, failing to capture the directionality and strength of biological interactions. Interpretability at both the modality and feature levels also remains limited. To address these challenges, we propose TF-DWGNet, a novel Graph Neural Network framework that combines tree-based Directed Weighted graph construction with Tensor Fusion for multiclass cancer subtype classification. TF-DWGNet introduces two key innovations: a supervised tree-based approach for constructing directed, weighted graphs tailored to each omics modality, and a tensor fusion mechanism that captures unimodal, bimodal, and trimodal interactions using low-rank decomposition for efficiency. TF-DWGNet enables modality-specific representation learning, joint embedding fusion, and interpretable subtype prediction. Experiments on real-world cancer datasets show that TF-DWGNet consistently outperforms state-of-the-art baselines across multiple metrics and statistical tests. Moreover, it provides biologically meaningful insights by ranking influential features and modalities. These results highlight TF-DWGNet's potential for effective and interpretable multi-omics integration in cancer research.

## 📝 요약

이 논문은 다중 오믹스 데이터를 활용한 암 아형 분류를 위한 새로운 그래프 신경망 프레임워크인 TF-DWGNet을 제안합니다. 기존 방법들이 방향성과 상호작용 강도를 제대로 반영하지 못하는 문제를 해결하기 위해, TF-DWGNet은 감독된 트리 기반의 방향성 가중 그래프를 각 오믹스 모달리티에 맞춰 구축하고, 텐서 융합 메커니즘을 통해 단일, 이중, 삼중 모달리티 간 상호작용을 효율적으로 포착합니다. 이를 통해 모달리티별 표현 학습, 공동 임베딩 융합, 해석 가능한 아형 예측이 가능해집니다. 실제 암 데이터셋 실험 결과, TF-DWGNet은 여러 지표에서 기존 최첨단 기법들을 능가하며, 중요한 특징과 모달리티를 순위화하여 생물학적으로 의미 있는 통찰을 제공합니다. 이 연구는 암 연구에서 다중 오믹스 통합의 효과적이고 해석 가능한 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. TF-DWGNet은 트리 기반의 방향성 및 가중치를 가진 그래프를 구축하여 각 오믹스 모달리티에 맞춘 그래프 신경망 프레임워크를 제안합니다.
- 2. 텐서 융합 메커니즘을 통해 단일, 이중, 삼중 모달 상호작용을 효율적으로 캡처하여 다중 암 아형 분류를 수행합니다.
- 3. TF-DWGNet은 모달리티별 표현 학습, 공동 임베딩 융합, 해석 가능한 아형 예측을 가능하게 합니다.
- 4. 실제 암 데이터셋 실험에서 TF-DWGNet은 여러 지표와 통계 테스트에서 최신 기법들을 능가하는 성능을 보입니다.
- 5. TF-DWGNet은 중요한 특징과 모달리티를 순위화하여 생물학적으로 의미 있는 통찰을 제공합니다.


---

*Generated on 2025-09-24 02:06:19*