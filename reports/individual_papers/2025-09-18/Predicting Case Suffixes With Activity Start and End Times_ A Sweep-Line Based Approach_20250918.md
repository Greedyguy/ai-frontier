# Predicting Case Suffixes With Activity Start and End Times: A Sweep-Line Based Approach

**Korean Title:** 활동 시작 및 종료 시간을 사용한 사례 접미사 예측: 스윕 라인 기반 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Muhammad Awais Ali|Muhammad Awais Ali]] [[authors/Marlon Dumas|Marlon Dumas]] [[authors/Fredrik Milani|Fredrik Milani]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Model Approach

## 🔗 유사한 논문
- [[ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (75.3% similar)
- [[From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (74.2% similar)
- [[DAG_ A Dual Causal Network for Time Series Forecasting with Exogenous Variables_20250919|DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (74.1% similar)
- [[Stochastic Clock Attention for Aligning Continuous and Ordered Sequences_20250918|Stochastic Clock Attention for Aligning Continuous and Ordered Sequences]] (74.0% similar)
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (73.8% similar)

## 📋 저자 정보

**Authors:** Muhammad Awais Ali, Marlon Dumas, Fredrik Milani

## 📄 Abstract (원문)

Predictive process monitoring techniques support the operational decision
making by predicting future states of ongoing cases of a business process. A
subset of these techniques predict the remaining sequence of activities of an
ongoing case (case suffix prediction). Existing approaches for case suffix
prediction generate sequences of activities with a single timestamp (e.g. the
end timestamp). This output is insufficient for resource capacity planning,
where we need to reason about the periods of time when resources will be busy
performing work. This paper introduces a technique for predicting case suffixes
consisting of activities with start and end timestamps. In other words, the
proposed technique predicts both the waiting time and the processing time of
each activity. Since the waiting time of an activity in a case depends on how
busy resources are in other cases, the technique adopts a sweep-line approach,
wherein the suffixes of all ongoing cases in the process are predicted in
lockstep, rather than predictions being made for each case in isolation. An
evaluation on real-life and synthetic datasets compares the accuracy of
different instantiations of this approach, demonstrating the advantages of a
multi-model approach to case suffix prediction.

## 🔍 Abstract (한글 번역)

예측적 프로세스 모니터링 기법은 비즈니스 프로세스의 진행 중인 사례의 미래 상태를 예측함으로써 운영 의사 결정을 지원합니다. 이러한 기법의 하위 집합은 진행 중인 사례의 남은 활동 시퀀스를 예측합니다(사례 접미사 예측). 기존의 사례 접미사 예측 접근법은 단일 타임스탬프(예: 종료 타임스탬프)를 가진 활동 시퀀스를 생성합니다. 이 출력은 자원 용량 계획에 있어 충분하지 않으며, 여기서는 자원이 작업을 수행하면서 바쁘게 될 시간대를 고려해야 합니다. 본 논문은 시작 및 종료 타임스탬프를 포함한 활동으로 구성된 사례 접미사를 예측하는 기법을 소개합니다. 즉, 제안된 기법은 각 활동의 대기 시간과 처리 시간을 모두 예측합니다. 사례 내 활동의 대기 시간은 다른 사례에서 자원이 얼마나 바쁜지에 따라 달라지므로, 이 기법은 프로세스 내 모든 진행 중인 사례의 접미사를 동기화하여 예측하는 스윕라인 접근법을 채택합니다. 실제 데이터셋과 합성 데이터셋에 대한 평가를 통해 이 접근법의 다양한 구현의 정확성을 비교하여, 사례 접미사 예측에 대한 다중 모델 접근법의 장점을 입증합니다.

## 📝 요약

이 논문은 비즈니스 프로세스의 진행 중인 사례에 대한 미래 상태를 예측하는 기법 중 하나로, 사례의 남은 활동 시퀀스를 시작 및 종료 타임스탬프와 함께 예측하는 새로운 방법을 제안합니다. 기존 방법은 단일 타임스탬프만을 제공하여 자원 용량 계획에 한계가 있었으나, 제안된 기법은 각 활동의 대기 시간과 처리 시간을 예측합니다. 이를 위해 모든 진행 중인 사례의 접미사를 동기화하여 예측하는 스윕 라인 접근법을 사용합니다. 실제 및 합성 데이터셋을 통한 평가 결과, 다중 모델 접근법이 사례 접미사 예측에 유리함을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 비즈니스 프로세스의 진행 중인 사례에 대한 미래 상태를 예측하여 운영 의사 결정을 지원하는 예측 프로세스 모니터링 기술을 다룹니다.

- 2. 기존의 사례 접미사 예측 기법은 단일 타임스탬프(예: 종료 타임스탬프)로 활동 시퀀스를 생성하여 자원 용량 계획에 충분하지 않습니다.

- 3. 본 논문에서는 시작 및 종료 타임스탬프를 포함한 활동으로 구성된 사례 접미사를 예측하는 기법을 제안합니다.

- 4. 제안된 기법은 각 활동의 대기 시간과 처리 시간을 모두 예측하며, 이는 자원이 다른 사례에서 얼마나 바쁜지에 따라 달라집니다.

- 5. 실생활 및 합성 데이터셋에 대한 평가를 통해 이 접근 방식의 다양한 구현의 정확성을 비교하고, 다중 모델 접근 방식의 이점을 입증합니다.

---

*Generated on 2025-09-20 05:53:49*