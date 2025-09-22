
# Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning

**Korean Title:** 연속 시간 가치 반복을 통한 다중 에이전트 강화 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Continuous-Time Multi-Agent Reinforcement Learning

## 🔗 유사한 논문
- [[Multi-Fidelity_Hybrid_Reinforcement_Learning_via_Information_Gain_Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (83.0% similar)
- [[Scalable_Multi-Objective_Robot_Reinforcement_Learning_through_Gradient_Conflict_Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.5% similar)
- [[Process-Supervised_Reinforcement_Learning_for_Interactive_Multimodal_Tool-Use_Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (82.3% similar)
- [[Vulnerable_Agent_Identification_in_Large-Scale_Multi-Agent_Reinforcement_Learning_20250919|Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning]] (82.0% similar)
- [[Resolve_Highway_Conflict_in_Multi-Autonomous_Vehicle_Controls_with_Local_State_Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09135v2 Announce Type: replace 
Abstract: Existing reinforcement learning (RL) methods struggle with complex dynamical systems that demand interactions at high frequencies or irregular time intervals. Continuous-time RL (CTRL) has emerged as a promising alternative by replacing discrete-time Bellman recursion with differential value functions defined as viscosity solutions of the Hamilton--Jacobi--Bellman (HJB) equation. While CTRL has shown promise, its applications have been largely limited to the single-agent domain. This limitation stems from two key challenges: (i) conventional solution methods for HJB equations suffer from the curse of dimensionality (CoD), making them intractable in high-dimensional systems; and (ii) even with HJB-based learning approaches, accurately approximating centralized value functions in multi-agent settings remains difficult, which in turn destabilizes policy training. In this paper, we propose a CT-MARL framework that uses physics-informed neural networks (PINNs) to approximate HJB-based value functions at scale. To ensure the value is consistent with its differential structure, we align value learning with value-gradient learning by introducing a Value Gradient Iteration (VGI) module that iteratively refines value gradients along trajectories. This improves gradient fidelity, in turn yielding more accurate values and stronger policy learning. We evaluate our method using continuous-time variants of standard benchmarks, including multi-agent particle environment (MPE) and multi-agent MuJoCo. Our results demonstrate that our approach consistently outperforms existing continuous-time RL baselines and scales to complex multi-agent dynamics.

## 🔍 Abstract (한글 번역)

arXiv:2509.09135v2 발표 유형: 교체  
초록: 기존의 강화 학습(RL) 방법은 높은 빈도 또는 불규칙한 시간 간격에서의 상호작용을 요구하는 복잡한 동적 시스템에서 어려움을 겪습니다. 연속 시간 강화 학습(CTRL)은 이산 시간 벨만 재귀를 해밀턴-자코비-벨만(HJB) 방정식의 점성 해로 정의된 미분 가치 함수로 대체하여 유망한 대안으로 부상했습니다. CTRL은 가능성을 보여주었지만, 그 응용은 주로 단일 에이전트 분야에 국한되어 있었습니다. 이러한 제한은 두 가지 주요 도전 과제에서 비롯됩니다: (i) HJB 방정식의 기존 해결 방법은 차원의 저주(CoD)로 인해 고차원 시스템에서 다루기 어렵고; (ii) HJB 기반 학습 접근법을 사용하더라도, 다중 에이전트 설정에서 중앙 집중식 가치 함수를 정확하게 근사화하는 것이 여전히 어려워 정책 학습을 불안정하게 만듭니다. 본 논문에서는 물리 정보 신경망(PINNs)을 사용하여 대규모로 HJB 기반 가치 함수를 근사화하는 CT-MARL 프레임워크를 제안합니다. 가치가 그 미분 구조와 일치하도록 하기 위해, 우리는 가치 학습을 가치-기울기 학습과 정렬하여 경로를 따라 가치 기울기를 반복적으로 정제하는 가치 기울기 반복(VGI) 모듈을 도입합니다. 이는 기울기 충실도를 향상시켜, 보다 정확한 가치와 강력한 정책 학습을 제공합니다. 우리는 다중 에이전트 입자 환경(MPE) 및 다중 에이전트 MuJoCo를 포함한 표준 벤치마크의 연속 시간 변형을 사용하여 우리의 방법을 평가합니다. 우리의 결과는 우리의 접근 방식이 기존의 연속 시간 RL 기준선을 일관되게 능가하며 복잡한 다중 에이전트 동적 시스템에 확장 가능함을 보여줍니다.

## 📝 요약

이 논문은 복잡한 동적 시스템에서 기존 강화 학습(RL) 방법의 한계를 극복하기 위해 연속 시간 강화 학습(CTRL)을 제안합니다. CTRL은 불규칙한 시간 간격의 상호작용을 처리하기 위해 해밀턴-자코비-벨만(HJB) 방정식의 점성 해로 정의된 미분 가치 함수를 사용합니다. 그러나 CTRL의 응용은 주로 단일 에이전트에 국한되었으며, 이는 고차원 시스템에서 차원의 저주(CoD)와 다중 에이전트 환경에서의 중앙 집중식 가치 함수 근사화의 어려움 때문입니다. 본 논문에서는 물리 기반 신경망(PINNs)을 활용하여 HJB 기반 가치 함수를 대규모로 근사화하는 CT-MARL 프레임워크를 제안합니다. 가치 학습과 가치-기울기 학습을 정렬하여 가치 기울기를 반복적으로 개선하는 Value Gradient Iteration(VGI) 모듈을 도입하여 더 정확한 가치와 강력한 정책 학습을 가능하게 합니다. 실험 결과, 제안된 방법은 기존 연속 시간 RL 기법을 능가하며 복잡한 다중 에이전트 동적 시스템에 확장 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존 강화 학습 방법은 높은 빈도나 불규칙한 시간 간격의 상호작용이 필요한 복잡한 동적 시스템에서 어려움을 겪습니다.

- 2. 연속 시간 강화 학습(CTRL)은 해밀턴-자코비-벨만(HJB) 방정식의 점성 해로 정의된 미분 가치 함수를 사용하여 유망한 대안으로 부상했습니다.

- 3. CTRL의 응용은 단일 에이전트 도메인에 주로 제한되었으며, 이는 차원의 저주(CoD)와 다중 에이전트 환경에서의 중앙 집중식 가치 함수 근사화의 어려움 때문입니다.

- 4. 본 논문에서는 물리 정보 신경망(PINNs)을 사용하여 HJB 기반 가치 함수를 대규모로 근사화하는 CT-MARL 프레임워크를 제안합니다.

- 5. 제안된 방법은 연속 시간 변형 표준 벤치마크에서 기존 연속 시간 강화 학습 기준을 일관되게 능가하고 복잡한 다중 에이전트 역학에 확장됩니다.

---

*Generated on 2025-09-19 15:40:57*