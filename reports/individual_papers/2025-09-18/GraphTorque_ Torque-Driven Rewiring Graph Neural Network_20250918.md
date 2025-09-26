---
keywords:
  - Graph Neural Networks
  - Graph Rewiring
  - Torque-Driven Hierarchical Rewiring
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2507.21422
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:26:32.455255",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Graph Rewiring",
    "Torque-Driven Hierarchical Rewiring"
  ],
  "rejected_keywords": [
    "Heterophilous Graphs"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.8,
    "Graph Rewiring": 0.7,
    "Torque-Driven Hierarchical Rewiring": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# GraphTorque: Torque-Driven Rewiring Graph Neural Network

**Korean Title:** 그래프토크: 토크 주도 재배선 그래프 신경망

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]]
**⚡ Unique Technical**: [[keywords/Graph Rewiring|graph rewiring]], [[keywords/Torque-Driven Hierarchical Rewiring|torque-driven hierarchical rewiring]]

## 🔗 유사한 논문
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (79.3% similar)
- [[NIRVANA: Structured pruning reimagined for large language models compression]] (78.6% similar)
- [[Multimodal Hate Detection Using Dual-Stream Graph Neural Networks]] (78.3% similar)
- [[Evolution Meets Diffusion: Efficient Neural Architecture Generation]] (78.2% similar)
- [[Soft_Graph_Transformer_for_MIMO_Detection_20250918|Soft Graph Transformer for MIMO Detection]] (77.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.21422v2 Announce Type: replace 
Abstract: Graph Neural Networks (GNNs) have emerged as powerful tools for learning from graph-structured data, leveraging message passing to diffuse information and update node representations. However, most efforts have suggested that native interactions encoded in the graph may not be friendly for this process, motivating the development of graph rewiring methods. In this work, we propose a torque-driven hierarchical rewiring strategy, inspired by the notion of torque in classical mechanics, dynamically modulating message passing to improve representation learning in heterophilous graphs and enhance robustness against noisy graphs. Specifically, we define an interference-aware torque metric that integrates structural distance and energy scores to quantify the perturbation induced by edges, thereby encouraging each node to aggregate information from its nearest low-energy neighbors. We use the metric to hierarchically reconfigure the receptive field of each layer by judiciously pruning high-torque edges and adding low-torque links, suppressing propagation noise and boosting pertinent signals. Extensive evaluations on benchmark datasets show that our approach surpasses state-of-the-art methods on both heterophilous and homophilous graphs, and maintains high accuracy on noisy graph.

## 🔍 Abstract (한글 번역)

arXiv:2507.21422v2 발표 유형: 대체
요약: 그래프 신경망(GNNs)은 그래프 구조화된 데이터로부터 학습하는 강력한 도구로 등장했으며, 메시지 전달을 활용하여 정보를 확산시키고 노드 표현을 업데이트합니다. 그러나 대부분의 노력은 그래프에 인코딩된 원시 상호작용이 이 프로세스에 적합하지 않을 수 있다는 것을 제안했으며, 이로 인해 그래프 재배선 방법의 발전이 동기부여되었습니다. 본 연구에서는 고전 역학의 토크 개념에서 영감을 받은 토크 주도의 계층적 재배선 전략을 제안합니다. 이는 이질적 그래프에서 표현 학습을 개선하고 잡음이 있는 그래프에 대한 강건성을 향상시키기 위해 메시지 전달을 동적으로 조절합니다. 구체적으로, 우리는 각 노드가 가장 가까운 저에너지 이웃으로부터 정보를 집계하도록 장려하기 위해 엣지에 의해 유발된 교란을 양적하는 구조적 거리와 에너지 점수를 통합하는 인터퍼런스 인식 토크 메트릭을 정의합니다. 우리는 이 메트릭을 사용하여 고토크 엣지를 신중하게 제거하고 저토크 링크를 추가하여 각 층의 수용 영역을 계층적으로 재구성하여 전파 잡음을 억제하고 적절한 신호를 강화합니다. 벤치마크 데이터셋에서의 포괄적인 평가 결과, 우리의 접근 방식이 이질적 및 동질적 그래프 모두에서 최첨단 방법을 능가하고 잡음이 있는 그래프에서도 높은 정확도를 유지함을 보여줍니다.

## 📝 요약

이 논문은 그래프 신경망(GNNs)이 그래프 구조 데이터로부터 학습하는 강력한 도구로 떠오르면서, 메시지 전달을 활용하여 정보를 확산시키고 노드 표현을 업데이트하는 방법에 중점을 두고 있다. 그러나 대부분의 노력은 그래프에 인코딩된 원시 상호작용이 이 프로세스에 적합하지 않을 수 있다고 제안하며, 그래프 재배선 방법의 발전을 도모하고 있다. 본 연구에서는 고전역학의 토크 개념에서 영감을 받은 토크 주도의 계층적 재배선 전략을 제안한다. 이를 통해 메시지 전달을 동적으로 변형하여 이종 그래프에서 표현 학습을 개선하고 잡음이 있는 그래프에 대한 강건성을 향상시킨다. 구조적 거리와 에너지 점수를 통합한 간섭 인식 토크 메트릭을 정의하여 에지에 의해 유발된 섭동을 측정하고, 각 노드가 가장 가까운 저에너지 이웃으로부터 정보를 집계하도록 장려한다. 이 메트릭을 사용하여 각 층의 수용 영역을 계층적으로 재구성하고, 고 토크 에지를 신중하게 제거하고 저 토크 링크를 추가하여 전파 잡음을 억제하고 적절한 신호를 강화한다. 벤치마크 데이터셋에서의 포괄적인 평가 결과, 본 접근 방식이 이종 및 동종 그래프에서 최신 기술 방법을 능가하며, 잡음이 있는 그래프에서도 높은 정확도를 유지한다.

## 🎯 주요 포인트

- 1. 그래프 신경망은 그래프 구조화된 데이터로부터 학습하는 강력한 도구로 부상하고 있으며, 메시지 전달을 통해 정보를 확산시키고 노드 표현을 업데이트합니다.

- 2. 그래프의 원래 상호작용은 이 프로세스에 적합하지 않을 수 있으며, 그래프 재배선 방법의 발전을 촉발합니다.

- 3. 토크에 영감을 받은 계층적 재배선 전략을 제안하며, 메시지 전달을 동적으로 변조하여 이종 그래프에서 표현 학습을 개선하고 잡음 그래프에 대한 강건성을 향상시킵니다.

---

*Generated on 2025-09-18 16:47:32*