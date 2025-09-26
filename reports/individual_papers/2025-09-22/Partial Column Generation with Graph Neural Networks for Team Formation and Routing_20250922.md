---
keywords:
  - Graph Neural Network
  - Team Formation and Routing Problem
  - Column Generation
  - Partial Column Generation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15275
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:52:34.889674",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Team Formation and Routing Problem",
    "Column Generation",
    "Partial Column Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Team Formation and Routing Problem": 0.8,
    "Column Generation": 0.72,
    "Partial Column Generation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the proposed solution, providing a strong link to existing research on neural networks and optimization.",
        "novelty_score": 0.35,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Team Formation and Routing Problem",
        "canonical": "Team Formation and Routing Problem",
        "aliases": [
          "Team Routing Problem"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific optimization problem addressed by the paper, providing a unique link to specialized literature.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Column Generation",
        "canonical": "Column Generation",
        "aliases": [
          "Column Generation Method"
        ],
        "category": "broad_technical",
        "rationale": "Column generation is a well-known optimization technique, connecting the paper to a broad range of optimization research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Partial Column Generation",
        "canonical": "Partial Column Generation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel strategy in partial column generation, offering a unique contribution to the field.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "optimization problem",
      "solution method",
      "computational experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Team Formation and Routing Problem",
      "resolved_canonical": "Team Formation and Routing Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Column Generation",
      "resolved_canonical": "Column Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Partial Column Generation",
      "resolved_canonical": "Partial Column Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Partial Column Generation with Graph Neural Networks for Team Formation and Routing

**Korean Title:** 부분 열 생성 및 그래프 신경망을 활용한 팀 구성 및 경로 설정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15275.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15275](https://arxiv.org/abs/2509.15275)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.5% similar)
- [[2025-09-22/Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems_20250922|Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems]] (79.6% similar)
- [[2025-09-18/Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (78.6% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (78.4% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Column Generation|Column Generation]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Team Formation and Routing Problem|Team Formation and Routing Problem]], [[keywords/Partial Column Generation|Partial Column Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15275v1 Announce Type: cross 
Abstract: The team formation and routing problem is a challenging optimization problem with several real-world applications in fields such as airport, healthcare, and maintenance operations. To solve this problem, exact solution methods based on column generation have been proposed in the literature. In this paper, we propose a novel partial column generation strategy for settings with multiple pricing problems, based on predicting which ones are likely to yield columns with a negative reduced cost. We develop a machine learning model tailored to the team formation and routing problem that leverages graph neural networks for these predictions. Computational experiments demonstrate that applying our strategy enhances the solution method and outperforms traditional partial column generation approaches from the literature, particularly on hard instances solved under a tight time limit.

## 🔍 Abstract (한글 번역)

arXiv:2509.15275v1 발표 유형: 교차  
초록: 팀 구성 및 경로 설정 문제는 공항, 의료, 유지보수 작업 등 여러 실제 응용 분야에서 도전적인 최적화 문제입니다. 이 문제를 해결하기 위해 문헌에서는 컬럼 생성에 기반한 정확한 해결 방법이 제안되었습니다. 본 논문에서는 여러 가격 책정 문제를 가진 환경에서 부정적인 감소 비용을 가진 컬럼을 생성할 가능성이 높은 문제를 예측하는 새로운 부분 컬럼 생성 전략을 제안합니다. 우리는 팀 구성 및 경로 설정 문제에 맞춘 기계 학습 모델을 개발하였으며, 이러한 예측을 위해 그래프 신경망을 활용합니다. 계산 실험 결과, 우리의 전략을 적용함으로써 해결 방법이 향상되었고, 특히 제한된 시간 내에 해결되는 어려운 사례에서 문헌의 전통적인 부분 컬럼 생성 접근법을 능가함을 보여줍니다.

## 📝 요약

이 논문은 팀 구성 및 경로 최적화 문제를 다루며, 공항, 의료, 유지보수 등 다양한 분야에 적용될 수 있는 문제를 해결하기 위한 새로운 방법론을 제안합니다. 기존의 열 생성 기반 정확한 해법 대신, 다중 가격 문제 상황에서 부정 감소 비용을 예측하여 부분 열 생성 전략을 제안합니다. 이를 위해 그래프 신경망을 활용한 기계 학습 모델을 개발하였습니다. 실험 결과, 제안된 전략이 기존 방법보다 특히 제한된 시간 내에 어려운 사례를 해결하는 데 있어 더 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 팀 구성 및 라우팅 문제는 공항, 의료, 유지보수 등 여러 분야에서 중요한 최적화 문제이다.
- 2. 본 논문에서는 다중 가격 문제 환경에서 부분 열 생성 전략을 제안한다.
- 3. 그래프 신경망을 활용한 기계 학습 모델을 개발하여 열의 음의 감소 비용을 예측한다.
- 4. 제안된 전략은 기존의 부분 열 생성 접근법보다 성능이 우수하며, 특히 제한된 시간 내에 해결해야 하는 어려운 사례에서 효과적이다.


---

*Generated on 2025-09-23 08:52:34*