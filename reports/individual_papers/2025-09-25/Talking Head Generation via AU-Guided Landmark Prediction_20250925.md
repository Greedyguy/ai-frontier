---
keywords:
  - Facial Action Units
  - Landmark Prediction
  - Diffusion-based Video Synthesis
  - Talking Head Generation
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19749
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:05:47.966696",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Facial Action Units",
    "Landmark Prediction",
    "Diffusion-based Video Synthesis",
    "Talking Head Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Facial Action Units": 0.78,
    "Landmark Prediction": 0.79,
    "Diffusion-based Video Synthesis": 0.82,
    "Talking Head Generation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Action Units",
        "canonical": "Facial Action Units",
        "aliases": [
          "AUs"
        ],
        "category": "unique_technical",
        "rationale": "Facial Action Units are central to the paper's method for expression control, offering a unique technical approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Landmark Prediction",
        "canonical": "Landmark Prediction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Landmark prediction is a key component in the proposed framework, linking to computer vision tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "Diffusion-based Synthesizer",
        "canonical": "Diffusion-based Video Synthesis",
        "aliases": [
          "Diffusion-based Synthesizer"
        ],
        "category": "unique_technical",
        "rationale": "This technique is crucial for generating realistic videos, representing a novel application of diffusion models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Talking Head Generation",
        "canonical": "Talking Head Generation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The core focus of the paper, connecting to advancements in video synthesis and animation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
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
      "candidate_surface": "Action Units",
      "resolved_canonical": "Facial Action Units",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Landmark Prediction",
      "resolved_canonical": "Landmark Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Diffusion-based Synthesizer",
      "resolved_canonical": "Diffusion-based Video Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Talking Head Generation",
      "resolved_canonical": "Talking Head Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Talking Head Generation via AU-Guided Landmark Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19749.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19749](https://arxiv.org/abs/2509.19749)

## 🔗 유사한 논문
- [[2025-09-24/Audio-Driven Universal Gaussian Head Avatars_20250924|Audio-Driven Universal Gaussian Head Avatars]] (84.4% similar)
- [[2025-09-23/Beat on Gaze_ Learning Stylized Generation of Gaze and Head Dynamics_20250923|Beat on Gaze: Learning Stylized Generation of Gaze and Head Dynamics]] (84.3% similar)
- [[2025-09-22/Tiny is not small enough_ High-quality, low-resource facial animation models through hybrid knowledge distillation_20250922|Tiny is not small enough: High-quality, low-resource facial animation models through hybrid knowledge distillation]] (82.3% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (82.3% similar)
- [[2025-09-23/Follow-Your-Emoji-Faster_ Towards Efficient, Fine-Controllable, and Expressive Freestyle Portrait Animation_20250923|Follow-Your-Emoji-Faster: Towards Efficient, Fine-Controllable, and Expressive Freestyle Portrait Animation]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Landmark Prediction|Landmark Prediction]], [[keywords/Talking Head Generation|Talking Head Generation]]
**⚡ Unique Technical**: [[keywords/Facial Action Units|Facial Action Units]], [[keywords/Diffusion-based Video Synthesis|Diffusion-based Video Synthesis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19749v1 Announce Type: new 
Abstract: We propose a two-stage framework for audio-driven talking head generation with fine-grained expression control via facial Action Units (AUs). Unlike prior methods relying on emotion labels or implicit AU conditioning, our model explicitly maps AUs to 2D facial landmarks, enabling physically grounded, per-frame expression control. In the first stage, a variational motion generator predicts temporally coherent landmark sequences from audio and AU intensities. In the second stage, a diffusion-based synthesizer generates realistic, lip-synced videos conditioned on these landmarks and a reference image. This separation of motion and appearance improves expression accuracy, temporal stability, and visual realism. Experiments on the MEAD dataset show that our method outperforms state-of-the-art baselines across multiple metrics, demonstrating the effectiveness of explicit AU-to-landmark modeling for expressive talking head generation.

## 📝 요약

이 논문은 얼굴 행동 단위(AUs)를 활용한 세밀한 표정 제어가 가능한 오디오 기반의 말하는 얼굴 생성 프레임워크를 제안합니다. 기존 방법과 달리, AUs를 2D 얼굴 랜드마크로 명시적으로 매핑하여 물리적으로 기반이 있는 프레임별 표정 제어를 가능하게 합니다. 첫 번째 단계에서는 변동 모션 생성기가 오디오와 AU 강도를 기반으로 시간적으로 일관된 랜드마크 시퀀스를 예측합니다. 두 번째 단계에서는 확산 기반 합성기가 이러한 랜드마크와 참조 이미지를 조건으로 사실적이고 립싱크된 영상을 생성합니다. 이 모션과 외형의 분리는 표현 정확성, 시간적 안정성, 시각적 사실성을 향상시킵니다. MEAD 데이터셋 실험 결과, 제안된 방법은 여러 지표에서 최신 기법들을 능가하며, 명시적인 AU-랜드마크 모델링의 효과성을 입증합니다.

## 🎯 주요 포인트

- 1. 제안된 프레임워크는 얼굴 행동 단위(AUs)를 통해 세밀한 표현 제어가 가능한 오디오 기반 말하는 얼굴 생성 기술을 제시합니다.
- 2. 모델은 AUs를 2D 얼굴 랜드마크로 명시적으로 매핑하여 물리적으로 근거 있는 프레임별 표현 제어를 가능하게 합니다.
- 3. 첫 번째 단계에서는 변동 모션 생성기가 오디오와 AU 강도로부터 시간적으로 일관된 랜드마크 시퀀스를 예측합니다.
- 4. 두 번째 단계에서는 확산 기반 합성기가 이러한 랜드마크와 참조 이미지를 조건으로 사실적이고 립싱크된 비디오를 생성합니다.
- 5. MEAD 데이터셋 실험 결과, 제안된 방법은 여러 지표에서 최신 기법들을 능가하며, 명시적인 AU-랜드마크 모델링의 효과성을 입증합니다.


---

*Generated on 2025-09-26 09:05:47*