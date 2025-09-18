
# Hierarchical Learning for Maze Navigation: Emergence of Mental Representations via Second-Order Learning

**Korean Title:** 미로 탐색을 위한 계층적 학습: 2차 학습을 통한 정신적 표현의 발생

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[keywords/broad/Graph Convolutional Network|Graph Convolutional Network]] [[keywords/broad/MLP controller|MLP controller]] [[keywords/specific/Optimal navigation paths|Optimal navigation paths]] [[keywords/evolved/Structured mental representations|Structured mental representations]] [[keywords/unique/Hierarchical Learning|Hierarchical Learning]] [[authors/Shalima Binta Manir|Shalima Binta Manir]] [[authors/Tim Oates|Tim Oates]] [[categories/cs.AI|cs.AI]] [[Imagined Autocurricula|79.9% similar]] [[GraphTorque: Torque-Driven Rewiring Graph Neural Network|76.3% similar]] [[OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft|76.0% similar]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Graph Convolutional Network, MLP controller
**🔗 Specific Connectable**: Optimal navigation paths
**🚀 Evolved Concepts**: Structured mental representations
**⭐ Unique Technical**: Hierarchical Learning
## 🔗 유사한 논문
- [[Imagined Autocurricula]] (79.9% similar)
- [[GraphTorque Torque-Driven Rewiring Graph Neural Network]] (76.3% similar)
- [[OpenHA A Series of Open-Source Hierarchical Agentic Models in Minecraft]] (76.0% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (75.8% similar)
- [[Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (75.7% similar)


**ArXiv ID**: [2509.14195v1](https://arxiv.org/abs/2509.14195v1)
**Published**: 2025-09-17
**Category**: cs.AI
**PDF**: [Download](http://arxiv.org/pdf/2509.14195v1)


## 🏷️ 추출된 키워드



`Graph Convolutional Network` • 

`MLP controller` • 

`Optimal navigation paths` • 

`Hierarchical Learning` • 

`Structured mental representations`



## 📋 저자 정보

**Authors:** Shalima Binta Manir, Tim Oates

## 📄 Abstract (원문)

Mental representation, characterized by structured internal models mirroring
external environments, is fundamental to advanced cognition but remains
challenging to investigate empirically. Existing theory hypothesizes that
second-order learning -- learning mechanisms that adapt first-order learning
(i.e., learning about the task/domain) -- promotes the emergence of such
environment-cognition isomorphism. In this paper, we empirically validate this
hypothesis by proposing a hierarchical architecture comprising a Graph
Convolutional Network (GCN) as a first-order learner and an MLP controller as a
second-order learner. The GCN directly maps node-level features to predictions
of optimal navigation paths, while the MLP dynamically adapts the GCN's
parameters when confronting structurally novel maze environments. We
demonstrate that second-order learning is particularly effective when the
cognitive system develops an internal mental map structurally isomorphic to the
environment. Quantitative and qualitative results highlight significant
performance improvements and robust generalization on unseen maze tasks,
providing empirical support for the pivotal role of structured mental
representations in maximizing the effectiveness of second-order learning.

## 🔍 Abstract (한글 번역)

정신적 표현은 외부 환경을 반영하는 구조화된 내부 모델에 의해 특징 지어지며, 고급 인지에 기본적이지만 실험적으로 조사하기 어렵습니다. 기존 이론은 두 번째 순서 학습 - 첫 번째 순서 학습을 적응시키는 학습 메커니즘(즉, 과제/도메인에 대한 학습) - 이러한 환경-인지 동형성의 발생을 촉진한다고 가설화합니다. 본 논문에서는 Graph Convolutional Network (GCN)을 첫 번째 순서 학습자로, MLP 컨트롤러를 두 번째 순서 학습자로 하는 계층적 아키텍처를 제안하여 이 가설을 실험적으로 검증합니다. GCN은 노드 수준의 특징을 최적의 탐색 경로 예측으로 직접 매핑하며, MLP는 구조적으로 새로운 미로 환경을 직면할 때 GCN의 매개변수를 동적으로 적응시킵니다. 우리는 두 번째 순서 학습이 인지 시스템이 환경과 구조적으로 동형인 내부적인 정신적 지도를 개발할 때 특히 효과적임을 보여줍니다. 양적 및 질적 결과는 보이지 않는 미로 과제에서의 중요한 성능 향상과 견고한 일반화를 강조하며, 구조화된 정신적 표현의 중요성을 강조하여 두 번째 순서 학습의 효과를 극대화하는 데 실험적 지원을 제공합니다.

## 📝 요약

이 논문은 환경을 반영하는 구조화된 내부 모델에 대한 정신적 표상이 고급 인지에 기본적이지만 실험적으로 탐구하기 어려운 것이라는 것을 강조한다. 이론은 둘째 학습 - 첫째 학습을 적응시키는 학습 메커니즘 - 이 환경-인지 동형성의 발생을 촉진한다고 가정한다. 본 논문에서는 Graph Convolutional Network (GCN)을 첫째 학습자로, MLP 컨트롤러를 둘째 학습자로 하는 계층적 아키텍처를 제안하여 이 가설을 검증한다. 둘째 학습은 환경에 구조적으로 새로운 미로 환경을 직면할 때 GCN의 매개변수를 동적으로 조정하며, 내부적인 정신적 지도를 개발할 때 특히 효과적임을 보여준다. 양적 및 질적 결과는 보다 효과적인 둘째 학습의 효과를 극대화하기 위한 구조화된 정신적 표상의 중요성을 실험적으로 지지하며, 보이지 않는 미로 작업에 대한 성능 향상과 견고한 일반화를 강조한다.

## 🎯 주요 포인트


- 정신적 표상은 외부 환경을 반영하는 구조화된 내부 모델에 의해 특징 지어지며, 고급 인지에 기본적이지만 실험적으로 조사하기 어렵다.

- 이 논문에서는 두 번째 학습이 첫 번째 학습을 적응시키는 학습 메커니즘인 이차 학습이 환경-인지 동형성의 발생을 촉진한다는 가설을 검증한다.

- 그래프 컨볼루션 네트워크(GCN)와 MLP 컨트롤러로 구성된 계층적 아키텍처를 제안하여 이 가설을 실험적으로 검증한다.

- 이차 학습은 인지 시스템이 환경과 구조적으로 동형인 내부 정신적 지도를 개발할 때 특히 효과적임을 입증한다.


---

*Generated on 2025-09-18 17:04:17*