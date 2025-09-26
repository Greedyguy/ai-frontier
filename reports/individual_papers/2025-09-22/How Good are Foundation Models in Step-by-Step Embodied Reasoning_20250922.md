---
keywords:
  - Foundation Model Embodied Reasoning
  - Multimodal Learning
  - Embodied Agents
  - Robot Intelligence
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15293
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:55:27.039254",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Model Embodied Reasoning",
    "Multimodal Learning",
    "Embodied Agents",
    "Robot Intelligence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Foundation Model Embodied Reasoning": 0.78,
    "Multimodal Learning": 0.8,
    "Embodied Agents": 0.77,
    "Robot Intelligence": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Foundation Model Embodied Reasoning",
        "canonical": "Foundation Model Embodied Reasoning",
        "aliases": [
          "FoMER"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel benchmark specifically designed to evaluate embodied reasoning in foundation models, offering unique insights into this research area.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Multimodal Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "LMMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is crucial for understanding and linking the capabilities of models that process multiple types of data, such as vision and language.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Embodied Agents",
        "canonical": "Embodied Agents",
        "aliases": [
          "Physical Agents"
        ],
        "category": "unique_technical",
        "rationale": "Embodied agents are central to the study of physical interaction and decision-making in real-world environments, a key focus of this paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Robot Intelligence",
        "canonical": "Robot Intelligence",
        "aliases": [
          "Robotic Intelligence"
        ],
        "category": "evolved_concepts",
        "rationale": "Robot intelligence encompasses the broader aim of improving decision-making and reasoning in robotic systems, as discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "step-by-step reasoning",
      "evaluation framework",
      "empirical analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Foundation Model Embodied Reasoning",
      "resolved_canonical": "Foundation Model Embodied Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Multimodal Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Embodied Agents",
      "resolved_canonical": "Embodied Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Robot Intelligence",
      "resolved_canonical": "Robot Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# How Good are Foundation Models in Step-by-Step Embodied Reasoning?

**Korean Title:** 기초 모델은 단계별 구현 추론에서 얼마나 우수한가?

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15293.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15293](https://arxiv.org/abs/2509.15293)

## 🔗 유사한 논문
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (84.4% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (84.4% similar)
- [[2025-09-22/Multi-Physics_ A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems_20250922|Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems]] (84.3% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory]] (84.0% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Foundation Model Embodied Reasoning|Foundation Model Embodied Reasoning]], [[keywords/Embodied Agents|Embodied Agents]]
**🚀 Evolved Concepts**: [[keywords/Robot Intelligence|Robot Intelligence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15293v1 Announce Type: new 
Abstract: Embodied agents operating in the physical world must make decisions that are not only effective but also safe, spatially coherent, and grounded in context. While recent advances in large multimodal models (LMMs) have shown promising capabilities in visual understanding and language generation, their ability to perform structured reasoning for real-world embodied tasks remains underexplored. In this work, we aim to understand how well foundation models can perform step-by-step reasoning in embodied environments. To this end, we propose the Foundation Model Embodied Reasoning (FoMER) benchmark, designed to evaluate the reasoning capabilities of LMMs in complex embodied decision-making scenarios. Our benchmark spans a diverse set of tasks that require agents to interpret multimodal observations, reason about physical constraints and safety, and generate valid next actions in natural language. We present (i) a large-scale, curated suite of embodied reasoning tasks, (ii) a novel evaluation framework that disentangles perceptual grounding from action reasoning, and (iii) empirical analysis of several leading LMMs under this setting. Our benchmark includes over 1.1k samples with detailed step-by-step reasoning across 10 tasks and 8 embodiments, covering three different robot types. Our results highlight both the potential and current limitations of LMMs in embodied reasoning, pointing towards key challenges and opportunities for future research in robot intelligence. Our data and code will be made publicly available.

## 🔍 Abstract (한글 번역)

arXiv:2509.15293v1 발표 유형: 신규  
초록: 물리적 세계에서 활동하는 구현된 에이전트는 효과적일 뿐만 아니라 안전하고, 공간적으로 일관되며, 맥락에 기반한 결정을 내려야 합니다. 최근의 대규모 멀티모달 모델(LMMs)의 발전은 시각적 이해와 언어 생성에서 유망한 능력을 보여주었지만, 실제 세계의 구현된 작업을 위한 구조적 추론을 수행하는 능력은 아직 충분히 탐구되지 않았습니다. 이 연구에서는 기본 모델이 구현된 환경에서 단계별 추론을 얼마나 잘 수행할 수 있는지를 이해하고자 합니다. 이를 위해, 우리는 복잡한 구현된 의사결정 시나리오에서 LMMs의 추론 능력을 평가하기 위해 설계된 Foundation Model Embodied Reasoning (FoMER) 벤치마크를 제안합니다. 우리의 벤치마크는 에이전트가 멀티모달 관찰을 해석하고, 물리적 제약과 안전에 대해 추론하며, 자연어로 유효한 다음 행동을 생성해야 하는 다양한 작업 세트를 포함합니다. 우리는 (i) 대규모로 큐레이션된 구현된 추론 작업 모음, (ii) 지각적 기반과 행동 추론을 분리하는 새로운 평가 프레임워크, (iii) 이 설정에서 여러 주요 LMMs의 실증적 분석을 제시합니다. 우리의 벤치마크는 10개의 작업과 8개의 구현을 통해 3가지 다른 로봇 유형을 다루며, 1.1k 이상의 샘플과 세부적인 단계별 추론을 포함합니다. 우리의 결과는 구현된 추론에서 LMMs의 잠재력과 현재의 한계를 강조하며, 로봇 지능의 미래 연구를 위한 주요 도전과 기회를 제시합니다. 우리의 데이터와 코드는 공개될 예정입니다.

## 📝 요약

이 논문은 물리적 세계에서 작동하는 구현된 에이전트의 단계별 추론 능력을 평가하기 위해 FoMER 벤치마크를 제안합니다. 이 벤치마크는 대규모 멀티모달 모델(LMMs)의 복잡한 의사결정 시나리오에서의 추론 능력을 평가하는 데 중점을 둡니다. 연구는 멀티모달 관찰 해석, 물리적 제약 및 안전성에 대한 추론, 자연어로의 유효한 행동 생성 능력을 포함한 다양한 과제를 다룹니다. 1.1k 이상의 샘플과 10개의 과제, 8개의 구현을 포함하며, LMMs의 현재 한계와 잠재력을 보여줍니다. 데이터와 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 본 연구는 물리적 세계에서의 화신 에이전트의 단계별 추론 능력을 평가하기 위해 FoMER 벤치마크를 제안합니다.
- 2. FoMER 벤치마크는 LMMs의 복잡한 화신 의사결정 시나리오에서의 추론 능력을 평가하기 위한 다양한 과제를 포함합니다.
- 3. 연구는 지각적 기반과 행동 추론을 분리하는 새로운 평가 프레임워크를 도입합니다.
- 4. 10개의 과제와 8개의 화신을 포함한 1.1k 이상의 샘플을 통해 LMMs의 잠재력과 현재 한계를 강조합니다.
- 5. 연구 데이터와 코드는 공개될 예정이며, 로봇 지능 연구의 주요 과제와 기회를 제시합니다.


---

*Generated on 2025-09-23 11:55:27*