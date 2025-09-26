---
keywords:
  - Graph Neural Networks
  - Optimization
  - Partial Separability
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:57:31.935274",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Optimization",
    "Partial Separability"
  ],
  "rejected_keywords": [
    "Randomized Local Coordination"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.82,
    "Optimization": 0.78,
    "Partial Separability": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Decentralized Optimization with Topology-Independent Communication

**Korean Title:** 토폴로지 독립적 통신을 통한 분산 최적화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Distributed optimization]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph-guided regularizers]]
**⚡ Unique Technical**: [[keywords/Partial Separability|Partial separability]]

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (84.5% similar)
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (83.6% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (81.4% similar)
- [[Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters_20250919|Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters]] (79.7% similar)
- [[Sampling Method for Generalized Graph Signals with Pre-selected Vertices via DC Optimization_20250918|Sampling Method for Generalized Graph Signals with Pre-selected Vertices via DC Optimization]] (79.6% similar)

## 📋 저자 정보

**Authors:** Ying Lin, Yao Kuang, Ahmet Alacaoglu, Michael P. Friedlander

## 📄 Abstract (원문)

Distributed optimization requires nodes to coordinate, yet full
synchronization scales poorly. When $n$ nodes collaborate through $m$ pairwise
regularizers, standard methods demand $\mathcal{O}(m)$ communications per
iteration. This paper proposes randomized local coordination: each node
independently samples one regularizer uniformly and coordinates only with nodes
sharing that term. This exploits partial separability, where each regularizer
$G_j$ depends on a subset $S_j \subseteq \{1,\ldots,n\}$ of nodes. For
graph-guided regularizers where $|S_j|=2$, expected communication drops to
exactly 2 messages per iteration. This method achieves
$\tilde{\mathcal{O}}(\varepsilon^{-2})$ iterations for convex objectives and
under strong convexity, $\mathcal{O}(\varepsilon^{-1})$ to an
$\varepsilon$-solution and $\mathcal{O}(\log(1/\varepsilon))$ to a
neighborhood. Replacing the proximal map of the sum $\sum_j G_j$ with the
proximal map of a single randomly selected regularizer $G_j$ preserves
convergence while eliminating global coordination. Experiments validate both
convergence rates and communication efficiency across synthetic and real-world
datasets.

## 🔍 Abstract (한글 번역)

분산 최적화는 노드들이 협력해야 하지만, 완전한 동기화는 확장성이 좋지 않습니다. $n$개의 노드가 $m$개의 쌍별 정규화 항을 통해 협력할 때, 표준 방법은 각 반복마다 $\mathcal{O}(m)$의 통신을 요구합니다. 본 논문은 무작위 지역 협력을 제안합니다: 각 노드는 독립적으로 하나의 정규화 항을 균등하게 샘플링하고, 그 항을 공유하는 노드들과만 협력합니다. 이는 각 정규화 항 $G_j$가 노드의 부분 집합 $S_j \subseteq \{1,\ldots,n\}$에 의존하는 부분적 분리 가능성을 활용합니다. $|S_j|=2$인 그래프 유도 정규화 항의 경우, 기대되는 통신량은 반복당 정확히 2개의 메시지로 감소합니다. 이 방법은 볼록 목적 함수에 대해 $\tilde{\mathcal{O}}(\varepsilon^{-2})$의 반복을 달성하며, 강한 볼록성 하에서는 $\varepsilon$-해에 대해 $\mathcal{O}(\varepsilon^{-1})$ 및 근방에 대해 $\mathcal{O}(\log(1/\varepsilon))$의 반복을 달성합니다. $\sum_j G_j$의 근사 사상(proximal map)을 단일 무작위로 선택된 정규화 항 $G_j$의 근사 사상으로 대체함으로써, 전역 협력을 제거하면서 수렴성을 유지합니다. 실험은 합성 및 실제 데이터셋에서 수렴 속도와 통신 효율성을 모두 검증합니다.

## 📝 요약

이 논문은 분산 최적화에서 노드 간의 완전한 동기화가 비효율적이라는 문제를 해결하기 위해 무작위 로컬 조정 방법을 제안합니다. 각 노드는 독립적으로 하나의 정규화 항을 샘플링하고 해당 항을 공유하는 노드와만 조정합니다. 이 방법은 부분 가분성을 활용하여, 그래프 기반 정규화의 경우 통신량을 반복당 평균 2개의 메시지로 줄입니다. 제안된 방법은 볼록 목적 함수에 대해 $\tilde{\mathcal{O}}(\varepsilon^{-2})$의 반복을 달성하며, 강한 볼록성 하에서는 $\varepsilon$-해에 대해 $\mathcal{O}(\varepsilon^{-1})$, $\varepsilon$-근방에 대해 $\mathcal{O}(\log(1/\varepsilon))$의 반복을 필요로 합니다. 실험 결과는 제안된 방법이 수렴 속도와 통신 효율성을 모두 향상시킴을 보여줍니다.

## 🎯 주요 포인트

- 1. 분산 최적화에서 노드 간의 완전한 동기화는 확장성이 낮으며, 제안된 방법은 무작위 지역 조정을 통해 이를 개선합니다.

- 2. 각 노드는 독립적으로 하나의 규제자를 샘플링하고 해당 규제자를 공유하는 노드와만 조정하여 통신을 최소화합니다.

- 3. 그래프 기반 규제자의 경우, 기대되는 통신 횟수는 반복당 정확히 2개의 메시지로 감소합니다.

- 4. 제안된 방법은 볼록 목적 함수에 대해 $\tilde{\mathcal{O}}(\varepsilon^{-2})$ 반복을 달성하며, 강한 볼록성 하에서는 $\varepsilon$-해에 대해 $\mathcal{O}(\varepsilon^{-1})$ 반복을, 근방에서는 $\mathcal{O}(\log(1/\varepsilon))$ 반복을 달성합니다.

- 5. 실험 결과는 제안된 방법의 수렴 속도와 통신 효율성을 입증합니다.

---

*Generated on 2025-09-20 05:54:34*