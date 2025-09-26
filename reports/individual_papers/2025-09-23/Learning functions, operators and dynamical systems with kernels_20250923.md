---
keywords:
  - Reproducing Kernel Hilbert Space
  - Operator Learning
  - Dynamical Systems
  - Koopman Operator Theory
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18071
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:02:00.583562",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reproducing Kernel Hilbert Space",
    "Operator Learning",
    "Dynamical Systems",
    "Koopman Operator Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reproducing Kernel Hilbert Space": 0.78,
    "Operator Learning": 0.77,
    "Dynamical Systems": 0.79,
    "Koopman Operator Theory": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "reproducing kernel Hilbert spaces",
        "canonical": "Reproducing Kernel Hilbert Space",
        "aliases": [
          "RKHS"
        ],
        "category": "unique_technical",
        "rationale": "Reproducing Kernel Hilbert Spaces are a foundational concept in statistical machine learning, offering a unique perspective on function learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "operator learning",
        "canonical": "Operator Learning",
        "aliases": [
          "Learning Operators"
        ],
        "category": "unique_technical",
        "rationale": "Operator learning extends traditional function learning to more complex structures, providing a bridge to dynamical systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "dynamical systems",
        "canonical": "Dynamical Systems",
        "aliases": [
          "Dynamic Systems"
        ],
        "category": "broad_technical",
        "rationale": "Dynamical systems are crucial for modeling time-dependent phenomena, linking to various fields in science and engineering.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Koopman operator theory",
        "canonical": "Koopman Operator Theory",
        "aliases": [
          "Koopman Theory"
        ],
        "category": "unique_technical",
        "rationale": "Koopman operator theory provides a linear perspective on nonlinear dynamical systems, facilitating advanced analysis and learning techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "scalar-valued learning",
      "suitable operator learning problem"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "reproducing kernel Hilbert spaces",
      "resolved_canonical": "Reproducing Kernel Hilbert Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "operator learning",
      "resolved_canonical": "Operator Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "dynamical systems",
      "resolved_canonical": "Dynamical Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Koopman operator theory",
      "resolved_canonical": "Koopman Operator Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Learning functions, operators and dynamical systems with kernels

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18071.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18071](https://arxiv.org/abs/2509.18071)

## 🔗 유사한 논문
- [[2025-09-23/Learning Neural Antiderivatives_20250923|Learning Neural Antiderivatives]] (79.1% similar)
- [[2025-09-23/Deep Learning as the Disciplined Construction of Tame Objects_20250923|Deep Learning as the Disciplined Construction of Tame Objects]] (77.8% similar)
- [[2025-09-22/KoopCast_ Trajectory Forecasting via Koopman Operators_20250922|KoopCast: Trajectory Forecasting via Koopman Operators]] (77.7% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (77.6% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dynamical Systems|Dynamical Systems]]
**⚡ Unique Technical**: [[keywords/Reproducing Kernel Hilbert Space|Reproducing Kernel Hilbert Space]], [[keywords/Operator Learning|Operator Learning]], [[keywords/Koopman Operator Theory|Koopman Operator Theory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18071v1 Announce Type: new 
Abstract: This expository article presents the approach to statistical machine learning based on reproducing kernel Hilbert spaces. The basic framework is introduced for scalar-valued learning and then extended to operator learning. Finally, learning dynamical systems is formulated as a suitable operator learning problem, leveraging Koopman operator theory.

## 📝 요약

이 논문은 재생커널 힐베르트 공간(RKHS)을 기반으로 한 통계적 기계 학습 접근법을 설명합니다. 먼저 스칼라 값을 학습하는 기본적인 틀을 소개한 후, 이를 연산자 학습으로 확장합니다. 마지막으로, 동적 시스템 학습을 적절한 연산자 학습 문제로 공식화하며, 쿠프만 연산자 이론을 활용합니다. 주요 기여는 RKHS를 통한 학습의 확장성과 동적 시스템에 대한 새로운 접근법 제시입니다.

## 🎯 주요 포인트

- 1. 본 논문은 재생커널 힐베르트 공간을 기반으로 한 통계적 기계 학습 접근법을 제시합니다.
- 2. 스칼라 값을 학습하는 기본적인 프레임워크가 소개됩니다.
- 3. 오퍼레이터 학습으로 확장된 접근법이 설명됩니다.
- 4. Koopman 오퍼레이터 이론을 활용하여 동적 시스템 학습이 적절한 오퍼레이터 학습 문제로 공식화됩니다.


---

*Generated on 2025-09-24 02:02:00*