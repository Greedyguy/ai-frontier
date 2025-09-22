# Probabilistic Conformal Coverage Guarantees in Small-Data Settings

**Korean Title:** 소규모 데이터 환경에서의 확률적 적합 범위 보장

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Probabilistic Guarantees

## 🔗 유사한 논문
- [[2025-09-18/Efficient Conformal Prediction for Regression Models under Label Noise_20250918|Efficient Conformal Prediction for Regression Models under Label Noise]] (79.7% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (78.5% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.4% similar)
- [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One Aligned Representation Pairs for Anomaly Detection]] (77.6% similar)
- [[2025-09-19/Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision_ An Information-Theoretic Impossibility_20250919|Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision An Information-Theoretic Impossibility]] (76.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15349v1 Announce Type: new 
Abstract: Conformal prediction provides distribution-free prediction sets with guaranteed marginal coverage. However, in split conformal prediction this guarantee is training-conditional only in expectation: across many calibration draws, the average coverage equals the nominal level, but the realized coverage for a single calibration set may vary substantially. This variance undermines effective risk control in practical applications. Here we introduce the Small Sample Beta Correction (SSBC), a plug-and-play adjustment to the conformal significance level that leverages the exact finite-sample distribution of conformal coverage to provide probabilistic guarantees, ensuring that with user-defined probability over the calibration draw, the deployed predictor achieves at least the desired coverage.

## 🔍 Abstract (한글 번역)

arXiv:2509.15349v1 발표 유형: 신규  
초록: 적합 예측(Conformal prediction)은 분포에 구애받지 않는 예측 집합을 제공하며, 이는 주변 커버리지를 보장합니다. 그러나 분할 적합 예측(split conformal prediction)에서는 이 보장이 훈련 조건에서만 기대치로 제공됩니다. 즉, 여러 보정 샘플에서 평균 커버리지는 명목 수준과 같지만, 단일 보정 세트에 대한 실현된 커버리지는 상당히 다를 수 있습니다. 이러한 분산은 실제 응용에서 효과적인 위험 통제를 저해합니다. 여기서 우리는 적합 유의 수준에 대한 플러그 앤 플레이 조정인 소표본 베타 보정(Small Sample Beta Correction, SSBC)을 소개합니다. 이는 적합 커버리지의 정확한 유한 샘플 분포를 활용하여 확률적 보장을 제공하며, 사용자가 정의한 확률로 보정 샘플에 대해 배포된 예측기가 최소한 원하는 커버리지를 달성하도록 보장합니다.

## 📝 요약

이 논문은 분할 적합 예측(split conformal prediction)의 한계를 보완하기 위해 소규모 샘플 베타 보정(SSBC)을 제안합니다. 기존 방법은 평균적으로 목표 커버리지를 달성하지만, 개별 검증 세트에서는 커버리지가 크게 변동할 수 있어 실질적인 위험 관리에 어려움이 있습니다. SSBC는 적합 커버리지의 유한 샘플 분포를 활용하여, 사용자 정의 확률에 따라 예측기가 최소한의 목표 커버리지를 달성하도록 보장합니다. 이 방법은 실용적인 확률적 보장을 제공하여 예측의 신뢰성을 높입니다.

## 🎯 주요 포인트

- 1. 대칭 예측은 분포에 구애받지 않는 예측 집합을 제공하며, 평균적으로 명목 수준의 보장을 제공합니다.

- 2. 분할 대칭 예측에서는 단일 보정 세트의 실현된 커버리지가 크게 변동할 수 있어 효과적인 위험 통제를 방해합니다.

- 3. SSBC(Small Sample Beta Correction)는 대칭 유의 수준에 대한 조정으로, 유한 샘플 분포를 활용하여 확률적 보장을 제공합니다.

- 4. SSBC는 사용자 정의 확률에 따라 보정 추출에서 배포된 예측기가 최소한의 원하는 커버리지를 달성하도록 보장합니다.

---

*Generated on 2025-09-22 15:11:01*