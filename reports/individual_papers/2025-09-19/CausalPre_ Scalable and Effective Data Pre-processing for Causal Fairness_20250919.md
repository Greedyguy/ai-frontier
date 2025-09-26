---
keywords:
  - Causal Fairness
  - Marginal Factorization
  - Distribution Estimation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15199
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:53:29.666542",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Causal Fairness",
    "Marginal Factorization",
    "Distribution Estimation"
  ],
  "rejected_keywords": [
    "Data Pre-processing"
  ],
  "similarity_scores": {
    "Causal Fairness": 0.78,
    "Marginal Factorization": 0.75,
    "Distribution Estimation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness

**Korean Title:** CausalPre: 인과적 공정성을 위한 확장 가능하고 효과적인 데이터 전처리

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Distribution Estimation|distribution estimation]]
**⚡ Unique Technical**: [[keywords/Causal Fairness|causal fairness]], [[keywords/Marginal Factorization|marginal factorization]]

## 🔗 유사한 논문
- [[Causal Clustering for Conditional Average Treatment Effects Estimation and Subgroup Discovery]] (79.3% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (77.6% similar)
- [[DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (77.6% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.5% similar)
- [[BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (77.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15199v1 Announce Type: new 
Abstract: Causal fairness in databases is crucial to preventing biased and inaccurate outcomes in downstream tasks. While most prior work assumes a known causal model, recent efforts relax this assumption by enforcing additional constraints. However, these approaches often fail to capture broader attribute relationships that are critical to maintaining utility. This raises a fundamental question: Can we harness the benefits of causal reasoning to design efficient and effective fairness solutions without relying on strong assumptions about the underlying causal model? In this paper, we seek to answer this question by introducing CausalPre, a scalable and effective causality-guided data pre-processing framework that guarantees justifiable fairness, a strong causal notion of fairness. CausalPre extracts causally fair relationships by reformulating the originally complex and computationally infeasible extraction task into a tailored distribution estimation problem. To ensure scalability, CausalPre adopts a carefully crafted variant of low-dimensional marginal factorization to approximate the joint distribution, complemented by a heuristic algorithm that efficiently tackles the associated computational challenge. Extensive experiments on benchmark datasets demonstrate that CausalPre is both effective and scalable, challenging the conventional belief that achieving causal fairness requires trading off relationship coverage for relaxed model assumptions.

## 🔍 Abstract (한글 번역)

arXiv:2509.15199v1 발표 유형: 신규  
초록: 데이터베이스에서의 인과적 공정성은 편향되고 부정확한 결과를 방지하기 위해 필수적입니다. 대부분의 이전 연구는 알려진 인과 모델을 가정하지만, 최근의 노력은 추가적인 제약을 부과하여 이 가정을 완화하고 있습니다. 그러나 이러한 접근법은 유용성을 유지하는 데 중요한 더 넓은 속성 관계를 포착하지 못하는 경우가 많습니다. 이는 근본적인 질문을 제기합니다: 기본 인과 모델에 대한 강한 가정에 의존하지 않고 인과 추론의 이점을 활용하여 효율적이고 효과적인 공정성 솔루션을 설계할 수 있을까요? 이 논문에서는 이 질문에 답하기 위해 CausalPre를 소개합니다. CausalPre는 정당한 공정성을 보장하는 확장 가능하고 효과적인 인과성 안내 데이터 전처리 프레임워크로, 강력한 인과적 공정성 개념을 제공합니다. CausalPre는 원래 복잡하고 계산적으로 실행 불가능한 추출 작업을 맞춤형 분포 추정 문제로 재구성하여 인과적으로 공정한 관계를 추출합니다. 확장성을 보장하기 위해, CausalPre는 결합 분포를 근사하기 위해 저차원 주변 분해의 신중하게 설계된 변형을 채택하고, 관련된 계산적 과제를 효율적으로 해결하는 휴리스틱 알고리즘을 보완합니다. 벤치마크 데이터셋에 대한 광범위한 실험은 CausalPre가 효과적이고 확장 가능하다는 것을 보여주며, 인과적 공정성을 달성하기 위해 관계 범위를 희생해야 한다는 기존의 믿음에 도전합니다.

## 📝 요약

이 논문은 데이터베이스에서 인과적 공정성을 확보하기 위한 새로운 접근법을 제안합니다. 기존 연구들은 주로 알려진 인과 모델을 가정하지만, 이 연구는 강한 인과 모델 가정 없이도 공정성을 달성할 수 있는 방법을 모색합니다. 이를 위해 CausalPre라는 데이터 전처리 프레임워크를 도입하여, 복잡한 인과 관계 추출 문제를 분포 추정 문제로 재구성합니다. CausalPre는 저차원 주변 분해와 휴리스틱 알고리즘을 활용하여 효율적이고 확장 가능한 방식으로 인과적 공정성을 보장합니다. 실험 결과, CausalPre는 기존의 인과 공정성 접근법이 가진 한계를 극복하며, 공정성과 효율성을 동시에 달성할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 데이터베이스에서 인과적 공정성은 편향되고 부정확한 결과를 방지하는 데 중요합니다.

- 2. 기존 연구는 알려진 인과 모델을 가정하지만, 최근 연구는 추가 제약을 통해 이 가정을 완화하려고 합니다.

- 3. CausalPre는 강력한 인과적 공정성을 보장하는 확장 가능하고 효과적인 데이터 전처리 프레임워크입니다.

- 4. CausalPre는 복잡한 추출 작업을 맞춤형 분포 추정 문제로 재구성하여 인과적으로 공정한 관계를 추출합니다.

- 5. CausalPre는 벤치마크 데이터셋 실험에서 효과적이고 확장 가능함을 입증하여, 인과적 공정성을 달성하기 위해 관계 커버리지를 희생해야 한다는 기존 믿음에 도전합니다.

---

*Generated on 2025-09-19 15:33:00*