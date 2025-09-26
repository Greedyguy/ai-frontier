---
keywords:
  - Zeroth-Order Optimization
  - Multi-Query Paradigm
  - Projection Alignment
  - Single-Query Approach
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15552
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:30:19.277359",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zeroth-Order Optimization",
    "Multi-Query Paradigm",
    "Projection Alignment",
    "Single-Query Approach"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zeroth-Order Optimization": 0.78,
    "Multi-Query Paradigm": 0.77,
    "Projection Alignment": 0.79,
    "Single-Query Approach": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zeroth-Order Optimization",
        "canonical": "Zeroth-Order Optimization",
        "aliases": [
          "ZO Optimization",
          "Zeroth Order Optimization"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique optimization technique central to the paper's discussion and not widely covered in existing vocabularies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-Query Paradigm",
        "canonical": "Multi-Query Paradigm",
        "aliases": [
          "Multi-Query Approach"
        ],
        "category": "unique_technical",
        "rationale": "The multi-query approach is a key concept in the paper, offering a new perspective on query allocation in optimization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Projection Alignment",
        "canonical": "Projection Alignment",
        "aliases": [
          "ZO-Align"
        ],
        "category": "unique_technical",
        "rationale": "Projection Alignment is a novel method introduced in the paper, providing a new aggregation technique in optimization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Single-Query Approach",
        "canonical": "Single-Query Approach",
        "aliases": [
          "Single Query"
        ],
        "category": "unique_technical",
        "rationale": "This approach is contrasted with the multi-query paradigm, highlighting its significance in optimization strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.62,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
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
      "candidate_surface": "Zeroth-Order Optimization",
      "resolved_canonical": "Zeroth-Order Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-Query Paradigm",
      "resolved_canonical": "Multi-Query Paradigm",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Projection Alignment",
      "resolved_canonical": "Projection Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Single-Query Approach",
      "resolved_canonical": "Single-Query Approach",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.62,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# The Multi-Query Paradox in Zeroth-Order Optimization

**Korean Title:** 제로차 최적화에서의 다중 쿼리 역설

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15552.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15552](https://arxiv.org/abs/2509.15552)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (82.9% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.6% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (80.6% similar)
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (80.0% similar)
- [[2025-09-19/Mechanism Design with Outliers and Predictions_20250919|Mechanism Design with Outliers and Predictions]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Zeroth-Order Optimization|Zeroth-Order Optimization]], [[keywords/Multi-Query Paradigm|Multi-Query Paradigm]], [[keywords/Projection Alignment|Projection Alignment]], [[keywords/Single-Query Approach|Single-Query Approach]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15552v1 Announce Type: new 
Abstract: Zeroth-order (ZO) optimization provides a powerful framework for problems where explicit gradients are unavailable and have to be approximated using only queries to function value. The prevalent single-query approach is simple, but suffers from high estimation variance, motivating a multi-query paradigm to improves estimation accuracy. This, however, creates a critical trade-off: under a fixed budget of queries (i.e. cost), queries per iteration and the total number of optimization iterations are inversely proportional to one another. How to best allocate this budget is a fundamental, under-explored question.
  This work systematically resolves this query allocation problem. We analyze two aggregation methods: the de facto simple averaging (ZO-Avg), and a new Projection Alignment method (ZO-Align) we derive from local surrogate minimization. By deriving convergence rates for both methods that make the dependence on the number of queries explicit across strongly convex, convex, non-convex, and stochastic settings, we uncover a stark dichotomy: For ZO-Avg, we prove that using more than one query per iteration is always query-inefficient, rendering the single-query approach optimal. On the contrary, ZO-Align generally performs better with more queries per iteration, resulting in a full-subspace estimation as the optimal approach. Thus, our work clarifies that the multi-query problem boils down to a choice not about an intermediate query size, but between two classic algorithms, a choice dictated entirely by the aggregation method used. These theoretical findings are also consistently validated by extensive experiments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15552v1 발표 유형: 신규  
초록: 제로차수(ZO) 최적화는 명시적인 기울기가 제공되지 않고 함수 값에 대한 질의만을 사용하여 근사해야 하는 문제에 대해 강력한 프레임워크를 제공합니다. 일반적인 단일 질의 접근 방식은 간단하지만 높은 추정 분산으로 인해 추정 정확도를 향상시키기 위한 다중 질의 패러다임이 필요합니다. 그러나 이는 중요한 절충 문제를 야기합니다: 고정된 질의 예산(즉, 비용) 하에서, 반복당 질의 수와 최적화 반복의 총 횟수는 서로 반비례합니다. 이 예산을 최적으로 할당하는 방법은 근본적이지만 충분히 탐구되지 않은 질문입니다.  
이 연구는 이러한 질의 할당 문제를 체계적으로 해결합니다. 우리는 두 가지 집계 방법을 분석합니다: 사실상의 단순 평균(ZO-Avg)과 지역 대리 최소화를 통해 도출한 새로운 투영 정렬 방법(ZO-Align)입니다. 강하게 볼록, 볼록, 비볼록, 확률적 설정 전반에 걸쳐 질의 수에 대한 의존성을 명시적으로 만드는 두 방법의 수렴 속도를 도출함으로써, 우리는 뚜렷한 이분법을 발견합니다: ZO-Avg의 경우, 반복당 하나 이상의 질의를 사용하는 것이 항상 질의 비효율적임을 증명하여 단일 질의 접근 방식이 최적임을 보여줍니다. 반면에, ZO-Align은 일반적으로 반복당 더 많은 질의로 더 나은 성능을 발휘하며, 결과적으로 전체 부분 공간 추정이 최적의 접근 방식이 됩니다. 따라서, 우리의 연구는 다중 질의 문제가 중간 질의 크기에 대한 선택이 아니라, 사용된 집계 방법에 의해 전적으로 결정되는 두 가지 고전 알고리즘 간의 선택으로 귀결됨을 명확히 합니다. 이러한 이론적 발견은 광범위한 실험을 통해 일관되게 검증됩니다.

## 📝 요약

이 논문은 명시적 기울기가 없는 문제에서 함수 값만으로 근사하여 최적화를 수행하는 영차(zeroth-order) 최적화의 쿼리 할당 문제를 다룹니다. 기존의 단일 쿼리 방법은 단순하지만 추정 변동성이 크며, 이를 개선하기 위해 다중 쿼리 방법이 제안됩니다. 논문에서는 두 가지 집계 방법인 단순 평균(ZO-Avg)과 새로운 투영 정렬 방법(ZO-Align)을 분석합니다. 강하게 볼록, 볼록, 비볼록, 확률적 설정에서 두 방법의 수렴 속도를 도출하여 쿼리 수에 대한 의존성을 명확히 합니다. 결과적으로, ZO-Avg는 단일 쿼리가 최적임을 증명하며, ZO-Align은 다중 쿼리가 더 효율적임을 보여줍니다. 이론적 발견은 실험을 통해 검증되었습니다.

## 🎯 주요 포인트

- 1. 제로스 오더(ZO) 최적화는 명시적 기울기가 없는 문제에서 함수 값 쿼리만으로 근사하여 최적화를 수행하는 강력한 프레임워크를 제공합니다.
- 2. 단일 쿼리 접근법은 간단하지만 높은 추정 분산 문제를 겪어, 정확도를 높이기 위한 다중 쿼리 패러다임이 필요합니다.
- 3. 쿼리 예산 하에서 쿼리당 반복 횟수와 최적화 반복 횟수 사이의 상충 관계가 존재하며, 이 예산을 최적으로 배분하는 것이 중요한 문제입니다.
- 4. ZO-Avg 방법에서는 반복당 하나 이상의 쿼리를 사용하는 것이 비효율적이며, 단일 쿼리 접근법이 최적임을 증명했습니다.
- 5. ZO-Align 방법은 반복당 더 많은 쿼리를 사용할 때 일반적으로 더 나은 성능을 보이며, 전체 서브스페이스 추정이 최적의 접근법임을 보여줍니다.


---

*Generated on 2025-09-23 10:30:19*