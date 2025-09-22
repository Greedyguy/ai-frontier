
# Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring

**Korean Title:** 시각 유도 그래프 색칠을 이용한 시각 재배열 작업을 위한 이산 추상화 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Graph Coloring, Attention Mechanism

## 🔗 유사한 논문
- [[Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.9% similar)
- [[TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (81.7% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (81.6% similar)
- [[Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (81.0% similar)
- [[GAF Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14460v1 Announce Type: new 
Abstract: Learning abstractions directly from data is a core challenge in robotics. Humans naturally operate at an abstract level, reasoning over high-level subgoals while delegating execution to low-level motor skills -- an ability that enables efficient problem solving in complex environments. In robotics, abstractions and hierarchical reasoning have long been central to planning, yet they are typically hand-engineered, demanding significant human effort and limiting scalability. Automating the discovery of useful abstractions directly from visual data would make planning frameworks more scalable and more applicable to real-world robotic domains. In this work, we focus on rearrangement tasks where the state is represented with raw images, and propose a method to induce discrete, graph-structured abstractions by combining structural constraints with an attention-guided visual distance. Our approach leverages the inherent bipartite structure of rearrangement problems, integrating structural constraints and visual embeddings into a unified framework. This enables the autonomous discovery of abstractions from vision alone, which can subsequently support high-level planning. We evaluate our method on two rearrangement tasks in simulation and show that it consistently identifies meaningful abstractions that facilitate effective planning and outperform existing approaches.

## 🔍 Abstract (한글 번역)

arXiv:2509.14460v1 발표 유형: 신규  
초록: 데이터로부터 추상화를 학습하는 것은 로봇 공학의 핵심 과제입니다. 인간은 자연스럽게 추상적 수준에서 작동하며, 고수준의 하위 목표를 논리적으로 사고하면서 저수준의 운동 기술에 실행을 위임합니다. 이러한 능력은 복잡한 환경에서 효율적인 문제 해결을 가능하게 합니다. 로봇 공학에서 추상화와 계층적 추론은 오랫동안 계획의 중심이었지만, 일반적으로 수작업으로 설계되어 상당한 인간의 노력이 필요하고 확장성이 제한됩니다. 시각적 데이터로부터 유용한 추상화를 자동으로 발견하면 계획 프레임워크가 더 확장 가능해지고 실제 로봇 도메인에 더 적용 가능해질 것입니다. 이 연구에서는 상태가 원시 이미지로 표현되는 재배치 작업에 초점을 맞추고, 구조적 제약과 주의 기반의 시각적 거리를 결합하여 이산적이고 그래프 구조화된 추상화를 유도하는 방법을 제안합니다. 우리의 접근법은 재배치 문제의 고유한 이분 그래프 구조를 활용하여 구조적 제약과 시각적 임베딩을 통합된 프레임워크로 통합합니다. 이는 시각 정보만으로 추상화를 자율적으로 발견할 수 있게 하며, 이후 고수준의 계획을 지원할 수 있습니다. 우리는 시뮬레이션에서 두 가지 재배치 작업에 대해 우리의 방법을 평가하고, 효과적인 계획을 촉진하고 기존 접근 방식을 능가하는 의미 있는 추상화를 일관되게 식별함을 보여줍니다.

## 📝 요약

이 논문은 로봇 공학에서 데이터로부터 직접 유용한 추상화를 학습하는 방법을 제안합니다. 기존의 추상화는 주로 수작업으로 설계되어 확장성이 제한적이었으나, 이 연구는 시각 데이터를 통해 자동으로 추상화를 발견하는 방법을 개발했습니다. 특히, 재배치 작업에서 구조적 제약과 주의 기반의 시각적 거리를 결합하여 이산적이고 그래프 구조의 추상화를 유도하는 방법론을 제시합니다. 이 접근법은 시뮬레이션에서 두 가지 재배치 작업에 적용되어 효과적인 계획을 지원하는 의미 있는 추상화를 일관되게 식별하며, 기존 방법들을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 로봇 공학에서 데이터로부터 직접 추상화를 학습하는 것은 핵심적인 도전 과제입니다.

- 2. 본 연구는 구조적 제약과 주의 기반 시각적 거리를 결합하여 이산적이고 그래프 구조의 추상화를 유도하는 방법을 제안합니다.

- 3. 제안된 방법은 재배치 문제의 고유한 이분 구조를 활용하여 시각적 임베딩과 구조적 제약을 통합합니다.

- 4. 시뮬레이션에서 두 가지 재배치 작업에 대한 평가 결과, 제안된 방법이 의미 있는 추상화를 일관되게 식별하여 효과적인 계획을 지원함을 보여줍니다.

- 5. 본 연구는 시각 정보만으로 추상화를 자동으로 발견하여 고수준 계획을 지원할 수 있는 가능성을 제시합니다.

---

*Generated on 2025-09-19 16:31:08*