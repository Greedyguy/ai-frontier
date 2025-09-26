---
keywords:
  - HénonNets
  - Hamiltonian Systems
  - Symplectic Integrators
  - Time-Adaptive HénonNets
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20212
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:46:33.526835",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HénonNets",
    "Hamiltonian Systems",
    "Symplectic Integrators",
    "Time-Adaptive HénonNets"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HénonNets": 0.78,
    "Hamiltonian Systems": 0.82,
    "Symplectic Integrators": 0.79,
    "Time-Adaptive HénonNets": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HénonNets",
        "canonical": "HénonNets",
        "aliases": [
          "Henon Nets"
        ],
        "category": "unique_technical",
        "rationale": "HénonNets are a specific type of neural network architecture relevant to the study of Hamiltonian systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hamiltonian systems",
        "canonical": "Hamiltonian Systems",
        "aliases": [
          "Hamiltonian dynamics"
        ],
        "category": "broad_technical",
        "rationale": "Hamiltonian systems are a fundamental concept in physics and mathematics, providing a strong link to related studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Symplectic integrators",
        "canonical": "Symplectic Integrators",
        "aliases": [
          "Symplectic methods"
        ],
        "category": "specific_connectable",
        "rationale": "Symplectic integrators are crucial for numerical solutions in Hamiltonian systems, linking to computational techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "T-HénonNets",
        "canonical": "Time-Adaptive HénonNets",
        "aliases": [
          "T-Henon Nets"
        ],
        "category": "unique_technical",
        "rationale": "T-HénonNets represent an advancement in neural network architectures for adaptive time-stepping in Hamiltonian systems.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "measurement data",
      "numerical experiments",
      "universal approximation theorems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HénonNets",
      "resolved_canonical": "HénonNets",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hamiltonian systems",
      "resolved_canonical": "Hamiltonian Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Symplectic integrators",
      "resolved_canonical": "Symplectic Integrators",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "T-HénonNets",
      "resolved_canonical": "Time-Adaptive HénonNets",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Time-adaptive H\'enonNets for separable Hamiltonian systems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20212.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20212](https://arxiv.org/abs/2509.20212)

## 🔗 유사한 논문
- [[2025-09-22/Time-adaptive SympNets for separable Hamiltonian systems_20250922|Time-adaptive SympNets for separable Hamiltonian systems]] (94.7% similar)
- [[2025-09-23/Data-efficient Kernel Methods for Learning Hamiltonian Systems_20250923|Data-efficient Kernel Methods for Learning Hamiltonian Systems]] (82.8% similar)
- [[2025-09-23/Deep Hierarchical Learning with Nested Subspace Networks_20250923|Deep Hierarchical Learning with Nested Subspace Networks]] (79.7% similar)
- [[2025-09-17/Floating-Body Hydrodynamic Neural Networks_20250917|Floating-Body Hydrodynamic Neural Networks]] (79.5% similar)
- [[2025-09-25/Hyperspectral Adapter for Semantic Segmentation with Vision Foundation Models_20250925|Hyperspectral Adapter for Semantic Segmentation with Vision Foundation Models]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Hamiltonian Systems|Hamiltonian Systems]]
**🔗 Specific Connectable**: [[keywords/Symplectic Integrators|Symplectic Integrators]]
**⚡ Unique Technical**: [[keywords/HénonNets|HénonNets]], [[keywords/Time-Adaptive HénonNets|Time-Adaptive HénonNets]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20212v1 Announce Type: new 
Abstract: Measurement data is often sampled irregularly, i.e., not on equidistant time grids. This is also true for Hamiltonian systems. However, existing machine learning methods, which learn symplectic integrators, such as SympNets [1] and H\'enonNets [2] still require training data generated by fixed step sizes. To learn time-adaptive symplectic integrators, an extension to SympNets called TSympNets is introduced in [3]. The aim of this work is to do a similar extension for H\'enonNets. We propose a novel neural network architecture called T-H\'enonNets, which is symplectic by design and can handle adaptive time steps. We also extend the T-H\'enonNet architecture to non-autonomous Hamiltonian systems. Additionally, we provide universal approximation theorems for both new architectures for separable Hamiltonian systems and discuss why it is difficult to handle non-separable Hamiltonian systems with the proposed methods. To investigate these theoretical approximation capabilities, we perform different numerical experiments.

## 📝 요약

이 논문은 불규칙하게 샘플링된 데이터를 처리할 수 있는 새로운 신경망 구조인 T-HénonNets를 제안합니다. 기존의 HénonNets를 확장하여 시간 적응형 심플렉틱 적분기를 학습할 수 있도록 설계되었습니다. 또한, T-HénonNets는 비자율적 해밀토니안 시스템에도 적용할 수 있으며, 분리 가능한 해밀토니안 시스템에 대한 보편 근사 정리를 제공합니다. 제안된 방법이 비분리 가능한 해밀토니안 시스템을 다루기 어려운 이유도 논의됩니다. 이론적 근사 능력을 검증하기 위해 다양한 수치 실험이 수행되었습니다.

## 🎯 주요 포인트

- 1. 기존의 SympNets와 HénonNets는 고정된 시간 간격의 데이터를 필요로 하지만, T-HénonNets는 적응형 시간 간격을 처리할 수 있는 새로운 신경망 구조를 제안합니다.
- 2. T-HénonNets는 설계상 심플렉틱하며, 비자율적인 해밀토니안 시스템에도 확장할 수 있습니다.
- 3. 분리 가능한 해밀토니안 시스템에 대한 새로운 아키텍처의 보편적 근사 정리를 제공하고, 비분리 가능한 시스템에 대한 어려움을 논의합니다.
- 4. 이론적 근사 능력을 조사하기 위해 다양한 수치 실험을 수행합니다.


---

*Generated on 2025-09-25 16:46:33*