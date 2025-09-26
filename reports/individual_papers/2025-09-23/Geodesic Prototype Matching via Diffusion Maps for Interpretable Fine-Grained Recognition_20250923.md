---
keywords:
  - Diffusion Maps
  - Prototype-based Recognition
  - Fine-Grained Recognition
  - Latent Manifold Structure
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17050
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:43:21.493038",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Maps",
    "Prototype-based Recognition",
    "Fine-Grained Recognition",
    "Latent Manifold Structure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Maps": 0.78,
    "Prototype-based Recognition": 0.82,
    "Fine-Grained Recognition": 0.8,
    "Latent Manifold Structure": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Maps",
        "canonical": "Diffusion Maps",
        "aliases": [
          "Diffusion Mapping"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion Maps are central to the paper's method for capturing intrinsic geometry, offering a unique approach to manifold learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Prototype-based Recognition",
        "canonical": "Prototype-based Recognition",
        "aliases": [
          "Prototype Recognition"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the paper's approach to interpretable recognition, linking to prototype learning methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Fine-Grained Recognition",
        "canonical": "Fine-Grained Recognition",
        "aliases": [
          "Fine-Grained Classification"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on fine-grained recognition, a specific area in computer vision, enhancing connectivity with related works.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      },
      {
        "surface": "Latent Manifold Structure",
        "canonical": "Latent Manifold Structure",
        "aliases": [
          "Manifold Structure"
        ],
        "category": "unique_technical",
        "rationale": "Understanding the latent manifold structure is key to the paper's method, offering a unique perspective on feature space geometry.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "Nonlinear manifolds",
      "Euclidean distances",
      "Semantic distinctions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Maps",
      "resolved_canonical": "Diffusion Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Prototype-based Recognition",
      "resolved_canonical": "Prototype-based Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Fine-Grained Recognition",
      "resolved_canonical": "Fine-Grained Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Latent Manifold Structure",
      "resolved_canonical": "Latent Manifold Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Geodesic Prototype Matching via Diffusion Maps for Interpretable Fine-Grained Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17050.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17050](https://arxiv.org/abs/2509.17050)

## 🔗 유사한 논문
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (83.3% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.4% similar)
- [[2025-09-18/GROOD_ GRadient-Aware Out-of-Distribution Detection_20250918|GROOD: GRadient-Aware Out-of-Distribution Detection]] (81.1% similar)
- [[2025-09-23/Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination_20250923|Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination]] (80.9% similar)
- [[2025-09-23/MVCL-DAF++_ Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion_20250923|MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Prototype-based Recognition|Prototype-based Recognition]], [[keywords/Fine-Grained Recognition|Fine-Grained Recognition]]
**⚡ Unique Technical**: [[keywords/Diffusion Maps|Diffusion Maps]], [[keywords/Latent Manifold Structure|Latent Manifold Structure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17050v1 Announce Type: new 
Abstract: Nonlinear manifolds are widespread in deep visual features, where Euclidean distances often fail to capture true similarity. This limitation becomes particularly severe in prototype-based interpretable fine-grained recognition, where subtle semantic distinctions are essential. To address this challenge, we propose a novel paradigm for prototype-based recognition that anchors similarity within the intrinsic geometry of deep features. Specifically, we distill the latent manifold structure of each class into a diffusion space and introduce a differentiable Nystr\"om interpolation, making the geometry accessible to both unseen samples and learnable prototypes. To ensure efficiency, we employ compact per-class landmark sets with periodic updates. This design keeps the embedding aligned with the evolving backbone, enabling fast and scalable inference. Extensive experiments on the CUB-200-2011 and Stanford Cars datasets show that our GeoProto framework produces prototypes focusing on semantically aligned parts, significantly outperforming Euclidean prototype networks.

## 📝 요약

이 논문은 깊은 시각적 특징에서 비유클리드적 거리가 유사성을 잘 포착하지 못하는 문제를 해결하기 위해, 새로운 프로토타입 기반 인식 패러다임을 제안합니다. 각 클래스의 잠재 매니폴드 구조를 확산 공간으로 변환하고, 미분 가능한 Nyström 보간법을 도입하여 새로운 샘플과 학습 가능한 프로토타입에 접근성을 제공합니다. 효율성을 위해 클래스별 랜드마크 세트를 사용하고, 주기적으로 업데이트하여 임베딩을 최신 상태로 유지합니다. CUB-200-2011 및 Stanford Cars 데이터셋에서의 실험 결과, 제안된 GeoProto 프레임워크가 의미적으로 정렬된 부분에 집중하는 프로토타입을 생성하며, 유클리드 프로토타입 네트워크보다 성능이 뛰어남을 보여줍니다.

## 🎯 주요 포인트

- 1. 비유클리드 거리의 한계를 극복하기 위해, 심층 특징의 내재적 기하학을 활용한 새로운 프로토타입 기반 인식 패러다임을 제안합니다.
- 2. 각 클래스의 잠재 매니폴드 구조를 확산 공간으로 증류하고, 미분 가능한 Nyström 보간법을 도입하여 기하학을 새로운 샘플과 학습 가능한 프로토타입에 적용합니다.
- 3. 효율성을 위해 주기적으로 업데이트되는 클래스별 랜드마크 집합을 사용하여 임베딩을 진화하는 백본과 정렬시킵니다.
- 4. 제안된 GeoProto 프레임워크는 CUB-200-2011 및 Stanford Cars 데이터셋에서 유클리드 프로토타입 네트워크를 크게 능가하는 성능을 보입니다.


---

*Generated on 2025-09-24 04:43:21*