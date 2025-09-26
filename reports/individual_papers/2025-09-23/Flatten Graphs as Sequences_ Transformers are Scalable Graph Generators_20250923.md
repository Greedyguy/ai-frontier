---
keywords:
  - Transformer
  - AutoGraph
  - Graph Generation
  - Substructure-conditioned Generation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.02216
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:37:50.783010",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "AutoGraph",
    "Graph Generation",
    "Substructure-conditioned Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "AutoGraph": 0.8,
    "Graph Generation": 0.78,
    "Substructure-conditioned Generation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformers",
        "canonical": "Transformer",
        "aliases": [
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the paper's methodology, linking it to a broad technical category.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "AutoGraph",
        "canonical": "AutoGraph",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "AutoGraph is the novel model introduced in the paper, representing a unique technical concept.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph Generation",
        "canonical": "Graph Generation",
        "aliases": [
          "Graph Generators"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Generation is a key application area for the model, linking it to specific connectable concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Substructure-conditioned Generation",
        "canonical": "Substructure-conditioned Generation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a unique feature of the model that allows for nuanced graph generation, enhancing specificity.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "sequence",
      "sampling complexity",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "AutoGraph",
      "resolved_canonical": "AutoGraph",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph Generation",
      "resolved_canonical": "Graph Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Substructure-conditioned Generation",
      "resolved_canonical": "Substructure-conditioned Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Flatten Graphs as Sequences: Transformers are Scalable Graph Generators

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.02216.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.02216](https://arxiv.org/abs/2502.02216)

## 🔗 유사한 논문
- [[2025-09-23/GraphWeave_ Interpretable and Robust Graph Generation via Random Walk Trajectories_20250923|GraphWeave: Interpretable and Robust Graph Generation via Random Walk Trajectories]] (84.0% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (81.6% similar)
- [[2025-09-23/GraphMend_ Code Transformations for Fixing Graph Breaks in PyTorch 2_20250923|GraphMend: Code Transformations for Fixing Graph Breaks in PyTorch 2]] (81.1% similar)
- [[2025-09-23/Optimizing Inference in Transformer-Based Models_ A Multi-Method Benchmark_20250923|Optimizing Inference in Transformer-Based Models: A Multi-Method Benchmark]] (81.0% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Graph Generation|Graph Generation]]
**⚡ Unique Technical**: [[keywords/AutoGraph|AutoGraph]], [[keywords/Substructure-conditioned Generation|Substructure-conditioned Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.02216v2 Announce Type: replace 
Abstract: We introduce AutoGraph, a scalable autoregressive model for attributed graph generation using decoder-only transformers. By flattening graphs into random sequences of tokens through a reversible process, AutoGraph enables modeling graphs as sequences without relying on additional node features that are expensive to compute, in contrast to diffusion-based approaches. This results in sampling complexity and sequence lengths that scale optimally linearly with the number of edges, making it scalable and efficient for large, sparse graphs. A key success factor of AutoGraph is that its sequence prefixes represent induced subgraphs, creating a direct link to sub-sentences in language modeling. Empirically, AutoGraph achieves state-of-the-art performance on synthetic and molecular benchmarks, with up to 100x faster generation and 3x faster training than leading diffusion models. It also supports substructure-conditioned generation without fine-tuning and shows promising transferability, bridging language modeling and graph generation to lay the groundwork for graph foundation models. Our code is available at https://github.com/BorgwardtLab/AutoGraph.

## 📝 요약

AutoGraph는 디코더 전용 트랜스포머를 사용하여 속성 그래프를 생성하는 확장 가능한 자기회귀 모델입니다. 그래프를 토큰의 임의 시퀀스로 변환하여 추가적인 노드 특징 없이도 그래프를 시퀀스로 모델링할 수 있습니다. 이는 엣지 수에 비례하여 샘플링 복잡도와 시퀀스 길이가 선형적으로 확장되어 대규모 희소 그래프에 효율적입니다. AutoGraph는 시퀀스 접두사가 유도된 부분 그래프를 나타내어 언어 모델링과 직접 연결됩니다. 실험 결과, 합성 및 분자 벤치마크에서 최첨단 성능을 보이며, 기존 확산 모델보다 최대 100배 빠른 생성과 3배 빠른 학습을 달성했습니다. 또한, 세부 구조 조건 생성과 전이 가능성을 보여 그래프 기초 모델의 기반을 마련합니다.

## 🎯 주요 포인트

- 1. AutoGraph는 디코더 전용 트랜스포머를 사용하여 속성 그래프 생성을 위한 확장 가능한 자기 회귀 모델을 제안합니다.
- 2. 그래프를 토큰의 랜덤 시퀀스로 변환하여 추가적인 노드 특징 없이도 그래프를 시퀀스로 모델링할 수 있습니다.
- 3. AutoGraph는 엣지 수에 따라 샘플링 복잡성과 시퀀스 길이가 선형적으로 확장되어 대규모 희소 그래프에 효율적입니다.
- 4. AutoGraph는 합성 및 분자 벤치마크에서 최첨단 성능을 달성하며, 기존 확산 모델보다 최대 100배 빠른 생성과 3배 빠른 학습을 제공합니다.
- 5. 하위 구조 조건부 생성을 지원하며, 언어 모델링과 그래프 생성을 연결하여 그래프 기초 모델의 기반을 마련합니다.


---

*Generated on 2025-09-24 02:37:50*