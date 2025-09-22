# Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds

**Korean Title:** 편향된 그래디언트 추정치를 사용하는 가속 그래디언트 방법: 위험 민감성, 높은 확률 보장, 및 큰 편차 경계

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Non Asymptotic Large Deviation Bounds|Non Asymptotic Large Deviation Bounds]] [[keywords/specific/Generalized Momentum Methods|Generalized Momentum Methods]] [[keywords/broad/Robust Control Theory|Robust Control Theory]] [[keywords/unique/Risk Sensitive Index|Risk Sensitive Index]] [[categories/cs.LG|cs.LG]] [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (83.3% similar) [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (83.0% similar) [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Non Asymptotic Large Deviation Bounds
**🔗 Specific Connectable**: Generalized Momentum Methods
**🔬 Broad Technical**: Robust Control Theory
**⭐ Unique Technical**: Risk Sensitive Index
## 🔗 유사한 논문
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (83.3% similar)
- [[2025-09-22/Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses_20250922|Policy Gradient Optimzation for Bayesian-Risk MDPs with General Convex Losses]] (83.0% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (81.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (81.5% similar)
- [[2025-09-18/Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain_20250918|Bellman Optimality of Average-Reward Robust Markov Decision Processes with a Constant Gain]] (81.1% similar)


**ArXiv ID**: [2509.13628](https://arxiv.org/abs/2509.13628)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13628.pdf)


**ArXiv ID**: [2509.13628](https://arxiv.org/abs/2509.13628)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13628.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Non Asymptotic Guarantees
**🔗 Specific Connectable**: Generalized Momentum Methods
**⭐ Unique Technical**: Risk Sensitive Index
**🔬 Broad Technical**: Robust Control Theory

## 🏷️ 추출된 키워드



`Robust Control Theory` • 

`Generalized Momentum Methods` • 

`Risk Sensitive Index` • 

`Non Asymptotic Large Deviation Bounds`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13628v2 Announce Type: replace-cross 
Abstract: We study trade-offs between convergence rate and robustness to gradient errors in the context of first-order methods. Our focus is on generalized momentum methods (GMMs)--a broad class that includes Nesterov's accelerated gradient, heavy-ball, and gradient descent methods--for minimizing smooth strongly convex objectives. We allow stochastic gradient errors that may be adversarial and biased, and quantify robustness of these methods to gradient errors via the risk-sensitive index (RSI) from robust control theory. For quadratic objectives with i.i.d. Gaussian noise, we give closed form expressions for RSI in terms of solutions to 2x2 matrix Riccati equations, revealing a Pareto frontier between RSI and convergence rate over the choice of step-size and momentum parameters. We then prove a large-deviation principle for time-averaged suboptimality in the large iteration limit and show that the rate function is, up to a scaling, the convex conjugate of the RSI function. We further show that the rate function and RSI are linked to the $H_\infty$-norm--a measure of robustness to the worst-case deterministic gradient errors--so that stronger worst-case robustness (smaller $H_\infty$-norm) leads to sharper decay of the tail probabilities for the average suboptimality. Beyond quadratics, under potentially biased sub-Gaussian gradient errors, we derive non-asymptotic bounds on a finite-time analogue of the RSI, yielding finite-time high-probability guarantees and non-asymptotic large-deviation bounds for the averaged iterates. In the case of smooth strongly convex functions, we also observe an analogous trade-off between RSI and convergence-rate bounds. To our knowledge, these are the first non-asymptotic guarantees for GMMs with biased gradients and the first risk-sensitive analysis of GMMs. Finally, we provide numerical experiments on a robust regression problem to illustrate our results.

## 🔍 Abstract (한글 번역)

arXiv:2509.13628v2 발표 유형: 교차 교체  
초록: 우리는 1차 방법의 맥락에서 수렴 속도와 기울기 오류에 대한 강건성 사이의 절충점을 연구합니다. 우리의 초점은 매끄럽고 강하게 볼록한 목적을 최소화하기 위한 Nesterov의 가속 기울기, 중력구, 기울기 하강 방법을 포함하는 광범위한 클래스인 일반화된 모멘텀 방법(GMMs)에 있습니다. 우리는 적대적이고 편향된 확률적 기울기 오류를 허용하며, 강건 제어 이론의 위험 민감 지수(RSI)를 통해 이러한 방법의 기울기 오류에 대한 강건성을 정량화합니다. 독립적으로 동일하게 분포된(i.i.d.) 가우시안 노이즈가 있는 이차 목적에 대해, 2x2 행렬 리카티 방정식의 해를 통해 RSI에 대한 닫힌 형식 표현을 제공하여 스텝 크기와 모멘텀 매개변수 선택에 따른 RSI와 수렴 속도 간의 파레토 전선을 드러냅니다. 그런 다음, 큰 반복 한계에서 시간 평균 비최적성에 대한 큰 편차 원리를 증명하고, 속도 함수가 스케일링에 따라 RSI 함수의 볼록 켤레임을 보여줍니다. 또한, 속도 함수와 RSI가 최악의 결정론적 기울기 오류에 대한 강건성의 척도인 $H_\infty$-노름과 연결되어 있음을 보여주어, 더 강한 최악의 경우 강건성(더 작은 $H_\infty$-노름)이 평균 비최적성의 꼬리 확률의 더 날카로운 감소로 이어짐을 나타냅니다. 편향된 서브 가우시안 기울기 오류가 있을 수 있는 경우, 우리는 RSI의 유한 시간 유사체에 대한 비대칭적 경계를 도출하여 유한 시간 높은 확률 보장과 평균 반복에 대한 비대칭적 큰 편차 경계를 제공합니다. 매끄럽고 강하게 볼록한 함수의 경우, 우리는 또한 RSI와 수렴 속도 경계 사이의 유사한 절충점을 관찰합니다. 우리가 아는 한, 이것들은 편향된 기울기를 가진 GMMs에 대한 최초의 비대칭적 보장이며, GMMs에 대한 최초의 위험 민감 분석입니다. 마지막으로, 우리의 결과를 설명하기 위해 강건 회귀 문제에 대한 수치 실험을 제공합니다.

## 📝 요약

이 논문은 1차 방법론에서 수렴 속도와 그래디언트 오류에 대한 강건성 사이의 상충 관계를 연구합니다. 일반화된 모멘텀 방법(GMMs)을 중심으로, 매끄럽고 강하게 볼록한 목표를 최소화하는 과정에서 발생할 수 있는 적대적이고 편향된 확률적 그래디언트 오류에 대한 강건성을 분석합니다. 이 연구는 이차 목표와 독립 동일 분포 가우시안 노이즈를 고려하여, 2x2 리카티 방정식의 해를 통해 위험 민감 지수(RSI)와 수렴 속도 간의 파레토 경계를 제시합니다. 또한, 시간 평균 부최적성에 대한 대편차 원리를 증명하고, RSI 함수의 볼록 켤레와 관련된 비율 함수를 제시합니다. 더 나아가, 최악의 결정론적 그래디언트 오류에 대한 강건성 척도인 $H_\infty$-노름과의 연관성을 보여줍니다. 비이차적 경우에도 편향된 서브가우시안 그래디언트 오류 하에서 비대칭적 경계와 높은 확률 보장을 제공합니다. 이는 GMMs의 편향된 그래디언트에 대한 최초의 비대칭적 보장과 위험 민감 분석입니다. 마지막으로, 강건한 회귀 문제를 통해 결과를 실험적으로 입증합니다.

## 🎯 주요 포인트


- 1. 일반화된 모멘텀 방법(GMMs)은 매끄럽고 강하게 볼록한 목적을 최소화하는 데 사용되며, 이 방법들은 확률적 그래디언트 오류에 대한 강건성을 위험 민감 지수(RSI)로 정량화합니다.

- 2. 이 논문은 i.i.d. 가우시안 노이즈를 가진 이차 목적 함수에 대해 RSI와 수렴 속도 간의 파레토 경계를 드러내며, 이는 스텝 크기와 모멘텀 매개변수 선택에 따라 달라집니다.

- 3. 시간 평균 비최적성에 대한 큰 편차 원리를 증명하고, 비율 함수가 RSI 함수의 볼록 켤레임을 보여줍니다.

- 4. 최악의 결정론적 그래디언트 오류에 대한 강건성을 측정하는 $H_\infty$-노름과 RSI 및 비율 함수 간의 연결을 밝혀내어, 강한 최악의 경우 강건성이 평균 비최적성의 꼬리 확률의 급격한 감소로 이어짐을 보여줍니다.

- 5. 편향된 그래디언트 오류가 있는 GMMs에 대한 비비대칭적 보장과 위험 민감 분석을 제공하는 최초의 연구입니다.


---

*Generated on 2025-09-22 16:18:17*