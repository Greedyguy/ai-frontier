
# Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning

**Korean Title:** 교통 공동 시뮬레이션 프레임워크: 인프라 카메라 센싱과 강화 학습의 활용

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Signal Control

## 🔗 유사한 논문
- [[Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (84.6% similar)
- [[LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (83.4% similar)
- [[MetaTrading An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (82.2% similar)
- [[An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (82.1% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.03925v2 Announce Type: replace-cross 
Abstract: Traffic simulations are commonly used to optimize urban traffic flow, with reinforcement learning (RL) showing promising potential for automated traffic signal control, particularly in intelligent transportation systems involving connected automated vehicles. Multi-agent reinforcement learning (MARL) is particularly effective for learning control strategies for traffic lights in a network using iterative simulations. However, existing methods often assume perfect vehicle detection, which overlooks real-world limitations related to infrastructure availability and sensor reliability. This study proposes a co-simulation framework integrating CARLA and SUMO, which combines high-fidelity 3D modeling with large-scale traffic flow simulation. Cameras mounted on traffic light poles within the CARLA environment use a YOLO-based computer vision system to detect and count vehicles, providing real-time traffic data as input for adaptive signal control in SUMO. MARL agents trained with four different reward structures leverage this visual feedback to optimize signal timings and improve network-wide traffic flow. Experiments in a multi-intersection test-bed demonstrate the effectiveness of the proposed MARL approach in enhancing traffic conditions using real-time camera based detection. The framework also evaluates the robustness of MARL under faulty or sparse sensing and compares the performance of YOLOv5 and YOLOv8 for vehicle detection. Results show that while better accuracy improves performance, MARL agents can still achieve significant improvements with imperfect detection, demonstrating scalability and adaptability for real-world scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2412.03925v2 발표 유형: 교체-교차  
초록: 교통 시뮬레이션은 도시 교통 흐름을 최적화하는 데 일반적으로 사용되며, 강화 학습(RL)은 특히 연결된 자동화 차량을 포함한 지능형 교통 시스템에서 자동화된 교통 신호 제어에 유망한 잠재력을 보여줍니다. 다중 에이전트 강화 학습(MARL)은 반복적인 시뮬레이션을 사용하여 네트워크 내의 교통 신호등에 대한 제어 전략을 학습하는 데 특히 효과적입니다. 그러나 기존 방법은 종종 완벽한 차량 감지를 가정하여 인프라 가용성과 센서 신뢰성과 관련된 실제 한계를 간과합니다. 본 연구는 고충실도 3D 모델링과 대규모 교통 흐름 시뮬레이션을 결합한 CARLA와 SUMO를 통합한 공동 시뮬레이션 프레임워크를 제안합니다. CARLA 환경 내의 교통 신호등 기둥에 장착된 카메라는 YOLO 기반 컴퓨터 비전 시스템을 사용하여 차량을 감지하고 계산하며, 이는 SUMO에서 적응형 신호 제어를 위한 입력으로 실시간 교통 데이터를 제공합니다. 네 가지 다른 보상 구조로 훈련된 MARL 에이전트는 이 시각적 피드백을 활용하여 신호 타이밍을 최적화하고 네트워크 전반의 교통 흐름을 개선합니다. 다중 교차로 테스트베드에서의 실험은 실시간 카메라 기반 감지를 사용하여 교통 상황을 개선하는 데 있어 제안된 MARL 접근 방식의 효과를 입증합니다. 이 프레임워크는 또한 결함이 있거나 드문 센싱 환경에서 MARL의 견고성을 평가하고, 차량 감지를 위한 YOLOv5와 YOLOv8의 성능을 비교합니다. 결과는 더 나은 정확도가 성능을 향상시키지만, MARL 에이전트가 불완전한 감지로도 여전히 상당한 개선을 달성할 수 있음을 보여주며, 이는 실제 시나리오에 대한 확장성과 적응성을 입증합니다.

## 📝 요약

이 연구는 CARLA와 SUMO를 통합한 공동 시뮬레이션 프레임워크를 제안하여, 실제 교통 상황에서의 한계를 고려한 다중 에이전트 강화 학습(MARL) 기반의 신호 제어를 구현합니다. CARLA 환경의 신호등에 장착된 카메라가 YOLO 기반 컴퓨터 비전 시스템을 통해 차량을 감지하고, 이를 SUMO의 적응형 신호 제어에 실시간 데이터로 제공합니다. 네 가지 보상 구조로 훈련된 MARL 에이전트는 이 시각적 피드백을 활용해 신호 타이밍을 최적화하고, 네트워크 전반의 교통 흐름을 개선합니다. 실험 결과, 제안된 MARL 접근법은 실시간 카메라 기반 감지를 통해 교통 조건을 효과적으로 개선하며, 불완전한 감지 상황에서도 성능을 유지하여 실제 적용 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 CARLA와 SUMO를 통합한 공동 시뮬레이션 프레임워크를 제안하여, 고정밀 3D 모델링과 대규모 교통 흐름 시뮬레이션을 결합합니다.

- 2. CARLA 환경 내 신호등 기둥에 장착된 카메라가 YOLO 기반 컴퓨터 비전 시스템을 사용하여 차량을 감지하고 실시간 교통 데이터를 제공합니다.

- 3. 제안된 MARL 접근법은 다양한 보상 구조를 통해 훈련된 에이전트를 활용하여, 실시간 카메라 기반 감지를 통해 신호 타이밍을 최적화하고 교통 흐름을 개선합니다.

- 4. 실험 결과, YOLOv5와 YOLOv8의 차량 감지 성능을 비교한 결과, 더 나은 정확도가 성능을 향상시키지만, 불완전한 감지에서도 MARL 에이전트가 상당한 개선을 이룰 수 있음을 보여줍니다.

- 5. 제안된 프레임워크는 불완전하거나 드문 센싱 환경에서도 MARL의 견고성을 평가하며, 실제 시나리오에 대한 확장성과 적응성을 입증합니다.

---

*Generated on 2025-09-19 15:43:53*