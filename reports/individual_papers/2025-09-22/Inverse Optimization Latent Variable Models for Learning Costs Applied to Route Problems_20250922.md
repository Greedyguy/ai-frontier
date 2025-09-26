---
keywords:
  - Inverse Optimization Latent Variable Model
  - Fenchel-Young loss
  - Constrained Optimization Problems
  - Inverse Reinforcement Learning
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15999
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:39:54.907746",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Inverse Optimization Latent Variable Model",
    "Fenchel-Young loss",
    "Constrained Optimization Problems",
    "Inverse Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Inverse Optimization Latent Variable Model": 0.78,
    "Fenchel-Young loss": 0.75,
    "Constrained Optimization Problems": 0.7,
    "Inverse Reinforcement Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Inverse Optimization Latent Variable Model",
        "canonical": "Inverse Optimization Latent Variable Model",
        "aliases": [
          "IO-LVM"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper's methodology and offers a novel approach to learning cost functions, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fenchel-Young loss",
        "canonical": "Fenchel-Young loss",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This loss function is crucial for shaping the latent space in the proposed model, providing a specific point of connection for optimization techniques.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.75
      },
      {
        "surface": "Constrained Optimization Problems",
        "canonical": "Constrained Optimization Problems",
        "aliases": [
          "COPs"
        ],
        "category": "broad_technical",
        "rationale": "Understanding COPs is essential for contextualizing the paper's focus on optimization with unknown cost functions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.84,
        "specificity_score": 0.67,
        "link_intent_score": 0.7
      },
      {
        "surface": "Inverse Reinforcement Learning",
        "canonical": "Inverse Reinforcement Learning",
        "aliases": [
          "IRL"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is contrasted with the proposed model, providing a point of comparison and connection to existing methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "solver",
      "training process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Inverse Optimization Latent Variable Model",
      "resolved_canonical": "Inverse Optimization Latent Variable Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fenchel-Young loss",
      "resolved_canonical": "Fenchel-Young loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Constrained Optimization Problems",
      "resolved_canonical": "Constrained Optimization Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.84,
        "specificity": 0.67,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Inverse Reinforcement Learning",
      "resolved_canonical": "Inverse Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems

**Korean Title:** 경로 문제에 적용된 비용 학습을 위한 역최적화 잠재 변수 모델

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15999.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15999](https://arxiv.org/abs/2509.15999)

## 🔗 유사한 논문
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (80.2% similar)
- [[2025-09-22/Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios_20250922|Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios]] (80.2% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (80.2% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.8% similar)
- [[2025-09-22/Partial Column Generation with Graph Neural Networks for Team Formation and Routing_20250922|Partial Column Generation with Graph Neural Networks for Team Formation and Routing]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Constrained Optimization Problems|Constrained Optimization Problems]]
**🔗 Specific Connectable**: [[keywords/Fenchel-Young loss|Fenchel-Young loss]], [[keywords/Inverse Reinforcement Learning|Inverse Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Inverse Optimization Latent Variable Model|Inverse Optimization Latent Variable Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15999v1 Announce Type: new 
Abstract: Learning representations for solutions of constrained optimization problems (COPs) with unknown cost functions is challenging, as models like (Variational) Autoencoders struggle to enforce constraints when decoding structured outputs. We propose an Inverse Optimization Latent Variable Model (IO-LVM) that learns a latent space of COP cost functions from observed solutions and reconstructs feasible outputs by solving a COP with a solver in the loop. Our approach leverages estimated gradients of a Fenchel-Young loss through a non-differentiable deterministic solver to shape the latent space. Unlike standard Inverse Optimization or Inverse Reinforcement Learning methods, which typically recover a single or context-specific cost function, IO-LVM captures a distribution over cost functions, enabling the identification of diverse solution behaviors arising from different agents or conditions not available during the training process. We validate our method on real-world datasets of ship and taxi routes, as well as paths in synthetic graphs, demonstrating its ability to reconstruct paths and cycles, predict their distributions, and yield interpretable latent representations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15999v1 발표 유형: 신규  
초록: 비용 함수가 알려지지 않은 제약 최적화 문제(COP)의 해를 위한 표현 학습은 도전적입니다. (변분) 오토인코더와 같은 모델은 구조화된 출력을 디코딩할 때 제약 조건을 적용하는 데 어려움을 겪습니다. 우리는 관찰된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, 루프 내에서 해석기를 사용하여 COP를 해결함으로써 실행 가능한 출력을 재구성하는 역최적화 잠재 변수 모델(IO-LVM)을 제안합니다. 우리의 접근법은 비분화 가능한 결정론적 해석기를 통해 펜첼-영 손실의 추정된 기울기를 활용하여 잠재 공간을 형성합니다. 표준 역최적화 또는 역강화학습 방법과 달리, 이는 일반적으로 단일 또는 특정 상황에 맞는 비용 함수를 복원하는 반면, IO-LVM은 비용 함수의 분포를 포착하여 훈련 과정에서 제공되지 않은 다양한 에이전트 또는 조건에서 발생하는 다양한 해의 행동을 식별할 수 있게 합니다. 우리는 선박 및 택시 경로의 실제 데이터셋과 합성 그래프의 경로에 대해 우리의 방법을 검증하여 경로와 사이클을 재구성하고, 그 분포를 예측하며, 해석 가능한 잠재 표현을 제공하는 능력을 입증합니다.

## 📝 요약

이 논문은 비용 함수가 알려지지 않은 제약 최적화 문제(COP)의 해를 위한 표현 학습을 다룹니다. 기존 모델들이 구조화된 출력에서 제약을 잘 적용하지 못하는 문제를 해결하기 위해, 저자들은 관찰된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, 루프 내에서 해석기를 사용하여 COP를 해결함으로써 적합한 출력을 재구성하는 '역최적화 잠재 변수 모델(IO-LVM)'을 제안합니다. 이 접근법은 Fenchel-Young 손실의 추정된 그래디언트를 비분화 결정론적 해석기를 통해 활용하여 잠재 공간을 형성합니다. 기존의 역최적화 또는 역강화학습 방법이 단일 또는 특정 상황에 맞는 비용 함수를 복원하는 것과 달리, IO-LVM은 다양한 비용 함수 분포를 포착하여 훈련 과정에서 제공되지 않은 다양한 에이전트나 조건에서 발생하는 다양한 해의 행동을 식별할 수 있습니다. 이 방법은 실제 선박 및 택시 경로 데이터셋과 합성 그래프 경로에서 검증되었으며, 경로와 사이클을 재구성하고 그 분포를 예측하며 해석 가능한 잠재 표현을 제공하는 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. IO-LVM은 관측된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, COP를 풀어 가능한 출력을 재구성합니다.
- 2. 비분화 가능한 결정론적 해석기를 통한 Fenchel-Young 손실의 추정된 그래디언트를 활용하여 잠재 공간을 형성합니다.
- 3. IO-LVM은 단일 또는 특정 상황의 비용 함수를 복원하는 기존 방법과 달리, 다양한 에이전트나 조건에서 발생하는 다양한 솔루션 행동을 식별할 수 있는 비용 함수의 분포를 포착합니다.
- 4. 실제 데이터셋(선박 및 택시 경로)과 합성 그래프 경로에서 IO-LVM의 성능을 검증하여 경로와 사이클을 재구성하고, 그 분포를 예측하며 해석 가능한 잠재 표현을 제공합니다.


---

*Generated on 2025-09-23 10:39:54*