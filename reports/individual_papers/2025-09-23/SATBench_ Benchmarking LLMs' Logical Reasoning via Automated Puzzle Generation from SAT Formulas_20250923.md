---
keywords:
  - Large Language Model
  - Boolean Satisfiability
  - Logical Reasoning
  - SATBench
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.14615
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:25:56.200732",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Boolean Satisfiability",
    "Logical Reasoning",
    "SATBench"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Boolean Satisfiability": 0.78,
    "Logical Reasoning": 0.8,
    "SATBench": 0.82
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
        "rationale": "Links to the broader context of AI and NLP research, connecting with existing work on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Boolean Satisfiability",
        "canonical": "Boolean Satisfiability",
        "aliases": [
          "SAT problems"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's methodology, providing a unique angle on logical reasoning in AI.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Logical Reasoning",
        "canonical": "Logical Reasoning",
        "aliases": [
          "Logical Puzzles"
        ],
        "category": "specific_connectable",
        "rationale": "Connects with research on reasoning capabilities of AI, a key aspect of the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "SATBench",
        "canonical": "SATBench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a novel benchmark introduced by the paper, crucial for linking related research efforts.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Boolean Satisfiability",
      "resolved_canonical": "Boolean Satisfiability",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Logical Reasoning",
      "resolved_canonical": "Logical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "SATBench",
      "resolved_canonical": "SATBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14615.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.14615](https://arxiv.org/abs/2505.14615)

## 🔗 유사한 논문
- [[2025-09-23/seqBench_ A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs_20250923|seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs]] (88.8% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (86.5% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (86.3% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (86.0% similar)
- [[2025-09-23/On LLM-Based Scientific Inductive Reasoning Beyond Equations_20250923|On LLM-Based Scientific Inductive Reasoning Beyond Equations]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Logical Reasoning|Logical Reasoning]]
**⚡ Unique Technical**: [[keywords/Boolean Satisfiability|Boolean Satisfiability]], [[keywords/SATBench|SATBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14615v2 Announce Type: replace 
Abstract: We introduce SATBench, a benchmark for evaluating the logical reasoning capabilities of large language models (LLMs) through logical puzzles derived from Boolean satisfiability (SAT) problems. Unlike prior work that focuses on inference rule-based reasoning, which often involves deducing conclusions from a set of premises, our approach leverages the search-based nature of SAT problems, where the objective is to find a solution that fulfills a specified set of logical constraints. Each instance in SATBench is generated from a SAT formula, then translated into a puzzle using LLMs. The generation process is fully automated and allows for adjustable difficulty by varying the number of clauses. All 2100 puzzles are validated through both LLM-based and solver-based consistency checks, with human validation on a subset. Experimental results show that even the strongest model, o4-mini, achieves only 65.0% accuracy on hard UNSAT problems, close to the random baseline of 50%. Our error analysis reveals systematic failures such as satisfiability bias, context inconsistency, and condition omission, highlighting limitations of current LLMs in search-based logical reasoning. Our code and data are publicly available at https://github.com/Anjiang-Wei/SATBench

## 📝 요약

SATBench는 대형 언어 모델(LLM)의 논리적 추론 능력을 평가하기 위한 벤치마크로, 부울 만족도(SAT) 문제에서 파생된 논리 퍼즐을 사용합니다. 기존 연구와 달리, SATBench는 논리적 제약을 충족하는 해를 찾는 SAT 문제의 탐색 기반 특성을 활용합니다. 퍼즐은 SAT 공식을 LLM을 통해 자동 생성하며, 난이도 조절이 가능합니다. 2100개의 퍼즐은 LLM 및 솔버 기반의 일관성 검증을 거쳤고, 일부는 인간 검증도 수행되었습니다. 실험 결과, 가장 강력한 모델인 o4-mini도 어려운 UNSAT 문제에서 65.0%의 정확도를 기록해, 무작위 기준인 50%에 근접했습니다. 오류 분석을 통해 현재 LLM의 탐색 기반 논리 추론의 한계를 드러내는 체계적 실패를 확인했습니다. 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. SATBench는 대형 언어 모델(LLM)의 논리적 추론 능력을 평가하기 위해 SAT 문제에서 파생된 논리 퍼즐을 사용하는 벤치마크입니다.
- 2. SATBench는 완전 자동화된 생성 과정을 통해 난이도를 조절할 수 있으며, LLM 및 솔버 기반의 일관성 검사를 통해 검증되었습니다.
- 3. 실험 결과, 가장 강력한 모델인 o4-mini조차도 어려운 UNSAT 문제에서 65.0%의 정확도를 기록하여 무작위 기준인 50%에 근접한 성과를 보였습니다.
- 4. 오류 분석 결과, 현재 LLM의 한계로서 만족 가능성 편향, 문맥 불일치, 조건 누락 등의 체계적인 실패가 드러났습니다.
- 5. SATBench의 코드와 데이터는 공개되어 있으며, 연구자들이 LLM의 논리적 추론 능력을 더욱 발전시킬 수 있는 기회를 제공합니다.


---

*Generated on 2025-09-24 00:25:56*