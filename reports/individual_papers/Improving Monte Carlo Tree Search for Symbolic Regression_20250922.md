# Improving Monte Carlo Tree Search for Symbolic Regression

**Korean Title:** 심볼릭 회귀를 위한 몬테카를로 트리 탐색 개선

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: State-jumping Actions

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (81.5% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (79.7% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (79.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.6% similar)
- [[2025-09-22/Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering_20250922|Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15929v1 Announce Type: new 
Abstract: Symbolic regression aims to discover concise, interpretable mathematical expressions that satisfy desired objectives, such as fitting data, posing a highly combinatorial optimization problem. While genetic programming has been the dominant approach, recent efforts have explored reinforcement learning methods for improving search efficiency. Monte Carlo Tree Search (MCTS), with its ability to balance exploration and exploitation through guided search, has emerged as a promising technique for symbolic expression discovery. However, its traditional bandit strategies and sequential symbol construction often limit performance. In this work, we propose an improved MCTS framework for symbolic regression that addresses these limitations through two key innovations: (1) an extreme bandit allocation strategy tailored for identifying globally optimal expressions, with finite-time performance guarantees under polynomial reward decay assumptions; and (2) evolution-inspired state-jumping actions such as mutation and crossover, which enable non-local transitions to promising regions of the search space. These state-jumping actions also reshape the reward landscape during the search process, improving both robustness and efficiency. We conduct a thorough numerical study to the impact of these improvements and benchmark our approach against existing symbolic regression methods on a variety of datasets, including both ground-truth and black-box datasets. Our approach achieves competitive performance with state-of-the-art libraries in terms of recovery rate, attains favorable positions on the Pareto frontier of accuracy versus model complexity. Code is available at https://github.com/PKU-CMEGroup/MCTS-4-SR.

## 🔍 Abstract (한글 번역)

arXiv:2509.15929v1 발표 유형: 신규  
초록: 심볼릭 회귀는 데이터 적합과 같은 원하는 목표를 만족하는 간결하고 해석 가능한 수학적 표현을 발견하는 것을 목표로 하며, 이는 매우 조합적인 최적화 문제를 제기합니다. 유전 프로그래밍이 지배적인 접근 방식이었지만, 최근에는 검색 효율성을 향상시키기 위한 강화 학습 방법이 탐구되고 있습니다. 탐색을 안내하여 탐색과 활용의 균형을 맞출 수 있는 몬테카를로 트리 탐색(MCTS)은 심볼릭 표현 발견을 위한 유망한 기법으로 부상하고 있습니다. 그러나 전통적인 밴딧 전략과 순차적 심볼 구성은 종종 성능을 제한합니다. 본 연구에서는 이러한 한계를 해결하기 위해 두 가지 주요 혁신을 통해 심볼릭 회귀를 위한 개선된 MCTS 프레임워크를 제안합니다: (1) 다항 보상 감소 가정 하에서 유한 시간 성능 보장을 갖는 전역 최적 표현 식별을 위한 극단적 밴딧 할당 전략; (2) 탐색 공간의 유망한 영역으로 비국소적 전이를 가능하게 하는 돌연변이 및 교차와 같은 진화 영감을 받은 상태 점프 동작. 이러한 상태 점프 동작은 검색 과정에서 보상 지형을 재구성하여 강건성과 효율성을 모두 향상시킵니다. 우리는 이러한 개선의 영향을 철저히 수치적으로 연구하고, 다양한 데이터셋(기준 데이터셋 및 블랙박스 데이터셋 포함)에서 기존 심볼릭 회귀 방법과 우리의 접근 방식을 비교 평가합니다. 우리의 접근 방식은 복구율 측면에서 최첨단 라이브러리와 경쟁력 있는 성능을 달성하고, 정확도 대 모델 복잡성의 파레토 전선에서 유리한 위치를 차지합니다. 코드는 https://github.com/PKU-CMEGroup/MCTS-4-SR에서 사용할 수 있습니다.

## 📝 요약

이 논문은 심볼릭 회귀 문제에서 효율적인 수식을 발견하기 위해 개선된 몬테카를로 트리 탐색(MCTS) 기법을 제안합니다. 기존의 유전 프로그래밍 대신 강화 학습을 활용하여 탐색 효율성을 높이고자 하며, 두 가지 주요 혁신을 도입합니다. 첫째, 전역 최적 수식을 찾기 위한 극단적 밴딧 할당 전략을 통해 성능을 개선합니다. 둘째, 진화적 영감을 받은 상태 점프 행동(변이와 교차)을 도입하여 탐색 공간의 유망한 영역으로 비지역적 전이를 가능하게 합니다. 이를 통해 탐색 과정에서 보상 지형을 재구성하여 강건성과 효율성을 향상시킵니다. 다양한 데이터셋에서 기존 방법들과 비교한 결과, 본 접근법은 높은 회복률과 정확도 대비 모델 복잡성의 파레토 전선에서 유리한 위치를 차지합니다.

## 🎯 주요 포인트

- 1. 심볼릭 회귀 문제에서 기존의 유전 프로그래밍 대신 강화 학습 방법이 탐색 효율성을 개선하는 데 주목받고 있다.

- 2. 몬테카를로 트리 탐색(MCTS)은 탐색과 활용의 균형을 통해 심볼릭 표현 발견에 유망한 기술로 부상하고 있다.

- 3. 본 연구는 전통적인 MCTS의 성능 한계를 극복하기 위해 극단적인 밴딧 할당 전략과 진화 영감을 받은 상태 점프 동작을 도입한 개선된 MCTS 프레임워크를 제안한다.

- 4. 제안된 방법은 다양한 데이터셋에서 기존의 심볼릭 회귀 방법과 비교하여 경쟁력 있는 성능을 보이며, 정확도와 모델 복잡성의 파레토 전선에서 유리한 위치를 차지한다.

- 5. 연구 결과는 코드와 함께 https://github.com/PKU-CMEGroup/MCTS-4-SR에서 제공된다.

---

*Generated on 2025-09-22 15:27:29*