# Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection

**Korean Title:** 대형 언어 모델 기반 의사 결정 변환기를 활용한 UAV 지원 데이터 수집

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Zhixion Chen|Zhixion Chen]] [[authors/Jiangzhou Wang|Jiangzhou Wang]] [[authors/and Hyundong Shin|and Hyundong Shin]] [[authors/Arumugam Nallanathan|Arumugam Nallanathan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Trajectory Optimization, Resource Allocation

## 🔗 유사한 논문
- [[Reinforcement Learning for Autonomous Point-to-Point UAV Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (85.4% similar)
- [[Agentic UAVs_ LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning_20250918|Agentic UAVs LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning]] (84.0% similar)
- [[SPAR_ Scalable LLM-based PDDL Domain Generation for Aerial Robotics_20250918|SPAR Scalable LLM-based PDDL Domain Generation for Aerial Robotics]] (82.5% similar)
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (81.6% similar)
- [[Language Conditioning Improves Accuracy of Aircraft Goal Prediction in Untowered Airspace_20250918|Language Conditioning Improves Accuracy of Aircraft Goal Prediction in Untowered Airspace]] (81.3% similar)

## 📋 저자 정보

**Authors:** Zhixion Chen, Jiangzhou Wang, and Hyundong Shin, Arumugam Nallanathan

## 📄 Abstract (원문)

The deployment of unmanned aerial vehicles (UAVs) for reliable and
energy-efficient data collection from spatially distributed devices holds great
promise in supporting diverse Internet of Things (IoT) applications.
Nevertheless, the limited endurance and communication range of UAVs necessitate
intelligent trajectory planning. While reinforcement learning (RL) has been
extensively explored for UAV trajectory optimization, its interactive nature
entails high costs and risks in real-world environments. Offline RL mitigates
these issues but remains susceptible to unstable training and heavily rely on
expert-quality datasets. To address these challenges, we formulate a joint UAV
trajectory planning and resource allocation problem to maximize energy
efficiency of data collection. The resource allocation subproblem is first
transformed into an equivalent linear programming formulation and solved
optimally with polynomial-time complexity. Then, we propose a large language
model (LLM)-empowered critic-regularized decision transformer (DT) framework,
termed LLM-CRDT, to learn effective UAV control policies. In LLM-CRDT, we
incorporate critic networks to regularize the DT model training, thereby
integrating the sequence modeling capabilities of DT with critic-based value
guidance to enable learning effective policies from suboptimal datasets.
Furthermore, to mitigate the data-hungry nature of transformer models, we
employ a pre-trained LLM as the transformer backbone of the DT model and adopt
a parameter-efficient fine-tuning strategy, i.e., LoRA, enabling rapid
adaptation to UAV control tasks with small-scale dataset and low computational
overhead. Extensive simulations demonstrate that LLM-CRDT outperforms benchmark
online and offline RL methods, achieving up to 36.7\% higher energy efficiency
than the current state-of-the-art DT approaches.

## 🔍 Abstract (한글 번역)

무인 항공기(UAV)를 활용한 공간적으로 분산된 장치로부터의 신뢰성 있고 에너지 효율적인 데이터 수집은 다양한 사물인터넷(IoT) 응용 프로그램을 지원하는 데 큰 가능성을 제공합니다. 그러나 UAV의 제한된 지속 시간과 통신 범위는 지능적인 경로 계획을 필요로 합니다. 강화 학습(RL)은 UAV 경로 최적화를 위해 광범위하게 탐구되었지만, 그 상호작용적 특성은 실제 환경에서 높은 비용과 위험을 수반합니다. 오프라인 RL은 이러한 문제를 완화하지만 불안정한 학습에 취약하며 전문가 수준의 데이터셋에 크게 의존합니다. 이러한 도전 과제를 해결하기 위해, 우리는 데이터 수집의 에너지 효율성을 극대화하기 위한 UAV 경로 계획과 자원 할당 문제를 공동으로 수립합니다. 자원 할당 하위 문제는 먼저 동등한 선형 프로그래밍 공식으로 변환되어 다항 시간 복잡도로 최적 해결됩니다. 그런 다음, 우리는 LLM-CRDT라고 불리는 대형 언어 모델(LLM) 기반의 비평가-정규화 결정 변환기(DT) 프레임워크를 제안하여 효과적인 UAV 제어 정책을 학습합니다. LLM-CRDT에서는 비평가 네트워크를 통합하여 DT 모델 학습을 정규화함으로써, DT의 시퀀스 모델링 기능과 비평가 기반의 가치 지침을 결합하여 비최적 데이터셋으로부터 효과적인 정책을 학습할 수 있도록 합니다. 또한, 변환기 모델의 데이터 의존성을 완화하기 위해 사전 학습된 LLM을 DT 모델의 변환기 백본으로 사용하고, 소규모 데이터셋과 낮은 계산 오버헤드로 UAV 제어 작업에 빠르게 적응할 수 있도록 매개변수 효율적인 미세 조정 전략, 즉 LoRA를 채택합니다. 광범위한 시뮬레이션 결과, LLM-CRDT는 벤치마크 온라인 및 오프라인 RL 방법을 능가하며, 현재 최첨단 DT 접근 방식보다 최대 36.7% 높은 에너지 효율성을 달성함을 보여줍니다.

## 📝 요약

이 논문은 무인 항공기(UAV)를 활용한 에너지 효율적인 데이터 수집을 위한 경로 계획 문제를 다룹니다. 기존 강화 학습(RL)의 한계를 극복하기 위해, 저자들은 UAV 경로 계획과 자원 할당 문제를 통합하여 에너지 효율을 극대화하는 방법을 제안합니다. 자원 할당 문제는 선형 프로그래밍으로 변환하여 최적 해결하고, LLM-CRDT라는 새로운 프레임워크를 통해 UAV 제어 정책을 학습합니다. 이 프레임워크는 대형 언어 모델(LLM)을 활용하여 데이터 부족 문제를 해결하고, LoRA 기법을 통해 소규모 데이터셋에서도 빠른 적응을 가능하게 합니다. 시뮬레이션 결과, LLM-CRDT는 기존 방법들보다 최대 36.7% 높은 에너지 효율을 달성했습니다.

## 🎯 주요 포인트

- 1. 무인 항공기(UAV)의 제한된 지속성과 통신 범위를 극복하기 위해 지능적인 경로 계획이 필요합니다.

- 2. 오프라인 강화 학습(RL)은 UAV 경로 최적화의 비용과 위험을 줄이지만 불안정한 훈련과 전문가 수준 데이터셋에 대한 의존성이 문제입니다.

- 3. UAV의 에너지 효율적인 데이터 수집을 극대화하기 위해 경로 계획과 자원 할당 문제를 공동으로 해결합니다.

- 4. LLM-CRDT 프레임워크는 대규모 언어 모델(LLM)을 활용하여 UAV 제어 정책을 효과적으로 학습하며, 비판 네트워크를 통합하여 불완전한 데이터셋에서도 효과적인 정책 학습을 가능하게 합니다.

- 5. 사전 훈련된 LLM을 사용하여 데이터가 많이 필요한 변환기 모델의 한계를 극복하고, LoRA 전략을 통해 소규모 데이터셋으로 신속한 UAV 제어 작업 적응을 실현합니다.

---

*Generated on 2025-09-20 09:22:51*