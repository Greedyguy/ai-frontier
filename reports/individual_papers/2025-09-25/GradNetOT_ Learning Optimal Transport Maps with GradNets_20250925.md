---
keywords:
  - Optimal Transport
  - Monge-Ampère Equation
  - Monotone Gradient Networks
  - Neural Network
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2507.13191
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:09:25.403329",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Optimal Transport",
    "Monge-Ampère Equation",
    "Monotone Gradient Networks",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Optimal Transport": 0.85,
    "Monge-Ampère Equation": 0.8,
    "Monotone Gradient Networks": 0.88,
    "Neural Network": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [
          "OT"
        ],
        "category": "unique_technical",
        "rationale": "Optimal Transport is central to the paper's focus and connects to various applications in computational mathematics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Monge-Ampère equation",
        "canonical": "Monge-Ampère Equation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Monge-Ampère equation is crucial for understanding the mathematical foundation of the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monotone Gradient Networks",
        "canonical": "Monotone Gradient Networks",
        "aliases": [
          "mGradNets"
        ],
        "category": "unique_technical",
        "rationale": "Monotone Gradient Networks are a novel approach introduced by the authors, central to their method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are a fundamental technology underlying the proposed method, connecting it to a broad field of research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Monge-Ampère equation",
      "resolved_canonical": "Monge-Ampère Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monotone Gradient Networks",
      "resolved_canonical": "Monotone Gradient Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GradNetOT: Learning Optimal Transport Maps with GradNets

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.13191.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2507.13191](https://arxiv.org/abs/2507.13191)

## 🔗 유사한 논문
- [[2025-09-23/HOTA_ Hamiltonian framework for Optimal Transport Advection_20250923|HOTA: Hamiltonian framework for Optimal Transport Advection]] (85.4% similar)
- [[2025-09-24/Neighbor Embeddings Using Unbalanced Optimal Transport Metrics_20250924|Neighbor Embeddings Using Unbalanced Optimal Transport Metrics]] (82.4% similar)
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (81.9% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.3% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Optimal Transport|Optimal Transport]], [[keywords/Monge-Ampère Equation|Monge-Ampère Equation]], [[keywords/Monotone Gradient Networks|Monotone Gradient Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.13191v2 Announce Type: replace 
Abstract: Monotone gradient functions play a central role in solving the Monge formulation of the optimal transport (OT) problem, which arises in modern applications ranging from fluid dynamics to robot swarm control. When the transport cost is the squared Euclidean distance, Brenier's theorem guarantees that the unique optimal transport map satisfies a Monge-Amp\`ere equation and is the gradient of a convex function. In [arXiv:2301.10862] [arXiv:2404.07361], we proposed Monotone Gradient Networks (mGradNets), neural networks that directly parameterize the space of monotone gradient maps. In this work, we leverage mGradNets to directly learn the optimal transport mapping by minimizing a training loss function defined using the Monge-Amp\`ere equation. We empirically show that the structural bias of mGradNets facilitates the learning of optimal transport maps across both image morphing tasks and high-dimensional OT problems.

## 📝 요약

이 논문은 최적 수송 문제의 Monge 형식을 해결하는 데 중요한 역할을 하는 단조 기울기 함수에 관한 연구입니다. 특히, 수송 비용이 유클리드 거리의 제곱일 때, Brenier의 정리에 따라 최적 수송 맵이 Monge-Ampère 방정식을 만족하고 볼록 함수의 기울기임을 보장합니다. 저자들은 Monotone Gradient Networks(mGradNets)라는 신경망을 제안하여 단조 기울기 맵의 공간을 직접 매개변수화하였습니다. 본 연구에서는 mGradNets를 활용하여 Monge-Ampère 방정식을 이용한 손실 함수를 최소화함으로써 최적 수송 맵을 학습합니다. 실험 결과, mGradNets의 구조적 편향이 이미지 변형 및 고차원 최적 수송 문제에서 최적 수송 맵 학습을 촉진함을 입증하였습니다.

## 🎯 주요 포인트

- 1. 단조 그라디언트 함수는 최적 수송 문제의 Monge 공식화를 해결하는 데 핵심적인 역할을 한다.
- 2. Brenier의 정리에 따르면, 수송 비용이 제곱 유클리드 거리일 때, 최적 수송 맵은 Monge-Ampère 방정식을 만족하고 볼록 함수의 그라디언트이다.
- 3. Monotone Gradient Networks (mGradNets)는 단조 그라디언트 맵의 공간을 직접 매개변수화하는 신경망으로 제안되었다.
- 4. mGradNets를 활용하여 Monge-Ampère 방정식을 사용한 손실 함수를 최소화함으로써 최적 수송 맵을 직접 학습할 수 있다.
- 5. mGradNets의 구조적 편향은 이미지 변형 작업과 고차원 최적 수송 문제에서 최적 수송 맵 학습을 용이하게 한다.


---

*Generated on 2025-09-25 17:09:25*