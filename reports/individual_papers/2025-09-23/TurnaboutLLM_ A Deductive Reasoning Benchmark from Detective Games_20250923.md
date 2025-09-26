---
keywords:
  - Large Language Model
  - Deductive Reasoning
  - Chain-of-Thought Prompting
  - Context Size
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.15712
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:56:46.253656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Deductive Reasoning",
    "Chain-of-Thought Prompting",
    "Context Size"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Deductive Reasoning": 0.8,
    "Chain-of-Thought Prompting": 0.82,
    "Context Size": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on evaluating deductive reasoning capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "deductive reasoning",
        "canonical": "Deductive Reasoning",
        "aliases": [
          "deductive logic"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding the evaluation framework presented in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Chain-of-Thought prompting",
        "canonical": "Chain-of-Thought Prompting",
        "aliases": [
          "CoT prompting"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for linking strategies used to enhance reasoning in LLMs.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "context size",
        "canonical": "Context Size",
        "aliases": [
          "narrative context size"
        ],
        "category": "unique_technical",
        "rationale": "Important for understanding the factors affecting model performance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "dataset",
      "testimonies",
      "evidences"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "deductive reasoning",
      "resolved_canonical": "Deductive Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Chain-of-Thought prompting",
      "resolved_canonical": "Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "context size",
      "resolved_canonical": "Context Size",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.15712.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.15712](https://arxiv.org/abs/2505.15712)

## 🔗 유사한 논문
- [[2025-09-23/InMind_ Evaluating LLMs in Capturing and Applying Individual Human Reasoning Styles_20250923|InMind: Evaluating LLMs in Capturing and Applying Individual Human Reasoning Styles]] (87.5% similar)
- [[2025-09-23/LLMsPark_ A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts_20250923|LLMsPark: A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts]] (87.4% similar)
- [[2025-09-23/D-REX_ A Benchmark for Detecting Deceptive Reasoning in Large Language Models_20250923|D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models]] (86.8% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (86.6% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
**⚡ Unique Technical**: [[keywords/Deductive Reasoning|Deductive Reasoning]], [[keywords/Context Size|Context Size]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.15712v2 Announce Type: replace 
Abstract: This paper introduces TurnaboutLLM, a novel framework and dataset for evaluating the deductive reasoning abilities of Large Language Models (LLMs) by leveraging the interactive gameplay of detective games Ace Attorney and Danganronpa. The framework tasks LLMs with identifying contradictions between testimonies and evidences within long narrative contexts, a challenging task due to the large answer space and diverse reasoning types presented by its questions. We evaluate twelve state-of-the-art LLMs on the dataset, hinting at limitations of popular strategies for enhancing deductive reasoning such as extensive thinking and Chain-of-Thought prompting. The results also suggest varying effects of context size, the number of reasoning step and answer space size on model performance. Overall, TurnaboutLLM presents a substantial challenge for LLMs' deductive reasoning abilities in complex, narrative-rich environments.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 연역적 추론 능력을 평가하기 위한 새로운 프레임워크와 데이터셋인 TurnaboutLLM을 소개합니다. 이 프레임워크는 'Ace Attorney'와 'Danganronpa' 같은 탐정 게임의 상호작용을 활용하여, LLM이 긴 서사적 맥락에서 증언과 증거 간의 모순을 식별하도록 합니다. 12개의 최신 LLM을 평가한 결과, 연역적 추론을 강화하기 위한 일반적인 전략인 심층 사고와 연쇄적 사고 유도법의 한계를 시사합니다. 또한, 맥락의 크기, 추론 단계 수, 답변 공간 크기가 모델 성능에 미치는 다양한 영향을 제시합니다. TurnaboutLLM은 복잡하고 서사적인 환경에서 LLM의 연역적 추론 능력에 상당한 도전 과제를 제공합니다.

## 🎯 주요 포인트

- 1. TurnaboutLLM은 Ace Attorney와 Danganronpa 게임을 활용하여 대형 언어 모델(LLM)의 연역적 추론 능력을 평가하는 새로운 프레임워크와 데이터셋을 소개합니다.
- 2. 이 프레임워크는 LLM이 긴 서사적 맥락 내에서 증언과 증거 사이의 모순을 식별하도록 요구하며, 이는 다양한 추론 유형과 큰 답변 공간 때문에 도전적인 과제입니다.
- 3. 12개의 최첨단 LLM을 데이터셋에서 평가한 결과, 광범위한 사고와 Chain-of-Thought 프롬프트와 같은 연역적 추론 강화 전략의 한계를 암시합니다.
- 4. 연구 결과는 맥락 크기, 추론 단계 수 및 답변 공간 크기가 모델 성능에 미치는 다양한 영향을 시사합니다.
- 5. 전반적으로 TurnaboutLLM은 복잡하고 서사적인 환경에서 LLM의 연역적 추론 능력에 상당한 도전을 제시합니다.


---

*Generated on 2025-09-24 03:56:46*