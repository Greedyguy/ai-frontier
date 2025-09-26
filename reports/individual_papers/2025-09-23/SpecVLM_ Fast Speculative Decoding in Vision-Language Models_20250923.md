---
keywords:
  - Vision-Language Model
  - Speculative Decoding
  - Elastic Visual Compressor
  - Online-Logit Distillation
  - Autoregressive Inference
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.11815
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:29:30.507887",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Speculative Decoding",
    "Elastic Visual Compressor",
    "Online-Logit Distillation",
    "Autoregressive Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Speculative Decoding": 0.8,
    "Elastic Visual Compressor": 0.78,
    "Online-Logit Distillation": 0.77,
    "Autoregressive Inference": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This is a trending concept that bridges vision and language processing, crucial for linking multimodal research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Speculative Decoding",
        "canonical": "Speculative Decoding",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique technique for accelerating model inference, relevant for linking to performance optimization studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Elastic Visual Compressor",
        "canonical": "Elastic Visual Compressor",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel component for adaptive visual data processing, useful for linking to efficiency and compression research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Online-Logit Distillation",
        "canonical": "Online-Logit Distillation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces an innovative training protocol, relevant for linking to distillation and training efficiency.",
        "novelty_score": 0.72,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Autoregressive Inference",
        "canonical": "Autoregressive Inference",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational concept in model inference, essential for linking to various model architectures.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
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
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Speculative Decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Elastic Visual Compressor",
      "resolved_canonical": "Elastic Visual Compressor",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Online-Logit Distillation",
      "resolved_canonical": "Online-Logit Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Autoregressive Inference",
      "resolved_canonical": "Autoregressive Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SpecVLM: Fast Speculative Decoding in Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11815.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.11815](https://arxiv.org/abs/2509.11815)

## 🔗 유사한 논문
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (94.0% similar)
- [[2025-09-23/Spec-VLA_ Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance_20250923|Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance]] (89.9% similar)
- [[2025-09-23/Spiffy_ Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding_20250923|Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding]] (85.9% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (85.0% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Autoregressive Inference|Autoregressive Inference]]
**⚡ Unique Technical**: [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/Elastic Visual Compressor|Elastic Visual Compressor]], [[keywords/Online-Logit Distillation|Online-Logit Distillation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11815v2 Announce Type: replace-cross 
Abstract: Speculative decoding is a powerful way to accelerate autoregressive large language models (LLMs), but directly porting it to vision-language models (VLMs) faces unique systems constraints: the prefill stage is dominated by visual tokens whose count scales with image resolution and video length, inflating both compute and memory, especially the key-value (KV) cache. We study speculative decoding for VLMs and introduce SpecVLM, a practical system that (1) establishes a strong EAGLE-2-style baseline, EagleVLM, delivering 1.5--2.3x end-to-end speedups over full autoregressive inference, and (2) further accelerates VLM inference with an elastic visual compressor that adaptively selects among pruning, pooling, convolution, and resampler primitives to balance FLOPs/parameters and accuracy per input. To avoid costly offline distillation corpora, we propose an online-logit distillation protocol that trains the draft model with on-the-fly teacher logits and penultimate features using a combined cross-entropy and Smooth L1 objective, eliminating storage and preprocessing while remaining compute-efficient. This protocol reveals a training-time scaling effect: longer online training monotonically increases the draft model's average accepted length, improving speculative efficiency. Empirically, SpecVLM achieves additional acceleration, culminating in 2.5--2.9x end-to-end speedups within 5 epochs across LLaVA and MMMU, consistently over resolutions and task difficulties, while preserving the target model's output distribution (lossless decoding). Our code is available at https://github.com/haiduo/SpecVLM.

## 📝 요약

SpecVLM은 비전-언어 모델(VLM)의 추론 속도를 향상시키기 위한 시스템으로, EAGLE-2 스타일의 EagleVLM을 기반으로 하여 전체 자가회귀 추론 대비 1.5~2.3배의 속도 향상을 제공합니다. 이 시스템은 적응형 시각 압축기를 활용하여 FLOPs/파라미터와 정확도 간의 균형을 맞추며, 오프라인 증류 코퍼스를 사용하지 않고 온라인 로짓 증류 프로토콜을 통해 저장 및 전처리 없이 효율적인 학습을 가능케 합니다. 이를 통해 SpecVLM은 LLaVA 및 MMMU에서 5 에포크 내에 2.5~2.9배의 속도 향상을 달성하며, 해상도와 작업 난이도에 관계없이 목표 모델의 출력 분포를 유지합니다.

## 🎯 주요 포인트

- 1. SpecVLM은 EAGLE-2 스타일의 EagleVLM을 기반으로 하여, 완전한 자회귀 추론에 비해 1.5~2.3배의 속도 향상을 제공합니다.
- 2. SpecVLM은 탄력적인 비주얼 압축기를 도입하여, FLOPs/파라미터와 정확도를 균형 있게 조정하며 VLM 추론을 가속화합니다.
- 3. 온라인 로짓 증류 프로토콜을 제안하여 저장 및 전처리 없이도 효율적인 계산을 유지하며, 훈련 시간 동안 초안 모델의 수용 길이를 증가시킵니다.
- 4. SpecVLM은 LLaVA와 MMMU에서 5 에포크 내에 2.5~2.9배의 속도 향상을 달성하며, 해상도와 작업 난이도에 관계없이 일관된 성능을 보입니다.
- 5. SpecVLM은 대상 모델의 출력 분포를 유지하면서 손실 없는 디코딩을 실현합니다.


---

*Generated on 2025-09-24 01:29:30*