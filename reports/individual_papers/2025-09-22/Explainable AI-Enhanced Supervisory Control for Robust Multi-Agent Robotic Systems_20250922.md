# Explainable AI-Enhanced Supervisory Control for Robust Multi-Agent Robotic Systems

**Korean Title:** 설명 가능한 인공지능 강화 감독 제어를 통한 견고한 다중 에이전트 로봇 시스템

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Sliding Mode Controller, Timed Automata

## 🔗 유사한 논문
- [[2025-09-19/AdapJ_ An Adaptive Extended Jacobian Controller for Soft Manipulators_20250919|AdapJ An Adaptive Extended Jacobian Controller for Soft Manipulators]] (82.9% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections A Multi-Agent Reinforcement Learning Approach]] (82.0% similar)
- [[2025-09-22/MICA_ Multi-Agent Industrial Coordination Assistant_20250922|MICA Multi-Agent Industrial Coordination Assistant]] (81.8% similar)
- [[2025-09-18/ASTREA_ Introducing Agentic Intelligence for Orbital Thermal Autonomy_20250918|ASTREA Introducing Agentic Intelligence for Orbital Thermal Autonomy]] (81.5% similar)
- [[2025-09-18/Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15491v1 Announce Type: cross 
Abstract: We present an explainable AI-enhanced supervisory control framework for multi-agent robotics that combines (i) a timed-automata supervisor for safe, auditable mode switching, (ii) robust continuous control (Lyapunov-based controller for large-angle maneuver; sliding-mode controller (SMC) with boundary layers for precision and disturbance rejection), and (iii) an explainable predictor that maps mission context to gains and expected performance (energy, error). Monte Carlo-driven optimization provides the training data, enabling transparent real-time trade-offs.
  We validated the approach in two contrasting domains, spacecraft formation flying and autonomous underwater vehicles (AUVs). Despite different environments (gravity/actuator bias vs. hydrodynamic drag/currents), both share uncertain six degrees of freedom (6-DOF) rigid-body dynamics, relative motion, and tight tracking needs, making them representative of general robotic systems. In the space mission, the supervisory logic selects parameters that meet mission criteria. In AUV leader-follower tests, the same SMC structure maintains a fixed offset under stochastic currents with bounded steady error. In spacecraft validation, the SMC controller achieved submillimeter alignment with 21.7% lower tracking error and 81.4% lower energy consumption compared to Proportional-Derivative PD controller baselines. At the same time, in AUV tests, SMC maintained bounded errors under stochastic currents. These results highlight both the portability and the interpretability of the approach for safety-critical, resource-constrained multi-agent robotics.

## 🔍 Abstract (한글 번역)

arXiv:2509.15491v1 발표 유형: 교차  
초록: 우리는 다중 에이전트 로봇 공학을 위한 설명 가능한 AI 강화 감독 제어 프레임워크를 제시합니다. 이 프레임워크는 (i) 안전하고 감사 가능한 모드 전환을 위한 시간 자동자 감독자, (ii) 강력한 연속 제어(대각도 기동을 위한 Lyapunov 기반 제어기; 정밀도 및 방해 거부를 위한 경계층을 갖춘 슬라이딩 모드 제어기(SMC)), (iii) 임무 맥락을 이득과 예상 성능(에너지, 오류)으로 매핑하는 설명 가능한 예측기를 결합합니다. 몬테카를로 기반 최적화는 투명한 실시간 절충을 가능하게 하는 훈련 데이터를 제공합니다. 우리는 이 접근 방식을 서로 대조되는 두 가지 영역, 즉 우주선 편대 비행과 자율 수중 차량(AUV)에서 검증했습니다. 중력/작동기 편향 대 유체역학적 항력/해류와 같은 다른 환경에도 불구하고, 둘 다 불확실한 6자유도(6-DOF) 강체 역학, 상대 운동 및 엄격한 추적 요구 사항을 공유하여 일반적인 로봇 시스템을 대표합니다. 우주 임무에서는 감독 논리가 임무 기준을 충족하는 매개변수를 선택합니다. AUV 리더-팔로워 테스트에서는 동일한 SMC 구조가 확률적 해류 하에서 제한된 정상 상태 오류로 고정 오프셋을 유지합니다. 우주선 검증에서 SMC 제어기는 비례-미분(PD) 제어기 기준선과 비교하여 21.7% 낮은 추적 오류와 81.4% 낮은 에너지 소비로 서브밀리미터 정렬을 달성했습니다. 동시에 AUV 테스트에서는 SMC가 확률적 해류 하에서 제한된 오류를 유지했습니다. 이러한 결과는 안전이 중요한 자원 제약 다중 에이전트 로봇 공학에 대한 접근 방식의 이식성과 해석 가능성을 강조합니다.

## 📝 요약

이 논문은 다중 에이전트 로봇 시스템을 위한 설명 가능한 AI 기반 감독 제어 프레임워크를 제안합니다. 이 프레임워크는 (i) 안전하고 감사 가능한 모드 전환을 위한 시간 오토마타 감독, (ii) 강건한 연속 제어(대각도 기동을 위한 Lyapunov 기반 제어기; 정밀성과 외란 거부를 위한 슬라이딩 모드 제어기), (iii) 임무 맥락을 이득과 예상 성능(에너지, 오류)으로 매핑하는 설명 가능한 예측기로 구성됩니다. 몬테카를로 기반 최적화를 통해 훈련 데이터를 제공하여 실시간 투명한 트레이드오프를 가능하게 합니다. 이 접근법은 우주선 편대 비행과 자율 수중 차량(AUV)에서 검증되었습니다. 두 환경은 서로 다르지만, 불확실한 6자유도 강체 역학과 상대 운동, 엄격한 추적 요구를 공유하여 일반 로봇 시스템을 대표합니다. 우주 임무에서는 감독 논리가 임무 기준을 충족하는 매개변수를 선택하고, AUV 테스트에서는 동일한 SMC 구조가 확률적 전류 하에서 고정 오프셋을 유지합니다. 우주선 검증에서는 SMC 제어기가 PD 제어기 대비 21.7% 낮은 추적 오류와 81.4% 낮은 에너지 소비로 아밀리미터 이하의 정렬을 달성했습니다. AUV 테스트에서도 SMC는 확률적 전류 하에서 오류를 제한했습니다. 이러한 결과는 안전이 중요한 자원 제약 다중 에이전트 로봇 시스템에서 접근법의 이식성과 해석 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 로봇 시스템을 위한 설명 가능한 AI 기반 감독 제어 프레임워크를 제안하였습니다.

- 2. 제안된 프레임워크는 안전한 모드 전환을 위한 시간 오토마타 감독자와 강건한 연속 제어를 결합합니다.

- 3. 몬테카를로 기반 최적화를 통해 실시간 트레이드오프가 가능한 투명한 학습 데이터를 제공합니다.

- 4. 제안된 방법은 우주선 편대 비행과 자율 수중 차량(AUV)에서 검증되었으며, 두 환경 모두 불확실한 6자유도 강체 동역학을 공유합니다.

- 5. SMC 컨트롤러는 우주선 검증에서 PD 컨트롤러 대비 21.7% 낮은 추적 오류와 81.4% 낮은 에너지 소비를 달성했습니다.

---

*Generated on 2025-09-22 14:00:02*