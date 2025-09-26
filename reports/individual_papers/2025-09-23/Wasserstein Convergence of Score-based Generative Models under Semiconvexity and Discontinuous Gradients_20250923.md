---
keywords:
  - Score-based Generative Models
  - Wasserstein Convergence
  - Semiconvexity
  - Gaussian Mixtures
  - Reverse Diffusion Process
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.03432
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:42:07.268362",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Score-based Generative Models",
    "Wasserstein Convergence",
    "Semiconvexity",
    "Gaussian Mixtures",
    "Reverse Diffusion Process"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Score-based Generative Models": 0.78,
    "Wasserstein Convergence": 0.77,
    "Semiconvexity": 0.75,
    "Gaussian Mixtures": 0.7,
    "Reverse Diffusion Process": 0.76
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Score-based Generative Models",
        "canonical": "Score-based Generative Models",
        "aliases": [
          "SGMs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contributions and represents a specific class of generative models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Wasserstein Convergence",
        "canonical": "Wasserstein Convergence",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper provides new theoretical insights into this concept, which is crucial for understanding convergence in generative models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semiconvexity",
        "canonical": "Semiconvexity",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Semiconvexity is a key mathematical property leveraged in the paper to establish convergence results.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gaussian Mixtures",
        "canonical": "Gaussian Mixtures",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Gaussian mixtures are a common example of complex distributions discussed in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.72,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reverse Diffusion Process",
        "canonical": "Reverse Diffusion Process",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This process is fundamental to the functioning of SGMs and is a core concept in the paper.",
        "novelty_score": 0.66,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.76
      }
    ],
    "ban_list_suggestions": [
      "data distribution",
      "performance",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Score-based Generative Models",
      "resolved_canonical": "Score-based Generative Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Wasserstein Convergence",
      "resolved_canonical": "Wasserstein Convergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semiconvexity",
      "resolved_canonical": "Semiconvexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gaussian Mixtures",
      "resolved_canonical": "Gaussian Mixtures",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.72,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reverse Diffusion Process",
      "resolved_canonical": "Reverse Diffusion Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.76
      }
    }
  ]
}
-->

# Wasserstein Convergence of Score-based Generative Models under Semiconvexity and Discontinuous Gradients

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.03432.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.03432](https://arxiv.org/abs/2505.03432)

## 🔗 유사한 논문
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (81.8% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (81.6% similar)
- [[2025-09-19/A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation_20250919|A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation]] (79.8% similar)
- [[2025-09-23/DoubleGen_ Debiased Generative Modeling of Counterfactuals_20250923|DoubleGen: Debiased Generative Modeling of Counterfactuals]] (79.6% similar)
- [[2025-09-22/Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation_20250922|Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gaussian Mixtures|Gaussian Mixtures]]
**⚡ Unique Technical**: [[keywords/Score-based Generative Models|Score-based Generative Models]], [[keywords/Wasserstein Convergence|Wasserstein Convergence]], [[keywords/Semiconvexity|Semiconvexity]], [[keywords/Reverse Diffusion Process|Reverse Diffusion Process]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.03432v2 Announce Type: replace 
Abstract: Score-based Generative Models (SGMs) approximate a data distribution by perturbing it with Gaussian noise and subsequently denoising it via a learned reverse diffusion process. These models excel at modeling complex data distributions and generating diverse samples, achieving state-of-the-art performance across domains such as computer vision, audio generation, reinforcement learning, and computational biology. Despite their empirical success, existing Wasserstein-2 convergence analysis typically assume strong regularity conditions-such as smoothness or strict log-concavity of the data distribution-that are rarely satisfied in practice. In this work, we establish the first non-asymptotic Wasserstein-2 convergence guarantees for SGMs targeting semiconvex distributions with potentially discontinuous gradients. Our upper bounds are explicit and sharp in key parameters, achieving optimal dependence of $O(\sqrt{d})$ on the data dimension $d$ and convergence rate of order one. The framework accommodates a wide class of practically relevant distributions, including symmetric modified half-normal distributions, Gaussian mixtures, double-well potentials, and elastic net potentials. By leveraging semiconvexity without requiring smoothness assumptions on the potential such as differentiability, our results substantially broaden the theoretical foundations of SGMs, bridging the gap between empirical success and rigorous guarantees in non-smooth, complex data regimes.

## 📝 요약

이 논문은 Score-based Generative Models (SGMs)의 Wasserstein-2 수렴 보장을 비대칭적이고 비연속적인 기울기를 가진 반볼록 분포에 대해 최초로 제시합니다. 기존의 분석은 매끄러움이나 엄격한 로그 오목성과 같은 강한 정규성을 가정했으나, 본 연구는 이러한 가정 없이도 명시적이고 날카로운 상한을 제공하여 데이터 차원 $d$에 대해 $O(\sqrt{d})$의 최적 의존성을 달성합니다. 이로써 대칭 수정 반정규 분포, 가우시안 혼합, 이중 우물 포텐셜, 엘라스틱 넷 포텐셜 등 다양한 분포를 포괄하며, SGMs의 이론적 기반을 확장하여 복잡한 데이터 환경에서의 경험적 성공과 엄밀한 보장 간의 간극을 좁힙니다.

## 🎯 주요 포인트

- 1. Score-based Generative Models(SGMs)는 복잡한 데이터 분포를 모델링하고 다양한 샘플을 생성하는 데 뛰어난 성능을 보인다.
- 2. 기존의 Wasserstein-2 수렴 분석은 데이터 분포의 매끄러움이나 엄격한 로그 볼록성 같은 강한 정규성 조건을 가정하지만, 실제로는 드물게 만족된다.
- 3. 본 연구는 잠재적으로 불연속적인 기울기를 가진 반볼록 분포를 대상으로 하는 SGMs에 대해 최초의 비점근적 Wasserstein-2 수렴 보장을 확립했다.
- 4. 제안된 상한은 데이터 차원 $d$에 대해 $O(\sqrt{d})$의 최적 의존성과 1차 수렴 속도를 달성하며, 대칭 수정 반정규 분포, 가우시안 혼합, 이중 우물 포텐셜, 탄성 네트 포텐셜을 포함한 다양한 분포를 포괄한다.
- 5. 본 연구는 매끄러움 가정 없이 반볼록성을 활용하여 SGMs의 이론적 기초를 확장하고, 비매끄러운 복잡한 데이터 환경에서의 경험적 성공과 엄격한 보장 사이의 격차를 줄인다.


---

*Generated on 2025-09-24 02:42:07*