---
keywords:
  - Generative Motion Planners
  - Neural Network Verification
  - Vision-Language Model
  - Closed-Loop Safety
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19688
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:57:54.549167",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Motion Planners",
    "Neural Network Verification",
    "Vision-Language Model",
    "Closed-Loop Safety"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Motion Planners": 0.88,
    "Neural Network Verification": 0.82,
    "Vision-Language Model": 0.8,
    "Closed-Loop Safety": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generative Motion Planners",
        "canonical": "Generative Motion Planners",
        "aliases": [
          "GMPs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and is specific to the domain of motion planning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Neural Network Verification",
        "canonical": "Neural Network Verification",
        "aliases": [
          "NNV"
        ],
        "category": "specific_connectable",
        "rationale": "The verification of neural networks is a crucial aspect of the paper's methodology and links to broader verification techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This is a trending concept that connects to the paper's evaluation of diverse planners.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Closed-Loop Safety",
        "canonical": "Closed-Loop Safety",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Ensuring safety in closed-loop systems is a unique technical focus of the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
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
      "candidate_surface": "Generative Motion Planners",
      "resolved_canonical": "Generative Motion Planners",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Neural Network Verification",
      "resolved_canonical": "Neural Network Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Closed-Loop Safety",
      "resolved_canonical": "Closed-Loop Safety",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Formal Safety Verification and Refinement for Generative Motion Planners via Certified Local Stabilization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19688.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19688](https://arxiv.org/abs/2509.19688)

## 🔗 유사한 논문
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (82.1% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.8% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.8% similar)
- [[2025-09-25/Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving_20250925|Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving]] (81.7% similar)
- [[2025-09-25/LatentGuard_ Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation_20250925|LatentGuard: Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Network Verification|Neural Network Verification]]
**⚡ Unique Technical**: [[keywords/Generative Motion Planners|Generative Motion Planners]], [[keywords/Closed-Loop Safety|Closed-Loop Safety]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19688v1 Announce Type: cross 
Abstract: We present a method for formal safety verification of learning-based generative motion planners. Generative motion planners (GMPs) offer advantages over traditional planners, but verifying the safety and dynamic feasibility of their outputs is difficult since neural network verification (NNV) tools scale only to a few hundred neurons, while GMPs often contain millions. To preserve GMP expressiveness while enabling verification, our key insight is to imitate the GMP by stabilizing references sampled from the GMP with a small neural tracking controller and then applying NNV to the closed-loop dynamics. This yields reachable sets that rigorously certify closed-loop safety, while the controller enforces dynamic feasibility. Building on this, we construct a library of verified GMP references and deploy them online in a way that imitates the original GMP distribution whenever it is safe to do so, improving safety without retraining. We evaluate across diverse planners, including diffusion, flow matching, and vision-language models, improving safety in simulation (on ground robots and quadcopters) and on hardware (differential-drive robot).

## 📝 요약

이 논문은 학습 기반 생성 모션 플래너(GMP)의 형식적 안전성 검증 방법을 제안합니다. GMP는 전통적인 플래너에 비해 장점이 있지만, 그 출력의 안전성과 동적 실현 가능성을 검증하는 것은 어렵습니다. 이는 신경망 검증(NNV) 도구가 수백 개의 뉴런에만 확장 가능하기 때문입니다. 본 연구의 주요 기여는 GMP의 참조를 작은 신경망 추적 컨트롤러로 안정화하여 폐루프 동역학에 NNV를 적용하는 것입니다. 이를 통해 폐루프 안전성을 엄격하게 인증하는 도달 가능한 집합을 생성하며, 컨트롤러는 동적 실현 가능성을 보장합니다. 이를 기반으로 검증된 GMP 참조 라이브러리를 구축하고, 안전할 때마다 원래 GMP 분포를 모방하여 온라인으로 배포함으로써 재훈련 없이 안전성을 향상시킵니다. 다양한 플래너(확산, 흐름 매칭, 비전-언어 모델)에서 시뮬레이션 및 하드웨어(차동 구동 로봇) 테스트를 통해 안전성을 개선했습니다.

## 🎯 주요 포인트

- 1. 학습 기반 생성 모션 플래너(GMP)의 형식적 안전성 검증을 위한 새로운 방법을 제안합니다.
- 2. GMP의 표현력을 유지하면서 검증을 가능하게 하기 위해, GMP에서 샘플링한 참조를 안정화하는 작은 신경망 추적 컨트롤러를 사용합니다.
- 3. 폐루프 동역학에 NNV를 적용하여 폐루프 안전성을 엄격하게 인증하는 도달 가능한 집합을 얻습니다.
- 4. 검증된 GMP 참조 라이브러리를 구축하고, 안전할 때 원래 GMP 분포를 모방하여 온라인으로 배포하여 안전성을 향상시킵니다.
- 5. 다양한 플래너(확산, 흐름 매칭, 비전-언어 모델)를 평가하여 시뮬레이션 및 하드웨어에서 안전성을 개선합니다.


---

*Generated on 2025-09-25 16:57:54*