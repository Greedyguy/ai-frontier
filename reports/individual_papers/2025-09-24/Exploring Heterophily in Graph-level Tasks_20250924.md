<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:56:46.599300",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Heterophily in Graphs",
    "Motif-Based Graph Tasks",
    "Frequency-Adaptive Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Heterophily in Graphs": 0.79,
    "Motif-Based Graph Tasks": 0.77,
    "Frequency-Adaptive Models": 0.75
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
        "rationale": "Graph Neural Networks are central to the study of graph-level tasks, facilitating connections with existing research on neural architectures.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "heterophily",
        "canonical": "Heterophily in Graphs",
        "aliases": [
          "graph heterophily"
        ],
        "category": "unique_technical",
        "rationale": "Heterophily is a unique concept in graph theory that impacts graph-level learning, offering a novel perspective distinct from homophily.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "motif-based tasks",
        "canonical": "Motif-Based Graph Tasks",
        "aliases": [
          "graph motifs"
        ],
        "category": "unique_technical",
        "rationale": "Motif-based tasks are specific to graph-level learning, providing a unique angle for analyzing local structures within graphs.",
        "novelty_score": 0.71,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "frequency-adaptive model",
        "canonical": "Frequency-Adaptive Models",
        "aliases": [
          "adaptive frequency models"
        ],
        "category": "unique_technical",
        "rationale": "Frequency-adaptive models represent a novel approach to handling spectral components in graph-level tasks, enhancing model flexibility.",
        "novelty_score": 0.74,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "energy-based gradient flow",
      "synthetic datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "heterophily",
      "resolved_canonical": "Heterophily in Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "motif-based tasks",
      "resolved_canonical": "Motif-Based Graph Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.71,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "frequency-adaptive model",
      "resolved_canonical": "Frequency-Adaptive Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.74,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Exploring Heterophily in Graph-level Tasks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18893.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18893](https://arxiv.org/abs/2509.18893)

## 🔗 유사한 논문
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (81.5% similar)
- [[2025-09-19/Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community: Guiding the Fairness of Graphs via New Links]] (81.4% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (80.9% similar)
- [[2025-09-24/Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying_20250924|Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying]] (80.6% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Heterophily in Graphs|Heterophily in Graphs]], [[keywords/Motif-Based Graph Tasks|Motif-Based Graph Tasks]], [[keywords/Frequency-Adaptive Models|Frequency-Adaptive Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18893v1 Announce Type: new 
Abstract: While heterophily has been widely studied in node-level tasks, its impact on graph-level tasks remains unclear. We present the first analysis of heterophily in graph-level learning, combining theoretical insights with empirical validation. We first introduce a taxonomy of graph-level labeling schemes, and focus on motif-based tasks within local structure labeling, which is a popular labeling scheme. Using energy-based gradient flow analysis, we reveal a key insight: unlike frequency-dominated regimes in node-level tasks, motif detection requires mixed-frequency dynamics to remain flexible across multiple spectral components. Our theory shows that motif objectives are inherently misaligned with global frequency dominance, demanding distinct architectural considerations. Experiments on synthetic datasets with controlled heterophily and real-world molecular property prediction support our findings, showing that frequency-adaptive model outperform frequency-dominated models. This work establishes a new theoretical understanding of heterophily in graph-level learning and offers guidance for designing effective GNN architectures.

## 📝 요약

이 논문은 그래프 수준의 학습에서 이질성(heterophily)의 영향을 처음으로 분석한 연구입니다. 저자들은 그래프 수준의 라벨링 체계를 분류하고, 특히 모티프 기반의 로컬 구조 라벨링에 집중했습니다. 에너지 기반의 그래디언트 흐름 분석을 통해, 모티프 검출에는 다양한 주파수 성분에 적응할 수 있는 혼합 주파수 동역학이 필요하다는 중요한 통찰을 제시했습니다. 이론적으로 모티프 목표는 글로벌 주파수 지배와 맞지 않으며, 이를 위해서는 별도의 아키텍처 고려가 필요함을 보여주었습니다. 실험 결과, 이질성이 통제된 합성 데이터셋과 실제 분자 특성 예측에서 주파수 적응 모델이 주파수 지배 모델보다 우수한 성능을 보였습니다. 이 연구는 그래프 수준 학습에서 이질성에 대한 새로운 이론적 이해를 제공하고, 효과적인 그래프 신경망(GNN) 설계를 위한 지침을 제시합니다.

## 🎯 주요 포인트

- 1. 이 논문은 그래프 수준 학습에서의 이질성(heterophily)의 영향을 처음으로 분석하며, 이론적 통찰과 실증적 검증을 결합하여 제시합니다.
- 2. 그래프 수준의 라벨링 체계를 분류하고, 특히 지역 구조 라벨링 내에서 모티프 기반 작업에 초점을 맞춥니다.
- 3. 에너지 기반의 그래디언트 흐름 분석을 통해 모티프 탐지는 여러 스펙트럼 구성 요소에 걸쳐 유연성을 유지하기 위해 혼합 주파수 동역학이 필요하다는 중요한 통찰을 제공합니다.
- 4. 실험 결과, 주파수 적응 모델이 주파수 지배 모델보다 우수하다는 것을 보여주며, 이는 이론적 발견을 뒷받침합니다.
- 5. 이 연구는 그래프 수준 학습에서의 이질성에 대한 새로운 이론적 이해를 확립하고 효과적인 GNN 아키텍처 설계를 위한 지침을 제공합니다.


---

*Generated on 2025-09-24 14:56:46*