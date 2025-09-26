---
keywords:
  - Vision-Language Model
  - Text-to-3D Generation
  - Score Distillation Sampling
  - Geometric Coherence
  - Relational Reasoning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15772
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:09:58.207215",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Text-to-3D Generation",
    "Score Distillation Sampling",
    "Geometric Coherence",
    "Relational Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.89,
    "Text-to-3D Generation": 0.78,
    "Score Distillation Sampling": 0.77,
    "Geometric Coherence": 0.72,
    "Relational Reasoning": 0.74
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
          "Vision Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's proposed framework and are increasingly relevant in multimodal AI research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.89
      },
      {
        "surface": "Text-to-3D Generation",
        "canonical": "Text-to-3D Generation",
        "aliases": [
          "Text to 3D",
          "3D Generation from Text"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel application area that the paper specifically addresses, offering unique insights into 3D content creation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Score Distillation Sampling",
        "canonical": "Score Distillation Sampling",
        "aliases": [
          "SDS"
        ],
        "category": "unique_technical",
        "rationale": "SDS is a key technique discussed in the paper, crucial for understanding the proposed improvements.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Geometric Coherence",
        "canonical": "Geometric Coherence",
        "aliases": [
          "Geometric Consistency"
        ],
        "category": "specific_connectable",
        "rationale": "Geometric coherence is a critical aspect of the paper's evaluation of 3D models, relevant for linking to spatial analysis topics.",
        "novelty_score": 0.52,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Relational Reasoning",
        "canonical": "Relational Reasoning",
        "aliases": [
          "Object Relationships"
        ],
        "category": "specific_connectable",
        "rationale": "Relational reasoning is essential for understanding multi-object scenes, aligning with broader research in AI reasoning capabilities.",
        "novelty_score": 0.58,
        "connectivity_score": 0.8,
        "specificity_score": 0.76,
        "link_intent_score": 0.74
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
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Text-to-3D Generation",
      "resolved_canonical": "Text-to-3D Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Score Distillation Sampling",
      "resolved_canonical": "Score Distillation Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Geometric Coherence",
      "resolved_canonical": "Geometric Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Relational Reasoning",
      "resolved_canonical": "Relational Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.8,
        "specificity": 0.76,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation

**Korean Title:** 비전-언어 모델을 텍스트-3D 생성의 미분 가능한 의미적 및 공간적 보상으로 활용하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15772.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15772](https://arxiv.org/abs/2509.15772)

## 🔗 유사한 논문
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (85.8% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (84.1% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (83.7% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (82.9% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Geometric Coherence|Geometric Coherence]], [[keywords/Relational Reasoning|Relational Reasoning]]
**⚡ Unique Technical**: [[keywords/Text-to-3D Generation|Text-to-3D Generation]], [[keywords/Score Distillation Sampling|Score Distillation Sampling]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15772v1 Announce Type: new 
Abstract: Score Distillation Sampling (SDS) enables high-quality text-to-3D generation by supervising 3D models through the denoising of multi-view 2D renderings, using a pretrained text-to-image diffusion model to align with the input prompt and ensure 3D consistency. However, existing SDS-based methods face two fundamental limitations: (1) their reliance on CLIP-style text encoders leads to coarse semantic alignment and struggles with fine-grained prompts; and (2) 2D diffusion priors lack explicit 3D spatial constraints, resulting in geometric inconsistencies and inaccurate object relationships in multi-object scenes. To address these challenges, we propose VLM3D, a novel text-to-3D generation framework that integrates large vision-language models (VLMs) into the SDS pipeline as differentiable semantic and spatial priors. Unlike standard text-to-image diffusion priors, VLMs leverage rich language-grounded supervision that enables fine-grained prompt alignment. Moreover, their inherent vision language modeling provides strong spatial understanding, which significantly enhances 3D consistency for single-object generation and improves relational reasoning in multi-object scenes. We instantiate VLM3D based on the open-source Qwen2.5-VL model and evaluate it on the GPTeval3D benchmark. Experiments across diverse objects and complex scenes show that VLM3D significantly outperforms prior SDS-based methods in semantic fidelity, geometric coherence, and spatial correctness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15772v1 발표 유형: 신규  
초록: Score Distillation Sampling (SDS)는 사전 학습된 텍스트-이미지 확산 모델을 사용하여 입력 프롬프트와의 정렬을 보장하고 3D 일관성을 유지하면서 다중 뷰 2D 렌더링의 노이즈 제거를 통해 3D 모델을 감독함으로써 고품질의 텍스트-3D 생성을 가능하게 합니다. 그러나 기존의 SDS 기반 방법은 두 가지 근본적인 한계에 직면해 있습니다: (1) CLIP 스타일의 텍스트 인코더에 의존하여 세밀한 의미적 정렬이 어렵고 세부적인 프롬프트에 대한 대응이 부족하며; (2) 2D 확산 사전이 명시적인 3D 공간 제약을 결여하여 다중 객체 장면에서 기하학적 불일치와 부정확한 객체 관계를 초래합니다. 이러한 문제를 해결하기 위해, 우리는 VLM3D라는 새로운 텍스트-3D 생성 프레임워크를 제안합니다. 이는 대형 비전-언어 모델(VLMs)을 SDS 파이프라인에 통합하여 차별화된 의미적 및 공간적 사전으로 활용합니다. 표준 텍스트-이미지 확산 사전과 달리, VLMs는 세밀한 프롬프트 정렬을 가능하게 하는 풍부한 언어 기반 감독을 활용합니다. 게다가, 그들의 고유한 비전-언어 모델링은 강력한 공간 이해를 제공하여 단일 객체 생성의 3D 일관성을 크게 향상시키고 다중 객체 장면에서의 관계적 추론을 개선합니다. 우리는 오픈 소스 Qwen2.5-VL 모델을 기반으로 VLM3D를 구현하고 GPTeval3D 벤치마크에서 평가합니다. 다양한 객체와 복잡한 장면에 대한 실험 결과, VLM3D는 의미적 충실도, 기하학적 일관성 및 공간적 정확성에서 이전의 SDS 기반 방법을 현저히 능가하는 것으로 나타났습니다.

## 📝 요약

Score Distillation Sampling (SDS)는 텍스트-이미지 확산 모델을 활용하여 고품질의 텍스트-3D 생성이 가능하지만, 기존 방법론은 CLIP 스타일의 텍스트 인코더에 의존하여 세밀한 의미 정렬에 한계가 있으며, 2D 확산 모델은 명시적인 3D 공간 제약이 부족하여 기하학적 일관성이 떨어집니다. 이를 해결하기 위해 VLM3D라는 새로운 프레임워크를 제안합니다. VLM3D는 대형 비전-언어 모델(VLM)을 SDS 파이프라인에 통합하여 세밀한 프롬프트 정렬과 강력한 공간 이해를 제공합니다. 이를 통해 단일 객체 생성의 3D 일관성을 높이고, 다중 객체 장면에서의 관계 추론을 개선합니다. Qwen2.5-VL 모델을 기반으로 구현된 VLM3D는 GPTeval3D 벤치마크에서 평가되었으며, 실험 결과 다양한 객체와 복잡한 장면에서 기존 SDS 기반 방법들보다 의미적 충실도, 기하학적 일관성, 공간적 정확성에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Score Distillation Sampling(SDS)는 다중 뷰 2D 렌더링의 노이즈 제거를 통해 3D 모델을 감독하여 고품질의 텍스트-3D 생성을 가능하게 합니다.
- 2. 기존 SDS 기반 방법은 CLIP 스타일의 텍스트 인코더에 의존하여 세밀한 의미 정렬에 어려움을 겪고, 2D 확산 사전은 명시적인 3D 공간 제약이 부족하여 기하학적 불일치가 발생합니다.
- 3. VLM3D는 대형 비전-언어 모델(VLM)을 SDS 파이프라인에 통합하여 세밀한 프롬프트 정렬과 강력한 공간 이해를 통해 3D 일관성을 향상시킵니다.
- 4. VLM3D는 Qwen2.5-VL 모델을 기반으로 구현되었으며, GPTeval3D 벤치마크에서 평가되었습니다.
- 5. 실험 결과, VLM3D는 다양한 객체와 복잡한 장면에서 의미적 충실도, 기하학적 일관성, 공간적 정확성 측면에서 기존 SDS 기반 방법을 능가합니다.


---

*Generated on 2025-09-23 12:09:58*