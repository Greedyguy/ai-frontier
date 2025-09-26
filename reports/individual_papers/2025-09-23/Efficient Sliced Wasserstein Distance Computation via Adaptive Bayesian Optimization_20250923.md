---
keywords:
  - Sliced Wasserstein Distance
  - Bayesian Optimization
  - Quasi-Monte Carlo
  - Gradient Flows
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17405
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:52:45.254177",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sliced Wasserstein Distance",
    "Bayesian Optimization",
    "Quasi-Monte Carlo",
    "Gradient Flows"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sliced Wasserstein Distance": 0.8,
    "Bayesian Optimization": 0.75,
    "Quasi-Monte Carlo": 0.7,
    "Gradient Flows": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sliced Wasserstein Distance",
        "canonical": "Sliced Wasserstein Distance",
        "aliases": [
          "SW"
        ],
        "category": "unique_technical",
        "rationale": "A specific distance metric used in optimal transport, relevant for linking to topics in geometry and generative modeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Bayesian Optimization",
        "canonical": "Bayesian Optimization",
        "aliases": [
          "BO"
        ],
        "category": "broad_technical",
        "rationale": "A widely applicable optimization technique, useful for linking to various machine learning and optimization contexts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Quasi-Monte Carlo",
        "canonical": "Quasi-Monte Carlo",
        "aliases": [
          "QMC"
        ],
        "category": "specific_connectable",
        "rationale": "A method for numerical integration, relevant for linking to computational mathematics and simulation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Gradient Flows",
        "canonical": "Gradient Flows",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A concept in optimization and differential equations, useful for linking to mathematical modeling and analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "Sliced Wasserstein Distance",
      "resolved_canonical": "Sliced Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Bayesian Optimization",
      "resolved_canonical": "Bayesian Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Quasi-Monte Carlo",
      "resolved_canonical": "Quasi-Monte Carlo",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Gradient Flows",
      "resolved_canonical": "Gradient Flows",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Efficient Sliced Wasserstein Distance Computation via Adaptive Bayesian Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17405.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17405](https://arxiv.org/abs/2509.17405)

## 🔗 유사한 논문
- [[2025-09-23/Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs_20250923|Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs]] (83.5% similar)
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (82.2% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.4% similar)
- [[2025-09-17/A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations: Unifying Stochastic Mirror Descent, Learning and LLM Training]] (80.3% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Optimization|Bayesian Optimization]]
**🔗 Specific Connectable**: [[keywords/Quasi-Monte Carlo|Quasi-Monte Carlo]], [[keywords/Gradient Flows|Gradient Flows]]
**⚡ Unique Technical**: [[keywords/Sliced Wasserstein Distance|Sliced Wasserstein Distance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17405v1 Announce Type: new 
Abstract: The sliced Wasserstein distance (SW) reduces optimal transport on $\mathbb{R}^d$ to a sum of one-dimensional projections, and thanks to this efficiency, it is widely used in geometry, generative modeling, and registration tasks. Recent work shows that quasi-Monte Carlo constructions for computing SW (QSW) yield direction sets with excellent approximation error. This paper presents an alternate, novel approach: learning directions with Bayesian optimization (BO), particularly in settings where SW appears inside an optimization loop (e.g., gradient flows). We introduce a family of drop-in selectors for projection directions: BOSW, a one-shot BO scheme on the unit sphere; RBOSW, a periodic-refresh variant; ABOSW, an adaptive hybrid that seeds from competitive QSW sets and performs a few lightweight BO refinements; and ARBOSW, a restarted hybrid that periodically relearns directions during optimization. Our BO approaches can be composed with QSW and its variants (demonstrated by ABOSW/ARBOSW) and require no changes to downstream losses or gradients. We provide numerical experiments where our methods achieve state-of-the-art performance, and on the experimental suite of the original QSW paper, we find that ABOSW and ARBOSW can achieve convergence comparable to the best QSW variants with modest runtime overhead.

## 📝 요약

이 논문은 슬라이스드 와서슈타인 거리(SW)를 최적화 루프 내에서 사용할 때 방향을 학습하는 새로운 방법으로 베이지안 최적화(BO)를 제안합니다. 기존의 준-몬테카를로(QSW) 방법이 아닌, BO를 활용하여 투영 방향을 선택하는 BOSW, RBOSW, ABOSW, ARBOSW 등의 방법론을 소개합니다. 이 방법들은 QSW와 결합 가능하며, 추가적인 손실 함수나 그래디언트 변경이 필요 없습니다. 실험 결과, 제안된 방법들이 최첨단 성능을 달성하며, 특히 ABOSW와 ARBOSW는 기존 QSW 변형들과 유사한 수렴 성능을 보이면서도 실행 시간 오버헤드는 적습니다.

## 🎯 주요 포인트

- 1. Sliced Wasserstein 거리(SW)는 최적 수송 문제를 1차원 투영의 합으로 줄여 효율성을 높이며, 기하학, 생성 모델링, 등록 작업 등에 널리 사용된다.
- 2. 본 논문은 SW를 최적화 루프 내에서 사용할 때 방향을 학습하는 새로운 접근법으로 베이지안 최적화(BO)를 제안한다.
- 3. BOSW, RBOSW, ABOSW, ARBOSW와 같은 다양한 투영 방향 선택자를 도입하여 SW 계산의 효율성을 높인다.
- 4. 제안된 BO 접근법은 QSW 및 그 변형과 결합 가능하며, 하위 손실이나 기울기에 대한 변경이 필요 없다.
- 5. 실험 결과, 제안된 방법들이 최첨단 성능을 달성하며, ABOSW와 ARBOSW는 적은 실행 시간 오버헤드로 QSW 변형과 유사한 수렴 성능을 보인다.


---

*Generated on 2025-09-24 01:52:45*