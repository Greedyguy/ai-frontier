---
keywords:
  - Differentiable Intersectional Fairness Metrics
  - Intersectional Fairness
  - Pareto-Optimal Solutions
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:02:20.888365",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Differentiable Intersectional Fairness Metrics",
    "Intersectional Fairness",
    "Pareto-Optimal Solutions"
  ],
  "rejected_keywords": [
    "Multi-Objective Optimization"
  ],
  "similarity_scores": {
    "Differentiable Intersectional Fairness Metrics": 0.82,
    "Intersectional Fairness": 0.78,
    "Pareto-Optimal Solutions": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness

**Korean Title:** APFEx: 교차적 공정성을 위한 적응형 파레토 전선 탐색기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Pareto-Optimal Solutions|Pareto-optimal solutions]]
**⚡ Unique Technical**: [[keywords/Differentiable Intersectional Fairness Metrics|differentiable intersectional fairness metrics]], [[keywords/Intersectional Fairness|intersectional fairness]]

## 🔗 유사한 논문
- [[CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre Scalable and Effective Data Pre-processing for Causal Fairness]] (82.8% similar)
- [[Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community Guiding the Fairness of Graphs via New Links]] (80.0% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (78.7% similar)
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (78.3% similar)
- [[CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (78.3% similar)

## 📋 저자 정보

**Authors:** Priyobrata Mondal, Faizanuddin Ansari, Swagatam Das

## 📄 Abstract (원문)

Ensuring fairness in machine learning models is critical, especially when
biases compound across intersecting protected attributes like race, gender, and
age. While existing methods address fairness for single attributes, they fail
to capture the nuanced, multiplicative biases faced by intersectional
subgroups. We introduce Adaptive Pareto Front Explorer (APFEx), the first
framework to explicitly model intersectional fairness as a joint optimization
problem over the Cartesian product of sensitive attributes. APFEx combines
three key innovations- (1) an adaptive multi-objective optimizer that
dynamically switches between Pareto cone projection, gradient weighting, and
exploration strategies to navigate fairness-accuracy trade-offs, (2)
differentiable intersectional fairness metrics enabling gradient-based
optimization of non-smooth subgroup disparities, and (3) theoretical guarantees
of convergence to Pareto-optimal solutions. Experiments on four real-world
datasets demonstrate APFEx's superiority, reducing fairness violations while
maintaining competitive accuracy. Our work bridges a critical gap in fair ML,
providing a scalable, model-agnostic solution for intersectional fairness.

## 🔍 Abstract (한글 번역)

기계 학습 모델에서 공정성을 보장하는 것은 매우 중요합니다. 특히 인종, 성별, 나이와 같은 교차 보호 속성에서 편향이 복합적으로 발생할 때 더욱 그렇습니다. 기존의 방법들은 단일 속성에 대한 공정성을 다루지만, 교차 하위 그룹이 직면하는 미묘하고 복합적인 편향을 포착하지 못합니다. 우리는 민감한 속성의 데카르트 곱에 대한 공동 최적화 문제로 교차 공정성을 명시적으로 모델링하는 최초의 프레임워크인 Adaptive Pareto Front Explorer (APFEx)를 소개합니다. APFEx는 세 가지 주요 혁신을 결합합니다. (1) 공정성과 정확성 간의 균형을 탐색하기 위해 파레토 콘 투영, 그래디언트 가중치, 탐색 전략 간에 동적으로 전환하는 적응형 다중 목표 최적화기, (2) 비매끄러운 하위 그룹 격차의 그래디언트 기반 최적화를 가능하게 하는 미분 가능한 교차 공정성 지표, (3) 파레토 최적 솔루션으로의 수렴에 대한 이론적 보장. 네 개의 실제 데이터셋에 대한 실험은 APFEx의 우수성을 입증하며, 공정성 위반을 줄이면서도 경쟁력 있는 정확성을 유지합니다. 우리의 연구는 공정한 기계 학습에서 중요한 격차를 해소하며, 교차 공정성을 위한 확장 가능하고 모델에 구애받지 않는 솔루션을 제공합니다.

## 📝 요약

이 논문은 기계 학습 모델에서 교차하는 보호 속성(예: 인종, 성별, 나이) 간의 편향을 해결하기 위해 APFEx라는 새로운 프레임워크를 제안합니다. APFEx는 민감한 속성의 데카르트 곱을 통해 교차적 공정성을 공동 최적화 문제로 모델링하며, 적응형 다목적 최적화 기법을 사용하여 공정성과 정확성 간의 균형을 조절합니다. 또한, 미분 가능한 교차적 공정성 지표를 통해 비매끄러운 하위 그룹 불균형을 최적화하며, 이론적으로 파레토 최적 솔루션에 수렴함을 보장합니다. 실험 결과, APFEx는 공정성 위반을 줄이면서도 높은 정확성을 유지하여 기존 방법보다 우수한 성능을 보였습니다. 이 연구는 공정한 기계 학습에서 중요한 격차를 메우며, 교차적 공정성을 위한 확장 가능하고 모델에 구애받지 않는 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 기계 학습 모델에서 인종, 성별, 나이와 같은 교차 보호 속성에 대한 공정성을 보장하는 것이 중요합니다.

- 2. 기존 방법들은 단일 속성에 대한 공정성을 다루지만, 교차 하위 그룹이 직면하는 복합적 편향을 포착하지 못합니다.

- 3. APFEx는 민감한 속성의 데카르트 곱에 대한 공동 최적화 문제로 교차 공정성을 명시적으로 모델링하는 최초의 프레임워크입니다.

- 4. APFEx는 적응형 다중 목표 최적화, 미분 가능한 교차 공정성 지표, 파레토 최적 솔루션으로의 수렴에 대한 이론적 보장을 결합합니다.

- 5. 네 가지 실제 데이터셋에 대한 실험에서 APFEx는 공정성 위반을 줄이면서 경쟁력 있는 정확성을 유지하는 우수성을 입증했습니다.

---

*Generated on 2025-09-20 09:24:32*