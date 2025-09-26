---
keywords:
  - Neural Network
  - Low-Rank Neural Network
  - Time-Dependent PDEs
  - Singular Value Decomposition
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16395
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:07:35.964303",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Low-Rank Neural Network",
    "Time-Dependent PDEs",
    "Singular Value Decomposition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Low-Rank Neural Network": 0.82,
    "Time-Dependent PDEs": 0.8,
    "Singular Value Decomposition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Evolutionary Deep Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "EDNN"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader field of neural networks, facilitating connections with other deep learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Low-Rank Evolutionary Deep Neural Network",
        "canonical": "Low-Rank Neural Network",
        "aliases": [
          "LR-EDNN"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach within neural networks, emphasizing low-rank constraints, which is crucial for efficient learning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Time-Dependent Partial Differential Equations",
        "canonical": "Time-Dependent PDEs",
        "aliases": [
          "Time-Dependent PDE"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to mathematical modeling and numerical analysis, essential for scientific computing discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Singular Value Decomposition",
        "canonical": "Singular Value Decomposition",
        "aliases": [
          "SVD"
        ],
        "category": "specific_connectable",
        "rationale": "A key mathematical technique used in the paper, relevant for discussions on dimensionality reduction and matrix factorization.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "numerical solver",
      "parameter evolution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Evolutionary Deep Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Low-Rank Evolutionary Deep Neural Network",
      "resolved_canonical": "Low-Rank Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Time-Dependent Partial Differential Equations",
      "resolved_canonical": "Time-Dependent PDEs",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Singular Value Decomposition",
      "resolved_canonical": "Singular Value Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16395.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16395](https://arxiv.org/abs/2509.16395)

## 🔗 유사한 논문
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.8% similar)
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (81.5% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (81.4% similar)
- [[2025-09-23/Deep Hierarchical Learning with Nested Subspace Networks_20250923|Deep Hierarchical Learning with Nested Subspace Networks]] (80.9% similar)
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Time-Dependent PDEs|Time-Dependent PDEs]], [[keywords/Singular Value Decomposition|Singular Value Decomposition]]
**⚡ Unique Technical**: [[keywords/Low-Rank Neural Network|Low-Rank Neural Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16395v1 Announce Type: cross 
Abstract: We study the Evolutionary Deep Neural Network (EDNN) framework for accelerating numerical solvers of time-dependent partial differential equations (PDEs). We introduce a Low-Rank Evolutionary Deep Neural Network (LR-EDNN), which constrains parameter evolution to a low-rank subspace, thereby reducing the effective dimensionality of training while preserving solution accuracy. The low-rank tangent subspace is defined layer-wise by the singular value decomposition (SVD) of the current network weights, and the resulting update is obtained by solving a well-posed, tractable linear system within this subspace. This design augments the underlying numerical solver with a parameter efficient EDNN component without requiring full fine-tuning of all network weights. We evaluate LR-EDNN on representative PDE problems and compare it against corresponding baselines. Across cases, LR-EDNN achieves comparable accuracy with substantially fewer trainable parameters and reduced computational cost. These results indicate that low-rank constraints on parameter velocities, rather than full-space updates, provide a practical path toward scalable, efficient, and reproducible scientific machine learning for PDEs.

## 📝 요약

이 논문은 시간 의존 편미분 방정식(PDE)의 수치 해법을 가속화하기 위한 진화적 심층 신경망(EDNN) 프레임워크를 연구합니다. 저자들은 저차원 진화적 심층 신경망(LR-EDNN)을 도입하여, 매개변수의 진화를 저차원 부분 공간으로 제한함으로써 훈련의 차원을 줄이면서도 해의 정확성을 유지합니다. 이 방법은 현재 네트워크 가중치의 특이값 분해(SVD)를 통해 층별로 저차원 접선 부분 공간을 정의하고, 이 부분 공간 내에서 잘 정의된 선형 시스템을 해결하여 업데이트를 수행합니다. LR-EDNN은 모든 네트워크 가중치의 완전한 미세 조정 없이도 매개변수 효율적인 EDNN 구성 요소를 제공합니다. 대표적인 PDE 문제에 대한 평가 결과, LR-EDNN은 적은 수의 학습 가능한 매개변수와 감소된 계산 비용으로 유사한 정확성을 달성했습니다. 이는 매개변수 속도에 대한 저차원 제약이 전체 공간 업데이트보다 효율적이고 확장 가능한 과학적 기계 학습을 가능하게 함을 시사합니다.

## 🎯 주요 포인트

- 1. Evolutionary Deep Neural Network(EDNN) 프레임워크는 시간 의존 편미분 방정식(PDE)의 수치 해석기를 가속화하는 데 사용된다.
- 2. Low-Rank Evolutionary Deep Neural Network(LR-EDNN)는 파라미터 진화를 저차원 부분 공간으로 제한하여 훈련의 유효 차원을 줄이면서도 해의 정확성을 유지한다.
- 3. 저차원 접선 부분 공간은 현재 네트워크 가중치의 특이값 분해(SVD)를 통해 계층별로 정의되며, 이 부분 공간 내에서 선형 시스템을 해결하여 업데이트를 얻는다.
- 4. LR-EDNN은 모든 네트워크 가중치의 완전한 미세 조정 없이도 파라미터 효율적인 EDNN 컴포넌트를 제공하여 수치 해석기를 보강한다.
- 5. LR-EDNN은 대표적인 PDE 문제에서 기존의 기준 모델들과 비교하여 유사한 정확성을 유지하면서도 훈련 가능한 파라미터 수와 계산 비용을 크게 줄인다.


---

*Generated on 2025-09-24 02:07:35*