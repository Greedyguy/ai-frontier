---
keywords:
  - Discrete Diffusion Models
  - Absorbing Rate Matrices
  - KL Divergence
  - Convergence Guarantees
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.02318
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:44:50.812815",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Discrete Diffusion Models",
    "Absorbing Rate Matrices",
    "KL Divergence",
    "Convergence Guarantees"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Discrete Diffusion Models": 0.78,
    "Absorbing Rate Matrices": 0.82,
    "KL Divergence": 0.75,
    "Convergence Guarantees": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Discrete Diffusion Models",
        "canonical": "Discrete Diffusion Models",
        "aliases": [
          "Discrete State Space Diffusion",
          "Diffusion Models"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and offers a unique perspective on diffusion processes in discrete spaces.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Absorbing Rate Matrices",
        "canonical": "Absorbing Rate Matrices",
        "aliases": [
          "Absorbing Matrices"
        ],
        "category": "unique_technical",
        "rationale": "Absorbing rate matrices are a key focus of the paper, providing a novel approach to improving diffusion model performance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "KL Divergence",
        "canonical": "KL Divergence",
        "aliases": [
          "Kullback-Leibler Divergence"
        ],
        "category": "broad_technical",
        "rationale": "KL Divergence is a fundamental concept in measuring the difference between probability distributions, relevant to the paper's analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Convergence Guarantees",
        "canonical": "Convergence Guarantees",
        "aliases": [
          "Convergence Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "The paper provides new insights into convergence guarantees, which are crucial for validating the model's reliability.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "rate matrices",
      "forward process",
      "error bounds"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Discrete Diffusion Models",
      "resolved_canonical": "Discrete Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Absorbing Rate Matrices",
      "resolved_canonical": "Absorbing Rate Matrices",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "KL Divergence",
      "resolved_canonical": "KL Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Convergence Guarantees",
      "resolved_canonical": "Convergence Guarantees",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Absorb and Converge: Provable Convergence Guarantee for Absorbing Discrete Diffusion Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.02318.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.02318](https://arxiv.org/abs/2506.02318)

## 🔗 유사한 논문
- [[2025-09-23/Discrete Diffusion Models_ Novel Analysis and New Sampler Guarantees_20250923|Discrete Diffusion Models: Novel Analysis and New Sampler Guarantees]] (87.5% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (84.4% similar)
- [[2025-09-23/Wasserstein Convergence of Score-based Generative Models under Semiconvexity and Discontinuous Gradients_20250923|Wasserstein Convergence of Score-based Generative Models under Semiconvexity and Discontinuous Gradients]] (82.5% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (81.2% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/KL Divergence|KL Divergence]]
**🔗 Specific Connectable**: [[keywords/Convergence Guarantees|Convergence Guarantees]]
**⚡ Unique Technical**: [[keywords/Discrete Diffusion Models|Discrete Diffusion Models]], [[keywords/Absorbing Rate Matrices|Absorbing Rate Matrices]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02318v2 Announce Type: replace 
Abstract: Discrete state space diffusion models have shown significant advantages in applications involving discrete data, such as text and image generation. It has also been observed that their performance is highly sensitive to the choice of rate matrices, particularly between uniform and absorbing rate matrices. While empirical results suggest that absorbing rate matrices often yield better generation quality compared to uniform rate matrices, existing theoretical works have largely focused on the uniform rate matrices case. Notably, convergence guarantees and error analyses for absorbing diffusion models are still missing. In this work, we provide the first finite-time error bounds and convergence rate analysis for discrete diffusion models using absorbing rate matrices. We begin by deriving an upper bound on the KL divergence of the forward process, introducing a surrogate initialization distribution to address the challenge posed by the absorbing stationary distribution, which is a singleton and causes the KL divergence to be ill-defined. We then establish the first convergence guarantees for both the $\tau$-leaping and uniformization samplers under absorbing rate matrices, demonstrating improved rates over their counterparts using uniform rate matrices. Furthermore, under suitable assumptions, we provide convergence guarantees without early stopping. Our analysis introduces several new technical tools to address challenges unique to absorbing rate matrices. These include a Jensen-type argument for bounding forward process convergence, novel techniques for bounding absorbing score functions, and a non-divergent upper bound on the score near initialization that removes the need of early-stopping.

## 📝 요약

이 논문은 이산 상태 공간 확산 모델에서 흡수율 행렬을 사용하는 경우의 수렴 보장과 오류 분석을 처음으로 제시합니다. 기존 연구는 주로 균일율 행렬에 집중했으나, 흡수율 행렬이 더 나은 생성 품질을 제공하는 것으로 나타났습니다. 본 연구에서는 KL 발산의 상한을 도출하고, 흡수 정적 분포의 문제를 해결하기 위해 대체 초기화 분포를 도입했습니다. 또한, 흡수율 행렬을 사용하는 $\tau$-leaping 및 균일화 샘플러에 대한 수렴 보장을 확립하여 균일율 행렬을 사용하는 경우보다 개선된 수렴 속도를 보였습니다. 추가적으로, 조기 종료 없이도 수렴을 보장하는 조건을 제시했습니다. 이 과정에서 흡수율 행렬의 고유한 문제를 해결하기 위한 새로운 기술적 도구들을 도입했습니다.

## 🎯 주요 포인트

- 1. 이산 상태 공간 확산 모델은 텍스트 및 이미지 생성과 같은 이산 데이터 관련 응용에서 중요한 이점을 보여주고 있습니다.
- 2. 흡수율 행렬을 사용하는 경우, 유한 시간 오류 경계 및 수렴률 분석을 최초로 제공하였습니다.
- 3. 흡수율 행렬을 사용하는 확산 모델에 대해 $\tau$-leaping 및 균일화 샘플러의 수렴 보장을 확립하였으며, 이는 균일율 행렬을 사용하는 경우보다 개선된 수렴률을 보여줍니다.
- 4. 초기화 근처에서 점수의 비발산 상한을 도입하여 조기 중지를 필요로 하지 않는 수렴 보장을 제공하였습니다.
- 5. 흡수율 행렬에 특화된 새로운 기술 도구를 도입하여, 흡수 점수 함수의 경계를 설정하고, 초기화 분포의 대리 분포를 통해 KL 발산 문제를 해결하였습니다.


---

*Generated on 2025-09-24 02:44:50*