<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:25:31.854400",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Function Calling",
    "Large Language Model",
    "Instruction Following",
    "Benchmark",
    "Formatting Rules"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Function Calling": 0.75,
    "Large Language Model": 0.8,
    "Instruction Following": 0.78,
    "Benchmark": 0.7,
    "Formatting Rules": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Function Calling",
        "canonical": "Function Calling",
        "aliases": [
          "Function Invocation"
        ],
        "category": "unique_technical",
        "rationale": "Function calling is a core capability being evaluated, making it a unique technical focus of the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the evaluation, connecting to broader discussions on AI capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Instruction Following",
        "canonical": "Instruction Following",
        "aliases": [
          "Adherence to Instructions"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a benchmark specifically for evaluating instruction following, highlighting its unique focus.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Benchmark",
        "canonical": "Benchmark",
        "aliases": [
          "Evaluation Framework"
        ],
        "category": "specific_connectable",
        "rationale": "Benchmarks are crucial for evaluating AI models, providing a direct link to performance assessments.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Formatting Rules",
        "canonical": "Formatting Rules",
        "aliases": [
          "Format Adherence"
        ],
        "category": "unique_technical",
        "rationale": "The paper highlights the importance of adhering to specific formatting rules, a unique aspect of the evaluation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
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
      "candidate_surface": "Function Calling",
      "resolved_canonical": "Function Calling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Instruction Following",
      "resolved_canonical": "Instruction Following",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Benchmark",
      "resolved_canonical": "Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Formatting Rules",
      "resolved_canonical": "Formatting Rules",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Instruction-Following Evaluation in Function Calling for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18420.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18420](https://arxiv.org/abs/2509.18420)

## 🔗 유사한 논문
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (83.1% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (81.7% similar)
- [[2025-09-18/Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (81.1% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (81.0% similar)
- [[2025-09-23/Digging Into the Internal_ Causality-Based Analysis of LLM Function Calling_20250923|Digging Into the Internal: Causality-Based Analysis of LLM Function Calling]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Benchmark|Benchmark]]
**⚡ Unique Technical**: [[keywords/Function Calling|Function Calling]], [[keywords/Instruction Following|Instruction Following]], [[keywords/Formatting Rules|Formatting Rules]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18420v1 Announce Type: new 
Abstract: Function calling is a core capability of large language models, essential for AI agents. Existing benchmarks such as the Berkeley Function Calling Leaderboard (BFCL), tau^2-Bench (arXiv:2506.07982), and ACEBench (arXiv:2501.12851) evaluate argument correctness but do not test adherence to format instructions embedded in parameter descriptions, such as enclosing values in double quotes or using ISO date formats.
  We introduce IFEval-FC, a benchmark inspired by IFEval (arXiv:2311.07911) that assesses precise instruction following in function calling. IFEval-FC encodes verifiable formats directly within JSON schema descriptions, for example specifying that a value must not contain punctuation. It includes 750 test cases, each consisting of a function with an embedded format for one of its input parameters and a corresponding user query. Evaluation is fully algorithmic, ensuring objectivity, reproducibility, and scalability.
  Our results show that even state-of-the-art proprietary models, including GPT-5 and Claude 4.1 Opus, frequently fail to follow basic formatting rules, highlighting a practical limitation for real-world agent systems. The complete codebase and data are publicly available at https://github.com/Skripkon/IFEval-FC.

## 📝 요약

이 논문은 대규모 언어 모델의 핵심 기능인 함수 호출에서 형식 지침 준수 여부를 평가하는 새로운 벤치마크 IFEval-FC를 소개합니다. 기존 벤치마크는 인수의 정확성만 평가하지만, IFEval-FC는 JSON 스키마를 통해 형식 지침 준수 여부를 테스트합니다. 750개의 테스트 사례를 포함하며, 알고리즘적 평가를 통해 객관성과 재현성을 보장합니다. 연구 결과, 최신 모델들도 기본 형식 규칙을 자주 위반하는 것으로 나타나, 실제 에이전트 시스템에서의 한계를 드러냅니다. 전체 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. IFEval-FC는 함수 호출에서 정확한 지침 준수를 평가하는 새로운 벤치마크로, JSON 스키마 설명 내에 검증 가능한 형식을 인코딩합니다.
- 2. IFEval-FC는 750개의 테스트 케이스를 포함하며, 각 케이스는 입력 매개변수에 대한 형식이 내장된 함수와 사용자 쿼리로 구성됩니다.
- 3. 평가 과정은 완전히 알고리즘적으로 이루어져 객관성, 재현성, 확장성을 보장합니다.
- 4. 최신 모델인 GPT-5와 Claude 4.1 Opus조차 기본적인 형식 규칙을 자주 따르지 못하며, 이는 실제 에이전트 시스템에서의 실용적 한계를 드러냅니다.
- 5. 전체 코드베이스와 데이터는 공개적으로 제공되며, GitHub에서 확인할 수 있습니다.


---

*Generated on 2025-09-24 13:25:31*