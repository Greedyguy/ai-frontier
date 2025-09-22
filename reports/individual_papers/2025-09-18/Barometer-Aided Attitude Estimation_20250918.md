
# Barometer-Aided Attitude Estimation

**Korean Title:** 기압계 지원 자세 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Complementary Filter

## 🔗 유사한 논문
- [[Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (78.8% similar)
- [[Disturbance-Aware_Dynamical_Trajectory_Planning_for_Air-Land_Bimodal_Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (78.2% similar)
- [[NavMoE_Hybrid_Model-_and_Learning-based_Traversability_Estimation_for_Local_Navigation_via_Mixture_of_Experts_20250918|NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (78.0% similar)
- [[Gaussian_Alignment_for_Relative_Camera_Pose_Estimation_via_Single-View_Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (77.1% similar)
- [[Occupancy-aware_Trajectory_Planning_for_Autonomous_Valet_Parking_in_Uncertain_Dynamic_Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (76.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13649v1 Announce Type: new 
Abstract: Accurate and robust attitude estimation is a central challenge for autonomous vehicles operating in GNSS-denied or highly dynamic environments. In such cases, Inertial Measurement Units (IMUs) alone are insufficient for reliable tilt estimation due to the ambiguity between gravitational and inertial accelerations. While auxiliary velocity sensors, such as GNSS, Pitot tubes, Doppler radar, or visual odometry, are often used, they can be unavailable, intermittent, or costly. This work introduces a barometer-aided attitude estimation architecture that leverages barometric altitude measurements to infer vertical velocity and attitude within a nonlinear observer on SO(3). The design cascades a deterministic Riccati observer with a complementary filter, ensuring Almost Global Asymptotic Stability (AGAS) under a uniform observability condition while maintaining geometric consistency. The analysis highlights barometer-aided estimation as a lightweight and effective complementary modality.

## 🔍 Abstract (한글 번역)

arXiv:2509.13649v1 발표 유형: 새로운
요약: 정확하고 견고한 자세 추정은 GNSS가 거부되거나 고도 동적 환경에서 운영되는 자율 주행 차량에 대한 중요한 과제입니다. 이러한 경우에는 관성 측정 장치(IMUs)만으로는 신뢰할 수있는 기울기 추정이 어렵습니다. 중력 및 관성 가속도 사이의 모호성 때문입니다. 보조 속도 센서인 GNSS, 피토타입, 도플러 레이더 또는 시각적 오도메트리와 같은 보조 장치가 종종 사용되지만 사용할 수 없거나 간헐적이거나 비용이 많이 들 수 있습니다. 본 연구는 대기압 보조 자세 추정 구조를 소개합니다. 이 구조는 대기압 고도 측정을 활용하여 수직 속도와 자세를 SO(3)의 비선형 옵저버 내에서 추론합니다. 이 설계는 결정론적 리카티 옵저버를 보완 필터와 연계시켜 거의 전역적으로 점근적 안정성(AGAS)을 보장하면서 기하학적 일관성을 유지합니다. 이 분석은 대기압 보조 추정을 경량이면서 효과적인 보조 모달리티로 강조합니다.

## 📝 요약

자율주행 차량이 GNSS가 제한된 환경이나 고도 변화가 심한 환경에서 정확하고 견고한 자세 추정은 중요한 과제이다. 본 논문은 기압계 고도 측정을 활용하여 수직 속도와 자세를 추정하는 비선형 옵저버를 소개한다. 이 설계는 결정론적 Riccati 옵저버와 보완 필터를 연쇄시켜 거의 전역 점근 안정성을 보장하면서 기하학적 일관성을 유지한다. 분석 결과, 기압계 보조 추정은 가벼우면서 효과적인 보조 모달리티로 나타났다.

## 🎯 주요 포인트

- 자율 주행 차량에서 중요한 도전 과제는 GNSS가 제한되거나 고도의 동적 환경에서 작동할 때 정확하고 견고한 자세 추정이다.

- 보조 속도 센서를 사용하는 것이 일반적이지만 가용하지 않거나 가끔식이거나 비용이 많이 들 수 있다.

- 이 연구는 기압계 고도 측정을 활용하여 수직 속도와 자세를 추론하는 방법을 제안하며 이를 통해 가벼우면서도 효과적인 보조 모달리티로 강조한다.

---

*Generated on 2025-09-18 17:14:31*