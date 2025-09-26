---
keywords:
  - Machine Learning
  - Deep Learning
  - Random Nonlinear Projections
  - Protein Folding
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17937
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:27:58.520897",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Deep Learning",
    "Random Nonlinear Projections",
    "Protein Folding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Deep Learning": 0.8,
    "Random Nonlinear Projections": 0.7,
    "Protein Folding": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a central theme of the paper, connecting it to a broad range of computational techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Deep Neural Networks",
        "canonical": "Deep Learning",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a key method discussed for handling large feature spaces, linking to advanced computational models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Random Nonlinear Projections",
        "canonical": "Random Nonlinear Projections",
        "aliases": [
          "Random Projections"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach discussed in the paper for feature space compression, offering unique insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Protein Folding",
        "canonical": "Protein Folding",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Protein Folding is a specific application area for the discussed methods, linking molecular dynamics to computational techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "feature selection",
      "trajectory analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Random Nonlinear Projections",
      "resolved_canonical": "Random Nonlinear Projections",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Protein Folding",
      "resolved_canonical": "Protein Folding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Random functions as data compressors for machine learning of molecular processes

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17937.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17937](https://arxiv.org/abs/2509.17937)

## 🔗 유사한 논문
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (82.2% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (80.9% similar)
- [[2025-09-23/Active Learning for Machine Learning Driven Molecular Dynamics_20250923|Active Learning for Machine Learning Driven Molecular Dynamics]] (80.7% similar)
- [[2025-09-23/Fast, Accurate and Interpretable Graph Classification with Topological Kernels_20250923|Fast, Accurate and Interpretable Graph Classification with Topological Kernels]] (80.3% similar)
- [[2025-09-23/AI-based Methods for Simulating, Sampling, and Predicting Protein Ensembles_20250923|AI-based Methods for Simulating, Sampling, and Predicting Protein Ensembles]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]], [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Protein Folding|Protein Folding]]
**⚡ Unique Technical**: [[keywords/Random Nonlinear Projections|Random Nonlinear Projections]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17937v1 Announce Type: cross 
Abstract: Machine learning (ML) is rapidly transforming the way molecular dynamics simulations are performed and analyzed, from materials modeling to studies of protein folding and function. ML algorithms are often employed to learn low-dimensional representations of conformational landscapes and to cluster trajectories into relevant metastable states. Most of these algorithms require selecting a small number of features that describe the problem of interest. Although deep neural networks can tackle large numbers of input features, the training costs increase with input size, which makes the selection of a subset of features mandatory for most problems of practical interest. Here, we show that random nonlinear projections can be used to compress large feature spaces and make computations faster without substantial loss of information. We describe an efficient way to produce random projections and then exemplify the general procedure for protein folding. For our test cases NTL9 and the double-norleucin variant of the villin headpiece, we find that random compression retains the core static and dynamic information of the original high dimensional feature space and makes trajectory analysis more robust.

## 📝 요약

이 논문은 기계 학습(ML)이 분자 동역학 시뮬레이션에 미치는 영향을 다루며, 특히 단백질 접힘과 기능 연구에 초점을 맞추고 있습니다. ML 알고리즘은 저차원 표현을 학습하고 궤적을 메타안정 상태로 클러스터링하는 데 사용됩니다. 대부분의 알고리즘은 문제를 설명하는 소수의 특징을 선택해야 하며, 이는 입력 크기에 따라 훈련 비용이 증가하기 때문입니다. 본 연구에서는 무작위 비선형 투영을 사용하여 큰 특징 공간을 압축하고 계산 속도를 높이는 방법을 제안합니다. 이 방법은 정보 손실 없이 효율적인 무작위 투영을 생성하며, 단백질 접힘 사례인 NTL9와 villin 헤드피스의 변형체에 적용하여 원래의 고차원 특징 공간의 핵심 정보를 유지하면서 궤적 분석의 견고성을 향상시킵니다.

## 🎯 주요 포인트

- 1. 기계 학습은 분자 동역학 시뮬레이션의 수행 및 분석 방식을 혁신적으로 변화시키고 있다.
- 2. 기계 학습 알고리즘은 저차원 표현을 학습하고 궤적을 관련 준안정 상태로 군집화하는 데 사용된다.
- 3. 입력 특징의 수가 많아질수록 훈련 비용이 증가하므로, 특징의 부분 집합을 선택하는 것이 중요하다.
- 4. 무작위 비선형 투영을 사용하여 큰 특징 공간을 압축하고 계산 속도를 향상시킬 수 있다.
- 5. 무작위 압축은 원래의 고차원 특징 공간의 핵심 정적 및 동적 정보를 유지하면서 궤적 분석을 더 견고하게 만든다.


---

*Generated on 2025-09-24 02:27:58*