---
keywords:
  - Transformer
  - Causality-Induced Positional Encoding
  - Directed Acyclic Graph
  - Hyperbolic Space
  - Attention Mechanism
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16629
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:41:26.613191",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Causality-Induced Positional Encoding",
    "Directed Acyclic Graph",
    "Hyperbolic Space",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Causality-Induced Positional Encoding": 0.8,
    "Directed Acyclic Graph": 0.78,
    "Hyperbolic Space": 0.72,
    "Attention Mechanism": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are central to the paper's methodology, linking to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Causality-Induced Positional Encoding",
        "canonical": "Causality-Induced Positional Encoding",
        "aliases": [
          "CAPE"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced by the paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Weighted Directed Acyclic Graph",
        "canonical": "Directed Acyclic Graph",
        "aliases": [
          "DAG"
        ],
        "category": "specific_connectable",
        "rationale": "DAGs are essential for representing causal structures, linking to graph theory and causal inference.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hyperbolic Space",
        "canonical": "Hyperbolic Space",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Hyperbolic space is used for embedding the DAG, connecting to geometric representations in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Self-Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Self-Attention"
        ],
        "category": "specific_connectable",
        "rationale": "The self-attention mechanism is a key component of transformers, facilitating connections to neural network architectures.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
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
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Causality-Induced Positional Encoding",
      "resolved_canonical": "Causality-Induced Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Weighted Directed Acyclic Graph",
      "resolved_canonical": "Directed Acyclic Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hyperbolic Space",
      "resolved_canonical": "Hyperbolic Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Self-Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16629.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16629](https://arxiv.org/abs/2509.16629)

## 🔗 유사한 논문
- [[2025-09-22/Positional Encoding in Transformer-Based Time Series Models_ A Survey_20250922|Positional Encoding in Transformer-Based Time Series Models: A Survey]] (85.3% similar)
- [[2025-09-19/DyWPE_ Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers_20250919|DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers]] (80.3% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (79.9% similar)
- [[2025-09-23/ViTCAE_ ViT-based Class-conditioned Autoencoder_20250923|ViTCAE: ViT-based Class-conditioned Autoencoder]] (79.4% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Directed Acyclic Graph|Directed Acyclic Graph]], [[keywords/Hyperbolic Space|Hyperbolic Space]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Causality-Induced Positional Encoding|Causality-Induced Positional Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16629v1 Announce Type: new 
Abstract: Positional encoding is essential for supplementing transformer with positional information of tokens. Existing positional encoding methods demand predefined token/feature order, rendering them unsuitable for real-world data with non-sequential yet causally-related features. To address this limitation, we propose CAPE, a novel method that identifies underlying causal structure over non-sequential features as a weighted directed acyclic graph (DAG) using generalized structural equation modeling. The DAG is then embedded in hyperbolic space where its geometric structure is well-preserved using a hyperboloid model-based approach that effectively captures two important causal graph properties (causal strength & causal specificity). This step yields causality-aware positional encodings for the features, which are converted into their rotary form for integrating with transformer's self-attention mechanism. Theoretical analysis reveals that CAPE-generated rotary positional encodings possess three valuable properties for enhanced self-attention, including causal distance-induced attenuation, causal generality-induced attenuation, and robustness to positional disturbances. We evaluate CAPE over both synthetic and real-word datasets, empirically demonstrating its theoretical properties and effectiveness in enhancing transformer for data with non-sequential features. Our code is available at https://github.com/Catchxu/CAPE.

## 📝 요약

이 논문은 비순차적이지만 인과적으로 관련된 특징을 가진 실제 데이터에 적합한 새로운 위치 인코딩 방법인 CAPE를 제안합니다. CAPE는 일반화된 구조 방정식 모델링을 사용하여 비순차적 특징의 인과 구조를 가중 방향 비순환 그래프로 식별하고, 이를 쌍곡 공간에 임베딩하여 인과 강도와 특이성을 효과적으로 포착합니다. 이 과정에서 생성된 인과성 인식 위치 인코딩은 트랜스포머의 자기 주의 메커니즘에 통합됩니다. 이론적 분석을 통해 CAPE가 생성한 회전 위치 인코딩이 인과 거리와 일반성에 따른 감쇠 및 위치 교란에 대한 강건성을 포함한 세 가지 중요한 속성을 가짐을 보여줍니다. CAPE는 합성 및 실제 데이터셋에서 평가되어 이론적 속성과 트랜스포머 성능 향상에 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. CAPE는 비순차적 특징의 인과 구조를 가중치 방향 비순환 그래프로 식별하여 하이퍼볼릭 공간에 임베딩하는 새로운 방법입니다.
- 2. 하이퍼볼로이드 모델 기반 접근법을 사용하여 인과 그래프의 두 가지 중요한 속성인 인과 강도와 인과 특이성을 효과적으로 포착합니다.
- 3. CAPE가 생성한 회전형 위치 인코딩은 인과 거리 유도 감쇠, 인과 일반성 유도 감쇠, 위치 교란에 대한 강건성을 포함한 세 가지 중요한 속성을 가집니다.
- 4. CAPE는 합성 및 실제 데이터 세트에서 평가되었으며, 비순차적 특징이 있는 데이터에서 트랜스포머의 성능을 향상시키는 데 효과적임을 실증적으로 입증했습니다.


---

*Generated on 2025-09-24 01:41:26*