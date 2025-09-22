# State Space Models over Directed Graphs

**Korean Title:** 지시 그래프 상의 상태 공간 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Junzhi She|Junzhi She]] [[authors/Xunkai Li|Xunkai Li]] [[authors/Rong-Hua Li|Rong-Hua Li]] [[authors/Guoren Wang|Guoren Wang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Directed Graph Learning

## 🔗 유사한 논문
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (81.4% similar)
- [[Exploring the Global-to-Local Attention Scheme in Graph Transformers_ An Empirical Study_20250918|Exploring the Global-to-Local Attention Scheme in Graph Transformers An Empirical Study]] (80.7% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (80.6% similar)
- [[Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation A Robustness Analysis]] (80.4% similar)
- [[Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community Guiding the Fairness of Graphs via New Links]] (78.6% similar)

## 📋 저자 정보

**Authors:** Junzhi She, Xunkai Li, Rong-Hua Li, Guoren Wang

## 📄 Abstract (원문)

Directed graphs are ubiquitous across numerous domains, where the
directionality of edges encodes critical causal dependencies. However, existing
GNNs and graph Transformers tailored for directed graphs face two major
challenges: (1) effectively capturing long-range causal dependencies derived
from directed edges; (2) balancing accuracy and training efficiency when
processing large-scale graph datasets. In recent years, state space models
(SSMs) have achieved substantial progress in causal sequence tasks, and their
variants designed for graphs have demonstrated state-of-the-art accuracy while
maintaining high efficiency across various graph learning benchmarks. However,
existing graph state space models are exclusively designed for undirected
graphs, which limits their performance in directed graph learning. To this end,
we propose an innovative approach DirEgo2Token which sequentializes directed
graphs via k-hop ego graphs. This marks the first systematic extension of state
space models to the field of directed graph learning. Building upon this, we
develop DirGraphSSM, a novel directed graph neural network architecture that
implements state space models on directed graphs via the message-passing
mechanism. Experimental results demonstrate that DirGraphSSM achieves
state-of-the-art performance on three representative directed graph learning
tasks while attaining competitive performance on two additional tasks with
1.5$\times $ to 2$\times $ training speed improvements compared to existing
state-of-the-art models.

## 🔍 Abstract (한글 번역)

방향 그래프는 여러 분야에서 널리 사용되며, 여기서 간선의 방향성은 중요한 인과적 의존성을 암호화합니다. 그러나 방향 그래프에 맞춰진 기존의 그래프 신경망(GNN)과 그래프 트랜스포머는 두 가지 주요 과제에 직면해 있습니다: (1) 방향 간선에서 파생된 장거리 인과적 의존성을 효과적으로 포착하는 것; (2) 대규모 그래프 데이터셋을 처리할 때 정확성과 학습 효율성의 균형을 맞추는 것. 최근 몇 년간 상태 공간 모델(SSM)은 인과적 순차 작업에서 상당한 진전을 이루었으며, 그래프를 위해 설계된 그 변형들은 다양한 그래프 학습 벤치마크에서 높은 효율성을 유지하면서 최첨단 정확성을 입증했습니다. 그러나 기존의 그래프 상태 공간 모델은 무방향 그래프에만 설계되어 있어 방향 그래프 학습에서의 성능이 제한됩니다. 이를 해결하기 위해 우리는 k-hop 에고 그래프를 통해 방향 그래프를 순차화하는 혁신적인 접근법인 DirEgo2Token을 제안합니다. 이는 상태 공간 모델을 방향 그래프 학습 분야로 체계적으로 확장한 최초의 사례입니다. 이를 바탕으로 우리는 메시지 전달 메커니즘을 통해 방향 그래프에서 상태 공간 모델을 구현하는 새로운 방향 그래프 신경망 아키텍처인 DirGraphSSM을 개발했습니다. 실험 결과, DirGraphSSM은 세 가지 대표적인 방향 그래프 학습 과제에서 최첨단 성능을 달성했으며, 추가적인 두 가지 과제에서도 경쟁력 있는 성능을 보이며 기존 최첨단 모델에 비해 1.5배에서 2배의 학습 속도 향상을 이루었습니다.

## 📝 요약

이 논문은 방향성 그래프의 학습을 위한 새로운 접근법인 DirEgo2Token과 DirGraphSSM을 제안합니다. 기존의 그래프 신경망과 트랜스포머가 방향성 그래프에서 장거리 인과 관계를 효과적으로 포착하지 못하고, 대규모 데이터셋에서의 효율성과 정확성 균형 문제를 해결하지 못하는 한계를 극복하고자 합니다. DirEgo2Token은 k-hop 에고 그래프를 통해 방향성 그래프를 순차화하며, DirGraphSSM은 메시지 전달 메커니즘을 통해 방향성 그래프에 상태 공간 모델을 구현합니다. 실험 결과, DirGraphSSM은 세 가지 대표적인 방향성 그래프 학습 과제에서 최첨단 성능을 보였으며, 두 가지 추가 과제에서도 기존 모델 대비 1.5배에서 2배의 학습 속도 향상을 이루었습니다.

## 🎯 주요 포인트

- 1. 기존의 GNNs와 그래프 트랜스포머는 방향성 그래프에서 장거리 인과 의존성을 효과적으로 포착하는 데 어려움을 겪고 있습니다.

- 2. 상태 공간 모델(SSM)은 인과 시퀀스 작업에서 상당한 진전을 이루었으며, 그래프 변형 모델은 높은 효율성을 유지하면서 최첨단 정확도를 보여주었습니다.

- 3. 기존의 그래프 상태 공간 모델은 무방향 그래프에만 설계되어 방향성 그래프 학습에서 성능이 제한됩니다.

- 4. DirEgo2Token 접근법은 k-hop 에고 그래프를 통해 방향성 그래프를 순차화하여 상태 공간 모델을 방향성 그래프 학습 분야로 확장합니다.

- 5. DirGraphSSM은 메시지 전달 메커니즘을 통해 방향성 그래프에 상태 공간 모델을 구현하여 세 가지 대표적인 방향성 그래프 학습 작업에서 최첨단 성능을 달성했습니다.

---

*Generated on 2025-09-20 09:37:17*