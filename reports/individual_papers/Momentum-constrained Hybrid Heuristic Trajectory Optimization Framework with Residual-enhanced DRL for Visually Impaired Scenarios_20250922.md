# Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios

**Korean Title:** 모멘텀 제약 하이브리드 휴리스틱 궤적 최적화 프레임워크와 잔여 강화 심층 강화 학습을 통한 시각 장애 시나리오 대응

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Residual-enhanced DRL

## 🔗 유사한 논문
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.2% similar)
- [[2025-09-19/PA-MPPI_ Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments_20250919|PA-MPPI Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments]] (81.8% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (81.4% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (81.1% similar)
- [[2025-09-18/Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15582v1 Announce Type: cross 
Abstract: This paper proposes a momentum-constrained hybrid heuristic trajectory optimization framework (MHHTOF) tailored for assistive navigation in visually impaired scenarios, integrating trajectory sampling generation, optimization and evaluation with residual-enhanced deep reinforcement learning (DRL). In the first stage, heuristic trajectory sampling cluster (HTSC) is generated in the Frenet coordinate system using third-order interpolation with fifth-order polynomials and momentum-constrained trajectory optimization (MTO) constraints to ensure smoothness and feasibility. After first stage cost evaluation, the second stage leverages a residual-enhanced actor-critic network with LSTM-based temporal feature modeling to adaptively refine trajectory selection in the Cartesian coordinate system. A dual-stage cost modeling mechanism (DCMM) with weight transfer aligns semantic priorities across stages, supporting human-centered optimization. Experimental results demonstrate that the proposed LSTM-ResB-PPO achieves significantly faster convergence, attaining stable policy performance in approximately half the training iterations required by the PPO baseline, while simultaneously enhancing both reward outcomes and training stability. Compared to baseline method, the selected model reduces average cost and cost variance by 30.3% and 53.3%, and lowers ego and obstacle risks by over 77%. These findings validate the framework's effectiveness in enhancing robustness, safety, and real-time feasibility in complex assistive planning tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15582v1 발표 유형: 교차  
초록: 본 논문은 시각 장애인 시나리오에서의 보조 내비게이션을 위해 모멘텀 제약 하이브리드 휴리스틱 궤적 최적화 프레임워크(MHHTOF)를 제안하며, 궤적 샘플링 생성, 최적화 및 평가를 잔차 강화 심층 학습(DRL)과 통합합니다. 첫 번째 단계에서는 프레네 좌표계에서 5차 다항식을 사용한 3차 보간과 모멘텀 제약 궤적 최적화(MTO) 제약을 통해 휴리스틱 궤적 샘플링 클러스터(HTSC)를 생성하여 부드러움과 실행 가능성을 보장합니다. 첫 번째 단계의 비용 평가 후, 두 번째 단계에서는 LSTM 기반의 시간적 특징 모델링을 갖춘 잔차 강화 액터-크리틱 네트워크를 활용하여 데카르트 좌표계에서 궤적 선택을 적응적으로 개선합니다. 가중치 전이를 통한 이중 단계 비용 모델링 메커니즘(DCMM)은 단계 간 의미적 우선순위를 정렬하여 인간 중심의 최적화를 지원합니다. 실험 결과에 따르면, 제안된 LSTM-ResB-PPO는 PPO 기준선이 요구하는 훈련 반복 횟수의 절반 정도에서 안정적인 정책 성능을 달성하며, 보상 결과와 훈련 안정성을 동시에 향상시킵니다. 기준 방법과 비교할 때, 선택된 모델은 평균 비용과 비용 변동성을 각각 30.3% 및 53.3% 감소시키고, 자아 및 장애물 위험을 77% 이상 줄입니다. 이러한 결과는 복잡한 보조 계획 작업에서 프레임워크의 견고성, 안전성 및 실시간 실행 가능성을 향상시키는 데 있어 효과적임을 입증합니다.

## 📝 요약

이 논문은 시각 장애인을 위한 보조 내비게이션에 적합한 모멘텀 제약 하이브리드 휴리스틱 경로 최적화 프레임워크(MHHTOF)를 제안합니다. 이 프레임워크는 경로 샘플 생성, 최적화 및 평가를 잔차 강화 학습(DRL)과 통합합니다. 첫 번째 단계에서는 프레네 좌표계에서 5차 다항식과 모멘텀 제약 경로 최적화(MTO) 제약을 사용하여 휴리스틱 경로 샘플링 클러스터(HTSC)를 생성합니다. 두 번째 단계에서는 LSTM 기반의 잔차 강화 액터-크리틱 네트워크를 활용하여 경로 선택을 적응적으로 개선합니다. 실험 결과, 제안된 LSTM-ResB-PPO는 PPO 기준보다 약 절반의 훈련 반복으로 안정적인 정책 성능을 달성하며, 보상 결과와 훈련 안정성을 향상시킵니다. 또한, 평균 비용과 비용 변동성을 각각 30.3%와 53.3% 줄이고, 자아 및 장애물 위험을 77% 이상 감소시킵니다. 이러한 결과는 복잡한 보조 계획 작업에서 프레임워크의 효과성을 입증합니다.

## 🎯 주요 포인트

- 1. 이 논문은 시각 장애인을 위한 보조 내비게이션에 적합한 모멘텀 제약 하이브리드 휴리스틱 경로 최적화 프레임워크(MHHTOF)를 제안합니다.

- 2. 첫 번째 단계에서는 프레네 좌표계에서 3차 보간법과 5차 다항식, 모멘텀 제약 경로 최적화(MTO) 제약을 사용하여 휴리스틱 경로 샘플링 클러스터(HTSC)를 생성합니다.

- 3. 두 번째 단계에서는 잔차 강화된 액터-크리틱 네트워크와 LSTM 기반의 시간적 특징 모델링을 활용하여 경로 선택을 적응적으로 개선합니다.

- 4. 제안된 LSTM-ResB-PPO는 PPO 기준선보다 약 절반의 훈련 반복에서 안정적인 정책 성능을 달성하며, 보상 결과와 훈련 안정성을 동시에 향상시킵니다.

- 5. 실험 결과, 제안된 모델은 평균 비용과 비용 변동성을 각각 30.3%와 53.3% 감소시키고, 자아 및 장애물 위험을 77% 이상 낮춥니다.

---

*Generated on 2025-09-22 14:04:34*