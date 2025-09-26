---
keywords:
  - Graph Neural Network
  - Self-supervised Learning
  - Neural Circuitry Inference
  - Ring Attractor Networks
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17174
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:20:15.748901",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Self-supervised Learning",
    "Neural Circuitry Inference",
    "Ring Attractor Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.92,
    "Self-supervised Learning": 0.85,
    "Neural Circuitry Inference": 0.78,
    "Ring Attractor Networks": 0.72
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
          "Graph Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the study, GNNs are used to model neural interactions and infer connectivity.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "Self-supervised structure learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervised structure discovery"
        ],
        "category": "specific_connectable",
        "rationale": "The study employs self-supervised learning to infer neural circuitry, linking connectivity and dynamics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neural circuitry inference",
        "canonical": "Neural Circuitry Inference",
        "aliases": [
          "Neural circuit discovery"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application of GNNs in neuroscience, focusing on inferring neural circuits.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Ring attractor networks",
        "canonical": "Ring Attractor Networks",
        "aliases": [
          "Ring attractors"
        ],
        "category": "unique_technical",
        "rationale": "Used as a synthetic data source, these networks are pivotal for testing the model's inference capabilities.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "neural activity",
      "spiking activity",
      "real data"
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
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Self-supervised structure learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neural circuitry inference",
      "resolved_canonical": "Neural Circuitry Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Ring attractor networks",
      "resolved_canonical": "Ring Attractor Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17174.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17174](https://arxiv.org/abs/2509.17174)

## 🔗 유사한 논문
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (84.6% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (84.3% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (84.3% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (83.8% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Neural Circuitry Inference|Neural Circuitry Inference]], [[keywords/Ring Attractor Networks|Ring Attractor Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17174v1 Announce Type: cross 
Abstract: Inferring synaptic connectivity from neural population activity is a fundamental challenge in computational neuroscience, complicated by partial observability and mismatches between inference models and true circuit dynamics. In this study, we propose a graph-based neural inference model that simultaneously predicts neural activity and infers latent connectivity by modeling neurons as interacting nodes in a graph. The architecture features two distinct modules: one for learning structural connectivity and another for predicting future spiking activity via a graph neural network (GNN). Our model accommodates unobserved neurons through auxiliary nodes, allowing for inference in partially observed circuits. We evaluate this approach using synthetic data from ring attractor networks and real spike recordings from head direction cells in mice. Across a wide range of conditions, including varying recurrent connectivity, external inputs, and incomplete observations, our model consistently outperforms standard baselines, resolving spurious correlations more effectively and recovering accurate weight profiles. When applied to real data, the inferred connectivity aligns with theoretical predictions of continuous attractor models. These results highlight the potential of GNN-based models to infer latent neural circuitry through self-supervised structure learning, while leveraging the spike prediction task to flexibly link connectivity and dynamics across both simulated and biological neural systems.

## 📝 요약

이 연구는 신경 집단 활동으로부터 시냅스 연결성을 추론하는 문제를 해결하기 위해 그래프 기반 신경 추론 모델을 제안합니다. 이 모델은 뉴런을 그래프의 상호작용 노드로 모델링하여 신경 활동을 예측하고 잠재적 연결성을 추론합니다. 두 개의 모듈로 구성된 이 아키텍처는 구조적 연결성을 학습하고 그래프 신경망(GNN)을 통해 미래의 스파이크 활동을 예측합니다. 관측되지 않은 뉴런은 보조 노드를 통해 처리하여 부분적으로 관측된 회로에서도 추론이 가능합니다. 이 모델은 링 어트랙터 네트워크의 합성 데이터와 쥐의 머리 방향 세포에서 얻은 실제 스파이크 기록을 사용하여 평가되었으며, 다양한 조건에서 기존의 기준 모델보다 우수한 성능을 보였습니다. 특히, 잘못된 상관관계를 효과적으로 해결하고 정확한 가중치 프로파일을 복원하는 데 뛰어났습니다. 실제 데이터에 적용했을 때, 추론된 연결성은 이론적 예측과 일치했습니다. 이 결과는 GNN 기반 모델이 자가 지도 구조 학습을 통해 잠재적 신경 회로를 추론할 수 있는 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 그래프 기반 신경 추론 모델을 제안하여 신경 활동을 예측하고 잠재적 연결성을 추론합니다.
- 2. 모델은 구조적 연결성을 학습하는 모듈과 그래프 신경망(GNN)을 통한 미래 스파이크 활동 예측 모듈로 구성됩니다.
- 3. 보조 노드를 통해 관찰되지 않은 뉴런을 수용하여 부분적으로 관찰된 회로에서도 추론이 가능합니다.
- 4. 다양한 조건에서 모델은 표준 기준을 능가하며, 잘못된 상관관계를 효과적으로 해결하고 정확한 가중치 프로파일을 복원합니다.
- 5. 실제 데이터에 적용 시, 추론된 연결성은 연속 어트랙터 모델의 이론적 예측과 일치합니다.


---

*Generated on 2025-09-24 02:20:15*