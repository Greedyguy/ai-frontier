---
keywords:
  - Transductive Program Synthesis
  - Large Language Model
  - Active Learning
  - Playgol
  - MBPP+
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17393
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:59:35.125506",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transductive Program Synthesis",
    "Large Language Model",
    "Active Learning",
    "Playgol",
    "MBPP+"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transductive Program Synthesis": 0.78,
    "Large Language Model": 0.85,
    "Active Learning": 0.77,
    "Playgol": 0.72,
    "MBPP+": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "transductive program synthesis",
        "canonical": "Transductive Program Synthesis",
        "aliases": [
          "test-time transduction"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to program synthesis that leverages test inputs, enhancing robustness and efficiency.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the proposed method for predicting outputs and eliminating inconsistent hypotheses.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "active learning",
        "canonical": "Active Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Describes the framework's approach to improving synthesis by actively selecting test inputs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Playgol",
        "canonical": "Playgol",
        "aliases": [
          "string transformation benchmark"
        ],
        "category": "unique_technical",
        "rationale": "A specific dataset used to evaluate the method, relevant for linking to similar benchmarks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "MBPP+",
        "canonical": "MBPP+",
        "aliases": [
          "Python code generation benchmark"
        ],
        "category": "unique_technical",
        "rationale": "Another dataset used for evaluation, important for connections to code generation tasks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.62,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "robustness",
      "efficiency",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "transductive program synthesis",
      "resolved_canonical": "Transductive Program Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "active learning",
      "resolved_canonical": "Active Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Playgol",
      "resolved_canonical": "Playgol",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "MBPP+",
      "resolved_canonical": "MBPP+",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.62,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Program Synthesis via Test-Time Transduction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17393.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17393](https://arxiv.org/abs/2509.17393)

## 🔗 유사한 논문
- [[2025-09-22/Rethinking Molecule Synthesizability with Chain-of-Reaction_20250922|Rethinking Molecule Synthesizability with Chain-of-Reaction]] (81.6% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (81.0% similar)
- [[2025-09-19/Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (80.6% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (80.3% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Active Learning|Active Learning]]
**⚡ Unique Technical**: [[keywords/Transductive Program Synthesis|Transductive Program Synthesis]], [[keywords/Playgol|Playgol]], [[keywords/MBPP+|MBPP+]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17393v1 Announce Type: new 
Abstract: We introduce transductive program synthesis, a new formulation of the program synthesis task that explicitly leverages test inputs during synthesis. While prior approaches to program synthesis--whether based on natural language descriptions or input-output examples--typically aim to generalize from training examples, they often struggle with robustness, especially in real-world settings where training examples are limited and test inputs involve various edge cases. To address this, we propose a novel framework that improves robustness by treating synthesis as an active learning over a finite hypothesis class defined by programs' outputs. We use an LLM to predict outputs for selected test inputs and eliminate inconsistent hypotheses, where the inputs are chosen via a greedy maximin algorithm to minimize the number of LLM queries required. We evaluate our approach on two real-world datasets: Playgol, a string transformation benchmark, and MBPP+, a Python code generation benchmark. We demonstrate that our method significantly improves program synthesis in both accuracy and efficiency. We release our code at https://github.com/klee972/SYNTRA.

## 📝 요약

이 논문은 테스트 입력을 활용하는 새로운 프로그램 합성 방식인 전이적 프로그램 합성을 소개합니다. 기존의 프로그램 합성 방법은 훈련 예시로부터 일반화를 목표로 하지만, 실제 환경에서는 훈련 예시가 제한적이고 테스트 입력이 다양한 경계 사례를 포함해 강건성에 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 프로그램의 출력을 기반으로 한 유한 가설 집합에서 능동 학습으로 합성을 처리하는 새로운 프레임워크를 제안합니다. 선택된 테스트 입력에 대해 LLM을 사용하여 출력을 예측하고 일관되지 않은 가설을 제거하며, 입력은 LLM 쿼리 수를 최소화하기 위해 탐욕적 최대 최소 알고리즘으로 선택됩니다. Playgol과 MBPP+ 데이터셋에서의 실험 결과, 이 방법이 프로그램 합성의 정확성과 효율성을 크게 향상시킴을 보여줍니다. 코드는 https://github.com/klee972/SYNTRA에서 공개되었습니다.

## 🎯 주요 포인트

- 1. 전이적 프로그램 합성은 테스트 입력을 합성 과정에서 활용하여 기존 방법의 한계를 극복하려는 새로운 접근 방식입니다.
- 2. 제안된 프레임워크는 프로그램의 출력에 의해 정의된 유한한 가설 집합을 통해 능동 학습을 수행하여 합성의 견고성을 향상시킵니다.
- 3. LLM을 사용하여 선택된 테스트 입력에 대한 출력을 예측하고, 불일치하는 가설을 제거하여 LLM 쿼리 수를 최소화합니다.
- 4. 제안된 방법은 Playgol과 MBPP+ 데이터셋에서 프로그램 합성의 정확성과 효율성을 크게 향상시킵니다.
- 5. 연구의 코드는 https://github.com/klee972/SYNTRA에서 공개되었습니다.


---

*Generated on 2025-09-23 22:59:35*