---
keywords:
  - Trace Abstraction Refinement
  - Software Model Checking
  - Ultimate Automizer
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13699
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:18:56.483216",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Trace Abstraction Refinement",
    "Software Model Checking",
    "Ultimate Automizer"
  ],
  "rejected_keywords": [
    "Parallel Computing"
  ],
  "similarity_scores": {
    "Trace Abstraction Refinement": 0.79,
    "Software Model Checking": 0.78,
    "Ultimate Automizer": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Multi-Threaded Software Model Checking via Parallel Trace Abstraction Refinement

**Korean Title:** 병렬 추적 추상화 정제를 통한 다중 스레드 소프트웨어 모델 검사

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Software Model Checking|software model checking]]
**⚡ Unique Technical**: [[keywords/Trace Abstraction Refinement|trace abstraction refinement]], [[keywords/Ultimate Automizer|Ultimate Automizer]]

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (79.7% similar)
- [[Trace_Sampling_2.0_Code_Knowledge_Enhanced_Span-level_Sampling_for_Distributed_Tracing_20250918|Trace Sampling 2.0: Code Knowledge Enhanced Span-level Sampling for Distributed Tracing]] (79.2% similar)
- [[An_LLM_Agentic_Approach_for_Legal-Critical_Software_A_Case_Study_for_Tax_Prep_Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (78.5% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (78.4% similar)
- [[Self-Guided_Function_Calling_in_Large_Language_Models_via_Stepwise_Experience_Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13699v1 Announce Type: cross 
Abstract: Automatic software verification is a valuable means for software quality assurance. However, automatic verification and in particular software model checking can be time-consuming, which hinders their practical applicability e.g., the use in continuous integration. One solution to address the issue is to reduce the response time of the verification procedure by leveraging today's multi-core CPUs.
  In this paper, we propose a solution to parallelize trace abstraction, an abstraction-based approach to software model checking. The underlying idea of our approach is to parallelize the abstraction refinement. More concretely, our approach analyzes different traces (syntactic program paths) that could violate the safety property in parallel. We realize our parallelized version of trace abstraction in the verification tool Ulti mate Automizer and perform a thorough evaluation. Our evaluation shows that our parallelization is more effective than sequential trace abstraction and can provide results significantly faster on many time-consuming tasks. Also, our approach is more effective than DSS, a recent parallel approach to abstraction-based software model checking.

## 🔍 Abstract (한글 번역)

arXiv:2509.13699v1 발표 유형: 교차
요약: 자동 소프트웨어 검증은 소프트웨어 품질 보증을 위한 가치 있는 수단입니다. 그러나 자동 검증 및 특히 소프트웨어 모델 검사는 시간이 많이 소요되어 연속적인 통합 등에서의 실용성을 방해할 수 있습니다. 이 문제를 해결하기 위한 한 가지 방법은 오늘날의 멀티코어 CPU를 활용하여 검증 절차의 응답 시간을 줄이는 것입니다.
본 논문에서는 소프트웨어 모델 검사에 대한 추상화 기반 접근 방식인 추적 추상화를 병렬화하는 솔루션을 제안합니다. 우리 접근 방식의 기본 아이디어는 추상화 정제를 병렬화하는 것입니다. 구체적으로, 우리 접근 방식은 안전 속성을 위반할 수 있는 서로 다른 추적(구문적 프로그램 경로)을 병렬로 분석합니다. 우리는 검증 도구 Ulti mate Automizer에서 추적 추상화의 병렬화 버전을 실현하고 철저한 평가를 수행합니다. 우리의 평가 결과, 우리의 병렬화가 순차적 추적 추상화보다 효과적이며 많은 시간이 소요되는 작업에서 결과를 상당히 빠르게 제공할 수 있음을 보여줍니다. 또한, 우리 접근 방식은 최근의 추상화 기반 소프트웨어 모델 검사에 대한 병렬 접근 방식인 DSS보다 더 효과적입니다.

## 📝 요약

이 논문은 소프트웨어 품질 보증을 위한 자동 소프트웨어 검증의 시간 소요 문제를 해결하기 위해 오늘날의 멀티코어 CPU를 활용하여 추적 추상화를 병렬화하는 방법을 제안한다. 이를 통해 안전 속성을 위반할 수 있는 다양한 추적을 병렬로 분석함으로써 검증 절차의 응답 시간을 단축시킨다. Ulti mate Automizer에서 병렬화된 추적 추상화를 구현하고 철저한 평가를 실시한 결과, 순차적 추적 추상화보다 훨씬 빠른 결과를 제공할 수 있음을 확인하였으며, DSS보다 더 효과적인 것으로 나타났다. 이는 소프트웨어 모델 검증에 대한 새로운 병렬 접근 방법을 제시한 것으로 볼 수 있다.

## 🎯 주요 포인트

- 소프트웨어 모델 검증을 위한 추상화 기반 접근 방식을 병렬화하여 검증 프로세스의 응답 시간을 단축하는 방법을 제안함

- 병렬 추상화를 통해 안전 속성을 위반할 수 있는 다양한 추적을 병렬로 분석하여 검증 성능을 향상시킴

- Ulti mate Automizer에서 병렬 추상화를 구현하고 평가 결과, 순차적 추상화보다 빠르게 결과를 제공하며 최근 병렬 접근 방식보다 효과적임.

---

*Generated on 2025-09-18 17:23:31*