---
keywords:
  - Large Language Model
  - 3D Scene Understanding
  - Vision-Language Model
  - 3D Task Planning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16721
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:31:41.778310",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "3D Scene Understanding",
    "Vision-Language Model",
    "3D Task Planning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "3D Scene Understanding": 0.78,
    "Vision-Language Model": 0.82,
    "3D Task Planning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "MLLMs"
        ],
        "category": "broad_technical",
        "rationale": "Linking this to existing work on language models helps connect research on extending these models to new modalities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "3D Scene Understanding",
        "canonical": "3D Scene Understanding",
        "aliases": [
          "3D Scene Parsing"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique focus of the paper, crucial for linking to specific research in 3D environments.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This connects the paper to the evolving field of integrating vision and language, a key aspect of the research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "3D Task Planning",
        "canonical": "3D Task Planning",
        "aliases": [
          "InPlan3D"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area of the research, providing a link to task-oriented studies in 3D environments.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "scene",
      "framework",
      "description"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "3D Scene Understanding",
      "resolved_canonical": "3D Scene Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "3D Task Planning",
      "resolved_canonical": "3D Task Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Text-Scene: A Scene-to-Language Parsing Framework for 3D Scene Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16721.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16721](https://arxiv.org/abs/2509.16721)

## 🔗 유사한 논문
- [[2025-09-22/SCENEFORGE_ Enhancing 3D-text alignment with Structured Scene Compositions_20250922|SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions]] (87.0% similar)
- [[2025-09-18/UniPLV_ Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision_20250918|UniPLV: Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision]] (85.2% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (84.7% similar)
- [[2025-09-22/OptiScene_ LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization_20250922|OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization]] (83.9% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/3D Scene Understanding|3D Scene Understanding]], [[keywords/3D Task Planning|3D Task Planning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16721v1 Announce Type: cross 
Abstract: Enabling agents to understand and interact with complex 3D scenes is a fundamental challenge for embodied artificial intelligence systems. While Multimodal Large Language Models (MLLMs) have achieved significant progress in 2D image understanding, extending such capabilities to 3D scenes remains difficult: 1) 3D environment involves richer concepts such as spatial relationships, affordances, physics, layout, and so on, 2) the absence of large-scale 3D vision-language datasets has posed a significant obstacle. In this paper, we introduce Text-Scene, a framework that automatically parses 3D scenes into textual descriptions for scene understanding. Given a 3D scene, our model identifies object attributes and spatial relationships, and then generates a coherent summary of the whole scene, bridging the gap between 3D observation and language without requiring human-in-the-loop intervention. By leveraging both geometric analysis and MLLMs, Text-Scene produces descriptions that are accurate, detailed, and human-interpretable, capturing object-level details and global-level context. Experimental results on benchmarks demonstrate that our textual parses can faithfully represent 3D scenes and benefit downstream tasks. To evaluate the reasoning capability of MLLMs, we present InPlan3D, a comprehensive benchmark for 3D task planning, consisting of 3174 long-term planning tasks across 636 indoor scenes. We emphasize clarity and accessibility in our approach, aiming to make 3D scene content understandable through language. Code and datasets will be released.

## 📝 요약

이 논문은 복잡한 3D 장면을 이해하고 상호작용할 수 있는 인공지능 시스템 개발을 목표로 합니다. 기존의 다중모달 대형 언어 모델(MLLMs)이 2D 이미지 이해에서 성과를 거두었지만, 3D 장면으로 확장하는 데 어려움이 있습니다. 이를 해결하기 위해, 이 논문은 3D 장면을 자동으로 텍스트로 변환하는 'Text-Scene' 프레임워크를 제안합니다. 이 모델은 3D 장면의 객체 속성과 공간 관계를 식별하고, 인간의 개입 없이 장면의 전체적인 요약을 생성합니다. 실험 결과, 이 방법은 3D 장면을 정확하고 상세하게 표현하며, 후속 작업에 유용함을 보여줍니다. 또한, 3D 작업 계획을 위한 'InPlan3D' 벤치마크를 제시하여 MLLMs의 추론 능력을 평가합니다. 연구의 코드와 데이터셋은 공개될 예정입니다.

## 🎯 주요 포인트

- 1. Text-Scene은 3D 장면을 자동으로 텍스트 설명으로 변환하여 장면 이해를 돕는 프레임워크입니다.
- 2. 이 모델은 3D 장면에서 객체 속성과 공간 관계를 식별하고, 전체 장면의 일관된 요약을 생성합니다.
- 3. Text-Scene은 기하학적 분석과 다중모달 대형 언어 모델(MLLMs)을 활용하여 정확하고 상세하며 인간이 해석 가능한 설명을 제공합니다.
- 4. InPlan3D는 3D 작업 계획을 위한 포괄적인 벤치마크로, 636개의 실내 장면에서 3174개의 장기 계획 작업을 포함합니다.
- 5. 코드와 데이터셋은 공개될 예정이며, 3D 장면 내용을 언어로 이해할 수 있도록 접근성을 강조합니다.


---

*Generated on 2025-09-23 23:31:41*