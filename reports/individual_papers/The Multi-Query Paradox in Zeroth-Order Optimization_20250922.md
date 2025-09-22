# The Multi-Query Paradox in Zeroth-Order Optimization

**Korean Title:** 제로차 최적화에서의 다중 쿼리 역설

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Query Paradigm

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (82.9% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.6% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (80.6% similar)
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (80.0% similar)
- [[2025-09-19/Mechanism Design with Outliers and Predictions_20250919|Mechanism Design with Outliers and Predictions]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15552v1 Announce Type: new 
Abstract: Zeroth-order (ZO) optimization provides a powerful framework for problems where explicit gradients are unavailable and have to be approximated using only queries to function value. The prevalent single-query approach is simple, but suffers from high estimation variance, motivating a multi-query paradigm to improves estimation accuracy. This, however, creates a critical trade-off: under a fixed budget of queries (i.e. cost), queries per iteration and the total number of optimization iterations are inversely proportional to one another. How to best allocate this budget is a fundamental, under-explored question.
  This work systematically resolves this query allocation problem. We analyze two aggregation methods: the de facto simple averaging (ZO-Avg), and a new Projection Alignment method (ZO-Align) we derive from local surrogate minimization. By deriving convergence rates for both methods that make the dependence on the number of queries explicit across strongly convex, convex, non-convex, and stochastic settings, we uncover a stark dichotomy: For ZO-Avg, we prove that using more than one query per iteration is always query-inefficient, rendering the single-query approach optimal. On the contrary, ZO-Align generally performs better with more queries per iteration, resulting in a full-subspace estimation as the optimal approach. Thus, our work clarifies that the multi-query problem boils down to a choice not about an intermediate query size, but between two classic algorithms, a choice dictated entirely by the aggregation method used. These theoretical findings are also consistently validated by extensive experiments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15552v1 발표 유형: 신규  
초록: 영차(zeroth-order, ZO) 최적화는 명시적인 기울기를 사용할 수 없고 함수 값에 대한 쿼리만을 사용하여 근사해야 하는 문제에 강력한 프레임워크를 제공합니다. 일반적인 단일 쿼리 접근법은 간단하지만, 높은 추정 분산으로 인해 추정 정확도를 향상시키기 위한 다중 쿼리 패러다임을 필요로 합니다. 그러나 이는 중요한 트레이드오프를 발생시킵니다: 쿼리의 고정된 예산(즉, 비용) 하에서, 한 번의 반복당 쿼리 수와 최적화 반복의 총 횟수는 서로 반비례합니다. 이 예산을 최적으로 할당하는 방법은 근본적이고 충분히 탐구되지 않은 질문입니다.  
이 연구는 이 쿼리 할당 문제를 체계적으로 해결합니다. 우리는 두 가지 집계 방법을 분석합니다: 사실상 단순 평균화(ZO-Avg)와 지역 대리 최소화를 통해 도출한 새로운 투영 정렬 방법(ZO-Align). 강하게 볼록, 볼록, 비볼록, 확률적 설정 전반에 걸쳐 쿼리 수에 대한 의존성을 명시적으로 만드는 두 방법의 수렴 속도를 도출함으로써, 우리는 뚜렷한 이분법을 발견합니다: ZO-Avg의 경우, 반복당 하나 이상의 쿼리를 사용하는 것은 항상 쿼리 비효율적임을 증명하여 단일 쿼리 접근법이 최적임을 보여줍니다. 반대로, ZO-Align은 일반적으로 반복당 더 많은 쿼리를 사용하여 더 나은 성능을 보이며, 최적의 접근법으로 전체 부분 공간 추정을 초래합니다. 따라서, 우리의 연구는 다중 쿼리 문제가 중간 쿼리 크기에 관한 선택이 아니라, 사용된 집계 방법에 의해 전적으로 결정되는 두 가지 고전적인 알고리즘 중 하나를 선택하는 문제임을 명확히 합니다. 이러한 이론적 발견은 광범위한 실험을 통해 일관되게 검증되었습니다.

## 📝 요약

이 논문은 명시적 기울기가 없는 문제에서 함수 값만을 이용해 근사하는 영차수(Zeroth-order) 최적화의 쿼리 할당 문제를 해결합니다. 기존의 단일 쿼리 방식은 단순하지만 추정 변동성이 높아 다중 쿼리 방식을 통해 정확성을 개선할 수 있습니다. 그러나 고정된 쿼리 예산 하에서 쿼리 수와 최적화 반복 횟수 간의 상충 관계가 발생합니다. 본 연구는 이 문제를 체계적으로 분석하여 두 가지 집계 방법을 비교합니다: 단순 평균(ZO-Avg)과 새로운 투영 정렬 방법(ZO-Align). 강하게 볼록, 볼록, 비볼록, 확률적 설정에서 두 방법의 수렴 속도를 도출하여, ZO-Avg는 단일 쿼리가 최적임을, ZO-Align은 다중 쿼리가 더 효율적임을 밝혔습니다. 이론적 발견은 실험을 통해 검증되었습니다.

## 🎯 주요 포인트

- 1. 영차(zeroth-order) 최적화는 명시적인 기울기가 없는 문제에서 함수 값 쿼리만으로 근사해야 하는 강력한 프레임워크를 제공합니다.

- 2. 단일 쿼리 접근법은 간단하지만 높은 추정 분산 문제를 겪어 다중 쿼리 패러다임이 필요합니다.

- 3. 쿼리 예산 하에서 쿼리 수와 최적화 반복 횟수 간의 상충 관계가 존재하며, 이를 최적으로 할당하는 문제는 중요하지만 충분히 탐구되지 않았습니다.

- 4. ZO-Avg와 ZO-Align 두 가지 집계 방법을 분석하여 쿼리 수에 따른 수렴 속도를 도출하고, 각 방법의 최적 쿼리 수를 제시합니다.

- 5. 실험을 통해 이론적 결과를 검증하며, 집계 방법에 따라 최적의 쿼리 수가 달라진다는 결론을 내립니다.

---

*Generated on 2025-09-22 15:19:41*