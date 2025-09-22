# Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation

**Korean Title:** 게임에서 플레이어별 오목한 결합 제약을 가진 내쉬 균형: 존재성과 계산

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Philip Jordan|Philip Jordan]] [[authors/Maryam Kamgarpour|Maryam Kamgarpour]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Playerwise Concave Constraints

## 🔗 유사한 논문
- [[Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (84.2% similar)
- [[Zero-sum turn games using Q-learning_ finite computation with security guarantees_20250918|Zero-sum turn games using Q-learning finite computation with security guarantees]] (81.2% similar)
- [[Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (80.0% similar)
- [[Polynomial-Time Approximation Schemes via Utility Alignment_ Unit-Demand Pricing and More_20250918|Polynomial-Time Approximation Schemes via Utility Alignment Unit-Demand Pricing and More]] (79.3% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (78.9% similar)

## 📋 저자 정보

**Authors:** Philip Jordan, Maryam Kamgarpour

## 📄 Abstract (원문)

We study the existence and computation of Nash equilibria in continuous
static games where the players' admissible strategies are subject to shared
coupling constraints, i.e., constraints that depend on their \emph{joint}
strategies. Specifically, we focus on a class of games characterized by
playerwise concave utilities and playerwise concave constraints. Prior results
on the existence of Nash equilibria are not applicable to this class, as they
rely on strong assumptions such as joint convexity of the feasible set. By
leveraging topological fixed point theory and novel structural insights into
the contractibility of feasible sets under playerwise concave constraints, we
give an existence proof for Nash equilibria under weaker conditions. Having
established existence, we then focus on the computation of Nash equilibria via
independent gradient methods under the additional assumption that the utilities
admit a potential function. To account for the possibly nonconvex feasible
region, we employ a log barrier regularized gradient ascent with adaptive
stepsizes. Starting from an initial feasible strategy profile and under exact
gradient feedback, the proposed method converges to an $\epsilon$-approximate
constrained Nash equilibrium within $\mathcal{O}(\epsilon^{-3})$ iterations.

## 🔍 Abstract (한글 번역)

우리는 플레이어들의 허용 가능한 전략이 공유된 결합 제약, 즉 그들의 \emph{공동} 전략에 의존하는 제약에 종속되는 연속 정적 게임에서 내시 균형의 존재와 계산을 연구합니다. 구체적으로, 우리는 플레이어별로 오목한 효용과 플레이어별로 오목한 제약 조건으로 특징지어지는 게임의 한 종류에 초점을 맞춥니다. 내시 균형의 존재에 대한 기존 결과는 실현 가능한 집합의 공동 볼록성과 같은 강한 가정에 의존하기 때문에 이 클래스에 적용되지 않습니다. 우리는 위상 고정점 이론과 플레이어별 오목한 제약 조건 하에서 실현 가능한 집합의 수축성에 대한 새로운 구조적 통찰을 활용하여 더 약한 조건 하에서 내시 균형의 존재에 대한 증명을 제공합니다. 존재를 확립한 후, 우리는 효용이 잠재 함수(potential function)를 허용한다는 추가 가정 하에 독립적인 경사 방법을 통해 내시 균형의 계산에 집중합니다. 비볼록 실현 가능 영역을 고려하기 위해, 우리는 적응형 스텝 사이즈를 가진 로그 장벽 정규화 경사 상승법을 사용합니다. 초기의 실현 가능한 전략 프로파일에서 시작하여 정확한 경사 피드백 하에서 제안된 방법은 $\mathcal{O}(\epsilon^{-3})$ 반복 내에 $\epsilon$-근사 제약 내시 균형에 수렴합니다.

## 📝 요약

이 논문은 연속 정적 게임에서 플레이어들의 전략이 공동 제약 조건을 따르는 경우의 내쉬 균형의 존재와 계산을 연구합니다. 기존 연구는 가능한 집합의 공동 볼록성을 가정하지만, 본 연구는 플레이어별 오목한 효용 함수와 제약 조건을 가진 게임에 대해 더 약한 조건 하에서 내쉬 균형의 존재를 증명합니다. 이를 위해 위상 고정점 이론과 새로운 구조적 통찰을 활용했습니다. 또한, 효용 함수가 잠재 함수로 표현될 수 있다는 추가 가정 하에 독립적인 그래디언트 방법을 통해 내쉬 균형을 계산합니다. 비볼록한 가능 영역을 고려하여 로그 배리어 정규화된 그래디언트 상승법을 사용하며, 초기 전략 프로파일에서 시작해 정확한 그래디언트 피드백을 통해 $\mathcal{O}(\epsilon^{-3})$ 반복 내에 $\epsilon$-근사 제약 내쉬 균형에 수렴합니다.

## 🎯 주요 포인트

- 1. 본 연구는 연속적인 정적 게임에서 공유 결합 제약 조건 하의 내쉬 균형의 존재와 계산을 다룹니다.

- 2. 기존의 내쉬 균형 존재성 결과는 강한 가정에 의존하여 본 연구의 게임 클래스에는 적용되지 않습니다.

- 3. 플레이어별 오목한 제약 조건 하에서의 수축 가능성에 대한 구조적 통찰을 통해 내쉬 균형의 존재를 증명합니다.

- 4. 효용 함수가 잠재 함수로 표현될 수 있다는 추가 가정 하에 독립적인 그래디언트 방법을 사용하여 내쉬 균형을 계산합니다.

- 5. 제안된 방법은 초기 전략 프로파일에서 시작하여 $\mathcal{O}(\epsilon^{-3})$ 반복 내에 $\epsilon$-근사 제한 내쉬 균형으로 수렴합니다.

---

*Generated on 2025-09-20 09:15:51*