---
keywords:
  - Machine Learning
  - Interference Graph
  - Graph Coloring
  - Gradient Interference
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16959
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:38:55.239114",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Interference Graph",
    "Graph Coloring",
    "Gradient Interference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.72,
    "Interference Graph": 0.78,
    "Graph Coloring": 0.8,
    "Gradient Interference": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-task learning",
        "canonical": "Machine Learning",
        "aliases": [
          "multitask learning"
        ],
        "category": "broad_technical",
        "rationale": "Multi-task learning is a key aspect of the paper and connects well with general machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "interference graph",
        "canonical": "Interference Graph",
        "aliases": [
          "conflict graph"
        ],
        "category": "unique_technical",
        "rationale": "The interference graph is a novel concept introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "graph-coloring",
        "canonical": "Graph Coloring",
        "aliases": [
          "coloring algorithm"
        ],
        "category": "specific_connectable",
        "rationale": "Graph coloring is a specific technique used in the paper, linking it to broader graph theory concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "gradient interference",
        "canonical": "Gradient Interference",
        "aliases": [
          "gradient conflict"
        ],
        "category": "unique_technical",
        "rationale": "Gradient interference is a unique technical term central to the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "scheduler",
      "mini-batch",
      "training step"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-task learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "interference graph",
      "resolved_canonical": "Interference Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "graph-coloring",
      "resolved_canonical": "Graph Coloring",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "gradient interference",
      "resolved_canonical": "Gradient Interference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Gradient Interference-Aware Graph Coloring for Multitask Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16959.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16959](https://arxiv.org/abs/2509.16959)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial Graph Fusion for Incomplete Multi-view Semi-supervised Learning with Tensorial Imputation_20250922|Adversarial Graph Fusion for Incomplete Multi-view Semi-supervised Learning with Tensorial Imputation]] (82.6% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.0% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (80.9% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (80.6% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Coloring|Graph Coloring]]
**⚡ Unique Technical**: [[keywords/Interference Graph|Interference Graph]], [[keywords/Gradient Interference|Gradient Interference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16959v1 Announce Type: cross 
Abstract: When different objectives conflict with each other in multi-task learning, gradients begin to interfere and slow convergence, thereby reducing the final model's performance. To address this, we introduce a scheduler that computes gradient interference, constructs an interference graph, and then applies greedy graph-coloring to partition tasks into groups that align well with each other. At each training step, only one group (color class) of tasks are activated. The grouping partition is constantly recomputed as task relationships evolve throughout training. By ensuring that each mini-batch contains only tasks that pull the model in the same direction, our method improves the effectiveness of any underlying multi-task learning optimizer without additional tuning. Since tasks within these groups will update in compatible directions, model performance will be improved rather than impeded. Empirical results on six different datasets show that this interference-aware graph-coloring approach consistently outperforms baselines and state-of-the-art multi-task optimizers.

## 📝 요약

이 논문은 다중 작업 학습에서 목표 간의 충돌로 인한 성능 저하 문제를 해결하기 위해 새로운 스케줄러를 제안합니다. 이 스케줄러는 그래디언트 간섭을 계산하고 간섭 그래프를 구성한 후, 탐욕적 그래프 색칠을 통해 작업을 잘 맞는 그룹으로 나눕니다. 각 훈련 단계에서는 한 그룹의 작업만 활성화되며, 이는 작업 관계가 변화함에 따라 지속적으로 재계산됩니다. 이 방법은 미니배치가 동일한 방향으로 모델을 이끌도록 하여 다중 작업 학습 최적화기의 효과를 향상시킵니다. 실험 결과, 이 간섭 인식 그래프 색칠 접근법은 여섯 개의 데이터셋에서 기존 방법과 최신 최적화 기법을 일관되게 능가했습니다.

## 🎯 주요 포인트

- 1. 다중 작업 학습에서 목표 간의 충돌로 인한 그래디언트 간섭 문제를 해결하기 위해 간섭 그래프를 구성하고 이를 기반으로 작업을 그룹화하는 스케줄러를 도입했습니다.
- 2. 각 훈련 단계에서는 한 그룹(색상 클래스)의 작업만 활성화되며, 작업 간의 관계가 진화함에 따라 그룹화가 지속적으로 재계산됩니다.
- 3. 제안된 방법은 미니 배치가 동일한 방향으로 모델을 이끌도록 하여, 추가 튜닝 없이도 다중 작업 학습 최적화기의 효과를 향상시킵니다.
- 4. 호환 가능한 방향으로 업데이트되는 그룹 내 작업 덕분에 모델 성능이 개선됩니다.
- 5. 여섯 개의 다양한 데이터셋에 대한 실험 결과, 이 간섭 인식 그래프 색칠 기법이 기존의 방법과 최신 다중 작업 최적화 기법보다 일관되게 우수한 성능을 보였습니다.


---

*Generated on 2025-09-23 23:38:55*