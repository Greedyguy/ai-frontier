---
keywords:
  - Sparse Identification of Nonlinear Dynamical Systems
  - Greedy Sampling Neural Network
  - Neural Network
  - Partial Differential Equations
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2405.08613
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:55:29.486728",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Identification of Nonlinear Dynamical Systems",
    "Greedy Sampling Neural Network",
    "Neural Network",
    "Partial Differential Equations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Identification of Nonlinear Dynamical Systems": 0.78,
    "Greedy Sampling Neural Network": 0.81,
    "Neural Network": 0.72,
    "Partial Differential Equations": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Identification of Nonlinear Dynamical Systems",
        "canonical": "Sparse Identification of Nonlinear Dynamical Systems",
        "aliases": [
          "SINDy"
        ],
        "category": "unique_technical",
        "rationale": "This is a core concept of the paper, crucial for understanding the methodology and its applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Greedy Sampling Neural Network",
        "canonical": "Greedy Sampling Neural Network",
        "aliases": [
          "GN-SINDy"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach combining greedy sampling with neural networks, central to the paper's contribution.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.81
      },
      {
        "surface": "Deep Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "A foundational technology in the paper, linking it to broader machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "Partial Differential Equations",
        "canonical": "Partial Differential Equations",
        "aliases": [
          "PDEs"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on modeling complex systems, providing a key link to mathematical modeling.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "data-driven technique",
      "computational costs",
      "snapshot matrix"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Identification of Nonlinear Dynamical Systems",
      "resolved_canonical": "Sparse Identification of Nonlinear Dynamical Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Greedy Sampling Neural Network",
      "resolved_canonical": "Greedy Sampling Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Deep Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Partial Differential Equations",
      "resolved_canonical": "Partial Differential Equations",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GN-SINDy: Greedy Sampling Neural Network in Sparse Identification of Nonlinear Partial Differential Equations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2405.08613.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2405.08613](https://arxiv.org/abs/2405.08613)

## 🔗 유사한 논문
- [[2025-09-17/Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems_20250917|Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems]] (84.7% similar)
- [[2025-09-23/Data-Driven Discovery of PDEs via the Adjoint Method_20250923|Data-Driven Discovery of PDEs via the Adjoint Method]] (80.4% similar)
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (79.3% similar)
- [[2025-09-23/Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs_20250923|Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs]] (78.8% similar)
- [[2025-09-23/DimINO_ Dimension-Informed Neural Operator Learning_20250923|DimINO: Dimension-Informed Neural Operator Learning]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Partial Differential Equations|Partial Differential Equations]]
**⚡ Unique Technical**: [[keywords/Sparse Identification of Nonlinear Dynamical Systems|Sparse Identification of Nonlinear Dynamical Systems]], [[keywords/Greedy Sampling Neural Network|Greedy Sampling Neural Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.08613v2 Announce Type: replace-cross 
Abstract: The sparse identification of nonlinear dynamical systems (SINDy) is a data-driven technique employed for uncovering and representing the fundamental dynamics of intricate systems based on observational data. However, a primary obstacle in the discovery of models for nonlinear partial differential equations (PDEs) lies in addressing the challenges posed by the curse of dimensionality and large datasets. Consequently, the strategic selection of the most informative samples within a given dataset plays a crucial role in reducing computational costs and enhancing the effectiveness of SINDy-based algorithms. To this aim, we employ a greedy sampling approach to the snapshot matrix of a PDE to obtain its valuable samples, which are suitable to train a deep neural network (DNN) in a SINDy framework. SINDy based algorithms often consist of a data collection unit, constructing a dictionary of basis functions, computing the time derivative, and solving a sparse identification problem which ends to regularised least squares minimization. In this paper, we extend the results of a SINDy based deep learning model discovery (DeePyMoD) approach by integrating greedy sampling technique in its data collection unit and new sparsity promoting algorithms in the least squares minimization unit. In this regard we introduce the greedy sampling neural network in sparse identification of nonlinear partial differential equations (GN-SINDy) which blends a greedy sampling method, the DNN, and the SINDy algorithm. In the implementation phase, to show the effectiveness of GN-SINDy, we compare its results with DeePyMoD by using a Python package that is prepared for this purpose on numerous PDE discovery

## 📝 요약

이 논문은 비선형 동역학 시스템의 희소 식별(SINDy) 기법을 개선하기 위해, 고차원 데이터와 대규모 데이터셋의 문제를 해결하는 방법을 제시합니다. 특히, 데이터셋 내에서 가장 유용한 샘플을 전략적으로 선택하여 계산 비용을 줄이고 SINDy 기반 알고리즘의 효율성을 높이는 것을 목표로 합니다. 이를 위해 PDE의 스냅샷 행렬에 탐욕적 샘플링 접근법을 적용하여, 심층 신경망(DNN)을 훈련시키기에 적합한 샘플을 추출합니다. 논문에서는 DeePyMoD 접근법에 탐욕적 샘플링 기법과 새로운 희소성 촉진 알고리즘을 통합한 GN-SINDy를 소개하며, Python 패키지를 사용하여 DeePyMoD와 비교 실험을 통해 GN-SINDy의 효과성을 입증합니다.

## 🎯 주요 포인트

- 1. SINDy는 관찰 데이터를 기반으로 복잡한 시스템의 기본 동역학을 발견하고 표현하는 데이터 기반 기법이다.
- 2. 비선형 편미분 방정식(PDE) 모델 발견의 주요 장애물은 차원의 저주와 대규모 데이터셋 처리에 있다.
- 3. 데이터셋 내에서 가장 정보가 풍부한 샘플을 전략적으로 선택하는 것이 SINDy 기반 알고리즘의 비용 절감과 효과 증대에 중요하다.
- 4. GN-SINDy는 탐욕적 샘플링 방법, 심층 신경망(DNN), SINDy 알고리즘을 결합하여 비선형 PDE의 희소 식별을 수행한다.
- 5. GN-SINDy의 효과를 입증하기 위해 DeePyMoD와 비교하여 여러 PDE 발견 사례에서 Python 패키지를 사용해 결과를 비교하였다.


---

*Generated on 2025-09-24 02:55:29*