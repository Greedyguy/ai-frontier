# Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery

**Korean Title:** 다이나믹 신경 호기심이 자율적 목표 발견을 위한 학습 유연성을 향상시킴

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Attention Mechanism, Multi-layer Perceptrons

## 🔗 유사한 논문
- [[2025-09-18/Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (81.8% similar)
- [[2025-09-17/Prompt2Auto_ From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning_20250917|Prompt2Auto From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning]] (81.7% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (81.5% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (81.2% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (81.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.00152v2 Announce Type: replace-cross 
Abstract: The autonomous learning of new goals in robotics remains a complex issue to address. Here, we propose a model where curiosity influence learning flexibility. To do so, this paper proposes to root curiosity and attention together by taking inspiration from the Locus Coeruleus-Norepinephrine system along with various cognitive processes such as cognitive persistence and visual habituation. We apply our approach by experimenting with a simulated robotic arm on a set of objects with varying difficulty. The robot first discovers new goals via bottom-up attention through motor babbling with an inhibition of return mechanism, then engage to the learning of goals due to neural activity arising within the curiosity mechanism. The architecture is modelled with dynamic neural fields and the learning of goals such as pushing the objects in diverse directions is supported by the use of forward and inverse models implemented by multi-layer perceptrons. The adoption of dynamic neural fields to model curiosity, habituation and persistence allows the robot to demonstrate various learning trajectories depending on the object. In addition, the approach exhibits interesting properties regarding the learning of similar goals as well as the continuous switch between exploration and exploitation.

## 🔍 Abstract (한글 번역)

arXiv:2412.00152v2 발표 유형: 교차 교체  
초록: 로봇 공학에서 새로운 목표를 자율적으로 학습하는 것은 여전히 해결해야 할 복잡한 문제로 남아 있습니다. 여기서 우리는 호기심이 학습 유연성에 영향을 미치는 모델을 제안합니다. 이를 위해 이 논문은 청색반점-노르에피네프린 시스템과 인지적 지속성 및 시각적 습관화와 같은 다양한 인지 과정을 바탕으로 호기심과 주의를 함께 뿌리내리는 것을 제안합니다. 우리는 난이도가 다양한 객체 세트를 사용하여 시뮬레이션된 로봇 팔을 실험함으로써 우리의 접근 방식을 적용합니다. 로봇은 먼저 귀환 억제 메커니즘을 통한 운동 재잘거림을 통해 하향식 주의로 새로운 목표를 발견한 후, 호기심 메커니즘 내에서 발생하는 신경 활동으로 인해 목표 학습에 참여합니다. 이 아키텍처는 동적 신경 필드로 모델링되며, 다양한 방향으로 객체를 밀어내는 것과 같은 목표의 학습은 다층 퍼셉트론에 의해 구현된 순방향 및 역방향 모델의 사용에 의해 지원됩니다. 호기심, 습관화 및 지속성을 모델링하기 위해 동적 신경 필드를 채택함으로써 로봇은 객체에 따라 다양한 학습 경로를 보여줄 수 있습니다. 또한, 이 접근 방식은 유사한 목표의 학습과 탐색과 활용 간의 지속적인 전환에 관한 흥미로운 특성을 보여줍니다.

## 📝 요약

이 논문은 로봇 공학에서 새로운 목표를 자율적으로 학습하는 문제를 다룹니다. 호기심이 학습 유연성에 미치는 영향을 탐구하며, Locus Coeruleus-Norepinephrine 시스템과 인지적 지속성, 시각적 습관화 등의 인지 과정을 결합한 모델을 제안합니다. 시뮬레이션된 로봇 팔을 이용해 다양한 난이도의 객체를 대상으로 실험을 수행하였으며, 로봇은 하위 주의와 운동 탐색을 통해 새로운 목표를 발견하고, 호기심 메커니즘에 의해 목표 학습에 참여합니다. 동적 신경 필드를 활용한 이 아키텍처는 호기심, 습관화, 지속성을 모델링하여 객체에 따라 다양한 학습 경로를 보여줍니다. 또한, 유사한 목표 학습 및 탐색과 활용 간의 지속적인 전환에서 흥미로운 특성을 나타냅니다.

## 🎯 주요 포인트

- 1. 로봇의 새로운 목표 학습에 있어 호기심이 학습 유연성에 미치는 영향을 모델링하였다.

- 2. Locus Coeruleus-Norepinephrine 시스템과 인지 지속성, 시각적 습관화 등의 인지 과정을 결합하여 호기심과 주의를 함께 뿌리내리는 접근법을 제안하였다.

- 3. 모터 바블링과 반환 억제 메커니즘을 통해 로봇이 새로운 목표를 발견하고, 호기심 메커니즘의 신경 활동을 통해 목표 학습에 참여한다.

- 4. 동적 신경 필드를 사용하여 호기심, 습관화, 지속성을 모델링함으로써 로봇이 객체에 따라 다양한 학습 경로를 보일 수 있도록 하였다.

- 5. 유사한 목표 학습 및 탐색과 활용 간의 지속적인 전환에 대한 흥미로운 특성을 나타낸다.

---

*Generated on 2025-09-22 14:40:24*