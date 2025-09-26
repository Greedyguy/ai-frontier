---
keywords:
  - Reinforcement Learning
  - Sim-to-Real Transfer
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13731
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:13:15.564326",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Sim-to-Real Transfer",
    "Vision-Language Model"
  ],
  "rejected_keywords": [
    "Flexible Flat Cables",
    "Foundation Models"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.9,
    "Sim-to-Real Transfer": 0.8,
    "Vision-Language Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Reinforcement Learning for Robotic Insertion of Flexible Cables in Industrial Settings

**Korean Title:** 산업 환경에서 유연한 케이블을 로봇이 삽입하는 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Sim-to-Real Transfer|Sim-to-Real Transfer]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 🔗 유사한 논문
- [[SHaRe-RL_Structured,_Interactive_Reinforcement_Learning_for_Contact-Rich_Industrial_Assembly_Tasks_20250918|SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks]] (85.8% similar)
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (80.6% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (80.2% similar)
- [[Maximizing UAV Cellular Connectivity with Reinforcement Learning for BVLoS Path Planning]] (79.5% similar)
- [[Efficient_Tactile_Perception_with_Soft_Electrical_Impedance_Tomography_and_Pre-trained_Transformer_20250918|Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13731v1 Announce Type: new 
Abstract: The industrial insertion of flexible flat cables (FFCs) into receptacles presents a significant challenge owing to the need for submillimeter precision when handling the deformable cables. In manufacturing processes, FFC insertion with robotic manipulators often requires laborious human-guided trajectory generation. While Reinforcement Learning (RL) offers a solution to automate this task without modeling complex properties of FFCs, the nondeterminism caused by the deformability of FFCs requires significant efforts and time on training. Moreover, training directly in a real environment is dangerous as industrial robots move fast and possess no safety measure. We propose an RL algorithm for FFC insertion that leverages a foundation model-based real-to-sim approach to reduce the training time and eliminate the risk of physical damages to robots and surroundings. Training is done entirely in simulation, allowing for random exploration without the risk of physical damages. Sim-to-real transfer is achieved through semantic segmentation masks which leave only those visual features relevant to the insertion tasks such as the geometric and spatial information of the cables and receptacles. To enhance generality, we use a foundation model, Segment Anything Model 2 (SAM2). To eleminate human intervention, we employ a Vision-Language Model (VLM) to automate the initial prompting of SAM2 to find segmentation masks. In the experiments, our method exhibits zero-shot capabilities, which enable direct deployments to real environments without fine-tuning.

## 🔍 Abstract (한글 번역)

arXiv:2509.13731v1 발표 유형: 새로운
요약: 유연한 평면 케이블 (FFC)을 콘센트에 삽입하는 산업적인 과정은 변형 가능한 케이블을 다룰 때 서브밀리미터 정밀도가 필요하기 때문에 상당한 어려움을 겪고 있습니다. 제조 공정에서 로봇 조작기를 사용한 FFC 삽입은 종종 복잡한 인간 유도 궤적 생성을 필요로 합니다. 강화 학습 (RL)은 FFC의 복잡한 특성을 모델링하지 않고도 이 작업을 자동화하는 해결책을 제공하지만, FFC의 변형성으로 인한 불확실성은 훈련에 상당한 노력과 시간이 필요합니다. 또한, 실제 환경에서 직접 훈련하는 것은 산업용 로봇이 빠르게 움직이고 안전 장치가 없기 때문에 위험합니다. 우리는 FFC 삽입을 위한 RL 알고리즘을 제안합니다. 이 알고리즘은 훈련 시간을 줄이고 로봇 및 주변 환경에 물리적 손상의 위험을 없애기 위해 기초 모델 기반의 실제-시뮬레이션 접근을 활용합니다. 훈련은 완전히 시뮬레이션에서 이루어지며 물리적 손상의 위험이 없는 무작위 탐색이 가능합니다. 시뮬레이션을 통해 시맨틱 세그멘테이션 마스크를 통해 시뮬레이션에서 실제로 전이되는 시뮬-투-리얼 전이를 달성합니다. 이는 케이블과 콘센트의 기하학적 및 공간적 정보와 같은 삽입 작업에 관련된 시각적 특징만 남기기 때문입니다. 일반성을 향상시키기 위해 우리는 Segment Anything Model 2 (SAM2)라는 기초 모델을 사용합니다. 인간 개입을 없애기 위해 Vision-Language Model (VLM)을 사용하여 SAM2의 초기 프롬프팅을 자동화합니다. 실험에서 우리의 방법은 제로샷 기능을 보여주며, 세밀한 조정 없이 실제 환경으로 직접 배포할 수 있게 합니다.

## 📝 요약

유연한 평면 케이블(FFC)을 삽입하는 산업적 도전은 변형 가능한 케이블을 다룰 때 서브밀리미터 정밀도가 필요하기 때문에 중요하다. 로봇 조작기를 사용한 FFC 삽입은 복잡한 속성 모델링 없이도 자동화할 수 있는 강화 학습(RL)을 제안한다. 우리는 시뮬레이션에서 훈련을 통해 실제 환경에서의 위험을 없애고 훈련 시간을 줄이는 RL 알고리즘을 제안한다. 실험에서 우리의 방법은 제로샷 기능을 보여 실제 환경에 직접 배포할 수 있다.

## 🎯 주요 포인트

- 유연한 평평한 케이블(FFC) 삽입의 정밀도 문제 해결을 위한 RL 알고리즘 제안

- 시뮬레이션을 통한 훈련으로 실제 환경에서의 위험을 최소화하고 훈련 시간을 단축

- 시맨틱 세그멘테이션 마스크를 통한 시뮬레이션에서의 훈련과 실제 환경 전이 가능

- 인간 개입을 최소화하고 제로샷 능력을 통해 실제 환경에 직접 배포 가능

---

*Generated on 2025-09-18 17:15:00*