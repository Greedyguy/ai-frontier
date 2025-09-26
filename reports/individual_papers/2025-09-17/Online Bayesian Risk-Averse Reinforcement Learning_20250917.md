---
keywords:
  - Reinforcement Learning
  - Uncertainty Quantification
  - Online Contextual Multi-Arm Bandits
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:48:56.871332",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Uncertainty Quantification",
    "Online Contextual Multi-Arm Bandits"
  ],
  "rejected_keywords": [
    "Bayesian Risk Markov Decision Process"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Uncertainty Quantification": 0.8,
    "Online Contextual Multi-Arm Bandits": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Online Bayesian Risk-Averse Reinforcement Learning

**Korean Title:** 온라인 베이지안 위험 회피 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Uncertainty Quantification|Epistemic Uncertainty]]
**⚡ Unique Technical**: [[keywords/Online Contextual Multi-Arm Bandits|Online Contextual Multi-Arm Bandits]]

## 🔗 유사한 논문
- [[Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (84.1% similar)
- [[Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (82.3% similar)
- [[Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (80.2% similar)
- [[Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (79.9% similar)
- [[Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (79.6% similar)

## 📋 저자 정보

**Authors:** Yuhao Wang, Enlu Zhou

## 📄 Abstract (원문)

In this paper, we study the Bayesian risk-averse formulation in reinforcement
learning (RL). To address the epistemic uncertainty due to a lack of data, we
adopt the Bayesian Risk Markov Decision Process (BRMDP) to account for the
parameter uncertainty of the unknown underlying model. We derive the asymptotic
normality that characterizes the difference between the Bayesian risk value
function and the original value function under the true unknown distribution.
The results indicate that the Bayesian risk-averse approach tends to
pessimistically underestimate the original value function. This discrepancy
increases with stronger risk aversion and decreases as more data become
available. We then utilize this adaptive property in the setting of online RL
as well as online contextual multi-arm bandits (CMAB), a special case of online
RL. We provide two procedures using posterior sampling for both the general RL
problem and the CMAB problem. We establish a sub-linear regret bound, with the
regret defined as the conventional regret for both the RL and CMAB settings.
Additionally, we establish a sub-linear regret bound for the CMAB setting with
the regret defined as the Bayesian risk regret. Finally, we conduct numerical
experiments to demonstrate the effectiveness of the proposed algorithm in
addressing epistemic uncertainty and verifying the theoretical properties.

## 🔍 Abstract (한글 번역)

이 논문에서는 강화 학습(RL)에서 베이지안 위험 회피 공식화를 연구합니다. 데이터 부족으로 인한 인식론적 불확실성을 해결하기 위해, 우리는 미지의 기본 모델의 매개변수 불확실성을 고려하기 위해 베이지안 위험 마르코프 결정 프로세스(BRMDP)를 채택합니다. 우리는 베이지안 위험 가치 함수와 실제 미지의 분포 하에서의 원래 가치 함수 간의 차이를 특징짓는 점근적 정규성을 도출합니다. 결과는 베이지안 위험 회피 접근법이 원래의 가치 함수를 비관적으로 과소평가하는 경향이 있음을 나타냅니다. 이 불일치는 더 강한 위험 회피와 함께 증가하며, 더 많은 데이터가 제공될수록 감소합니다. 그런 다음 우리는 온라인 RL 설정 및 온라인 컨텍스추얼 멀티암드 밴딧(CMAB), 즉 온라인 RL의 특수한 경우에서 이 적응적 특성을 활용합니다. 우리는 일반적인 RL 문제와 CMAB 문제 모두에 대해 사후 샘플링을 사용하는 두 가지 절차를 제공합니다. 우리는 RL 및 CMAB 설정 모두에 대해 전통적인 후회로 정의된 서브-리니어 후회 경계를 확립합니다. 추가적으로, 우리는 베이지안 위험 후회로 정의된 CMAB 설정에 대한 서브-리니어 후회 경계를 확립합니다. 마지막으로, 우리는 인식론적 불확실성을 해결하고 이론적 속성을 검증하는 데 있어 제안된 알고리즘의 효과를 입증하기 위해 수치 실험을 수행합니다.

## 📝 요약

이 논문은 강화 학습에서 베이지안 위험 회피 접근법을 연구합니다. 데이터 부족으로 인한 불확실성을 해결하기 위해, 미지의 모델 파라미터 불확실성을 고려한 베이지안 위험 마르코프 결정 프로세스(BRMDP)를 채택했습니다. 연구 결과, 베이지안 위험 회피 접근법은 원래 가치 함수를 비관적으로 과소평가하며, 이는 위험 회피가 강할수록 증가하고 데이터가 많아질수록 감소합니다. 이러한 적응적 특성을 온라인 강화 학습과 온라인 문맥 기반 다중 슬롯머신 문제(CMAB)에 적용하였으며, 두 가지 상황 모두에 대해 후행 샘플링을 사용하는 절차를 제안했습니다. 일반적인 강화 학습 문제와 CMAB 문제에서 전통적인 후회와 베이지안 위험 후회에 대한 서브-선형 후회 경계를 확립했습니다. 마지막으로, 제안된 알고리즘의 효과성을 수치 실험을 통해 입증했습니다.

## 🎯 주요 포인트

- 1. 본 논문에서는 강화 학습에서 베이지안 위험 회피 공식을 연구하고, 데이터 부족으로 인한 인식 불확실성을 해결하기 위해 BRMDP를 채택합니다.

- 2. 베이지안 위험 가치 함수와 원래 가치 함수 간의 차이를 설명하는 점근적 정규성을 도출하였으며, 베이지안 접근법이 원래 가치 함수를 과소평가하는 경향이 있음을 발견했습니다.

- 3. 위험 회피가 강할수록 이 차이는 증가하고, 데이터가 많아질수록 감소하는 경향이 있습니다.

- 4. 온라인 강화 학습 및 온라인 문맥적 다중 무장 강도 문제 설정에서 후행 표본 추출을 사용하여 두 가지 절차를 제안하고, 서브-선형 후회를 입증했습니다.

- 5. 수치 실험을 통해 제안된 알고리즘이 인식 불확실성을 효과적으로 해결하고 이론적 특성을 검증함을 보여주었습니다.

---

*Generated on 2025-09-20 07:49:28*