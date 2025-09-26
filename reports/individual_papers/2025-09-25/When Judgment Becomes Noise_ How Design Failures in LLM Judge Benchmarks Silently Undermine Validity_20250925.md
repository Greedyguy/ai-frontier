---
keywords:
  - Large Language Model Benchmarks
  - Psychometric Validity
  - ELO Aggregation
  - Schema Incoherence
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20293
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:05:51.430521",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model Benchmarks",
    "Psychometric Validity",
    "ELO Aggregation",
    "Schema Incoherence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model Benchmarks": 0.78,
    "Psychometric Validity": 0.74,
    "ELO Aggregation": 0.71,
    "Schema Incoherence": 0.69
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-judged benchmarks",
        "canonical": "Large Language Model Benchmarks",
        "aliases": [
          "LLM Benchmarks"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to discussions on evaluation frameworks for language models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "psychometric validity",
        "canonical": "Psychometric Validity",
        "aliases": [
          "validity signals"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel evaluation metric for benchmarking reliability.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.81,
        "link_intent_score": 0.74
      },
      {
        "surface": "ELO-style aggregation",
        "canonical": "ELO Aggregation",
        "aliases": [
          "ELO ranking"
        ],
        "category": "unique_technical",
        "rationale": "Links to ranking systems used in competitive settings.",
        "novelty_score": 0.68,
        "connectivity_score": 0.73,
        "specificity_score": 0.77,
        "link_intent_score": 0.71
      },
      {
        "surface": "schema incoherence",
        "canonical": "Schema Incoherence",
        "aliases": [
          "incoherent schema"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific design flaw impacting benchmark validity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.66,
        "specificity_score": 0.75,
        "link_intent_score": 0.69
      }
    ],
    "ban_list_suggestions": [
      "benchmark rankings",
      "high-confidence rankings",
      "evaluation schema"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-judged benchmarks",
      "resolved_canonical": "Large Language Model Benchmarks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "psychometric validity",
      "resolved_canonical": "Psychometric Validity",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.81,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "ELO-style aggregation",
      "resolved_canonical": "ELO Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.73,
        "specificity": 0.77,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "schema incoherence",
      "resolved_canonical": "Schema Incoherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.66,
        "specificity": 0.75,
        "link_intent": 0.69
      }
    }
  ]
}
-->

# When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20293.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20293](https://arxiv.org/abs/2509.20293)

## 🔗 유사한 논문
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (84.8% similar)
- [[2025-09-23/LLMsPark_ A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts_20250923|LLMsPark: A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts]] (84.3% similar)
- [[2025-09-25/Do Before You Judge_ Self-Reference as a Pathway to Better LLM Evaluation_20250925|Do Before You Judge: Self-Reference as a Pathway to Better LLM Evaluation]] (84.3% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (83.7% similar)
- [[2025-09-23/SATBench_ Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas_20250923|SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Model Benchmarks|Large Language Model Benchmarks]]
**⚡ Unique Technical**: [[keywords/Psychometric Validity|Psychometric Validity]], [[keywords/ELO Aggregation|ELO Aggregation]], [[keywords/Schema Incoherence|Schema Incoherence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20293v1 Announce Type: cross 
Abstract: LLM-judged benchmarks are increasingly used to evaluate complex model behaviors, yet their design introduces failure modes absent in conventional ground-truth based benchmarks. We argue that without tight objectives and verifiable constructions, benchmark rankings can produce high-confidence rankings that are in fact largely noise. We introduce two mechanisms to diagnose these issues. Schematic adherence quantifies how much of a judge's overall verdict is explained by the explicit evaluation schema, revealing unexplained variance when judges deviate from their own rubric. Psychometric validity aggregates internal consistency and discriminant validity signals to quantify irreducible uncertainty in any benchmarking run. Applying these tools to Arena-Hard Auto, we find severe schema incoherence and factor collapse across popular judges: for example, unexplained variance exceeding 90 percent for DeepSeek-R1-32B and factor correlations above 0.93 for most criteria. We also show that the ELO-style aggregation used by Arena-Hard Auto collapses and masks genuine ranking uncertainty. Our results highlight design failures that undermine validity and offer actionable principles for building better-scoped, reliability-aware LLM-judged benchmarks. We release our code at https://anonymous.4open.science/r/judgment-to-noise-947D/README.md

## 📝 요약

이 논문은 LLM(대형 언어 모델) 기반 평가 기준의 설계 문제를 지적하며, 기존의 명확한 정답 기반 평가와 달리 높은 불확실성을 내포할 수 있음을 주장합니다. 저자들은 평가 기준의 일관성을 측정하는 '도식적 준수'와 심리측정학적 타당성을 활용하여 평가의 불확실성을 진단하는 두 가지 방법을 제시합니다. 이를 Arena-Hard Auto에 적용한 결과, 평가 기준의 일관성 부족과 높은 상관관계로 인한 평가 신뢰성 문제를 발견했습니다. 이러한 문제를 해결하기 위한 개선 방안을 제안하며, 관련 코드를 공개했습니다.

## 🎯 주요 포인트

- 1. LLM-judged 벤치마크는 복잡한 모델 행동 평가에 사용되지만, 기존의 진실 기반 벤치마크와는 다른 실패 모드를 가지고 있다.
- 2. 명확한 목표와 검증 가능한 구조가 없으면 벤치마크 순위는 실제로는 노이즈에 불과한 높은 신뢰도의 순위를 생성할 수 있다.
- 3. 스키마 일관성은 판사의 평가가 명시된 평가 스키마에 의해 얼마나 설명되는지를 정량화하여, 판사가 자신의 기준에서 벗어날 때 설명되지 않는 변동성을 드러낸다.
- 4. 심리측정학적 타당성은 내부 일관성과 변별 타당성 신호를 집계하여 벤치마킹 실행에서 줄일 수 없는 불확실성을 정량화한다.
- 5. Arena-Hard Auto에 이 도구들을 적용한 결과, 인기 있는 판사들 사이에서 심각한 스키마 불일치와 요소 붕괴가 발견되었으며, ELO 스타일의 집계 방식이 진정한 순위 불확실성을 은폐한다는 것을 보여준다.


---

*Generated on 2025-09-25 16:05:51*