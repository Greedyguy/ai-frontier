---
keywords:
  - Graph Variate Neural Networks
  - Graph Neural Network
  - Graph Signal Processing
  - EEG Motor-Imagery Classification
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20311
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:48:25.685936",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Variate Neural Networks",
    "Graph Neural Network",
    "Graph Signal Processing",
    "EEG Motor-Imagery Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Variate Neural Networks": 0.88,
    "Graph Neural Network": 0.85,
    "Graph Signal Processing": 0.8,
    "EEG Motor-Imagery Classification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Variate Neural Networks",
        "canonical": "Graph Variate Neural Networks",
        "aliases": [
          "GVNNs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel neural network architecture that extends GNNs for spatio-temporal data, enhancing connectivity with existing graph-based models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "A foundational concept in the paper, linking it to existing graph-based learning models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Signal Processing",
        "canonical": "Graph Signal Processing",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Provides a methodological basis for the proposed GVNNs, connecting to signal processing techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "EEG motor-imagery classification",
        "canonical": "EEG Motor-Imagery Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights a specific application of GVNNs, linking to neuroscience and brain-computer interface research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "Graph Variate Neural Networks",
      "resolved_canonical": "Graph Variate Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Signal Processing",
      "resolved_canonical": "Graph Signal Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "EEG motor-imagery classification",
      "resolved_canonical": "EEG Motor-Imagery Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Graph Variate Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20311.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20311](https://arxiv.org/abs/2509.20311)

## 🔗 유사한 논문
- [[2025-09-22/EvoBrain_ Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network_20250922|EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network]] (85.3% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (85.2% similar)
- [[2025-09-23/Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks_20250923|Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks]] (85.2% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (84.8% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Graph Signal Processing|Graph Signal Processing]]
**⚡ Unique Technical**: [[keywords/Graph Variate Neural Networks|Graph Variate Neural Networks]], [[keywords/EEG Motor-Imagery Classification|EEG Motor-Imagery Classification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20311v1 Announce Type: new 
Abstract: Modelling dynamically evolving spatio-temporal signals is a prominent challenge in the Graph Neural Network (GNN) literature. Notably, GNNs assume an existing underlying graph structure. While this underlying structure may not always exist or is derived independently from the signal, a temporally evolving functional network can always be constructed from multi-channel data. Graph Variate Signal Analysis (GVSA) defines a unified framework consisting of a network tensor of instantaneous connectivity profiles against a stable support usually constructed from the signal itself. Building on GVSA and tools from graph signal processing, we introduce Graph-Variate Neural Networks (GVNNs): layers that convolve spatio-temporal signals with a signal-dependent connectivity tensor combining a stable long-term support with instantaneous, data-driven interactions. This design captures dynamic statistical interdependencies at each time step without ad hoc sliding windows and admits an efficient implementation with linear complexity in sequence length. Across forecasting benchmarks, GVNNs consistently outperform strong graph-based baselines and are competitive with widely used sequence models such as LSTMs and Transformers. On EEG motor-imagery classification, GVNNs achieve strong accuracy highlighting their potential for brain-computer interface applications.

## 📝 요약

이 논문은 동적으로 변화하는 시공간 신호를 모델링하는 새로운 방법론인 Graph-Variate Neural Networks (GVNNs)를 소개합니다. GVNNs는 신호에 의존하는 연결 텐서를 사용하여 시공간 신호를 컨볼루션하며, 이는 장기적 안정성과 순간적인 데이터 기반 상호작용을 결합합니다. 이 접근법은 임의의 슬라이딩 윈도우 없이 각 시점에서의 동적 통계적 상호의존성을 포착하며, 시퀀스 길이에 선형적인 복잡도로 효율적으로 구현됩니다. GVNNs는 예측 벤치마크에서 기존의 강력한 그래프 기반 모델들을 능가하며, LSTMs와 Transformers와 같은 널리 사용되는 시퀀스 모델들과 경쟁력을 보입니다. 특히, EEG 운동-이미지 분류에서 높은 정확도를 보여 뇌-컴퓨터 인터페이스 응용에 잠재력을 나타냅니다.

## 🎯 주요 포인트

- 1. Graph Neural Network(GNN) 문헌에서 동적으로 변화하는 시공간 신호를 모델링하는 것은 중요한 도전 과제입니다.
- 2. Graph Variate Signal Analysis(GVSA)는 신호로부터 안정적인 지지 기반을 구축하여 즉각적인 연결 프로파일의 네트워크 텐서를 정의하는 통합 프레임워크를 제공합니다.
- 3. Graph-Variate Neural Networks(GVNNs)는 신호 의존적 연결 텐서를 사용하여 시공간 신호를 컨볼루션하는 계층을 도입하여 동적 통계적 상호 의존성을 효과적으로 포착합니다.
- 4. GVNNs는 예측 벤치마크에서 강력한 그래프 기반 기준을 지속적으로 능가하며, LSTMs 및 Transformers와 같은 널리 사용되는 시퀀스 모델과 경쟁력을 갖추고 있습니다.
- 5. EEG 운동-이미지 분류에서 GVNNs는 높은 정확도를 달성하여 뇌-컴퓨터 인터페이스 응용 프로그램에서의 잠재력을 강조합니다.


---

*Generated on 2025-09-25 16:48:25*