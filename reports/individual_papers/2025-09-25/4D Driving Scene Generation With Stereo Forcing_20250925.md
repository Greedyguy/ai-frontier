---
keywords:
  - 4D Scene Generation
  - Novel View Synthesis
  - PhiGenesis
  - Stereo Forcing
  - Video Variational Autoencoder
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20251
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:14:49.917400",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "4D Scene Generation",
    "Novel View Synthesis",
    "PhiGenesis",
    "Stereo Forcing",
    "Video Variational Autoencoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "4D Scene Generation": 0.78,
    "Novel View Synthesis": 0.82,
    "PhiGenesis": 0.85,
    "Stereo Forcing": 0.77,
    "Video Variational Autoencoder": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "4D scene generation",
        "canonical": "4D Scene Generation",
        "aliases": [
          "4D driving scenes",
          "4D scene synthesis"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept specific to the paper's approach, linking it to advancements in scene generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Novel View Synthesis",
        "canonical": "Novel View Synthesis",
        "aliases": [
          "NVS"
        ],
        "category": "specific_connectable",
        "rationale": "A key task in computer vision, linking this work to broader research in view synthesis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "PhiGenesis",
        "canonical": "PhiGenesis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The core framework introduced in the paper, essential for linking to its specific contributions.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Stereo Forcing",
        "canonical": "Stereo Forcing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel conditioning strategy introduced in the paper, important for understanding its unique approach.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Video VAE",
        "canonical": "Video Variational Autoencoder",
        "aliases": [
          "Video VAE"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of generative models in video processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "temporal generation",
      "geometric reconstruction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "4D scene generation",
      "resolved_canonical": "4D Scene Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Novel View Synthesis",
      "resolved_canonical": "Novel View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "PhiGenesis",
      "resolved_canonical": "PhiGenesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Stereo Forcing",
      "resolved_canonical": "Stereo Forcing",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Video VAE",
      "resolved_canonical": "Video Variational Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# 4D Driving Scene Generation With Stereo Forcing

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20251.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20251](https://arxiv.org/abs/2509.20251)

## 🔗 유사한 논문
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance]] (85.0% similar)
- [[2025-09-24/Lyra_ Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation_20250924|Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation]] (84.2% similar)
- [[2025-09-23/Generating 360{\deg} Video is What You Need For a 3D Scene_20250923|Generating 360{\deg} Video is What You Need For a 3D Scene]] (83.7% similar)
- [[2025-09-23/RLGF_ Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation_20250923|RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation]] (83.2% similar)
- [[2025-09-23/4DGCPro_ Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming_20250923|4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Novel View Synthesis|Novel View Synthesis]], [[keywords/Video Variational Autoencoder|Video Variational Autoencoder]]
**⚡ Unique Technical**: [[keywords/4D Scene Generation|4D Scene Generation]], [[keywords/PhiGenesis|PhiGenesis]], [[keywords/Stereo Forcing|Stereo Forcing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20251v1 Announce Type: new 
Abstract: Current generative models struggle to synthesize dynamic 4D driving scenes that simultaneously support temporal extrapolation and spatial novel view synthesis (NVS) without per-scene optimization. Bridging generation and novel view synthesis remains a major challenge. We present PhiGenesis, a unified framework for 4D scene generation that extends video generation techniques with geometric and temporal consistency. Given multi-view image sequences and camera parameters, PhiGenesis produces temporally continuous 4D Gaussian splatting representations along target 3D trajectories. In its first stage, PhiGenesis leverages a pre-trained video VAE with a novel range-view adapter to enable feed-forward 4D reconstruction from multi-view images. This architecture supports single-frame or video inputs and outputs complete 4D scenes including geometry, semantics, and motion. In the second stage, PhiGenesis introduces a geometric-guided video diffusion model, using rendered historical 4D scenes as priors to generate future views conditioned on trajectories. To address geometric exposure bias in novel views, we propose Stereo Forcing, a novel conditioning strategy that integrates geometric uncertainty during denoising. This method enhances temporal coherence by dynamically adjusting generative influence based on uncertainty-aware perturbations. Our experimental results demonstrate that our method achieves state-of-the-art performance in both appearance and geometric reconstruction, temporal generation and novel view synthesis (NVS) tasks, while simultaneously delivering competitive performance in downstream evaluations. Homepage is at \href{https://jiangxb98.github.io/PhiGensis}{PhiGensis}.

## 📝 요약

PhiGenesis는 4D 장면 생성을 위한 통합 프레임워크로, 시간적 외삽과 공간적 새로운 시점 합성을 동시에 지원하는 것을 목표로 합니다. 이 방법은 멀티뷰 이미지 시퀀스와 카메라 매개변수를 입력으로 받아, 목표 3D 경로를 따라 시간적으로 연속적인 4D 가우시안 스플래팅 표현을 생성합니다. 첫 번째 단계에서는 사전 학습된 비디오 VAE와 새로운 범위-뷰 어댑터를 활용하여 멀티뷰 이미지로부터 피드포워드 방식의 4D 재구성을 지원합니다. 두 번째 단계에서는 기하학적 노출 편향을 해결하기 위해 Stereo Forcing이라는 새로운 조건 전략을 도입하여 시간적 일관성을 향상시킵니다. 실험 결과, PhiGenesis는 외관 및 기하학적 재구성, 시간적 생성 및 새로운 시점 합성(NVS) 작업에서 최첨단 성능을 달성하며, 다운스트림 평가에서도 경쟁력 있는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. PhiGenesis는 기하학적 및 시간적 일관성을 갖춘 4D 장면 생성을 위한 통합 프레임워크를 제안합니다.
- 2. 이 모델은 멀티뷰 이미지 시퀀스와 카메라 매개변수를 입력으로 받아 목표 3D 경로를 따라 시간적으로 연속적인 4D 가우시안 스플래팅 표현을 생성합니다.
- 3. PhiGenesis는 사전 학습된 비디오 VAE와 새로운 범위-뷰 어댑터를 활용하여 멀티뷰 이미지로부터 피드포워드 4D 재구성을 지원합니다.
- 4. 기하학적 노출 편향을 해결하기 위해, PhiGenesis는 'Stereo Forcing'이라는 새로운 조건 전략을 도입하여 불확실성 인식 교란을 기반으로 생성적 영향을 동적으로 조정합니다.
- 5. 실험 결과, PhiGenesis는 외관 및 기하학적 재구성, 시간적 생성 및 새로운 뷰 합성(NVS) 작업에서 최첨단 성능을 달성하며, 다운스트림 평가에서도 경쟁력 있는 성능을 제공합니다.


---

*Generated on 2025-09-26 09:14:49*