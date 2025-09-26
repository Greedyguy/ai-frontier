---
keywords:
  - Optimization
  - Full Waveform Inversion
  - Cycle Skipping
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:25:07.674146",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Optimization",
    "Full Waveform Inversion",
    "Cycle Skipping"
  ],
  "rejected_keywords": [
    "Neural Networks"
  ],
  "similarity_scores": {
    "Optimization": 0.8,
    "Full Waveform Inversion": 0.78,
    "Cycle Skipping": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Inspired by machine learning optimization: can gradient-based optimizers solve cycle skipping in full waveform inversion given sufficient iterations?

**Korean Title:** 기계 학습 최적화에 영감을 받아: 충분한 반복 횟수가 주어졌을 때, 그래디언트 기반 최적화 기법이 전파형상 역산에서의 주기 건너뛰기 문제를 해결할 수 있는가?

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Gradient-based optimizers]]
**⚡ Unique Technical**: [[keywords/Full Waveform Inversion|Full waveform inversion]], [[keywords/Cycle Skipping|Cycle skipping]]

## 🔗 유사한 논문
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (76.7% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (76.1% similar)
- [[Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250918|Mind the Gap Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (75.8% similar)
- [[The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (75.6% similar)
- [[Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (75.6% similar)

## 📋 저자 정보

**Authors:** Xinru Mu, Omar M. Saad, Shaowen Wang, Tariq Alkhalifah

## 📄 Abstract (원문)

Full waveform inversion (FWI) iteratively updates the velocity model by
minimizing the difference between observed and simulated data. Due to the high
computational cost and memory requirements associated with global optimization
algorithms, FWI is typically implemented using local optimization methods.
However, when the initial velocity model is inaccurate and low-frequency
seismic data (e.g., below 3 Hz) are absent, the mismatch between simulated and
observed data may exceed half a cycle, a phenomenon known as cycle skipping. In
such cases, local optimization algorithms (e.g., gradient-based local
optimizers) tend to converge to local minima, leading to inaccurate inversion
results. In machine learning, neural network training is also an optimization
problem prone to local minima. It often employs gradient-based optimizers with
a relatively large learning rate (beyond the theoretical limits of local
optimization that are usually determined numerically by a line search), which
allows the optimization to behave like a quasi-global optimizer. Consequently,
after training for several thousand iterations, we can obtain a neural network
model with strong generative capability. In this study, we also employ
gradient-based optimizers with a relatively large learning rate for FWI.
Results from both synthetic and field data experiments show that FWI may
initially converge to a local minimum; however, with sufficient additional
iterations, the inversion can gradually approach the global minimum, slowly
from shallow subsurface to deep, ultimately yielding an accurate velocity
model. Furthermore, numerical examples indicate that, given sufficient
iterations, reasonable velocity inversion results can still be achieved even
when low-frequency data below 5 Hz are missing.

## 🔍 Abstract (한글 번역)

전파형 역산(FWI)은 관측 데이터와 시뮬레이션 데이터 간의 차이를 최소화하여 속도 모델을 반복적으로 갱신합니다. 전역 최적화 알고리즘과 관련된 높은 계산 비용과 메모리 요구 사항 때문에, FWI는 일반적으로 지역 최적화 방법을 사용하여 구현됩니다. 그러나 초기 속도 모델이 부정확하고 저주파 지진 데이터(예: 3 Hz 이하)가 없는 경우, 시뮬레이션 데이터와 관측 데이터 간의 불일치가 반주기 이상이 될 수 있으며, 이를 사이클 스키핑(cycle skipping) 현상이라고 합니다. 이러한 경우, 지역 최적화 알고리즘(예: 기울기 기반 지역 최적화기)은 지역 최소값에 수렴하는 경향이 있어 부정확한 역산 결과를 초래할 수 있습니다. 기계 학습에서는 신경망 훈련도 지역 최소값에 취약한 최적화 문제입니다. 이는 종종 비교적 큰 학습률을 가진 기울기 기반 최적화기를 사용하여, 최적화가 준전역 최적화기처럼 작동할 수 있게 합니다. 결과적으로 수천 번의 반복 훈련 후, 강력한 생성 능력을 가진 신경망 모델을 얻을 수 있습니다. 본 연구에서는 FWI에 대해 비교적 큰 학습률을 가진 기울기 기반 최적화기를 사용합니다. 합성 및 현장 데이터 실험 결과, FWI는 초기에는 지역 최소값에 수렴할 수 있지만, 충분한 추가 반복을 통해 역산이 전역 최소값에 점진적으로 접근할 수 있으며, 얕은 지하에서 깊은 지하로 천천히 진행되어 궁극적으로 정확한 속도 모델을 얻을 수 있음을 보여줍니다. 또한, 수치 예제는 충분한 반복이 주어질 경우, 5 Hz 이하의 저주파 데이터가 없어도 합리적인 속도 역산 결과를 여전히 얻을 수 있음을 나타냅니다.

## 📝 요약

이 연구는 Full waveform inversion(FWI)에서 초기 속도 모델이 부정확하고 저주파 데이터가 부족할 때 발생하는 사이클 스키핑 문제를 해결하기 위해, 머신러닝에서 사용하는 큰 학습률의 경사 기반 최적화 방법을 적용했습니다. 기존의 국소 최적화 방법은 지역 최소값에 수렴하여 부정확한 결과를 초래할 수 있지만, 제안된 방법은 충분한 반복을 통해 전역 최소값에 점진적으로 접근할 수 있음을 보여주었습니다. 실험 결과, 저주파 데이터가 부족한 경우에도 충분한 반복을 통해 정확한 속도 모델을 얻을 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. FWI는 관측 데이터와 시뮬레이션 데이터 간의 차이를 최소화하여 속도 모델을 반복적으로 갱신하는 방법이다.

- 2. 초기 속도 모델이 부정확하고 저주파 지진 데이터가 없을 경우, 사이클 스키핑 현상이 발생하여 지역 최적화 알고리즘이 부정확한 결과로 수렴할 수 있다.

- 3. 머신러닝에서는 큰 학습률을 사용하는 경사 기반 최적화가 준-전역 최적화기로 작동하여 강력한 생성 능력을 가진 모델을 얻을 수 있다.

- 4. 본 연구에서는 FWI에 큰 학습률을 가진 경사 기반 최적화를 적용하여, 초기에는 지역 최소값에 수렴하더라도 추가 반복을 통해 전역 최소값에 점진적으로 접근할 수 있음을 보였다.

- 5. 충분한 반복이 주어지면, 5 Hz 이하의 저주파 데이터가 없어도 합리적인 속도 역산 결과를 얻을 수 있다.

---

*Generated on 2025-09-20 02:43:48*