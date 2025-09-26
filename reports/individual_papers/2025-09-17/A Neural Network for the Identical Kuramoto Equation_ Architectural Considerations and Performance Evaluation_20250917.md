---
keywords:
  - Deep Learning
  - Activation Functions
  - Kuramoto Model
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:03:05.713850",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Activation Functions",
    "Kuramoto Model"
  ],
  "rejected_keywords": [
    "Nonlocal Conservation Laws"
  ],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Activation Functions": 0.8,
    "Kuramoto Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation

**Korean Title:** 동일한 쿠라마토 방정식을 위한 신경망: 구조적 고려사항 및 성능 평가

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Neural Networks]]
**🔗 Specific Connectable**: [[keywords/Activation Functions|activation function]]
**⚡ Unique Technical**: [[keywords/Kuramoto Model|Kuramoto model]]

## 🔗 유사한 논문
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (81.4% similar)
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (80.9% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.4% similar)
- [[Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks_20250917|Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks]] (79.8% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (79.4% similar)

## 📋 저자 정보

**Authors:** Nishantak Panigrahi, Mayank Patwal

## 📄 Abstract (원문)

In this paper, we investigate the efficiency of Deep Neural Networks (DNNs)
to approximate the solution of a nonlocal conservation law derived from the
identical-oscillator Kuramoto model, focusing on the evaluation of an
architectural choice and its impact on solution accuracy based on the energy
norm and computation time. Through systematic experimentation, we demonstrate
that network configuration parameters-specifically, activation function
selection (tanh vs. sin vs. ReLU), network depth (4-8 hidden layers), width
(64-256 neurons), and training methodology (collocation points, epoch
count)-significantly influence convergence characteristics. We observe that
tanh activation yields stable convergence across configurations, whereas sine
activation can attain marginally lower errors and training times in isolated
cases, but occasionally produce nonphysical artefacts. Our comparative analysis
with traditional numerical methods shows that optimally configured DNNs offer
competitive accuracy with notably different computational trade-offs.
Furthermore, we identify fundamental limitations of standard feed-forward
architectures when handling singular or piecewise-constant solutions, providing
empirical evidence that such networks inherently oversmooth sharp features due
to the natural function space limitations of standard activation functions.
This work contributes to the growing body of research on neural network-based
scientific computing by providing practitioners with empirical guidelines for
DNN implementation while illuminating fundamental theoretical constraints that
must be overcome to expand their applicability to more challenging physical
systems with discontinuities.

## 🔍 Abstract (한글 번역)

이 논문에서는 동일한 진동자 쿠라마토 모델에서 유도된 비국소 보존 법칙의 해를 근사하기 위한 심층 신경망(Deep Neural Networks, DNNs)의 효율성을 조사하며, 에너지 노름과 계산 시간을 기반으로 한 해의 정확성에 미치는 건축적 선택의 평가에 중점을 둡니다. 체계적인 실험을 통해 네트워크 구성 매개변수, 즉 활성화 함수 선택(tanh vs. sin vs. ReLU), 네트워크 깊이(4-8개의 은닉층), 폭(64-256개의 뉴런), 훈련 방법론(콜로케이션 포인트, 에포크 수)이 수렴 특성에 상당한 영향을 미친다는 것을 보여줍니다. 우리는 tanh 활성화가 구성 전반에 걸쳐 안정적인 수렴을 제공하는 반면, 사인 활성화는 특정 경우에 약간 더 낮은 오류와 훈련 시간을 달성할 수 있지만 때때로 비물리적 인공물을 생성할 수 있음을 관찰합니다. 전통적인 수치 방법과의 비교 분석을 통해 최적의 DNN 구성은 상당히 다른 계산적 절충을 가지면서도 경쟁력 있는 정확성을 제공함을 보여줍니다. 또한, 표준 피드포워드 아키텍처가 특이점이나 구간별 상수 해를 처리할 때의 근본적인 한계를 식별하며, 이러한 네트워크가 표준 활성화 함수의 자연적 함수 공간 제한으로 인해 본질적으로 급격한 특징을 과도하게 부드럽게 만든다는 실증적 증거를 제공합니다. 이 연구는 신경망 기반 과학 계산에 대한 연구의 증가하는 본문에 기여하며, 실무자에게 DNN 구현에 대한 실증적 지침을 제공하고 불연속성을 가진 보다 도전적인 물리적 시스템에 대한 적용 가능성을 확장하기 위해 극복해야 할 근본적인 이론적 제약을 조명합니다.

## 📝 요약

이 논문은 동일 진동자 쿠라모토 모델에서 유도된 비국소 보존 법칙의 해를 근사하는 딥러닝 네트워크(DNN)의 효율성을 연구합니다. 네트워크 구성 요소인 활성화 함수(tanh, sin, ReLU), 네트워크 깊이와 너비, 훈련 방법론이 수렴 특성에 미치는 영향을 체계적으로 실험했습니다. tanh 활성화 함수는 안정적인 수렴을 보여주며, sin 활성화 함수는 특정 상황에서 낮은 오류와 훈련 시간을 제공하지만 비물리적 결과를 초래할 수 있습니다. 전통적 수치 해법과 비교하여 최적화된 DNN은 경쟁력 있는 정확성을 제공하지만 계산적 차이가 있습니다. 또한, 표준 피드포워드 구조가 급격한 특징을 다루는 데 한계가 있음을 밝혔습니다. 이 연구는 과학적 계산에서 DNN의 구현 가이드라인을 제공하고, 불연속성을 가진 물리 시스템에 대한 적용성을 확장하기 위한 이론적 제약을 조명합니다.

## 🎯 주요 포인트

- 1. 딥러닝 네트워크의 구성 요소, 특히 활성화 함수 선택과 네트워크의 깊이 및 너비가 수렴 특성에 큰 영향을 미친다.

- 2. tanh 활성화 함수는 안정적인 수렴을 보이며, sine 활성화 함수는 특정 경우에 더 낮은 오류와 짧은 학습 시간을 제공할 수 있지만 비물리적 결과를 초래할 수 있다.

- 3. 최적화된 DNN은 전통적인 수치 해석 방법과 비교하여 경쟁력 있는 정확도를 제공하지만 계산적 트레이드오프가 다르다.

- 4. 표준 피드포워드 아키텍처는 특이점이나 조각별 상수 솔루션을 처리할 때 본질적으로 날카로운 특징을 과도하게 부드럽게 만드는 한계를 가진다.

- 5. 이 연구는 신경망 기반 과학 계산에 대한 실증적 지침을 제공하며, 불연속성을 가진 물리 시스템에 대한 적용성을 확장하기 위한 이론적 제약을 밝힌다.

---

*Generated on 2025-09-20 07:37:12*