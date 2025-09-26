---
keywords:
  - Point-RTD
  - Transformer
  - 3D Point Cloud
  - Discriminator-Generator Architecture
  - Chamfer Distance
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17207
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:49:10.961785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Point-RTD",
    "Transformer",
    "3D Point Cloud",
    "Discriminator-Generator Architecture",
    "Chamfer Distance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Point-RTD": 0.78,
    "Transformer": 0.85,
    "3D Point Cloud": 0.82,
    "Discriminator-Generator Architecture": 0.8,
    "Chamfer Distance": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Point-RTD",
        "canonical": "Point-RTD",
        "aliases": [
          "Replaced Token Denoising"
        ],
        "category": "unique_technical",
        "rationale": "Point-RTD is a novel pretraining strategy specifically designed for 3D point cloud tasks, offering a unique approach that enhances model performance.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer Models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer-based Models"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture in machine learning, widely applicable across various domains including 3D point cloud tasks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "3D Point Cloud",
        "canonical": "3D Point Cloud",
        "aliases": [
          "Point Cloud"
        ],
        "category": "specific_connectable",
        "rationale": "3D point clouds are a critical data type in computer vision, and linking to this concept enhances understanding of spatial data processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Discriminator-Generator Architecture",
        "canonical": "Discriminator-Generator Architecture",
        "aliases": [
          "GAN Architecture"
        ],
        "category": "specific_connectable",
        "rationale": "This architecture is key in the proposed method, facilitating effective denoising and learning of structural priors in point clouds.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Chamfer Distance",
        "canonical": "Chamfer Distance",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Chamfer Distance is a crucial metric for evaluating the accuracy of 3D reconstructions, relevant for assessing model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "pretraining strategy",
      "reconstruction error",
      "classification accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Point-RTD",
      "resolved_canonical": "Point-RTD",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer Models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "3D Point Cloud",
      "resolved_canonical": "3D Point Cloud",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Discriminator-Generator Architecture",
      "resolved_canonical": "Discriminator-Generator Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Chamfer Distance",
      "resolved_canonical": "Chamfer Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Point-RTD: Replaced Token Denoising for Pretraining Transformer Models on Point Clouds

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17207.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17207](https://arxiv.org/abs/2509.17207)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Real 3D_ Fusing 2D Vision with Pseudo 3D Representations for Robotic Manipulation Learning_20250923|No Need for Real 3D: Fusing 2D Vision with Pseudo 3D Representations for Robotic Manipulation Learning]] (82.0% similar)
- [[2025-09-22/The Missing Piece_ A Case for Pre-Training in 3D Medical Object Detection_20250922|The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection]] (81.6% similar)
- [[2025-09-18/Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression_20250918|Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression]] (81.2% similar)
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (81.1% similar)
- [[2025-09-22/SegDINO3D_ 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features_20250922|SegDINO3D: 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/3D Point Cloud|3D Point Cloud]], [[keywords/Discriminator-Generator Architecture|Discriminator-Generator Architecture]], [[keywords/Chamfer Distance|Chamfer Distance]]
**⚡ Unique Technical**: [[keywords/Point-RTD|Point-RTD]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17207v1 Announce Type: cross 
Abstract: Pre-training strategies play a critical role in advancing the performance of transformer-based models for 3D point cloud tasks. In this paper, we introduce Point-RTD (Replaced Token Denoising), a novel pretraining strategy designed to improve token robustness through a corruption-reconstruction framework. Unlike traditional mask-based reconstruction tasks that hide data segments for later prediction, Point-RTD corrupts point cloud tokens and leverages a discriminator-generator architecture for denoising. This shift enables more effective learning of structural priors and significantly enhances model performance and efficiency. On the ShapeNet dataset, Point-RTD reduces reconstruction error by over 93% compared to PointMAE, and achieves more than 14x lower Chamfer Distance on the test set. Our method also converges faster and yields higher classification accuracy on ShapeNet, ModelNet10, and ModelNet40 benchmarks, clearly outperforming the baseline Point-MAE framework in every case.

## 📝 요약

이 논문에서는 3D 포인트 클라우드 작업에서 트랜스포머 기반 모델의 성능을 향상시키기 위한 새로운 사전 학습 전략인 Point-RTD(대체 토큰 디노이징)를 제안합니다. Point-RTD는 전통적인 마스크 기반 재구성 작업과 달리 포인트 클라우드 토큰을 손상시키고, 디스크리미네이터-제너레이터 아키텍처를 활용하여 디노이징을 수행합니다. 이를 통해 구조적 사전 정보를 더 효과적으로 학습하고 모델 성능과 효율성을 크게 향상시킵니다. ShapeNet 데이터셋에서 Point-RTD는 PointMAE 대비 재구성 오류를 93% 이상 줄이고, 테스트 세트에서 Chamfer Distance를 14배 이상 낮춥니다. 또한, ShapeNet, ModelNet10, ModelNet40 벤치마크에서 더 빠르게 수렴하고 높은 분류 정확도를 달성하여 기존의 Point-MAE 프레임워크를 능가합니다.

## 🎯 주요 포인트

- 1. Point-RTD는 3D 포인트 클라우드 작업에서 토큰 강인성을 향상시키기 위해 고안된 새로운 사전 학습 전략입니다.
- 2. Point-RTD는 전통적인 마스크 기반 복원 작업과 달리 포인트 클라우드 토큰을 손상시키고, 판별자-생성자 아키텍처를 활용하여 노이즈를 제거합니다.
- 3. ShapeNet 데이터셋에서 Point-RTD는 PointMAE와 비교하여 재구성 오류를 93% 이상 감소시키고, 테스트 세트에서 14배 이상 낮은 Chamfer Distance를 달성합니다.
- 4. Point-RTD는 ShapeNet, ModelNet10, ModelNet40 벤치마크에서 더 빠르게 수렴하며, 더 높은 분류 정확도를 기록하여 Point-MAE 프레임워크를 능가합니다.


---

*Generated on 2025-09-23 23:49:10*