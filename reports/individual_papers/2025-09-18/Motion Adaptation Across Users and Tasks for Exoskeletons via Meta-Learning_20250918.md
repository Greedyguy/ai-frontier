
# Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning

**Korean Title:** 메타러닝을 통한 외골격을 위한 사용자 및 작업 간 동작 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized Assistance

## 🔗 유사한 논문
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (86.0% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.3% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (82.0% similar)
- [[Embodied_Navigation_Foundation_Model_20250918|Embodied Navigation Foundation Model]] (81.0% similar)
- [[Meta-Optimization_and_Program_Search_using_Language_Models_for_Task_and_Motion_Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13736v1 Announce Type: new 
Abstract: Wearable exoskeletons can augment human strength and reduce muscle fatigue during specific tasks. However, developing personalized and task-generalizable assistance algorithms remains a critical challenge. To address this, a meta-imitation learning approach is proposed. This approach leverages a task-specific neural network to predict human elbow joint movements, enabling effective assistance while enhancing generalization to new scenarios. To accelerate data collection, full-body keypoint motions are extracted from publicly available RGB video and motion-capture datasets across multiple tasks, and subsequently retargeted in simulation. Elbow flexion trajectories generated in simulation are then used to train the task-specific neural network within the model-agnostic meta-learning (MAML) framework, which allows the network to rapidly adapt to novel tasks and unseen users with only a few gradient updates. The adapted network outputs personalized references tracked by a gravity-compensated PD controller to ensure stable assistance. Experimental results demonstrate that the exoskeleton significantly reduces both muscle activation and metabolic cost for new users performing untrained tasks, compared to performing without exoskeleton assistance. These findings suggest that the proposed framework effectively improves task generalization and user adaptability for wearable exoskeleton systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.13736v1 발표 유형: 새로운
요약: 착용형 외골격은 특정 작업 중 인간의 힘을 증강시키고 근육 피로를 감소시킬 수 있습니다. 그러나 맞춤 및 작업 일반화 지원 알고리즘 개발은 여전히 중요한 과제입니다. 이를 해결하기 위해 메타-모방 학습 접근 방식이 제안되었습니다. 이 방법은 인간의 팔꿈치 관절 운동을 예측하기 위해 작업별 신경망을 활용하여 효과적인 지원을 가능하게 하며 새로운 시나리오에 대한 일반화를 향상시킵니다. 데이터 수집을 가속화하기 위해 공개적으로 제공되는 RGB 비디오 및 모션 캡처 데이터 세트에서 전신 주요 포인트 동작이 추출되고 이후 시뮬레이션에서 재지정됩니다. 시뮬레이션에서 생성된 팔꿈치 굴곡 궤적은 모델에 중립적인 메타-러닝 (MAML) 프레임워크 내에서 작업별 신경망을 훈련하는 데 사용되며, 이를 통해 네트워크가 새로운 작업 및 보이지 않는 사용자에 빠르게 적응할 수 있습니다. 적응된 네트워크는 안정적인 지원을 보장하기 위해 중력 보상 PD 컨트롤러에 의해 추적되는 개인화된 참조를 출력합니다. 실험 결과는 외골격이 없는 상태에서 수행하는 새로운 사용자의 훈련되지 않은 작업에 대해 근육 활성화 및 대사 비용을 크게 감소시킨다는 것을 보여줍니다. 이 결과는 제안된 프레임워크가 착용형 외골격 시스템의 작업 일반화 및 사용자 적응성을 효과적으로 향상시킨다는 것을 시사합니다.

## 📝 요약

이 연구는 개인 맞춤형 및 과업 일반화 가능한 보조 알고리즘 개발이 중요한 과제인 웨어러블 외골격을 다룹니다. 메타-모방 학습 접근 방식을 제안하여 과업별 신경망을 활용하여 인간 팔꿈치 운동을 예측하고 새로운 시나리오에 대한 일반화를 강화합니다. 공개 RGB 비디오 및 모션 캡처 데이터셋에서 완전한 몸 키포인트 동작을 추출하고 시뮬레이션에서 재타겟팅하여 데이터 수집을 가속화합니다. 시뮬레이션에서 생성된 팔 굴곡 궤적은 MAML 프레임워크 내에서 과업별 신경망을 훈련하는 데 사용되어 새로운 과업 및 보지 않은 사용자에 빠르게 적응할 수 있습니다. 실험 결과는 외골격이 새로운 사용자가 훈련되지 않은 과업을 수행할 때 근육 활성화와 대사 비용을 현저히 감소시키는 것을 보여줍니다. 이러한 결과는 제안된 프레임워크가 웨어러블 외골격 시스템의 과업 일반화와 사용자 적응성을 효과적으로 향상시킨다는 것을 시사합니다.

## 🎯 주요 포인트

- 개인 맞춤형 및 작업 일반화 지원 알고리즘 개발은 중요한 도전 과제이다.

- 공개적으로 사용 가능한 RGB 비디오 및 모션 캡처 데이터 세트에서 풀 바디 키포인트 모션을 추출하여 데이터 수집을 가속화한다.

- 제안된 프레임워크는 착용형 외골격 시스템의 작업 일반화와 사용자 적응성을 효과적으로 향상시킨다.

---

*Generated on 2025-09-18 17:15:30*