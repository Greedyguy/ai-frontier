# Geometric Integration for Neural Control Variates

**Korean Title:** 신경 제어 변수를 위한 기하학적 적분

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Neural Control Variates, Multilayered Perceptron

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.1% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (80.3% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (80.1% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (79.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15538v1 Announce Type: cross 
Abstract: Control variates are a variance-reduction technique for Monte Carlo integration. The principle involves approximating the integrand by a function that can be analytically integrated, and integrating using the Monte Carlo method only the residual difference between the integrand and the approximation, to obtain an unbiased estimate. Neural networks are universal approximators that could potentially be used as a control variate. However, the challenge lies in the analytic integration, which is not possible in general. In this manuscript, we study one of the simplest neural network models, the multilayered perceptron (MLP) with continuous piecewise linear activation functions, and its possible analytic integration. We propose an integration method based on integration domain subdivision, employing techniques from computational geometry to solve this problem in 2D. We demonstrate that an MLP can be used as a control variate in combination with our integration method, showing applications in the light transport simulation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15538v1 발표 유형: 교차  
초록: 제어 변수는 몬테카를로 적분의 분산 감소 기법입니다. 이 원리는 적분할 함수를 분석적으로 적분할 수 있는 함수로 근사하고, 몬테카를로 방법을 사용하여 적분할 함수와 근사치 간의 잔차 차이만 적분하여 편향 없는 추정치를 얻는 것입니다. 신경망은 보편적인 근사 도구로서 제어 변수로 사용될 가능성이 있습니다. 그러나 일반적으로 분석적 적분이 불가능하다는 점에서 도전 과제가 있습니다. 이 논문에서는 가장 간단한 신경망 모델 중 하나인 다층 퍼셉트론(MLP)과 연속적인 조각별 선형 활성화 함수를 사용하여 가능한 분석적 적분을 연구합니다. 우리는 2D에서 이 문제를 해결하기 위해 계산 기하학의 기법을 활용하여 적분 영역 분할에 기반한 적분 방법을 제안합니다. 우리는 MLP가 우리의 적분 방법과 결합하여 제어 변수로 사용될 수 있음을 입증하고, 이를 광전달 시뮬레이션에 응용하는 사례를 보여줍니다.

## 📝 요약

이 논문은 몬테카를로 적분의 분산 감소 기법인 제어 변수에 대해 다룹니다. 신경망을 제어 변수로 활용할 가능성을 탐구하며, 특히 다층 퍼셉트론(MLP) 모델과 연속적 조각별 선형 활성화 함수의 분석적 적분 가능성을 연구합니다. 저자들은 2D에서 계산 기하학 기법을 사용하여 적분 영역을 세분화하는 방법을 제안하고, 이를 통해 MLP가 제어 변수로 활용될 수 있음을 보입니다. 이 방법은 특히 광 전송 시뮬레이션에 응용될 수 있음을 시연합니다.

## 🎯 주요 포인트

- 1. 제어 변량은 몬테카를로 적분의 분산 감소 기법으로, 적분 함수를 분석적으로 적분 가능한 함수로 근사하여 잔차만 몬테카를로 방법으로 적분한다.

- 2. 신경망은 보편 근사기로서 제어 변량으로 사용될 수 있지만, 일반적으로 분석적 적분이 불가능하다는 문제가 있다.

- 3. 본 논문에서는 연속적인 조각별 선형 활성화 함수를 가진 다층 퍼셉트론(MLP)의 가능한 분석적 적분을 연구한다.

- 4. 2D에서 계산 기하학 기법을 활용한 적분 영역 세분화 기반의 적분 방법을 제안한다.

- 5. 제안된 적분 방법과 MLP를 결합하여 제어 변량으로 활용할 수 있음을 보이며, 조명 운반 시뮬레이션에의 응용을 제시한다.

---

*Generated on 2025-09-22 15:39:24*