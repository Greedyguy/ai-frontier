<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:50:09.811554",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Exemplar Theory",
    "Large Language Model",
    "Global Explanation Methods"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.92,
    "Exemplar Theory": 0.78,
    "Large Language Model": 0.85,
    "Global Explanation Methods": 0.8
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
        "rationale": "Central to the paper's methodology and connects with existing literature on neural networks for graph data.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "Exemplar Theory",
        "canonical": "Exemplar Theory",
        "aliases": [
          "Exemplar-based Approach"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel application of cognitive science theory to GNN interpretability, enhancing cross-disciplinary links.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Utilized in the paper for rule derivation, connecting with the broader trend of language model applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Global Explanation Methods",
        "canonical": "Global Explanation Methods",
        "aliases": [
          "Global Explainers"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on the underdeveloped area of global interpretability in GNNs, offering a new perspective.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "node classification",
      "motif discovery",
      "coverage maximization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Exemplar Theory",
      "resolved_canonical": "Exemplar Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Global Explanation Methods",
      "resolved_canonical": "Global Explanation Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# GnnXemplar: Exemplars to Explanations - Natural Language Rules for Global GNN Interpretability

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18376.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18376](https://arxiv.org/abs/2509.18376)

## 🔗 유사한 논문
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (90.6% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (84.2% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (83.7% similar)
- [[2025-09-22/Generating Part-Based Global Explanations Via Correspondence_20250922|Generating Part-Based Global Explanations Via Correspondence]] (83.4% similar)
- [[2025-09-24/Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying_20250924|Graph Neural Networks with Similarity-Navigated Probabilistic Feature Copying]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Exemplar Theory|Exemplar Theory]], [[keywords/Global Explanation Methods|Global Explanation Methods]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18376v1 Announce Type: new 
Abstract: Graph Neural Networks (GNNs) are widely used for node classification, yet their opaque decision-making limits trust and adoption. While local explanations offer insights into individual predictions, global explanation methods, those that characterize an entire class, remain underdeveloped. Existing global explainers rely on motif discovery in small graphs, an approach that breaks down in large, real-world settings where subgraph repetition is rare, node attributes are high-dimensional, and predictions arise from complex structure-attribute interactions. We propose GnnXemplar, a novel global explainer inspired from Exemplar Theory from cognitive science. GnnXemplar identifies representative nodes in the GNN embedding space, exemplars, and explains predictions using natural language rules derived from their neighborhoods. Exemplar selection is framed as a coverage maximization problem over reverse k-nearest neighbors, for which we provide an efficient greedy approximation. To derive interpretable rules, we employ a self-refining prompt strategy using large language models (LLMs). Experiments across diverse benchmarks show that GnnXemplar significantly outperforms existing methods in fidelity, scalability, and human interpretability, as validated by a user study with 60 participants.

## 📝 요약

이 논문은 그래프 신경망(GNN)의 전반적인 설명을 제공하는 새로운 방법론인 GnnXemplar를 제안합니다. GnnXemplar는 인지과학의 전형 이론에서 영감을 받아, GNN 임베딩 공간에서 대표 노드(전형)를 식별하고, 이들의 주변 정보를 바탕으로 자연어 규칙을 통해 예측을 설명합니다. 전형 선택은 역 k-최근접 이웃을 통한 커버리지 최대화 문제로 설정되며, 효율적인 탐욕적 근사 방법을 제공합니다. 또한, 대형 언어 모델(LLM)을 활용한 자기 정제 프롬프트 전략으로 해석 가능한 규칙을 도출합니다. 다양한 벤치마크 실험 결과, GnnXemplar는 기존 방법들보다 충실도, 확장성, 인간 해석성에서 뛰어난 성능을 보이며, 60명의 참가자를 대상으로 한 사용자 연구에서도 이를 검증했습니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN)의 불투명한 의사결정 과정을 극복하기 위해 GnnXemplar라는 새로운 글로벌 설명 방법을 제안합니다.
- 2. GnnXemplar는 인지 과학의 전형 이론에서 영감을 받아 GNN 임베딩 공간에서 대표 노드를 식별하고, 이웃으로부터 자연어 규칙을 도출하여 예측을 설명합니다.
- 3. 전형 선택은 역 k-최근접 이웃에 대한 커버리지 최대화 문제로 설정되며, 효율적인 탐욕적 근사 방법을 제공합니다.
- 4. 해석 가능한 규칙을 도출하기 위해 대형 언어 모델(LLM)을 활용한 자기 정제 프롬프트 전략을 사용합니다.
- 5. 다양한 벤치마크 실험에서 GnnXemplar는 기존 방법들에 비해 충실도, 확장성, 인간 해석성에서 뛰어난 성능을 보였으며, 60명의 참가자를 대상으로 한 사용자 연구에서 검증되었습니다.


---

*Generated on 2025-09-24 14:50:09*