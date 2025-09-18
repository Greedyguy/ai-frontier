
# A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks

**Korean Title:** 물리학 지식을 활용한 신경망에서 불확실성 양자화를 위한 일치 예측 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Spatially Adaptive Uncertainty Bands|Spatially Adaptive Uncertainty Bands]] [[keywords/broad/Physics-Informed Neural Networks|Physics-Informed Neural Networks]] [[keywords/broad/Conformal Prediction|Conformal Prediction]] [[keywords/specific/Uncertainty Quantification|Uncertainty Quantification]] [[keywords/unique/Local Conformal Quantile Estimation|Local Conformal Quantile Estimation]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Spatially Adaptive Uncertainty Bands
**🔬 Broad Technical**: Physics-Informed Neural Networks, Conformal Prediction
**🔗 Specific Connectable**: Uncertainty Quantification
**⭐ Unique Technical**: Local Conformal Quantile Estimation

**ArXiv ID**: [2509.13717](https://arxiv.org/abs/2509.13717)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13717.pdf)


## 🏷️ 추출된 키워드



`Physics-Informed Neural Networks` • 

`Conformal Prediction` • 

`Uncertainty Quantification` • 

`Local Conformal Quantile Estimation` • 

`Spatially Adaptive Uncertainty Bands`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13717v1 Announce Type: new 
Abstract: Physics-Informed Neural Networks (PINNs) have emerged as a powerful framework for solving PDEs, yet existing uncertainty quantification (UQ) approaches for PINNs generally lack rigorous statistical guarantees. In this work, we bridge this gap by introducing a distribution-free conformal prediction (CP) framework for UQ in PINNs. This framework calibrates prediction intervals by constructing nonconformity scores on a calibration set, thereby yielding distribution-free uncertainty estimates with rigorous finite-sample coverage guarantees for PINNs. To handle spatial heteroskedasticity, we further introduce local conformal quantile estimation, enabling spatially adaptive uncertainty bands while preserving theoretical guarantee. Through systematic evaluations on typical PDEs (damped harmonic oscillator, Poisson, Allen-Cahn, and Helmholtz equations) and comprehensive testing across multiple uncertainty metrics, our results demonstrate that the proposed framework achieves reliable calibration and locally adaptive uncertainty intervals, consistently outperforming heuristic UQ approaches. By bridging PINNs with distribution-free UQ, this work introduces a general framework that not only enhances calibration and reliability, but also opens new avenues for uncertainty-aware modeling of complex PDE systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.13717v1 발표 유형: 새로운
요약: 물리학 지식 기반 신경망 (PINNs)은 PDE를 해결하는 강력한 프레임워크로 등장했지만, 기존의 PINNs에 대한 불확실성 양자화 (UQ) 접근 방식은 일반적으로 엄격한 통계적 보증이 부족합니다. 본 연구에서는 이 간극을 메워 PINNs에서 UQ를 위한 분포 무관한 일치 예측 (CP) 프레임워크를 소개함으로써 이를 극복합니다. 이 프레임워크는 보정 세트에서 비일치 점수를 구성하여 예측 구간을 보정함으로써 PINNs에 대한 엄격한 유한 샘플 커버리지 보증을 갖는 분포 무관한 불확실성 추정을 제공합니다. 공간 이분산성을 처리하기 위해 우리는 지역적 일치 분위수 추정을 소개하여 이론적 보증을 유지하면서 공간적으로 적응적인 불확실성 대역을 가능하게 합니다. 감쇠된 조화 진동자, 포아송, 알렌-칸, 헬름홀츠 방정식과 같은 전형적인 PDE에 대한 체계적인 평가 및 다양한 불확실성 메트릭을 통한 포괄적인 테스트를 통해, 우리의 결과는 제안된 프레임워크가 신뢰할 수 있는 보정과 지역적으로 적응적인 불확실성 구간을 달성하며, 휴리스틱 UQ 접근 방식을 일관되게 능가한다는 것을 보여줍니다. PINNs와 분포 무관한 UQ를 연결함으로써, 본 연구는 보정과 신뢰성을 향상시킬 뿐만 아니라 복잡한 PDE 시스템의 불확실성을 인식하는 모델링을 위한 새로운 길을 열어줍니다.

## 📝 요약

본 연구는 물리학 지식이 반영된 신경망(PINNs)이 편미분방정식(PDEs)을 해결하는 강력한 프레임워크로 등장했지만, 기존의 PINNs에 대한 불확실성 추정(UQ) 방법은 일반적으로 엄격한 통계적 보장이 부족하다. 본 연구에서는 이 간극을 메우기 위해 PINNs의 UQ를 위한 분포-프리(conformal prediction, CP) 프레임워크를 소개한다. 이 프레임워크는 적합성 집합에서 비적합성 점수를 구성하여 예측 구간을 보정함으로써, PINNs에 대한 엄격한 유한 샘플 커버리지 보장을 갖는 분포-프리 불확실성 추정을 제공한다. 공간 이분산성을 처리하기 위해 지역적 적합성 분위수 추정을 도입하여 이론적 보장을 유지하면서 공간적으로 적응적인 불확실성 대역을 구현한다. 표준 PDEs(감쇠진동자, 포아송, 알렌-칸, 헬름홀츠 방정식)에 대한 체계적인 평가와 다양한 불확실성 측정을 통한 포괄적인 테스트를 통해, 제안된 프레임워크가 신뢰할 수 있는 보정과 지역적으로 적응적인 불확실성 구간을 달성하며, 휴리스틱 UQ 방법을 일관되게 능가함을 입증한다. PINNs와 분포-프리 UQ를 결합함으로써, 이 연구는 보정과 신뢰성을 향상시키는데 그치지 않고 복잡한 PDE 시스템에 대한 불확실성 인식 모델링을 위한 새로운 길을 열어준다.

## 🎯 주요 포인트


- 1. 물리학 지식을 활용한 신경망(PINNs)은 PDE 해결에 강력한 프레임워크로 나타났으며, 기존의 불확실성 양자화(UQ) 방법은 엄격한 통계적 보장이 부족한 경향이 있음.

- 2. 분포에 대한 자유로운 일치 예측(CP) 프레임워크를 도입하여 PINNs의 UQ에 대한 엄격한 유한 샘플 커버리지 보장을 제공함.

- 3. 공간적 이분산성을 처리하기 위해 지역적 일치 분위수 추정을 도입하여 이론적 보장을 유지하면서 공간적으로 적응적인 불확실성 대역을 가능하게 함.


---

*Generated on 2025-09-18 16:38:25*