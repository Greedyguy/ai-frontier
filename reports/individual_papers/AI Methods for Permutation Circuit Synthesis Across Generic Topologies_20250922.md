# AI Methods for Permutation Circuit Synthesis Across Generic Topologies

**Korean Title:** 일반적 토폴로지 전반에 걸친 순열 회로 합성을 위한 AI 기법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Topology Selection

## 🔗 유사한 논문
- [[2025-09-17/TopoSizing_ An LLM-aided Framework of Topology-based Understanding and Sizing for AMS Circuits_20250917|TopoSizing An LLM-aided Framework of Topology-based Understanding and Sizing for AMS Circuits]] (79.8% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (78.9% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (78.9% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (77.7% similar)
- [[2025-09-17/A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (77.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16020v1 Announce Type: cross 
Abstract: This paper investigates artificial intelligence (AI) methodologies for the synthesis and transpilation of permutation circuits across generic topologies. Our approach uses Reinforcement Learning (RL) techniques to achieve near-optimal synthesis of permutation circuits up to 25 qubits. Rather than developing specialized models for individual topologies, we train a foundational model on a generic rectangular lattice, and employ masking mechanisms to dynamically select subsets of topologies during the synthesis. This enables the synthesis of permutation circuits on any topology that can be embedded within the rectangular lattice, without the need to re-train the model. In this paper we show results for 5x5 lattice and compare them to previous AI topology-oriented models and classical methods, showing that they outperform classical heuristics, and match previous specialized AI models, and performs synthesis even for topologies that were not seen during training. We further show that the model can be fine tuned to strengthen the performance for selected topologies of interest. This methodology allows a single trained model to efficiently synthesize circuits across diverse topologies, allowing its practical integration into transpilation workflows.

## 🔍 Abstract (한글 번역)

arXiv:2509.16020v1 발표 유형: 교차  
초록: 이 논문은 일반적인 토폴로지에서 순열 회로의 합성과 변환을 위한 인공지능(AI) 방법론을 조사합니다. 우리의 접근 방식은 강화 학습(RL) 기법을 사용하여 최대 25 큐비트의 순열 회로의 거의 최적 합성을 달성합니다. 개별 토폴로지를 위한 특수 모델을 개발하는 대신, 우리는 일반적인 직사각형 격자에서 기본 모델을 훈련하고, 합성 중에 토폴로지의 하위 집합을 동적으로 선택하기 위해 마스킹 메커니즘을 사용합니다. 이를 통해 직사각형 격자 내에 임베딩할 수 있는 모든 토폴로지에서 순열 회로의 합성이 가능하며, 모델을 재훈련할 필요가 없습니다. 이 논문에서는 5x5 격자에 대한 결과를 보여주고, 이전의 AI 토폴로지 지향 모델 및 고전적 방법과 비교하여, 고전적 휴리스틱을 능가하고, 이전의 특수 AI 모델과 일치하며, 훈련 중에 보지 못한 토폴로지에 대해서도 합성을 수행함을 보여줍니다. 또한 모델이 관심 있는 특정 토폴로지의 성능을 강화하기 위해 미세 조정될 수 있음을 보여줍니다. 이 방법론은 단일 훈련 모델이 다양한 토폴로지에서 회로를 효율적으로 합성할 수 있게 하여, 변환 워크플로우에 실질적으로 통합될 수 있도록 합니다.

## 📝 요약

이 논문은 다양한 토폴로지에서 순열 회로의 합성과 변환을 위한 인공지능(AI) 방법론을 연구합니다. 강화 학습(RL) 기법을 활용하여 최대 25 큐비트의 순열 회로를 거의 최적에 가깝게 합성합니다. 개별 토폴로지에 특화된 모델을 개발하는 대신, 일반적인 직사각형 격자에서 기초 모델을 훈련하고 마스킹 메커니즘을 사용하여 합성 중에 동적으로 토폴로지의 하위 집합을 선택합니다. 이를 통해 모델을 재훈련할 필요 없이 직사각형 격자에 내장될 수 있는 모든 토폴로지에서 순열 회로를 합성할 수 있습니다. 5x5 격자에 대한 결과는 기존 AI 토폴로지 지향 모델 및 고전적 방법과 비교하여 우수한 성능을 보이며, 훈련되지 않은 토폴로지에서도 합성을 수행할 수 있습니다. 또한 특정 토폴로지에 대한 성능을 강화하기 위해 모델을 미세 조정할 수 있음을 보여줍니다. 이 방법론은 단일 훈련 모델이 다양한 토폴로지에서 효율적으로 회로를 합성할 수 있도록 하여 변환 워크플로에 실질적으로 통합될 수 있습니다.

## 🎯 주요 포인트

- 1. 본 논문은 강화 학습 기법을 활용하여 최대 25 큐비트의 순열 회로를 근사 최적 합성하는 AI 방법론을 제안합니다.

- 2. 사각 격자에서 기초 모델을 훈련하고 마스킹 메커니즘을 사용하여 다양한 토폴로지를 동적으로 선택하여 합성을 수행합니다.

- 3. 제안된 방법론은 사각 격자에 내장될 수 있는 모든 토폴로지에서 순열 회로를 합성할 수 있으며, 재훈련이 필요하지 않습니다.

- 4. 5x5 격자에서의 결과는 기존 AI 토폴로지 지향 모델 및 고전적 방법과 비교하여 우수한 성능을 보이며, 훈련 시 보지 못한 토폴로지에서도 합성을 수행합니다.

- 5. 단일 훈련 모델로 다양한 토폴로지에서 회로를 효율적으로 합성할 수 있어, 실질적인 트랜스파일레이션 워크플로우에 통합이 가능합니다.

---

*Generated on 2025-09-22 14:22:21*