
# Optimal Algorithms for Bandit Learning in Matching Markets

**Korean Title:** 매칭 시장에서의 밴딧 학습을 위한 최적 알고리즘

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Two-sided Learning

## 🔗 유사한 논문
- [[Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (82.1% similar)
- [[Graph Feedback Bandits on Similar Arms With and Without Graph Structures]] (81.4% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.9% similar)
- [[Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (79.0% similar)
- [[Polynomial-Time Approximation Schemes via Utility Alignment Unit-Demand Pricing and More]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14466v1 Announce Type: cross 
Abstract: We study the problem of pure exploration in matching markets under uncertain preferences, where the goal is to identify a stable matching with confidence parameter $\delta$ and minimal sample complexity. Agents learn preferences via stochastic rewards, with expected values indicating preferences. This finds use in labor market platforms like Upwork, where firms and freelancers must be matched quickly despite noisy observations and no prior knowledge, in a stable manner that prevents dissatisfaction. We consider markets with unique stable matching and establish information-theoretic lower bounds on sample complexity for (1) one-sided learning, where one side of the market knows its true preferences, and (2) two-sided learning, where both sides are uncertain. We propose a computationally efficient algorithm and prove that it asymptotically ($\delta\to 0$) matches the lower bound to a constant for one-sided learning. Using the insights from the lower bound, we extend our algorithm to the two-sided learning setting and provide experimental results showing that it closely matches the lower bound on sample complexity. Finally, using a system of ODEs, we characterize the idealized fluid path that our algorithm chases.

## 🔍 Abstract (한글 번역)

arXiv:2509.14466v1 발표 유형: 교차  
초록: 우리는 불확실한 선호도 하에서 매칭 시장에서의 순수 탐색 문제를 연구하며, 목표는 신뢰 매개변수 $\delta$와 최소 샘플 복잡성을 가진 안정적인 매칭을 식별하는 것입니다. 에이전트는 확률적 보상을 통해 선호도를 학습하며, 기대값이 선호도를 나타냅니다. 이는 Upwork와 같은 노동 시장 플랫폼에서 유용하며, 기업과 프리랜서가 소음이 있는 관측과 사전 지식 없이도 불만을 방지하는 안정적인 방식으로 신속하게 매칭되어야 합니다. 우리는 고유한 안정적 매칭을 가진 시장을 고려하고, (1) 시장의 한쪽이 자신의 실제 선호도를 알고 있는 경우의 단측 학습과 (2) 양쪽 모두가 불확실한 경우의 양측 학습에 대한 샘플 복잡성의 정보 이론적 하한을 확립합니다. 우리는 계산적으로 효율적인 알고리즘을 제안하고, 단측 학습의 경우 점근적으로 ($\delta\to 0$) 상수에 대해 하한과 일치함을 증명합니다. 하한에서 얻은 통찰력을 사용하여, 우리는 양측 학습 설정으로 알고리즘을 확장하고, 샘플 복잡성의 하한에 근접하게 일치함을 보여주는 실험 결과를 제공합니다. 마지막으로, ODE 시스템을 사용하여 알고리즘이 추적하는 이상적인 유체 경로를 특성화합니다.

## 📝 요약

이 논문은 불확실한 선호도 하에서 매칭 시장의 순수 탐색 문제를 다룹니다. 목표는 최소한의 샘플 복잡도로 안정적인 매칭을 식별하는 것입니다. 노동 시장 플랫폼에서 유용하며, 정보 이론적 하한을 설정하여 한쪽 또는 양쪽 모두 선호도를 모르는 경우에 대한 샘플 복잡도를 분석합니다. 제안된 알고리즘은 계산 효율적이며, 한쪽 학습에서는 하한에 근접하고, 양쪽 학습으로 확장하여 실험 결과 하한에 근접함을 보입니다. ODE 시스템을 통해 알고리즘이 추적하는 이상적인 경로를 설명합니다.

## 🎯 주요 포인트

- 1. 불확실한 선호도 하에서 안정적인 매칭을 식별하는 문제를 연구하며, 목표는 최소 샘플 복잡도로 안정적인 매칭을 식별하는 것입니다.

- 2. 정보 이론적 하한을 설정하여 한쪽 학습과 양쪽 학습의 샘플 복잡도를 분석했습니다.

- 3. 한쪽 학습의 경우, 제안된 알고리즘이 계산적으로 효율적이며 하한에 비해 점근적으로 일치함을 증명했습니다.

- 4. 양쪽 학습 설정으로 알고리즘을 확장하고, 실험 결과를 통해 샘플 복잡도의 하한에 가깝게 일치함을 보였습니다.

- 5. ODE 시스템을 사용하여 알고리즘이 추적하는 이상적인 유체 경로를 특성화했습니다.

---

*Generated on 2025-09-19 16:45:33*