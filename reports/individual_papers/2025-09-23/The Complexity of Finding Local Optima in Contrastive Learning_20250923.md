---
keywords:
  - Self-supervised Learning
  - Local Optima in Optimization
  - Polynomial Local Search
  - Continuous Local Search
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16898
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:44:38.201079",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Local Optima in Optimization",
    "Polynomial Local Search",
    "Continuous Local Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Local Optima in Optimization": 0.78,
    "Polynomial Local Search": 0.75,
    "Continuous Local Search": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Objective",
          "Contrastive Method"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a key technique within self-supervised learning, which is a trending topic in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Local Optima",
        "canonical": "Local Optima in Optimization",
        "aliases": [
          "Local Minimum",
          "Local Maximum"
        ],
        "category": "unique_technical",
        "rationale": "Understanding local optima is crucial for linking to optimization problems in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Polynomial Local Search",
        "canonical": "Polynomial Local Search",
        "aliases": [
          "PLS"
        ],
        "category": "unique_technical",
        "rationale": "PLS is a specific complexity class relevant to the paper's focus on optimization complexity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Continuous Local Search",
        "canonical": "Continuous Local Search",
        "aliases": [
          "CLS"
        ],
        "category": "unique_technical",
        "rationale": "CLS is another complexity class that provides insights into continuous optimization challenges.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "Triplet Loss",
      "Embeddings"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Local Optima",
      "resolved_canonical": "Local Optima in Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Polynomial Local Search",
      "resolved_canonical": "Polynomial Local Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Continuous Local Search",
      "resolved_canonical": "Continuous Local Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# The Complexity of Finding Local Optima in Contrastive Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16898.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16898](https://arxiv.org/abs/2509.16898)

## 🔗 유사한 논문
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (83.3% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (78.9% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (78.5% similar)
- [[2025-09-23/Local Mechanisms of Compositional Generalization in Conditional Diffusion_20250923|Local Mechanisms of Compositional Generalization in Conditional Diffusion]] (78.5% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Local Optima in Optimization|Local Optima in Optimization]], [[keywords/Polynomial Local Search|Polynomial Local Search]], [[keywords/Continuous Local Search|Continuous Local Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16898v1 Announce Type: new 
Abstract: Contrastive learning is a powerful technique for discovering meaningful data representations by optimizing objectives based on $\textit{contrastive information}$, often given as a set of weighted triplets $\{(x_i, y_i^+, z_{i}^-)\}_{i = 1}^m$ indicating that an "anchor" $x_i$ is more similar to a "positive" example $y_i$ than to a "negative" example $z_i$. The goal is to find representations (e.g., embeddings in $\mathbb{R}^d$ or a tree metric) where anchors are placed closer to positive than to negative examples. While finding $\textit{global}$ optima of contrastive objectives is $\mathsf{NP}$-hard, the complexity of finding $\textit{local}$ optima -- representations that do not improve by local search algorithms such as gradient-based methods -- remains open. Our work settles the complexity of finding local optima in various contrastive learning problems by proving $\mathsf{PLS}$-hardness in discrete settings (e.g., maximize satisfied triplets) and $\mathsf{CLS}$-hardness in continuous settings (e.g., minimize Triplet Loss), where $\mathsf{PLS}$ (Polynomial Local Search) and $\mathsf{CLS}$ (Continuous Local Search) are well-studied complexity classes capturing local search dynamics in discrete and continuous optimization, respectively. Our results imply that no polynomial time algorithm (local search or otherwise) can find a local optimum for various contrastive learning problems, unless $\mathsf{PLS}\subseteq\mathsf{P}$ (or $\mathsf{CLS}\subseteq \mathsf{P}$ for continuous problems). Even in the unlikely scenario that $\mathsf{PLS}\subseteq\mathsf{P}$ (or $\mathsf{CLS}\subseteq \mathsf{P}$), our reductions imply that there exist instances where local search algorithms need exponential time to reach a local optimum, even for $d=1$ (embeddings on a line).

## 📝 요약

이 논문은 대조 학습(contrastive learning)의 지역 최적화 문제의 복잡성을 해결합니다. 대조 학습은 데이터 표현을 찾기 위해 "앵커"가 "긍정" 예시보다 "부정" 예시에 더 가깝지 않도록 하는 목표를 최적화합니다. 전역 최적화는 $\mathsf{NP}$-난해하지만, 지역 최적화의 복잡성은 미지였습니다. 본 연구는 이 문제의 복잡성을 $\mathsf{PLS}$-난해성(이산 설정)과 $\mathsf{CLS}$-난해성(연속 설정)으로 증명했습니다. 이는 대조 학습 문제에서 다항 시간 알고리즘으로 지역 최적점을 찾는 것이 불가능함을 시사하며, 심지어 $d=1$인 경우에도 지역 탐색 알고리즘이 지수적 시간이 필요할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 대조 학습은 데이터 표현을 발견하기 위한 강력한 기법으로, 대조 정보에 기반한 목표를 최적화하여 의미 있는 데이터 표현을 찾는다.
- 2. 대조 목표의 전역 최적해를 찾는 것은 NP-난해하지만, 지역 최적해를 찾는 복잡성은 미해결 상태였다.
- 3. 본 연구는 다양한 대조 학습 문제에서 지역 최적해를 찾는 복잡성을 PLS-난해성과 CLS-난해성을 통해 규명하였다.
- 4. PLS 및 CLS는 각각 이산 및 연속 최적화에서 지역 탐색 동태를 포착하는 복잡성 클래스이다.
- 5. 연구 결과는 다양한 대조 학습 문제에서 다항 시간 알고리즘으로 지역 최적해를 찾는 것이 불가능함을 시사한다.


---

*Generated on 2025-09-24 01:44:38*