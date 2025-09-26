---
keywords:
  - Transformer
  - Flow Matching Generative Model
  - Audio-Driven Talking Portrait
  - Speech-Driven Emotion Enhancement
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2412.01064
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:48:45.030844",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Flow Matching Generative Model",
    "Audio-Driven Talking Portrait",
    "Speech-Driven Emotion Enhancement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Flow Matching Generative Model": 0.7,
    "Audio-Driven Talking Portrait": 0.72,
    "Speech-Driven Emotion Enhancement": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based vector field predictor",
        "canonical": "Transformer",
        "aliases": [
          "Transformer predictor",
          "Vector field Transformer"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology in machine learning, facilitating connections to various related models and techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "flow matching generative model",
        "canonical": "Flow Matching Generative Model",
        "aliases": [
          "Flow-based generative model",
          "Flow matching model"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, offering unique insights into generative model advancements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "audio-driven talking portrait",
        "canonical": "Audio-Driven Talking Portrait",
        "aliases": [
          "Audio-driven portrait animation",
          "Talking portrait"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and connects to advancements in audio-visual synthesis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "speech-driven emotion enhancement",
        "canonical": "Speech-Driven Emotion Enhancement",
        "aliases": [
          "Emotion enhancement via speech",
          "Speech emotion enhancement"
        ],
        "category": "unique_technical",
        "rationale": "This technique highlights the integration of emotion in generative models, linking to emotional AI research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.78,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "portrait image animation",
      "temporally consistent video generation",
      "fast sampling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based vector field predictor",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "flow matching generative model",
      "resolved_canonical": "Flow Matching Generative Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "audio-driven talking portrait",
      "resolved_canonical": "Audio-Driven Talking Portrait",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "speech-driven emotion enhancement",
      "resolved_canonical": "Speech-Driven Emotion Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.78,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait

**Korean Title:** FLOAT: 오디오 기반의 말하는 초상화를 위한 생성적 모션 잠재 흐름 매칭

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.01064.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2412.01064](https://arxiv.org/abs/2412.01064)

## 🔗 유사한 논문
- [[2025-09-22/Generating Moving 3D Soundscapes with Latent Diffusion Models_20250922|Generating Moving 3D Soundscapes with Latent Diffusion Models]] (83.0% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (82.3% similar)
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (82.1% similar)
- [[2025-09-17/RFM-Editing_ Rectified Flow Matching for Text-guided Audio Editing_20250917|RFM-Editing: Rectified Flow Matching for Text-guided Audio Editing]] (81.1% similar)
- [[2025-09-22/Compose Yourself_ Average-Velocity Flow Matching for One-Step Speech Enhancement_20250922|Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Flow Matching Generative Model|Flow Matching Generative Model]], [[keywords/Audio-Driven Talking Portrait|Audio-Driven Talking Portrait]], [[keywords/Speech-Driven Emotion Enhancement|Speech-Driven Emotion Enhancement]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.01064v5 Announce Type: replace-cross 
Abstract: With the rapid advancement of diffusion-based generative models, portrait image animation has achieved remarkable results. However, it still faces challenges in temporally consistent video generation and fast sampling due to its iterative sampling nature. This paper presents FLOAT, an audio-driven talking portrait video generation method based on flow matching generative model. Instead of a pixel-based latent space, we take advantage of a learned orthogonal motion latent space, enabling efficient generation and editing of temporally consistent motion. To achieve this, we introduce a transformer-based vector field predictor with an effective frame-wise conditioning mechanism. Additionally, our method supports speech-driven emotion enhancement, enabling a natural incorporation of expressive motions. Extensive experiments demonstrate that our method outperforms state-of-the-art audio-driven talking portrait methods in terms of visual quality, motion fidelity, and efficiency.

## 🔍 Abstract (한글 번역)

arXiv:2412.01064v5 발표 유형: 교차 교체  
초록: 확산 기반 생성 모델의 급속한 발전으로 인해 초상화 이미지 애니메이션이 놀라운 결과를 달성했습니다. 그러나 반복적인 샘플링 특성으로 인해 시간적으로 일관된 비디오 생성과 빠른 샘플링에서 여전히 어려움을 겪고 있습니다. 이 논문에서는 흐름 매칭 생성 모델에 기반한 오디오 구동 대화형 초상화 비디오 생성 방법인 FLOAT를 제시합니다. 픽셀 기반 잠재 공간 대신 학습된 직교 운동 잠재 공간을 활용하여 시간적으로 일관된 운동의 효율적인 생성 및 편집을 가능하게 합니다. 이를 위해 효과적인 프레임 단위 조건 메커니즘을 갖춘 트랜스포머 기반 벡터 필드 예측기를 도입합니다. 또한, 우리의 방법은 음성 구동 감정 향상을 지원하여 표현력이 풍부한 동작을 자연스럽게 통합할 수 있습니다. 광범위한 실험을 통해 우리의 방법이 시각적 품질, 운동 충실도 및 효율성 측면에서 최첨단 오디오 구동 대화형 초상화 방법을 능가함을 입증합니다.

## 📝 요약

이 논문에서는 FLOW라는 오디오 기반의 얼굴 애니메이션 생성 방법을 제안합니다. 이 방법은 흐름 매칭 생성 모델을 사용하여 픽셀 기반이 아닌 학습된 정규 직교 운동 잠재 공간을 활용함으로써 시간적으로 일관된 모션을 효율적으로 생성하고 편집할 수 있습니다. 또한, 트랜스포머 기반의 벡터 필드 예측기를 도입하여 프레임 단위의 효과적인 조건부 메커니즘을 구현하였습니다. 이 방법은 감정 표현을 자연스럽게 강화할 수 있는 기능도 지원합니다. 실험 결과, 제안된 방법은 시각적 품질, 모션 충실도, 효율성 측면에서 기존의 오디오 기반 얼굴 애니메이션 생성 방법을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 흐름 매칭 생성 모델을 기반으로 한 오디오 기반의 말하는 초상화 비디오 생성 방법인 FLOAT를 제안합니다.
- 2. 학습된 직교 운동 잠재 공간을 활용하여 시간적으로 일관된 움직임을 효율적으로 생성하고 편집할 수 있습니다.
- 3. 효과적인 프레임별 조건 메커니즘을 갖춘 트랜스포머 기반 벡터 필드 예측기를 도입하였습니다.
- 4. 감정 표현을 자연스럽게 포함할 수 있는 말 기반 감정 향상을 지원합니다.
- 5. 실험 결과, 제안된 방법이 시각적 품질, 움직임 충실도 및 효율성 측면에서 최신 오디오 기반 말하는 초상화 방법보다 우수함을 보여줍니다.


---

*Generated on 2025-09-23 09:48:45*