---
keywords:
  - Tri-plane Representation
  - Hybrid-plane Representation
  - Spherical Tri-plane
  - 3D-aware Generative Adversarial Networks
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16748
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:33:26.649333",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tri-plane Representation",
    "Hybrid-plane Representation",
    "Spherical Tri-plane",
    "3D-aware Generative Adversarial Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Tri-plane Representation": 0.78,
    "Hybrid-plane Representation": 0.82,
    "Spherical Tri-plane": 0.75,
    "3D-aware Generative Adversarial Networks": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tri-plane-like representations",
        "canonical": "Tri-plane Representation",
        "aliases": [
          "Tri-plane",
          "Tri-plane Model"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a specific technical approach in 3D-aware GANs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hy-plane representation",
        "canonical": "Hybrid-plane Representation",
        "aliases": [
          "Hy-plane",
          "Hybrid-plane"
        ],
        "category": "unique_technical",
        "rationale": "Introduced as a novel solution in the paper, it combines planar and spherical planes for improved image synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Spherical tri-planes",
        "canonical": "Spherical Tri-plane",
        "aliases": [
          "Spherical Tri-plane Model"
        ],
        "category": "unique_technical",
        "rationale": "A variation of tri-plane representations that addresses feature entanglement issues in 3D modeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "3D-aware GANs",
        "canonical": "3D-aware Generative Adversarial Networks",
        "aliases": [
          "3D-aware GAN",
          "3D GAN"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area for the discussed representations, linking to broader GAN research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "feature entanglement",
      "feature map"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Tri-plane-like representations",
      "resolved_canonical": "Tri-plane Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hy-plane representation",
      "resolved_canonical": "Hybrid-plane Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Spherical tri-planes",
      "resolved_canonical": "Spherical Tri-plane",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "3D-aware GANs",
      "resolved_canonical": "3D-aware Generative Adversarial Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# HyPlaneHead: Rethinking Tri-plane-like Representations in Full-Head Image Synthesis

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16748.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16748](https://arxiv.org/abs/2509.16748)

## 🔗 유사한 논문
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (81.9% similar)
- [[2025-09-23/Disentangling Content from Style to Overcome Shortcut Learning_ A Hybrid Generative-Discriminative Learning Framework_20250923|Disentangling Content from Style to Overcome Shortcut Learning: A Hybrid Generative-Discriminative Learning Framework]] (80.1% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (80.0% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (77.9% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/3D-aware Generative Adversarial Networks|3D-aware Generative Adversarial Networks]]
**⚡ Unique Technical**: [[keywords/Tri-plane Representation|Tri-plane Representation]], [[keywords/Hybrid-plane Representation|Hybrid-plane Representation]], [[keywords/Spherical Tri-plane|Spherical Tri-plane]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16748v1 Announce Type: new 
Abstract: Tri-plane-like representations have been widely adopted in 3D-aware GANs for head image synthesis and other 3D object/scene modeling tasks due to their efficiency. However, querying features via Cartesian coordinate projection often leads to feature entanglement, which results in mirroring artifacts. A recent work, SphereHead, attempted to address this issue by introducing spherical tri-planes based on a spherical coordinate system. While it successfully mitigates feature entanglement, SphereHead suffers from uneven mapping between the square feature maps and the spherical planes, leading to inefficient feature map utilization during rendering and difficulties in generating fine image details. Moreover, both tri-plane and spherical tri-plane representations share a subtle yet persistent issue: feature penetration across convolutional channels can cause interference between planes, particularly when one plane dominates the others. These challenges collectively prevent tri-plane-based methods from reaching their full potential. In this paper, we systematically analyze these problems for the first time and propose innovative solutions to address them. Specifically, we introduce a novel hybrid-plane (hy-plane for short) representation that combines the strengths of both planar and spherical planes while avoiding their respective drawbacks. We further enhance the spherical plane by replacing the conventional theta-phi warping with a novel near-equal-area warping strategy, which maximizes the effective utilization of the square feature map. In addition, our generator synthesizes a single-channel unified feature map instead of multiple feature maps in separate channels, thereby effectively eliminating feature penetration. With a series of technical improvements, our hy-plane representation enables our method, HyPlaneHead, to achieve state-of-the-art performance in full-head image synthesis.

## 📝 요약

이 논문은 3D 인식 GAN에서 사용되는 Tri-plane 표현 방식의 문제점을 분석하고 이를 개선하기 위한 새로운 접근법을 제안합니다. 기존의 Tri-plane 방식은 특징 얽힘 문제로 인해 이미지에 왜곡을 초래하며, SphereHead는 이를 구형 좌표계로 해결하려 했으나 비효율적인 특징 맵 활용 문제를 겪었습니다. 본 연구에서는 이러한 문제를 해결하기 위해 평면과 구형의 장점을 결합한 새로운 하이브리드 평면(hy-plane) 표현 방식을 도입하였습니다. 또한, 기존의 theta-phi 왜곡을 개선한 새로운 왜곡 전략을 적용하여 특징 맵의 활용도를 극대화하였고, 단일 채널 통합 특징 맵을 생성하여 특징 침투 문제를 해결했습니다. 이러한 기술적 개선을 통해 HyPlaneHead는 전체 머리 이미지 합성에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. Tri-plane-like 표현 방식은 효율성 때문에 3D 인식 GAN에서 널리 사용되지만, 좌표 투영으로 인한 특징 얽힘 문제로 거울 이미지 아티팩트가 발생할 수 있습니다.
- 2. SphereHead는 구형 좌표계를 기반으로 한 구형 트라이-플레인을 도입하여 특징 얽힘 문제를 해결했으나, 비효율적인 특징 맵 활용과 세부 이미지 생성의 어려움이 있습니다.
- 3. 트라이-플레인과 구형 트라이-플레인 모두에서 특징 침투 문제가 발생하여, 한 평면이 다른 평면을 지배할 때 간섭이 생길 수 있습니다.
- 4. 본 논문에서는 이러한 문제를 체계적으로 분석하고, 평면과 구형 평면의 장점을 결합한 하이브리드 평면(hy-plane) 표현을 제안합니다.
- 5. 새로운 근접-동등-면적 왜곡 전략을 도입하여 구형 평면의 효과적인 활용을 극대화하고, 단일 채널 통합 특징 맵을 생성하여 특징 침투를 제거합니다.


---

*Generated on 2025-09-24 04:33:26*