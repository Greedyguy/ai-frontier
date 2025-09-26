---
keywords:
  - Large Language Model
  - Equivalence Checking
  - Program Semantics
  - Program Analysis
  - Superoptimization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.12466
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:47:11.950770",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Equivalence Checking",
    "Program Semantics",
    "Program Analysis",
    "Superoptimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Equivalence Checking": 0.8,
    "Program Semantics": 0.78,
    "Program Analysis": 0.77,
    "Superoptimization": 0.76
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on evaluating reasoning capabilities in code-related tasks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Equivalence Checking",
        "canonical": "Equivalence Checking",
        "aliases": [
          "Program Equivalence",
          "Semantic Equivalence"
        ],
        "category": "unique_technical",
        "rationale": "Core concept for assessing program semantics understanding in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Program Semantics",
        "canonical": "Program Semantics",
        "aliases": [
          "Code Semantics"
        ],
        "category": "unique_technical",
        "rationale": "Essential for understanding the depth of LLMs' reasoning capabilities.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Program Analysis",
        "canonical": "Program Analysis",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Important for generating program pairs and ensuring high-confidence labels.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Superoptimization",
        "canonical": "Superoptimization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Used in generating challenging program pairs, highlighting advanced optimization techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.76
      }
    ],
    "ban_list_suggestions": [
      "task",
      "model",
      "benchmark",
      "evaluation"
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
      "candidate_surface": "Equivalence Checking",
      "resolved_canonical": "Equivalence Checking",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Program Semantics",
      "resolved_canonical": "Program Semantics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Program Analysis",
      "resolved_canonical": "Program Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Superoptimization",
      "resolved_canonical": "Superoptimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.76
      }
    }
  ]
}
-->

# EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.12466.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.12466](https://arxiv.org/abs/2502.12466)

## 🔗 유사한 논문
- [[2025-09-23/seqBench_ A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs_20250923|seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs]] (88.8% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (88.5% similar)
- [[2025-09-23/SATBench_ Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas_20250923|SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas]] (87.6% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (87.1% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Program Analysis|Program Analysis]], [[keywords/Superoptimization|Superoptimization]]
**⚡ Unique Technical**: [[keywords/Equivalence Checking|Equivalence Checking]], [[keywords/Program Semantics|Program Semantics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.12466v3 Announce Type: replace-cross 
Abstract: As large language models (LLMs) become integral to code-related tasks, a central question emerges: Do LLMs truly understand program semantics? We introduce EquiBench, a new benchmark for evaluating LLMs through equivalence checking, i.e., determining whether two programs produce identical outputs for all possible inputs. Unlike prior code generation benchmarks, this task directly tests a model's ability to reason about program semantics. EquiBench consists of 2400 program pairs across four languages and six categories. These pairs are generated through program analysis, compiler scheduling, and superoptimization, ensuring high-confidence labels, nontrivial difficulty, and full automation. We evaluate 19 state-of-the-art LLMs and find that in the most challenging categories, the best accuracies are 63.8% and 76.2%, only modestly above the 50% random baseline. Further analysis reveals that models often rely on syntactic similarity rather than exhibiting robust reasoning about program semantics, highlighting current limitations. Our code and dataset are publicly available at https://github.com/Anjiang-Wei/equibench

## 📝 요약

대형 언어 모델(LLMs)이 코드 관련 작업에 필수적이 되면서, 이들이 프로그램 의미를 진정으로 이해하는지에 대한 질문이 제기됩니다. 우리는 EquiBench라는 새로운 벤치마크를 소개하여 LLMs를 동등성 검사로 평가합니다. 이는 두 프로그램이 모든 가능한 입력에 대해 동일한 출력을 생성하는지를 판단하는 작업입니다. EquiBench는 네 개의 언어와 여섯 개의 범주에 걸쳐 2400개의 프로그램 쌍으로 구성되어 있으며, 프로그램 분석, 컴파일러 스케줄링, 초최적화를 통해 생성됩니다. 19개의 최신 LLMs를 평가한 결과, 가장 어려운 범주에서 최고 정확도는 63.8%와 76.2%로, 50%의 무작위 기준을 약간 상회하는 수준입니다. 분석 결과, 모델들이 프로그램 의미에 대한 강력한 추론보다는 구문 유사성에 의존하는 경향이 있음을 보여주어 현재의 한계를 강조합니다. 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. EquiBench는 프로그램의 동등성 검사를 통해 대형 언어 모델(LLM)의 프로그램 의미 이해 능력을 평가하는 새로운 벤치마크입니다.
- 2. 이 벤치마크는 네 가지 언어와 여섯 가지 카테고리에서 2400개의 프로그램 쌍으로 구성되어 있으며, 프로그램 분석, 컴파일러 스케줄링, 슈퍼최적화를 통해 생성되었습니다.
- 3. 19개의 최첨단 LLM을 평가한 결과, 가장 어려운 카테고리에서 최고 정확도는 63.8%와 76.2%로, 50%의 랜덤 기준선보다 약간 높은 수준입니다.
- 4. 분석 결과, 모델들이 프로그램 의미에 대한 견고한 추론보다는 구문적 유사성에 의존하는 경향이 있음을 보여주었습니다.
- 5. EquiBench의 코드와 데이터셋은 https://github.com/Anjiang-Wei/equibench에서 공개적으로 이용 가능합니다.


---

*Generated on 2025-09-24 00:47:11*