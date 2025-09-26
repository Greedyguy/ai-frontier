<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:27:19.740677",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Topological Feature Compression",
    "Molecular Representation Learning",
    "Higher-order Topological Signals"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Topological Feature Compression": 0.78,
    "Molecular Representation Learning": 0.82,
    "Higher-order Topological Signals": 0.75
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
        "rationale": "Central to the paper's methodology and connects with existing literature on neural networks for graph data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Topological Feature Compression",
        "canonical": "Topological Feature Compression",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach that is specific to the paper's contribution, enhancing the understanding of GNNs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Molecular Representation Learning",
        "canonical": "Molecular Representation Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key application area of the research, linking to broader efforts in cheminformatics and bioinformatics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Higher-order Topological Signals",
        "canonical": "Higher-order Topological Signals",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a complex concept that is central to the paper's methodology, offering potential for unique insights.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "predictive accuracy",
      "computational efficiency",
      "human-interpretable structure"
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
      "candidate_surface": "Topological Feature Compression",
      "resolved_canonical": "Topological Feature Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Molecular Representation Learning",
      "resolved_canonical": "Molecular Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Higher-order Topological Signals",
      "resolved_canonical": "Higher-order Topological Signals",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Topological Feature Compression for Molecular Graph Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.07807.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2508.07807](https://arxiv.org/abs/2508.07807)

## 🔗 유사한 논문
- [[2025-09-23/Fast, Accurate and Interpretable Graph Classification with Topological Kernels_20250923|Fast, Accurate and Interpretable Graph Classification with Topological Kernels]] (85.1% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (83.9% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (83.8% similar)
- [[2025-09-23/Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination_20250923|Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination]] (83.5% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Molecular Representation Learning|Molecular Representation Learning]]
**⚡ Unique Technical**: [[keywords/Topological Feature Compression|Topological Feature Compression]], [[keywords/Higher-order Topological Signals|Higher-order Topological Signals]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.07807v2 Announce Type: replace 
Abstract: Recent advances in molecular representation learning have produced highly effective encodings of molecules for numerous cheminformatics and bioinformatics tasks. However, extracting general chemical insight while balancing predictive accuracy, interpretability, and computational efficiency remains a major challenge. In this work, we introduce a novel Graph Neural Network (GNN) architecture that combines compressed higher-order topological signals with standard molecular features. Our approach captures global geometric information while preserving computational tractability and human-interpretable structure. We evaluate our model across a range of benchmarks, from small-molecule datasets to complex material datasets, and demonstrate superior performance using a parameter-efficient architecture. We achieve the best performing results in both accuracy and robustness across almost all benchmarks. We open source all code \footnote{All code and results can be found on Github https://github.com/rahulkhorana/TFC-PACT-Net}.

## 📝 요약

이 논문에서는 분자 표현 학습의 최신 발전을 바탕으로, 예측 정확성, 해석 가능성, 계산 효율성을 균형 있게 유지하면서 일반적인 화학적 통찰을 추출하는 새로운 그래프 신경망(GNN) 아키텍처를 제안합니다. 이 모델은 압축된 고차원 위상 신호와 표준 분자 특성을 결합하여 전역적인 기하 정보를 포착하면서도 계산 가능성과 해석 가능성을 유지합니다. 다양한 데이터셋에서 평가한 결과, 대부분의 벤치마크에서 정확성과 견고성 면에서 우수한 성능을 보였습니다. 모든 코드는 오픈 소스로 제공됩니다.

## 🎯 주요 포인트

- 1. 새로운 그래프 신경망(GNN) 아키텍처를 제안하여 분자의 전역 기하 정보를 캡처하면서 계산 효율성과 해석 가능성을 유지합니다.
- 2. 제안된 모델은 작은 분자 데이터셋부터 복잡한 물질 데이터셋까지 다양한 벤치마크에서 우수한 성능을 보입니다.
- 3. 매개변수 효율적인 아키텍처를 통해 거의 모든 벤치마크에서 최고 수준의 정확도와 견고성을 달성합니다.
- 4. 모든 코드와 결과는 오픈 소스로 제공되며, GitHub에서 확인할 수 있습니다.


---

*Generated on 2025-09-24 15:27:19*