<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:56:53.915207",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Event-based Stereo Depth Estimation",
    "Uncertainty-aware Refinement Network",
    "Uncertainty Modeling",
    "Local-global Context Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Event-based Stereo Depth Estimation": 0.78,
    "Uncertainty-aware Refinement Network": 0.8,
    "Uncertainty Modeling": 0.72,
    "Local-global Context Module": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Event-based Stereo Depth Estimation",
        "canonical": "Event-based Stereo Depth Estimation",
        "aliases": [
          "Event-based Depth Estimation",
          "Stereo Depth Estimation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized task within computer vision that connects to advancements in event camera technology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty-aware Refinement Network",
        "canonical": "Uncertainty-aware Refinement Network",
        "aliases": [
          "URNet"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to handling uncertainty in depth estimation, crucial for linking to uncertainty modeling techniques.",
        "novelty_score": 0.82,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Kullback-Leibler divergence-based uncertainty modeling",
        "canonical": "Uncertainty Modeling",
        "aliases": [
          "KL divergence-based modeling"
        ],
        "category": "broad_technical",
        "rationale": "Links to statistical methods used in various machine learning applications for modeling uncertainty.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Local-global refinement module",
        "canonical": "Local-global Context Module",
        "aliases": [
          "Local-global Module"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to techniques in neural networks that balance local details with global context, relevant in deep learning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
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
      "candidate_surface": "Event-based Stereo Depth Estimation",
      "resolved_canonical": "Event-based Stereo Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty-aware Refinement Network",
      "resolved_canonical": "Uncertainty-aware Refinement Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Kullback-Leibler divergence-based uncertainty modeling",
      "resolved_canonical": "Uncertainty Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Local-global refinement module",
      "resolved_canonical": "Local-global Context Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# URNet: Uncertainty-aware Refinement Network for Event-based Stereo Depth Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18184.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18184](https://arxiv.org/abs/2509.18184)

## 🔗 유사한 논문
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (84.7% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (82.6% similar)
- [[2025-09-23/Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling_20250923|Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling]] (81.9% similar)
- [[2025-09-23/StereoAdapter_ Adapting Stereo Depth Estimation to Underwater Scenes_20250923|StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes]] (81.1% similar)
- [[2025-09-18/NDLPNet_ A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset_20250918|NDLPNet: A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Uncertainty Modeling|Uncertainty Modeling]]
**🔗 Specific Connectable**: [[keywords/Local-global Context Module|Local-global Context Module]]
**⚡ Unique Technical**: [[keywords/Event-based Stereo Depth Estimation|Event-based Stereo Depth Estimation]], [[keywords/Uncertainty-aware Refinement Network|Uncertainty-aware Refinement Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18184v1 Announce Type: new 
Abstract: Event cameras provide high temporal resolution, high dynamic range, and low latency, offering significant advantages over conventional frame-based cameras. In this work, we introduce an uncertainty-aware refinement network called URNet for event-based stereo depth estimation. Our approach features a local-global refinement module that effectively captures fine-grained local details and long-range global context. Additionally, we introduce a Kullback-Leibler (KL) divergence-based uncertainty modeling method to enhance prediction reliability. Extensive experiments on the DSEC dataset demonstrate that URNet consistently outperforms state-of-the-art (SOTA) methods in both qualitative and quantitative evaluations.

## 📝 요약

이 연구는 이벤트 카메라를 활용한 스테레오 깊이 추정에서 불확실성을 고려한 URNet이라는 네트워크를 제안합니다. URNet은 세밀한 지역적 정보와 장거리 전역적 문맥을 효과적으로 포착하는 지역-전역 정제 모듈을 특징으로 하며, KL 발산 기반의 불확실성 모델링 방법을 도입하여 예측 신뢰성을 향상시킵니다. DSEC 데이터셋을 활용한 실험 결과, URNet은 정성적 및 정량적 평가에서 최신 기법들을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 이벤트 카메라는 높은 시간 해상도, 높은 동적 범위, 낮은 지연 시간을 제공하여 기존 프레임 기반 카메라보다 큰 이점을 제공합니다.
- 2. URNet은 이벤트 기반 스테레오 깊이 추정을 위한 불확실성 인식 정제 네트워크로, 세밀한 지역적 디테일과 장거리 글로벌 컨텍스트를 효과적으로 포착하는 로컬-글로벌 정제 모듈을 특징으로 합니다.
- 3. Kullback-Leibler (KL) 발산 기반의 불확실성 모델링 방법을 도입하여 예측 신뢰성을 향상시켰습니다.
- 4. DSEC 데이터셋에 대한 광범위한 실험 결과, URNet이 정성적 및 정량적 평가에서 최신 기술(SOTA) 방법들을 일관되게 능가함을 보여줍니다.


---

*Generated on 2025-09-24 15:56:53*