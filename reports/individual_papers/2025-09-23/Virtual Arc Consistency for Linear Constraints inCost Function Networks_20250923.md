---
keywords:
  - Constraint Programming
  - Soft Arc Consistency
  - Linear Constraints
  - Local Cost Functions
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17706
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:02:50.766811",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Constraint Programming",
    "Soft Arc Consistency",
    "Linear Constraints",
    "Local Cost Functions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Constraint Programming": 0.78,
    "Soft Arc Consistency": 0.82,
    "Linear Constraints": 0.79,
    "Local Cost Functions": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Constraint Programming",
        "canonical": "Constraint Programming",
        "aliases": [
          "CP"
        ],
        "category": "broad_technical",
        "rationale": "Constraint Programming is a foundational concept in optimization and problem-solving, linking to various computational methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Soft Arc Consistency",
        "canonical": "Soft Arc Consistency",
        "aliases": [
          "SAC"
        ],
        "category": "unique_technical",
        "rationale": "Soft Arc Consistency is a specialized algorithmic approach that enhances constraint satisfaction problems, relevant for linking advanced techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Linear Constraints",
        "canonical": "Linear Constraints",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Linear Constraints are integral to optimization problems and connect to various mathematical modeling techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Local Cost Functions",
        "canonical": "Local Cost Functions",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Local Cost Functions offer a nuanced approach to optimization, enhancing the expressiveness of constraint models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "minimization problems",
      "variable domains",
      "solving time"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Constraint Programming",
      "resolved_canonical": "Constraint Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Soft Arc Consistency",
      "resolved_canonical": "Soft Arc Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Linear Constraints",
      "resolved_canonical": "Linear Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Local Cost Functions",
      "resolved_canonical": "Local Cost Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Virtual Arc Consistency for Linear Constraints inCost Function Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17706.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17706](https://arxiv.org/abs/2509.17706)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.6% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.7% similar)
- [[2025-09-22/HyP-ASO_ A Hybrid Policy-based Adaptive Search Optimization Framework for Large-Scale Integer Linear Programs_20250922|HyP-ASO: A Hybrid Policy-based Adaptive Search Optimization Framework for Large-Scale Integer Linear Programs]] (79.6% similar)
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (79.4% similar)
- [[2025-09-22/Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems_20250922|Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Constraint Programming|Constraint Programming]]
**🔗 Specific Connectable**: [[keywords/Linear Constraints|Linear Constraints]]
**⚡ Unique Technical**: [[keywords/Soft Arc Consistency|Soft Arc Consistency]], [[keywords/Local Cost Functions|Local Cost Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17706v1 Announce Type: new 
Abstract: In Constraint Programming, solving discrete minimization problems with hard and soft constraints can be done either using (i) soft global constraints, (ii) a reformulation into a linear program, or (iii) a reformulation into local cost functions. Approach (i) benefits from a vast catalog of constraints. Each soft constraint propagator communicates with other soft constraints only through the variable domains, resulting in weak lower bounds. Conversely, the approach (ii) provides a global view with strong bounds, but the size of the reformulation can be problematic. We focus on approach (iii) in which soft arc consistency (SAC) algorithms produce bounds of intermediate quality. Recently, the introduction of linear constraints as local cost functions increases their modeling expressiveness. We adapt an existing SAC algorithm to handle linear constraints. We show that our algorithm significantly improves the lower bounds compared to the original algorithm on several benchmarks, reducing solving time in some cases.

## 📝 요약

이 논문은 제약 프로그래밍에서의 이산 최소화 문제 해결 방법을 다룹니다. 기존의 세 가지 접근법 중, 저자들은 지역 비용 함수로의 재구성(iii)에 중점을 두었습니다. 이 접근법은 중간 품질의 경계를 제공하며, 최근에는 선형 제약을 지역 비용 함수로 도입하여 모델링 표현력을 높였습니다. 저자들은 기존의 소프트 아크 일관성(SAC) 알고리즘을 선형 제약에 맞게 수정하였고, 이를 통해 여러 벤치마크에서 원래 알고리즘보다 더 나은 하한을 제공하여 해결 시간을 단축시켰음을 보였습니다.

## 🎯 주요 포인트

- 1. 제약 프로그래밍에서 하드 및 소프트 제약 조건을 포함한 이산 최소화 문제 해결 방법에는 소프트 글로벌 제약, 선형 프로그램으로의 재구성, 지역 비용 함수로의 재구성이 있다.
- 2. 소프트 글로벌 제약은 다양한 제약 조건 카탈로그를 활용하지만 약한 하한을 제공한다.
- 3. 선형 프로그램으로의 재구성은 강력한 하한을 제공하지만, 재구성의 크기가 문제가 될 수 있다.
- 4. 지역 비용 함수 접근법에서는 소프트 아크 일관성(SAC) 알고리즘이 중간 품질의 하한을 제공한다.
- 5. 본 연구에서는 선형 제약을 지역 비용 함수로 처리하는 SAC 알고리즘을 개선하여 여러 벤치마크에서 하한을 크게 개선하고 해결 시간을 단축시켰다.


---

*Generated on 2025-09-23 23:02:50*