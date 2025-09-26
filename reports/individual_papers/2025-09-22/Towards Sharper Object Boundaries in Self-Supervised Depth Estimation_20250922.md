---
keywords:
  - Self-supervised Learning
  - Monocular Depth Estimation
  - Depth Discontinuities
  - Variance-aware Loss Functions
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15987
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:25:33.111034",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Monocular Depth Estimation",
    "Depth Discontinuities",
    "Variance-aware Loss Functions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Monocular Depth Estimation": 0.78,
    "Depth Discontinuities": 0.72,
    "Variance-aware Loss Functions": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised depth estimation",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised depth",
          "self-supervised estimation"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key approach in the paper, aligning with existing concepts in self-supervised methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Monocular depth estimation",
        "canonical": "Monocular Depth Estimation",
        "aliases": [
          "single-view depth estimation"
        ],
        "category": "unique_technical",
        "rationale": "Monocular depth estimation is a specific technical focus of the paper, offering unique insights into 3D scene understanding.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Depth discontinuities",
        "canonical": "Depth Discontinuities",
        "aliases": [
          "depth edges",
          "depth boundaries"
        ],
        "category": "unique_technical",
        "rationale": "The paper's focus on improving depth discontinuities is a novel contribution to the field of depth estimation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      },
      {
        "surface": "Variance-aware loss functions",
        "canonical": "Variance-aware Loss Functions",
        "aliases": [
          "variance-based loss",
          "uncertainty-aware loss"
        ],
        "category": "unique_technical",
        "rationale": "The introduction of variance-aware loss functions is a unique methodological contribution that enhances depth estimation accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "3D scene understanding",
      "spurious intermediate 3D points"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised depth estimation",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Monocular depth estimation",
      "resolved_canonical": "Monocular Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Depth discontinuities",
      "resolved_canonical": "Depth Discontinuities",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Variance-aware loss functions",
      "resolved_canonical": "Variance-aware Loss Functions",
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

# Towards Sharper Object Boundaries in Self-Supervised Depth Estimation

**Korean Title:** 자기 지도 심도 추정에서 더 선명한 객체 경계를 향하여

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15987.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15987](https://arxiv.org/abs/2509.15987)

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (82.9% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (81.4% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (81.0% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (80.8% similar)
- [[2025-09-19/UCorr_ Wire Detection and Depth Estimation for Autonomous Drones_20250919|UCorr: Wire Detection and Depth Estimation for Autonomous Drones]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Monocular Depth Estimation|Monocular Depth Estimation]], [[keywords/Depth Discontinuities|Depth Discontinuities]], [[keywords/Variance-aware Loss Functions|Variance-aware Loss Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15987v1 Announce Type: cross 
Abstract: Accurate monocular depth estimation is crucial for 3D scene understanding, but existing methods often blur depth at object boundaries, introducing spurious intermediate 3D points. While achieving sharp edges usually requires very fine-grained supervision, our method produces crisp depth discontinuities using only self-supervision. Specifically, we model per-pixel depth as a mixture distribution, capturing multiple plausible depths and shifting uncertainty from direct regression to the mixture weights. This formulation integrates seamlessly into existing pipelines via variance-aware loss functions and uncertainty propagation. Extensive evaluations on KITTI and VKITTIv2 show that our method achieves up to 35% higher boundary sharpness and improves point cloud quality compared to state-of-the-art baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15987v1 발표 유형: 교차  
초록: 정확한 단안 깊이 추정은 3D 장면 이해에 필수적이지만, 기존 방법들은 종종 객체 경계에서 깊이를 흐리게 하여 잘못된 중간 3D 포인트를 도입합니다. 선명한 경계를 달성하려면 매우 세밀한 감독이 필요하지만, 우리 방법은 자기 감독만으로 선명한 깊이 불연속성을 생성합니다. 구체적으로, 우리는 픽셀 단위의 깊이를 혼합 분포로 모델링하여 여러 가능한 깊이를 포착하고 불확실성을 직접 회귀에서 혼합 가중치로 전환합니다. 이 공식은 분산 인식 손실 함수와 불확실성 전파를 통해 기존 파이프라인에 원활하게 통합됩니다. KITTI 및 VKITTIv2에 대한 광범위한 평가 결과, 우리 방법은 경계 선명도를 최대 35% 향상시키고 최첨단 기준선과 비교하여 포인트 클라우드 품질을 개선함을 보여줍니다.

## 📝 요약

이 논문은 단안 깊이 추정에서 객체 경계의 흐릿함을 해결하기 위해 자기 지도 학습을 활용한 새로운 방법을 제안합니다. 기존 방법들이 세밀한 감독을 필요로 하는 반면, 제안된 방법은 픽셀 단위 깊이를 혼합 분포로 모델링하여 불확실성을 혼합 가중치로 전환합니다. 이 접근법은 기존 파이프라인에 쉽게 통합되며, 분산 인식 손실 함수와 불확실성 전파를 통해 구현됩니다. KITTI와 VKITTIv2 데이터셋에서의 평가 결과, 경계 선명도가 최대 35% 향상되고, 포인트 클라우드 품질이 개선되었습니다.

## 🎯 주요 포인트

- 1. 본 연구는 객체 경계에서 깊이 흐림 현상을 줄이고 날카로운 깊이 불연속성을 생성하는 방법을 제안합니다.
- 2. 제안된 방법은 매우 세밀한 감독 없이도 자기 감독만으로 날카로운 경계선을 달성합니다.
- 3. 각 픽셀의 깊이를 혼합 분포로 모델링하여 여러 가능한 깊이를 포착하고 불확실성을 혼합 가중치로 전환합니다.
- 4. 제안된 방법은 분산 인식 손실 함수와 불확실성 전파를 통해 기존 파이프라인에 원활하게 통합됩니다.
- 5. KITTI 및 VKITTIv2 데이터셋에서의 평가 결과, 경계 선명도가 최대 35% 향상되고 포인트 클라우드 품질이 개선되었습니다.


---

*Generated on 2025-09-23 09:25:33*