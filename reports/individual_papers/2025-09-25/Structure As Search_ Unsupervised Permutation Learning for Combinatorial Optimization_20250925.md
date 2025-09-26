---
keywords:
  - Neural Network
  - Combinatorial Optimization
  - Permutation Learning
  - Hamiltonian Cycle
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.04164
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:29:56.044187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Combinatorial Optimization",
    "Permutation Learning",
    "Hamiltonian Cycle"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Combinatorial Optimization": 0.79,
    "Permutation Learning": 0.74,
    "Hamiltonian Cycle": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Net"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the proposed method, capturing combinatorial structures directly.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Combinatorial Optimization",
        "canonical": "Combinatorial Optimization",
        "aliases": [
          "Combinatorial Problem Solving"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on solving combinatorial optimization problems using learned permutations.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Permutation Learning",
        "canonical": "Permutation Learning",
        "aliases": [
          "Learning Permutations"
        ],
        "category": "unique_technical",
        "rationale": "Permutation learning is a novel approach central to the paper's methodology.",
        "novelty_score": 0.78,
        "connectivity_score": 0.59,
        "specificity_score": 0.85,
        "link_intent_score": 0.74
      },
      {
        "surface": "Hamiltonian Cycles",
        "canonical": "Hamiltonian Cycle",
        "aliases": [
          "Hamiltonian Circuit"
        ],
        "category": "specific_connectable",
        "rationale": "Hamiltonian cycles are used in the paper to transform and solve the optimization problem.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Combinatorial Optimization",
      "resolved_canonical": "Combinatorial Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Permutation Learning",
      "resolved_canonical": "Permutation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.59,
        "specificity": 0.85,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Hamiltonian Cycles",
      "resolved_canonical": "Hamiltonian Cycle",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Structure As Search: Unsupervised Permutation Learning for Combinatorial Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.04164.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.04164](https://arxiv.org/abs/2507.04164)

## 🔗 유사한 논문
- [[2025-09-22/AI Methods for Permutation Circuit Synthesis Across Generic Topologies_20250922|AI Methods for Permutation Circuit Synthesis Across Generic Topologies]] (80.0% similar)
- [[2025-09-23/Cover Learning for Large-Scale Topology Representation_20250923|Cover Learning for Large-Scale Topology Representation]] (79.8% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (79.7% similar)
- [[2025-09-22/Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems_20250922|Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems]] (79.5% similar)
- [[2025-09-23/Random functions as data compressors for machine learning of molecular processes_20250923|Random functions as data compressors for machine learning of molecular processes]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Hamiltonian Cycle|Hamiltonian Cycle]]
**⚡ Unique Technical**: [[keywords/Combinatorial Optimization|Combinatorial Optimization]], [[keywords/Permutation Learning|Permutation Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04164v3 Announce Type: replace-cross 
Abstract: We propose a non-autoregressive framework for the Travelling Salesman Problem where solutions emerge directly from learned permutations, without requiring explicit search. By applying a similarity transformation to Hamiltonian cycles, the model learns to approximate permutation matrices via continuous relaxations. Our unsupervised approach achieves competitive performance against classical heuristics, demonstrating that the inherent structure of the problem can effectively guide combinatorial optimization without sequential decision-making. Our method offers concrete evidence that neural networks can directly capture and exploit combinatorial structure.

## 📝 요약

이 논문은 순차적 탐색 없이 학습된 순열을 통해 외판원 문제의 해를 도출하는 비자기회귀적 프레임워크를 제안합니다. 해밀턴 순환에 유사 변환을 적용하여, 모델이 순열 행렬을 연속적 완화로 근사하도록 학습합니다. 비지도 학습 접근법을 통해 전통적인 휴리스틱과 경쟁력 있는 성능을 보이며, 문제의 내재된 구조가 조합 최적화를 효과적으로 안내할 수 있음을 보여줍니다. 이 방법은 신경망이 조합 구조를 직접 포착하고 활용할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 비자기회귀적 프레임워크를 통해 외판원 문제의 해답을 명시적 탐색 없이 학습된 순열에서 직접 도출합니다.
- 2. 해밀턴 사이클에 유사 변환을 적용하여, 모델이 연속적 완화를 통해 순열 행렬을 근사하도록 학습합니다.
- 3. 비지도 학습 접근법으로 고전적 휴리스틱과 경쟁력 있는 성능을 달성합니다.
- 4. 문제의 내재된 구조가 순차적 의사결정 없이 조합 최적화를 효과적으로 안내할 수 있음을 보여줍니다.
- 5. 신경망이 조합적 구조를 직접 포착하고 활용할 수 있음을 구체적으로 입증합니다.


---

*Generated on 2025-09-25 16:29:56*