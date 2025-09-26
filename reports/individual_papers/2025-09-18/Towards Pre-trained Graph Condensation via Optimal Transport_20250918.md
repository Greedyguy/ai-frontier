---
keywords:
  - Graph Neural Networks
  - Graph Condensation
  - Optimal Transport
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:04:25.878984",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Graph Condensation",
    "Optimal Transport"
  ],
  "rejected_keywords": [
    "Semantic Harmonizer",
    "Uncertainty Quantification"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.8,
    "Graph Condensation": 0.78,
    "Optimal Transport": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Towards Pre-trained Graph Condensation via Optimal Transport

**Korean Title:** 최적 수송을 통한 사전 학습된 그래프 응축 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]]
**⚡ Unique Technical**: [[keywords/Graph Condensation|Graph Condensation]], [[keywords/Optimal Transport|Optimal Transport]]

## 🔗 유사한 논문
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (83.0% similar)
- [[Exploring the Global-to-Local Attention Scheme in Graph Transformers_ An Empirical Study_20250918|Exploring the Global-to-Local Attention Scheme in Graph Transformers An Empirical Study]] (80.8% similar)
- [[Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community Guiding the Fairness of Graphs via New Links]] (80.4% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (79.7% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (79.5% similar)

## 📋 저자 정보

**Authors:** Yeyu Yan, Shuai Zheng, Wenjun Hui, Xiangkai Zhu, Dong Chen, Zhenfeng Zhu, Yao Zhao, Kunlun He

## 📄 Abstract (원문)

Graph condensation (GC) aims to distill the original graph into a small-scale
graph, mitigating redundancy and accelerating GNN training. However,
conventional GC approaches heavily rely on rigid GNNs and task-specific
supervision. Such a dependency severely restricts their reusability and
generalization across various tasks and architectures. In this work, we revisit
the goal of ideal GC from the perspective of GNN optimization consistency, and
then a generalized GC optimization objective is derived, by which those
traditional GC methods can be viewed nicely as special cases of this
optimization paradigm. Based on this, Pre-trained Graph Condensation (PreGC)
via optimal transport is proposed to transcend the limitations of task- and
architecture-dependent GC methods. Specifically, a hybrid-interval graph
diffusion augmentation is presented to suppress the weak generalization ability
of the condensed graph on particular architectures by enhancing the uncertainty
of node states. Meanwhile, the matching between optimal graph transport plan
and representation transport plan is tactfully established to maintain semantic
consistencies across source graph and condensed graph spaces, thereby freeing
graph condensation from task dependencies. To further facilitate the adaptation
of condensed graphs to various downstream tasks, a traceable semantic
harmonizer from source nodes to condensed nodes is proposed to bridge semantic
associations through the optimized representation transport plan in
pre-training. Extensive experiments verify the superiority and versatility of
PreGC, demonstrating its task-independent nature and seamless compatibility
with arbitrary GNNs.

## 🔍 Abstract (한글 번역)

그래프 응축(GC)은 원래 그래프를 소규모 그래프로 증류하여 중복성을 줄이고 GNN 훈련을 가속화하는 것을 목표로 합니다. 그러나 기존의 GC 접근 방식은 경직된 GNN과 특정 작업에 대한 감독에 크게 의존합니다. 이러한 의존성은 다양한 작업과 아키텍처에 걸쳐 재사용성과 일반화를 심각하게 제한합니다. 본 연구에서는 GNN 최적화 일관성의 관점에서 이상적인 GC의 목표를 재검토하고, 이를 통해 전통적인 GC 방법들이 이 최적화 패러다임의 특별한 사례로 간주될 수 있는 일반화된 GC 최적화 목표를 도출합니다. 이를 바탕으로 최적 수송을 통한 사전 훈련된 그래프 응축(PreGC)이 제안되어 작업 및 아키텍처 의존적인 GC 방법의 한계를 초월합니다. 구체적으로, 특정 아키텍처에서 응축된 그래프의 약한 일반화 능력을 억제하기 위해 하이브리드 간격 그래프 확산 증강이 제시되어 노드 상태의 불확실성을 강화합니다. 동시에, 최적 그래프 수송 계획과 표현 수송 계획 간의 매칭이 교묘하게 설정되어 소스 그래프와 응축된 그래프 공간 간의 의미적 일관성을 유지함으로써 그래프 응축을 작업 의존성에서 해방시킵니다. 응축된 그래프의 다양한 다운스트림 작업에 대한 적응을 더욱 촉진하기 위해, 사전 훈련에서 최적화된 표현 수송 계획을 통해 소스 노드와 응축 노드 간의 의미적 연관성을 연결하는 추적 가능한 의미 조화기가 제안됩니다. 광범위한 실험을 통해 PreGC의 우수성과 다재다능함이 검증되었으며, 작업 독립적인 특성과 임의의 GNN과의 원활한 호환성을 입증합니다.

## 📝 요약

그래프 응축(GC)은 원래 그래프를 작은 규모로 축소하여 중복을 줄이고 GNN 훈련을 가속화하는 것을 목표로 합니다. 기존 GC 방법은 특정 과제와 아키텍처에 의존하여 재사용성과 일반화가 제한됩니다. 본 연구에서는 GNN 최적화 일관성 관점에서 이상적인 GC 목표를 재검토하고, 이를 통해 전통적인 GC 방법을 특수 사례로 볼 수 있는 일반화된 GC 최적화 목표를 도출했습니다. 이를 기반으로, 최적 수송을 통한 사전 훈련 그래프 응축(PreGC)을 제안하여 과제 및 아키텍처 의존성을 초월합니다. 하이브리드 간격 그래프 확산 증강을 통해 특정 아키텍처에서 응축 그래프의 일반화 능력을 향상시키고, 최적 그래프 수송 계획과 표현 수송 계획 간의 매칭을 통해 의미적 일관성을 유지합니다. 또한, 다양한 다운스트림 작업에 적응할 수 있도록 소스 노드와 응축 노드 간의 의미적 연결을 위한 추적 가능한 의미 조화기를 제안합니다. 실험 결과, PreGC의 우수성과 범용성이 입증되었으며, 과제 독립적 특성과 다양한 GNN과의 호환성을 보여주었습니다.

## 🎯 주요 포인트

- 1. 그래프 응축(GC)은 원래 그래프를 소규모 그래프로 압축하여 중복성을 줄이고 GNN 훈련을 가속화하는 것을 목표로 합니다.

- 2. 기존의 GC 방법은 경직된 GNN과 특정 과제에 대한 감독에 크게 의존하여 재사용성과 일반화를 제한합니다.

- 3. 본 연구에서는 GNN 최적화 일관성 관점에서 이상적인 GC 목표를 재검토하고, 이를 바탕으로 일반화된 GC 최적화 목표를 도출합니다.

- 4. 최적 운송을 통한 사전 훈련 그래프 응축(PreGC)은 과제 및 아키텍처 의존성을 초월하여 그래프 응축의 한계를 극복합니다.

- 5. PreGC는 다양한 GNN과의 호환성을 유지하면서 과제 독립적인 특성을 입증하여 우수성과 다재다능성을 보여줍니다.

---

*Generated on 2025-09-20 05:44:49*