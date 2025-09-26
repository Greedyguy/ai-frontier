<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:04:02.281271",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Flexible Gradient Tracking",
    "Accelerated Flexible Gradient Tracking",
    "Pareto-optimal Trade-off",
    "Nonconvex Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Flexible Gradient Tracking": 0.8,
    "Accelerated Flexible Gradient Tracking": 0.78,
    "Pareto-optimal Trade-off": 0.75,
    "Nonconvex Optimization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FlexGT",
        "canonical": "Flexible Gradient Tracking",
        "aliases": [
          "FlexGT"
        ],
        "category": "unique_technical",
        "rationale": "FlexGT is a novel method introduced in the paper, offering a unique approach to distributed optimization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Acc-FlexGT",
        "canonical": "Accelerated Flexible Gradient Tracking",
        "aliases": [
          "Acc-FlexGT"
        ],
        "category": "unique_technical",
        "rationale": "Acc-FlexGT is an accelerated variant of FlexGT, providing a specific enhancement to the method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pareto-optimal trade-off",
        "canonical": "Pareto-optimal Trade-off",
        "aliases": [
          "Pareto-optimal"
        ],
        "category": "specific_connectable",
        "rationale": "The concept of Pareto-optimal trade-offs is central to balancing communication and computation in optimization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "nonconvex case",
        "canonical": "Nonconvex Optimization",
        "aliases": [
          "nonconvex"
        ],
        "category": "broad_technical",
        "rationale": "Nonconvex optimization is a fundamental concept in the paper's analysis of convergence rates.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "efficiency",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "FlexGT",
      "resolved_canonical": "Flexible Gradient Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Acc-FlexGT",
      "resolved_canonical": "Accelerated Flexible Gradient Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pareto-optimal trade-off",
      "resolved_canonical": "Pareto-optimal Trade-off",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "nonconvex case",
      "resolved_canonical": "Nonconvex Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Pareto-optimal Tradeoffs Between Communication and Computation with Flexible Gradient Tracking

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18129.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18129](https://arxiv.org/abs/2509.18129)

## 🔗 유사한 논문
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (86.1% similar)
- [[2025-09-24/A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization_20250924|A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization]] (84.3% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (84.0% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (82.5% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonconvex Optimization|Nonconvex Optimization]]
**🔗 Specific Connectable**: [[keywords/Pareto-optimal Trade-off|Pareto-optimal Trade-off]]
**⚡ Unique Technical**: [[keywords/Flexible Gradient Tracking|Flexible Gradient Tracking]], [[keywords/Accelerated Flexible Gradient Tracking|Accelerated Flexible Gradient Tracking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18129v1 Announce Type: cross 
Abstract: This paper addresses distributed optimization problems in non-i.i.d. scenarios, focusing on the interplay between communication and computation efficiency. To this end, we propose FlexGT, a flexible snapshot gradient tracking method with tunable numbers of local updates and neighboring communications in each round. Leveraging a unified convergence analysis framework, we prove that FlexGT achieves a linear or sublinear convergence rate depending on objective-specific properties--from (strongly) convex to nonconvex--and the above-mentioned tunable parameters. FlexGT is provably robust to the heterogeneity across nodes and attains the best-known communication and computation complexity among existing results. Moreover, we introduce an accelerated gossip-based variant, termed Acc-FlexGT, and show that with prior knowledge of the graph, it achieves a Pareto-optimal trade-off between communication and computation. Particularly, Acc-FlexGT achieves the optimal iteration complexity of $\tilde{\mathcal{O}} \left( L/\epsilon +L\sigma ^2/\left( n\epsilon^2 \sqrt{1-\sqrt{\rho _W}} \right) \right) $ for the nonconvex case, matching the existing lower bound up to a logarithmic factor, and improves the existing results for the strongly convex case by a factor of $\tilde{\mathcal{O}} \left( 1/\sqrt{\epsilon} \right)$, where $\epsilon$ is the targeted accuracy, $n$ the number of nodes, $L$ the Lipschitz constant, $\rho_W$ the spectrum gap of the graph, and $\sigma$ the stochastic gradient variance. Numerical examples are provided to demonstrate the effectiveness of the proposed methods.

## 📝 요약

이 논문은 비독립적이고 동일한 분포가 아닌(non-i.i.d.) 상황에서의 분산 최적화 문제를 다루며, 통신과 계산 효율성 간의 상호작용에 중점을 둡니다. 이를 위해, 각 라운드에서 조정 가능한 로컬 업데이트와 이웃 간 통신 횟수를 가진 유연한 스냅샷 그래디언트 추적 방법인 FlexGT를 제안합니다. 통합된 수렴 분석 프레임워크를 활용하여, FlexGT가 (강)볼록에서 비볼록까지의 목표 특성에 따라 선형 또는 아선형 수렴 속도를 달성함을 증명합니다. FlexGT는 노드 간 이질성에 강인하며, 기존 결과 중 최상의 통신 및 계산 복잡성을 달성합니다. 또한, 가속화된 가십 기반 변형인 Acc-FlexGT를 도입하여, 그래프에 대한 사전 지식을 통해 통신과 계산 간의 파레토 최적 균형을 달성함을 보여줍니다. 특히, Acc-FlexGT는 비볼록 경우에 대해 최적의 반복 복잡도를 달성하며, 강볼록 경우에 대해 기존 결과를 개선합니다. 수치 예시를 통해 제안된 방법의 효과를 입증합니다.

## 🎯 주요 포인트

- 1. FlexGT는 각 라운드에서 조정 가능한 로컬 업데이트와 이웃 간 통신 횟수를 통해 비독립적 분포 시나리오에서의 분산 최적화 문제를 해결합니다.
- 2. FlexGT는 (강)볼록부터 비볼록까지의 목표 특성에 따라 선형 또는 아선형 수렴 속도를 달성하며, 노드 간 이질성에 강인한 성능을 보입니다.
- 3. Acc-FlexGT는 그래프의 사전 지식을 활용하여 통신과 계산 사이의 파레토 최적의 균형을 이루며, 비볼록 경우에 대해 최적의 반복 복잡도를 달성합니다.
- 4. Acc-FlexGT는 강볼록 경우에 대해 기존 결과를 $\tilde{\mathcal{O}} \left( 1/\sqrt{\epsilon} \right)$ 만큼 개선하며, 이는 목표 정확도 $\epsilon$, 노드 수 $n$, 리프시츠 상수 $L$, 그래프의 스펙트럼 갭 $\rho_W$, 확률적 기울기 분산 $\sigma$에 따라 달라집니다.
- 5. 제안된 방법의 효과를 입증하기 위해 수치적 예시가 제공됩니다.


---

*Generated on 2025-09-24 15:04:02*