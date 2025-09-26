---
keywords:
  - Deformable Image Registration
  - Mixture of Experts
  - Attention Mechanism
  - Spatial Heterogeneous Mixture of Experts
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20073
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:12:23.273250",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deformable Image Registration",
    "Mixture of Experts",
    "Attention Mechanism",
    "Spatial Heterogeneous Mixture of Experts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deformable Image Registration": 0.78,
    "Mixture of Experts": 0.82,
    "Attention Mechanism": 0.79,
    "Spatial Heterogeneous Mixture of Experts": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deformable Image Registration",
        "canonical": "Deformable Image Registration",
        "aliases": [
          "DIR"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution and connects to specialized fields in medical imaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mixture of Experts",
        "canonical": "Mixture of Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "A key mechanism introduced in the paper, linking to advanced neural network architectures.",
        "novelty_score": 0.68,
        "connectivity_score": 0.8,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Attention Heads",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Heads"
        ],
        "category": "specific_connectable",
        "rationale": "Integral to the encoder's function, enhancing feature extraction, and connects to known attention models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Spatial Heterogeneous Mixture of Experts",
        "canonical": "Spatial Heterogeneous Mixture of Experts",
        "aliases": [
          "SHMoE"
        ],
        "category": "unique_technical",
        "rationale": "A novel approach for predicting deformation fields, specific to the paper's methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Encoder-Decoder architectures",
      "Dice score",
      "abdominal CT dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deformable Image Registration",
      "resolved_canonical": "Deformable Image Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mixture of Experts",
      "resolved_canonical": "Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.8,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Attention Heads",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Spatial Heterogeneous Mixture of Experts",
      "resolved_canonical": "Spatial Heterogeneous Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SHMoAReg: Spark Deformable Image Registration via Spatial Heterogeneous Mixture of Experts and Attention Heads

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20073.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20073](https://arxiv.org/abs/2509.20073)

## 🔗 유사한 논문
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (84.6% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (83.6% similar)
- [[2025-09-23/GM-MoE_ Low-Light Enhancement with Gated-Mechanism Mixture-of-Experts_20250923|GM-MoE: Low-Light Enhancement with Gated-Mechanism Mixture-of-Experts]] (83.6% similar)
- [[2025-09-22/Ideal Registration? Segmentation is All You Need_20250922|Ideal Registration? Segmentation is All You Need]] (83.4% similar)
- [[2025-09-23/CoBEVMoE_ Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception_20250923|CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mixture of Experts|Mixture of Experts]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Deformable Image Registration|Deformable Image Registration]], [[keywords/Spatial Heterogeneous Mixture of Experts|Spatial Heterogeneous Mixture of Experts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20073v1 Announce Type: new 
Abstract: Encoder-Decoder architectures are widely used in deep learning-based Deformable Image Registration (DIR), where the encoder extracts multi-scale features and the decoder predicts deformation fields by recovering spatial locations. However, current methods lack specialized extraction of features (that are useful for registration) and predict deformation jointly and homogeneously in all three directions. In this paper, we propose a novel expert-guided DIR network with Mixture of Experts (MoE) mechanism applied in both encoder and decoder, named SHMoAReg. Specifically, we incorporate Mixture of Attention heads (MoA) into encoder layers, while Spatial Heterogeneous Mixture of Experts (SHMoE) into the decoder layers. The MoA enhances the specialization of feature extraction by dynamically selecting the optimal combination of attention heads for each image token. Meanwhile, the SHMoE predicts deformation fields heterogeneously in three directions for each voxel using experts with varying kernel sizes. Extensive experiments conducted on two publicly available datasets show consistent improvements over various methods, with a notable increase from 60.58% to 65.58% in Dice score for the abdominal CT dataset. Furthermore, SHMoAReg enhances model interpretability by differentiating experts' utilities across/within different resolution layers. To the best of our knowledge, we are the first to introduce MoE mechanism into DIR tasks. The code will be released soon.

## 📝 요약

이 논문은 심층 학습 기반의 변형 이미지 정합(Deformable Image Registration, DIR)에서 사용되는 인코더-디코더 구조의 한계를 극복하기 위해 새로운 전문가 유도 DIR 네트워크인 SHMoAReg를 제안합니다. 이 네트워크는 인코더와 디코더에 전문가 혼합(Mixture of Experts, MoE) 메커니즘을 적용하여, 인코더에서는 주의 메커니즘(Mixture of Attention heads, MoA)을 통해 이미지 토큰에 최적화된 주의 헤드를 선택하고, 디코더에서는 공간적으로 이질적인 전문가 혼합(SHMoE)을 통해 각 방향으로 이질적인 변형 필드를 예측합니다. 두 개의 공개 데이터셋에서의 실험 결과, 복부 CT 데이터셋에서 Dice 점수가 60.58%에서 65.58%로 향상되는 등 다양한 방법에 비해 일관된 성능 향상을 보였습니다. 또한, SHMoAReg는 다양한 해상도 층에서 전문가의 유용성을 구별하여 모델 해석 가능성을 높입니다. MoE 메커니즘을 DIR 작업에 도입한 것은 이번이 처음입니다. 코드도 곧 공개될 예정입니다.

## 🎯 주요 포인트

- 1. SHMoAReg는 인코더와 디코더에 전문가 혼합(MoE) 메커니즘을 적용한 새로운 DIR 네트워크입니다.
- 2. 인코더 레이어에 주의력 혼합(MoA)을 도입하여 이미지 토큰에 대한 최적의 주의력 조합을 동적으로 선택합니다.
- 3. 디코더 레이어에 공간 이질적 전문가 혼합(SHMoE)을 적용하여 각 방향으로 변형 필드를 이질적으로 예측합니다.
- 4. 두 개의 공개 데이터셋에서 실험한 결과, SHMoAReg는 다양한 방법에 비해 성능이 향상되었으며, 복부 CT 데이터셋에서 Dice 점수가 60.58%에서 65.58%로 증가했습니다.
- 5. SHMoAReg는 전문가의 유용성을 구분하여 모델 해석 가능성을 높입니다.


---

*Generated on 2025-09-26 09:12:23*