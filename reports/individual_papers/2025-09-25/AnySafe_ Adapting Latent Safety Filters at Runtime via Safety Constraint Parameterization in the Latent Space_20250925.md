---
keywords:
  - Latent Safety Filters
  - Hamilton-Jacobi Reachability Analysis
  - Latent Space
  - Conformal Calibration
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19555
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:55:26.479441",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Safety Filters",
    "Hamilton-Jacobi Reachability Analysis",
    "Latent Space",
    "Conformal Calibration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Safety Filters": 0.78,
    "Hamilton-Jacobi Reachability Analysis": 0.82,
    "Latent Space": 0.7,
    "Conformal Calibration": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "latent safety filters",
        "canonical": "Latent Safety Filters",
        "aliases": [
          "latent safety filter"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution, providing a novel approach to safety in latent spaces.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hamilton-Jacobi reachability analysis",
        "canonical": "Hamilton-Jacobi Reachability Analysis",
        "aliases": [
          "HJ reachability analysis"
        ],
        "category": "specific_connectable",
        "rationale": "This is a foundational method referenced in the paper, connecting to established safety control techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "latent space",
        "canonical": "Latent Space",
        "aliases": [
          "latent spaces"
        ],
        "category": "broad_technical",
        "rationale": "Latent spaces are a fundamental concept in machine learning, relevant to the paper's approach.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "conformal calibration",
        "canonical": "Conformal Calibration",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is used to align the system's safety constraints, offering a novel calibration approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "latent safety filters",
      "resolved_canonical": "Latent Safety Filters",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hamilton-Jacobi reachability analysis",
      "resolved_canonical": "Hamilton-Jacobi Reachability Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "latent space",
      "resolved_canonical": "Latent Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "conformal calibration",
      "resolved_canonical": "Conformal Calibration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# AnySafe: Adapting Latent Safety Filters at Runtime via Safety Constraint Parameterization in the Latent Space

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19555.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19555](https://arxiv.org/abs/2509.19555)

## 🔗 유사한 논문
- [[2025-09-18/Designing Latent Safety Filters using Pre-Trained Vision Models_20250918|Designing Latent Safety Filters using Pre-Trained Vision Models]] (85.2% similar)
- [[2025-09-23/ORN-CBF_ Learning Observation-conditioned Residual Neural Control Barrier Functions via Hypernetworks_20250923|ORN-CBF: Learning Observation-conditioned Residual Neural Control Barrier Functions via Hypernetworks]] (84.0% similar)
- [[2025-09-25/LatentGuard_ Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation_20250925|LatentGuard: Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation]] (82.3% similar)
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (81.5% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Latent Space|Latent Space]]
**🔗 Specific Connectable**: [[keywords/Hamilton-Jacobi Reachability Analysis|Hamilton-Jacobi Reachability Analysis]]
**⚡ Unique Technical**: [[keywords/Latent Safety Filters|Latent Safety Filters]], [[keywords/Conformal Calibration|Conformal Calibration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19555v1 Announce Type: cross 
Abstract: Recent works have shown that foundational safe control methods, such as Hamilton-Jacobi (HJ) reachability analysis, can be applied in the latent space of world models. While this enables the synthesis of latent safety filters for hard-to-model vision-based tasks, they assume that the safety constraint is known a priori and remains fixed during deployment, limiting the safety filter's adaptability across scenarios. To address this, we propose constraint-parameterized latent safety filters that can adapt to user-specified safety constraints at runtime. Our key idea is to define safety constraints by conditioning on an encoding of an image that represents a constraint, using a latent-space similarity measure. The notion of similarity to failure is aligned in a principled way through conformal calibration, which controls how closely the system may approach the constraint representation. The parameterized safety filter is trained entirely within the world model's imagination, treating any image seen by the model as a potential test-time constraint, thereby enabling runtime adaptation to arbitrary safety constraints. In simulation and hardware experiments on vision-based control tasks with a Franka manipulator, we show that our method adapts at runtime by conditioning on the encoding of user-specified constraint images, without sacrificing performance. Video results can be found on https://any-safe.github.io

## 📝 요약

이 논문은 사용자가 지정한 안전 제약 조건에 적응할 수 있는 제약 조건 매개화 잠재 안전 필터를 제안합니다. 기존의 Hamilton-Jacobi 도달 가능성 분석을 잠재 공간에서 활용하여 시뮬레이션 및 실제 실험에서 프랑카 조작기를 사용한 비전 기반 제어 작업에 적용했습니다. 이 방법은 이미지 인코딩을 통해 안전 제약을 정의하고, 잠재 공간 유사성 측정을 통해 실패와의 유사성을 정교하게 조정합니다. 이를 통해 모델이 본 이미지를 테스트 시 제약 조건으로 간주하여 런타임에서 다양한 안전 제약에 적응할 수 있습니다.

## 🎯 주요 포인트

- 1. 기존의 안전 제어 방법인 Hamilton-Jacobi 도달 가능성 분석이 세계 모델의 잠재 공간에 적용될 수 있음을 보여줍니다.
- 2. 제안된 방법은 사용자 지정 안전 제약 조건에 맞춰 런타임에서 적응할 수 있는 제약-매개변수화된 잠재 안전 필터를 제공합니다.
- 3. 안전 제약 조건은 이미지의 인코딩을 기반으로 정의되며, 잠재 공간 유사성 측정을 통해 실패와의 유사성을 원칙적으로 정렬합니다.
- 4. 제안된 안전 필터는 세계 모델의 상상 속에서 훈련되며, 모델이 본 모든 이미지를 잠재적인 테스트 시간 제약 조건으로 처리합니다.
- 5. Franka 매니퓰레이터를 사용한 시뮬레이션 및 하드웨어 실험에서 사용자 지정 제약 이미지의 인코딩에 따라 성능 저하 없이 런타임 적응이 가능함을 입증합니다.


---

*Generated on 2025-09-25 16:55:26*