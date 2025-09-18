
# Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds

**Korean Title:** 편향된 기울기 추정을 사용한 가속화된 그래디언트 방법: 위험 감지, 고확률 보장 및 대폭 차이 한계

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Non-asymptotic guarantees|Non-asymptotic guarantees]] [[keywords/broad/First-order methods|First-order methods]] [[keywords/broad/Generalized momentum methods|Generalized momentum methods]] [[keywords/specific/Robust control theory|Robust control theory]] [[keywords/unique/Risk-sensitive index (RSI|Risk-sensitive index (RSI]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Finite-time High-probability Guarantees
**🔬 Broad Technical**: First-order Methods, Generalized Momentum Methods
**🔗 Specific Connectable**: Robust Control Theory
**⭐ Unique Technical**: Risk-sensitive Index (RSI

**ArXiv ID**: [2509.13628](https://arxiv.org/abs/2509.13628)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13628.pdf)


## 🏷️ 추출된 키워드



`First-order methods` • 

`Generalized momentum methods` • 

`Robust control theory` • 

`Risk-sensitive index (RSI` • 

`Finite-time high-probability guarantees`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13628v1 Announce Type: cross 
Abstract: We study trade-offs between convergence rate and robustness to gradient errors in first-order methods. Our focus is on generalized momentum methods (GMMs), a class that includes Nesterov's accelerated gradient, heavy-ball, and gradient descent. We allow stochastic gradient errors that may be adversarial and biased, and quantify robustness via the risk-sensitive index (RSI) from robust control theory. For quadratic objectives with i.i.d. Gaussian noise, we give closed-form expressions for RSI using 2x2 Riccati equations, revealing a Pareto frontier between RSI and convergence rate over stepsize and momentum choices. We prove a large-deviation principle for time-averaged suboptimality and show that the rate function is, up to scaling, the convex conjugate of the RSI. We further connect RSI to the $H_{\infty}$-norm, showing that stronger worst-case robustness (smaller $H_{\infty}$ norm) yields sharper decay of tail probabilities. Beyond quadratics, under biased sub-Gaussian gradient errors, we derive non-asymptotic bounds on a finite-time analogue of the RSI, giving finite-time high-probability guarantees and large-deviation bounds. We also observe an analogous trade-off between RSI and convergence-rate bounds for smooth strongly convex functions. To our knowledge, these are the first non-asymptotic guarantees and risk-sensitive analysis of GMMs with biased gradients. Numerical experiments on robust regression illustrate the results.

## 🔍 Abstract (한글 번역)

arXiv:2509.13628v1 발표 유형: 교차
요약: 우리는 일차 방법에서 수렴 속도와 기울기 오차에 대한 견고성 사이의 트레이드오프를 연구합니다. 우리의 초점은 네스테로프의 가속 그래디언트, 헤비볼, 그리고 그래디언트 강하와 같은 클래스인 일반화된 모멘텀 방법(GMMs)에 있습니다. 우리는 적대적이고 편향된 확률적 그래디언트 오차를 허용하며, 로버스트 제어 이론의 위험 감지 지수(RSI)를 통해 견고성을 양적화합니다. 독립적인 가우시안 노이즈가 있는 이차 목적 함수에 대해, 2x2 리카티 방정식을 사용하여 RSI의 폐쇄형 표현식을 제시하고, 스텝사이즈와 모멘텀 선택에 따른 RSI와 수렴 속도 사이의 파레토 프론티어를 드러냅니다. 우리는 시간 평균 부적합에 대한 대규모 편차 원리를 증명하고, 그 속도 함수가 RSI의 볼록 켄쥬게이트임을 스케일링을 제외하고 보여줍니다. 더 나아가 RSI를 $H_{\infty}$-norm에 연결하여, 더 강한 최악의 경우 견고성(더 작은 $H_{\infty}$ norm)이 꼬리 확률의 빠른 감소를 제공함을 보여줍니다. 이차 함수 이상에서 편향된 서브-가우시안 그래디언트 오차 하에서, RSI의 유한 시간 해석의 비조약적 한계를 유도하여, 유한 시간 내 높은 확률 보장과 대규모 편차 한계를 제공합니다. 또한 매끄럽고 강하게 볼록한 함수에 대한 RSI와 수렴 속도 한계 사이의 유사한 트레이드오프를 관찰합니다. 우리의 지식으로는, 이것들은 편향된 그래디언트를 가진 GMMs의 비조약적 보증과 위험 감지 분석입니다. 견고한 회귀에 대한 수치 실험은 결과를 설명합니다.

## 📝 요약

본 연구는 일차 방법에서 수렴 속도와 그래디언트 오차에 대한 강인성 사이의 트레이드오프를 연구한다. 특히 네스테로프의 가속 경사법, 헤비볼, 그리고 경사 하강법을 포함하는 일반화된 모멘텀 방법(GMMs)에 초점을 맞춘다. 우리는 적대적이고 편향된 확률적 그래디언트 오차를 허용하며, 로버스트 제어 이론의 위험 감각적 지수(RSI)를 통해 강인성을 양적화한다. 가우시안 노이즈가 있는 이차 목적 함수에 대해, 2x2 리카티 방정식을 사용하여 RSI의 닫힌 형태 식을 제시하고, 스텝사이즈와 모멘텀 선택에 따른 RSI와 수렴 속도 사이의 파레토 프론티어를 밝혀냈다. 또한, RSI를 $H_{\infty}$-노름과 연결시켜 최악의 경우 강인성이 높을수록 꼬리 확률의 빠른 감소를 나타낸다. 이 연구는 편향된 그래디언트를 가진 GMMs에 대한 최초의 비점근적 보증과 위험 감각적 분석을 제시한다. 실험 결과는 강건한 회귀에 대한 결과를 보여준다.

## 🎯 주요 포인트


- 1. 일차 방법에서 수렴 속도와 그래디언트 오차에 대한 강인성 사이의 트레이드 오프를 연구했다.

- 2. 일반화된 모멘텀 방법(GMMs)에 대한 위험 감각적 지수(RSI)를 사용하여 강인성을 양적화했다.

- 3. 페어토 프론티어를 보여주며 RSI와 수렴 속도 사이의 트레이드 오프를 밝혔다.

- 4. 편향된 서브-가우시안 그래디언트 오차에 대한 유한 시간 RSI에 대한 비조약적 한계를 유도했다.


---

*Generated on 2025-09-18 16:43:07*