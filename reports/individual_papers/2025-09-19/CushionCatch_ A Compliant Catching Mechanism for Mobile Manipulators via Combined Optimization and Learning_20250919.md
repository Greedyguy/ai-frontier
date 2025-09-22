
# CushionCatch: A Compliant Catching Mechanism for Mobile Manipulators via Combined Optimization and Learning

**Korean Title:** CushionCatch: 최적화와 학습을 결합한 이동 매니퓰레이터를 위한 유연한 포획 메커니즘

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: LSTM, Optimization

## 🔗 유사한 논문
- [[ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (83.1% similar)
- [[M4Diffuser Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (82.8% similar)
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (82.6% similar)
- [[One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (81.9% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.14754v4 Announce Type: replace 
Abstract: Catching flying objects with a cushioning process is a skill commonly performed by humans, yet it remains a significant challenge for robots. In this paper, we present a framework that combines optimization and learning to achieve compliant catching on mobile manipulators (CCMM). First, we propose a high-level capture planner for mobile manipulators (MM) that calculates the optimal capture point and joint configuration. Next, the pre-catching (PRC) planner ensures the robot reaches the target joint configuration as quickly as possible. To learn compliant catching strategies, we propose a network that leverages the strengths of LSTM for capturing temporal dependencies and positional encoding for spatial context (P-LSTM). This network is designed to effectively learn compliant strategies from human demonstrations. Following this, the post-catching (POC) planner tracks the compliant sequence output by the P-LSTM while avoiding potential collisions due to structural differences between humans and robots. We validate the CCMM framework through both simulated and real-world ball-catching scenarios, achieving a success rate of 98.70% in simulation, 92.59% in real-world tests, and a 28.7% reduction in impact torques. The open source code has be released for the reference of the community.

## 🔍 Abstract (한글 번역)

arXiv:2409.14754v4 발표 유형: 교체  
초록: 쿠션 과정을 통해 비행 물체를 잡는 것은 인간이 흔히 수행하는 기술이지만, 로봇에게는 여전히 중요한 도전 과제입니다. 본 논문에서는 이동 매니퓰레이터에서 유연한 포획을 달성하기 위해 최적화와 학습을 결합한 프레임워크를 제시합니다 (CCMM). 먼저, 이동 매니퓰레이터(MM)를 위한 고수준 포획 계획자를 제안하여 최적의 포획 지점과 관절 구성을 계산합니다. 다음으로, 사전 포획(PRC) 계획자는 로봇이 목표 관절 구성에 최대한 빨리 도달하도록 보장합니다. 유연한 포획 전략을 학습하기 위해, 우리는 LSTM의 시간적 의존성 포착 강점과 공간적 맥락을 위한 위치 인코딩을 활용하는 네트워크(P-LSTM)를 제안합니다. 이 네트워크는 인간의 시연으로부터 유연한 전략을 효과적으로 학습하도록 설계되었습니다. 이후, 포획 후(POC) 계획자는 인간과 로봇 간의 구조적 차이로 인한 잠재적 충돌을 피하면서 P-LSTM이 출력한 유연한 시퀀스를 추적합니다. 우리는 시뮬레이션과 실제 공 잡기 시나리오 모두에서 CCMM 프레임워크를 검증하였으며, 시뮬레이션에서 98.70%, 실제 테스트에서 92.59%의 성공률과 충격 토크의 28.7% 감소를 달성했습니다. 커뮤니티의 참고를 위해 오픈 소스 코드가 공개되었습니다.

## 📝 요약

이 논문은 로봇이 비행 물체를 잡는 기술을 개선하기 위한 최적화와 학습을 결합한 프레임워크(CCMM)를 제안합니다. 주요 기여는 모바일 매니퓰레이터(MM)를 위한 최적 캡처 지점과 관절 구성을 계산하는 캡처 플래너와 목표 관절 구성을 빠르게 도달하는 사전 캡처(Pre-catching) 플래너입니다. 또한, 인간의 시연을 통해 순응적 잡기 전략을 학습하는 P-LSTM 네트워크를 제안합니다. 이 네트워크는 LSTM과 위치 인코딩을 활용하여 시간적 의존성과 공간적 맥락을 효과적으로 학습합니다. 이후, 포스트 캡처(Post-catching) 플래너는 P-LSTM의 순응적 시퀀스를 추적하며 충돌을 피합니다. 시뮬레이션과 실제 실험에서 각각 98.70%와 92.59%의 성공률을 기록했으며, 충격 토크를 28.7% 감소시켰습니다. 연구 결과는 오픈 소스로 공개되었습니다.

## 🎯 주요 포인트

- 1. 이 논문은 최적화와 학습을 결합하여 모바일 매니퓰레이터에서 유연한 물체 잡기를 구현하는 프레임워크를 제안합니다.

- 2. 제안된 프레임워크는 최적의 포획 지점과 관절 구성을 계산하는 고수준 캡처 계획자와 목표 관절 구성에 신속히 도달하는 사전 포획 계획자를 포함합니다.

- 3. 인간의 시연에서 유연한 잡기 전략을 학습하기 위해 LSTM과 위치 인코딩을 활용한 네트워크(P-LSTM)를 제안합니다.

- 4. 제안된 CCMM 프레임워크는 시뮬레이션에서 98.70%, 실제 테스트에서 92.59%의 성공률을 달성했으며, 충격 토크를 28.7% 감소시켰습니다.

- 5. 이 연구의 오픈 소스 코드는 커뮤니티의 참조를 위해 공개되었습니다.

---

*Generated on 2025-09-19 16:37:32*