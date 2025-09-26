---
keywords:
  - Reinforcement Learning
  - Model Predictive Path Integral
  - Autonomous Drone Racing
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14726
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:26:54.483299",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Model Predictive Path Integral",
    "Autonomous Drone Racing"
  ],
  "rejected_keywords": [
    "Trajectory Tracking"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Model Predictive Path Integral": 0.78,
    "Autonomous Drone Racing": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Rethinking Reference Trajectories in Agile Drone Racing: A Unified Reference-Free Model-Based Controller via MPPI

**Korean Title:** 애자일 드론 레이싱에서 참조 궤적 재고: MPPI를 통한 통일된 참조 없는 모델 기반 제어기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Model Predictive Path Integral|Model Predictive Path Integral]], [[keywords/Autonomous Drone Racing|Autonomous Drone Racing]]

## 🔗 유사한 논문
- [[One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (82.6% similar)
- [[Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (81.4% similar)
- [[FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (80.9% similar)
- [[Reinforcement Learning for Autonomous Point-to-Point UAV Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (80.7% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14726v1 Announce Type: new 
Abstract: While model-based controllers have demonstrated remarkable performance in autonomous drone racing, their performance is often constrained by the reliance on pre-computed reference trajectories. Conventional approaches, such as trajectory tracking, demand a dynamically feasible, full-state reference, whereas contouring control relaxes this requirement to a geometric path but still necessitates a reference. Recent advancements in reinforcement learning (RL) have revealed that many model-based controllers optimize surrogate objectives, such as trajectory tracking, rather than the primary racing goal of directly maximizing progress through gates. Inspired by these findings, this work introduces a reference-free method for time-optimal racing by incorporating this gate progress objective, derived from RL reward shaping, directly into the Model Predictive Path Integral (MPPI) formulation. The sampling-based nature of MPPI makes it uniquely capable of optimizing the discontinuous and non-differentiable objective in real-time. We also establish a unified framework that leverages MPPI to systematically and fairly compare three distinct objective functions with a consistent dynamics model and parameter set: classical trajectory tracking, contouring control, and the proposed gate progress objective. We compare the performance of these three objectives when solved via both MPPI and a traditional gradient-based solver. Our results demonstrate that the proposed reference-free approach achieves competitive racing performance, rivaling or exceeding reference-based methods. Videos are available at https://zhaofangguo.github.io/racing_mppi/

## 🔍 Abstract (한글 번역)

arXiv:2509.14726v1 발표 유형: 신규  
초록: 모델 기반 제어기는 자율 드론 레이싱에서 놀라운 성능을 보여주었지만, 그 성능은 종종 사전 계산된 참조 궤적에 의존함으로써 제한됩니다. 궤적 추적과 같은 전통적인 접근 방식은 동적으로 실현 가능한 전체 상태 참조를 요구하는 반면, 컨투어링 제어는 이 요구 사항을 기하학적 경로로 완화하지만 여전히 참조가 필요합니다. 강화 학습(RL)의 최근 발전은 많은 모델 기반 제어기가 궤적 추적과 같은 대리 목표를 최적화하며, 게이트를 통한 진행을 직접 최대화하는 주요 레이싱 목표와는 다르다는 것을 밝혀냈습니다. 이러한 발견에 영감을 받아, 본 연구는 RL 보상 형성에서 파생된 게이트 진행 목표를 Model Predictive Path Integral (MPPI) 공식에 직접 통합하여 시간 최적의 레이싱을 위한 참조 없는 방법을 소개합니다. MPPI의 샘플링 기반 특성은 비연속적이고 비미분 가능한 목표를 실시간으로 최적화하는 데 독특한 능력을 제공합니다. 우리는 또한 MPPI를 활용하여 일관된 동역학 모델과 매개변수 세트를 사용하여 세 가지 서로 다른 목표 함수(고전적 궤적 추적, 컨투어링 제어, 제안된 게이트 진행 목표)를 체계적이고 공정하게 비교하는 통합 프레임워크를 확립합니다. 우리는 MPPI와 전통적인 기울기 기반 해석기를 통해 해결된 세 가지 목표의 성능을 비교합니다. 우리의 결과는 제안된 참조 없는 접근 방식이 참조 기반 방법과 경쟁하거나 그 이상의 레이싱 성능을 달성함을 보여줍니다. 비디오는 https://zhaofangguo.github.io/racing_mppi/에서 확인할 수 있습니다.

## 📝 요약

이 논문은 자율 드론 레이싱에서 기존의 경로 추적 방식이 사전 계산된 참조 경로에 의존하여 성능이 제한된다는 문제를 해결하고자 합니다. 이를 위해 강화 학습에서 영감을 받아, 참조 경로 없이 게이트 통과를 최대화하는 목표를 Model Predictive Path Integral (MPPI) 방법에 직접 통합한 새로운 방법을 제안합니다. MPPI의 샘플링 기반 특성은 비연속적이고 비미분 가능한 목표를 실시간으로 최적화하는 데 적합합니다. 또한, MPPI를 활용하여 전통적인 경로 추적, 윤곽 제어, 제안된 게이트 진행 목표의 성능을 공정하게 비교할 수 있는 통합 프레임워크를 구축했습니다. 실험 결과, 제안된 방법이 기존의 참조 기반 방법과 비슷하거나 더 나은 성능을 보임을 확인했습니다.

## 🎯 주요 포인트

- 1. 기존의 모델 기반 컨트롤러는 사전 계산된 참조 궤적에 의존하여 성능이 제한됩니다.

- 2. 최근 강화 학습(RL) 연구는 모델 기반 컨트롤러가 주로 궤적 추적과 같은 대리 목표를 최적화한다는 것을 보여줍니다.

- 3. 본 연구는 RL 보상 형성에서 파생된 게이트 진행 목표를 MPPI에 직접 통합하여 참조 없이 시간 최적의 레이싱을 구현합니다.

- 4. MPPI의 샘플링 기반 특성은 비연속적이고 비미분 가능한 목표를 실시간으로 최적화하는 데 적합합니다.

- 5. 제안된 참조 없는 접근 방식은 기존의 참조 기반 방법과 경쟁할 수 있는 레이싱 성능을 달성합니다.

---

*Generated on 2025-09-19 16:32:33*