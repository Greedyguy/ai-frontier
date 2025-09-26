---
keywords:
  - Continual Learning
  - Language-guided Supervision
  - Multi-Prototype Supervision
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16011
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:17:06.860980",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Learning",
    "Language-guided Supervision",
    "Multi-Prototype Supervision",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continual Learning": 0.78,
    "Language-guided Supervision": 0.81,
    "Multi-Prototype Supervision": 0.83,
    "Vision-Language Model": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "CL"
        ],
        "category": "broad_technical",
        "rationale": "Continual Learning is a foundational concept in machine learning, relevant for linking with other adaptive learning techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Language-guided supervision",
        "canonical": "Language-guided Supervision",
        "aliases": [
          "Language-guided"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach in the context of visual learning, enhancing the specificity of language and vision integration.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Multi-Prototype Supervision",
        "canonical": "Multi-Prototype Supervision",
        "aliases": [
          "MuproCL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new method for handling semantic ambiguity and visual diversity, crucial for linking advanced learning models.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.83
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This represents a growing area of research that bridges vision and language, enhancing connectivity with multimodal studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
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
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Language-guided supervision",
      "resolved_canonical": "Language-guided Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Multi-Prototype Supervision",
      "resolved_canonical": "Multi-Prototype Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Towards Robust Visual Continual Learning with Multi-Prototype Supervision

**Korean Title:** 강건한 시각적 지속 학습을 위한 다중 프로토타입 감독 방법 연구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16011.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16011](https://arxiv.org/abs/2509.16011)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (85.5% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (84.9% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (84.8% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (84.7% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Continual Learning|Continual Learning]]
**⚡ Unique Technical**: [[keywords/Language-guided Supervision|Language-guided Supervision]], [[keywords/Multi-Prototype Supervision|Multi-Prototype Supervision]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16011v1 Announce Type: new 
Abstract: Language-guided supervision, which utilizes a frozen semantic target from a Pretrained Language Model (PLM), has emerged as a promising paradigm for visual Continual Learning (CL). However, relying on a single target introduces two critical limitations: 1) semantic ambiguity, where a polysemous category name results in conflicting visual representations, and 2) intra-class visual diversity, where a single prototype fails to capture the rich variety of visual appearances within a class. To this end, we propose MuproCL, a novel framework that replaces the single target with multiple, context-aware prototypes. Specifically, we employ a lightweight LLM agent to perform category disambiguation and visual-modal expansion to generate a robust set of semantic prototypes. A LogSumExp aggregation mechanism allows the vision model to adaptively align with the most relevant prototype for a given image. Extensive experiments across various CL baselines demonstrate that MuproCL consistently enhances performance and robustness, establishing a more effective path for language-guided continual learning.

## 🔍 Abstract (한글 번역)

arXiv:2509.16011v1 발표 유형: 새로운 것  
초록: 사전 학습된 언어 모델(PLM)에서 고정된 의미적 목표를 활용하는 언어 안내 감독은 시각적 연속 학습(CL)을 위한 유망한 패러다임으로 부상하고 있습니다. 그러나 단일 목표에 의존하는 것은 두 가지 중요한 한계를 초래합니다: 1) 다의적 범주 이름이 상충되는 시각적 표현을 초래하는 의미적 모호성, 2) 단일 프로토타입이 클래스 내의 다양한 시각적 외형을 포착하지 못하는 클래스 내 시각적 다양성. 이를 해결하기 위해, 우리는 MuproCL이라는 새로운 프레임워크를 제안하여 단일 목표를 다중의, 문맥 인식 프로토타입으로 대체합니다. 구체적으로, 우리는 경량의 LLM 에이전트를 사용하여 범주 비모호화 및 시각-모달 확장을 수행하여 강력한 의미적 프로토타입 세트를 생성합니다. LogSumExp 집계 메커니즘은 비전 모델이 주어진 이미지에 가장 관련성이 높은 프로토타입과 적응적으로 정렬할 수 있도록 합니다. 다양한 CL 기준선에 대한 광범위한 실험을 통해 MuproCL이 성능과 견고성을 지속적으로 향상시키며, 언어 안내 연속 학습을 위한 보다 효과적인 경로를 확립함을 보여줍니다.

## 📝 요약

이 논문은 사전 학습된 언어 모델(PLM)을 활용한 언어 기반 감독이 시각적 지속 학습(CL)에서 유망한 접근법으로 떠오르고 있음을 설명합니다. 기존 방법의 한계를 극복하기 위해, MuproCL이라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 단일 목표 대신 다중, 문맥 인식 프로토타입을 사용하여 의미적 모호성과 클래스 내 시각적 다양성을 해결합니다. 경량 LLM 에이전트를 활용해 카테고리 비모호화와 시각-모달 확장을 수행하며, LogSumExp 집계 메커니즘을 통해 가장 관련성 높은 프로토타입과 적응적으로 정렬합니다. 다양한 CL 기준 실험에서 MuproCL은 성능과 견고성을 지속적으로 향상시켜 언어 기반 지속 학습의 효과적인 경로를 제시합니다.

## 🎯 주요 포인트

- 1. MuproCL은 단일 목표 대신 다중, 문맥 인식 프로토타입을 사용하여 시각적 지속 학습의 성능을 향상시킵니다.
- 2. 경량 LLM 에이전트를 활용하여 범주 비모호화 및 시각적 모달 확장을 수행합니다.
- 3. LogSumExp 집계 메커니즘을 통해 비전 모델이 주어진 이미지에 가장 관련성 있는 프로토타입과 적응적으로 정렬할 수 있도록 합니다.
- 4. 다양한 지속 학습 기준 실험에서 MuproCL은 일관되게 성능과 견고성을 향상시킵니다.
- 5. MuproCL은 언어 기반 지속 학습을 위한 보다 효과적인 경로를 제시합니다.


---

*Generated on 2025-09-23 12:17:06*