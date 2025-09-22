# Compose by Focus: Scene Graph-based Atomic Skills

**Korean Title:** 포커스에 의한 구성: 장면 그래프 기반의 원자적 기술

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Graph Neural Network, Vision Language Model

## 🔗 유사한 논문
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (82.5% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (82.2% similar)
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (81.9% similar)
- [[2025-09-18/textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|textsc{Gen2Real} Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (81.1% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (80.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16053v1 Announce Type: cross 
Abstract: A key requirement for generalist robots is compositional generalization - the ability to combine atomic skills to solve complex, long-horizon tasks. While prior work has primarily focused on synthesizing a planner that sequences pre-learned skills, robust execution of the individual skills themselves remains challenging, as visuomotor policies often fail under distribution shifts induced by scene composition. To address this, we introduce a scene graph-based representation that focuses on task-relevant objects and relations, thereby mitigating sensitivity to irrelevant variation. Building on this idea, we develop a scene-graph skill learning framework that integrates graph neural networks with diffusion-based imitation learning, and further combine "focused" scene-graph skills with a vision-language model (VLM) based task planner. Experiments in both simulation and real-world manipulation tasks demonstrate substantially higher success rates than state-of-the-art baselines, highlighting improved robustness and compositional generalization in long-horizon tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16053v1 발표 유형: 교차  
초록: 일반적인 로봇에게 중요한 요구 사항 중 하나는 조합적 일반화(compositional generalization)입니다. 이는 원자적 기술을 결합하여 복잡하고 장기적인 과제를 해결하는 능력을 의미합니다. 이전 연구는 주로 사전에 학습된 기술을 순서대로 배열하는 계획자를 합성하는 데 중점을 두었지만, 개별 기술의 견고한 실행은 여전히 도전 과제로 남아 있습니다. 이는 장면 구성에 의해 유도된 분포 변화에서 시각-운동 정책이 종종 실패하기 때문입니다. 이를 해결하기 위해 우리는 과제와 관련된 객체와 관계에 중점을 둔 장면 그래프 기반 표현을 도입하여 관련 없는 변동에 대한 민감성을 완화합니다. 이 아이디어를 바탕으로, 우리는 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발하고, "집중된" 장면 그래프 기술을 비전-언어 모델(VLM) 기반 과제 계획자와 결합합니다. 시뮬레이션 및 실제 조작 작업에서의 실험은 최첨단 기준선보다 상당히 높은 성공률을 보여주며, 장기 과제에서의 향상된 견고성과 조합적 일반화를 강조합니다.

## 📝 요약

이 논문은 일반 로봇의 조합적 일반화 능력을 향상시키기 위해 장면 그래프 기반의 표현 방식을 제안합니다. 이는 과제와 관련된 객체와 관계에 집중하여 불필요한 변동에 대한 민감성을 줄입니다. 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발하고, 이를 비전-언어 모델(VLM) 기반의 작업 계획자와 결합합니다. 실험 결과, 시뮬레이션 및 실제 조작 작업에서 최첨단 기준보다 높은 성공률을 보여주며, 장기 작업에서의 강인성과 조합적 일반화가 개선됨을 입증합니다.

## 🎯 주요 포인트

- 1. 일반 로봇의 핵심 요구 사항은 원자적 기술을 결합하여 복잡한 장기 과제를 해결하는 조합적 일반화 능력이다.

- 2. 기존 연구는 주로 사전 학습된 기술을 순차적으로 계획하는 데 초점을 맞추었으나, 개별 기술의 견고한 실행은 여전히 도전 과제이다.

- 3. 장면 그래프 기반 표현을 도입하여 작업 관련 객체와 관계에 집중함으로써 불필요한 변동에 대한 민감성을 완화한다.

- 4. 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발하고, 시각-언어 모델 기반의 작업 계획자와 결합한다.

- 5. 시뮬레이션 및 실제 조작 작업 실험에서 최첨단 기준보다 높은 성공률을 보여 장기 과제에서의 향상된 견고성과 조합적 일반화를 강조한다.

---

*Generated on 2025-09-22 14:23:21*