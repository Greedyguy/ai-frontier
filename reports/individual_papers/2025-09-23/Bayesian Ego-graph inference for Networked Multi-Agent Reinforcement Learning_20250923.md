---
keywords:
  - Bayesian Variational Inference
  - Networked Multi-Agent Reinforcement Learning
  - Ego-graph
  - Evidence Lower Bound
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16606
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:11:28.472681",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Variational Inference",
    "Networked Multi-Agent Reinforcement Learning",
    "Ego-graph",
    "Evidence Lower Bound"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Variational Inference": 0.85,
    "Networked Multi-Agent Reinforcement Learning": 0.79,
    "Ego-graph": 0.77,
    "Evidence Lower Bound": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian variational inference",
        "canonical": "Bayesian Variational Inference",
        "aliases": [
          "Bayesian VI"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for learning interaction structures in decentralized systems, enhancing connectivity with other inference methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Networked Multi-Agent Reinforcement Learning",
        "canonical": "Networked Multi-Agent Reinforcement Learning",
        "aliases": [
          "Networked-MARL"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific domain of reinforcement learning that focuses on decentralized agents, linking to broader MARL concepts.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Ego-graph",
        "canonical": "Ego-graph",
        "aliases": [
          "Ego network"
        ],
        "category": "unique_technical",
        "rationale": "Ego-graphs are central to the proposed framework, offering a unique perspective on agent interactions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.64,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Evidence Lower Bound",
        "canonical": "Evidence Lower Bound",
        "aliases": [
          "ELBO"
        ],
        "category": "specific_connectable",
        "rationale": "ELBO is a key objective function in variational inference, connecting to broader probabilistic models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian variational inference",
      "resolved_canonical": "Bayesian Variational Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Networked Multi-Agent Reinforcement Learning",
      "resolved_canonical": "Networked Multi-Agent Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Ego-graph",
      "resolved_canonical": "Ego-graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.64,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Evidence Lower Bound",
      "resolved_canonical": "Evidence Lower Bound",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# Bayesian Ego-graph inference for Networked Multi-Agent Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16606.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16606](https://arxiv.org/abs/2509.16606)

## 🔗 유사한 논문
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (87.2% similar)
- [[2025-09-23/HypeMARL_ Multi-Agent Reinforcement Learning For High-Dimensional, Parametric, and Distributed Systems_20250923|HypeMARL: Multi-Agent Reinforcement Learning For High-Dimensional, Parametric, and Distributed Systems]] (85.8% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (84.4% similar)
- [[2025-09-19/Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning_20250919|Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning]] (84.0% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Bayesian Variational Inference|Bayesian Variational Inference]], [[keywords/Evidence Lower Bound|Evidence Lower Bound]]
**⚡ Unique Technical**: [[keywords/Networked Multi-Agent Reinforcement Learning|Networked Multi-Agent Reinforcement Learning]], [[keywords/Ego-graph|Ego-graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16606v1 Announce Type: cross 
Abstract: In networked multi-agent reinforcement learning (Networked-MARL), decentralized agents must act under local observability and constrained communication over fixed physical graphs. Existing methods often assume static neighborhoods, limiting adaptability to dynamic or heterogeneous environments. While centralized frameworks can learn dynamic graphs, their reliance on global state access and centralized infrastructure is impractical in real-world decentralized systems. We propose a stochastic graph-based policy for Networked-MARL, where each agent conditions its decision on a sampled subgraph over its local physical neighborhood. Building on this formulation, we introduce BayesG, a decentralized actor-framework that learns sparse, context-aware interaction structures via Bayesian variational inference. Each agent operates over an ego-graph and samples a latent communication mask to guide message passing and policy computation. The variational distribution is trained end-to-end alongside the policy using an evidence lower bound (ELBO) objective, enabling agents to jointly learn both interaction topology and decision-making strategies. BayesG outperforms strong MARL baselines on large-scale traffic control tasks with up to 167 agents, demonstrating superior scalability, efficiency, and performance.

## 📝 요약

이 논문은 네트워크 기반 다중 에이전트 강화 학습(Networked-MARL)에서 에이전트들이 지역 관찰성과 제한된 통신 환경에서 작동해야 하는 문제를 다룹니다. 기존 방법들은 정적 이웃을 가정하여 동적 또는 이질적인 환경에 적응하기 어렵다는 한계가 있습니다. 이를 해결하기 위해, 각 에이전트가 자신의 지역 물리적 이웃 내에서 샘플링된 부분 그래프를 기반으로 결정을 내리는 확률적 그래프 기반 정책을 제안합니다. 이 접근법을 바탕으로, 우리는 BayesG라는 분산형 액터 프레임워크를 소개합니다. BayesG는 베이지안 변분 추론을 통해 희소하고 상황 인식적인 상호작용 구조를 학습하며, 각 에이전트는 자아 그래프를 기반으로 잠재 통신 마스크를 샘플링하여 메시지 전달과 정책 계산을 안내합니다. 이 변분 분포는 증거 하한(ELBO) 목표를 사용하여 정책과 함께 학습되어, 에이전트들이 상호작용 토폴로지와 의사결정 전략을 동시에 학습할 수 있게 합니다. BayesG는 최대 167개의 에이전트가 참여하는 대규모 교통 제어 작업에서 뛰어난 확장성, 효율성 및 성능을 보여 기존의 MARL 기준선을 능가합니다.

## 🎯 주요 포인트

- 1. 네트워크 기반 다중 에이전트 강화 학습(Networked-MARL)에서 에이전트는 로컬 관측성과 제한된 통신을 통해 작동해야 하며, 기존 방법은 정적 이웃을 가정하여 동적 또는 이질적인 환경에 적응하기 어렵습니다.
- 2. 제안된 확률적 그래프 기반 정책은 에이전트가 로컬 물리적 이웃에서 샘플링된 서브그래프에 따라 결정을 내리도록 하여, 중앙 집중식 시스템의 비현실적인 요구를 피합니다.
- 3. BayesG는 베이지안 변분 추론을 통해 희소하고 상황 인식적인 상호작용 구조를 학습하는 분산형 액터 프레임워크로, 각 에이전트가 자아 그래프를 기반으로 작동하며 잠재 통신 마스크를 샘플링하여 메시지 전달과 정책 계산을 안내합니다.
- 4. 변분 분포는 증거 하한(ELBO) 목표를 사용하여 정책과 함께 엔드 투 엔드로 훈련되며, 에이전트가 상호작용 토폴로지와 의사결정 전략을 공동으로 학습할 수 있게 합니다.
- 5. BayesG는 최대 167개의 에이전트가 참여하는 대규모 교통 제어 작업에서 강력한 MARL 기준선을 능가하여 우수한 확장성, 효율성 및 성능을 입증합니다.


---

*Generated on 2025-09-24 02:11:28*