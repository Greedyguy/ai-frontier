# Efficient Conformal Prediction for Regression Models under Label Noise

**Korean Title:** 레이블 노이즈 하의 회귀 모델을 위한 효율적인 적합 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Yahav Cohen|Yahav Cohen]] [[authors/Jacob Goldberger|Jacob Goldberger]] [[authors/Tom Tirer|Tom Tirer]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Conformal Prediction

## 🔗 유사한 논문
- [[Towards Trustworthy Vital Sign Forecasting_ Leveraging Uncertainty for Prediction Intervals_20250918|Towards Trustworthy Vital Sign Forecasting Leveraging Uncertainty for Prediction Intervals]] (77.9% similar)
- [[Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (76.8% similar)
- [[Optimal Learning from Label Proportions with General Loss Functions_20250919|Optimal Learning from Label Proportions with General Loss Functions]] (76.3% similar)
- [[Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (75.6% similar)
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (75.5% similar)

## 📋 저자 정보

**Authors:** Yahav Cohen, Jacob Goldberger, Tom Tirer

## 📄 Abstract (원문)

In high-stakes scenarios, such as medical imaging applications, it is
critical to equip the predictions of a regression model with reliable
confidence intervals. Recently, Conformal Prediction (CP) has emerged as a
powerful statistical framework that, based on a labeled calibration set,
generates intervals that include the true labels with a pre-specified
probability. In this paper, we address the problem of applying CP for
regression models when the calibration set contains noisy labels. We begin by
establishing a mathematically grounded procedure for estimating the noise-free
CP threshold. Then, we turn it into a practical algorithm that overcomes the
challenges arising from the continuous nature of the regression problem. We
evaluate the proposed method on two medical imaging regression datasets with
Gaussian label noise. Our method significantly outperforms the existing
alternative, achieving performance close to the clean-label setting.

## 🔍 Abstract (한글 번역)

고위험 시나리오, 예를 들어 의료 영상 응용 분야에서는 회귀 모델의 예측에 신뢰할 수 있는 신뢰 구간을 제공하는 것이 중요합니다. 최근에는 라벨이 지정된 보정 세트를 기반으로 사전 지정된 확률로 실제 라벨을 포함하는 구간을 생성하는 강력한 통계적 프레임워크인 적합 예측(Conformal Prediction, CP)이 주목받고 있습니다. 본 논문에서는 보정 세트에 잡음이 있는 라벨이 포함된 경우 회귀 모델에 CP를 적용하는 문제를 다룹니다. 먼저, 잡음이 없는 CP 임계값을 추정하기 위한 수학적으로 근거 있는 절차를 확립합니다. 그런 다음, 회귀 문제의 연속적인 특성에서 발생하는 문제를 극복할 수 있는 실용적인 알고리즘으로 전환합니다. 제안된 방법을 가우시안 라벨 잡음이 있는 두 개의 의료 영상 회귀 데이터셋에서 평가한 결과, 기존의 대안을 크게 능가하며 깨끗한 라벨 설정에 가까운 성능을 달성했습니다.

## 📝 요약

이 논문은 의료 영상과 같은 중요한 분야에서 회귀 모델의 예측에 신뢰할 수 있는 신뢰 구간을 제공하는 방법을 제안합니다. 최근 주목받고 있는 통계적 프레임워크인 적합 예측(Conformal Prediction, CP)을 활용하여, 레이블에 노이즈가 포함된 경우에도 신뢰 구간을 생성할 수 있도록 개선했습니다. 저자들은 먼저 수학적으로 노이즈 없는 CP 임계값을 추정하는 절차를 확립하고, 이를 실제 알고리즘으로 구현하여 회귀 문제의 연속성 문제를 해결했습니다. 제안된 방법은 가우시안 레이블 노이즈가 있는 두 개의 의료 영상 데이터셋에서 기존 방법보다 우수한 성능을 보였으며, 깨끗한 레이블 설정에 가까운 성과를 달성했습니다.

## 🎯 주요 포인트

- 1. 회귀 모델의 예측에 신뢰할 수 있는 신뢰 구간을 제공하는 것이 중요합니다.

- 2. Conformal Prediction(CP)은 사전 지정된 확률로 참 레이블을 포함하는 구간을 생성하는 강력한 통계적 프레임워크입니다.

- 3. 본 논문에서는 노이즈가 있는 레이블을 포함한 보정 세트가 있을 때 CP를 회귀 모델에 적용하는 문제를 다룹니다.

- 4. 노이즈가 없는 CP 임계값을 추정하는 수학적으로 근거 있는 절차를 제시하고, 이를 실용적인 알고리즘으로 전환합니다.

- 5. 제안된 방법은 기존 대안을 크게 능가하며, 깨끗한 레이블 설정에 가까운 성능을 달성합니다.

---

*Generated on 2025-09-20 00:59:34*