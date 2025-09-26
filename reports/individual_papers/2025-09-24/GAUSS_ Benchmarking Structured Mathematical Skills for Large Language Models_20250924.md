<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:36:57.601981",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "GAUSS Benchmark",
    "Mathematical Skills",
    "Problem Solving and Communication Skills"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "GAUSS Benchmark": 0.8,
    "Mathematical Skills": 0.78,
    "Problem Solving and Communication Skills": 0.7
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus, linking to a broad technical category enhances connectivity across related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "GAUSS",
        "canonical": "GAUSS Benchmark",
        "aliases": [
          "General Assessment of Underlying Structured Skills"
        ],
        "category": "unique_technical",
        "rationale": "A unique benchmark introduced in the paper, crucial for linking specific research on mathematical skills evaluation.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "mathematical abilities",
        "canonical": "Mathematical Skills",
        "aliases": [
          "math skills",
          "math abilities"
        ],
        "category": "specific_connectable",
        "rationale": "Key focus of the benchmark, facilitating connections to research on skill evaluation and cognitive abilities.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "problem solving and communication",
        "canonical": "Problem Solving and Communication Skills",
        "aliases": [
          "problem-solving",
          "communication skills"
        ],
        "category": "specific_connectable",
        "rationale": "Specific skills assessed by GAUSS, relevant for linking to educational and cognitive skill research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "knowledge and understanding",
      "meta-skills and creativity"
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
      "candidate_surface": "GAUSS",
      "resolved_canonical": "GAUSS Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "mathematical abilities",
      "resolved_canonical": "Mathematical Skills",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "problem solving and communication",
      "resolved_canonical": "Problem Solving and Communication Skills",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GAUSS: Benchmarking Structured Mathematical Skills for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18122.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18122](https://arxiv.org/abs/2509.18122)

## 🔗 유사한 논문
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (83.7% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (83.5% similar)
- [[2025-09-23/LLMsPark_ A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts_20250923|LLMsPark: A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts]] (82.9% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (81.9% similar)
- [[2025-09-24/G\"odel Test_ Can Large Language Models Solve Easy Conjectures?_20250924|G\"odel Test: Can Large Language Models Solve Easy Conjectures?]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mathematical Skills|Mathematical Skills]], [[keywords/Problem Solving and Communication Skills|Problem Solving and Communication Skills]]
**⚡ Unique Technical**: [[keywords/GAUSS Benchmark|GAUSS Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18122v1 Announce Type: new 
Abstract: We introduce \textbf{GAUSS} (\textbf{G}eneral \textbf{A}ssessment of \textbf{U}nderlying \textbf{S}tructured \textbf{S}kills in Mathematics), a benchmark that evaluates LLMs' mathematical abilities across twelve core skill dimensions, grouped into three domains: knowledge and understanding, problem solving and communication, and meta-skills and creativity. By categorizing problems according to cognitive skills and designing tasks that isolate specific abilities, GAUSS constructs comprehensive, fine-grained, and interpretable profiles of models' mathematical abilities. These profiles faithfully represent their underlying mathematical intelligence. To exemplify how to use the \textsc{GAUSS} benchmark, we have derived the skill profile of \textsc{GPT-5-thinking}, revealing its strengths and weaknesses as well as its differences relative to \textsc{o4-mini-high}, thereby underscoring the value of multidimensional, skill-based evaluation.

## 📝 요약

이 논문은 수학적 능력을 평가하는 벤치마크인 GAUSS를 소개합니다. GAUSS는 지식 및 이해, 문제 해결 및 의사소통, 메타 스킬 및 창의성의 세 가지 영역에서 12개의 핵심 기술 차원을 통해 대형 언어 모델(LLM)의 수학적 능력을 평가합니다. 문제를 인지적 기술에 따라 분류하고 특정 능력을 분리하는 과제를 설계함으로써, GAUSS는 모델의 수학적 능력에 대한 포괄적이고 세밀하며 해석 가능한 프로필을 구축합니다. 이를 통해 모델의 수학적 지능을 충실히 나타냅니다. GAUSS 벤치마크의 사용 예시로, GPT-5-thinking의 기술 프로필을 도출하여 강점과 약점, 그리고 o4-mini-high와의 차이를 밝혀내어 다차원적이고 기술 기반의 평가의 가치를 강조합니다.

## 🎯 주요 포인트

- 1. GAUSS는 수학적 능력을 평가하기 위한 벤치마크로, 12개의 핵심 기술 차원을 통해 LLMs의 수학적 능력을 평가합니다.
- 2. GAUSS는 문제를 인지적 기술에 따라 분류하고 특정 능력을 분리하여 평가함으로써 모델의 수학적 능력에 대한 세밀하고 해석 가능한 프로필을 제공합니다.
- 3. GAUSS 벤치마크를 사용하여 GPT-5-thinking의 기술 프로필을 도출함으로써, 그 강점과 약점 및 o4-mini-high와의 차이를 밝혀냈습니다.
- 4. 다차원적이고 기술 기반의 평가의 가치를 강조하며, 모델의 수학적 지능을 충실히 나타냅니다.


---

*Generated on 2025-09-24 15:36:57*