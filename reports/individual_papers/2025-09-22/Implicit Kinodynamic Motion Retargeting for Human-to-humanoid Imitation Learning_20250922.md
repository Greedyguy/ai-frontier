# Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning

**Korean Title:** 인간에서 휴머노이드로의 모방 학습을 위한 암묵적 운동역학 모션 리타게팅

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Dual Encoder Decoder Architecture

## 🔗 유사한 논문
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (86.3% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (84.7% similar)
- [[2025-09-18/Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (84.5% similar)
- [[2025-09-18/textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|textsc{Gen2Real} Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (83.6% similar)
- [[2025-09-17/Prompt2Auto_ From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning_20250917|Prompt2Auto From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning]] (83.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15443v1 Announce Type: cross 
Abstract: Human-to-humanoid imitation learning aims to learn a humanoid whole-body controller from human motion. Motion retargeting is a crucial step in enabling robots to acquire reference trajectories when exploring locomotion skills. However, current methods focus on motion retargeting frame by frame, which lacks scalability. Could we directly convert large-scale human motion into robot-executable motion through a more efficient approach? To address this issue, we propose Implicit Kinodynamic Motion Retargeting (IKMR), a novel efficient and scalable retargeting framework that considers both kinematics and dynamics. In kinematics, IKMR pretrains motion topology feature representation and a dual encoder-decoder architecture to learn a motion domain mapping. In dynamics, IKMR integrates imitation learning with the motion retargeting network to refine motion into physically feasible trajectories. After fine-tuning using the tracking results, IKMR can achieve large-scale physically feasible motion retargeting in real time, and a whole-body controller could be directly trained and deployed for tracking its retargeted trajectories. We conduct our experiments both in the simulator and the real robot on a full-size humanoid robot. Extensive experiments and evaluation results verify the effectiveness of our proposed framework.

## 🔍 Abstract (한글 번역)

arXiv:2509.15443v1 발표 유형: 교차  
초록: 인간-휴머노이드 모방 학습은 인간의 움직임으로부터 휴머노이드 전신 제어기를 학습하는 것을 목표로 합니다. 모션 리타게팅은 로봇이 이동 기술을 탐색할 때 참조 궤적을 획득할 수 있도록 하는 중요한 단계입니다. 그러나 현재의 방법들은 프레임별로 모션 리타게팅에 초점을 맞추고 있어 확장성이 부족합니다. 대규모 인간의 움직임을 더 효율적인 방법으로 로봇이 실행 가능한 움직임으로 직접 변환할 수 있을까요? 이 문제를 해결하기 위해, 우리는 암묵적 운동역학 모션 리타게팅(Implicit Kinodynamic Motion Retargeting, IKMR)을 제안합니다. 이는 운동학과 동역학을 모두 고려한 새로운 효율적이고 확장 가능한 리타게팅 프레임워크입니다. 운동학에서는 IKMR이 모션 토폴로지 특징 표현과 이중 인코더-디코더 아키텍처를 사전 훈련하여 모션 도메인 매핑을 학습합니다. 동역학에서는 IKMR이 모방 학습을 모션 리타게팅 네트워크와 통합하여 물리적으로 실행 가능한 궤적으로 모션을 정제합니다. 추적 결과를 사용하여 세부 조정한 후, IKMR은 실시간으로 대규모 물리적으로 실행 가능한 모션 리타게팅을 달성할 수 있으며, 전신 제어기는 리타게팅된 궤적을 추적하기 위해 직접 훈련되고 배포될 수 있습니다. 우리는 시뮬레이터와 실제 로봇에서 풀 사이즈 휴머노이드 로봇을 사용하여 실험을 수행했습니다. 광범위한 실험과 평가 결과는 제안된 프레임워크의 효과성을 검증합니다.

## 📝 요약

이 논문은 인간의 동작을 휴머노이드 로봇에 모방 학습시키는 새로운 방법론인 암묵적 운동-동역학 모션 리타게팅(IKMR)을 제안합니다. 기존 방법들이 프레임 단위로 동작을 변환하는 데 비해, IKMR은 대규모 인간 동작을 로봇이 실행 가능한 형태로 효율적으로 변환합니다. IKMR은 운동학과 동역학을 모두 고려하여 모션 토폴로지 특징을 사전 학습하고, 이중 인코더-디코더 구조를 통해 모션 도메인 매핑을 학습합니다. 또한, 모방 학습을 통해 물리적으로 실현 가능한 궤적으로 동작을 정제합니다. 실험 결과, IKMR은 실시간으로 대규모 모션 리타게팅을 가능하게 하며, 실제 로봇 실험에서도 그 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. 인간의 대규모 모션을 로봇이 실행 가능한 모션으로 효율적으로 변환하는 방법을 제안합니다.

- 2. IKMR은 운동학과 역학을 고려한 새로운 리타게팅 프레임워크로, 모션 도메인 매핑을 학습합니다.

- 3. IKMR은 모방 학습과 모션 리타게팅 네트워크를 통합하여 물리적으로 실행 가능한 궤적을 생성합니다.

- 4. 실험 결과, IKMR은 대규모 모션 리타게팅을 실시간으로 수행하며, 전신 제어기를 직접 훈련 및 배포할 수 있습니다.

- 5. 시뮬레이터와 실제 로봇 실험을 통해 제안된 프레임워크의 효과가 입증되었습니다.

---

*Generated on 2025-09-22 13:57:06*