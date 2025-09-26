---
keywords:
  - Autoregressive Transformer
  - Video Diffusion Models
  - Distribution Matching Distillation
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2412.07772
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:22:48.774162",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Autoregressive Transformer",
    "Video Diffusion Models",
    "Distribution Matching Distillation",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Autoregressive Transformer": 0.78,
    "Video Diffusion Models": 0.77,
    "Distribution Matching Distillation": 0.75,
    "Zero-Shot Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "autoregressive transformer",
        "canonical": "Autoregressive Transformer",
        "aliases": [
          "autoregressive model",
          "AR transformer"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific adaptation of transformers for video generation, providing a unique connection point for autoregressive models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "video diffusion models",
        "canonical": "Video Diffusion Models",
        "aliases": [
          "video diffusion",
          "diffusion models for video"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specialized application of diffusion models in video generation, offering a unique technical link.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "distribution matching distillation",
        "canonical": "Distribution Matching Distillation",
        "aliases": [
          "DMD",
          "distillation technique"
        ],
        "category": "unique_technical",
        "rationale": "A novel distillation technique adapted for video models, enhancing connectivity through its unique application.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.79,
        "link_intent_score": 0.75
      },
      {
        "surface": "zero-shot manner",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot",
          "zero-shot inference"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader concept of zero-shot learning, which is a trending topic in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "interactive applications",
      "single frame",
      "entire sequence",
      "future",
      "latency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "autoregressive transformer",
      "resolved_canonical": "Autoregressive Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "video diffusion models",
      "resolved_canonical": "Video Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "distribution matching distillation",
      "resolved_canonical": "Distribution Matching Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.79,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "zero-shot manner",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# From Slow Bidirectional to Fast Autoregressive Video Diffusion Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.07772.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2412.07772](https://arxiv.org/abs/2412.07772)

## 🔗 유사한 논문
- [[2025-09-23/Survey of Video Diffusion Models_ Foundations, Implementations, and Applications_20250923|Survey of Video Diffusion Models: Foundations, Implementations, and Applications]] (86.9% similar)
- [[2025-09-24/Lyra_ Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation_20250924|Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation]] (86.0% similar)
- [[2025-09-23/QVGen_ Pushing the Limit of Quantized Video Generative Models_20250923|QVGen: Pushing the Limit of Quantized Video Generative Models]] (86.0% similar)
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (85.5% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Autoregressive Transformer|Autoregressive Transformer]], [[keywords/Video Diffusion Models|Video Diffusion Models]], [[keywords/Distribution Matching Distillation|Distribution Matching Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.07772v4 Announce Type: replace 
Abstract: Current video diffusion models achieve impressive generation quality but struggle in interactive applications due to bidirectional attention dependencies. The generation of a single frame requires the model to process the entire sequence, including the future. We address this limitation by adapting a pretrained bidirectional diffusion transformer to an autoregressive transformer that generates frames on-the-fly. To further reduce latency, we extend distribution matching distillation (DMD) to videos, distilling 50-step diffusion model into a 4-step generator. To enable stable and high-quality distillation, we introduce a student initialization scheme based on teacher's ODE trajectories, as well as an asymmetric distillation strategy that supervises a causal student model with a bidirectional teacher. This approach effectively mitigates error accumulation in autoregressive generation, allowing long-duration video synthesis despite training on short clips. Our model achieves a total score of 84.27 on the VBench-Long benchmark, surpassing all previous video generation models. It enables fast streaming generation of high-quality videos at 9.4 FPS on a single GPU thanks to KV caching. Our approach also enables streaming video-to-video translation, image-to-video, and dynamic prompting in a zero-shot manner.

## 📝 요약

현재의 비디오 확산 모델은 뛰어난 생성 품질을 보이지만, 쌍방향 주의 의존성 때문에 상호작용 애플리케이션에서는 어려움을 겪습니다. 본 연구는 사전 학습된 쌍방향 확산 변환기를 순차적 변환기로 변환하여 실시간 프레임 생성을 가능하게 했습니다. 또한, 분포 매칭 증류(DMD)를 비디오에 확장하여 50단계 확산 모델을 4단계 생성기로 증류함으로써 지연 시간을 줄였습니다. 안정적이고 고품질의 증류를 위해 교사의 ODE 경로를 기반으로 한 학생 초기화와 비대칭 증류 전략을 도입하여, 순차적 생성에서의 오류 누적을 효과적으로 완화했습니다. 이로 인해 짧은 클립으로 학습했음에도 장기간 비디오 합성이 가능해졌습니다. 제안된 모델은 VBench-Long 벤치마크에서 84.27점을 기록하며 이전의 모든 비디오 생성 모델을 능가했습니다. 또한, 단일 GPU에서 9.4 FPS로 고품질 비디오의 빠른 스트리밍 생성을 가능하게 했으며, 비디오-비디오 번역, 이미지-비디오 변환 및 동적 프롬프트를 제로샷 방식으로 지원합니다.

## 🎯 주요 포인트

- 1. 기존의 비디오 확산 모델은 인상적인 생성 품질을 보이지만, 쌍방향 주의 의존성으로 인해 상호작용 애플리케이션에서는 어려움을 겪습니다.
- 2. 우리는 사전 학습된 쌍방향 확산 변환기를 프레임을 실시간으로 생성하는 자기회귀 변환기로 변환하여 이 한계를 극복합니다.
- 3. 분포 매칭 증류(DMD)를 비디오로 확장하여 50단계 확산 모델을 4단계 생성기로 증류하여 지연 시간을 줄입니다.
- 4. 교사의 ODE 궤적을 기반으로 한 학생 초기화 및 비대칭 증류 전략을 도입하여 안정적이고 고품질의 증류를 가능하게 합니다.
- 5. 우리의 모델은 VBench-Long 벤치마크에서 84.27의 총 점수를 기록하며, 이전의 모든 비디오 생성 모델을 능가합니다.


---

*Generated on 2025-09-26 09:22:48*