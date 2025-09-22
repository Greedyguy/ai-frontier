# A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks

**Korean Title:** 물리 정보 신경망에서 불확실성 정량화를 위한 적합 예측 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Yifan Yu|Yifan Yu]] [[authors/Cheuk Hin Ho|Cheuk Hin Ho]] [[authors/Yangshuai Wang|Yangshuai Wang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distribution-Free Uncertainty Quantification

## 🔗 유사한 논문
- [[Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (85.0% similar)
- [[Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (83.8% similar)
- [[Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (82.2% similar)
- [[Efficient Conformal Prediction for Regression Models under Label Noise_20250918|Efficient Conformal Prediction for Regression Models under Label Noise]] (79.1% similar)
- [[An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (78.4% similar)

## 📋 저자 정보

**Authors:** Yifan Yu, Cheuk Hin Ho, Yangshuai Wang

## 📄 Abstract (원문)

Physics-Informed Neural Networks (PINNs) have emerged as a powerful framework
for solving PDEs, yet existing uncertainty quantification (UQ) approaches for
PINNs generally lack rigorous statistical guarantees. In this work, we bridge
this gap by introducing a distribution-free conformal prediction (CP) framework
for UQ in PINNs. This framework calibrates prediction intervals by constructing
nonconformity scores on a calibration set, thereby yielding distribution-free
uncertainty estimates with rigorous finite-sample coverage guarantees for
PINNs. To handle spatial heteroskedasticity, we further introduce local
conformal quantile estimation, enabling spatially adaptive uncertainty bands
while preserving theoretical guarantee. Through systematic evaluations on
typical PDEs (damped harmonic oscillator, Poisson, Allen-Cahn, and Helmholtz
equations) and comprehensive testing across multiple uncertainty metrics, our
results demonstrate that the proposed framework achieves reliable calibration
and locally adaptive uncertainty intervals, consistently outperforming
heuristic UQ approaches. By bridging PINNs with distribution-free UQ, this work
introduces a general framework that not only enhances calibration and
reliability, but also opens new avenues for uncertainty-aware modeling of
complex PDE systems.

## 🔍 Abstract (한글 번역)

물리학 기반 신경망(Physics-Informed Neural Networks, PINNs)은 편미분 방정식(PDEs)을 해결하는 강력한 프레임워크로 부상했지만, PINNs에 대한 기존의 불확실성 정량화(UQ) 접근법은 일반적으로 엄격한 통계적 보장을 결여하고 있습니다. 본 연구에서는 PINNs의 UQ를 위한 분포 자유 적합 예측(Conformal Prediction, CP) 프레임워크를 도입하여 이 격차를 해소합니다. 이 프레임워크는 보정 집합에서 비적합 점수를 구성하여 예측 구간을 보정함으로써, PINNs에 대해 엄격한 유한 샘플 커버리지 보장을 갖춘 분포 자유 불확실성 추정치를 제공합니다. 공간적 이분산성을 처리하기 위해, 우리는 이론적 보장을 유지하면서 공간적으로 적응적인 불확실성 대역을 가능하게 하는 지역 적합 분위수 추정을 추가로 도입합니다. 감쇠 조화 진동자, 포아송, 앨런-칸, 헬름홀츠 방정식과 같은 전형적인 PDE에 대한 체계적인 평가와 다양한 불확실성 지표에 대한 포괄적인 테스트를 통해, 제안된 프레임워크가 신뢰할 수 있는 보정과 지역적으로 적응적인 불확실성 구간을 달성하며, 일관되게 휴리스틱 UQ 접근법을 능가함을 보여줍니다. PINNs와 분포 자유 UQ를 연결함으로써, 본 연구는 보정과 신뢰성을 향상시킬 뿐만 아니라 복잡한 PDE 시스템의 불확실성 인식 모델링을 위한 새로운 길을 여는 일반적인 프레임워크를 소개합니다.

## 📝 요약

이 연구는 물리 기반 신경망(PINNs)의 불확실성 정량화(UQ)에 대한 새로운 접근법을 제안합니다. 기존의 UQ 방법론은 엄밀한 통계적 보장이 부족했으나, 본 연구는 분포에 의존하지 않는 적합 예측(CP) 프레임워크를 도입하여 이를 해결합니다. 이 프레임워크는 검정 집합에서 비적합 점수를 구축하여 PINNs에 대한 분포 자유 불확실성 추정치를 제공합니다. 또한, 공간적 이분산성을 처리하기 위해 지역 적합 분위수 추정을 도입하여 공간 적응적 불확실성 대역을 가능하게 합니다. 여러 편미분방정식(PDE) 및 다양한 불확실성 지표에 대한 평가 결과, 제안된 프레임워크는 신뢰할 수 있는 보정과 지역 적응적 불확실성 구간을 제공하며 기존의 경험적 UQ 방법을 능가함을 보여줍니다. 이를 통해 PINNs와 분포 자유 UQ를 연결하여 복잡한 PDE 시스템의 불확실성 인식 모델링에 새로운 가능성을 열었습니다.

## 🎯 주요 포인트

- 1. 본 연구는 PINNs의 불확실성 정량화(UQ)를 위한 분포 자유 적합 예측(CP) 프레임워크를 도입하여 엄격한 통계적 보장을 제공합니다.

- 2. 제안된 프레임워크는 비일관성 점수를 사용하여 예측 구간을 보정하고, 유한 샘플 범위 보장을 통해 PINNs의 불확실성을 추정합니다.

- 3. 공간적 이분산성을 처리하기 위해 지역 적합 분위수 추정을 도입하여 공간적으로 적응적인 불확실성 밴드를 제공합니다.

- 4. 여러 불확실성 메트릭에 대한 포괄적인 테스트를 통해 제안된 프레임워크가 신뢰할 수 있는 보정 및 지역적으로 적응적인 불확실성 구간을 달성함을 입증합니다.

- 5. 본 연구는 PINNs와 분포 자유 UQ를 연결하여 복잡한 PDE 시스템의 불확실성 인식 모델링을 위한 새로운 가능성을 제시합니다.

---

*Generated on 2025-09-20 09:38:47*