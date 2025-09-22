# Modeling Transformers as complex networks to analyze learning dynamics

**Korean Title:** 트랜스포머를 복잡한 네트워크로 모델링하여 학습 동역학 분석하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Stable Hierarchy of Information Spreader Components

## 🔗 유사한 논문
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (84.9% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (83.3% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (83.0% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.8% similar)
- [[2025-09-22/Knowledge-Driven Hallucination in Large Language Models_ An Empirical Study on Process Modeling_20250922|Knowledge-Driven Hallucination in Large Language Models An Empirical Study on Process Modeling]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15269v1 Announce Type: cross 
Abstract: The process by which Large Language Models (LLMs) acquire complex capabilities during training remains a key open question in mechanistic interpretability. This project investigates whether these learning dynamics can be characterized through the lens of Complex Network Theory (CNT). I introduce a novel methodology to represent a Transformer-based LLM as a directed, weighted graph where nodes are the model's computational components (attention heads and MLPs) and edges represent causal influence, measured via an intervention-based ablation technique. By tracking the evolution of this component-graph across 143 training checkpoints of the Pythia-14M model on a canonical induction task, I analyze a suite of graph-theoretic metrics. The results reveal that the network's structure evolves through distinct phases of exploration, consolidation, and refinement. Specifically, I identify the emergence of a stable hierarchy of information spreader components and a dynamic set of information gatherer components, whose roles reconfigure at key learning junctures. This work demonstrates that a component-level network perspective offers a powerful macroscopic lens for visualizing and understanding the self-organizing principles that drive the formation of functional circuits in LLMs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15269v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)이 훈련 중 복잡한 능력을 획득하는 과정은 기계적 해석 가능성에서 여전히 중요한 미해결 문제로 남아 있습니다. 이 프로젝트는 이러한 학습 동태가 복잡 네트워크 이론(CNT)의 관점에서 특성화될 수 있는지를 조사합니다. 저는 Transformer 기반 LLM을 방향성 가중 그래프로 표현하는 새로운 방법론을 소개합니다. 여기서 노드는 모델의 계산 구성 요소(어텐션 헤드와 MLP)이고, 엣지는 개입 기반 제거 기법을 통해 측정된 인과적 영향을 나타냅니다. Pythia-14M 모델의 표준 귀납 작업에 대한 143개의 훈련 체크포인트에 걸쳐 이 구성 요소 그래프의 진화를 추적함으로써, 저는 일련의 그래프 이론적 지표를 분석합니다. 결과는 네트워크의 구조가 탐색, 통합, 정제의 뚜렷한 단계를 통해 진화함을 보여줍니다. 구체적으로, 정보 확산 구성 요소의 안정적인 계층 구조의 출현과 정보 수집 구성 요소의 동적 집합을 식별했으며, 이들의 역할은 주요 학습 시점에서 재구성됩니다. 이 연구는 구성 요소 수준의 네트워크 관점이 LLM에서 기능적 회로 형성을 주도하는 자기 조직 원리를 시각화하고 이해하는 데 강력한 거시적 렌즈를 제공함을 입증합니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)이 훈련 중 복잡한 능력을 획득하는 과정을 복잡 네트워크 이론(CNT) 관점에서 분석합니다. 트랜스포머 기반 LLM을 방향성 가중 그래프로 표현하는 새로운 방법론을 제안하여, 모델의 계산 구성 요소(어텐션 헤드와 MLP)를 노드로, 개입 기반 절제 기법을 통해 인과적 영향을 나타내는 간선을 사용합니다. Pythia-14M 모델의 143개 훈련 체크포인트에서 구성 요소 그래프의 진화를 추적하며, 그래프 이론적 지표를 분석했습니다. 결과적으로 네트워크 구조가 탐색, 통합, 정제의 뚜렷한 단계를 거쳐 진화하며, 정보 확산 구성 요소의 안정적 계층과 동적 정보 수집 구성 요소가 주요 학습 시점에서 재구성됨을 발견했습니다. 이 연구는 구성 요소 수준의 네트워크 관점이 LLM의 기능적 회로 형성을 주도하는 자기 조직 원리를 이해하는 강력한 거시적 시각을 제공함을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 대형 언어 모델(LLM)의 학습 역학을 복잡 네트워크 이론(CNT)의 관점에서 설명할 수 있는지를 조사합니다.

- 2. Transformer 기반 LLM을 방향성 있는 가중 그래프로 표현하는 새로운 방법론을 제안합니다.

- 3. Pythia-14M 모델의 143개 학습 체크포인트를 통해 그래프 이론적 메트릭을 분석하여 네트워크 구조가 탐색, 통합, 정제의 단계를 거쳐 진화함을 발견했습니다.

- 4. 정보 확산 구성 요소의 안정적인 계층 구조와 정보 수집 구성 요소의 동적 집합이 학습의 주요 시점에서 재구성되는 것을 확인했습니다.

- 5. 구성 요소 수준의 네트워크 관점이 LLM의 기능적 회로 형성을 주도하는 자기 조직화 원리를 시각화하고 이해하는 강력한 거시적 관점을 제공함을 보여줍니다.

---

*Generated on 2025-09-22 13:51:43*