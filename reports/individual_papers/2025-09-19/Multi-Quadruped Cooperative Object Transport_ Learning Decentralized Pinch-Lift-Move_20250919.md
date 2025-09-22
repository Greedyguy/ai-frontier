
# Multi-Quadruped Cooperative Object Transport: Learning Decentralized Pinch-Lift-Move

**Korean Title:** 다중 사족보행 로봇의 협력적 물체 운반: 분산된 집게-들기-이동 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Quadruped Coordination

## 🔗 유사한 논문
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (83.6% similar)
- [[Flexible and Foldable Workspace Analysis and Object Manipulation Using a Soft, Interconnected, Origami-Inspired Actuator Array]] (82.0% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (81.3% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (80.3% similar)
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14342v1 Announce Type: new 
Abstract: We study decentralized cooperative transport using teams of N-quadruped robots with arm that must pinch, lift, and move ungraspable objects through physical contact alone. Unlike prior work that relies on rigid mechanical coupling between robots and objects, we address the more challenging setting where mechanically independent robots must coordinate through contact forces alone without any communication or centralized control. To this end, we employ a hierarchical policy architecture that separates base locomotion from arm control, and propose a constellation reward formulation that unifies position and orientation tracking to enforce rigid contact behavior. The key insight is encouraging robots to behave as if rigidly connected to the object through careful reward design and training curriculum rather than explicit mechanical constraints. Our approach enables coordination through shared policy parameters and implicit synchronization cues - scaling to arbitrary team sizes without retraining. We show extensive simulation experiments to demonstrate robust transport across 2-10 robots on diverse object geometries and masses, along with sim2real transfer results on lightweight objects.

## 🔍 Abstract (한글 번역)

arXiv:2509.14342v1 발표 유형: 신규  
초록: 우리는 N-사족보행 로봇 팀을 사용하여 비가시적인 물체를 물리적 접촉만으로 집어 올리고 이동시키는 분산형 협력 운송을 연구합니다. 이전 연구와 달리 로봇과 물체 사이의 강체 기계적 결합에 의존하지 않고, 기계적으로 독립적인 로봇들이 통신이나 중앙 제어 없이 접촉력만으로 조정해야 하는 더 어려운 환경을 다룹니다. 이를 위해, 우리는 기본 보행과 팔 제어를 분리하는 계층적 정책 구조를 사용하고, 위치 및 방향 추적을 통합하여 강체 접촉 행동을 강제하는 별자리 보상 공식을 제안합니다. 핵심 통찰력은 명시적인 기계적 제약보다는 신중한 보상 설계와 훈련 과정을 통해 로봇들이 물체에 강체로 연결된 것처럼 행동하도록 장려하는 것입니다. 우리의 접근 방식은 공유 정책 매개변수와 암시적 동기화 신호를 통해 조정을 가능하게 하며, 재훈련 없이 임의의 팀 크기로 확장할 수 있습니다. 우리는 다양한 물체의 기하학적 형태와 질량에 대해 2-10개의 로봇을 사용한 견고한 운송을 시뮬레이션 실험을 통해 광범위하게 보여주고, 경량 물체에 대한 sim2real 전이 결과를 제시합니다.

## 📝 요약

이 논문은 N개의 사족보행 로봇 팀이 물리적 접촉만으로 잡을 수 없는 물체를 집어 들어 이동시키는 탈중앙화 협력 운송 문제를 다룹니다. 기존 연구와 달리, 로봇과 물체 간의 기계적 연결 없이 접촉력만으로 조정해야 하는 도전적인 환경을 설정합니다. 이를 위해, 로봇의 기본 이동과 팔 제어를 분리하는 계층적 정책 구조를 사용하고, 위치와 방향 추적을 통합한 보상 체계를 제안하여 엄격한 접촉 행동을 유도합니다. 주요 기여는 명시적 기계적 제약 없이 보상 설계와 훈련 과정을 통해 로봇이 물체에 강하게 연결된 것처럼 행동하도록 유도하는 것입니다. 이 접근법은 공유 정책 매개변수와 암묵적 동기화 신호를 통해 조정을 가능하게 하며, 재훈련 없이 임의의 팀 크기로 확장할 수 있습니다. 다양한 물체 형상과 질량에 대해 2-10개의 로봇이 참여하는 시뮬레이션 실험을 통해 강력한 운송 능력을 입증하고, 경량 물체에 대한 sim2real 전이 결과도 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 N개의 사족보행 로봇 팀이 물리적 접촉만으로 잡을 수 없는 물체를 집고, 들어 올리고, 이동시키는 탈중앙화 협력 운송을 다룹니다.

- 2. 로봇과 물체 간의 강체 기계적 결합에 의존하지 않고, 접촉력만으로 조정해야 하는 도전적인 환경을 대상으로 합니다.

- 3. 계층적 정책 아키텍처를 사용하여 로봇의 기본 이동과 팔 제어를 분리하고, 위치 및 방향 추적을 통합하는 보상 공식을 제안합니다.

- 4. 로봇이 물체에 강체로 연결된 것처럼 행동하도록 유도하여 명시적인 기계적 제약 없이 조정을 가능하게 합니다.

- 5. 다양한 물체 형상과 질량에 대해 2-10개의 로봇이 견고하게 운송하는 시뮬레이션 실험과 경량 물체에 대한 sim2real 전이 결과를 보여줍니다.

---

*Generated on 2025-09-19 16:28:56*