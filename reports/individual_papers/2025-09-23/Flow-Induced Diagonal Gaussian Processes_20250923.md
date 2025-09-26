---
keywords:
  - Flow-Induced Diagonal Gaussian Processes
  - Normalising Flow
  - Out-of-Distribution Detection
  - Spectral Regularization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17153
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:45:52.425200",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Flow-Induced Diagonal Gaussian Processes",
    "Normalising Flow",
    "Out-of-Distribution Detection",
    "Spectral Regularization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Flow-Induced Diagonal Gaussian Processes": 0.85,
    "Normalising Flow": 0.78,
    "Out-of-Distribution Detection": 0.82,
    "Spectral Regularization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Flow-Induced Diagonal Gaussian Processes",
        "canonical": "Flow-Induced Diagonal Gaussian Processes",
        "aliases": [
          "FiD-GP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel compression framework introduced in the paper, crucial for understanding its unique contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "normalising-flow priors",
        "canonical": "Normalising Flow",
        "aliases": [
          "normalizing flow"
        ],
        "category": "specific_connectable",
        "rationale": "Normalising flows are a key component in the framework, linking to probabilistic modeling techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Out-of-Distribution detection",
        "canonical": "Out-of-Distribution Detection",
        "aliases": [
          "OoD detection"
        ],
        "category": "specific_connectable",
        "rationale": "OoD detection is a significant application of the framework, relevant to robustness in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "spectral regularisations",
        "canonical": "Spectral Regularization",
        "aliases": [
          "spectral regularisations"
        ],
        "category": "specific_connectable",
        "rationale": "Spectral regularization is crucial for the model's expressiveness and stability, linking to optimization techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "compression framework",
      "neural network's weight uncertainty"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Flow-Induced Diagonal Gaussian Processes",
      "resolved_canonical": "Flow-Induced Diagonal Gaussian Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "normalising-flow priors",
      "resolved_canonical": "Normalising Flow",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Out-of-Distribution detection",
      "resolved_canonical": "Out-of-Distribution Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "spectral regularisations",
      "resolved_canonical": "Spectral Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Flow-Induced Diagonal Gaussian Processes

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17153.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17153](https://arxiv.org/abs/2509.17153)

## 🔗 유사한 논문
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (82.1% similar)
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT: Online Diffusion Reinforcement with Forward Process]] (79.5% similar)
- [[2025-09-18/Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression_20250918|Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression]] (79.2% similar)
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive: Energy Flow Field for End-to-End Autonomous Driving]] (79.1% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Normalising Flow|Normalising Flow]], [[keywords/Out-of-Distribution Detection|Out-of-Distribution Detection]], [[keywords/Spectral Regularization|Spectral Regularization]]
**⚡ Unique Technical**: [[keywords/Flow-Induced Diagonal Gaussian Processes|Flow-Induced Diagonal Gaussian Processes]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17153v1 Announce Type: cross 
Abstract: We present Flow-Induced Diagonal Gaussian Processes (FiD-GP), a compression framework that incorporates a compact inducing weight matrix to project a neural network's weight uncertainty into a lower-dimensional subspace. Critically, FiD-GP relies on normalising-flow priors and spectral regularisations to augment its expressiveness and align the inducing subspace with feature-gradient geometry through a numerically stable projection mechanism objective. Furthermore, we demonstrate how the prediction framework in FiD-GP can help to design a single-pass projection for Out-of-Distribution (OoD) detection. Our analysis shows that FiD-GP improves uncertainty estimation ability on various tasks compared with SVGP-based baselines, satisfies tight spectral residual bounds with theoretically guaranteed OoD detection, and significantly compresses the neural network's storage requirements at the cost of increased inference computation dependent on the number of inducing weights employed. Specifically, in a comprehensive empirical study spanning regression, image classification, semantic segmentation, and out-of-distribution detection benchmarks, it cuts Bayesian training cost by several orders of magnitude, compresses parameters by roughly 51%, reduces model size by about 75%, and matches state-of-the-art accuracy and uncertainty estimation.

## 📝 요약

Flow-Induced Diagonal Gaussian Processes (FiD-GP)는 신경망의 가중치 불확실성을 저차원 공간으로 투영하기 위해 압축 유도 가중치 행렬을 활용하는 프레임워크입니다. FiD-GP는 정규화 흐름 사전과 스펙트럼 정규화를 통해 표현력을 높이고, 유도 하위 공간을 특징-기울기 기하학에 맞추어 수치적으로 안정적인 투영 메커니즘을 제공합니다. 또한, FiD-GP의 예측 프레임워크는 단일 패스 투영을 통해 분포 외 검출(OoD)을 설계할 수 있도록 돕습니다. FiD-GP는 다양한 작업에서 불확실성 추정 능력을 개선하고, 이론적으로 보장된 OoD 검출을 제공하며, 신경망의 저장 요구를 크게 줄입니다. 회귀, 이미지 분류, 의미론적 분할, OoD 검출 벤치마크를 아우르는 실험에서 베이지안 훈련 비용을 크게 줄이고, 매개변수를 약 51% 압축하며, 모델 크기를 약 75% 감소시키면서도 최첨단 정확도와 불확실성 추정을 달성했습니다.

## 🎯 주요 포인트

- 1. FiD-GP는 신경망의 가중치 불확실성을 저차원 부분 공간으로 투영하기 위해 압축 유도 가중치 행렬을 사용하는 압축 프레임워크입니다.
- 2. FiD-GP는 정규화 흐름 사전 및 스펙트럼 정규화를 활용하여 유도 부분 공간을 특징-기울기 기하학과 정렬합니다.
- 3. FiD-GP는 단일 패스 투영을 통해 분포 외 탐지를 설계할 수 있는 예측 프레임워크를 제공합니다.
- 4. FiD-GP는 다양한 작업에서 불확실성 추정 능력을 개선하고, 이론적으로 보장된 분포 외 탐지를 충족하며, 신경망의 저장 요구를 크게 압축합니다.
- 5. FiD-GP는 회귀, 이미지 분류, 의미론적 분할 및 분포 외 탐지 벤치마크에서 베이지안 훈련 비용을 크게 절감하고, 모델 크기를 약 75% 줄이며, 최첨단 정확도와 불확실성 추정을 달성합니다.


---

*Generated on 2025-09-23 23:45:52*