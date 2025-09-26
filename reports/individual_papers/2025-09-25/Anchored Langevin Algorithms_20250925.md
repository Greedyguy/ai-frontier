---
keywords:
  - Langevin Dynamics
  - Heavy-Tailed Distributions
  - Wasserstein Distance
  - Anchored Langevin Dynamics
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19455
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:54:32.057964",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Langevin Dynamics",
    "Heavy-Tailed Distributions",
    "Wasserstein Distance",
    "Anchored Langevin Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Langevin Dynamics": 0.82,
    "Heavy-Tailed Distributions": 0.71,
    "Wasserstein Distance": 0.77,
    "Anchored Langevin Dynamics": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Langevin diffusion",
        "canonical": "Langevin Dynamics",
        "aliases": [
          "Langevin process"
        ],
        "category": "specific_connectable",
        "rationale": "Langevin Dynamics is a foundational concept in stochastic processes and is crucial for linking to related sampling methods in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "heavy-tailed distributions",
        "canonical": "Heavy-Tailed Distributions",
        "aliases": [
          "heavy tails"
        ],
        "category": "unique_technical",
        "rationale": "Understanding heavy-tailed distributions is essential for advanced statistical modeling and links to specialized probabilistic methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.81,
        "link_intent_score": 0.71
      },
      {
        "surface": "2-Wasserstein distance",
        "canonical": "Wasserstein Distance",
        "aliases": [
          "Earth Mover's Distance"
        ],
        "category": "unique_technical",
        "rationale": "The Wasserstein Distance is a key metric in optimal transport theory, facilitating connections to various applications in machine learning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "anchored Langevin dynamics",
        "canonical": "Anchored Langevin Dynamics",
        "aliases": [
          "anchored Langevin"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach addresses limitations in traditional Langevin methods, offering a new perspective for sampling non-differentiable and heavy-tailed targets.",
        "novelty_score": 0.88,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
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
      "candidate_surface": "Langevin diffusion",
      "resolved_canonical": "Langevin Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "heavy-tailed distributions",
      "resolved_canonical": "Heavy-Tailed Distributions",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.81,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "2-Wasserstein distance",
      "resolved_canonical": "Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "anchored Langevin dynamics",
      "resolved_canonical": "Anchored Langevin Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Anchored Langevin Algorithms

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19455.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19455](https://arxiv.org/abs/2509.19455)

## 🔗 유사한 논문
- [[2025-09-22/A noise-corrected Langevin algorithm and sampling by half-denoising_20250922|A noise-corrected Langevin algorithm and sampling by half-denoising]] (83.3% similar)
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (82.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (81.9% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.4% similar)
- [[2025-09-19/Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters_20250919|Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Langevin Dynamics|Langevin Dynamics]]
**⚡ Unique Technical**: [[keywords/Heavy-Tailed Distributions|Heavy-Tailed Distributions]], [[keywords/Wasserstein Distance|Wasserstein Distance]], [[keywords/Anchored Langevin Dynamics|Anchored Langevin Dynamics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19455v1 Announce Type: cross 
Abstract: Standard first-order Langevin algorithms such as the unadjusted Langevin algorithm (ULA) are obtained by discretizing the Langevin diffusion and are widely used for sampling in machine learning because they scale to high dimensions and large datasets. However, they face two key limitations: (i) they require differentiable log-densities, excluding targets with non-differentiable components; and (ii) they generally fail to sample heavy-tailed targets. We propose anchored Langevin dynamics, a unified approach that accommodates non-differentiable targets and certain classes of heavy-tailed distributions. The method replaces the original potential with a smooth reference potential and modifies the Langevin diffusion via multiplicative scaling. We establish non-asymptotic guarantees in the 2-Wasserstein distance to the target distribution and provide an equivalent formulation derived via a random time change of the Langevin diffusion. We provide numerical experiments to illustrate the theory and practical performance of our proposed approach.

## 📝 요약

이 논문은 비분화 가능 대상과 특정 유형의 두꺼운 꼬리 분포를 처리할 수 있는 앵커드 랑주뱅 동역학을 제안합니다. 이는 기존의 랑주뱅 알고리즘이 가진 비분화 가능 로그 밀도와 두꺼운 꼬리 분포 샘플링의 한계를 극복합니다. 제안된 방법은 원래의 잠재함수를 매끄러운 참조 잠재함수로 대체하고, 랑주뱅 확산을 곱셈적 스케일링으로 수정합니다. 2-바서슈타인 거리에서 목표 분포에 대한 비대칭적 보장을 제공하며, 랑주뱅 확산의 무작위 시간 변화를 통해 동등한 공식화를 제시합니다. 수치 실험을 통해 이론과 실용적 성능을 입증합니다.

## 🎯 주요 포인트

- 1. 기존의 일차 랑주뱅 알고리즘은 비분화 가능한 로그 밀도를 처리할 수 없고, 무거운 꼬리를 가진 분포를 샘플링하는 데 실패한다는 한계를 가진다.
- 2. 제안된 앵커드 랑주뱅 다이내믹스는 비분화 가능한 목표와 특정 클래스의 무거운 꼬리 분포를 수용할 수 있는 통합 접근법이다.
- 3. 이 방법은 원래의 포텐셜을 부드러운 참조 포텐셜로 대체하고, 랑주뱅 확산을 곱셈적 스케일링으로 수정한다.
- 4. 목표 분포에 대한 2-바서슈타인 거리에서의 비점근적 보장을 확립하고, 랑주뱅 확산의 랜덤 시간 변화를 통한 동등한 공식화를 제공한다.
- 5. 제안된 접근법의 이론적 및 실질적 성능을 설명하기 위한 수치 실험을 제공한다.


---

*Generated on 2025-09-25 16:54:32*