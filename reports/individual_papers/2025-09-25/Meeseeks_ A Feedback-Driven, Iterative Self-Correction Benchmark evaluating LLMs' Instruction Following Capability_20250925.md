---
keywords:
  - Large Language Model
  - Chain-of-Thought Prompting
  - Self-Correction Methodologies
  - Feedback Mechanism
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2504.21625
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:53:50.778096",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Prompting",
    "Self-Correction Methodologies",
    "Feedback Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Prompting": 0.78,
    "Self-Correction Methodologies": 0.8,
    "Feedback Mechanism": 0.77
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
        "rationale": "Central to the paper's focus on instruction-following capabilities and feedback mechanisms.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought prompting",
        "canonical": "Chain-of-Thought Prompting",
        "aliases": [
          "CoT prompting"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a specific technique relevant to the iterative self-correction process discussed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "self-correction methodologies",
        "canonical": "Self-Correction Methodologies",
        "aliases": [
          "self-correction methods"
        ],
        "category": "unique_technical",
        "rationale": "Describes a unique approach central to the benchmark's functionality.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "feedback mechanism",
        "canonical": "Feedback Mechanism",
        "aliases": [
          "feedback systems"
        ],
        "category": "unique_technical",
        "rationale": "Integral to the iterative improvement process of LLMs as described in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "instruction",
      "benchmark",
      "performance",
      "analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought prompting",
      "resolved_canonical": "Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "self-correction methodologies",
      "resolved_canonical": "Self-Correction Methodologies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "feedback mechanism",
      "resolved_canonical": "Feedback Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Meeseeks: A Feedback-Driven, Iterative Self-Correction Benchmark evaluating LLMs' Instruction Following Capability

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.21625.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2504.21625](https://arxiv.org/abs/2504.21625)

## 🔗 유사한 논문
- [[2025-09-25/Language Models Fail to Introspect About Their Knowledge of Language_20250925|Language Models Fail to Introspect About Their Knowledge of Language]] (87.1% similar)
- [[2025-09-23/seqBench_ A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs_20250923|seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs]] (87.1% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (86.6% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.6% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (86.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
**⚡ Unique Technical**: [[keywords/Self-Correction Methodologies|Self-Correction Methodologies]], [[keywords/Feedback Mechanism|Feedback Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.21625v5 Announce Type: replace 
Abstract: The capability to precisely adhere to instructions is a cornerstone for Large Language Models (LLMs) to function as dependable agents in real-world scenarios. However, confronted with complex prompts, LLMs frequently encounter difficulties in fulfilling all specified requirements within a single response. Drawing inspiration from recent advancements in Chain-of-Thought (CoT) prompting and self-correction methodologies, we introduce Meeseeks (The name is inspired by Mr. Meeseeks from "Rick and Morty," a character renowned for efficiently accomplishing assigned tasks. See: https://en.wikipedia.org/wiki/Mr._Meeseeks), a fully automated iterative instruction-following benchmark equipped with an integrated feedback mechanism. Meeseeks identifies erroneous components in model responses and provides corresponding feedback accurately, thereby iteratively guiding the model toward self-correction. The dataset contains over 700 curated instances annotated by 32 distinct capability tags in Chinese and English. Extensive experimental results reveal that different state-of-the-art commercial and open-source LLMs exhibit vastly disparate performance, and even after 20 turns of iterative feedback-driven self-correction, nearly all models demonstrate suboptimal performance. We conducted comprehensive analysis from both macro and instance levels, uncovering numerous common issues prevalent in current state-of-the-art models, as well as several counterintuitive phenomena. We've open-sourced our work on https://github.com/ADoublLEN/Meeseeks.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 복잡한 지시를 정확히 따르는 능력을 향상시키기 위해 Meeseeks라는 자동화된 벤치마크를 소개합니다. Meeseeks는 모델의 응답에서 오류를 식별하고 피드백을 제공하여 모델이 스스로 수정할 수 있도록 유도합니다. 700개 이상의 사례가 포함된 데이터셋을 통해 다양한 상용 및 오픈 소스 LLM의 성능을 평가한 결과, 대부분의 모델이 20번의 피드백 후에도 최적의 성능을 보이지 못했습니다. 연구는 현재 최첨단 모델의 일반적인 문제와 몇 가지 예기치 않은 현상을 밝혀냈으며, 연구 결과는 오픈 소스로 공개되었습니다.

## 🎯 주요 포인트

- 1. Meeseeks는 복잡한 지시 사항을 충실히 따르기 위해 설계된 자동화된 반복적 지시 수행 벤치마크입니다.
- 2. 이 벤치마크는 모델 응답의 오류를 식별하고 피드백을 제공하여 모델이 자체 수정할 수 있도록 유도합니다.
- 3. 데이터셋은 중국어와 영어로 된 700개 이상의 사례를 포함하고 있으며, 32개의 능력 태그로 주석이 달려 있습니다.
- 4. 실험 결과, 상업 및 오픈 소스 LLM의 성능이 크게 다르며, 20번의 반복적인 피드백 후에도 거의 모든 모델이 최적의 성능을 보이지 않았습니다.
- 5. 연구는 매크로 및 개별 사례 수준에서의 분석을 통해 현재 최첨단 모델의 일반적인 문제와 몇 가지 직관에 반하는 현상을 밝혀냈습니다.


---

*Generated on 2025-09-26 08:53:50*