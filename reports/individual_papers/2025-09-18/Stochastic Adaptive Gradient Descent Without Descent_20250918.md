# Stochastic Adaptive Gradient Descent Without Descent

**Korean Title:** 확률적 적응 경사 하강법 없이 하강하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Jean-François Aujol|Jean-François Aujol]] [[authors/Jérémie Bigot|Jérémie Bigot]] [[authors/Camille Castera|Camille Castera]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Adaptive Step-size Strategy

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.2% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (77.2% similar)
- [[Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (76.7% similar)
- [[Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (76.6% similar)
- [[Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors_20250919|Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors]] (75.9% similar)

## 📋 저자 정보

**Authors:** Jean-François Aujol, Jérémie Bigot, Camille Castera

## 📄 Abstract (원문)

We introduce a new adaptive step-size strategy for convex optimization with
stochastic gradient that exploits the local geometry of the objective function
only by means of a first-order stochastic oracle and without any
hyper-parameter tuning. The method comes from a theoretically-grounded
adaptation of the Adaptive Gradient Descent Without Descent method to the
stochastic setting. We prove the convergence of stochastic gradient descent
with our step-size under various assumptions, and we show that it empirically
competes against tuned baselines.

## 🔍 Abstract (한글 번역)

새로운 적응형 스텝 크기 전략을 소개합니다. 이 전략은 확률적 기울기를 사용하는 볼록 최적화에서 목표 함수의 국소 기하학을 첫 번째 차수의 확률적 오라클만을 통해 활용하며, 하이퍼파라미터 조정이 필요 없습니다. 이 방법은 Adaptive Gradient Descent Without Descent 방법을 확률적 환경에 맞게 이론적으로 적응시킨 결과입니다. 우리는 다양한 가정 하에서 우리의 스텝 크기를 사용한 확률적 경사 하강법의 수렴성을 증명하며, 이 방법이 조정된 기준선과 비교하여 경험적으로 경쟁력을 갖춘다는 것을 보여줍니다.

## 📝 요약

이 논문은 확률적 경사 하강법(SGD)에서 새로운 적응형 스텝 사이즈 전략을 제안합니다. 이 방법은 목표 함수의 지역 기하학을 활용하며, 1차 확률적 오라클만을 사용하고 하이퍼파라미터 튜닝이 필요 없습니다. 기존의 Adaptive Gradient Descent Without Descent 방법을 확률적 환경에 맞게 이론적으로 조정한 것입니다. 제안된 스텝 사이즈를 사용한 SGD의 수렴성을 다양한 가정 하에 증명하였으며, 실험적으로 튜닝된 기존 방법들과 경쟁력을 보였습니다.

## 🎯 주요 포인트

- 1. 새로운 적응형 스텝 크기 전략은 목적 함수의 지역 기하학을 활용하여 하이퍼파라미터 튜닝 없이 확률적 기울기 하강을 수행합니다.

- 2. 이 방법은 Adaptive Gradient Descent Without Descent 방법을 확률적 설정에 맞게 이론적으로 적응시킨 것입니다.

- 3. 제안된 스텝 크기를 사용하는 확률적 기울기 하강법의 수렴성을 다양한 가정 하에 증명하였습니다.

- 4. 제안된 방법은 실험적으로 튜닝된 기준선과 경쟁력을 가집니다.

---

*Generated on 2025-09-20 01:39:34*