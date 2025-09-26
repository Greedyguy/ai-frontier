---
keywords:
  - Diffusion Models
  - Probabilistic Inversion
  - Subsurface Modeling
  - Conditional Modeling
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2507.15809
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:40:12.107085",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Probabilistic Inversion",
    "Subsurface Modeling",
    "Conditional Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.88,
    "Probabilistic Inversion": 0.8,
    "Subsurface Modeling": 0.78,
    "Conditional Modeling": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion Process",
          "Diffusion Posterior Sampling"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are central to the paper's methodology and offer a unique approach to generative modeling, making them a key concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Probabilistic inversion",
        "canonical": "Probabilistic Inversion",
        "aliases": [
          "Probabilistic Modeling",
          "Inversion Process"
        ],
        "category": "unique_technical",
        "rationale": "Probabilistic inversion is a specialized technique discussed in the paper, crucial for understanding the application of diffusion models in subsurface modeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multivariate subsurface modeling",
        "canonical": "Subsurface Modeling",
        "aliases": [
          "Geological Modeling",
          "Subsurface Generation"
        ],
        "category": "unique_technical",
        "rationale": "Subsurface modeling is a specific application area that benefits from the discussed methodologies, providing a clear link to geological and geophysical studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.76,
        "specificity_score": 0.79,
        "link_intent_score": 0.78
      },
      {
        "surface": "Conditional modeling",
        "canonical": "Conditional Modeling",
        "aliases": [
          "Conditioning Data",
          "Data Conditioning"
        ],
        "category": "specific_connectable",
        "rationale": "Conditional modeling is a key aspect of the paper's approach, allowing for the integration of various data types, which is essential for linking to data-driven methodologies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
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
      "candidate_surface": "Diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Probabilistic inversion",
      "resolved_canonical": "Probabilistic Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multivariate subsurface modeling",
      "resolved_canonical": "Subsurface Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.76,
        "specificity": 0.79,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Conditional modeling",
      "resolved_canonical": "Conditional Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Diffusion models for multivariate subsurface generation and efficient probabilistic inversion

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.15809.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2507.15809](https://arxiv.org/abs/2507.15809)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (86.6% similar)
- [[2025-09-23/Extract and Diffuse_ Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement_20250923|Extract and Diffuse: Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement]] (83.8% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (83.3% similar)
- [[2025-09-25/Multimodal Atmospheric Super-Resolution With Deep Generative Models_20250925|Multimodal Atmospheric Super-Resolution With Deep Generative Models]] (83.3% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Conditional Modeling|Conditional Modeling]]
**⚡ Unique Technical**: [[keywords/Probabilistic Inversion|Probabilistic Inversion]], [[keywords/Subsurface Modeling|Subsurface Modeling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.15809v2 Announce Type: replace-cross 
Abstract: Diffusion models offer stable training and state-of-the-art performance for deep generative modeling tasks. Here, we consider their use in the context of multivariate subsurface modeling and probabilistic inversion. We first demonstrate that diffusion models enhance multivariate modeling capabilities compared to variational autoencoders and generative adversarial networks. In diffusion modeling, the generative process involves a comparatively large number of time steps with update rules that can be modified to account for conditioning data. We propose different corrections to the popular Diffusion Posterior Sampling approach by Chung et al. (2023). In particular, we introduce a likelihood approximation accounting for the noise-contamination that is inherent in diffusion modeling. We assess performance in a multivariate geological scenario involving facies and correlated acoustic impedance. Conditional modeling is demonstrated using both local hard data (well logs) and nonlinear geophysics (fullstack seismic data). Our tests show significantly improved statistical robustness, enhanced sampling of the posterior probability density function and reduced computational costs, compared to the original approach. The method can be used with both hard and indirect conditioning data, individually or simultaneously. As the inversion is included within the diffusion process, it is faster than other methods requiring an outer-loop around the generative model, such as Markov chain Monte Carlo.

## 📝 요약

이 논문은 확산 모델을 다변량 지하 모델링 및 확률적 역산 문제에 적용한 연구를 다룹니다. 확산 모델은 변분 오토인코더와 생성적 적대 신경망에 비해 다변량 모델링 능력을 향상시킵니다. 저자들은 Chung et al. (2023)의 확산 후방 샘플링 접근법을 수정하여 노이즈 오염을 고려한 우도 근사치를 제안합니다. 이 방법은 다변량 지질 시나리오에서 조건부 모델링을 수행하며, 기존 방법보다 통계적 강건성과 계산 효율성을 개선합니다. 또한, 확산 과정 내에 역산을 포함하여 다른 방법보다 빠른 성능을 보입니다.

## 🎯 주요 포인트

- 1. 확산 모델은 변분 오토인코더와 생성적 적대 신경망에 비해 다변량 모델링 능력을 향상시킨다.
- 2. 확산 모델링에서 생성 과정은 비교적 많은 시간 단계와 조건부 데이터를 고려할 수 있는 업데이트 규칙을 포함한다.
- 3. Chung et al. (2023)의 Diffusion Posterior Sampling 접근법에 대한 여러 수정안을 제안하며, 특히 노이즈 오염을 고려한 가능성 근사를 도입한다.
- 4. 다변량 지질 시나리오에서 조건부 모델링은 지역적 경성 데이터와 비선형 지구물리학 데이터를 사용하여 성능을 평가한다.
- 5. 제안된 방법은 통계적 견고성을 개선하고, 사후 확률 밀도 함수의 샘플링을 향상시키며, 계산 비용을 줄인다.


---

*Generated on 2025-09-26 08:40:12*