---
keywords:
  - Tilted Empirical Risk Minimization
  - Outlier Detection
  - Robust Regression
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15141
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:54:59.889942",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tilted Empirical Risk Minimization",
    "Outlier Detection",
    "Robust Regression"
  ],
  "rejected_keywords": [
    "Empirical Risk Minimization"
  ],
  "similarity_scores": {
    "Tilted Empirical Risk Minimization": 0.78,
    "Outlier Detection": 0.77,
    "Robust Regression": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Benefits of Online Tilted Empirical Risk Minimization: A Case Study of Outlier Detection and Robust Regression

**Korean Title:** 온라인 기울어진 경험적 위험 최소화의 이점: 이상치 탐지 및 강건 회귀의 사례 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Outlier Detection|Outlier Detection]], [[keywords/Robust Regression|Robust Regression]]
**⚡ Unique Technical**: [[keywords/Tilted Empirical Risk Minimization|Tilted Empirical Risk Minimization]]

## 🔗 유사한 논문
- [[Multi-Fidelity_Hybrid_Reinforcement_Learning_via_Information_Gain_Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.8% similar)
- [[Sample_Efficient_Experience_Replay_in_Non-stationary_Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (79.1% similar)
- [[Optimal_Learning_from_Label_Proportions_with_General_Loss_Functions_20250919|Optimal Learning from Label Proportions with General Loss Functions]] (78.5% similar)
- [[Accelerated Gradient Methods with Biased Gradient Estimates Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (77.5% similar)
- [[Efficient Last-Iterate Convergence in Regret Minimization via Adaptive Reward Transformation]] (77.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15141v1 Announce Type: cross 
Abstract: Empirical Risk Minimization (ERM) is a foundational framework for supervised learning but primarily optimizes average-case performance, often neglecting fairness and robustness considerations. Tilted Empirical Risk Minimization (TERM) extends ERM by introducing an exponential tilt hyperparameter $t$ to balance average-case accuracy with worst-case fairness and robustness. However, in online or streaming settings where data arrive one sample at a time, the classical TERM objective degenerates to standard ERM, losing tilt sensitivity. We address this limitation by proposing an online TERM formulation that removes the logarithm from the classical objective, preserving tilt effects without additional computational or memory overhead. This formulation enables a continuous trade-off controlled by $t$, smoothly interpolating between ERM ($t \to 0$), fairness emphasis ($t > 0$), and robustness to outliers ($t < 0$). We empirically validate online TERM on two representative streaming tasks: robust linear regression with adversarial outliers and minority-class detection in binary classification. Our results demonstrate that negative tilting effectively suppresses outlier influence, while positive tilting improves recall with minimal impact on precision, all at per-sample computational cost equivalent to ERM. Online TERM thus recovers the full robustness-fairness spectrum of classical TERM in an efficient single-sample learning regime.

## 🔍 Abstract (한글 번역)

arXiv:2509.15141v1 발표 유형: 교차  
초록: 경험적 위험 최소화(ERM)는 지도 학습을 위한 기초적인 프레임워크이지만, 주로 평균적인 성능을 최적화하여 공정성과 견고성 고려를 종종 간과합니다. 기울어진 경험적 위험 최소화(TERM)는 평균적인 정확도와 최악의 경우의 공정성과 견고성을 균형 있게 조절하기 위해 지수 기울기 하이퍼파라미터 $t$를 도입하여 ERM을 확장합니다. 그러나 데이터가 한 번에 하나씩 도착하는 온라인 또는 스트리밍 환경에서는, 고전적인 TERM 목표가 표준 ERM으로 퇴화하여 기울기 민감성을 잃습니다. 우리는 고전적인 목표에서 로그를 제거하여 추가적인 계산이나 메모리 부담 없이 기울기 효과를 유지하는 온라인 TERM 공식을 제안하여 이 한계를 해결합니다. 이 공식은 $t$에 의해 제어되는 연속적인 절충을 가능하게 하여, ERM ($t \to 0$), 공정성 강조 ($t > 0$), 이상치에 대한 견고성 ($t < 0$) 사이를 부드럽게 보간합니다. 우리는 두 가지 대표적인 스트리밍 작업인 적대적 이상치가 있는 견고한 선형 회귀와 이진 분류에서의 소수 클래스 탐지에 대해 온라인 TERM을 경험적으로 검증합니다. 우리의 결과는 부정적인 기울기가 효과적으로 이상치의 영향을 억제하고, 긍정적인 기울기가 정밀도에 최소한의 영향을 미치면서 재현율을 향상시킨다는 것을 보여줍니다. 모든 것이 ERM과 동등한 샘플당 계산 비용으로 이루어집니다. 따라서 온라인 TERM은 효율적인 단일 샘플 학습 체계에서 고전적인 TERM의 전체 견고성-공정성 스펙트럼을 회복합니다.

## 📝 요약

Empirical Risk Minimization(ERM)은 평균 성능 최적화에 중점을 두지만 공정성과 강건성을 간과할 수 있습니다. 이를 개선하기 위해 Tilted Empirical Risk Minimization(TERM)은 지수 기울기 매개변수 $t$를 도입하여 평균 성능과 최악의 경우의 공정성 및 강건성을 균형 있게 조절합니다. 그러나 온라인 환경에서는 기존 TERM 목표가 ERM으로 퇴화하는 문제가 있습니다. 이를 해결하기 위해 우리는 로그를 제거한 온라인 TERM 공식을 제안하여 기울기 효과를 유지하면서 추가적인 계산이나 메모리 부담 없이 조절할 수 있도록 했습니다. 이 공식은 $t$에 따라 ERM($t \to 0$), 공정성 강조($t > 0$), 이상치에 대한 강건성($t < 0$)을 매끄럽게 조절합니다. 두 가지 스트리밍 작업에서 온라인 TERM을 실험한 결과, 음의 기울기는 이상치 영향을 억제하고 양의 기울기는 재현율을 향상시키면서 정밀도에 미치는 영향을 최소화함을 확인했습니다. 온라인 TERM은 단일 샘플 학습 환경에서 효율적으로 강건성과 공정성의 전체 스펙트럼을 회복합니다.

## 🎯 주요 포인트

- 1. 기울어진 경험적 위험 최소화(TERM)는 평균 성능과 최악의 경우의 공정성과 강건성을 균형 있게 조정합니다.

- 2. 온라인 환경에서 기존 TERM 목적은 표준 ERM으로 퇴화하여 기울기 민감성을 잃습니다.

- 3. 제안된 온라인 TERM 공식은 로그를 제거하여 추가적인 계산 또는 메모리 부담 없이 기울기 효과를 유지합니다.

- 4. 온라인 TERM은 기울기 매개변수 $t$를 통해 ERM, 공정성 강조, 이상치에 대한 강건성 간의 연속적인 절충을 가능하게 합니다.

- 5. 실험 결과, 온라인 TERM은 이상치의 영향을 억제하고 소수 클래스 검출에서 재현율을 향상시킵니다.

---

*Generated on 2025-09-19 15:37:00*