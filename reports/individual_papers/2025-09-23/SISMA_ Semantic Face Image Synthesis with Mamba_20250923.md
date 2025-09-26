---
keywords:
  - Diffusion Models
  - Semantic Image Synthesis
  - Attention Mechanism
  - CelebAMask-HQ Dataset
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17651
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:58:29.675687",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Semantic Image Synthesis",
    "Attention Mechanism",
    "CelebAMask-HQ Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.75,
    "Semantic Image Synthesis": 0.8,
    "Attention Mechanism": 0.78,
    "CelebAMask-HQ Dataset": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion Model"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion Models are central to the paper's methodology and are a distinct concept in image synthesis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Semantic Image Synthesis",
        "canonical": "Semantic Image Synthesis",
        "aliases": [
          "SIS"
        ],
        "category": "unique_technical",
        "rationale": "Semantic Image Synthesis is a specific application area that connects to various image generation techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Attention Layers",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Layer"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanism is a key component in many neural network architectures, facilitating connections to related works.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "CelebAMask-HQ",
        "canonical": "CelebAMask-HQ Dataset",
        "aliases": [
          "CelebAMask-HQ"
        ],
        "category": "unique_technical",
        "rationale": "CelebAMask-HQ is a specific dataset used in the experiments, relevant for linking to similar datasets and studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
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
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Semantic Image Synthesis",
      "resolved_canonical": "Semantic Image Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Attention Layers",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CelebAMask-HQ",
      "resolved_canonical": "CelebAMask-HQ Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SISMA: Semantic Face Image Synthesis with Mamba

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17651.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17651](https://arxiv.org/abs/2509.17651)

## 🔗 유사한 논문
- [[2025-09-23/SynergyNet_ Fusing Generative Priors and State-Space Models for Facial Beauty Prediction_20250923|SynergyNet: Fusing Generative Priors and State-Space Models for Facial Beauty Prediction]] (86.0% similar)
- [[2025-09-23/Achilles' Heel of Mamba_ Essential difficulties of the Mamba architecture demonstrated by synthetic data_20250923|Achilles' Heel of Mamba: Essential difficulties of the Mamba architecture demonstrated by synthetic data]] (84.9% similar)
- [[2025-09-18/Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (82.3% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (82.3% similar)
- [[2025-09-23/Stable Video-Driven Portraits_20250923|Stable Video-Driven Portraits]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Semantic Image Synthesis|Semantic Image Synthesis]], [[keywords/CelebAMask-HQ Dataset|CelebAMask-HQ Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17651v1 Announce Type: new 
Abstract: Diffusion Models have become very popular for Semantic Image Synthesis (SIS) of human faces. Nevertheless, their training and inference is computationally expensive and their computational requirements are high due to the quadratic complexity of attention layers. In this paper, we propose a novel architecture called SISMA, based on the recently proposed Mamba. SISMA generates high quality samples by controlling their shape using a semantic mask at a reduced computational demand. We validated our approach through comprehensive experiments with CelebAMask-HQ, revealing that our architecture not only achieves a better FID score yet also operates at three times the speed of state-of-the-art architectures. This indicates that the proposed design is a viable, lightweight substitute to transformer-based models.

## 📝 요약

이 논문에서는 인간 얼굴의 의미적 이미지 합성을 위한 새로운 아키텍처 SISMA를 제안합니다. SISMA는 최근 제안된 Mamba를 기반으로 하며, 의미적 마스크를 사용해 모양을 제어하면서도 계산 요구량을 줄여 고품질 샘플을 생성합니다. CelebAMask-HQ 데이터셋을 통해 실험한 결과, SISMA는 기존 최첨단 아키텍처보다 세 배 빠르게 작동하면서도 더 나은 FID 점수를 달성했습니다. 이는 SISMA가 트랜스포머 기반 모델의 경량 대안이 될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. Diffusion 모델은 인간 얼굴의 의미적 이미지 합성(SIS)에 널리 사용되지만, 계산 요구 사항이 높고 주의 레이어의 복잡성 때문에 훈련과 추론에 많은 계산 비용이 든다.
- 2. 본 논문에서는 최근 제안된 Mamba를 기반으로 한 새로운 아키텍처 SISMA를 제안하며, 이는 의미적 마스크를 사용하여 모양을 제어하면서도 계산 요구를 줄여 고품질 샘플을 생성한다.
- 3. CelebAMask-HQ 데이터셋을 사용한 실험을 통해 SISMA가 더 나은 FID 점수를 달성하면서도 최첨단 아키텍처보다 3배 빠르게 작동함을 검증하였다.
- 4. 제안된 SISMA 디자인은 transformer 기반 모델의 가벼운 대안으로서의 가능성을 보여준다.


---

*Generated on 2025-09-24 04:58:29*