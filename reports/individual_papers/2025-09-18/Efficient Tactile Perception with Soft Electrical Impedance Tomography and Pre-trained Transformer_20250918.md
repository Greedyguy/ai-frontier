
# Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer

**Korean Title:** 부드러운 전기 임피던스 단층촬영 및 사전 훈련된 트랜스포머를 활용한 효율적인 촉각 지각.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Tactile sensing

## 🔗 유사한 논문
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (82.1% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (79.8% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (79.5% similar)
- [[PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models]] (79.5% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02824v2 Announce Type: replace 
Abstract: Tactile sensing is fundamental to robotic systems, enabling interactions through physical contact in multiple tasks. Despite its importance, achieving high-resolution, large-area tactile sensing remains challenging. Electrical Impedance Tomography (EIT) has emerged as a promising approach for large-area, distributed tactile sensing with minimal electrode requirements which can lend itself to addressing complex contact problems in robotics. However, existing EIT-based tactile reconstruction methods often suffer from high computational costs or depend on extensive annotated simulation datasets, hindering its viability in real-world settings. To address this shortcoming, here we propose a Pre-trained Transformer for EIT-based Tactile Reconstruction (PTET), a learning-based framework that bridges the simulation-to-reality gap by leveraging self-supervised pretraining on simulation data and fine-tuning with limited real-world data. In simulations, PTET requires 99.44 percent fewer annotated samples than equivalent state-of-the-art approaches (2,500 vs. 450,000 samples) while achieving reconstruction performance improvements of up to 43.57 percent under identical data conditions. Fine-tuning with real-world data further enables PTET to overcome discrepancies between simulated and experimental datasets, achieving superior reconstruction and detail recovery in practical scenarios. The improved reconstruction accuracy, data efficiency, and robustness in real-world tasks establish it as a scalable and practical solution for tactile sensing systems in robotics, especially for object handling and adaptive grasping under varying pressure conditions.

## 🔍 Abstract (한글 번역)

arXiv:2506.02824v2 발표 유형: 대체
요약: 촉각 감지는 로봇 시스템에서 기본적이며, 여러 작업에서 물리적 접촉을 통한 상호 작용을 가능하게 합니다. 그러나 고해상도 및 대면적 촉각 감지를 달성하는 것은 여전히 어려운 과제입니다. 전기 임피던스 단층촬영(EIT)은 최소한의 전극 요구 사항을 가진 대면적 분산 촉각 감지에 대한 유망한 접근 방식으로 등장했으며, 로봇 과제에서 복잡한 접촉 문제를 해결하는 데 도움이 될 수 있습니다. 그러나 기존의 EIT 기반 촉각 재구성 방법은 종종 높은 계산 비용을 지니거나 방대한 주석이 달린 시뮬레이션 데이터셋에 의존하여 현실 세팅에서의 적용 가능성을 방해합니다. 이러한 결점을 해결하기 위해 본 연구에서는 EIT 기반 촉각 재구성을 위한 사전 훈련된 트랜스포머(PTET)를 제안합니다. 이는 시뮬레이션 데이터에서의 자기 감독 사전 훈련을 활용하고 제한된 현실 데이터로 세밀 조정하여 시뮬레이션과 현실 간의 간극을 줄이는 학습 기반 프레임워크입니다. 시뮬레이션에서 PTET는 동일한 데이터 조건 하에서 동등한 최첨단 접근 방식보다 99.44% 적은 주석이 달린 샘플(2,500 대 450,000 샘플)을 필요로 하며, 재구성 성능을 최대 43.57% 향상시킵니다. 현실 데이터로 세밀 조정함으로써 PTET는 시뮬레이션과 실험 데이터셋 간의 불일치를 극복하여 실용적 시나리오에서 우수한 재구성 및 세부 복원을 달성합니다. 실제 과제에서의 향상된 재구성 정확도, 데이터 효율성 및 강건성은 이를 로봇학의 촉각 감지 시스템에 대한 확장 가능하고 실용적인 솔루션으로 확립시킵니다, 특히 다양한 압력 조건 하에서의 물체 처리 및 적응적 쥐기에 적합합니다.

## 📝 요약

로봇 시스템에서의 촉각 감지는 물리적 접촉을 통해 상호작용을 가능케 하며 여러 작업에 필수적이다. 그러나 고해상도 대면적의 촉각 감지를 달성하는 것은 여전히 어렵다. 전기 임피던스 단층촬영(EIT)은 소규모 전극 요구사항으로 대면적 분산 촉각 감지에 유망한 접근법으로 등장했다. 본 논문에서는 시뮬레이션 데이터에 대한 자가지도 사전학습을 활용하고 제한된 실제 데이터로 세밀조정하는 학습 기반 프레임워크인 PTET을 제안한다. PTET은 동일한 데이터 조건 하에서 최대 43.57%의 재구성 성능 향상을 달성하면서 상태-of-the-art 접근법보다 99.44% 적은 주석이 달린 샘플(2,500 vs. 450,000 샘플)을 필요로 한다. 실제 데이터로 세밀조정함으로써 PTET은 시뮬레이션과 실험 데이터 간의 불일치를 극복하며 실용적인 시나리오에서 우수한 재구성과 세부 복구를 달성한다. 이는 로봇학에서 물체 처리와 다양한 압력 조건 하에서의 적응적인 움켜쥠에 특히 유용한 촉각 감지 시스템의 확장 가능하고 실용적인 솔루션으로 자리매김한다.

## 🎯 주요 포인트

- 로봇 시스템에서 중요한 접촉 상호작용을 가능하게 하는 고해상도 대면적 촉각 감지는 여전히 어려움

- 전기 임피던스 단층촬영(EIT)은 적은 전극 요구 사항으로 대면적 분산 촉각 감지에 유망한 접근 방식으로 부상

- PTET는 시뮬레이션 데이터에 대한 자가지도 사전 훈련을 활용하고 제한된 실제 데이터로 세밀 조정하여 재구성 성능을 향상

- PTET는 현실 세계에서 뛰어난 재구성 및 세부 복구 능력을 갖추어 로봇학의 촉각 감지 시스템에 실용적인 해결책으로 자리매김함.

---

*Generated on 2025-09-18 17:19:35*