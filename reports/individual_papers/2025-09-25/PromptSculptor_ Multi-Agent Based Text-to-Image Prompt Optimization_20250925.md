---
keywords:
  - Vision-Language Model
  - PromptSculptor
  - Chain-of-Thought Reasoning
  - Multi-Agent System
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.12446
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:35:12.040766",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "PromptSculptor",
    "Chain-of-Thought Reasoning",
    "Multi-Agent System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.8,
    "PromptSculptor": 0.78,
    "Chain-of-Thought Reasoning": 0.77,
    "Multi-Agent System": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Text-to-Image models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "T2I models",
          "Text-to-Image systems"
        ],
        "category": "evolved_concepts",
        "rationale": "Connects to the growing field of models that integrate visual and linguistic data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "PromptSculptor",
        "canonical": "PromptSculptor",
        "aliases": [
          "Prompt Optimization Framework"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel framework specifically designed for optimizing prompts in generative AI.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Chain-of-Thought reasoning",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "A method that enhances understanding and inference in AI, relevant to prompt refinement.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "multi-agent framework",
        "canonical": "Multi-Agent System",
        "aliases": [
          "multi-agent architecture"
        ],
        "category": "broad_technical",
        "rationale": "Describes a system architecture that is applicable across various AI applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "generative AI",
      "user feedback",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Text-to-Image models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "PromptSculptor",
      "resolved_canonical": "PromptSculptor",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Chain-of-Thought reasoning",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "multi-agent framework",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# PromptSculptor: Multi-Agent Based Text-to-Image Prompt Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12446.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.12446](https://arxiv.org/abs/2509.12446)

## 🔗 유사한 논문
- [[2025-09-24/PromptEnhancer_ A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting_20250924|PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting]] (89.9% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (85.0% similar)
- [[2025-09-23/PromptSuite_ A Task-Agnostic Framework for Multi-Prompt Generation_20250923|PromptSuite: A Task-Agnostic Framework for Multi-Prompt Generation]] (83.9% similar)
- [[2025-09-23/ComposeMe_ Attribute-Specific Image Prompts for Controllable Human Image Generation_20250923|ComposeMe: Attribute-Specific Image Prompts for Controllable Human Image Generation]] (83.9% similar)
- [[2025-09-24/Attack for Defense_ Adversarial Agents for Point Prompt Optimization Empowering Segment Anything Model_20250924|Attack for Defense: Adversarial Agents for Point Prompt Optimization Empowering Segment Anything Model]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Agent System|Multi-Agent System]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]]
**⚡ Unique Technical**: [[keywords/PromptSculptor|PromptSculptor]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12446v2 Announce Type: replace-cross 
Abstract: The rapid advancement of generative AI has democratized access to powerful tools such as Text-to-Image models. However, to generate high-quality images, users must still craft detailed prompts specifying scene, style, and context-often through multiple rounds of refinement. We propose PromptSculptor, a novel multi-agent framework that automates this iterative prompt optimization process. Our system decomposes the task into four specialized agents that work collaboratively to transform a short, vague user prompt into a comprehensive, refined prompt. By leveraging Chain-of-Thought reasoning, our framework effectively infers hidden context and enriches scene and background details. To iteratively refine the prompt, a self-evaluation agent aligns the modified prompt with the original input, while a feedback-tuning agent incorporates user feedback for further refinement. Experimental results demonstrate that PromptSculptor significantly enhances output quality and reduces the number of iterations needed for user satisfaction. Moreover, its model-agnostic design allows seamless integration with various T2I models, paving the way for industrial applications.

## 📝 요약

PromptSculptor는 텍스트-이미지(T2I) 모델의 프롬프트 최적화 과정을 자동화하는 새로운 다중 에이전트 프레임워크입니다. 이 시스템은 짧고 모호한 사용자 프롬프트를 포괄적이고 정교한 프롬프트로 변환하기 위해 네 개의 전문 에이전트가 협력합니다. Chain-of-Thought 추론을 활용하여 숨겨진 맥락을 추론하고 장면 및 배경 세부사항을 풍부하게 만듭니다. 자기 평가 에이전트는 수정된 프롬프트를 원래 입력과 정렬하고, 피드백 조정 에이전트는 사용자 피드백을 반영하여 추가로 개선합니다. 실험 결과, PromptSculptor는 출력 품질을 크게 향상시키고 사용자 만족을 위한 반복 횟수를 줄이며, 다양한 T2I 모델과의 원활한 통합이 가능해 산업적 응용 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. PromptSculptor는 사용자의 짧고 모호한 프롬프트를 포괄적이고 정제된 프롬프트로 변환하는 자동화된 프롬프트 최적화 프레임워크입니다.
- 2. 이 시스템은 네 개의 전문 에이전트로 작업을 분해하여 협력적으로 프롬프트를 개선합니다.
- 3. Chain-of-Thought 추론을 활용하여 숨겨진 맥락을 추론하고 장면 및 배경 세부 정보를 풍부하게 합니다.
- 4. 실험 결과, PromptSculptor는 출력 품질을 크게 향상시키고 사용자 만족을 위한 반복 횟수를 줄입니다.
- 5. 모델에 구애받지 않는 설계로 다양한 텍스트-이미지 변환 모델과의 원활한 통합이 가능합니다.


---

*Generated on 2025-09-25 16:35:12*