---
keywords:
  - Theory of Mind
  - Multimodal Mental States
  - Multimodal Learning
  - Vision-Language Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2507.04415
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:06:51.111525",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Theory of Mind",
    "Multimodal Mental States",
    "Multimodal Learning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Theory of Mind": 0.78,
    "Multimodal Mental States": 0.79,
    "Multimodal Learning": 0.81,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Theory of Mind",
        "canonical": "Theory of Mind",
        "aliases": [
          "ToM"
        ],
        "category": "unique_technical",
        "rationale": "Theory of Mind is a central concept in understanding social intelligence and is crucial for linking multimodal AI research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal Mental States",
        "canonical": "Multimodal Mental States",
        "aliases": [
          "MoMentS"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific benchmark introduced in the paper, providing a unique dataset for evaluating Theory of Mind in AI.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is essential for integrating various data types, which is a key challenge highlighted in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.72,
        "link_intent_score": 0.81
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are crucial for understanding and integrating visual and textual data, as discussed in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "performance",
      "questions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Theory of Mind",
      "resolved_canonical": "Theory of Mind",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal Mental States",
      "resolved_canonical": "Multimodal Mental States",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.72,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MOMENTS: A Comprehensive Multimodal Benchmark for Theory of Mind

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.04415.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2507.04415](https://arxiv.org/abs/2507.04415)

## 🔗 유사한 논문
- [[2025-09-23/TactfulToM_ Do LLMs Have the Theory of Mind Ability to Understand White Lies?_20250923|TactfulToM: Do LLMs Have the Theory of Mind Ability to Understand White Lies?]] (85.0% similar)
- [[2025-09-23/AuditoryBench++_ Can Language Models Understand Auditory Knowledge without Hearing?_20250923|AuditoryBench++: Can Language Models Understand Auditory Knowledge without Hearing?]] (84.5% similar)
- [[2025-09-19/OnlineMate_ An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning_20250919|OnlineMate: An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (84.0% similar)
- [[2025-09-23/Evaluating Multimodal Large Language Models with Daily Composite Tasks in Home Environments_20250923|Evaluating Multimodal Large Language Models with Daily Composite Tasks in Home Environments]] (82.9% similar)
- [[2025-09-22/How Good are Foundation Models in Step-by-Step Embodied Reasoning?_20250922|How Good are Foundation Models in Step-by-Step Embodied Reasoning?]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Theory of Mind|Theory of Mind]], [[keywords/Multimodal Mental States|Multimodal Mental States]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04415v2 Announce Type: replace 
Abstract: Understanding Theory of Mind is essential for building socially intelligent multimodal agents capable of perceiving and interpreting human behavior. We introduce MoMentS (Multimodal Mental States), a comprehensive benchmark designed to assess the ToM capabilities of multimodal large language models (LLMs) through realistic, narrative-rich scenarios presented in short films. MoMentS includes over 2,300 multiple-choice questions spanning seven distinct ToM categories. The benchmark features long video context windows and realistic social interactions that provide deeper insight into characters' mental states. We evaluate several MLLMs and find that although vision generally improves performance, models still struggle to integrate it effectively. For audio, models that process dialogues as audio do not consistently outperform transcript-based inputs. Our findings highlight the need to improve multimodal integration and point to open challenges that must be addressed to advance AI's social understanding.

## 📝 요약

이 논문은 사회적으로 지능적인 멀티모달 에이전트를 구축하기 위해 필수적인 마음 이론(ToM)의 이해를 평가하는 MoMentS라는 벤치마크를 소개합니다. MoMentS는 짧은 영화에 등장하는 현실적이고 서사적인 시나리오를 통해 멀티모달 대형 언어 모델(LLMs)의 ToM 능력을 평가하며, 7가지 ToM 범주에 걸쳐 2,300개 이상의 객관식 질문을 포함합니다. 연구 결과, 시각 정보가 성능을 향상시키지만 효과적으로 통합하는 데 어려움이 있으며, 오디오 대화의 경우 텍스트 기반 입력보다 일관된 우위를 보이지 않는다는 점을 발견했습니다. 이 연구는 멀티모달 통합의 개선 필요성과 AI의 사회적 이해를 발전시키기 위한 과제를 강조합니다.

## 🎯 주요 포인트

- 1. MoMentS는 인간 행동을 인식하고 해석할 수 있는 사회적으로 지능적인 멀티모달 에이전트를 구축하기 위한 Theory of Mind 평가를 위한 벤치마크입니다.
- 2. MoMentS는 7개의 ToM 카테고리에 걸쳐 2,300개 이상의 객관식 질문을 포함하고 있으며, 현실적인 사회적 상호작용을 통해 캐릭터의 정신 상태에 대한 깊은 통찰을 제공합니다.
- 3. 비전 모달리티는 성능을 향상시키지만, 모델들이 이를 효과적으로 통합하는 데 어려움을 겪고 있습니다.
- 4. 오디오 모달리티의 경우, 대화를 오디오로 처리하는 모델이 텍스트 기반 입력보다 일관되게 우수한 성능을 보이지는 않습니다.
- 5. 연구 결과는 멀티모달 통합의 개선 필요성을 강조하며, AI의 사회적 이해를 발전시키기 위해 해결해야 할 과제를 제시합니다.


---

*Generated on 2025-09-24 04:06:51*