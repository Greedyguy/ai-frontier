<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:21:37.989133",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Conditional Generative Modeling",
    "Flow-Based Methods",
    "Diffusion Methods",
    "ImageNet",
    "Fréchet Inception Distance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Conditional Generative Modeling": 0.78,
    "Flow-Based Methods": 0.8,
    "Diffusion Methods": 0.77,
    "ImageNet": 0.82,
    "Fréchet Inception Distance": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Conditional Generative Modeling",
        "canonical": "Conditional Generative Modeling",
        "aliases": [
          "Conditional Generation",
          "Conditional Models"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology and offers a unique approach to generative modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Flow-Based Methods",
        "canonical": "Flow-Based Methods",
        "aliases": [
          "Flow Models",
          "Flow Techniques"
        ],
        "category": "unique_technical",
        "rationale": "Flow-based methods are a specific approach within generative modeling, crucial for understanding the paper's contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion Methods",
        "canonical": "Diffusion Methods",
        "aliases": [
          "Diffusion Models"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion methods are a key component of the paper's approach, relevant for linking to other generative modeling techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "ImageNet-256",
        "canonical": "ImageNet",
        "aliases": [
          "ImageNet Dataset"
        ],
        "category": "broad_technical",
        "rationale": "ImageNet is a widely used dataset in computer vision, providing a strong link to related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      },
      {
        "surface": "FID",
        "canonical": "Fréchet Inception Distance",
        "aliases": [
          "FID Score"
        ],
        "category": "specific_connectable",
        "rationale": "FID is a standard metric for evaluating generative models, facilitating connections to performance evaluation discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
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
      "candidate_surface": "Conditional Generative Modeling",
      "resolved_canonical": "Conditional Generative Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Flow-Based Methods",
      "resolved_canonical": "Flow-Based Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion Methods",
      "resolved_canonical": "Diffusion Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "ImageNet-256",
      "resolved_canonical": "ImageNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "FID",
      "resolved_canonical": "Fréchet Inception Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# CAR-Flow: Condition-Aware Reparameterization Aligns Source and Target for Better Flow Matching

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19300.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19300](https://arxiv.org/abs/2509.19300)

## 🔗 유사한 논문
- [[2025-09-24/Flow marching for a generative PDE foundation model_20250924|Flow marching for a generative PDE foundation model]] (81.9% similar)
- [[2025-09-24/HazeFlow_ Revisit Haze Physical Model as ODE and Non-Homogeneous Haze Generation for Real-World Dehazing_20250924|HazeFlow: Revisit Haze Physical Model as ODE and Non-Homogeneous Haze Generation for Real-World Dehazing]] (81.4% similar)
- [[2025-09-23/Efficient Rectified Flow for Image Fusion_20250923|Efficient Rectified Flow for Image Fusion]] (81.4% similar)
- [[2025-09-19/MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE: one-step generative speech enhancement via conditional mean flow]] (81.1% similar)
- [[2025-09-24/Training Flow Matching Models with Reliable Labels via Self-Purification_20250924|Training Flow Matching Models with Reliable Labels via Self-Purification]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/ImageNet|ImageNet]]
**🔗 Specific Connectable**: [[keywords/Fréchet Inception Distance|Fréchet Inception Distance]]
**⚡ Unique Technical**: [[keywords/Conditional Generative Modeling|Conditional Generative Modeling]], [[keywords/Flow-Based Methods|Flow-Based Methods]], [[keywords/Diffusion Methods|Diffusion Methods]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19300v1 Announce Type: new 
Abstract: Conditional generative modeling aims to learn a conditional data distribution from samples containing data-condition pairs. For this, diffusion and flow-based methods have attained compelling results. These methods use a learned (flow) model to transport an initial standard Gaussian noise that ignores the condition to the conditional data distribution. The model is hence required to learn both mass transport and conditional injection. To ease the demand on the model, we propose Condition-Aware Reparameterization for Flow Matching (CAR-Flow) -- a lightweight, learned shift that conditions the source, the target, or both distributions. By relocating these distributions, CAR-Flow shortens the probability path the model must learn, leading to faster training in practice. On low-dimensional synthetic data, we visualize and quantify the effects of CAR. On higher-dimensional natural image data (ImageNet-256), equipping SiT-XL/2 with CAR-Flow reduces FID from 2.07 to 1.68, while introducing less than 0.6% additional parameters.

## 📝 요약

이 논문은 조건부 생성 모델링에서 조건부 데이터 분포를 학습하는 새로운 방법론인 CAR-Flow를 제안합니다. 기존의 확산 및 흐름 기반 방법은 조건을 무시한 초기 표준 가우시안 노이즈를 조건부 데이터 분포로 변환하는 데 중점을 두었습니다. CAR-Flow는 소스와 타겟 분포를 조건에 맞게 재배치하여 모델이 학습해야 하는 확률 경로를 단축시킵니다. 이를 통해 학습 속도가 빨라지며, ImageNet-256 데이터셋에서 FID 점수를 2.07에서 1.68로 낮추면서도 매개변수 증가를 0.6% 미만으로 유지했습니다.

## 🎯 주요 포인트

- 1. 조건부 생성 모델링은 데이터-조건 쌍을 포함하는 샘플에서 조건부 데이터 분포를 학습하는 것을 목표로 합니다.
- 2. CAR-Flow는 조건을 고려한 재매개변환을 통해 모델의 학습 부담을 줄이고, 훈련 속도를 향상시킵니다.
- 3. CAR-Flow는 소스와 타겟 분포를 재배치하여 모델이 학습해야 하는 확률 경로를 단축시킵니다.
- 4. ImageNet-256 데이터셋에서 CAR-Flow를 적용한 SiT-XL/2 모델은 FID를 2.07에서 1.68로 감소시켰습니다.
- 5. CAR-Flow는 0.6% 미만의 추가 매개변수로 성능 향상을 이루었습니다.


---

*Generated on 2025-09-24 16:21:37*