---
keywords:
  - Machine Learning
  - Time-dependent Density Functional Theory
  - Autoregressive Neural Operators
  - Electron Dynamics Simulations
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2508.16554
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:40:40.416290",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Time-dependent Density Functional Theory",
    "Autoregressive Neural Operators",
    "Electron Dynamics Simulations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Time-dependent Density Functional Theory": 0.8,
    "Autoregressive Neural Operators": 0.78,
    "Electron Dynamics Simulations": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Machine Learning is a broad technical term that connects various advanced computational techniques, including those used in this paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Time-dependent density functional theory",
        "canonical": "Time-dependent Density Functional Theory",
        "aliases": [
          "TDDFT"
        ],
        "category": "unique_technical",
        "rationale": "TDDFT is a specialized method in quantum mechanics, crucial for linking studies of electron dynamics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Autoregressive neural operators",
        "canonical": "Autoregressive Neural Operators",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, enhancing the connectivity with machine learning applications in physics.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Electron dynamics simulations",
        "canonical": "Electron Dynamics Simulations",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term is specific to the study of electron behavior under perturbations, linking to computational physics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
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
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Time-dependent density functional theory",
      "resolved_canonical": "Time-dependent Density Functional Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Autoregressive neural operators",
      "resolved_canonical": "Autoregressive Neural Operators",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Electron dynamics simulations",
      "resolved_canonical": "Electron Dynamics Simulations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Machine Learning Time Propagators for Time-Dependent Density Functional Theory Simulations

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.16554.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2508.16554](https://arxiv.org/abs/2508.16554)

## 🔗 유사한 논문
- [[2025-09-25/Model-Agnostic AI Framework with Explicit Time Integration for Long-Term Fluid Dynamics Prediction_20250925|Model-Agnostic AI Framework with Explicit Time Integration for Long-Term Fluid Dynamics Prediction]] (81.7% similar)
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (81.7% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (81.6% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.4% similar)
- [[2025-09-24/Machine-Learning Interatomic Potentials for Long-Range Systems_20250924|Machine-Learning Interatomic Potentials for Long-Range Systems]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Time-dependent Density Functional Theory|Time-dependent Density Functional Theory]], [[keywords/Autoregressive Neural Operators|Autoregressive Neural Operators]], [[keywords/Electron Dynamics Simulations|Electron Dynamics Simulations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.16554v2 Announce Type: replace-cross 
Abstract: Time-dependent density functional theory (TDDFT) is a widely used method to investigate electron dynamics under external time-dependent perturbations such as laser fields. In this work, we present a machine learning approach to accelerate electron dynamics simulations based on real time TDDFT using autoregressive neural operators as time-propagators for the electron density. By leveraging physics-informed constraints and featurization, and high-resolution training data, our model achieves superior accuracy and computational speed compared to traditional numerical solvers. We demonstrate the effectiveness of our model on a class of one-dimensional diatomic molecules under the influence of a range of laser parameters. This method has potential in enabling on-the-fly modeling of laser-irradiated molecules and materials by utilizing fast machine learning predictions in a large space of varying experimental parameters of the laser.

## 📝 요약

이 논문에서는 시간 의존 밀도 범함수 이론(TDDFT)을 기반으로 한 전자 동역학 시뮬레이션을 가속화하기 위해 머신러닝 접근법을 제안합니다. 구체적으로, 자귀회귀 신경 연산자를 전자 밀도의 시간 전파자로 활용하여 전통적인 수치 해법보다 뛰어난 정확도와 계산 속도를 달성했습니다. 이 모델은 물리 기반 제약과 특징화, 고해상도 학습 데이터를 활용하여 개발되었으며, 다양한 레이저 매개변수 하에서 일차원 이원자 분자에 대한 실험을 통해 그 효과성을 입증했습니다. 이 방법은 다양한 실험 매개변수 공간에서 레이저로 조사된 분자와 물질의 실시간 모델링을 가능하게 할 잠재력을 지니고 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 실시간 TDDFT 기반 전자 동역학 시뮬레이션을 가속화하기 위해 자가회귀 신경 연산자를 전자 밀도의 시간 전파자로 사용하는 기계 학습 접근법을 제시합니다.
- 2. 물리학 기반 제약 조건과 특징화, 고해상도 학습 데이터를 활용하여 기존 수치 해법보다 우수한 정확도와 계산 속도를 달성합니다.
- 3. 다양한 레이저 매개변수 하에서 1차원 이원자 분자 클래스에 대한 모델의 효과를 입증합니다.
- 4. 이 방법은 레이저 조사 분자 및 재료의 실시간 모델링을 가능하게 하여 다양한 실험적 레이저 매개변수 공간에서 빠른 기계 학습 예측을 활용할 잠재력을 가지고 있습니다.


---

*Generated on 2025-09-26 08:40:40*