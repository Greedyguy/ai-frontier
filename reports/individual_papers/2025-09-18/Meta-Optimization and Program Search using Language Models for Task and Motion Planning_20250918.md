
# Meta-Optimization and Program Search using Language Models for Task and Motion Planning

**Korean Title:** 작업 및 동작 계획을 위한 언어 모델을 사용한 메타 최적화 및 프로그램 검색

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Trajectory Optimization

## 🔗 유사한 논문
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (83.4% similar)
- [[One-Step_Model_Predictive_Path_Integral_for_Manipulator_Motion_Planning_Using_Configuration_Space_Distance_Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (82.4% similar)
- [[PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models]] (81.6% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (81.5% similar)
- [[Humanoid_Agent_via_Embodied_Chain-of-Action_Reasoning_with_Multimodal_Foundation_Models_for_Zero-Shot_Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.03725v2 Announce Type: replace 
Abstract: Intelligent interaction with the real world requires robotic agents to jointly reason over high-level plans and low-level controls. Task and motion planning (TAMP) addresses this by combining symbolic planning and continuous trajectory generation. Recently, foundation model approaches to TAMP have presented impressive results, including fast planning times and the execution of natural language instructions. Yet, the optimal interface between high-level planning and low-level motion generation remains an open question: prior approaches are limited by either too much abstraction (e.g., chaining simplified skill primitives) or a lack thereof (e.g., direct joint angle prediction). Our method introduces a novel technique employing a form of meta-optimization to address these issues by: (i) using program search over trajectory optimization problems as an interface between a foundation model and robot control, and (ii) leveraging a zero-order method to optimize numerical parameters in the foundation model output. Results on challenging object manipulation and drawing tasks confirm that our proposed method improves over prior TAMP approaches.

## 🔍 Abstract (한글 번역)

arXiv:2505.03725v2 발표 유형: 대체
요약: 실제 세계와의 지능적 상호작용을 위해서는 로봇 에이전트가 고수준 계획과 저수준 제어를 함께 고려해야 합니다. 작업 및 동작 계획(Task and motion planning, TAMP)은 상징적 계획과 연속적 궤적 생성을 결합하여 이를 다룹니다. 최근 TAMP에 대한 기초 모델 접근 방식은 빠른 계획 시간과 자연어 명령의 실행을 포함한 인상적인 결과를 제시했습니다. 그러나 고수준 계획과 저수준 동작 생성 사이의 최적 인터페이스는 여전히 열린 문제입니다: 이전 접근 방식은 너무 많은 추상화(예: 단순화된 기술 기본 요소를 연결) 또는 그 부족(예: 직접적인 관절 각도 예측)으로 제한됩니다. 우리의 방법은 이러한 문제를 해결하기 위해 메타 최적화 형태를 활용하는 새로운 기술을 소개합니다: (i) 기초 모델과 로봇 제어 사이의 인터페이스로서 궤적 최적화 문제에 대한 프로그램 검색을 사용하고, (ii) 기초 모델 출력의 숫자 매개변수를 최적화하기 위해 제로 순서 방법을 활용합니다. 어려운 물체 조작 및 그림 그리기 작업에 대한 결과는 우리의 제안된 방법이 이전 TAMP 접근 방식을 개선함을 확인합니다.

## 📝 요약

로봇 에이전트가 고수준 계획과 저수준 제어를 함께 고려하여 현실 세계와 지능적 상호작용을 하는 것은 중요하다. 이를 위해 과업 및 동작 계획(Task and motion planning, TAMP)은 상징적 계획과 연속적 궤적 생성을 결합한다. 이 연구는 고수준 계획과 저수준 모션 생성 사이의 최적 인터페이스에 대한 문제를 다루었는데, 새로운 메타 최적화 기술을 도입하여 이를 해결하였다. 실험 결과는 우리의 방법이 이전 TAMP 접근법보다 성능을 향상시킨다는 것을 확인하였다.

## 🎯 주요 포인트

- 로봇 에이전트가 고수준 계획과 저수준 제어를 함께 추론해야 함

- 과제 및 모션 계획은 상징적 계획과 연속적 궤적 생성을 결합함

- 과거의 TAMP 접근 방식은 고수준 계획과 저수준 모션 생성 사이의 최적 인터페이스가 여전히 미해결 문제임

- 우리의 방법은 메타 최적화를 사용하여 이 문제를 해결함

- 우리의 제안된 방법은 이전 TAMP 접근 방식보다 개선됨

---

*Generated on 2025-09-18 17:19:00*