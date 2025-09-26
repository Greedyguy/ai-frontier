---
keywords:
  - Wasserstein Distance
  - Mixed-Integer Nonlinear Programming
  - Generalized Nash Equilibrium Problem
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13985
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:32:33.838329",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Wasserstein Distance",
    "Mixed-Integer Nonlinear Programming",
    "Generalized Nash Equilibrium Problem"
  ],
  "rejected_keywords": [
    "Distributionally Robust Chance Constraints"
  ],
  "similarity_scores": {
    "Wasserstein Distance": 0.8,
    "Mixed-Integer Nonlinear Programming": 0.77,
    "Generalized Nash Equilibrium Problem": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game

**Korean Title:** 일반화된 내쉬 게임에서 와서스타인 거리를 통한 분포적으로 견고한 평형유지

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Mixed-Integer Nonlinear Programming|Mixed-Integer Nonlinear Programming]]
**🔗 Specific Connectable**: [[keywords/Wasserstein Distance|Wasserstein Distance]]
**⚡ Unique Technical**: [[keywords/Generalized Nash Equilibrium Problem|Generalized Nash Equilibrium Problem]]

## 🔗 유사한 논문
- [[Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation]] (84.6% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.8% similar)
- [[Polynomial-Time_Approximation_Schemes_via_Utility_Alignment_Unit-Demand_Pricing_and_More_20250918|Polynomial-Time Approximation Schemes via Utility Alignment: Unit-Demand Pricing and More]] (80.6% similar)
- [[Privacy-Preserving Uncertainty Disclosure for Facilitating Enhanced Energy Storage Dispatch]] (80.0% similar)
- [[Efficient Last-Iterate Convergence in Regret Minimization via Adaptive Reward Transformation]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13985v1 Announce Type: new 
Abstract: Generalized Nash equilibrium problem (GNEP) is fundamental for practical applications where multiple self-interested agents work together to make optimal decisions. In this work, we study GNEP with shared distributionally robust chance constraints (DRCCs) for incorporating inevitable uncertainties. The DRCCs are defined over the Wasserstein ball, which can be explicitly characterized even with limited sample data. To determine the equilibrium of the GNEP, we propose an exact approach to transform the original computationally intractable problem into a deterministic formulation using the Nikaido-Isoda function. Specifically, we show that when all agents' objectives are quadratic in their respective variables, the equilibrium can be obtained by solving a typical mixed-integer nonlinear programming (MINLP) problem, where the integer and continuous variables are decoupled in both the objective function and the constraints. This structure significantly improves computational tractability, as demonstrated through a case study on the charging station pricing problem.

## 🔍 Abstract (한글 번역)

arXiv:2509.13985v1 발표 유형: 새로운
요약: 일반화된 나시 균형 문제(GNEP)는 여러 이해관계를 가진 에이전트들이 최적의 결정을 내리기 위해 함께 일하는 실제 응용 프로그램에 기본적입니다. 본 연구에서는 불가피한 불확실성을 포함하기 위해 공유된 분포적으로 견고한 확률 제약 조건(DRCCs)을 갖는 GNEP를 연구합니다. DRCCs는 워서스타인 볼 위에 정의되어 있으며, 제한된 샘플 데이터로도 명확하게 특성화할 수 있습니다. GNEP의 균형을 결정하기 위해, 우리는 니카이도-이소다 함수를 사용하여 원래의 계산적으로 해결하기 어려운 문제를 결정론적 형태로 변환하는 정확한 방법을 제안합니다. 특히, 모든 에이전트의 목표가 각각의 변수에 대해 이차적인 경우, 균형은 정수 및 연속 변수가 목적 함수 및 제약 조건 모두에서 분리되는 전형적인 혼합 정수 비선형 프로그래밍(MINLP) 문제를 해결함으로써 얻을 수 있음을 보여줍니다. 이 구조는 충전소 가격 문제에 대한 사례 연구를 통해 시연된 바와 같이 계산적으로 다루기 쉽도록 크게 개선됩니다.

## 📝 요약

본 연구는 다수의 이해관계자가 최적의 결정을 내리기 위해 협력하는 실제 응용 프로그램에서 기본적인 일반화된 내쉬 균형 문제(GNEP)를 다룬다. 불가피한 불확실성을 포함하기 위해 공유된 분포적으로 견고한 찬스 제약 조건(DRCCs)을 사용한다. DRCCs는 워세스타인 볼 위에 정의되며, 제한된 샘플 데이터로도 명확하게 특성화될 수 있다. GNEP의 균형을 결정하기 위해, 우리는 Nikaido-Isoda 함수를 사용하여 원래의 계산적으로 해결하기 어려운 문제를 결정론적 공식으로 변환하는 정확한 방법을 제안한다. 특히, 모든 에이전트의 목적이 각각의 변수에 대해 이차적인 경우, 균형은 전형적인 혼합정수 비선형 프로그래밍(MINLP) 문제를 풀어 얻을 수 있으며, 여기서 정수 및 연속 변수는 목적 함수와 제약 조건 모두에서 분리된다. 이 구조는 계산적으로 다루기 쉽게 개선되었으며, 충전소 가격 문제에 대한 사례 연구를 통해 시연되었다.

## 🎯 주요 포인트

- 본 연구에서는 불가피한 불확실성을 포함하기 위해 공유 분포적으로 견고한 확률 제약 조건(DRCCs)을 사용한 일반화된 나시 균형 문제(GNEP)를 연구하였다.

- GNEP의 균형을 결정하기 위해 Nikaido-Isoda 함수를 사용하여 원래의 계산적으로 해결하기 어려운 문제를 결정론적 형태로 변환하는 정확한 방법을 제안하였다.

- 모든 에이전트의 목적이 각각의 변수에 대해 이차적인 경우, 균형은 전형적인 혼합정수 비선형 프로그래밍(MINLP) 문제를 풀어 얻을 수 있음을 보여주었다.

---

*Generated on 2025-09-18 17:24:42*