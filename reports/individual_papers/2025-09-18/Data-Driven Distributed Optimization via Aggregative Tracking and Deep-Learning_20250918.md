
# Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning

**Korean Title:** 데이터 기반 분산 최적화를 위한 집계 추적 및 딥 러닝을 통한 방법Maintain the academic tone and technical terminology appropriately.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Data-Driven Optimization

## 🔗 유사한 논문
- [[Distributionally_Robust_Equilibria_over_the_Wasserstein_Distance_for_Generalized_Nash_Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (81.8% similar)
- [[Privacy-Preserving Uncertainty Disclosure for Facilitating Enhanced Energy Storage Dispatch]] (81.4% similar)
- [[Polynomial-Time_Approximation_Schemes_via_Utility_Alignment_Unit-Demand_Pricing_and_More_20250918|Polynomial-Time Approximation Schemes via Utility Alignment: Unit-Demand Pricing and More]] (80.1% similar)
- [[Welfare and Cost Aggregation for Multi-Agent Control: When to Choose Which Social Cost Function, and Why?]] (79.9% similar)
- [[Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04668v2 Announce Type: replace-cross 
Abstract: In this paper, we propose a novel distributed data-driven optimization scheme. In detail, we focus on the so-called aggregative framework, a scenario in which a set of agents aim to cooperatively minimize the sum of local costs, each depending on both local decision variables and an aggregation of all of them. We consider a data-driven setup where each objective function is unknown and can be sampled at a single point per iteration (thanks to, e.g., feedback from users or sensors). We address this scenario through a distributed algorithm combining three components: (i) a learning part leveraging neural networks to learn the local costs descent direction, (ii) an optimization routine steering the estimates according to the learned direction to minimize the global cost, and (iii) a tracking mechanism locally reconstructing the unavailable global quantities. Using tools from system theory, i.e., timescale separation and averaging theory, we formally prove that in strongly convex setups, the distributed scheme linearly converges to a neighborhood of the optimum, whose radius depends on the accuracy of the neural networks. Finally, numerical simulations validate the theoretical results.

## 🔍 Abstract (한글 번역)

arXiv:2503.04668v2 공지 유형: 교체-교차
요약: 본 논문에서는 새로운 분산 데이터 주도 최적화 방법을 제안한다. 구체적으로, 우리는 집합이 협력하여 지역 비용의 합을 최소화하려고 하는 상황인 집합적 프레임워크에 초점을 맞춘다. 각각의 지역 의사결정 변수와 그들 모두의 집합에 의존하는 지역 비용에 대해 고려한다. 우리는 각 목적 함수가 알려지지 않고 반복당 한 지점에서 샘플링될 수 있는 데이터 주도 설정을 고려한다 (예: 사용자 또는 센서로부터의 피드백을 통해). 우리는 세 가지 구성 요소를 결합한 분산 알고리즘을 통해 이 상황을 다룬다: (i) 지역 비용 하강 방향을 학습하기 위해 신경망을 활용하는 학습 부분, (ii) 학습된 방향에 따라 추정치를 조정하여 전역 비용을 최소화하는 최적화 루틴, 그리고 (iii) 사용할 수 없는 전역 양을 지역적으로 재구성하는 추적 메커니즘. 시스템 이론의 도구를 사용하여, 즉 시간 척도 분리 및 평균 이론을 사용하여, 우리는 강하게 볼록한 설정에서 분산 방식이 최적점의 근처로 선형 수렴함을 형식적으로 증명한다. 마지막으로, 수치 시뮬레이션을 통해 이론적 결과를 검증한다.

## 📝 요약

본 논문에서는 새로운 분산 데이터 주도 최적화 방법론을 제안한다. 본 연구는 집합적 프레임워크에 초점을 맞추며, 일련의 에이전트들이 협력하여 지역 비용의 합을 최소화하는 시나리오를 다룬다. 각각의 지역 의사결정 변수와 그들의 집합을 집계한 것에 따라 지역 비용이 달라지는 상황이다. 우리는 각 목적 함수가 미지수이며 한 번의 반복당 하나의 지점에서 샘플링될 수 있는 데이터 주도 설정을 고려한다. 우리는 신경망을 활용하여 지역 비용 하강 방향을 학습하는 학습 부분, 학습된 방향에 따라 추정치를 조정하여 전역 비용을 최소화하는 최적화 루틴, 그리고 사용할 수 없는 전역 양을 지역적으로 재구성하는 추적 메커니즘을 결합한 분산 알고리즘을 제안한다. 강하게 볼록한 설정에서, 분산 방법론이 최적점 근처로 선형 수렴함을 공식적으로 증명하며, 이때 최적점의 반경은 신경망의 정확도에 따라 결정된다. 최종적으로, 수치 시뮬레이션은 이론적 결과를 검증한다.

## 🎯 주요 포인트

- 1. 분산 데이터 기반 최적화 방법 제안

- 2. 각 에이전트가 협력적으로 지역 비용의 합을 최소화하는 시나리오에 초점

- 3. 신경망을 활용하여 지역 비용 하강 방향을 학습하고 전역 비용을 최소화하는 최적화 루틴을 결합하는 분산 알고리즘 제안

- 4. 강하게 볼록한 설정에서 분산 방법이 최적점 주변으로 선형 수렴함을 이론적으로 증명

- 5. 수치 시뮬레이션을 통해 이론적 결과를 검증함.

---

*Generated on 2025-09-18 17:26:18*