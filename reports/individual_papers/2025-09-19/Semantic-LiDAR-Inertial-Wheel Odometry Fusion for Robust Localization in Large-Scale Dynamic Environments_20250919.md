
# Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments

**Korean Title:** 대규모 동적 환경에서의 강인한 위치 추정을 위한 의미론적 LiDAR-관성-휠 오도메트리 융합

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Iterative Error-State Kalman Filter, Semantic Voxel Map

## 🔗 유사한 논문
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (86.6% similar)
- [[Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (84.0% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (83.0% similar)
- [[InterKey Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap]] (82.6% similar)
- [[Human Interaction for Collaborative Semantic SLAM using Extended Reality_20250919|Human Interaction for Collaborative Semantic SLAM using Extended Reality]] (82.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14999v1 Announce Type: new 
Abstract: Reliable, drift-free global localization presents significant challenges yet remains crucial for autonomous navigation in large-scale dynamic environments. In this paper, we introduce a tightly-coupled Semantic-LiDAR-Inertial-Wheel Odometry fusion framework, which is specifically designed to provide high-precision state estimation and robust localization in large-scale dynamic environments. Our framework leverages an efficient semantic-voxel map representation and employs an improved scan matching algorithm, which utilizes global semantic information to significantly reduce long-term trajectory drift. Furthermore, it seamlessly fuses data from LiDAR, IMU, and wheel odometry using a tightly-coupled multi-sensor fusion Iterative Error-State Kalman Filter (iESKF). This ensures reliable localization without experiencing abnormal drift. Moreover, to tackle the challenges posed by terrain variations and dynamic movements, we introduce a 3D adaptive scaling strategy that allows for flexible adjustments to wheel odometry measurement weights, thereby enhancing localization precision. This study presents extensive real-world experiments conducted in a one-million-square-meter automated port, encompassing 3,575 hours of operational data from 35 Intelligent Guided Vehicles (IGVs). The results consistently demonstrate that our system outperforms state-of-the-art LiDAR-based localization methods in large-scale dynamic environments, highlighting the framework's reliability and practical value.

## 🔍 Abstract (한글 번역)

arXiv:2509.14999v1 발표 유형: 신규  
초록: 신뢰할 수 있고 드리프트 없는 글로벌 로컬라이제이션은 상당한 도전 과제를 제시하지만, 대규모 동적 환경에서 자율 주행을 위해 필수적입니다. 본 논문에서는 대규모 동적 환경에서 높은 정밀도의 상태 추정과 강력한 로컬라이제이션을 제공하도록 설계된 긴밀하게 결합된 시맨틱-LiDAR-관성-휠 오도메트리 융합 프레임워크를 소개합니다. 우리의 프레임워크는 효율적인 시맨틱-복셀 맵 표현을 활용하고, 글로벌 시맨틱 정보를 활용하여 장기적인 궤적 드리프트를 크게 줄이는 개선된 스캔 매칭 알고리즘을 사용합니다. 또한, LiDAR, IMU 및 휠 오도메트리 데이터를 긴밀하게 결합된 다중 센서 융합 반복 오차 상태 칼만 필터(iESKF)를 사용하여 매끄럽게 융합합니다. 이는 비정상적인 드리프트 없이 신뢰할 수 있는 로컬라이제이션을 보장합니다. 더 나아가, 지형 변화와 동적 움직임이 제기하는 문제를 해결하기 위해 휠 오도메트리 측정 가중치를 유연하게 조정할 수 있는 3D 적응형 스케일링 전략을 도입하여 로컬라이제이션 정밀도를 향상시킵니다. 본 연구는 35대의 지능형 유도 차량(IGV)으로부터 3,575시간의 운영 데이터를 포함한 백만 평방미터 규모의 자동화된 항구에서 수행된 광범위한 실제 실험을 제시합니다. 결과는 일관되게 대규모 동적 환경에서 최첨단 LiDAR 기반 로컬라이제이션 방법보다 우리의 시스템이 우수함을 보여주며, 프레임워크의 신뢰성과 실용적 가치를 강조합니다.

## 📝 요약

이 논문은 대규모 동적 환경에서의 자율 주행을 위한 신뢰성 있는 전역 위치 추정을 목표로, 고정밀 상태 추정과 강력한 위치 추정을 제공하는 Semantic-LiDAR-Inertial-Wheel Odometry 융합 프레임워크를 제안합니다. 이 프레임워크는 효율적인 시맨틱-복셀 맵 표현과 글로벌 시맨틱 정보를 활용한 개선된 스캔 매칭 알고리즘을 통해 장기적인 경로 드리프트를 크게 줄입니다. 또한, LiDAR, IMU, 휠 오도메트리 데이터를 iESKF를 통해 긴밀하게 융합하여 비정상적인 드리프트 없이 신뢰성 있는 위치 추정을 보장합니다. 지형 변화와 동적 움직임에 대응하기 위해 3D 적응형 스케일링 전략을 도입하여 휠 오도메트리 측정 가중치를 유연하게 조정함으로써 위치 추정 정밀도를 높입니다. 100만 평방미터 규모의 자동화 항구에서 3,575시간의 운영 데이터를 통해 실험한 결과, 제안된 시스템이 기존의 LiDAR 기반 위치 추정 방법보다 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 대규모 동적 환경에서 고정밀 상태 추정과 강력한 위치 추정을 제공하는 Semantic-LiDAR-Inertial-Wheel Odometry 융합 프레임워크를 소개합니다.

- 2. 효율적인 시맨틱-복셀 맵 표현과 개선된 스캔 매칭 알고리즘을 활용하여 장기적인 궤적 드리프트를 크게 줄입니다.

- 3. LiDAR, IMU, 휠 오도메트리 데이터를 긴밀하게 융합하는 iESKF를 사용하여 비정상적인 드리프트 없이 신뢰할 수 있는 위치 추정을 보장합니다.

- 4. 지형 변화와 동적 움직임에 대응하기 위해 3D 적응형 스케일링 전략을 도입하여 휠 오도메트리 측정 가중치를 유연하게 조정합니다.

- 5. 3575시간의 운영 데이터를 기반으로 한 실험 결과, 제안된 시스템이 대규모 동적 환경에서 최첨단 LiDAR 기반 위치 추정 방법보다 우수한 성능을 보임을 입증합니다.

---

*Generated on 2025-09-19 16:35:22*