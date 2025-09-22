# Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems

**Korean Title:** 계층적 자기-어텐션: 다중 스케일 문제로의 신경 어텐션 메커니즘 일반화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Scale Attention

## 🔗 유사한 논문
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC) A Cognitive-Inspired Approach for Attention Management in Transformers]] (82.6% similar)
- [[2025-09-19/Fast Multipole Attention_ A Scalable Multilevel Attention Mechanism for Text and Images_20250919|Fast Multipole Attention A Scalable Multilevel Attention Mechanism for Text and Images]] (82.2% similar)
- [[2025-09-18/Stochastic Clock Attention for Aligning Continuous and Ordered Sequences_20250918|Stochastic Clock Attention for Aligning Continuous and Ordered Sequences]] (80.9% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (79.5% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15448v1 Announce Type: cross 
Abstract: Transformers and their attention mechanism have been revolutionary in the field of Machine Learning. While originally proposed for the language data, they quickly found their way to the image, video, graph, etc. data modalities with various signal geometries. Despite this versatility, generalizing the attention mechanism to scenarios where data is presented at different scales from potentially different modalities is not straightforward. The attempts to incorporate hierarchy and multi-modality within transformers are largely based on ad hoc heuristics, which are not seamlessly generalizable to similar problems with potentially different structures. To address this problem, in this paper, we take a fundamentally different approach: we first propose a mathematical construct to represent multi-modal, multi-scale data. We then mathematically derive the neural attention mechanics for the proposed construct from the first principle of entropy minimization. We show that the derived formulation is optimal in the sense of being the closest to the standard Softmax attention while incorporating the inductive biases originating from the hierarchical/geometric information of the problem. We further propose an efficient algorithm based on dynamic programming to compute our derived attention mechanism. By incorporating it within transformers, we show that the proposed hierarchical attention mechanism not only can be employed to train transformer models in hierarchical/multi-modal settings from scratch, but it can also be used to inject hierarchical information into classical, pre-trained transformer models post training, resulting in more efficient models in zero-shot manner.

## 🔍 Abstract (한글 번역)

arXiv:2509.15448v1 발표 유형: 교차  
초록: 트랜스포머와 그 주의 메커니즘은 머신 러닝 분야에서 혁신적이었습니다. 원래 언어 데이터를 위해 제안되었지만, 이미지, 비디오, 그래프 등 다양한 신호 기하학을 가진 데이터 모달리티로 빠르게 확장되었습니다. 이러한 다재다능함에도 불구하고, 잠재적으로 다른 모달리티에서 다양한 규모로 데이터가 제공되는 시나리오에 주의 메커니즘을 일반화하는 것은 간단하지 않습니다. 트랜스포머 내에서 계층 구조와 다중 모달리티를 통합하려는 시도는 주로 임시방편적인 휴리스틱에 기반하고 있으며, 이는 잠재적으로 다른 구조를 가진 유사한 문제에 원활하게 일반화되지 않습니다. 이 문제를 해결하기 위해, 본 논문에서는 근본적으로 다른 접근 방식을 취합니다: 우리는 먼저 다중 모달, 다중 규모 데이터를 표현하기 위한 수학적 구조를 제안합니다. 그런 다음 제안된 구조에 대한 신경 주의 메커니즘을 엔트로피 최소화의 첫 번째 원리에서 수학적으로 도출합니다. 우리는 도출된 공식이 문제의 계층적/기하학적 정보에서 유래한 귀납적 편향을 통합하면서 표준 소프트맥스 주의와 가장 가까운 최적의 형태임을 보여줍니다. 또한, 우리는 동적 프로그래밍을 기반으로 한 효율적인 알고리즘을 제안하여 도출된 주의 메커니즘을 계산합니다. 이를 트랜스포머에 통합함으로써, 제안된 계층적 주의 메커니즘이 계층적/다중 모달 설정에서 트랜스포머 모델을 처음부터 훈련하는 데 사용될 수 있을 뿐만 아니라, 훈련 후 기존의 사전 훈련된 트랜스포머 모델에 계층적 정보를 주입하여 제로샷 방식으로 더 효율적인 모델을 만들 수 있음을 보여줍니다.

## 📝 요약

이 논문은 트랜스포머의 주의 메커니즘을 다양한 신호 기하학을 가진 다중 모달 및 다중 스케일 데이터에 일반화하는 새로운 접근 방식을 제안합니다. 기존의 방법들이 임시방편적인 휴리스틱에 의존하는 반면, 본 연구는 다중 모달, 다중 스케일 데이터를 수학적으로 표현하는 구조를 제안하고, 엔트로피 최소화 원칙에서 출발하여 주의 메커니즘을 수학적으로 도출합니다. 이 도출된 메커니즘은 표준 소프트맥스 주의와 가장 가까우면서도 계층적/기하학적 정보를 통합하여 최적임을 보입니다. 또한, 동적 프로그래밍을 기반으로 효율적인 알고리즘을 제안하여, 계층적 주의 메커니즘을 트랜스포머에 통합함으로써 계층적/다중 모달 환경에서 트랜스포머 모델을 처음부터 학습시키거나, 사전 학습된 모델에 계층 정보를 주입하여 제로샷 방식으로 더 효율적인 모델을 구현할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 트랜스포머의 주의 메커니즘은 다양한 데이터 모달리티에 적용되며, 특히 다중 스케일 및 다중 모달리티 시나리오에 일반화하는 것이 어렵다.

- 2. 기존의 트랜스포머는 계층 구조와 다중 모달리티를 통합하는 데 있어 임시방편적인 방법에 의존하고 있다.

- 3. 본 논문에서는 다중 모달, 다중 스케일 데이터를 표현하기 위한 수학적 구조를 제안하고, 이를 기반으로 엔트로피 최소화 원칙에서 출발하여 주의 메커니즘을 도출하였다.

- 4. 제안된 주의 메커니즘은 계층적/기하학적 정보로부터 유도된 귀납적 편향을 포함하면서도 표준 소프트맥스 주의 메커니즘에 가장 근접한 최적의 형태를 가진다.

- 5. 동적 프로그래밍을 기반으로 한 효율적인 알고리즘을 통해 제안된 주의 메커니즘을 계산하고, 이를 트랜스포머에 통합하여 계층적/다중 모달 설정에서의 학습 및 기존 모델에 계층적 정보를 주입하는 데 활용할 수 있다.

---

*Generated on 2025-09-22 13:57:47*