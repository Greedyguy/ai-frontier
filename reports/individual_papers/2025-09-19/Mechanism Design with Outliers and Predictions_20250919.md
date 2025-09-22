
# Mechanism Design with Outliers and Predictions

**Korean Title:** 이상치 및 예측을 고려한 메커니즘 설계

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Prediction Enhanced Mechanisms

## 🔗 유사한 논문
- [[Polynomial-Time Approximation Schemes via Utility Alignment Unit-Demand Pricing and More]] (81.1% similar)
- [[Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (80.0% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.1% similar)
- [[Welfare and Cost Aggregation for Multi-Agent Control When to Choose Which Social Cost Function, and Why]] (78.3% similar)
- [[Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09561v2 Announce Type: replace 
Abstract: We initiate the study of mechanism design with outliers, where the designer can discard $z$ agents from the social cost objective. This setting is particularly relevant when some agents exhibit extreme or atypical preferences. As a natural case study, we consider facility location on the line: $n$ strategic agents report their preferred locations, and a mechanism places a facility to minimize a social cost function. In our setting, the $z$ agents farthest from the chosen facility are excluded from the social cost. While it may seem intuitive that discarding outliers improves efficiency, our results reveal that the opposite can hold.
  We derive tight bounds for deterministic strategyproof mechanisms under the two most-studied objectives: utilitarian and egalitarian social cost. Our results offer a comprehensive view of the impact of outliers. We first show that when $z \ge n/2$, no strategyproof mechanism can achieve a bounded approximation for either objective. For egalitarian cost, selecting the $(z + 1)$-th order statistic is strategyproof and 2-approximate. In fact, we show that this is best possible by providing a matching lower bound. Notably, this lower bound of 2 persists even when the mechanism has access to a prediction of the optimal location, in stark contrast to the setting without outliers. For utilitarian cost, we show that strategyproof mechanisms cannot effectively exploit outliers, leading to the counterintuitive outcome that approximation guarantees worsen as the number of outliers increases. However, in this case, access to a prediction allows us to design a strategyproof mechanism achieving the best possible trade-off between consistency and robustness. Finally, we also establish lower bounds for randomized mechanisms that are truthful in expectation.

## 🔍 Abstract (한글 번역)

arXiv:2509.09561v2 발표 유형: 교체  
초록: 우리는 메커니즘 설계에서 이상치(outliers)를 고려한 연구를 시작합니다. 여기서 설계자는 사회적 비용 목표에서 $z$ 에이전트를 제외할 수 있습니다. 이 설정은 일부 에이전트가 극단적이거나 비정형적인 선호를 보일 때 특히 관련이 있습니다. 자연스러운 사례 연구로서, 우리는 직선상의 시설 위치 문제를 고려합니다: $n$명의 전략적 에이전트가 그들의 선호 위치를 보고하고, 메커니즘은 사회적 비용 함수를 최소화하기 위해 시설을 배치합니다. 우리 설정에서는 선택된 시설에서 가장 먼 $z$명의 에이전트가 사회적 비용에서 제외됩니다. 이상치를 제외하면 효율성이 향상될 것이라는 직관이 있을 수 있지만, 우리의 결과는 그 반대가 될 수 있음을 보여줍니다.

우리는 가장 많이 연구된 두 가지 목표, 즉 공리주의적(utilitarian) 및 평등주의적(egalitarian) 사회적 비용에 대해 결정론적 전략적 메커니즘에 대한 엄밀한 경계를 도출합니다. 우리의 결과는 이상치의 영향에 대한 포괄적인 관점을 제공합니다. 먼저, $z \ge n/2$일 때, 어떤 전략적 메커니즘도 두 목표에 대해 유한한 근사치를 달성할 수 없음을 보여줍니다. 평등주의적 비용의 경우, $(z + 1)$번째 순서 통계를 선택하는 것이 전략적으로 증명 가능하며 2-근사적입니다. 사실, 우리는 일치하는 하한을 제공함으로써 이것이 최선의 가능성을 보여줍니다. 특히, 이 하한 2는 메커니즘이 최적 위치에 대한 예측에 접근할 수 있는 경우에도 지속되며, 이는 이상치가 없는 설정과는 현저히 대조적입니다. 공리주의적 비용의 경우, 우리는 전략적 메커니즘이 이상치를 효과적으로 활용할 수 없음을 보여주며, 이상치의 수가 증가함에 따라 근사 보장이 악화되는 역설적인 결과를 초래합니다. 그러나 이 경우, 예측에 대한 접근은 일관성과 강건성 사이의 최상의 균형을 달성하는 전략적 메커니즘을 설계할 수 있게 합니다. 마지막으로, 우리는 기대상 진실한 무작위 메커니즘에 대한 하한도 확립합니다.

## 📝 요약

이 논문은 이상치가 있는 환경에서의 메커니즘 설계를 연구합니다. 특히, 선형 시설 위치 문제를 다루며, 일부 에이전트의 극단적 선호를 고려해 사회적 비용에서 $z$명의 에이전트를 제외할 수 있는 상황을 분석합니다. 연구 결과, 이상치를 제외하는 것이 효율성을 항상 개선하지 않음을 발견했습니다. 결정론적 전략적 메커니즘에 대한 엄밀한 경계를 도출했으며, $z \ge n/2$인 경우 어떤 전략적 메커니즘도 유틸리티적 또는 평등적 사회 비용에 대해 유한한 근사치를 달성할 수 없음을 보였습니다. 평등적 비용에서는 $(z + 1)$번째 순서 통계량을 선택하는 것이 2-근사적이고 최적임을 증명했습니다. 유틸리티적 비용에서는 이상치를 활용하는 것이 오히려 근사 보장을 악화시킬 수 있음을 밝혔고, 예측을 활용한 전략적 메커니즘 설계로 일관성과 견고성의 최적 균형을 달성할 수 있음을 제시했습니다. 마지막으로, 기대치에서 진실한 무작위 메커니즘에 대한 하한도 확립했습니다.

## 🎯 주요 포인트

- 1. 아웃라이어를 제외하는 메커니즘 디자인을 연구하며, 사회적 비용 목표에서 $z$ 에이전트를 제외할 수 있는 설정을 제안합니다.

- 2. 시설 위치 문제에서 아웃라이어를 제외하는 것이 효율성을 높이는 것이 아니라는 역설적인 결과를 발견했습니다.

- 3. 결정론적 전략적 메커니즘에 대해 공리적 및 평등주의적 사회 비용 목표에서의 엄밀한 경계를 도출했습니다.

- 4. 평등주의 비용의 경우, $(z + 1)$번째 순서 통계량을 선택하는 것이 전략적으로 증명 가능하고 2-근사적임을 보였습니다.

- 5. 공리적 비용의 경우, 예측 접근을 통해 일관성과 강건성 간의 최적 균형을 달성하는 전략적 메커니즘을 설계할 수 있음을 보여줍니다.

---

*Generated on 2025-09-19 16:50:40*