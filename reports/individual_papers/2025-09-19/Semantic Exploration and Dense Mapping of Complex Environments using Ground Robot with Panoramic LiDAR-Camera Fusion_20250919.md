
# Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion

**Korean Title:** 복합 환경의 의미론적 탐색 및 밀집 매핑을 위한 파노라마 LiDAR-카메라 융합을 이용한 지상 로봇 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dense Semantic Mapping

## 🔗 유사한 논문
- [[Search-TTA A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (83.6% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (83.1% similar)
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (83.1% similar)
- [[MCGS-SLAM A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (82.8% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22880v3 Announce Type: replace-cross 
Abstract: This paper presents a system for autonomous semantic exploration and dense semantic target mapping of a complex unknown environment using a ground robot equipped with a LiDAR-panoramic camera suite. Existing approaches often struggle to balance collecting high-quality observations from multiple view angles and avoiding unnecessary repetitive traversal. To fill this gap, we propose a complete system combining mapping and planning. We first redefine the task as completing both geometric coverage and semantic viewpoint observation. We then manage semantic and geometric viewpoints separately and propose a novel Priority-driven Decoupled Local Sampler to generate local viewpoint sets. This enables explicit multi-view semantic inspection and voxel coverage without unnecessary repetition. Building on this, we develop a hierarchical planner to ensure efficient global coverage. In addition, we propose a Safe Aggressive Exploration State Machine, which allows aggressive exploration behavior while ensuring the robot's safety. Our system includes a plug-and-play semantic target mapping module that integrates seamlessly with state-of-the-art SLAM algorithms for pointcloud-level dense semantic target mapping. We validate our approach through extensive experiments in both realistic simulations and complex real-world environments. Simulation results show that our planner achieves faster exploration and shorter travel distances while guaranteeing a specified number of multi-view inspections. Real-world experiments further confirm the system's effectiveness in achieving accurate dense semantic object mapping of unstructured environments.

## 🔍 Abstract (한글 번역)

arXiv:2505.22880v3 발표 유형: 교차 대체  
초록: 이 논문은 LiDAR-파노라마 카메라 장비를 갖춘 지상 로봇을 사용하여 복잡하고 미지의 환경을 자율적으로 의미론적으로 탐색하고 밀집된 의미론적 목표 지도를 작성하는 시스템을 제시합니다. 기존 접근 방식은 여러 시야각에서 고품질 관측을 수집하는 것과 불필요한 반복 탐색을 피하는 것 사이의 균형을 맞추는 데 종종 어려움을 겪습니다. 이러한 격차를 해소하기 위해 우리는 매핑과 계획을 결합한 완전한 시스템을 제안합니다. 우리는 먼저 과제를 기하학적 커버리지와 의미론적 시점 관찰을 모두 완료하는 것으로 재정의합니다. 그런 다음 의미론적 및 기하학적 시점을 별도로 관리하고, 지역 시점 세트를 생성하기 위한 새로운 우선순위 기반 분리 지역 샘플러를 제안합니다. 이를 통해 불필요한 반복 없이 명시적인 다중 시점 의미론적 검사와 복셀 커버리지가 가능합니다. 이를 바탕으로 효율적인 글로벌 커버리지를 보장하는 계층적 계획자를 개발합니다. 또한, 로봇의 안전을 보장하면서 공격적인 탐색 행동을 허용하는 안전한 공격적 탐색 상태 기계를 제안합니다. 우리의 시스템은 최첨단 SLAM 알고리즘과 원활하게 통합되어 포인트클라우드 수준의 밀집된 의미론적 목표 매핑을 수행할 수 있는 플러그 앤 플레이 의미론적 목표 매핑 모듈을 포함합니다. 우리는 현실적인 시뮬레이션과 복잡한 실제 환경 모두에서 광범위한 실험을 통해 우리의 접근 방식을 검증합니다. 시뮬레이션 결과는 우리의 계획자가 더 빠른 탐색과 더 짧은 이동 거리를 달성하면서 지정된 수의 다중 시점 검사를 보장함을 보여줍니다. 실제 실험은 비정형 환경의 정확한 밀집 의미론적 객체 매핑을 달성하는 데 있어 시스템의 효과를 추가로 확인합니다.

## 📝 요약

이 논문은 LiDAR-파노라마 카메라를 장착한 지상 로봇을 이용해 복잡한 미지의 환경에서 자율적인 의미 탐색과 밀집 의미 대상 매핑 시스템을 제안합니다. 기존 방법들은 여러 각도에서 고품질 관찰을 수집하는 것과 불필요한 반복 이동을 피하는 것 사이에서 균형을 잡기 어려워합니다. 이를 해결하기 위해, 우리는 매핑과 계획을 결합한 완전한 시스템을 제안합니다. 기하학적 커버리지와 의미적 관점 관찰을 완료하는 것으로 작업을 재정의하고, 우선순위 기반의 분리된 로컬 샘플러를 제안하여 명시적인 다중 관점 의미 검사와 복셀 커버리지를 가능하게 합니다. 또한, 안전한 공격적 탐색 상태 기계를 도입하여 로봇의 안전을 보장하면서도 공격적인 탐색을 수행할 수 있게 합니다. 우리의 시스템은 최신 SLAM 알고리즘과 통합되어 포인트클라우드 수준의 밀집 의미 대상 매핑을 수행합니다. 시뮬레이션과 실제 환경 실험을 통해 제안된 시스템의 효율성과 정확성을 입증하였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 LiDAR-파노라마 카메라를 장착한 지상 로봇을 이용하여 복잡하고 미지의 환경에서 자율적인 의미 탐색 및 밀집 의미 대상 매핑 시스템을 제안합니다.

- 2. 제안된 시스템은 기하학적 커버리지와 의미적 관점 관찰을 동시에 완료하는 작업으로 재정의하고, 의미적 및 기하학적 관점을 별도로 관리하여 불필요한 반복을 피하면서 명시적인 다중 관점 의미 검사와 복셀 커버리지를 가능하게 합니다.

- 3. 안전한 공격적 탐색 상태 기계를 제안하여 로봇의 안전을 보장하면서 공격적인 탐색 행동을 허용합니다.

- 4. 플러그 앤 플레이 방식의 의미 대상 매핑 모듈을 포함하여 최신 SLAM 알고리즘과 원활하게 통합하여 포인트클라우드 수준의 밀집 의미 대상 매핑을 수행합니다.

- 5. 시뮬레이션 및 실제 환경 실험을 통해 제안된 시스템의 빠른 탐색, 짧은 이동 거리, 정확한 밀집 의미 객체 매핑 성능을 검증하였습니다.

---

*Generated on 2025-09-19 15:16:31*