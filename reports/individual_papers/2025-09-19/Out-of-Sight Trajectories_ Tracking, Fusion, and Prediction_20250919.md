
# Out-of-Sight Trajectories: Tracking, Fusion, and Prediction

**Korean Title:** 보이지 않는 궤적: 추적, 융합 및 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Trajectory Prediction, Sensor Data Denoising

## 🔗 유사한 논문
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.6% similar)
- [[Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (80.0% similar)
- [[DECAMP Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (79.6% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (79.1% similar)
- [[Occupancy-aware_Trajectory_Planning_for_Autonomous_Valet_Parking_in_Uncertain_Dynamic_Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15219v1 Announce Type: cross 
Abstract: Trajectory prediction is a critical task in computer vision and autonomous systems, playing a key role in autonomous driving, robotics, surveillance, and virtual reality. Existing methods often rely on complete and noise-free observational data, overlooking the challenges associated with out-of-sight objects and the inherent noise in sensor data caused by limited camera coverage, obstructions, and the absence of ground truth for denoised trajectories. These limitations pose safety risks and hinder reliable prediction in real-world scenarios. In this extended work, we present advancements in Out-of-Sight Trajectory (OST), a novel task that predicts the noise-free visual trajectories of out-of-sight objects using noisy sensor data. Building on our previous research, we broaden the scope of Out-of-Sight Trajectory Prediction (OOSTraj) to include pedestrians and vehicles, extending its applicability to autonomous driving, robotics, surveillance, and virtual reality. Our enhanced Vision-Positioning Denoising Module leverages camera calibration to establish a vision-positioning mapping, addressing the lack of visual references, while effectively denoising noisy sensor data in an unsupervised manner. Through extensive evaluations on the Vi-Fi and JRDB datasets, our approach achieves state-of-the-art performance in both trajectory denoising and prediction, significantly surpassing previous baselines. Additionally, we introduce comparisons with traditional denoising methods, such as Kalman filtering, and adapt recent trajectory prediction models to our task, providing a comprehensive benchmark. This work represents the first initiative to integrate vision-positioning projection for denoising noisy sensor trajectories of out-of-sight agents, paving the way for future advances. The code and preprocessed datasets are available at github.com/Hai-chao-Zhang/OST

## 🔍 Abstract (한글 번역)

arXiv:2509.15219v1 발표 유형: 교차  
초록: 궤적 예측은 컴퓨터 비전과 자율 시스템에서 중요한 과제로, 자율 주행, 로봇 공학, 감시, 가상 현실에서 핵심적인 역할을 합니다. 기존 방법들은 종종 완전하고 잡음이 없는 관찰 데이터를 기반으로 하며, 시야 밖 물체와 제한된 카메라 범위, 장애물, 잡음이 제거된 궤적에 대한 실제 데이터의 부재로 인해 발생하는 센서 데이터의 고유한 잡음과 관련된 문제를 간과합니다. 이러한 제한은 안전 위험을 초래하고 실제 시나리오에서 신뢰할 수 있는 예측을 방해합니다. 이 확장된 연구에서는 시야 밖 궤적(OST)에서의 발전을 제시하며, 잡음이 있는 센서 데이터를 사용하여 시야 밖 물체의 잡음 없는 시각적 궤적을 예측하는 새로운 과제를 소개합니다. 이전 연구를 바탕으로, 우리는 시야 밖 궤적 예측(OOSTraj)의 범위를 보행자와 차량을 포함하도록 확장하여 자율 주행, 로봇 공학, 감시, 가상 현실에의 적용 가능성을 넓혔습니다. 향상된 비전-포지셔닝 잡음 제거 모듈은 카메라 보정을 활용하여 비전-포지셔닝 매핑을 설정하고, 시각적 참조의 부족 문제를 해결하며, 비지도 방식으로 잡음이 있는 센서 데이터를 효과적으로 잡음 제거합니다. Vi-Fi 및 JRDB 데이터셋에 대한 광범위한 평가를 통해, 우리의 접근 방식은 궤적 잡음 제거 및 예측에서 최첨단 성능을 달성하며, 이전 기준을 크게 능가합니다. 또한, 칼만 필터링과 같은 전통적인 잡음 제거 방법과의 비교를 소개하고, 최근 궤적 예측 모델을 우리의 과제에 맞게 조정하여 포괄적인 벤치마크를 제공합니다. 이 연구는 시야 밖 에이전트의 잡음 있는 센서 궤적을 잡음 제거하기 위해 비전-포지셔닝 투영을 통합하는 첫 번째 시도로, 향후 발전의 길을 열어줍니다. 코드와 전처리된 데이터셋은 github.com/Hai-chao-Zhang/OST에서 이용할 수 있습니다.

## 📝 요약

이 논문은 자율 주행, 로봇 공학, 감시, 가상 현실 등에서 중요한 역할을 하는 경로 예측 문제를 다룹니다. 기존 방법들은 완전하고 잡음이 없는 데이터를 가정하지만, 이 연구는 시야 밖 객체의 잡음 있는 센서 데이터를 활용하여 잡음 없는 경로를 예측하는 새로운 과제인 Out-of-Sight Trajectory (OST)를 제안합니다. 특히, 카메라 보정을 활용한 Vision-Positioning Denoising Module을 통해 시각적 참조가 부족한 문제를 해결하고, 비지도 학습 방식으로 센서 데이터의 잡음을 제거합니다. Vi-Fi와 JRDB 데이터셋을 통한 평가에서 기존 방법들을 능가하는 성능을 보였으며, Kalman 필터링 등 전통적인 방법과의 비교도 포함하여 포괄적인 벤치마크를 제공합니다. 이 연구는 시야 밖 객체의 잡음 있는 경로를 시각-위치 투영을 통해 제거하는 최초의 시도로, 향후 발전 가능성을 제시합니다. 관련 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 본 연구는 시야 밖 객체의 노이즈 없는 시각적 궤적을 예측하는 새로운 과제인 Out-of-Sight Trajectory (OST)를 제시합니다.

- 2. Vision-Positioning Denoising Module을 통해 카메라 보정을 활용하여 시각-위치 매핑을 구축하고, 비지도 방식으로 센서 데이터의 노이즈를 제거합니다.

- 3. Vi-Fi 및 JRDB 데이터셋을 통한 평가에서, 제안된 방법은 궤적 노이즈 제거 및 예측에서 최첨단 성능을 달성하며 기존 기준선을 크게 초과합니다.

- 4. Kalman 필터링과 같은 전통적인 노이즈 제거 방법과의 비교를 통해 포괄적인 벤치마크를 제공합니다.

- 5. 이 연구는 시야 밖 에이전트의 노이즈 센서 궤적을 제거하기 위해 시각-위치 투영을 통합한 최초의 시도로, 향후 발전의 길을 열었습니다.

---

*Generated on 2025-09-19 15:37:26*