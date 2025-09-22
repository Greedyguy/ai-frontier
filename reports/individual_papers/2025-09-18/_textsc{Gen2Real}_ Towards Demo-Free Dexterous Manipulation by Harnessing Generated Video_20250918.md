
# \textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video

**Korean Title:** \textsc{Gen2Real}: 생성된 비디오를 활용하여 데모 없이 민첩한 조작을 실현하기 위해

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Physics-aware Interaction Optimization Model

## 🔗 유사한 논문
- [[PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models]] (86.1% similar)
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (83.7% similar)
- [[Learning Multimodal Attention for Manipulating Deformable Objects with Changing States]] (83.0% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.8% similar)
- [[Motion_Adaptation_Across_Users_and_Tasks_for_Exoskeletons_via_Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (82.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14178v1 Announce Type: new 
Abstract: Dexterous manipulation remains a challenging robotics problem, largely due to the difficulty of collecting extensive human demonstrations for learning. In this paper, we introduce \textsc{Gen2Real}, which replaces costly human demos with one generated video and drives robot skill from it: it combines demonstration generation that leverages video generation with pose and depth estimation to yield hand-object trajectories, trajectory optimization that uses Physics-aware Interaction Optimization Model (PIOM) to impose physics consistency, and demonstration learning that retargets human motions to a robot hand and stabilizes control with an anchor-based residual Proximal Policy Optimization (PPO) policy. Using only generated videos, the learned policy achieves a 77.3\% success rate on grasping tasks in simulation and demonstrates coherent executions on a real robot. We also conduct ablation studies to validate the contribution of each component and demonstrate the ability to directly specify tasks using natural language, highlighting the flexibility and robustness of \textsc{Gen2Real} in generalizing grasping skills from imagined videos to real-world execution.

## 🔍 Abstract (한글 번역)

arXiv:2509.14178v1 발표 유형: 새로운
요약: 미세한 조작은 주로 학습을 위해 방대한 인간 데모를 수집하는 어려움으로 인해 어려운 로봇 공학 문제로 남아 있습니다. 본 논문에서는 비용이 많이 드는 인간 데모를 하나 생성된 비디오로 대체하고 로봇 기술을 이동시키는 \textsc{Gen2Real}을 소개합니다. 이는 비디오 생성을 활용한 데모 생성, 포즈 및 깊이 추정을 결합하여 손-물체 궤적을 생성하고, 물리학 일관성을 부여하기 위해 물리학 인지 최적화 모델 (PIOM)을 사용하는 궤적 최적화, 그리고 인간 동작을 로봇 손에 재타겟팅하고 앵커 기반의 잔여 근접 정책 최적화 (PPO) 정책으로 제어를 안정화하는 데모 학습을 결합합니다. 생성된 비디오만 사용하여 학습된 정책은 시뮬레이션에서 77.3%의 성공률을 달성하고 실제 로봇에서 일관된 실행을 보여줍니다. 또한 각 구성 요소의 기여를 검증하기 위해 소성 연구를 수행하고, 자연어를 사용하여 직접 작업을 지정할 수 있는 능력을 보여줌으로써, \textsc{Gen2Real}의 그리핑 기술을 상상된 비디오에서 실제 실행으로 일반화하는 유연성과 견고성을 강조합니다.

## 📝 요약

이 논문은 인간 데모 수집의 어려움으로 인해 여전히 어려운 로봇의 미세 조작 문제에 대해 다루고 있습니다. 본 연구에서는 비용이 많이 드는 인간 데모 대신 생성된 비디오를 활용하여 로봇 스킬을 구축하는 \textsc{Gen2Real}을 소개합니다. 이는 비디오 생성을 활용한 데모 생성, 자세 및 깊이 추정을 결합하여 손-물체 궤적을 얻는 것, 물리학 일관성을 부여하기 위해 물리학 인식 최적화 모델(PIOM)을 활용한 궤적 최적화, 그리고 인간 동작을 로봇 손에 재타겟팅하고 앵커 기반 잔차 근접 정책 최적화(PPO) 정책으로 제어를 안정화하는 데모 학습을 결합합니다. 생성된 비디오만을 사용하여 학습된 정책은 시뮬레이션에서 77.3%의 성공률을 달성하고 실제 로봇에서 일관된 실행을 보여줍니다. 또한 각 구성 요소의 기여를 검증하기 위해 소거 연구를 수행하고 자연어를 사용하여 작업을 직접 지정할 수 있는 능력을 보여줌으로써, \textsc{Gen2Real}의 일반적인 쥐집 능력과 견고성을 강조하고 있습니다.

## 🎯 주요 포인트

- 인간 데모 수집의 어려움을 극복하기 위해 생성된 비디오를 활용한 로봇 스킬 학습 방법 소개

- 생성된 비디오만을 사용하여 시뮬레이션에서 77.3%의 성공률을 달성하고 실제 로봇에서 일관된 실행을 보임

- 각 구성 요소의 기여를 검증하기 위한 실험 및 자연어를 사용하여 직접 작업을 지정하는 능력을 보여줌

- \textsc{Gen2Real}의 유연성과 견고성 강조 및 상상된 비디오에서 현실 세계 실행으로 총화하는 능력을 시연함

---

*Generated on 2025-09-18 17:18:16*