---
keywords:
  - Vision-Language Model
  - 3D Spatial Reasoning
  - Structured Prompting
  - Simulation Data
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.03642
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:01:51.342652",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "3D Spatial Reasoning",
    "Structured Prompting",
    "Simulation Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "3D Spatial Reasoning": 0.79,
    "Structured Prompting": 0.82,
    "Simulation Data": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's discussion on enhancing 3D spatial reasoning, linking to recent trends in multimodal AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "3D Spatial Reasoning",
        "canonical": "3D Spatial Reasoning",
        "aliases": [
          "3D Spatial Understanding"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving 3D spatial reasoning capabilities, a unique technical aspect not commonly addressed in existing vocabularies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Structured Prompting",
        "canonical": "Structured Prompting",
        "aliases": [
          "SpatialMind"
        ],
        "category": "unique_technical",
        "rationale": "Structured prompting is a novel approach introduced in the paper, crucial for decomposing complex scenes for better spatial reasoning.",
        "novelty_score": 0.71,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Simulation Data",
        "canonical": "Simulation Data",
        "aliases": [
          "3D Simulation Scenes"
        ],
        "category": "broad_technical",
        "rationale": "Simulation data is essential for training and testing the proposed framework, offering a broad technical link to data-driven AI research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "robotic navigation",
      "embodied interaction",
      "fine-tuning strategies"
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
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "3D Spatial Reasoning",
      "resolved_canonical": "3D Spatial Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Structured Prompting",
      "resolved_canonical": "Structured Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.71,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Simulation Data",
      "resolved_canonical": "Simulation Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

**Korean Title:** 비디오로부터의 공간 이해: 구조화된 프롬프트와 시뮬레이션 데이터의 만남

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.03642.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.03642](https://arxiv.org/abs/2506.03642)

## 🔗 유사한 논문
- [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model]] (85.3% similar)
- [[2025-09-22/GRE Suite_ Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains_20250922|GRE Suite: Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains]] (84.7% similar)
- [[2025-09-22/Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation_20250922|Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation]] (84.1% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (83.1% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Simulation Data|Simulation Data]]
**⚡ Unique Technical**: [[keywords/3D Spatial Reasoning|3D Spatial Reasoning]], [[keywords/Structured Prompting|Structured Prompting]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.03642v2 Announce Type: replace-cross 
Abstract: Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction. However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained vision-language models (VLMs). To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture. This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built from diverse 3D simulation scenes through an automated construction process designed for fine-tuning. Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.

## 🔍 Abstract (한글 번역)

arXiv:2506.03642v2 발표 유형: 교체-교차  
초록: 시각-공간적 이해, 즉 시각적 입력으로부터 객체 관계와 배치를 추론하는 능력은 로봇 내비게이션 및 구현된 상호작용과 같은 후속 작업에 필수적입니다. 그러나 기존 방법들은 공간적 불확실성과 데이터 부족에 직면하여 사전 학습된 비전-언어 모델(VLMs)의 3D 공간 추론 능력을 제한합니다. 이러한 문제를 해결하기 위해, 우리는 사전 학습된 VLMs의 아키텍처를 수정하지 않고 3D 공간 추론을 향상시키기 위한 통합 프레임워크를 제시합니다. 이 프레임워크는 복잡한 장면과 질문을 해석 가능한 추론 단계로 분해하는 구조화된 프롬프트 전략인 SpatialMind와, 다양한 3D 시뮬레이션 장면에서 자동화된 구축 과정을 통해 개발된 확장 가능한 질문-응답 데이터셋인 ScanForgeQA를 결합합니다. 여러 벤치마크에 걸친 광범위한 실험은 우리의 프롬프트 및 미세 조정 전략의 개별적 및 결합된 효과를 입증하며, 시각-공간적 이해에 대한 향후 연구에 영감을 줄 수 있는 통찰력을 제공합니다.

## 📝 요약

이 논문은 사전 학습된 비전-언어 모델(VLM)의 3D 공간 추론 능력을 향상시키기 위한 통합 프레임워크를 제안합니다. 기존 방법들이 공간 불확실성과 데이터 부족 문제를 겪는 것에 반해, 이 연구는 VLM의 아키텍처를 수정하지 않고도 성능을 개선할 수 있는 방법을 제시합니다. 주요 기여로는 복잡한 장면과 질문을 해석 가능한 추론 단계로 분해하는 구조화된 프롬프트 전략인 SpatialMind와 다양한 3D 시뮬레이션 장면에서 자동으로 구축된 대규모 질문-응답 데이터셋인 ScanForgeQA가 있습니다. 여러 벤치마크 실험을 통해 이 프레임워크의 효과가 입증되었으며, 이는 향후 시각-공간 이해 연구에 영감을 줄 수 있습니다.

## 🎯 주요 포인트

- 1. 시각적-공간적 이해는 로봇 내비게이션 및 구현된 상호작용과 같은 다운스트림 작업에 필수적입니다.
- 2. 기존 방법들은 공간적 불확실성과 데이터 부족으로 인해 사전 학습된 비전-언어 모델의 3D 공간 추론 능력이 제한됩니다.
- 3. SpatialMind와 ScanForgeQA를 결합한 통합 프레임워크는 모델 아키텍처를 수정하지 않고 3D 공간 추론을 향상시킵니다.
- 4. 다양한 벤치마크 실험을 통해 프롬프트 전략과 미세 조정 전략의 개별 및 결합 효과가 입증되었습니다.
- 5. 연구 결과는 시각적-공간적 이해에 대한 향후 연구에 영감을 줄 수 있는 통찰력을 제공합니다.


---

*Generated on 2025-09-23 10:01:51*