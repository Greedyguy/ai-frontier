<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:54:57.326890",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Table-to-Report Task",
    "T2R-bench",
    "Industrial Tables"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Table-to-Report Task": 0.78,
    "T2R-bench": 0.82,
    "Industrial Tables": 0.77
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
        "rationale": "Large Language Models are central to the paper's discussion on table reasoning and report generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Table-to-Report Task",
        "canonical": "Table-to-Report Task",
        "aliases": [
          "T2R Task"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique task proposed by the paper, crucial for understanding the benchmark's purpose.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "T2R-bench",
        "canonical": "T2R-bench",
        "aliases": [
          "T2R Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "The benchmark is a central contribution of the paper, providing a new resource for evaluating LLMs.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Industrial Tables",
        "canonical": "Industrial Tables",
        "aliases": [
          "Real-World Tables"
        ],
        "category": "specific_connectable",
        "rationale": "The use of real-world industrial tables is a key aspect of the benchmark's design and application.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "complexity",
      "diversity",
      "evaluation criteria"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Table-to-Report Task",
      "resolved_canonical": "Table-to-Report Task",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "T2R-bench",
      "resolved_canonical": "T2R-bench",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Industrial Tables",
      "resolved_canonical": "Industrial Tables",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# T2R-bench: A Benchmark for Generating Article-Level Reports from Real World Industrial Tables

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.19813.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2508.19813](https://arxiv.org/abs/2508.19813)

## 🔗 유사한 논문
- [[2025-09-23/TableEval_ A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering_20250923|TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering]] (84.9% similar)
- [[2025-09-23/Quality Assessment of Tabular Data using Large Language Models and Code Generation_20250923|Quality Assessment of Tabular Data using Large Language Models and Code Generation]] (83.4% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (83.2% similar)
- [[2025-09-23/Table2LaTeX-RL_ High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models_20250923|Table2LaTeX-RL: High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models]] (83.2% similar)
- [[2025-09-23/seqBench_ A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs_20250923|seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Industrial Tables|Industrial Tables]]
**⚡ Unique Technical**: [[keywords/Table-to-Report Task|Table-to-Report Task]], [[keywords/T2R-bench|T2R-bench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.19813v4 Announce Type: replace 
Abstract: Extensive research has been conducted to explore the capabilities of large language models (LLMs) in table reasoning. However, the essential task of transforming tables information into reports remains a significant challenge for industrial applications. This task is plagued by two critical issues: 1) the complexity and diversity of tables lead to suboptimal reasoning outcomes; and 2) existing table benchmarks lack the capacity to adequately assess the practical application of this task. To fill this gap, we propose the table-to-report task and construct a bilingual benchmark named T2R-bench, where the key information flow from the tables to the reports for this task. The benchmark comprises 457 industrial tables, all derived from real-world scenarios and encompassing 19 industry domains as well as 4 types of industrial tables. Furthermore, we propose an evaluation criteria to fairly measure the quality of report generation. The experiments on 25 widely-used LLMs reveal that even state-of-the-art models like Deepseek-R1 only achieves performance with 62.71 overall score, indicating that LLMs still have room for improvement on T2R-bench.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 테이블 추론 능력을 탐구하는 연구로, 테이블 정보를 보고서로 변환하는 작업의 어려움을 다룹니다. 주요 기여는 테이블-보고서 변환 작업을 제안하고, 이를 평가하기 위한 이중 언어 벤치마크인 T2R-bench를 구축한 것입니다. T2R-bench는 19개 산업 분야와 4가지 유형의 산업 테이블을 포함한 457개의 실제 테이블로 구성되어 있습니다. 또한, 보고서 생성 품질을 공정하게 평가하기 위한 기준도 제안되었습니다. 25개의 LLM을 실험한 결과, 최첨단 모델인 Deepseek-R1조차 62.71의 점수를 기록하여 LLM이 T2R-bench에서 개선의 여지가 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 표 추론 능력은 광범위하게 연구되었으나, 표 정보를 보고서로 변환하는 작업은 여전히 산업적 응용에서 큰 도전 과제로 남아 있다.
- 2. 표의 복잡성과 다양성으로 인해 최적의 추론 결과를 얻기 어렵고, 기존의 표 벤치마크는 이 작업의 실제 응용을 충분히 평가하지 못한다.
- 3. 이러한 격차를 해소하기 위해, 우리는 표-보고서 변환 작업을 제안하고, 이 작업을 위한 핵심 정보 흐름을 포함하는 이중 언어 벤치마크 T2R-bench를 구축하였다.
- 4. T2R-bench는 19개 산업 도메인과 4가지 유형의 산업 표를 포함하는 457개의 실제 시나리오에서 유래한 산업 표로 구성되어 있다.
- 5. 25개의 널리 사용되는 LLM에 대한 실험 결과, 최첨단 모델인 Deepseek-R1조차 62.71의 전체 점수만을 기록하여 LLM이 T2R-bench에서 여전히 개선의 여지가 있음을 나타낸다.


---

*Generated on 2025-09-24 15:54:57*