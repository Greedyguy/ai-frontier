---
keywords:
  - Diffusion Models
  - Straight Consistent Trajectory
  - Consistency Model Distillation
  - Rectified Flow Method
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2502.16972
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:19:00.237833",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Straight Consistent Trajectory",
    "Consistency Model Distillation",
    "Rectified Flow Method"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.72,
    "Straight Consistent Trajectory": 0.78,
    "Consistency Model Distillation": 0.75,
    "Rectified Flow Method": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Pre-trained diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Pre-trained diffusion",
          "Diffusion model"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are a fundamental concept in generative modeling, linking to various machine learning techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.72
      },
      {
        "surface": "Straight Consistent Trajectory",
        "canonical": "Straight Consistent Trajectory",
        "aliases": [
          "SCoT"
        ],
        "category": "unique_technical",
        "rationale": "SCoT is a novel approach combining consistency and rectified flow methods, crucial for understanding advancements in diffusion model distillation.",
        "novelty_score": 0.91,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Consistency model distillation",
        "canonical": "Consistency Model Distillation",
        "aliases": [
          "Consistency distillation"
        ],
        "category": "specific_connectable",
        "rationale": "This method is key in improving sampling efficiency, linking to broader themes in model optimization.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.73,
        "link_intent_score": 0.75
      },
      {
        "surface": "Rectified flow method",
        "canonical": "Rectified Flow Method",
        "aliases": [
          "Rectified flow"
        ],
        "category": "specific_connectable",
        "rationale": "This method is significant for enabling faster sampling in diffusion models, connecting to numerical analysis techniques.",
        "novelty_score": 0.64,
        "connectivity_score": 0.77,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "sampling efficiency",
      "numerical ODE solvers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Pre-trained diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Straight Consistent Trajectory",
      "resolved_canonical": "Straight Consistent Trajectory",
      "decision": "linked",
      "scores": {
        "novelty": 0.91,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Consistency model distillation",
      "resolved_canonical": "Consistency Model Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.73,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Rectified flow method",
      "resolved_canonical": "Rectified Flow Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.64,
        "connectivity": 0.77,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# SCoT: Straight Consistent Trajectory for Pre-Trained Diffusion Model Distillations

**Korean Title:** SCoT: 사전 훈련된 확산 모델 증류를 위한 직선적 일관 궤적

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.16972.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2502.16972](https://arxiv.org/abs/2502.16972)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.6% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.5% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (80.3% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (80.0% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Consistency Model Distillation|Consistency Model Distillation]], [[keywords/Rectified Flow Method|Rectified Flow Method]]
**⚡ Unique Technical**: [[keywords/Straight Consistent Trajectory|Straight Consistent Trajectory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.16972v2 Announce Type: replace-cross 
Abstract: Pre-trained diffusion models are commonly used to generate clean data (e.g., images) from random noises, effectively forming pairs of noises and corresponding clean images. Distillation on these pre-trained models can be viewed as the process of constructing advanced trajectories within the pair to accelerate sampling. For instance, consistency model distillation develops consistent projection functions to regulate trajectories, although sampling efficiency remains a concern. Rectified flow method enforces straight trajectories to enable faster sampling, yet relies on numerical ODE solvers, which may introduce approximation errors. In this work, we bridge the gap between the consistency model and the rectified flow method by proposing a Straight Consistent Trajectory~(SCoT) model. SCoT enjoys the benefits of both approaches for fast sampling, producing trajectories with consistent and straight properties simultaneously. These dual properties are strategically balanced by targeting two critical objectives: (1) regulating the gradient of SCoT's mapping to a constant, (2) ensuring trajectory consistency. Extensive experimental results demonstrate the effectiveness and efficiency of SCoT.

## 🔍 Abstract (한글 번역)

arXiv:2502.16972v2 발표 유형: 교차 교체  
초록: 사전 학습된 확산 모델은 일반적으로 무작위 노이즈로부터 깨끗한 데이터(예: 이미지)를 생성하는 데 사용되며, 이는 효과적으로 노이즈와 해당 깨끗한 이미지의 쌍을 형성합니다. 이러한 사전 학습된 모델에 대한 증류는 샘플링을 가속화하기 위해 쌍 내에서 고급 경로를 구성하는 과정으로 볼 수 있습니다. 예를 들어, 일관성 모델 증류는 경로를 조절하기 위해 일관된 투사 함수를 개발하지만 샘플링 효율성은 여전히 ​​문제입니다. 수정된 흐름 방법은 더 빠른 샘플링을 가능하게 하기 위해 직선 경로를 강제하지만, 근사 오류를 초래할 수 있는 수치적 ODE 해석기에 의존합니다. 이 연구에서는 일관성 모델과 수정된 흐름 방법 간의 격차를 해소하기 위해 직선 일관 경로(SCoT) 모델을 제안합니다. SCoT는 빠른 샘플링을 위해 두 접근 방식의 이점을 동시에 누리며, 일관성과 직선 속성을 동시에 갖춘 경로를 생성합니다. 이러한 이중 속성은 두 가지 중요한 목표를 겨냥하여 전략적으로 균형을 이룹니다: (1) SCoT의 매핑 기울기를 일정하게 조절, (2) 경로 일관성을 보장. 광범위한 실험 결과는 SCoT의 효과성과 효율성을 입증합니다.

## 📝 요약

이 논문은 SCoT(Straight Consistent Trajectory) 모델을 제안하여 사전 학습된 확산 모델의 샘플링 효율성을 향상시킵니다. SCoT는 일관성 모델과 수정된 흐름 방법의 장점을 결합하여, 일관되고 직선적인 경로를 생성함으로써 빠른 샘플링을 가능하게 합니다. 이 모델은 경로의 기울기를 일정하게 유지하고 경로의 일관성을 보장하는 두 가지 목표를 달성합니다. 실험 결과, SCoT 모델이 효과적이고 효율적인 샘플링을 제공함을 입증했습니다.

## 🎯 주요 포인트

- 1. 사전 학습된 확산 모델은 랜덤 노이즈에서 깨끗한 데이터를 생성하는 데 사용되며, 이는 노이즈와 대응되는 깨끗한 이미지의 쌍을 형성합니다.
- 2. SCoT 모델은 일관성과 직선성을 동시에 갖춘 경로를 생성하여 빠른 샘플링을 가능하게 합니다.
- 3. SCoT는 일관성 모델과 수정된 흐름 방법의 장점을 결합하여 샘플링 효율성을 높입니다.
- 4. SCoT의 두 가지 주요 목표는 매핑의 기울기를 일정하게 조절하고 경로의 일관성을 보장하는 것입니다.
- 5. 광범위한 실험 결과는 SCoT의 효과성과 효율성을 입증합니다.


---

*Generated on 2025-09-23 11:19:00*